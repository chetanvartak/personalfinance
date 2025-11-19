from datetime import date, datetime
from typing import List, Optional

from sqlalchemy import asc, desc
from app.schemas.merchant import MerchantCreate
from app.models.merchant import Merchant, MerchantDescription
from sqlalchemy.orm import joinedload

class MerchantRepository:
    def __init__(self, db):
        self.db = db


    def list_all(self):
        return self.db.query(Merchant).options(
            joinedload(Merchant.default_account),
            joinedload(Merchant.default_category),
            joinedload(Merchant.descriptions)
        ).all()

    def get(self, merchant_id: int):
        return self.db.query(Merchant).options(
            joinedload(Merchant.default_account),
            joinedload(Merchant.default_category),
            joinedload(Merchant.descriptions)
        ).filter(Merchant.id == merchant_id).one_or_none()

    def create(self, merchant_create):
        merchant = Merchant(
            merchant_name=merchant_create.merchant_name,
            default_category_id=merchant_create.default_category_id,
            default_account_id=merchant_create.default_account_id,
        )

        # Add any provided descriptions
        for d in (merchant_create.descriptions or []):
            # d may be a pydantic model or dict-like
            if isinstance(d, dict):
                desc_text = d.get("description")
            else:
                desc_text = getattr(d, "description", None)
            if desc_text:
                merchant.descriptions.append(MerchantDescription(description=desc_text))

        self.db.add(merchant)
        self.db.commit()
        self.db.refresh(merchant)
        return merchant

    def bulk_create(self, merchants_to_create: List[MerchantCreate]) -> List[Merchant]:
        """
        Creates multiple merchants in a single database session.

        Args:
            merchants_to_create: A list of merchant creation schemas.

        Returns:
            A list of the created merchant objects.
        """
        merchants = []
        for merchant_schema in merchants_to_create:
            m = Merchant(
                merchant_name=merchant_schema.merchant_name,
                default_category_id=merchant_schema.default_category_id,
                default_account_id=merchant_schema.default_account_id,
            )
            for d in (merchant_schema.descriptions or []):
                if isinstance(d, dict):
                    desc_text = d.get("description")
                else:
                    desc_text = getattr(d, "description", None)
                if desc_text:
                    m.descriptions.append(MerchantDescription(description=desc_text))
            merchants.append(m)
        # Add each merchant individually

        self.db.add_all(merchants)
        
        self.db.commit()
        # Note: self.db.refresh() does not work on a list.
        # The objects in the 'merchants' list are updated with IDs by SQLAlchemy.
        return merchants

    def update(self, merchant: Merchant, updates: dict):
        for key, value in updates.items():
            if hasattr(merchant, key) and value is not None:
                setattr(merchant, key, value)
        # Handle nested descriptions if provided
        if "descriptions" in updates:
            # Replace existing descriptions with provided list
            merchant.descriptions[:] = []
            for d in updates.get("descriptions") or []:
                desc_text = d.get("description") if isinstance(d, dict) else getattr(d, "description", None)
                if desc_text:
                    merchant.descriptions.append(MerchantDescription(description=desc_text))

        self.db.add(merchant)
        self.db.commit()
        self.db.refresh(merchant)
        return merchant
    def search(
        self,
        start_date: datetime,
        end_date: datetime,
        account_ids: Optional[List[int]] = None,
        category_ids: Optional[List[int]] = None,
        description: Optional[str] = None,
    ):
        """
        Searches for transactions based on the given criteria.

        Args:
            start_date: The start of the date range (inclusive).
            end_date: The end of the date range (inclusive).
            account_ids: An optional list of account IDs to filter by.
            category_ids: An optional list of category IDs to filter by.
            description: An optional description pattern to filter by (case-insensitive).

        Returns:
            A list of transactions matching the criteria.
        """
        query = self.db.query(Merchant)

        # 2. Optional Account IDs
        if account_ids:
            query = query.filter(Merchant.default_account_id.in_(account_ids))

        # 3. Optional Description (ILIKE comparison)
        if description:
            query = query.filter(Merchant.merchant_name.ilike(f"%{description}%"))
        # 4. Optional Category IDs
        if category_ids:
            query = query.filter(Merchant.default_category_id.in_(category_ids))

        return query.options(
            joinedload(Merchant.default_account),
            joinedload(Merchant.default_category),
            joinedload(Merchant.descriptions)
        ).all()

    def delete(self, tx: Merchant):
        self.db.delete(tx)
        self.db.commit()
        return None

    def list_filtered_merchants(self, page: int, page_size: int, sort_by: str, sort_order: str, search: Optional[str] = None, account_id: Optional[int] = None, category_id: Optional[int] = None, date_from: Optional[datetime] = None, date_to: Optional[datetime] = None):
        query = self.db.query(Merchant).options(
            joinedload(Merchant.default_account),
            joinedload(Merchant.default_category)
        )

        # Filtering
        if search:
            query = query.filter(Merchant.merchant_name.ilike(f"%{search}%"))
        if account_id:
            query = query.filter(Merchant.default_account_id == account_id)
        if category_id:
            query = query.filter(Merchant.default_category_id == category_id)
        if date_from:
            query = query.filter(Merchant.created_at >= date_from)
        if date_to:
            query = query.filter(Merchant.created_at <= date_to)

        # Sorting
        sort_column = getattr(Merchant, sort_by)
        if sort_order == "desc":
            query = query.order_by(desc(sort_column))
        else:
            query = query.order_by(asc(sort_column))

        total = query.count()
        items = query.offset((page - 1) * page_size).limit(page_size).all()
        return {
            "merchants": items,
            "total": total,
            "page": page,
            "page_size": page_size
        }