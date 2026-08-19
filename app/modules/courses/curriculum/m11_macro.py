"""Module 11 — Macro, Market Cycles & Narratives."""

from app.modules.courses.curriculum.spec import LessonSpec, ModuleSpec, homework
from app.modules.courses.models import CourseLevel, CoursePhase

MODULE = ModuleSpec(
    slug="macro-and-cycles",
    title="Macro, Market Cycles & Narratives",
    summary=(
        "The backdrop that decides whether good analysis works: liquidity and rates, the shape "
        "of crypto cycles, capital rotation, and how narratives are born and die."
    ),
    level=CourseLevel.ADVANCED,
    phase=CoursePhase.ANALYSIS,
    lessons=[
        LessonSpec(
            title="Why crypto trades with macro",
            minutes=8,
            body=(
                "For its first decade crypto was largely uncorrelated with everything else — a "
                "small, retail-driven market that traded on its own news. That is no longer true, "
                "and pretending otherwise leads to persistent confusion about why a "
                "well-researched "
                "position is falling on a day with no crypto news.\n\n"
                "Three things changed. Institutional participation arrived, and institutions "
                "manage crypto inside a portfolio alongside equities and bonds, adjusting exposure "
                "by the same risk framework. Regulated access products brought conventional "
                "capital that behaves conventionally. And leverage tied the market to funding "
                "conditions — when it becomes expensive to borrow, leveraged positions across all "
                "assets get reduced together.\n\n"
                "The practical result is that crypto now behaves like a high-beta risk asset. It "
                "generally rises when investors are willing to take risk and falls when they are "
                "not, with amplitude larger than equities in both directions. Correlations are not "
                "constant — they spike during stress, which is exactly when diversification would "
                "be valuable — but the direction of the relationship is now stable enough to plan "
                "around.\n\n"
                "What follows for you:\n\n"
                "- Know the macro calendar. Inflation prints and central bank decisions move "
                "crypto meaningfully, and being unaware of them means being surprised by "
                "volatility that was scheduled.\n"
                "- Do not expect crypto to hedge an equity drawdown. In the sharpest declines it "
                "has fallen further, not less.\n"
                "- Treat total portfolio risk as one number. If you hold equities and crypto, you "
                "hold more of one bet than the two lines suggest.\n\n"
                "The independent-asset thesis may return as the market matures. It is not the "
                "present reality, and positioning for the market you wish existed is expensive."
            ),
        ),
        LessonSpec(
            title="Liquidity, rates and the dollar",
            minutes=9,
            body=(
                "If you track one macro variable, track liquidity: how much money is available in "
                "the financial system and whether that amount is growing. Risk assets, crypto most "
                "of all, are extraordinarily sensitive to it.\n\n"
                "Interest rates are the primary transmission mechanism. When rates are low, "
                "holding cash pays nothing and borrowing is cheap, so capital moves toward "
                "risk. When rates rise, safe assets pay a real return, and every speculative "
                "asset must compete against that. The 2022 decline coincided with the fastest rate "
                "rise in decades; that was not a coincidence, and it overwhelmed every "
                "crypto-specific fundamental in both directions.\n\n"
                "Central bank balance sheets matter alongside rates. Expansion adds liquidity "
                "directly; contraction withdraws it. Watching the direction of change is generally "
                "more useful than the level.\n\n"
                "The dollar is the third leg. A strengthening dollar tightens global financial "
                "conditions, because dollar-denominated debt gets harder to service worldwide. "
                "Crypto is priced in dollars and has historically struggled during sustained "
                "dollar strength.\n\n"
                "What to actually watch, in order of usefulness:\n\n"
                "- The direction of policy rates and, more importantly, expectations of future "
                "rates, which markets price continuously.\n"
                "- The dollar index, as a trend rather than a daily figure.\n"
                "- Credit spreads, which widen when investors demand more compensation for risk — "
                "one of the better early warnings available.\n"
                "- Inflation data, mainly because it drives rate expectations.\n\n"
                "You do not need to forecast any of this, and attempting to will not go well. What "
                "you need is awareness of the regime: is liquidity expanding or contracting? "
                "Strategies that work beautifully in the first environment fail in the second, and "
                "knowing which one you are in should change your position sizing."
            ),
        ),
        LessonSpec(
            title="The four-year cycle and what drives it",
            minutes=9,
            body=(
                "Crypto has historically moved in roughly four-year cycles, and the pattern is "
                "consistent enough to be worth understanding — and uncertain enough that betting "
                "your capital on its precise repetition is unwise.\n\n"
                "The mechanical anchor is Bitcoin's halving, which cuts the rate of new issuance "
                "roughly every four years. The supply of new coins reaching the market falls; if "
                "demand holds, the reduced sell pressure supports price. Historically the largest "
                "advances have occurred in the twelve to eighteen months following a halving.\n\n"
                "The reflexive engine matters more than the arithmetic. Rising prices attract "
                "attention, attention brings new capital, new capital pushes prices higher, which "
                "attracts more attention. The same loop runs in reverse: falling prices produce "
                "forced selling from leveraged positions, which pushes prices lower, which "
                "triggers more. Neither phase is really about the halving; the halving simply sets "
                "the timing of the initial impulse.\n\n"
                "The rough shape, which you will recognise:\n\n"
                "- Accumulation: prices flat and low after a long decline, sentiment absent, "
                "builders working. Boring, and where the best risk-adjusted entries have "
                "historically been.\n"
                "- Early advance: prices rising with little public attention, majors leading.\n"
                "- Expansion: broad participation, capital rotating into smaller assets, media "
                "coverage, new products.\n"
                "- Euphoria: parabolic moves, extreme leverage, obviously worthless assets rising "
                "hardest, and confident claims that it is different this time.\n"
                "- Decline: a sharp initial break, a rally that fails, then a grinding fall over "
                "months as leverage unwinds.\n\n"
                "The honest caveats: three or four cycles is not a statistical sample. The "
                "halving's proportional supply impact shrinks each time. Macro conditions now "
                "dominate in a way they did not before. Use the cycle as a lens for where "
                "sentiment sits, not as a calendar for what happens next."
            ),
        ),
        LessonSpec(
            title="What tops and bottoms actually look like",
            minutes=9,
            body=(
                "Nobody rings a bell, but extremes do have recognisable characteristics — mostly "
                "behavioural rather than technical, and mostly visible in what people around you "
                "are doing.\n\n"
                "Signs that have accompanied major tops:\n\n"
                "- Assets with no product or mechanism outperforming assets with both, by a wide "
                "margin.\n"
                "- Leverage at extremes: persistently high funding rates, record open interest, "
                "and frequent large liquidation cascades.\n"
                "- Retail participation surging — app store rankings, search interest, "
                "non-financial media covering prices, people with no prior interest asking what to "
                "buy.\n"
                "- Long-term holders distributing into strength while newer participants absorb "
                "supply.\n"
                "- A widespread belief that a permanent new regime has arrived, and that "
                "traditional valuation no longer applies.\n"
                "- Parabolic price action, where each advance is steeper than the last.\n\n"
                "Signs that have accompanied major bottoms:\n\n"
                "- Capitulation on enormous volume, with a large share of coins moving at a "
                "realised loss.\n"
                "- Sentiment surveys at extremes and media declaring the sector finished.\n"
                "- Prices below the aggregate cost basis of holders, meaning the average "
                "participant is underwater.\n"
                "- Miner or validator stress, forcing sales from producers.\n"
                "- Long-term holders accumulating steadily while price does nothing.\n"
                "- Volatility collapsing and price going flat for months. Bottoms are boring, not "
                "dramatic.\n\n"
                "Two things to hold onto. Extremes take longer than they should — 'obviously "
                "overextended' can continue for months, and being early is indistinguishable from "
                "being wrong while it is happening. And these are contextual reads, not triggers: "
                "their value is in adjusting how much risk you take, not in calling a date. Scale "
                "exposure gradually as evidence accumulates rather than making a single decision."
            ),
        ),
        LessonSpec(
            title="Dominance and capital rotation",
            minutes=8,
            body=(
                "Capital does not enter the whole market at once. It arrives in a fairly "
                "consistent order, and knowing that order tells you what kind of environment you "
                "are in.\n\n"
                "Bitcoin dominance — Bitcoin's share of total crypto market capitalisation — is "
                "the standard measure. The historical pattern runs: new capital enters through "
                "Bitcoin first, because it is the most familiar and most liquid, pushing dominance "
                "up. Once Bitcoin's move matures, profits rotate into Ethereum and large "
                "alternatives, and dominance falls. Later, capital moves further out into smaller "
                "assets. In declines the flow reverses — capital retreats to Bitcoin and "
                "stablecoins, and dominance rises as smaller assets fall harder.\n\n"
                "This gives you a practical read:\n\n"
                "- Dominance rising with prices rising: Bitcoin-led advance, alternatives "
                "underperform.\n"
                "- Dominance falling with prices rising: broad risk appetite, alternatives "
                "outperform. Historically the most rewarding and most dangerous phase.\n"
                "- Dominance rising with prices falling: flight to relative safety, and "
                "alternatives are usually falling much harder than the index suggests.\n\n"
                "Two important caveats. Dominance is a ratio, so it moves when either side moves — "
                "rising dominance can mean Bitcoin rising or alternatives falling, and those are "
                "different situations. And its long-run behaviour is distorted by the sheer number "
                "of new assets created each cycle, which mechanically dilutes it.\n\n"
                "The practical application is not prediction but expectation-setting. If you hold "
                "smaller assets in a Bitcoin-led phase, underperformance is the normal outcome, "
                "not evidence your thesis is broken. And when capital has rotated far out into the "
                "smallest assets, you are late in the sequence — which is precisely when position "
                "sizes should be coming down rather than up."
            ),
        ),
        LessonSpec(
            title="Narratives: how they form, and how they end",
            minutes=9,
            body=(
                "Crypto capital moves in narratives — themes that concentrate attention and money "
                "on a category for months. Understanding the mechanics is more useful than trying "
                "to guess the next one.\n\n"
                "The life cycle is consistent. A genuine technical development or a plausible "
                "story appears. Early participants who follow the space closely accumulate "
                "quietly. "
                "The theme gets a name, which matters more than it should — a named category is "
                "investable in a way an unnamed one is not. Attention builds, prices rise, and the "
                "rise itself becomes the strongest evidence for the story. New projects appear to "
                "capture the flow, most of them low quality. Eventually attention peaks, capital "
                "rotates to the next theme, and the category declines regardless of whether the "
                "underlying development succeeded.\n\n"
                "The uncomfortable observation is that narrative performance is largely "
                "independent of delivery. Categories have risen enormously on the promise of "
                "technology that never shipped, and technology that shipped successfully has "
                "declined because attention moved elsewhere. In the short term you are trading "
                "attention, not adoption.\n\n"
                "How to use this without being used by it:\n\n"
                "- Identify the current dominant narrative explicitly, and write it down. Simply "
                "naming it reduces its grip on your judgment.\n"
                "- Distinguish where you are in its life cycle. Entering a narrative that already "
                "has a name and mainstream coverage is entering late.\n"
                "- Separate the trade from the investment. A narrative position is a trade with a "
                "defined exit; an investment needs the fundamentals from Module 9.\n"
                "- Watch for the tell: when projects begin rebranding to attach themselves to a "
                "theme, the theme is mature.\n\n"
                "And accept that you will miss most of them. Chasing every narrative means "
                "arriving late repeatedly, which is a reliable way to lose money in a rising "
                "market."
            ),
        ),
        LessonSpec(
            title="Measuring sentiment",
            minutes=8,
            body=(
                "Sentiment is the aggregate emotional state of participants, and it is useful "
                "precisely because it is most extreme when it is most wrong. Measuring it — rather "
                "than sensing it — is what makes it usable, because your own sentiment is part of "
                "the crowd's.\n\n"
                "Available measures, roughly in order of reliability:\n\n"
                "- Funding rates and open interest. Positioning is sentiment expressed with money, "
                "which makes it the most honest signal available. Extreme positive funding means "
                "crowded long.\n"
                "- The put-call ratio and options skew, showing what participants are paying to "
                "protect against.\n"
                "- Composite fear and greed indices, which bundle volatility, volume, social "
                "activity and dominance into a single figure. Crude, but useful at extremes.\n"
                "- Search interest and app rankings, which track retail attention well.\n"
                "- Social volume and tone, noisy but informative at extremes.\n"
                "- Surveys and positioning reports from institutional sources.\n\n"
                "How to use them. Sentiment is a contrarian indicator at extremes only. Extreme "
                "fear has historically marked better buying opportunities than any level of "
                "technical support; extreme greed has marked poor entries. In the middle range it "
                "tells you nothing, and most of the time it sits in the middle range.\n\n"
                "The most valuable application is on yourself. Sentiment extremes are visible "
                "internally before they are visible in data: the desire to add size after a strong "
                "run, the reluctance to buy after a decline, the urge to check prices "
                "constantly. Your own emotional state is a sample of the crowd's, which is exactly "
                "why journalling how you felt at entry — the column from Module 2 — becomes "
                "genuinely predictive over time. When you find yourself certain, that is the "
                "signal worth noticing."
            ),
        ),
        LessonSpec(
            title="Building your own cycle map",
            minutes=8,
            body=(
                "The point of this module is not to predict the cycle but to know roughly where "
                "you are, so that your risk-taking is proportionate. A written map does that.\n\n"
                "Build it from four inputs, each answered in one line:\n\n"
                "- Liquidity regime. Are rates and central bank balance sheets expanding or "
                "contracting? Is the dollar strengthening or weakening?\n"
                "- Cycle position. Where does the sequence in this module suggest we sit — "
                "accumulation, advance, expansion, euphoria, decline?\n"
                "- Rotation. Is dominance rising or falling, and how far out has capital moved?\n"
                "- Sentiment. Where are funding, fear and greed, and retail attention?\n\n"
                "Then write one paragraph: what these four say together, and — critically — what "
                "would change your mind. Date it.\n\n"
                "Now derive the only output that matters: your total exposure level. Not which "
                "assets, but how much. A reasonable framework is to hold a lower share of your "
                "risk budget deployed in euphoric conditions and a higher share in accumulation "
                "conditions, adjusted gradually. That single discipline — being smaller when "
                "everyone is confident and larger when nobody is — captures most of the practical "
                "value of macro analysis, and it does not require you to be right about timing.\n\n"
                "Review monthly. Compare each new map against the last and note what changed and "
                "whether you acted on it. Over a full cycle this file becomes a record of how your "
                "judgment behaves under different conditions, which is genuinely rare and "
                "genuinely useful.\n\n"
                "One discipline: write the map before you look at your portfolio's performance. "
                "Assessing the environment after seeing your own profit and loss is not assessment."
            ),
        ),
        homework(
            title="Week 11 homework — write your macro map",
            minutes=12,
            body=(
                "1. Build the map.\n\n"
                "Complete all four inputs — liquidity, cycle position, rotation, sentiment — with "
                "actual current figures, not impressions. Find the numbers: current policy rate "
                "and direction, dollar index trend, Bitcoin dominance and its three-month change, "
                "funding rates, a fear and greed reading. Date it.\n\n"
                "2. Write the paragraph.\n\n"
                "What do these four say together, and what specific observation would change your "
                "conclusion? Be concrete — 'if dominance falls below X' rather than 'if things "
                "change'.\n\n"
                "3. Set your exposure.\n\n"
                "Based on the map, state what percentage of your risk budget you think should be "
                "deployed right now, and why. Compare it to what you actually have deployed. If "
                "they differ, write what you will do about it.\n\n"
                "4. Name the narrative.\n\n"
                "Identify the current dominant narrative in one sentence. Estimate where it sits "
                "in its life cycle and what evidence supports that. Note whether you own anything "
                "in it, and whether you bought it as a trade or an investment.\n\n"
                "5. Historical study.\n\n"
                "Pick one previous cycle top or bottom. List which of the signs from this module "
                "were present, and which were absent. Write one sentence on what you would "
                "realistically have concluded in real time."
            ),
        ),
    ],
)
