"""Sample blog content for V1.

Seeding is idempotent (keyed on slug), so it is safe to run repeatedly. This
stands in for a future content-management module — the shape here matches what
an admin panel would eventually write.
"""

from datetime import UTC, datetime, timedelta

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.blog.models import Blog

_NOW = datetime(2026, 8, 1, tzinfo=UTC)


def _body(*paragraphs: str) -> str:
    return "\n\n".join(paragraphs)


SEED_BLOGS: list[dict] = [
    {
        "slug": "reading-bitcoin-dominance-in-2026",
        "title": "Reading Bitcoin Dominance in 2026",
        "excerpt": "BTC dominance is one of the most misread metrics in crypto. Here is a "
        "framework for using it as a market-structure signal rather than a headline.",
        "category": "markets",
        "author": "Elena Report",
        "reading_time_minutes": 6,
        "cover_image_url": "https://images.unsplash.com/photo-1518546305927-5a555bb7020d?w=1200&q=80",
        "published_at": _NOW,
        "content": _body(
            "Bitcoin dominance measures BTC's share of the total crypto market "
            "capitalization. On its own it is neither bullish nor bearish — it is a "
            "ratio, and ratios move for two different reasons.",
            "When dominance rises in a falling market, capital is rotating toward "
            "relative safety. When it rises in a rising market, Bitcoin is leading and "
            "altcoins have not yet caught the bid. Distinguishing between the two is the "
            "entire skill.",
            "The practical takeaway: never read dominance without also reading total "
            "market cap. The pair together tells you whether risk appetite is expanding "
            "or contracting, which is the question that actually matters.",
        ),
    },
    {
        "slug": "what-defi-got-right",
        "title": "What DeFi Got Right (and What It Still Hasn't)",
        "excerpt": "Composability was the breakthrough. Risk management was the blind spot. "
        "A sober look at where decentralized finance actually delivered.",
        "category": "defi",
        "author": "Marcus Chen",
        "reading_time_minutes": 8,
        "cover_image_url": "https://images.unsplash.com/photo-1639762681485-074b7f938ba0?w=1200&q=80",
        "published_at": _NOW - timedelta(days=3),
        "content": _body(
            "Decentralized finance made one genuinely novel contribution: permissionless "
            "composability. Any protocol could build on any other without asking for "
            "access, and that unlocked a design space traditional finance simply cannot "
            "reach.",
            "The blind spot was systemic risk. Composability cuts both ways — the same "
            "connections that let liquidity flow freely also let failures cascade. Several "
            "of the largest DeFi collapses were not smart-contract bugs but risk "
            "concentration nobody was measuring.",
            "The next chapter of DeFi is less about new primitives and more about "
            "legibility: being able to see, price, and contain risk across a network of "
            "interdependent protocols.",
        ),
    },
    {
        "slug": "a-plain-language-guide-to-etfs",
        "title": "A Plain-Language Guide to Crypto ETFs",
        "excerpt": "Spot ETFs changed who can hold crypto and how. Here is what they are, "
        "how they work, and why the plumbing matters more than the headline.",
        "category": "insights",
        "author": "Priya Nair",
        "reading_time_minutes": 5,
        "cover_image_url": "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=1200&q=80",
        "published_at": _NOW - timedelta(days=6),
        "content": _body(
            "A spot crypto ETF holds the underlying asset and issues shares that trade on "
            "a traditional exchange. For most institutions, that wrapper is the difference "
            "between being able to allocate and not.",
            "The mechanics that matter are creation and redemption: authorized "
            "participants exchange baskets of the asset for shares, which keeps the ETF "
            "price tethered to the underlying. When that mechanism works smoothly, "
            "tracking error stays small.",
            "For a research platform, ETFs are worth watching because their flows are a "
            "clean, reported proxy for institutional demand — one of the few in a market "
            "that is otherwise hard to survey.",
        ),
    },
    {
        "slug": "regulation-is-not-one-thing",
        "title": "Regulation Is Not One Thing",
        "excerpt": "Custody, securities law, stablecoins, and taxation are separate regimes "
        "moving at different speeds. Treating them as a single story leads to bad calls.",
        "category": "regulation",
        "author": "Elena Report",
        "reading_time_minutes": 7,
        "cover_image_url": "https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=1200&q=80",
        "published_at": _NOW - timedelta(days=9),
        "content": _body(
            "The word 'regulation' collapses at least four distinct regimes into one: how "
            "assets are custodied, whether a token is a security, how stablecoins are "
            "backed and supervised, and how gains are taxed.",
            "These move independently and often in different directions. A jurisdiction "
            "can have clear stablecoin rules and deeply unsettled securities questions at "
            "the same time. Reading them as a single sentiment score is how analysts get "
            "surprised.",
            "The disciplined approach is to track each regime on its own timeline and ask "
            "which one actually governs the decision in front of you.",
        ),
    },
    {
        "slug": "ethereum-after-the-merge-era",
        "title": "Ethereum After the Merge Era",
        "excerpt": "Proof-of-stake settled the energy debate. The open questions now are "
        "about scaling economics and where value accrues in a rollup-centric world.",
        "category": "ethereum",
        "author": "Marcus Chen",
        "reading_time_minutes": 6,
        "cover_image_url": "https://images.unsplash.com/photo-1622630998477-20aa696ecb05?w=1200&q=80",
        "published_at": _NOW - timedelta(days=12),
        "content": _body(
            "The transition to proof-of-stake resolved Ethereum's most visible criticism — "
            "energy use — but it also reframed the harder questions around economics and "
            "scaling.",
            "In a rollup-centric roadmap, most activity moves to layer-2 networks that "
            "settle back to Ethereum. That raises a genuine open question: how much value "
            "accrues to the base layer versus the rollups built on top of it.",
            "For researchers, the metric to watch is not transaction count but fee "
            "capture — where users actually pay, and which layer keeps the revenue.",
        ),
    },
    {
        "slug": "market-structure-basics-liquidity",
        "title": "Market Structure Basics: Why Liquidity Is the Real Story",
        "excerpt": "Price gets the headlines, but liquidity determines whether that price "
        "means anything. A short primer on depth, spread, and slippage.",
        "category": "markets",
        "author": "Priya Nair",
        "reading_time_minutes": 5,
        "cover_image_url": "https://images.unsplash.com/photo-1642790551116-18e150f248e9?w=1200&q=80",
        "published_at": _NOW - timedelta(days=15),
        "content": _body(
            "A quoted price is only as meaningful as the liquidity behind it. In thin "
            "markets, a headline number can be moved by a single order, which is why "
            "depth matters as much as price.",
            "Three measures do most of the work: bid-ask spread tells you the cost of "
            "entry, order-book depth tells you how much you can trade before moving the "
            "market, and slippage tells you what a realistic fill looks like.",
            "For a market-intelligence platform, surfacing liquidity context alongside "
            "price is what separates a data feed from actual insight.",
        ),
    },
]


async def seed_blogs(db: AsyncSession) -> int:
    """Insert seed blogs that don't already exist. Returns count inserted."""
    existing = set((await db.execute(select(Blog.slug))).scalars().all())
    to_insert = [Blog(**data) for data in SEED_BLOGS if data["slug"] not in existing]
    if to_insert:
        db.add_all(to_insert)
        await db.commit()
    return len(to_insert)
