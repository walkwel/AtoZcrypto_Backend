"""Module 7 — Trade Setups & Entry Models."""

from app.modules.courses.curriculum.spec import LessonSpec, ModuleSpec, homework
from app.modules.courses.models import CourseLevel, CoursePhase

MODULE = ModuleSpec(
    slug="trade-setups",
    title="Trade Setups & Entry Models",
    summary=(
        "Turning chart reading into repeatable setups: breakouts, pullbacks, ranges and "
        "reversals, each with a defined invalidation, a target and an honest expectancy."
    ),
    level=CourseLevel.INTERMEDIATE,
    phase=CoursePhase.ANALYSIS,
    lessons=[
        LessonSpec(
            title="Trendlines and channels",
            minutes=8,
            body=(
                "A trendline connects successive higher lows in an uptrend or lower highs in a "
                "downtrend. Done properly it visualises the rate at which one side is advancing; "
                "done carelessly it is a way to draw whatever conclusion you already wanted.\n\n"
                "Rules that keep it honest:\n\n"
                "- Use at least three touches. Two points define a line, which means any two "
                "points define a line — a third touch is the first evidence the market is actually "
                "respecting it.\n"
                "- Connect the extremes of wicks or the bodies consistently. Either convention "
                "works; switching between them to make a line fit does not.\n"
                "- Steeper lines break sooner. A near-vertical trendline describes an "
                "unsustainable rate, not a strong trend.\n"
                "- Do not redraw a line because price broke it. That break is the information.\n\n"
                "A channel adds a parallel line on the opposite side, giving you a band. It is "
                "more useful than a single trendline because it suggests both where pullbacks may "
                "find support and where advances may stall, which means it hands you an entry and "
                "a target at once. Price riding the upper edge repeatedly indicates strength; "
                "failing to reach it on a subsequent leg is often the first sign of a weakening "
                "trend.\n\n"
                "The most reliable use is not the break itself but the retest afterwards. A "
                "trendline broken and then retested from the other side, holding, gives you a "
                "defined entry with invalidation a short distance away — which is what makes a "
                "position sizeable.\n\n"
                "One warning that saves a lot of money: trendline breaks produce a high rate of "
                "false signals, especially on lower timeframes and especially in crypto's "
                "volatility. Treat a break as a prompt to look for confirmation — a retest, a "
                "change in structure, a volume expansion — rather than as a signal in itself."
            ),
        ),
        LessonSpec(
            title="The breakout setup",
            minutes=9,
            body=(
                "A breakout trade takes a position as price leaves a defined range, on the "
                "reasoning that compression resolves into expansion and the direction of the "
                "break reveals which side ran out of supply.\n\n"
                "The anatomy of a good one:\n\n"
                "- A clear, well-tested boundary. The more times a level has held, the more orders "
                "sit around it and the more meaningful its failure is.\n"
                "- Contraction beforehand. Narrowing range and falling volatility before the break "
                "indicates a coiled spring rather than a drift.\n"
                "- Volume expansion on the break itself. This is the single best filter. A break "
                "on volume similar to the preceding average is usually noise.\n"
                "- A close beyond the level on your chosen timeframe, not merely a touch.\n\n"
                "The failure mode is the false breakout, and it is common enough that it is "
                "practically a setup of its own. Price pushes just beyond an obvious level, "
                "triggers the stops resting there, finds no follow-through, and reverses back "
                "inside. Whether this is deliberate or simply where the orders were does not "
                "matter; what matters is that it happens often.\n\n"
                "Two ways to handle it, each with a real cost. Enter on the break and accept a "
                "worse win rate for better prices, with invalidation on a close back inside. Or "
                "wait for the retest — let price break, come back to test the level from the other "
                "side, and enter if it holds. The retest gives a much tighter invalidation and a "
                "better win rate, at the cost of missing the moves that never look back. Neither "
                "is superior; pick one, apply it consistently, and measure it.\n\n"
                "Targets for a breakout are usually derived from the height of the prior range "
                "projected from the break, or the next significant level above. Set it before you "
                "enter, and check that the distance justifies the risk before you commit."
            ),
        ),
        LessonSpec(
            title="The pullback setup",
            minutes=9,
            body=(
                "The pullback is the highest-quality setup available to a patient retail trader, "
                "because it enters in the direction of an established trend at a price the trend "
                "has already demonstrated it defends.\n\n"
                "The logic is simple. In an uptrend, price advances, then retraces as short-term "
                "buyers take profits. If the trend is intact, that retracement stops above the "
                "previous higher low and buyers step back in. You are entering with the trend, "
                "near the level where you will know quickly if it has ended.\n\n"
                "What makes a pullback worth trading:\n\n"
                "- It retraces into an area that already matters: a prior level, a broken "
                "resistance that should now act as support, a moving average the trend has "
                "respected, or a high-volume node.\n"
                "- It is orderly. Overlapping candles and declining volume during the pullback "
                "indicate profit-taking. A fast, expanding-volume drop is distribution, not a "
                "pause.\n"
                "- Structure holds. The previous higher low is not breached.\n"
                "- Something confirms the resumption — a rejection wick, an engulfing candle, a "
                "reclaim of a short-term level.\n\n"
                "Invalidation is naturally placed below the pullback's low or below the structural "
                "higher low, which is usually close enough to allow a decent position size. That "
                "combination — trend behind you, tight invalidation, obvious target at the "
                "previous high or beyond — is why this setup carries most professional trend "
                "trading.\n\n"
                "The difficulty is entirely psychological. A pullback always feels like the trend "
                "is ending, because that is exactly what it looks like in the moment. This is why "
                "the entry criteria must be written down in advance: at the point where the setup "
                "is best, your instinct will be to wait for more clarity, and by the time clarity "
                "arrives the entry is gone."
            ),
        ),
        LessonSpec(
            title="Trading ranges",
            minutes=8,
            body=(
                "Markets spend most of their time going sideways, so a strategy that only works in "
                "trends is idle most of the year. Range trading is the discipline of profiting "
                "from that, and its first requirement is correctly identifying that you are in a "
                "range at all.\n\n"
                "A range needs at least two touches of a defined high and a defined low, with "
                "price oscillating between them and no sequence of higher highs or lower lows. "
                "Volume typically declines as the range matures — participants lose interest — and "
                "expands on the eventual break.\n\n"
                "The method:\n\n"
                "- Buy near the lower boundary, sell near the upper one. Enter at the edges, never "
                "in the middle, where you have neither a good price nor a defined invalidation.\n"
                "- Invalidation sits just beyond the boundary — a close outside, not a wick.\n"
                "- Target the opposite edge, or take partial profit at the midpoint if the range "
                "is wide.\n"
                "- Reduce size relative to trend trades. Ranges break, and they usually break "
                "against the last position you took inside them.\n\n"
                "The danger is that ranges end without announcement, and the trade that loses is "
                "the one at the edge that finally gives way. Two habits mitigate this. Watch for "
                "the character of the touches: failing to reach the far edge on successive "
                "attempts indicates pressure building in that direction. And respect the range's "
                "age — the longer it persists and the tighter it compresses, the closer the "
                "resolution and the more violent it tends to be.\n\n"
                "There is also a legitimate decision to simply stand aside. If a range is narrow "
                "relative to fees and volatility, the expected return does not cover the cost of "
                "trading it. Recognising an unprofitable market is a skill, and 'no position' "
                "beats a mediocre one every time."
            ),
        ),
        LessonSpec(
            title="Reversals, and why they are the hardest trades",
            minutes=9,
            body=(
                "Catching a turn is the most attractive trade to imagine and the most reliably "
                "expensive one to attempt. Understanding why is more valuable than any reversal "
                "pattern.\n\n"
                "The core problem: a trend in progress has demonstrated its direction, while a "
                "reversal is a hypothesis about something that has not happened. You are trading "
                "against the observable evidence and in favour of an assumption. Trends also "
                "persist far longer than seems reasonable, particularly in crypto, where reflexive "
                "flows push moves well past any sensible valuation.\n\n"
                "If you take reversals, take them with structure:\n\n"
                "- Require exhaustion first. Extended distance from a moving average, momentum "
                "divergence, climactic volume, a parabolic final leg. Exhaustion is a "
                "precondition, never a signal by itself.\n"
                "- Require a level. Reversals from major higher-timeframe support or resistance "
                "are a different proposition from reversals in open space.\n"
                "- Require a structural break before committing size. In a downtrend, wait for the "
                "first higher low. That single rule turns a guess into a trade with an "
                "invalidation.\n"
                "- Size smaller. Lower win rate demands smaller risk per attempt.\n\n"
                "The alternative is to stop trying to catch turns and instead trade the trend that "
                "follows one. Waiting for a change of structure means giving up the first portion "
                "of the new move in exchange for evidence, and over a year that trade is almost "
                "always worth making.\n\n"
                "One practical warning specific to this market: 'it cannot go lower' is not "
                "analysis, and an asset down 90% can fall another 90%. Percentage declines "
                "compound in a way intuition handles badly, and buying because something is "
                "'cheap' relative to its own past price is not a thesis."
            ),
        ),
        LessonSpec(
            title="Confluence: stacking independent evidence",
            minutes=8,
            body=(
                "Confluence means several independent factors pointing the same way at the same "
                "price. The word 'independent' is the entire lesson — most traders stack "
                "correlated signals and mistake the resulting agreement for strength.\n\n"
                "Five moving averages agreeing is not five pieces of evidence. They are five views "
                "of the same price series, and they will always broadly agree. Adding RSI, MACD "
                "and a stochastic to a chart mostly tells you the same momentum fact three "
                "times.\n\n"
                "Genuinely independent inputs come from different domains:\n\n"
                "- Price structure: a higher-timeframe level, a prior swing, a broken level being "
                "retested.\n"
                "- Momentum: one oscillator, showing whether pressure supports the move.\n"
                "- Participation: volume behaviour and, for derivatives, funding and open "
                "interest.\n"
                "- Positioning: on-chain flows or exchange balances, covered in Module 10.\n"
                "- Fundamentals: is there a reason for demand, from Module 9.\n"
                "- Macro: does the wider environment support risk-taking, from Module 11.\n\n"
                "A setup where a weekly level, a momentum divergence, expanding volume and "
                "supportive positioning coincide is a genuinely different proposition from one "
                "supported by four indicators derived from the same closes.\n\n"
                "Two disciplines make this practical. Define in advance how many independent "
                "factors a trade requires, and write them down as a checklist — three is a common "
                "threshold. And be willing to conclude that they do not align, which happens far "
                "more often than not. The purpose of a confluence rule is to disqualify the "
                "majority of setups; a filter that passes everything is not a filter.\n\n"
                "Also note what confluence cannot do: it improves your odds, it does not remove "
                "the possibility of being wrong. Every trade still needs an invalidation, however "
                "many factors agreed."
            ),
        ),
        LessonSpec(
            title="Invalidation and targets",
            minutes=9,
            body=(
                "Every trade needs two prices decided before entry: where you are wrong, and where "
                "you are finished. Without both you cannot size the position, cannot judge whether "
                "the trade is worth taking, and will make both decisions later under pressure.\n\n"
                "Invalidation is not 'the amount I am willing to lose'. It is the price at which "
                "your reason for entering no longer holds. If you bought a pullback because "
                "structure was intact, invalidation is below the structural low. If you bought a "
                "breakout retest, invalidation is a close back inside the range. Then place the "
                "stop slightly beyond that level — not on it — because levels are zones and noise "
                "around them is normal.\n\n"
                "The critical consequence: the distance to invalidation determines your position "
                "size, not the other way around. If the correct invalidation is 12% away and your "
                "risk rule allows 1% of capital, the position is small. That is the trade the "
                "market is offering. Tightening the stop to justify a larger position is the most "
                "common and most expensive inversion in retail trading — it produces a stream of "
                "small losses on ideas that were correct.\n\n"
                "Targets should be derived from the chart, not from a desired return. Use the next "
                "significant level, a measured move projected from the pattern, the opposite edge "
                "of a range, or a volatility-based projection. Then check the ratio: if the target "
                "is 6% away and invalidation is 5% away, the trade needs to win far more often "
                "than most setups do.\n\n"
                "Two refinements. Consider scaling out — a first target that banks a gain and "
                "de-risks, a runner with a trailed stop. And define a time stop as well as a price "
                "stop: if the thesis has not begun working within a defined period, the setup has "
                "gone stale even if the stop has not been hit. Capital sitting in a trade that is "
                "doing nothing has a cost, and stale positions are where attention quietly leaks."
            ),
        ),
        LessonSpec(
            title="Risk-reward, win rate and expectancy",
            minutes=9,
            body=(
                "Whether a strategy makes money is arithmetic, and the arithmetic is worth being "
                "able to do in your head. Expectancy is the average result per trade:\n\n"
                "expectancy = (win rate × average win) − (loss rate × average loss)\n\n"
                "A positive number means the approach makes money over enough repetitions. A "
                "negative one means it does not, no matter how good any individual trade felt.\n\n"
                "The immediate consequence is that win rate alone tells you nothing. A strategy "
                "winning 40% of the time with three-to-one reward-to-risk returns 0.6R per trade "
                "on average. A strategy winning 70% with a half-to-one ratio returns 0.05R — "
                "barely positive, and negative after fees. The second one feels far better to "
                "trade, which is precisely why so many people run it.\n\n"
                "Expressing everything in R — multiples of the amount risked — is the habit that "
                "makes this usable. A trade risking 1% of capital that returns 2.5% is +2.5R, "
                "whatever the position size or asset. Journalling in R lets you compare trades "
                "across time and instruments, and it removes the emotional weight of currency "
                "amounts from your review.\n\n"
                "Two things follow that matter more than they appear. Sample size: expectancy is "
                "meaningless over ten trades. Random sequences of ten produce almost any result, "
                "so judging a strategy on a handful of outcomes is judging noise. Aim for fifty "
                "before drawing conclusions, and expect long losing streaks even from a good "
                "system — a 40% win rate produces runs of six losses regularly.\n\n"
                "And costs are part of the equation. Spread, fees and slippage subtract from every "
                "trade. A strategy with an edge of 0.15R per trade and costs of 0.1R has almost "
                "nothing left. This is the honest reason frequency matters: more trades multiply "
                "costs against a fixed edge."
            ),
        ),
        LessonSpec(
            title="Building your setup catalogue",
            minutes=8,
            body=(
                "Consistency comes from trading a small number of setups you have defined "
                "precisely, not from recognising many patterns loosely. Your catalogue is the "
                "document that makes this concrete.\n\n"
                "For each setup you intend to trade, write:\n\n"
                "- A name, so you can tag it in your journal.\n"
                "- Market conditions where it applies — trending, ranging, a specific volatility "
                "regime.\n"
                "- Entry criteria, specific enough that two people reading it would mark the same "
                "candles.\n"
                "- Invalidation rule, stated structurally rather than as a percentage.\n"
                "- Target rule.\n"
                "- Position size rule.\n"
                "- Disqualifiers: conditions under which you skip it even if the shape appears.\n\n"
                "Start with two setups, not eight. One trend-following (a pullback), one "
                "mean-reverting (a range edge) is enough to cover most conditions, and the "
                "constraint is the point — you cannot evaluate eight setups over a realistic "
                "number of trades, so you will never learn which ones work.\n\n"
                "Then tag every journal entry with the setup name. After fifty trades, group by "
                "tag and compute expectancy for each. You will usually find that one setup carries "
                "the results and another quietly loses money. That finding is worth more than any "
                "amount of further study, and it is unavailable to anyone who trades whatever "
                "looks good on the day.\n\n"
                "Review the catalogue quarterly. Retire setups with negative expectancy over a "
                "meaningful sample. Refine criteria based on what your losing trades had in "
                "common — that is usually where the disqualifier list comes from. Add a new setup "
                "only when an existing one is retired, so the catalogue stays small enough to "
                "measure."
            ),
        ),
        homework(
            title="Week 7 homework — define and test two setups",
            minutes=12,
            body=(
                "1. Write your setup catalogue.\n\n"
                "Define exactly two setups using the seven fields from the last lesson: name, "
                "conditions, entry, invalidation, target, size, disqualifiers. Be specific enough "
                "that a stranger could apply them. Vague criteria are how discretion sneaks back "
                "in.\n\n"
                "2. Find ten historical examples.\n\n"
                "Scroll back through charts and find five instances of each setup. For each, mark "
                "the entry, the invalidation and the target, and record what actually happened in "
                "R multiples. Be strict: if you would not have recognised it in real time without "
                "seeing what came next, it does not count.\n\n"
                "3. Compute expectancy.\n\n"
                "From your ten examples, calculate win rate, average win in R, average loss in R, "
                "and expectancy for each setup. Then write one sentence acknowledging that ten "
                "samples is far too few to conclude anything — and note what sample size you will "
                "wait for.\n\n"
                "4. Write your disqualifiers.\n\n"
                "Look at the examples that failed. What did they have in common? Add at least one "
                "disqualifier to each setup based on what you found.\n\n"
                "5. Forward test.\n\n"
                "For the next two weeks, mark every occurrence of your setups on live charts "
                "before the outcome is known — on paper, without trading them. This is the only "
                "honest test, and it is the one almost nobody does."
            ),
        ),
    ],
)
