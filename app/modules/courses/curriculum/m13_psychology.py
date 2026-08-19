"""Module 13 — Trading Psychology & Discipline."""

from app.modules.courses.curriculum.spec import LessonSpec, ModuleSpec, homework
from app.modules.courses.models import CourseLevel, CoursePhase

MODULE = ModuleSpec(
    slug="psychology-and-discipline",
    title="Trading Psychology & Discipline",
    summary=(
        "Why capable people execute badly, the specific biases that cost the most money, and "
        "the routines that let you follow a plan when following it is hardest."
    ),
    level=CourseLevel.INTERMEDIATE,
    phase=CoursePhase.RISK_AND_STRATEGY,
    lessons=[
        LessonSpec(
            title="Why knowing is not doing",
            minutes=8,
            body=(
                "By this point in the programme you know more about markets than most "
                "participants. That knowledge will not, on its own, produce good results — and "
                "understanding why is the beginning of actually improving.\n\n"
                "The gap exists because analysis and execution happen in different states. You "
                "research calmly, with no money at stake and no time pressure. You execute with "
                "capital committed, prices moving, and a physical stress response that measurably "
                "narrows attention and biases you toward immediate relief. Studies of traders "
                "consistently find that decision quality falls under exactly these conditions — "
                "and everyone believes they are the exception.\n\n"
                "This is why the professional answer is not 'be more disciplined'. Willpower is a "
                "depleting resource and a poor foundation. The answer is structure: decisions made "
                "in advance, written down, and executed mechanically. A stop-loss order placed at "
                "entry does not need you to be calm later. A position size from a spreadsheet does "
                "not need you to be objective about how confident you feel.\n\n"
                "The practical framing for this module: treat your future self as an unreliable "
                "employee. Capable, but prone to panic, overconfidence and boredom. Your job now "
                "is to write procedures that produce acceptable outcomes even when that person is "
                "having a bad day.\n\n"
                "Everything that follows is a specific failure mode with a specific structural "
                "fix. None of the fixes require you to become a different person, which is "
                "fortunate, because you will not."
            ),
        ),
        LessonSpec(
            title="The biases that cost the most",
            minutes=9,
            body=(
                "A handful of cognitive biases account for most avoidable losses. Naming them "
                "matters, because a named pattern is one you can catch in yourself.\n\n"
                "Confirmation bias. Once you hold a position you preferentially notice supporting "
                "information. You follow accounts that agree, discount critics as uninformed, and "
                "read every ambiguous development favourably. The fix is procedural: write the "
                "bear case before entering, and deliberately read the strongest opposing argument "
                "each time you review.\n\n"
                "Anchoring. Fixating on a reference price — what you paid, the previous high, a "
                "round number. 'I will sell when it gets back to my entry' is anchoring, and the "
                "market has no knowledge of your entry. The fix: evaluate every holding as though "
                "you were buying it today at today's price. If you would not buy it now, you are "
                "holding it for a reason unrelated to its merits.\n\n"
                "Recency bias. Weighting the last few weeks far above the last few years. After a "
                "long rally, risk feels low precisely when it is highest. The fix is looking at "
                "longer timeframes deliberately, and reading your own notes from a different "
                "market regime.\n\n"
                "Sunk cost. Continuing because of what you have already lost, in money or in "
                "research effort. The hours you spent studying an asset are gone regardless of "
                "what you do next.\n\n"
                "Hindsight bias. After the fact, everything looks obvious, which corrupts your "
                "ability to learn — you conclude you 'knew' and simply failed to act, when in "
                "fact you did not know. The only defence is a journal written before outcomes.\n\n"
                "Survivorship bias. You see the people who made spectacular returns because they "
                "post about it. The identical strategy that failed is invisible. Almost all "
                "publicly visible crypto success is filtered this way."
            ),
        ),
        LessonSpec(
            title="FOMO and the chase",
            minutes=8,
            body=(
                "Fear of missing out is the most expensive emotion in crypto, because the market "
                "is engineered to produce it continuously. There is always something rising "
                "faster than what you own, and social media surfaces it constantly.\n\n"
                "The mechanics are consistent. Something moves sharply. You notice it after the "
                "move. You watch it continue, which converts caution into regret. Eventually the "
                "pain of watching exceeds the fear of buying, and you enter — typically near the "
                "point of maximum attention, which is where late buyers provide exit liquidity for "
                "early ones. It then falls, and you either take a loss or hold something you never "
                "researched.\n\n"
                "What makes it hard is that it is not irrational in the moment. The move is real, "
                "the gains are real, and other people genuinely made money. The error is not in "
                "the observation but in the conclusion — that participation now carries the same "
                "risk it did before.\n\n"
                "Structural defences:\n\n"
                "- A mandatory waiting period. No position taken within 24 hours of first "
                "encountering the idea. Most FOMO does not survive a night's sleep, and genuine "
                "opportunities generally survive a day.\n"
                "- A research requirement. Nothing enters the portfolio without a completed "
                "template from Module 9. The friction is the point.\n"
                "- A written watchlist with entry levels defined in advance, so buying is "
                "executing a plan rather than reacting.\n"
                "- Accepting explicitly that you will miss most opportunities. You cannot "
                "participate in everything, and attempting to guarantees arriving late "
                "repeatedly.\n\n"
                "One reframe worth internalising: missing a gain costs nothing. It feels like a "
                "loss, but your capital is intact and available. Chasing a move and being wrong "
                "costs real money. These two outcomes feel similar and are not remotely "
                "comparable."
            ),
        ),
        LessonSpec(
            title="Loss aversion and the losers you keep",
            minutes=9,
            body=(
                "Losses hurt roughly twice as much as equivalent gains feel good. That asymmetry "
                "is well documented and it produces a specific, predictable, expensive pattern: "
                "people sell winners too early and hold losers too long.\n\n"
                "The reasoning is emotional rather than analytical. Selling a winner locks in a "
                "gain and feels like success. Selling a loser makes the loss real and feels like "
                "an admission of failure. While the position remains open the loss is somehow "
                "provisional. So the portfolio gradually fills with the worst holdings, which is "
                "precisely backwards.\n\n"
                "It compounds through averaging down. Adding to a losing position lowers the "
                "average entry and creates a feeling of progress, while actually increasing "
                "exposure to something already going against you. Done without a pre-defined "
                "limit, this is how a manageable loss becomes the position that defines your "
                "year.\n\n"
                "The structural fixes:\n\n"
                "- Stop-loss orders placed at entry, so the decision is made once, when you are "
                "objective.\n"
                "- The replacement test, applied to every holding: would I buy this today at this "
                "price? If no, sell. This removes your entry price from the decision entirely, "
                "which is the whole difficulty.\n"
                "- Scheduled reviews rather than reactive ones, so positions get examined on a "
                "calendar rather than when they hurt.\n"
                "- A pre-defined rule for adding to positions, including a maximum. Planned "
                "scaling is fine; unplanned averaging down is not.\n\n"
                "One reframe that helps genuinely: a stop-loss being hit is not a failure, it is "
                "the system working. Approximately half of well-chosen trades will lose — that is "
                "what a 50% win rate means. Losses are a cost of doing business, and treating each "
                "one as a verdict on your judgment guarantees you will eventually stop honouring "
                "them."
            ),
        ),
        LessonSpec(
            title="Overconfidence after winning",
            minutes=8,
            body=(
                "The most dangerous period in a trader's year is immediately after a run of "
                "success. This is counter-intuitive and it is well established, both in research "
                "and in the experience of nearly everyone who has traded for long.\n\n"
                "What happens is straightforward. A few wins — often driven substantially by "
                "favourable conditions rather than skill — get attributed to judgment. Confidence "
                "rises. Position sizes creep up. Setups that would have been rejected start "
                "looking acceptable. Risk rules feel like they were written for a less capable "
                "version of you. Then conditions change, and the larger positions taken on weaker "
                "setups produce losses out of proportion to the earlier gains.\n\n"
                "In a broad bull market this is nearly universal, because almost everything works "
                "and it is genuinely difficult to distinguish skill from a rising tide. The "
                "clearest sign is not arrogance; it is a quiet drift in behaviour — checking the "
                "position size calculator less often, skipping the research template, taking "
                "trades without writing them down.\n\n"
                "Defences:\n\n"
                "- Fixed fractional sizing based on current capital. Size rises with your account "
                "rather than with your mood, which is the correct relationship.\n"
                "- A rule requiring a written justification for any size increase beyond your "
                "standard risk, reviewed the following day.\n"
                "- Tracking your process separately from your results. Did you follow the plan? "
                "That question is answerable regardless of outcome, and it is the one that "
                "predicts your next hundred trades.\n"
                "- Reading your journal from the last drawdown when things are going well. It is "
                "an unpleasant and effective exercise.\n\n"
                "The honest question to ask after a strong run: how much of this was the market, "
                "and how much was me? In a rising market the answer is usually mostly the market, "
                "and being able to say so is what keeps you solvent when it stops rising."
            ),
        ),
        LessonSpec(
            title="Tilt, revenge trading and stopping",
            minutes=8,
            body=(
                "Tilt is the state in which frustration replaces analysis. It follows a painful "
                "loss, a stop hit just before the market went your way, or a missed move — and "
                "while you are in it, every decision is worse than the one you would make calmly, "
                "and you cannot tell.\n\n"
                "Revenge trading is its most common expression: immediately taking another "
                "position to recover what was just lost. The size is usually larger, the setup "
                "weaker, and the motivation is emotional repair rather than opportunity. This "
                "sequence — loss, larger loss, desperate position — is the standard anatomy of a "
                "blown account, and it typically unfolds within a single session.\n\n"
                "Recognise the physical and behavioural signs, because they precede the "
                "rationalisations: checking prices compulsively, arguing with people online about "
                "your position, feeling that the market is doing something to you personally, "
                "wanting to make it back today, an unusual urge to increase size.\n\n"
                "The only reliable intervention is pre-commitment, because in the state itself you "
                "will construct excellent arguments for continuing:\n\n"
                "- A daily loss limit that ends the session automatically, from Module 12.\n"
                "- A mandatory break after any loss above a threshold — twenty minutes minimum, "
                "away from the screen.\n"
                "- A rule that no new position is opened within an hour of a stop being hit.\n"
                "- A physical circuit breaker: close the platform, leave the room. Distance works "
                "when reasoning does not.\n\n"
                "The broader point is that stopping is a skill. Most people can analyse; far fewer "
                "can stop. The ability to close the laptop on a bad day is worth more over a "
                "career than any pattern in this programme, and unlike analysis it requires no "
                "talent — only a rule you wrote when you were calm."
            ),
        ),
        LessonSpec(
            title="Routines that do not depend on willpower",
            minutes=9,
            body=(
                "Consistency comes from routine, not from motivation. A routine you follow "
                "mechanically survives fatigue, distraction and stress in a way that intentions do "
                "not.\n\n"
                "A pre-market routine, twenty minutes: check the macro calendar for scheduled "
                "events, review your open positions and confirm every stop is in place and "
                "correctly sized, check your watchlist against your pre-defined entry levels, and "
                "write one line on your read of conditions. Nothing here involves deciding to "
                "trade; it establishes the state of things before you have any impulse to act "
                "on.\n\n"
                "A pre-trade routine: the execution checklist from Module 5, run every time "
                "without exception. If you cannot complete it, you do not take the trade — the "
                "incomplete checklist is the answer, not an obstacle.\n\n"
                "A post-trade routine: log it immediately with the reason and your emotional "
                "state, before the outcome is known. Reasons recorded afterwards are "
                "reconstructions.\n\n"
                "A weekly review, thirty minutes: every trade closed that week, your process "
                "adherence rate, your current portfolio heat, and one thing to do differently. "
                "Schedule it and treat it as unmissable.\n\n"
                "A monthly review: expectancy by setup, whether your rules still fit conditions, "
                "and a re-read of your macro map from Module 11.\n\n"
                "Two design principles make routines stick. Keep them short enough that you "
                "actually do them — a twenty-minute routine performed daily beats a two-hour one "
                "performed occasionally. And attach them to fixed times rather than to feelings, "
                "since 'when I get a chance' reliably means never.\n\n"
                "Set the boundaries too: defined hours for looking at markets, notifications off "
                "outside them, and no decisions after a certain hour. A market that never closes "
                "will consume as much of your attention as you allow, and attention spent is not "
                "attention available."
            ),
        ),
        LessonSpec(
            title="The journal as a mirror",
            minutes=9,
            body=(
                "The trading journal is the single highest-return habit available, and it is the "
                "one most people skip because its value is invisible for the first two months.\n\n"
                "What it does that memory cannot: memory is reconstructive and self-serving. You "
                "will remember your good calls vividly and your bad ones vaguely, and you will "
                "remember having reasons you did not have. A journal is the only honest record of "
                "what you actually thought before you knew the answer.\n\n"
                "What to record for every position, at entry:\n\n"
                "- Date, asset, direction, size, entry price.\n"
                "- The setup name from your catalogue.\n"
                "- Why — in one specific sentence.\n"
                "- Stop, target, and the resulting risk-reward.\n"
                "- Your emotional state: calm, uncertain, excited, frustrated.\n"
                "- Whether you followed your checklist completely.\n\n"
                "At exit: exit price, result in R, and what you would do differently.\n\n"
                "The analysis is where it pays. Monthly, group your trades and ask: which setups "
                "have positive expectancy? What do my losing trades have in common — a particular "
                "market condition, a time of day, a state of mind? What is my process adherence "
                "rate, and how do trades where I followed the plan compare with those where I did "
                "not?\n\n"
                "That last comparison is usually the most instructive thing you will discover. "
                "Most people find their rule-following trades are meaningfully profitable and "
                "their improvised ones are not — and the improvised ones cluster around "
                "identifiable emotional states. That finding is unavailable any other way, and it "
                "is worth more than any further study of patterns.\n\n"
                "Include the trades you did not take but considered. Over time this reveals "
                "whether your filters are protecting you or whether you are systematically "
                "declining your best setups."
            ),
        ),
        homework(
            title="Week 13 homework — audit yourself honestly",
            minutes=12,
            body=(
                "1. Bias inventory.\n\n"
                "Go through the six biases from lesson two. For each, write one specific instance "
                "where you recognise it in your own behaviour — in markets or elsewhere. Vague "
                "answers mean you have not looked. Then write the structural fix you will adopt "
                "for the two that cost you most.\n\n"
                "2. Journal upgrade.\n\n"
                "Extend the journal you started in Module 2 with the full field list from this "
                "module, including emotional state and checklist adherence. Backfill it for your "
                "last five trades as honestly as you can, marking which fields you are "
                "reconstructing rather than remembering.\n\n"
                "3. Write your routines.\n\n"
                "Pre-market, pre-trade, post-trade, weekly, monthly. Attach specific times to "
                "each. Put the weekly review in your calendar as a recurring appointment.\n\n"
                "4. Write your circuit breakers.\n\n"
                "Your daily loss limit, your mandatory break rule, and your physical stop "
                "procedure. Then write the three warning signs that tell you personally that you "
                "are on tilt. Keep this where you will see it while trading.\n\n"
                "5. The uncomfortable exercise.\n\n"
                "Write about your worst financial decision — any decision, not just in crypto. "
                "What state were you in? What would have stopped you? Then check whether the "
                "routines you just wrote would actually have stopped it. If not, revise them."
            ),
        ),
    ],
)
