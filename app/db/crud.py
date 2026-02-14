from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

# assuming the models are already imported from models module

async def create_user(session: AsyncSession, user_data: dict):
    new_user = User(**user_data)
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user

async def get_user(session: AsyncSession, user_id: int):
    result = await session.execute(select(User).where(User.id == user_id))
    return result.scalars().first()

async def update_user(session: AsyncSession, user_id: int, user_data: dict):
    user = await get_user(session, user_id)
    for key, value in user_data.items():
        setattr(user, key, value)
    await session.commit()
    await session.refresh(user)
    return user

async def delete_user(session: AsyncSession, user_id: int):
    user = await get_user(session, user_id)
    await session.delete(user)
    await session.commit()
    return user


async def create_apartment(session: AsyncSession, apartment_data: dict):
    new_apartment = Apartment(**apartment_data)
    session.add(new_apartment)
    await session.commit()
    await session.refresh(new_apartment)
    return new_apartment

async def get_apartment(session: AsyncSession, apartment_id: int):
    result = await session.execute(select(Apartment).where(Apartment.id == apartment_id))
    return result.scalars().first()

async def update_apartment(session: AsyncSession, apartment_id: int, apartment_data: dict):
    apartment = await get_apartment(session, apartment_id)
    for key, value in apartment_data.items():
        setattr(apartment, key, value)
    await session.commit()
    await session.refresh(apartment)
    return apartment

async def delete_apartment(session: AsyncSession, apartment_id: int):
    apartment = await get_apartment(session, apartment_id)
    await session.delete(apartment)
    await session.commit()
    return apartment


# Repeat the CRUD operations similarly for ApartmentMedia, ApartmentTag, Lead, Booking, ReferralCode, ReferralEvent, Payout, WebhookEvent, and ChannelPost

