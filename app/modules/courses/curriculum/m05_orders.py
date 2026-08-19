"""Module 5 — Order Types & Trade Execution."""

from app.modules.courses.curriculum.spec import LessonSpec, ModuleSpec, homework
from app.modules.courses.models import CourseLevel, CoursePhase

MODULE = ModuleSpec(
    slug="orders-and-execution",
    title="Order Types & Trade Execution",
    summary=(
        "Every order type you need, what each one costs you, and how to enter and exit positions "
        "without giving away your edge at the point of execution."
    ),
    level=CourseLevel.INTERMEDIATE,
    phase=CoursePhase.MARKET_MECHANICS,
    lessons=[
        LessonSpec(
            title="Market orders and limit orders",
            minutes=8,
            body=(
                "Every order is a choice between certainty of execution and certainty of price. "
                "You cannot have both, and knowing which one you need is most of execution "
                "skill.\n\n"
                "A market order buys or sells immediately at whatever prices are available. You "
                "are guaranteed to be filled and guaranteed nothing about the price. In a deep "
                "book on a calm day the difference is negligible. In a thin book, or during a "
                "fast move, a market order can fill several percent away from where you looked — "
                "and it pays the higher taker fee as well.\n\n"
                "A limit order specifies the worst price you will accept. Buy limits sit at or "
                "below the current price, sell limits at or above. You are guaranteed the price "
                "or better and guaranteed nothing about execution: if the market never reaches "
                "your level, or moves through it faster than your order can be matched, you are "
                "simply not filled. In return you usually pay a lower maker fee.\n\n"
                "The default should be limit orders. Most retail trades are not time-critical, and "
                "the accumulated saving on spread and fees is large over a year. Use market orders "
                "when execution genuinely matters more than a few basis points — closing a "
                "position that has invalidated, or getting out during a fast decline. In those "
                "moments, paying the spread is the cheap option.\n\n"
                "One practical technique: place buy limits a small distance inside the spread "
                "rather than at the top of the book. You may wait longer, but you capture the "
                "spread instead of paying it, and over hundreds of trades that difference is real "
                "money. And always check the estimated fill your interface shows before "
                "confirming — a market order preview that quotes an average price well away from "
                "the last trade is telling you the book is too thin for your size."
            ),
        ),
        LessonSpec(
            title="Stop orders and the gap you cannot avoid",
            minutes=9,
            body=(
                "A stop order is dormant until price touches a trigger level, at which point it "
                "becomes a live order. It is how you automate an exit so that a decision made "
                "calmly is executed without you.\n\n"
                "A stop-market order becomes a market order when triggered. You are certain to "
                "exit; you are not certain at what price. A stop-limit order becomes a limit "
                "order, so you control the price but risk not being filled at all — and the "
                "scenario where a stop-limit fails to fill is precisely the fast collapse you "
                "bought it to protect you from. For risk exits, prefer stop-market. Being out at a "
                "bad price beats being trapped in.\n\n"
                "The hazard both share is slippage past the trigger. Crypto gaps: a sharp move can "
                "jump straight through your level with nothing resting in between, and you fill "
                "well below your stop. This is not a malfunction; it is what happens when "
                "liquidity vanishes. Assume your realised loss can be larger than your stop "
                "implies, and size positions with that in mind.\n\n"
                "Placement matters as much as type. Stops clustered just under obvious round "
                "numbers and obvious support levels are visible liquidity, and price frequently "
                "wicks through them before reversing. Place your stop where your reason for the "
                "trade is actually wrong, not at the nearest tidy number — and if that distance is "
                "uncomfortably large, the answer is a smaller position, not a tighter stop.\n\n"
                "Two more practicalities. Some venues hold stop orders on their own servers "
                "rather than on the book, meaning the stop dies if the exchange has an outage. And "
                "moving a stop further away to avoid being hit is the most expensive habit in "
                "retail trading — it converts a defined loss into an undefined one. Move a stop "
                "toward profit only."
            ),
        ),
        LessonSpec(
            title="Take-profit, OCO and bracket orders",
            minutes=8,
            body=(
                "Exits deserve as much planning as entries, and the reason is behavioural: the "
                "moment you are in a position is the moment you are least able to think clearly "
                "about leaving it.\n\n"
                "A take-profit order is a limit order at your target, resting until reached. "
                "Setting one at entry means the profitable exit happens whether or not you are "
                "watching, and it removes the specific failure of watching a winner give back its "
                "gains while you wait for more.\n\n"
                "An OCO — one cancels the other — pairs a take-profit with a stop-loss. Whichever "
                "triggers first cancels the other automatically. This is the standard way to hold "
                "a position with both a defined risk and a defined reward, and without it you can "
                "end up with an orphaned order that opens a new position by accident.\n\n"
                "A bracket order does the same thing at entry: one submission specifying the "
                "entry, the stop and the target together. If your venue supports it, use it. "
                "Committing to all three at once forces you to state your risk-reward before you "
                "have any emotional stake in the outcome, which is the entire point.\n\n"
                "Two refinements worth adopting. First, scale your take-profit rather than using "
                "one level — for instance, a third at the first target, a third at the second, and "
                "the remainder trailed. This resolves the tension between banking gains and "
                "letting winners run, instead of forcing you to guess which regime you are in. "
                "Second, once the first target fills, move the stop to break-even on the "
                "remainder. From that point the position cannot lose money, which makes it far "
                "easier to hold through noise.\n\n"
                "Check how your venue handles partially filled brackets and whether cancelling one "
                "leg cancels the other. Discovering that behaviour during a fast move is not the "
                "time to learn it."
            ),
        ),
        LessonSpec(
            title="Trailing stops",
            minutes=7,
            body=(
                "A trailing stop follows price at a fixed distance — a percentage or an absolute "
                "amount — moving up as price rises and staying put when it falls. It exists to "
                "solve one specific problem: capturing a large trend without having to guess where "
                "it ends.\n\n"
                "The mechanics: set a 15% trail on a position at 100 and the stop sits at 85. If "
                "price reaches 150, the stop has risen to 127.50. If price then falls, the stop "
                "stays at 127.50 and executes there. You keep most of the move without ever "
                "predicting the top.\n\n"
                "The trade-off is entirely in the distance you choose, and it is a real one. A "
                "tight trail gets shaken out by ordinary volatility — in crypto, 10% pullbacks "
                "inside strong uptrends are routine — and you exit a trend that had much further "
                "to run. A wide trail survives noise but gives back a large portion of the "
                "peak.\n\n"
                "This is why trailing distance should be derived from the asset's own volatility "
                "rather than picked as a round number. A common approach is a multiple of average "
                "true range, which adapts automatically as conditions change. Module 8 covers ATR "
                "properly; the principle is that the same percentage is a very different amount of "
                "room on a stable major and on a small cap that moves 15% a day.\n\n"
                "Trailing stops suit trend-following positions where you have no specific price "
                "target and are trying to stay in as long as the trend persists. They suit "
                "range-bound positions poorly — there, a fixed target at the top of the range is "
                "better, because you already know where you expect the move to stop.\n\n"
                "One caution: not every venue implements trailing stops identically, and some "
                "evaluate them only on candle closes rather than continuously. Read the "
                "documentation on your own exchange before relying on one."
            ),
        ),
        LessonSpec(
            title="Scaling in and scaling out",
            minutes=8,
            body=(
                "Entering a position in one transaction requires you to be right about timing. "
                "Scaling — splitting entry and exit across several orders at different prices — "
                "removes that requirement, and the cost is modest.\n\n"
                "Scaling in means buying in tranches. You might take a third at your initial "
                "level, "
                "a third if price falls to a deeper level you would also be happy to own, and a "
                "third on confirmation that the thesis is working. The benefits are practical: "
                "your average entry improves if price moves against you initially, a single "
                "mistimed entry does not define the position, and psychologically you are far "
                "less likely to panic-sell a position you have not committed fully to.\n\n"
                "There is a discipline that makes this work and an anti-pattern that ruins it. The "
                "discipline is deciding all your levels and total size in advance, so scaling in "
                "is executing a plan. The anti-pattern is averaging down — adding to a loser "
                "because it is cheaper now, with no pre-defined limit. The first is a plan; the "
                "second is a plan dissolving under stress, and it is how small losses become "
                "account-defining ones.\n\n"
                "Scaling out is the mirror image. Sell a portion at your first target to bank a "
                "real gain and reduce risk, another at the second, and let the remainder run with "
                "a trailing stop. You will never exit at the top, but you will never round-trip a "
                "large winner to nothing either, and the second failure is far more common and far "
                "more damaging to your willingness to hold the next one.\n\n"
                "For long-term positions, the same logic applies across months rather than hours: "
                "accumulate on a schedule, distribute into strength on a schedule. Writing the "
                "schedule down while you are calm is what makes it survive the moment when you are "
                "not."
            ),
        ),
        LessonSpec(
            title="Dollar-cost averaging as an execution method",
            minutes=8,
            body=(
                "Dollar-cost averaging means investing a fixed amount at fixed intervals "
                "regardless of price. It is usually presented as a beginner's compromise. It is "
                "better understood as a deliberate execution method with a specific set of "
                "properties.\n\n"
                "What it does well: it removes timing from the decision entirely, which removes "
                "the largest source of behavioural error. A fixed sum buys more units when prices "
                "are low and fewer when high, so your average cost sits below the average price "
                "over the period. It converts investing into a scheduled task, which is the only "
                "form that reliably survives a busy life and a frightening market. And it makes "
                "declines psychologically tolerable — a falling price is your next purchase "
                "improving, not a verdict on your judgment.\n\n"
                "What it does not do: it does not protect you from a bad asset. Averaging into "
                "something in permanent decline simply buys more of a loss. Asset selection still "
                "has to be right, which is what the Analysis phase is for. In a market that rises "
                "steadily throughout, a lump sum invested at the start would also have beaten it — "
                "that is arithmetic, and it is not an argument against a method whose purpose is "
                "limiting the damage of being wrong about timing.\n\n"
                "Practical points that matter more than the theory:\n\n"
                "- Choose an interval you can sustain for years. Weekly and monthly both work; "
                "consistency beats frequency.\n"
                "- Automate it if your venue allows, but check the fees — some recurring-buy "
                "features charge substantially more than placing the order yourself.\n"
                "- Decide in advance how long the programme runs and when you review it, so "
                "stopping is a decision rather than a mood.\n"
                "- Consider a rule to accelerate purchases after large declines. This adds "
                "discretion, so write the trigger down beforehand.\n\n"
                "Most sensible long-term crypto exposure is built this way. It is unexciting, "
                "which is precisely why it works."
            ),
        ),
        LessonSpec(
            title="Time in force, partial fills and order hygiene",
            minutes=8,
            body=(
                "The details around an order determine what happens when the market does not "
                "cooperate, and each one has produced expensive surprises.\n\n"
                "Time in force says how long an order lives. Good-till-cancelled rests until "
                "filled or cancelled — the default for most trading, and the one that needs "
                "housekeeping. Immediate-or-cancel fills what it can right away and cancels the "
                "rest, useful when you want to take available liquidity without leaving a resting "
                "order. Fill-or-kill executes completely or not at all. Post-only rejects the "
                "order if it would execute immediately, guaranteeing maker fees — worth using "
                "whenever you are placing resting orders and want the lower fee.\n\n"
                "Partial fills are normal for larger orders in thin books. The consequences to "
                "watch: your position is smaller than intended, so any stop sized to the full "
                "position is now wrong; and some venues charge per-fill, so a heavily fragmented "
                "order costs more. Always check actual filled quantity rather than assuming.\n\n"
                "Order hygiene is unglamorous and prevents genuine accidents:\n\n"
                "- Review open orders regularly and cancel ones whose reasoning has expired. A "
                "forgotten limit order from three weeks ago can fill into a market you no longer "
                "want to be in.\n"
                "- After any position change, confirm your stops still match the position size.\n"
                "- Know whether your venue reserves margin for open orders, and whether an "
                "unfilled order is quietly limiting your available balance.\n"
                "- Check that closing a position actually cancels its associated orders. An "
                "orphaned stop can open a new short when you thought you were flat.\n\n"
                "Set a recurring five-minute slot to check open orders and positions. Nothing here "
                "generates profit; all of it prevents losses that have nothing to do with your "
                "analysis."
            ),
        ),
        LessonSpec(
            title="An execution checklist",
            minutes=8,
            body=(
                "Execution is where good analysis leaks value. A written checklist run before "
                "every order takes under a minute and eliminates the errors that are pure cost.\n\n"
                "Before submitting:\n\n"
                "- Right asset, right pair, right venue. Confirm the ticker — duplicate and "
                "lookalike tickers are common.\n"
                "- Right direction. Read it aloud if you are tired.\n"
                "- Size checked against your risk rule, not against what looks affordable. Module "
                "12 makes this concrete.\n"
                "- Stop level defined and placed where the idea is wrong.\n"
                "- Target defined, and the resulting risk-reward acceptable before you enter.\n"
                "- Order type chosen deliberately: limit unless there is a reason.\n"
                "- Estimated fill checked against the last traded price.\n"
                "- Total cost estimated — spread plus fees, both directions.\n\n"
                "After submitting:\n\n"
                "- Confirm the fill and the actual average price.\n"
                "- Confirm stop and target are live and sized to the filled quantity.\n"
                "- Log the trade in your journal with the reason, before you know the outcome. "
                "Reasons written afterwards are reconstructions, and they are usually "
                "flattering.\n\n"
                "Two rules that belong on the same card. If you cannot complete the checklist, do "
                "not place the trade — an incomplete checklist is not an obstacle, it is the "
                "answer. And never place an order while feeling urgency: urgency in a market open "
                "every hour of every day is always manufactured, usually by you.\n\n"
                "Keep this beside your screen for the first hundred trades. By then it is a habit, "
                "and habits are what remain when attention runs out."
            ),
        ),
        homework(
            title="Week 5 homework — practise the mechanics",
            minutes=12,
            body=(
                "Use tiny amounts. The point is to make every order type familiar before it "
                "matters.\n\n"
                "1. Place and observe.\n\n"
                "With the smallest size your exchange allows, place: a limit buy below the market "
                "and watch whether it fills; a post-only order and confirm the maker fee; and a "
                "market order, then compare the average fill price with the price you saw when you "
                "clicked. Record all three fees.\n\n"
                "2. Build a bracket.\n\n"
                "Open a small position with a stop-loss and a take-profit attached (OCO or "
                "bracket). Note where you placed the stop and why that level means the idea is "
                "wrong. Leave it running and observe what happens to the other leg when one "
                "triggers.\n\n"
                "3. Compute your risk-reward.\n\n"
                "For that position, write down: entry, stop, target, the distance to each, and the "
                "ratio. Then answer honestly — would you take this trade if you knew you would "
                "only be right 40% of the time?\n\n"
                "4. Write your execution checklist.\n\n"
                "Adapt the checklist from this module to your venue and your style. Keep it to one "
                "screen. Put it where you will actually see it when placing an order.\n\n"
                "5. Order hygiene sweep.\n\n"
                "Review every open order in your account. Cancel anything whose reasoning no "
                "longer applies. Confirm every open position has a stop matching its current size."
            ),
        ),
    ],
)
