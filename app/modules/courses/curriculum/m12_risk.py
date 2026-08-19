"""Module 12 — Risk Management & Position Sizing."""

from app.modules.courses.curriculum.spec import LessonSpec, ModuleSpec, homework
from app.modules.courses.models import CourseLevel, CoursePhase

MODULE = ModuleSpec(
    slug="risk-management",
    title="Risk Management & Position Sizing",
    summary=(
        "The module that decides whether everything else matters: drawdown arithmetic, sizing "
        "from invalidation, portfolio heat, correlation, and the limits you set before you need "
        "them."
    ),
    level=CourseLevel.INTERMEDIATE,
    phase=CoursePhase.RISK_AND_STRATEGY,
    lessons=[
        LessonSpec(
            title="The arithmetic of drawdown",
            minutes=8,
            body=(
                "Losses and gains are not symmetric, and the asymmetry gets worse the deeper you "
                "go. This is the most important arithmetic in investing, and it is worth "
                "committing to memory.\n\n"
                "To recover from a loss you need a larger percentage gain than the loss itself:\n\n"
                "- Down 10% requires +11% to recover.\n"
                "- Down 25% requires +33%.\n"
                "- Down 50% requires +100%.\n"
                "- Down 75% requires +300%.\n"
                "- Down 90% requires +900%.\n\n"
                "The curve is gentle until roughly 20% and then turns brutal. A 50% loss means you "
                "must double your remaining capital simply to return to where you started — which "
                "in most markets takes years, and in the meantime you are not compounding, you are "
                "repairing.\n\n"
                "Two consequences follow directly. First, capital preservation is not caution, it "
                "is mathematics: avoiding large drawdowns matters more to long-run returns than "
                "capturing large gains, because the recovery cost of a deep hole exceeds the "
                "opportunity cost of a missed rally. Second, the argument for cutting losses "
                "early is not about being right; it is that small losses live in the gentle part "
                "of the curve where recovery is realistic.\n\n"
                "There is also a psychological cliff that arrives before the mathematical one. "
                "Most people stop trading their plan somewhere around a 30% drawdown — they "
                "either freeze or start taking desperate positions to recover. So the practical "
                "limit is not where the maths becomes impossible but where you become unable to "
                "execute, and that is considerably shallower.\n\n"
                "Everything in this module follows from these numbers. If you take one idea from "
                "the whole programme, take this: the primary job is not to make money, it is to "
                "avoid the losses that make making money impossible."
            ),
        ),
        LessonSpec(
            title="Risk per trade",
            minutes=9,
            body=(
                "The foundational rule of professional risk management is to define, in advance, "
                "the maximum you can lose on any single position — as a fixed fraction of your "
                "capital.\n\n"
                "The common standard is 1% per trade, sometimes 2% for experienced traders with "
                "measured edge. It sounds absurdly conservative until you look at what it "
                "survives. At 1% risk, ten consecutive losses cost roughly 10% of capital: "
                "unpleasant, entirely recoverable, and you are still trading your plan. At 10% "
                "risk per trade, the same ten losses cost about 65%, which requires a 186% gain to "
                "recover and almost certainly ends your participation.\n\n"
                "Losing streaks are not hypothetical. A strategy that wins 50% of the time will "
                "produce a run of seven losses within a few hundred trades — that is simply what "
                "randomness looks like. Your risk per trade determines whether that inevitable "
                "streak is an inconvenience or the end.\n\n"
                "Important distinctions:\n\n"
                "- Risk is not position size. Risking 1% of a $10,000 account is $100 — but if "
                "your invalidation is 10% away, the position itself is $1,000. The two numbers are "
                "connected by the stop distance, which is the subject of the next lesson.\n"
                "- Risk is per idea, not per ticker. Three positions that would all fail for the "
                "same reason are one trade with three names.\n"
                "- Risk is against current capital, not your starting capital or your peak. This "
                "makes sizing shrink automatically during drawdowns, which is exactly the "
                "behaviour you want.\n\n"
                "For long-term investment positions rather than trades, the equivalent question is "
                "position size relative to total portfolio, since there may be no stop. There the "
                "test is: if this went to zero, would it change my plans? If yes, it is too "
                "large — regardless of how convinced you are."
            ),
        ),
        LessonSpec(
            title="Sizing from invalidation",
            minutes=9,
            body=(
                "Position size should be the output of a calculation, never an input. The "
                "calculation is simple and it removes the most common source of catastrophic "
                "loss.\n\n"
                "Position size = (capital × risk %) ÷ distance to stop\n\n"
                "With $10,000 capital, 1% risk and an invalidation 8% below entry: risk amount is "
                "$100, and $100 ÷ 0.08 gives a position of $1,250. If the invalidation were only "
                "2% away, the same $100 of risk supports a $5,000 position.\n\n"
                "This is the inversion that matters. Most people decide how much they want to buy "
                "and then place a stop somewhere convenient. The correct order is to identify "
                "where the idea is wrong, then let the arithmetic tell you the size. A wide "
                "invalidation means a small position; that is not a problem to be engineered "
                "around, it is the trade the market is offering.\n\n"
                "Two failure modes this prevents. Tightening a stop to justify a bigger position "
                "produces a stream of small losses on ideas that were correct but never given "
                "room. And taking a full-size position with a distant stop produces the occasional "
                "loss large enough to undo months of work.\n\n"
                "Practical refinements:\n\n"
                "- Add expected slippage to the stop distance in illiquid assets. Your realised "
                "loss will be worse than your stop implies.\n"
                "- Include fees in the risk amount for short-term trades.\n"
                "- Cap any single position as a percentage of the portfolio regardless of what the "
                "formula says. A very tight stop can otherwise produce an enormous position, and "
                "a gap through it would be devastating.\n"
                "- When scaling in, size the total planned position, not each tranche "
                "separately.\n\n"
                "Do this calculation every time, in a spreadsheet or a calculator. Estimating it "
                "mentally is where discipline erodes, and it erodes fastest when you are most "
                "confident."
            ),
        ),
        LessonSpec(
            title="Portfolio heat and correlation",
            minutes=9,
            body=(
                "Sizing each position correctly is not enough if all of them fail together. "
                "Portfolio heat is your total risk across all open positions, and it is the number "
                "that determines whether a bad week is survivable.\n\n"
                "If you hold eight positions each risking 1%, your heat is 8% — but only if they "
                "are independent. In crypto they rarely are. Correlations across the sector run "
                "high in normal conditions and approach one during stress, which means eight "
                "positions can behave as a single position eight times too large exactly when it "
                "matters.\n\n"
                "This is the mechanism behind most account-ending losses. Each trade looked "
                "prudent in isolation; the portfolio was not.\n\n"
                "Practical controls:\n\n"
                "- Cap total heat. Six percent is a reasonable ceiling for most people; if you are "
                "at the cap, a new position requires closing an existing one.\n"
                "- Group by correlation, not by ticker. Assets in the same category, or that would "
                "all fail on the same macro event, count as one bucket with one shared limit.\n"
                "- Assume correlations rise in a decline. Stress-test by asking what happens if "
                "everything falls 30% simultaneously, because that scenario has occurred "
                "repeatedly.\n"
                "- Count exposure outside your trading account. Equity holdings, employment in the "
                "sector, and any leveraged position all belong in the same calculation.\n\n"
                "There is a subtler correlation worth naming: the one between your positions and "
                "your income. If your job depends on the same market, a downturn hits both at "
                "once. People routinely take crypto risk that would be sensible for someone with "
                "an uncorrelated salary and is not sensible for them.\n\n"
                "Review heat before every new position, not weekly. It is a live number, and the "
                "moment it matters is the moment you are about to add to it."
            ),
        ),
        LessonSpec(
            title="Sizing to volatility",
            minutes=8,
            body=(
                "A fixed percentage stop is a different amount of risk on a stable major than on a "
                "small cap that moves 15% a day. Volatility-based sizing normalises this so every "
                "position carries comparable risk regardless of what it is.\n\n"
                "The method uses ATR from Module 8. Set the stop at a multiple of ATR beyond your "
                "structural invalidation, then size from that distance. Because ATR expands in "
                "volatile conditions, stops widen and positions shrink automatically. In quiet "
                "conditions the reverse happens. You are no longer making a judgment call about "
                "conditions in the moment; the arithmetic makes it for you.\n\n"
                "Worked example. Two assets, both with an invalidation 5% away structurally. Asset "
                "A has a daily ATR of 2%; asset B has 8%. A 1.5-ATR buffer puts A's stop at 8% and "
                "B's at 17%. With 1% risk on $10,000, A supports a $1,250 position and B supports "
                "$588. Same risk, very different sizes — and the second position will not be "
                "stopped out by an ordinary Tuesday.\n\n"
                "This approach has three benefits worth the extra step. It prevents the classic "
                "error of sizing a volatile small cap like a major. It adapts as market conditions "
                "change without requiring you to notice. And it makes results across different "
                "assets comparable in your journal, because every trade risks the same amount.\n\n"
                "For longer-term positions the same principle applies at portfolio level: allocate "
                "smaller weights to more volatile assets so their contribution to total portfolio "
                "risk is roughly equal. A portfolio equally weighted by capital is not equally "
                "weighted by risk — the volatile positions dominate the outcome entirely, which is "
                "usually the opposite of what the investor intended."
            ),
        ),
        LessonSpec(
            title="Drawdown limits and circuit breakers",
            minutes=8,
            body=(
                "Position-level risk controls what one trade can cost. Circuit breakers control "
                "what a bad run can cost, and they exist because judgment degrades exactly when it "
                "is most needed.\n\n"
                "Set three limits in advance, in writing:\n\n"
                "- A daily loss limit. Reach it and you stop for the day. Typically two to three "
                "times your per-trade risk. This exists specifically to prevent revenge trading, "
                "which reliably follows a painful loss.\n"
                "- A weekly or monthly limit, perhaps 6%. Reach it and you reduce size by half "
                "until you have recovered, or stop entirely for the period.\n"
                "- A maximum drawdown limit, perhaps 15–20% from peak. Reach it and you stop "
                "completely, review everything, and only restart with a written plan and reduced "
                "size.\n\n"
                "The reason these must be pre-committed is that in the moment you will have "
                "excellent arguments against them. The market will look like it is about to turn. "
                "You will feel that you have identified your mistake. This feeling is not "
                "information — it is the standard experience of everyone who has ever blown up an "
                "account.\n\n"
                "Pair the limits with a re-entry procedure so stopping is not indefinite: a "
                "required review of the last twenty trades, a written statement of what went "
                "wrong, and a return at half size until a defined recovery. Without a re-entry "
                "path, people either ignore the limit or never trade again.\n\n"
                "A note for long-term investors: circuit breakers still apply, but at the "
                "portfolio level. A rule such as 'if the portfolio falls 25%, I stop adding and "
                "review the thesis for each holding rather than averaging down automatically' "
                "prevents the most common way conviction becomes concentration."
            ),
        ),
        LessonSpec(
            title="Diversification that actually diversifies",
            minutes=9,
            body=(
                "Holding twenty crypto assets is not diversification. It is one bet expressed "
                "twenty times, and it carries the illusion of safety while delivering none of the "
                "substance.\n\n"
                "Genuine diversification requires holdings that respond differently to the same "
                "events. Within crypto that is difficult, because nearly everything correlates "
                "with Bitcoin, and correlations rise toward one during stress — the precise moment "
                "diversification is supposed to help.\n\n"
                "What does provide real separation:\n\n"
                "- Assets outside crypto entirely. This is the only reliable diversification "
                "available, and for most people the honest answer to 'how do I diversify my crypto "
                "portfolio' is 'own things that are not crypto'.\n"
                "- Cash and stablecoins, which are a position, not an absence of one. Holding a "
                "meaningful cash weight is the simplest way to reduce portfolio volatility and it "
                "buys optionality when prices fall.\n"
                "- Different risk tiers within crypto: a large, liquid core behaves differently "
                "from speculative satellites, even though both fall in a decline.\n"
                "- Custody and counterparty diversification. Splitting across venues and storage "
                "methods diversifies operational risk, which is a genuinely independent failure "
                "mode from price.\n"
                "- Time. Building positions across months rather than at once diversifies entry "
                "price, which is a real and underrated form of it.\n\n"
                "The practical structure most people converge on is a core-satellite one: a large "
                "majority in one or two assets you would hold through a full cycle, and a small "
                "remainder in higher-risk positions each sized so that a total loss is "
                "irrelevant.\n\n"
                "And be honest about over-diversification. Twenty positions cannot be researched "
                "or monitored properly by one person with a job. Beyond about eight, additional "
                "names dilute your best ideas while adding work — and unmonitored positions are "
                "where unpleasant surprises accumulate."
            ),
        ),
        LessonSpec(
            title="When leverage is rational, and when it is not",
            minutes=8,
            body=(
                "Leverage is a tool with narrow legitimate uses and enormous capacity for harm. "
                "The honest position is that most retail participants should not use it, and the "
                "reason is not moral — it is that the arithmetic is unforgiving.\n\n"
                "The core problem is that leverage does not simply multiply returns; it "
                "multiplies volatility, and volatility drag compounds against you. A leveraged "
                "position that swings violently loses value relative to an unleveraged one even "
                "when the underlying ends flat. Add liquidation risk and the outcome is that "
                "leveraged positions can be right about direction and still end at zero.\n\n"
                "Where leverage is defensible:\n\n"
                "- Hedging. Shorting a small amount against a large spot position to reduce "
                "exposure without selling, which may have tax or custody advantages.\n"
                "- Capital efficiency at low multiples for professionals with measured edge and "
                "strict controls.\n"
                "- Short-term positions with tight, well-tested invalidation, at 2–3x, where the "
                "leverage is a substitute for tying up capital rather than a way to enlarge the "
                "bet.\n\n"
                "Where it is not: increasing position size because your capital feels too small; "
                "recovering losses faster; any position you would not take unleveraged; and "
                "anything at 10x or above, which in crypto is a coin flip with fees.\n\n"
                "If you use it, the rules are not optional. Keep it to 2–3x. Use isolated margin "
                "so one position cannot consume the account. Size from invalidation exactly as "
                "with spot, so the leverage changes capital efficiency rather than risk. Never add "
                "margin to defend a losing position. Know your liquidation price before entering "
                "and keep it far outside normal volatility.\n\n"
                "The plainest test: if the position would be uncomfortable at 1x, leverage is not "
                "the solution to the discomfort."
            ),
        ),
        LessonSpec(
            title="Tail risk and the failures that are not price",
            minutes=8,
            body=(
                "Most risk management addresses price. The losses that end participation are often "
                "not price events at all, and they deserve explicit planning because no stop-loss "
                "protects against them.\n\n"
                "The list is short and each item has happened repeatedly:\n\n"
                "- Exchange insolvency or freeze. Your balance becomes a bankruptcy claim.\n"
                "- Loss of keys, or a compromised seed phrase.\n"
                "- Smart contract exploit draining a protocol you have funds in.\n"
                "- Stablecoin depeg, particularly during the stress when you need stability.\n"
                "- Regulatory action restricting access, custody or a specific asset.\n"
                "- Personal incapacity, where assets exist but nobody can reach them.\n\n"
                "None of these are addressed by position sizing. They are addressed by "
                "structure:\n\n"
                "- Spread counterparty exposure across venues, and keep only trading balances "
                "there.\n"
                "- Self-custody long-term holdings, with tested backups in separate locations.\n"
                "- Limit exposure to any single smart contract, and treat yield as compensation "
                "for risk rather than as free money.\n"
                "- Hold more than one stablecoin if you hold size, and understand what backs "
                "each.\n"
                "- Keep records that would let someone else — an accountant, an heir — reconstruct "
                "your position.\n\n"
                "The framing that makes this tractable is insurance thinking: accept a small, "
                "certain cost to eliminate a small probability of a catastrophic one. Holding "
                "assets in self-custody costs convenience. Splitting across venues costs "
                "efficiency. Keeping cash costs return. Each is a premium against an outcome you "
                "cannot recover from, and premiums always feel wasteful right up until the moment "
                "they do not."
            ),
        ),
        homework(
            title="Week 12 homework — build your risk framework",
            minutes=12,
            body=(
                "This produces the document you will trade from. Take it seriously.\n\n"
                "1. Build a position size calculator.\n\n"
                "In a spreadsheet: inputs for capital, risk percentage, entry price and stop "
                "price; outputs for risk amount, position size in currency and in units, and "
                "position size as a percentage of capital. Test it against the worked example in "
                "this module.\n\n"
                "2. Audit your current positions.\n\n"
                "For every position you hold, record: size, current portfolio weight, where your "
                "invalidation is, and what percentage of capital you would lose if it hit. Sum the "
                "last column — that is your portfolio heat. Write whether it is above or below the "
                "limit you are about to set.\n\n"
                "3. Run the correlation test.\n\n"
                "Group your positions by what would make them fail. How many independent bets do "
                "you actually have? Then model a simultaneous 30% decline across the sector and "
                "write the resulting portfolio loss as a number.\n\n"
                "4. Write your risk rules.\n\n"
                "One page: risk per trade, maximum portfolio heat, maximum single position, daily "
                "loss limit, monthly loss limit, maximum drawdown limit, and your re-entry "
                "procedure. Sign and date it.\n\n"
                "5. Write your tail-risk structure.\n\n"
                "Where assets are held, across how many counterparties, and what you would do "
                "tomorrow if your primary exchange halted withdrawals. If you do not have an "
                "answer, that is this week's real finding."
            ),
        ),
    ],
)
