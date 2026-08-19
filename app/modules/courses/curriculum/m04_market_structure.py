"""Module 4 — How Crypto Markets Actually Work."""

from app.modules.courses.curriculum.spec import LessonSpec, ModuleSpec, homework
from app.modules.courses.models import CourseLevel, CoursePhase

MODULE = ModuleSpec(
    slug="how-markets-work",
    title="How Crypto Markets Actually Work",
    summary=(
        "Order books, liquidity, who you are trading against, and the derivatives machinery that "
        "drives most of the volatility you will experience."
    ),
    level=CourseLevel.BEGINNER,
    phase=CoursePhase.MARKET_MECHANICS,
    lessons=[
        LessonSpec(
            title="The order book",
            minutes=8,
            body=(
                "Price is not a number an exchange decides. It is the record of the last trade, "
                "and the next one will happen wherever a buyer and a seller agree. The order book "
                "is where that negotiation is visible.\n\n"
                "The book has two sides. Bids are resting buy orders, listed from the highest "
                "price down. Asks are resting sell orders, listed from the lowest price up. The "
                "highest bid and lowest ask are the top of the book, and the gap between them is "
                "the spread. Nothing trades inside that gap — for a trade to happen, someone has "
                "to accept the other side's price.\n\n"
                "That gives you the two ways to trade. Place a limit order at a price inside or "
                "beyond the spread and it rests on the book, waiting; you are a maker, and you may "
                "never be filled. Place a market order and you cross the spread immediately, "
                "consuming resting orders; you are a taker, filled instantly at whatever prices "
                "are available.\n\n"
                "That word 'prices', plural, is the part beginners miss. If you buy more than the "
                "size resting at the best ask, the remainder fills at the next level, and the "
                "next. Your average price is worse than the number you saw. In a deep book the "
                "difference is invisible; in a thin one it can be several percent.\n\n"
                "Two things the book will not tell you. Resting orders can be cancelled "
                "instantly, so a wall of size at some level is a statement of intent, not a "
                "commitment — and placing large orders with no intention of filling them, then "
                "pulling them, is a well-known manipulation. And the book shows only that "
                "exchange. Crypto has no consolidated tape; the same asset trades on dozens of "
                "venues at slightly different prices, which is why aggregated price feeds and the "
                "book you are actually trading against can disagree."
            ),
        ),
        LessonSpec(
            title="Liquidity and why it decides everything",
            minutes=8,
            body=(
                "Liquidity is the ability to trade size without moving the price. It is the single "
                "most under-appreciated variable in crypto, and it explains most of the "
                "difference between a comfortable position and a trap.\n\n"
                "Measure it three ways. The spread tells you the immediate cost of a round trip. "
                "Depth — how much size rests within, say, 0.5% of the mid price — tells you how "
                "large a trade the book can absorb. Daily volume tells you how much interest "
                "exists over time, though it can be inflated by wash trading on smaller venues.\n\n"
                "Why it matters more than it appears:\n\n"
                "- Your entry and exit costs scale with your size relative to depth. A position "
                "you can build over a week may be one you cannot exit in an hour.\n"
                "- Liquidity is not constant. It is thinnest exactly when you most want it — "
                "during sharp moves, market makers widen spreads or step away entirely, so the "
                "depth you measured on a calm afternoon is not the depth available during a "
                "crash.\n"
                "- Thin books make price manipulation cheap. A small-cap asset can be moved "
                "double digits by an amount that would not register on a major.\n\n"
                "The practical test before taking any position: could I exit this in a falling "
                "market without moving the price against myself? If the honest answer is no, the "
                "position is too large for that asset, regardless of how good the idea is.\n\n"
                "This is also why liquidity should be an explicit filter in your research, not an "
                "afterthought. Many people discover an interesting small-cap asset, size it like a "
                "major, and then find that the thesis was right and the exit was impossible."
            ),
        ),
        LessonSpec(
            title="Who you are trading against",
            minutes=8,
            body=(
                "Every trade has a counterparty, and it is worth knowing who tends to be on the "
                "other side of yours.\n\n"
                "Market makers quote both sides continuously, earning the spread and hedging their "
                "inventory. They are not directional opponents — they profit from flow, not from "
                "your being wrong — but they are faster than you and they widen or withdraw when "
                "volatility spikes.\n\n"
                "Arbitrageurs keep prices aligned across venues and between spot and derivatives. "
                "They are why an asset does not trade at meaningfully different prices on two "
                "exchanges for long, and why obvious mispricings you spot are usually stale "
                "data.\n\n"
                "Systematic and high-frequency funds trade on signals and latency. You will not "
                "outrun them, and any strategy whose edge is speed is not available to you.\n\n"
                "Large discretionary holders — 'whales' — move size that the book cannot absorb at "
                "once, so they work orders over time. Their footprints are visible on-chain, which "
                "Module 10 covers.\n\n"
                "Retail participants, who are mostly reacting to price and news, and who cluster "
                "their stop orders at obvious levels.\n\n"
                "Two conclusions follow. First, your edge cannot be speed or information you got "
                "from a public feed — both are already priced in by the time you read them. A "
                "realistic retail edge is patience: you have no mandate, no redemption pressure "
                "and no reporting period, so you can wait for setups that institutions cannot. "
                "Second, obvious levels are obvious to everyone. Clusters of stop orders just "
                "below an obvious support level are liquidity that larger participants can and do "
                "trade toward — which is why price so often pokes through a level, triggers the "
                "stops and reverses. That is not a conspiracy; it is simply where the orders are."
            ),
        ),
        LessonSpec(
            title="Spot, futures and perpetual swaps",
            minutes=9,
            body=(
                "Spot trading is buying the asset. You own it, you can withdraw it, and the worst "
                "case is that it goes to zero. Everything else in this lesson is a derivative: a "
                "contract whose value references the asset without conveying ownership.\n\n"
                "A futures contract is an agreement to settle a price difference at a date. "
                "Crypto's dominant instrument, though, is the perpetual swap — a futures contract "
                "with no expiry. That creates a problem: without a settlement date, what keeps its "
                "price tied to spot?\n\n"
                "The answer is the funding rate. Periodically — often every eight hours — one side "
                "pays the other. When the perpetual trades above spot, longs pay shorts, making it "
                "expensive to stay long and attracting sellers. When it trades below, shorts pay "
                "longs. It is a continuous tether pulling the contract back toward the underlying "
                "price.\n\n"
                "Funding is also one of the most useful sentiment gauges available, and it is free "
                "to read:\n\n"
                "- Persistently high positive funding means the market is crowded long and paying "
                "for the privilege. Crowded positioning is fragile positioning.\n"
                "- Deeply negative funding means crowded short, which sets up violent upside "
                "squeezes.\n"
                "- Funding near neutral means positioning is not stretched, and moves are more "
                "likely driven by spot demand.\n\n"
                "Even if you never trade derivatives, they matter to you. Perpetual volume "
                "regularly exceeds spot volume by a wide margin, so derivative positioning drives "
                "much of the short-term volatility in the price of the asset you hold. The "
                "cascading liquidations that produce sudden vertical moves are a derivatives "
                "phenomenon — the next lesson explains the mechanism."
            ),
        ),
        LessonSpec(
            title="Leverage, margin and liquidation",
            minutes=9,
            body=(
                "Leverage lets you control a position larger than your capital by posting a "
                "fraction of it as margin. It is the fastest way to lose money in this market, and "
                "understanding it is necessary even if you never use it — because other people's "
                "leverage will move prices you trade.\n\n"
                "The arithmetic is unsentimental. At 10x, a 10% move against you wipes out your "
                "margin. At 20x, 5% does it. Crypto routinely moves 5% in an hour. This is why the "
                "overwhelming majority of leveraged retail accounts lose money: not because the "
                "direction was wrong, but because the position could not survive normal noise "
                "before the direction resolved.\n\n"
                "Liquidation is the mechanism. When your margin falls below the maintenance "
                "requirement, the exchange closes your position automatically — not at your chosen "
                "exit, but at whatever the market offers. You do not get to wait for a recovery. "
                "In fast markets you may also be liquidated at a worse price than your liquidation "
                "level implies.\n\n"
                "Liquidations cluster, and that is the important part. Many participants use "
                "similar leverage around similar levels, so a move that triggers one wave of "
                "liquidations forces market sells, which pushes price further, which triggers the "
                "next wave. This is the mechanism behind the vertical candles that appear to come "
                "from nowhere. Liquidation heatmaps showing where leveraged positions sit are "
                "widely published, which tells you those clusters are visible to everyone — "
                "including participants able to trade toward them.\n\n"
                "If you use leverage at all, the discipline is: keep it low (2–3x), size the "
                "position by the distance to your invalidation rather than by what the platform "
                "offers, use isolated margin so one position cannot consume your whole account, "
                "and never add margin to defend a losing position. That last habit converts a "
                "manageable loss into an account-ending one more often than anything else."
            ),
        ),
        LessonSpec(
            title="Market cap, supply and dilution",
            minutes=8,
            body=(
                "Market capitalisation is price multiplied by circulating supply. It is the "
                "standard way to compare assets, and it is misread constantly.\n\n"
                "The first mistake is treating it as money invested. It is not. It is the last "
                "traded price extrapolated across every unit in existence, most of which are not "
                "for sale. A modest amount of buying can lift a thin asset's market cap by "
                "billions, and those billions cannot be realised.\n\n"
                "The second is ignoring the difference between circulating and total supply. "
                "Circulating supply is what is liquid today. Total supply includes tokens locked "
                "in vesting schedules for teams and investors. Fully diluted valuation uses the "
                "maximum supply, and the gap between market cap and FDV is a schedule of future "
                "selling. An asset with 10% of supply circulating and the rest unlocking over two "
                "years faces persistent structural sell pressure, no matter how good the "
                "technology is.\n\n"
                "So when you look at an asset, check:\n\n"
                "- Circulating supply as a percentage of total. Below about a third deserves "
                "caution.\n"
                "- The unlock schedule, and specifically the next large cliff. Prices frequently "
                "weaken into these.\n"
                "- Who holds the locked supply. Early investors at a fraction of the current price "
                "have very different incentives from you.\n"
                "- Whether supply is inflating, and at what rate. Emissions paid to stakers or "
                "liquidity providers are dilution.\n\n"
                "The useful mental exercise is to ask what has to be true for this asset's market "
                "cap to double, expressed in real-world terms — how much capital, from whom, for "
                "what reason. Doing it honestly disqualifies a lot of ideas quickly, which is "
                "exactly what a research process is for."
            ),
        ),
        LessonSpec(
            title="Volume, open interest and reading participation",
            minutes=8,
            body=(
                "Price tells you where the market is. Volume and open interest tell you how much "
                "conviction is behind it, which is often the more useful information.\n\n"
                "Volume is how much traded in a period. The principle worth remembering: moves on "
                "expanding volume reflect genuine participation, while moves on declining volume "
                "reflect a lack of opposition. A breakout on heavy volume has buyers behind it. "
                "The same breakout on thin volume more often fails, because nothing supports the "
                "new level.\n\n"
                "Open interest is derivatives-specific: the total value of contracts currently "
                "open. Unlike volume, it measures positions held rather than activity. Reading the "
                "two together is a genuinely useful skill:\n\n"
                "- Price up, open interest up: new longs entering. A trend with fuel, and also "
                "with a growing pile of liquidations beneath it.\n"
                "- Price up, open interest down: shorts closing. A squeeze, which often exhausts "
                "itself once the shorts are gone.\n"
                "- Price down, open interest up: new shorts. Genuine bearish conviction.\n"
                "- Price down, open interest down: longs capitulating or being liquidated — "
                "position unwinding rather than new selling, and often closer to a low than it "
                "feels.\n\n"
                "Two cautions. Reported volume on smaller venues can be fabricated, so prefer "
                "aggregated data from sources that filter, and prefer volume from venues you would "
                "actually trade on. And volume is relative: what matters is today's volume "
                "compared with this asset's own recent average, not against another asset.\n\n"
                "Nothing here is a signal on its own. Volume and open interest are context that "
                "make the price action in the next two modules interpretable."
            ),
        ),
        LessonSpec(
            title="A market that never closes",
            minutes=8,
            body=(
                "Crypto trades every hour of every day, which sounds like an advantage and is "
                "mostly a hazard. Traditional markets close, and that close forces a pause, caps "
                "the damage of a bad session and gives participants time to think. Crypto offers "
                "none of that.\n\n"
                "Structure still exists, though, and it is worth knowing:\n\n"
                "- Liquidity follows the working day. It is deepest when European and US hours "
                "overlap, and thinnest in the late US and weekend hours. Sharp moves "
                "disproportionately happen in thin liquidity, because it takes less size to move "
                "the price.\n"
                "- Weekends are quieter and more prone to outsized moves, and traditional markets "
                "are closed so hedging is harder.\n"
                "- Scheduled macro events — US inflation prints, central bank decisions — now move "
                "crypto substantially. Know when they are.\n"
                "- Derivatives settlement and funding times create recurring flow.\n\n"
                "The behavioural consequence matters more than any of these. A market with no "
                "close invites constant monitoring, and constant monitoring produces "
                "overtrading — reacting to noise, sizing by mood, and being awake for moves you "
                "have no plan for. The professionals in this market are not watching it "
                "continuously; they have defined times to review and defined orders that work "
                "while they sleep.\n\n"
                "Practical defence: pick a review schedule and keep to it. Use resting limit "
                "orders and alerts rather than watching. Decide in advance whether you will act on "
                "a 3 a.m. move — and if the honest answer is that you would not, turn the "
                "notification off. You cannot be at your best at all hours, and a market that "
                "never sleeps will find the hour when you are not."
            ),
        ),
        homework(
            title="Week 4 homework — read a real market",
            minutes=12,
            body=(
                "Observation only this week. No trades.\n\n"
                "1. Depth comparison.\n\n"
                "Open the order book for a top-five asset and for something outside the top two "
                "hundred. For each, record: the spread as a percentage of price, and roughly how "
                "much size rests within 0.5% of mid on each side. Then answer in writing: what is "
                "the largest position I could exit in the small-cap without moving the price more "
                "than 1%?\n\n"
                "2. Funding and open interest.\n\n"
                "Find current funding rates and open interest for the largest asset. Note whether "
                "funding is positive or negative and how it has changed over the past week. Write "
                "one sentence on what that implies about positioning.\n\n"
                "3. Supply check.\n\n"
                "Pick any asset outside the top twenty. Record its circulating supply, total "
                "supply, market cap and fully diluted valuation. Find its unlock schedule. Write "
                "one sentence on what dilution over the next twelve months would do to the price "
                "if demand stayed exactly constant.\n\n"
                "4. Volume observation.\n\n"
                "Over three days, note the daily volume of one asset alongside its price change. "
                "Mark each day as expanding or contracting volume. At the end, write one "
                "observation about whether the moves you saw had participation behind them.\n\n"
                "Keep all four in your notes file. Module 8 will ask you to reread them."
            ),
        ),
    ],
)
