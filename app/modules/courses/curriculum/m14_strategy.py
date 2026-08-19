"""Module 14 — Building & Testing Your Strategy."""

from app.modules.courses.curriculum.spec import LessonSpec, ModuleSpec, homework
from app.modules.courses.models import CourseLevel, CoursePhase

MODULE = ModuleSpec(
    slug="building-your-strategy",
    title="Building & Testing Your Strategy",
    summary=(
        "Turning setups and rules into a written system: how to test it honestly, measure it "
        "properly, and know the difference between a strategy that stopped working and a normal "
        "losing streak."
    ),
    level=CourseLevel.ADVANCED,
    phase=CoursePhase.RISK_AND_STRATEGY,
    lessons=[
        LessonSpec(
            title="What a strategy actually is",
            minutes=8,
            body=(
                "A strategy is a complete set of rules that determines what you do in every "
                "situation you will encounter. Not a good idea, not an indicator, not a view about "
                "where prices are going — a decision procedure.\n\n"
                "It has to answer all of these, without ambiguity:\n\n"
                "- What do I trade? Which assets, and what disqualifies one.\n"
                "- When do I enter? Specific, observable conditions.\n"
                "- How much? A sizing rule, not a judgment.\n"
                "- When do I exit at a loss? A structural invalidation.\n"
                "- When do I exit at a profit? Targets or a trailing rule.\n"
                "- When do I not trade at all? Conditions that keep you out.\n"
                "- What are my limits? Per trade, per portfolio, per period.\n"
                "- How do I review, and what would make me change the rules?\n\n"
                "The test of completeness: could someone else read your document and take the same "
                "trades as you? If it requires your judgment at any step, that step is where your "
                "results will vary unpredictably — and where the variance will not be in your "
                "favour, because judgment degrades under exactly the conditions that produce "
                "trades.\n\n"
                "This does not mean discretion is forbidden. Most successful retail approaches are "
                "discretionary within a rule-based frame: rules define what qualifies and how much "
                "to risk, judgment selects among qualifying opportunities. What is not viable is "
                "the reverse — judgment about size and exits, which is where the damage "
                "happens.\n\n"
                "One more requirement: the strategy has to fit your life. A system requiring "
                "constant screen time will not be executed by someone with a job, and a "
                "half-executed system is worse than a simpler one followed completely. Choose the "
                "approach you will actually run, not the one that looks most sophisticated."
            ),
        ),
        LessonSpec(
            title="Writing the rules",
            minutes=9,
            body=(
                "Vagueness is where strategies fail, because vague rules bend to fit whatever you "
                "already want to do. The discipline is writing conditions that are observably true "
                "or false.\n\n"
                "Compare: 'enter when the trend is strong and price pulls back to support' — every "
                "term is elastic. Against: 'enter when price is above the rising 50-period moving "
                "average on the daily, retraces to within 1 ATR of a level marked in the previous "
                "week's review, and prints a close above the prior candle's high'. The second can "
                "be checked, journalled and tested. The first cannot be wrong.\n\n"
                "Write each rule so that two people would mark the same candles. Practical "
                "guidance:\n\n"
                "- Replace adjectives with measurements. 'High volume' becomes 'volume above its "
                "20-period average'.\n"
                "- Specify the timeframe for every condition. A rule without a timeframe is not a "
                "rule.\n"
                "- Specify whether you use closes or intraday touches. Be consistent.\n"
                "- Define your disqualifiers explicitly. Knowing when not to trade is at least "
                "half the system.\n"
                "- Write the exit rules with the same precision as the entries. Most written "
                "strategies are detailed about entry and hand-wave the exit, which is exactly "
                "backwards in terms of where returns come from.\n\n"
                "Keep the whole document short. A strategy with thirty conditions is not more "
                "robust; it is fitted to the past and will not survive contact with a different "
                "market. Four or five conditions per setup, two setups, is a realistic and "
                "testable system.\n\n"
                "Finally, version it. Date every revision and keep the old ones. When you review "
                "in six months you need to know which rules were in force for which trades, or "
                "your performance data means nothing."
            ),
        ),
        LessonSpec(
            title="Backtesting, and how it lies",
            minutes=10,
            body=(
                "Backtesting applies your rules to historical data to estimate how they would have "
                "performed. It is useful, and it is the source of more false confidence than any "
                "other activity in trading.\n\n"
                "The ways it misleads, roughly in order of danger:\n\n"
                "- Overfitting. Adjust parameters until results look excellent and you have "
                "described the past, not discovered an edge. The tell is fragility: if changing a "
                "moving average from 50 to 55 destroys the results, you have fitted noise. Robust "
                "edges degrade gracefully across nearby parameters.\n"
                "- Hindsight in rule design. You already know what happened. Choosing to test a "
                "rule about breakouts during a period you remember as trending is not a test.\n"
                "- Look-ahead bias. Using information that was not available at the decision point "
                "— including something as subtle as using a daily close to decide an entry that "
                "would have had to be placed during that day.\n"
                "- Survivorship bias. Testing on assets that still exist. The ones that went to "
                "zero are not in your dataset, and they were not obviously doomed at the time.\n"
                "- Ignoring costs. Spread, fees and slippage frequently turn a profitable backtest "
                "into a losing system, especially for higher-frequency rules.\n"
                "- Insufficient data. A strategy tested over one bull market has been tested "
                "against one regime.\n\n"
                "Doing it usefully: define the rules completely before looking at data. Test "
                "across multiple market regimes, including at least one severe decline. Include "
                "realistic costs. Reserve a portion of your data and never look at it until the "
                "rules are final, then test once on that reserved period — if results collapse, "
                "the rules were fitted.\n\n"
                "And hold the conclusion loosely. A backtest tells you a strategy was not "
                "obviously "
                "broken in the past. It is a filter for eliminating bad ideas, not evidence that a "
                "good one will work."
            ),
        ),
        LessonSpec(
            title="Forward testing",
            minutes=8,
            body=(
                "Forward testing means applying your rules to live markets in real time, without "
                "money or with a trivial amount. It is slower and far more honest than "
                "backtesting, because you cannot see what happens next.\n\n"
                "What it catches that a backtest cannot:\n\n"
                "- Whether you can actually identify your setups in real time. Patterns obvious in "
                "hindsight are frequently ambiguous as they form, and this gap is usually large.\n"
                "- Whether the rules are genuinely unambiguous, or whether you find yourself "
                "making judgment calls you did not know were there.\n"
                "- Whether you can execute — whether your entries actually fill, and at what "
                "prices.\n"
                "- How you behave. A backtest never made anyone anxious.\n\n"
                "How to run it properly. Record every signal before the outcome, with a timestamp: "
                "entry, stop, target, size. Record signals you decide to skip and why. Run it for "
                "long enough to accumulate a meaningful sample — thirty trades minimum, more if "
                "your setup is infrequent. And follow the rules exactly, including the trades you "
                "do not like, because filtering by feel is precisely the thing you are trying to "
                "measure.\n\n"
                "Paper trading has one well-known weakness: without money at stake it does not "
                "test psychology, and people execute paper trades far more calmly than real ones. "
                "The fix is to trade the smallest real size your venue allows rather than "
                "simulating. Real money at trivial size produces most of the emotional signal at "
                "almost none of the cost.\n\n"
                "Only after a forward test showing acceptable results and, more importantly, "
                "acceptable adherence, should size increase — and then gradually, over months."
            ),
        ),
        LessonSpec(
            title="Measuring performance properly",
            minutes=9,
            body=(
                "Return alone tells you almost nothing. Two strategies returning 40% are not "
                "comparable if one did it smoothly and the other went 60% down first.\n\n"
                "The measures that matter:\n\n"
                "- Expectancy in R, from Module 7. Average result per trade in multiples of risk. "
                "This is the core number.\n"
                "- Maximum drawdown: the largest peak-to-trough decline. This determines whether "
                "you could actually have held the strategy through it.\n"
                "- Win rate and average win versus average loss, which together explain the "
                "expectancy and tell you what kind of streaks to expect.\n"
                "- Longest losing streak, so you know what normal looks like before you experience "
                "it.\n"
                "- Return relative to volatility, in whatever form — the point is that returns "
                "achieved with less variation are worth more.\n"
                "- Return versus simply holding. If your active strategy underperforms buying and "
                "holding a major asset, all the work is producing negative value, and this "
                "comparison is the one most people avoid.\n\n"
                "Two process measures belong alongside the financial ones. Adherence rate: what "
                "share of your trades followed the rules completely. And the expectancy of "
                "rule-following trades versus improvised ones, which is usually the most "
                "actionable number in your entire journal.\n\n"
                "On sample size, be strict with yourself. Under thirty trades you are reading "
                "noise. Even a hundred trades leaves real uncertainty. Judging a strategy after "
                "eight trades — which is what almost everyone does — is judging randomness, and it "
                "leads to abandoning good systems and adopting bad ones.\n\n"
                "Finally, compare against the right benchmark and the right period. A strategy "
                "that "
                "made 30% in a market that rose 120% has not performed well, however good the "
                "absolute number looks."
            ),
        ),
        LessonSpec(
            title="Changing a strategy without destroying it",
            minutes=9,
            body=(
                "Every strategy has losing periods. The hardest judgment in trading is "
                "distinguishing a normal drawdown from an edge that has genuinely stopped "
                "working — and getting it wrong in either direction is expensive.\n\n"
                "Abandon too early and you strategy-hop: adopting each approach at the end of its "
                "good period and dropping it at the bottom of its bad one, capturing the worst of "
                "everything. Persist too long and you keep running something the market has "
                "adapted around.\n\n"
                "The discipline is to decide in advance what would constitute evidence, before you "
                "are in the drawdown and looking for a reason to act.\n\n"
                "Signs of a normal drawdown: the losing streak is within the range your backtest "
                "and forward test produced; your adherence rate is high; losses are distributed "
                "across setups rather than concentrated; market conditions are ones your strategy "
                "explicitly does not suit, and it is losing modestly rather than badly.\n\n"
                "Signs of a broken edge: the drawdown exceeds anything in your testing; the same "
                "setup fails repeatedly in conditions where it previously worked; the market "
                "structure your edge depended on has changed observably — liquidity, participants, "
                "or the mechanics of the venue; or losses persist across conditions.\n\n"
                "The procedure when you do change something:\n\n"
                "- Change one thing at a time. Multiple simultaneous changes make it impossible to "
                "learn what helped.\n"
                "- Write down the hypothesis and the evidence before changing anything.\n"
                "- Reduce size while testing the change rather than stopping entirely.\n"
                "- Give it a defined evaluation period and sample size before judging.\n"
                "- Never change rules during a drawdown in response to the drawdown itself. Make "
                "changes from a scheduled review, not from pain.\n\n"
                "The most common real problem is not a broken strategy but poor adherence. Check "
                "that first — it is cheaper to fix and far more often the cause."
            ),
        ),
        LessonSpec(
            title="Alerts and sensible automation",
            minutes=8,
            body=(
                "The right amount of automation for most people is not a trading bot. It is "
                "removing the need to watch, so that decisions happen at the times you chose "
                "rather than whenever you happened to look.\n\n"
                "The high-value, low-risk layer:\n\n"
                "- Price alerts at the levels from your weekly review. This replaces monitoring "
                "entirely: you are notified when something you already decided about becomes "
                "relevant.\n"
                "- Resting limit orders at planned entries, so opportunities are taken without "
                "your presence and without your mood.\n"
                "- Stop and target orders placed at entry, so exits do not require you to be "
                "available or calm.\n"
                "- Recurring buys for long-term accumulation, checked for fees.\n"
                "- Calendar reminders for reviews, rebalancing and unlock dates.\n\n"
                "That set removes most of the screen time and most of the impulsive decisions, and "
                "it requires no code.\n\n"
                "Full automation — a system that enters and exits without you — is a different "
                "undertaking. It demands a completely mechanical strategy, real software "
                "engineering, careful handling of exchange outages and partial fills, and "
                "monitoring of the automation itself. The failure modes are not the ones traders "
                "expect: bugs, API changes, connectivity, and a system that keeps running "
                "confidently after conditions have changed. If you pursue it, start with alerts, "
                "then semi-automation where the system proposes and you approve, and only then "
                "consider full execution — with strict limits and a kill switch.\n\n"
                "Be sceptical of purchased bots and copy-trading products. A genuinely profitable "
                "automated strategy has limited capacity and no reason to be sold; the business "
                "model of selling it is the tell."
            ),
        ),
        LessonSpec(
            title="Active or passive: choosing honestly",
            minutes=8,
            body=(
                "Before finalising a strategy, answer a question most people skip: should you be "
                "trading actively at all?\n\n"
                "The honest case for passive. Active trading requires time, emotional control and "
                "a genuine edge, and the majority of active retail participants underperform "
                "simply holding a major asset — after fees, taxes and mistakes. A disciplined "
                "accumulation plan with periodic rebalancing requires perhaps an hour a month, is "
                "far easier to execute consistently, and produces a lower tax and fee burden. For "
                "someone with a demanding job, that is very likely the higher-expectancy "
                "approach.\n\n"
                "The honest case for active. If you have the time, the temperament and a "
                "demonstrated edge — demonstrated meaning measured over a real sample, not felt — "
                "active management can improve returns and, more importantly, reduce drawdowns "
                "through risk management. The ability to be smaller in euphoric conditions is "
                "worth real money over a cycle.\n\n"
                "A reasonable resolution for most people is both, explicitly separated: a passive "
                "core built on a schedule and held through cycles, and a small active allocation "
                "where you apply what this programme taught. Keep them in separate accounts if "
                "you can, with separate records. The separation matters — mixing them means a bad "
                "trading month quietly consumes long-term capital, and the discipline of the core "
                "erodes.\n\n"
                "Whichever you choose, choose deliberately and write down why. The worst outcome "
                "is drifting between them: holding long-term until a position falls, then trading "
                "it; trading until a trade goes wrong, then calling it an investment. That drift "
                "is extremely common, it is how most portfolios end up full of losers, and "
                "naming your lane in advance is what prevents it."
            ),
        ),
        LessonSpec(
            title="Your trading plan document",
            minutes=9,
            body=(
                "Everything in this programme converges into one document. It should fit on two "
                "pages, and you should be able to open it and know exactly what to do.\n\n"
                "The structure:\n\n"
                "- Objective and horizon. From Module 1, revised with what you now know.\n"
                "- Capital and maximum loss. The number that caps everything.\n"
                "- Approach. Passive core, active allocation, or both — with the split.\n"
                "- Universe. What you will trade, and the liquidity threshold below which you will "
                "not.\n"
                "- Setups. Your catalogue from Module 7, with full criteria.\n"
                "- Risk rules. From Module 12: risk per trade, portfolio heat cap, maximum "
                "position, drawdown limits and the re-entry procedure.\n"
                "- Execution. Order types, the checklist, and your rules on slippage.\n"
                "- Routines. Daily, weekly and monthly, with times.\n"
                "- Circuit breakers. Loss limits and the tilt procedure from Module 13.\n"
                "- Custody. Tier structure from Module 3 and target percentages.\n"
                "- Review schedule. What you measure and when, and what would cause a rule "
                "change.\n\n"
                "Then two commitments, written explicitly because they are the ones that fail: "
                "what you will never do (trade without a stop, exceed your heat cap, act on an "
                "unsolicited message, add to a loser outside a plan), and what would make you stop "
                "entirely.\n\n"
                "Sign it and date it. Review it quarterly and version each revision. Read it "
                "before every session for the first month, then weekly.\n\n"
                "A plan you do not read is decoration. The value is not in having written it; it "
                "is that on the day the market is doing something frightening, the decision was "
                "made months ago by a calmer version of you."
            ),
        ),
        homework(
            title="Week 14 homework — write and test the system",
            minutes=12,
            body=(
                "1. Write the trading plan.\n\n"
                "Two pages, every section from the last lesson filled in with specifics drawn from "
                "your earlier homework. No placeholders. Sign and date it.\n\n"
                "2. Backtest one setup.\n\n"
                "Take your best setup and apply it manually across at least fifty historical "
                "instances, spanning both a rising and a falling market. Record every trade in R, "
                "including costs. Calculate expectancy, win rate, maximum drawdown and longest "
                "losing streak. Then write one paragraph on which of the six backtest biases you "
                "are most likely to have committed.\n\n"
                "3. Robustness check.\n\n"
                "Change one parameter of your setup by roughly 10% and re-run a portion of the "
                "test. If results collapse, note that the rule is fragile and consider why.\n\n"
                "4. Start a forward test.\n\n"
                "Begin logging every real-time signal from today — entry, stop, target, size, "
                "timestamp — at minimum size or on paper. Commit to thirty trades before drawing "
                "any conclusion, and write that commitment down.\n\n"
                "5. The benchmark question.\n\n"
                "Calculate what simply holding a major asset would have returned over your "
                "backtest period. Write one honest sentence comparing it to your strategy, and "
                "what that implies about whether you should be trading actively."
            ),
        ),
    ],
)
