"""Create (or promote) the bootstrap administrator account.

Usage:
    python -m scripts.create_admin                  # uses ADMIN_EMAIL / ADMIN_PASSWORD
    python -m scripts.create_admin a@b.com Secret1  # explicit credentials

Idempotent: running it again promotes the existing account to admin and resets
its password, which is also the escape hatch for a forgotten admin password.
"""

import asyncio
import sys

from app.core.config import get_settings
from app.core.database import SessionFactory
from app.modules.auth.models import User, UserRole
from app.modules.auth.repository import AuthRepository
from app.modules.auth.security import hash_password


async def create_admin(email: str, password: str, full_name: str = "Administrator") -> None:
    async with SessionFactory() as db:
        repo = AuthRepository(db)
        existing = await repo.get_user_by_email(email.lower())

        if existing is not None:
            existing.role = UserRole.ADMIN
            existing.password_hash = hash_password(password)
            existing.is_active = True
            await repo.save()
            print(f"Updated existing account to admin: {email}")
            return

        await repo.add_user(
            User(
                email=email.lower(),
                password_hash=hash_password(password),
                full_name=full_name,
                role=UserRole.ADMIN,
            )
        )
        print(f"Created admin account: {email}")


def main() -> None:
    settings = get_settings()
    if len(sys.argv) >= 3:
        email, password = sys.argv[1], sys.argv[2]
    else:
        email, password = settings.admin_email, settings.admin_password

    if not email or not password:
        sys.exit(
            "Set ADMIN_EMAIL and ADMIN_PASSWORD in .env, or pass them as arguments:\n"
            "  python -m scripts.create_admin admin@example.com StrongPass1"
        )

    asyncio.run(create_admin(email, password))


if __name__ == "__main__":
    main()
