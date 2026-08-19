"""Module 6 — Reading Charts: Candles, Timeframes & Structure."""

from app.modules.courses.curriculum.spec import LessonSpec, ModuleSpec, homework
from app.modules.courses.models import CourseLevel, CoursePhase

MODULE = ModuleSpec(
    slug="reading-charts",
    title="Reading Charts: Candles, Timeframes & Structure",
    summary=(
        "How to read price action honestly: what a candle encodes, how to choose a timeframe, "
        "and how to identify trend and structure without inventing patterns."
    ),
    level=CourseLevel.BEGINNER,
    phase=CoursePhase.MARKET_MECHANICS,
    lessons=[
        LessonSpec(
            title="What charts can and cannot tell you",
            minutes=7,
            body=(
                "A chart is a record of every transaction that has happened, arranged in time. "
                "That is all it is, and being precise about it prevents most of the "
                "disappointment people have with technical analysis.\n\n"
                "What a chart genuinely gives you is a map of where trades have already occurred: "
                "the levels people transacted at, the prices they defended, the areas price moved "
                "through quickly and the areas it lingered. Those are facts, and they matter "
                "because market participants remember their own entries. Someone who bought at a "
                "level and watched it fall often sells when it returns to break-even, which is why "
                "old levels keep producing reactions.\n\n"
                "Charts also encode collective behaviour, which is more stable than any individual "
                "forecast. Fear and greed express themselves in recognisable shapes across every "
                "market and every era, because the participants are always human even when the "
                "orders are automated.\n\n"
                "What a chart cannot do is tell you the future. No pattern has a reliable, "
                "repeatable probability that would survive honest testing; the useful ones shift "
                "the odds modestly, and only when combined with context. A chart also knows "
                "nothing about the thing it describes. It cannot see an insolvency, an exploit or "
                "a regulation, and it will show you a beautiful setup on an asset whose team "
                "disappeared last week.\n\n"
                "So the right framing is this: technical analysis is a decision framework, not a "
                "prediction engine. Its real value is that it gives you objective, pre-defined "
                "levels for entry, invalidation and target — which means you can size risk and "
                "know in advance when you are wrong. That discipline is worth far more than any "
                "individual signal, and it is why the rest of this module focuses on structure "
                "rather than on patterns with impressive names."
            ),
        ),
        LessonSpec(
            title="Reading a candlestick",
            minutes=8,
            body=(
                "Each candle summarises one period — a minute, an hour, a day — using four "
                "numbers: the open, the high, the low and the close. The body spans open to close, "
                "and the wicks reach out to the extremes.\n\n"
                "Colour convention is arbitrary; the information is in the shape.\n\n"
                "A long body means one side dominated the whole period and price closed far from "
                "where it opened. Conviction. A small body means the period ended near where it "
                "began — indecision, regardless of how far price travelled in between.\n\n"
                "Wicks are where the real information usually is. A long lower wick means price "
                "fell during the period and was bought back before the close: sellers tried and "
                "were rejected. A long upper wick means the reverse. A candle with a small body "
                "and a long wick in one direction is a statement that the market visited a price "
                "and refused it.\n\n"
                "Three things beginners routinely get wrong:\n\n"
                "- The close matters more than the extremes. Price touching a level intraday and "
                "closing back inside is very different from closing beyond it. Most level-based "
                "rules should use closes for exactly this reason.\n"
                "- A candle only means something in context. A long lower wick after a sustained "
                "decline into a level people care about is meaningful. The same candle in the "
                "middle of a range is noise.\n"
                "- Candle boundaries are arbitrary. A daily candle closes at midnight in whatever "
                "timezone your chart uses, and crypto never closes, so a 'daily close' is a "
                "convention rather than an event. Different platforms will show you slightly "
                "different candles for the same day.\n\n"
                "Get comfortable reading candles as a record of a fight between buyers and "
                "sellers, and where each of them gave up. That reading transfers to every setup "
                "in the next two modules."
            ),
        ),
        LessonSpec(
            title="Timeframes, and looking at more than one",
            minutes=8,
            body=(
                "The same asset looks bullish on one timeframe and bearish on another, and both "
                "readings can be correct. Timeframe is not a detail — it defines the question you "
                "are asking.\n\n"
                "The rule that resolves most confusion: your timeframe should match your holding "
                "period. If you intend to hold for months, your decisions belong on the weekly and "
                "daily charts, and the 15-minute chart is noise that will talk you out of a good "
                "position. If you are trading over hours, the daily gives you context and the "
                "hourly gives you entries. Trouble almost always comes from mismatching the two: "
                "entering on a five-minute signal and then holding for weeks because it went "
                "against you, or exiting a long-term position because of an intraday wobble.\n\n"
                "The standard approach is three timeframes:\n\n"
                "- A higher timeframe for direction. Where is the trend, and where are the levels "
                "that matter?\n"
                "- Your trading timeframe for the setup. Is a recognisable structure forming near "
                "one of those levels?\n"
                "- A lower timeframe for execution. Where exactly do I enter, and where is the "
                "invalidation tight enough to size properly?\n\n"
                "A common ratio is roughly four to six times between each: weekly, daily, "
                "four-hour; or daily, four-hour, one-hour.\n\n"
                "The discipline that makes this work is that the higher timeframe has authority. "
                "If the daily trend is down, a bullish hourly pattern is a counter-trend trade "
                "and should be treated as one: smaller, faster, with a tighter target. Most "
                "losing trades are lower-timeframe setups taken against a higher-timeframe trend, "
                "because the setup looked clean in isolation. Always zoom out before committing — "
                "it costs ten seconds and it prevents the majority of avoidable losses."
            ),
        ),
        LessonSpec(
            title="Trend and market structure",
            minutes=9,
            body=(
                "Trend is the most useful single read on a chart, and it can be defined "
                "objectively rather than by how the chart feels.\n\n"
                "An uptrend is a sequence of higher highs and higher lows. Each advance exceeds "
                "the previous peak and each pullback stops above the previous trough. A downtrend "
                "is lower highs and lower lows. When neither holds — highs and lows overlapping "
                "within a band — you have a range, and ranges are where most time is spent.\n\n"
                "The value of defining it this way is that it gives you a falsifiable statement. "
                "In an uptrend, the trend remains intact until a pullback breaks below the "
                "previous higher low. That break is a change of structure, and it is the earliest "
                "objective evidence the trend has ended. You are no longer guessing about tops; "
                "you have a level that either holds or does not.\n\n"
                "This gives you a simple framework:\n\n"
                "- In an uptrend, buy pullbacks toward the previous higher low or a level that "
                "held before, with invalidation below that low.\n"
                "- In a downtrend, sell rallies into previous lower highs — or, if you do not "
                "short, simply stay out. Not participating is a position.\n"
                "- In a range, trade toward the edges and expect the middle to be noise, or wait "
                "for the range to resolve.\n\n"
                "Two refinements worth knowing. A break of structure on high volume that then "
                "holds is far more convincing than one that immediately reverses back inside — the "
                "second is a failed break, and failed breaks often produce sharp moves the other "
                "way. And trend exists per timeframe: a downtrend on the four-hour inside an "
                "uptrend on the daily is normal, and is exactly the pullback the daily trend "
                "trader is waiting for.\n\n"
                "Mark structure before you look at anything else. Every indicator in the next "
                "module is more useful when you already know which of the three states you are in."
            ),
        ),
        LessonSpec(
            title="Support, resistance and the levels that matter",
            minutes=9,
            body=(
                "Support is a price area where buying has previously been sufficient to stop a "
                "decline; resistance is where selling has stopped an advance. They are areas, not "
                "lines, and treating them as precise prices is the most common way people misuse "
                "them.\n\n"
                "Why they work is behavioural, not magical. Traders remember their own entries. "
                "People who bought at a level and are underwater sell to break even when price "
                "returns. People who missed a move place orders where they wish they had bought. "
                "Stop orders cluster just beyond obvious levels. The level matters because orders "
                "sit there — which is also why levels stop working once those orders are gone.\n\n"
                "Not all levels are equal. The ones worth marking share these qualities:\n\n"
                "- Multiple touches, with a clear reaction each time.\n"
                "- Formed on high volume — real transactions, not a thin wick.\n"
                "- Visible on a higher timeframe. A weekly level outranks an hourly one.\n"
                "- Recent enough that participants still remember it, though major levels can "
                "persist for years.\n\n"
                "The most useful behaviour is the flip: broken resistance frequently becomes "
                "support, and vice versa. Sellers who defended a level and were overwhelmed often "
                "become buyers on the retest. A retest of a broken level, holding, is one of the "
                "highest-quality entries available, and it comes with an obvious invalidation.\n\n"
                "Practical discipline: mark levels on the higher timeframe before you look for "
                "trades, and mark few. A chart with twenty lines is a chart that will justify any "
                "decision you want to make. Three to five levels that genuinely produced reactions "
                "are worth more than a full screen. And expect overshoots — price frequently "
                "pushes through a level to trigger stops before reversing, which is why "
                "invalidation should sit beyond the noise, not on the line itself."
            ),
        ),
        LessonSpec(
            title="Volume at price, and where the market spent time",
            minutes=8,
            body=(
                "Standard volume tells you how much traded in each period. Volume-at-price — often "
                "shown as a horizontal profile beside the chart — tells you how much traded at "
                "each price, which is a different and frequently more useful question.\n\n"
                "The shape of that profile identifies two kinds of area. High-volume nodes are "
                "prices where a great deal changed hands: the market spent time there and many "
                "participants have positions from that area. These act as magnets and as "
                "congestion — price tends to return to them and tends to get stuck in them. "
                "Low-volume nodes are prices the market moved through quickly, where few positions "
                "exist. Price often traverses these fast in both directions, because there is "
                "little to slow it down.\n\n"
                "This gives you three practical reads:\n\n"
                "- Expect deceleration approaching a high-volume node and acceleration through a "
                "low-volume gap. Targets set inside a thin area are often reached quickly; targets "
                "set inside a thick one are often not reached at all.\n"
                "- The point of control — the single price with the most volume — is a reference "
                "the market repeatedly gravitates to. Its position relative to current price tells "
                "you whether recent trade has been accepted above or below the bulk of "
                "positioning.\n"
                "- The edges of a high-volume area often make better levels than the exact highs "
                "and lows, because that is where agreement ended.\n\n"
                "A related idea is the value area: the range containing roughly 70% of the volume. "
                "Price accepted inside it suggests balance; price rejected from its edge and "
                "returning inside suggests the attempted move failed.\n\n"
                "You do not need to become a volume-profile specialist. Simply knowing where the "
                "market has done most of its business, and where it has done almost none, "
                "improves target and stop placement immediately."
            ),
        ),
        LessonSpec(
            title="Chart patterns worth knowing",
            minutes=9,
            body=(
                "Patterns are shorthand for a story about supply and demand. They are worth "
                "learning for the story, not the shape — a pattern you cannot explain in terms of "
                "who is buying and who is trapped is a pattern you will misuse.\n\n"
                "Continuation patterns describe a pause inside a trend. A flag is a shallow "
                "counter-trend drift after a strong move: profit-taking without genuine reversal. "
                "A triangle is a compression where each swing is smaller, meaning one side is "
                "progressively giving ground; the direction of the eventual break usually follows "
                "the prevailing trend. Both resolve most convincingly on expanding volume — a "
                "break on falling volume is the common failure.\n\n"
                "Reversal patterns describe a trend failing. A double top is a second attempt at a "
                "high that fails, confirming when the intervening low breaks. A head and "
                "shoulders is three attempts where the last is weaker than the middle one, "
                "confirming on a close below the neckline. What both really encode is a "
                "structural break: buyers could not make a higher high, and then lost the previous "
                "low.\n\n"
                "Two honest caveats. First, patterns are far less reliable than their presentation "
                "suggests, and published success rates rarely survive out-of-sample testing. Treat "
                "them as one input, weighted by context — a head and shoulders at a major weekly "
                "resistance after an extended run is worth attention; the same shape mid-range is "
                "not. Second, humans are extremely good at seeing patterns that are not there. If "
                "you have to squint or redraw the lines to make it work, it is not a pattern.\n\n"
                "The practical value of a pattern is that it hands you a specific invalidation "
                "level and a measurable target. That is what makes a trade sizeable. If a setup "
                "does not give you both, it is an opinion rather than a plan."
            ),
        ),
        LessonSpec(
            title="Candlestick signals in context",
            minutes=8,
            body=(
                "A handful of individual candles are worth recognising, provided you remember they "
                "only mean something at a level that already matters.\n\n"
                "A pin bar — small body, long wick — shows an attempted move that was rejected. At "
                "the low of a decline into support, a long lower wick says sellers pushed and "
                "buyers took the whole move back within the period. That is a genuine change in "
                "the balance of pressure.\n\n"
                "An engulfing candle completely covers the previous candle's body and closes "
                "beyond it. It says one side not only won the period but reversed the previous "
                "one entirely. Bullish engulfing at support after a sequence of weak candles is "
                "among the more useful single-candle signals.\n\n"
                "An inside bar sits entirely within the previous candle's range: compression, a "
                "pause, often preceding an expansion. Traders use the break of the outer candle's "
                "range as a trigger.\n\n"
                "A doji — open and close nearly equal — is indecision. After a long trend it can "
                "mark exhaustion; in the middle of a range it means nothing at all.\n\n"
                "The rules that make these useful rather than dangerous:\n\n"
                "- Location first. The signal must occur at a level you identified beforehand. A "
                "pin bar in open space is not a trade.\n"
                "- Confirmation second. Wait for the close, and preferably for the next candle to "
                "act consistently.\n"
                "- Volume third. A reversal candle on unremarkable volume is a weak claim.\n"
                "- Timeframe matters. A daily signal outranks a five-minute one substantially.\n\n"
                "One more thing worth internalising: a signal gives you a defined invalidation — "
                "beyond the wick — which is what makes it tradeable. If you find yourself unable "
                "to say where the signal would be proven wrong, you have seen a shape rather than "
                "a setup."
            ),
        ),
        LessonSpec(
            title="How chart reading goes wrong",
            minutes=8,
            body=(
                "The failure modes are consistent, and knowing them by name is the fastest way to "
                "catch yourself in one.\n\n"
                "Confirmation bias. You want an asset to go up, so you find the bullish reading. "
                "The antidote is procedural: before you take any position, write the best case "
                "against it. If you cannot construct one, you do not understand the trade.\n\n"
                "Indicator stacking. Adding indicators until they agree. Most indicators are "
                "derived from the same price series, so agreement is not confirmation, it is "
                "repetition. Two or three genuinely different inputs are worth more than eight "
                "correlated ones.\n\n"
                "Timeframe shopping. Cycling through timeframes until one supports the position "
                "you already want. Decide your timeframe first, from your holding period, and "
                "read it honestly.\n\n"
                "Redrawing. Moving a trendline because price broke it. Once a level is invalidated "
                "it is information, not an inconvenience to be edited away.\n\n"
                "Hindsight. Every pattern is obvious after it resolves. The only honest test is "
                "marking your read on a chart before the outcome — which is exactly what the "
                "journal exists for.\n\n"
                "Over-precision. Treating a level as a single price, entering at exactly that "
                "number and placing a stop a hair beyond it. Levels are zones; noise around them "
                "is normal; a stop inside the noise will be hit even when you were right.\n\n"
                "Trading without invalidation. If you cannot state the price at which your idea is "
                "wrong, you have no plan and cannot size the position. This single omission "
                "accounts for more damage than every misread pattern combined.\n\n"
                "Notice that all seven are process failures rather than analytical ones. That is "
                "the actual lesson of the module: the analysis is the easy part."
            ),
        ),
        homework(
            title="Week 6 homework — mark up a real chart",
            minutes=12,
            body=(
                "Do this on a charting platform with drawing tools, and save your work — you will "
                "compare it against what actually happened in Module 14.\n\n"
                "1. Structure.\n\n"
                "Choose one liquid asset. On the daily chart, mark the last six months of swing "
                "highs and swing lows. Label the current state: uptrend, downtrend or range. Write "
                "the specific price at which that classification would change.\n\n"
                "2. Levels.\n\n"
                "Mark no more than five horizontal levels that produced clear reactions. For each, "
                "note how many times it was touched and whether volume was elevated there. Delete "
                "anything you cannot justify.\n\n"
                "3. Multi-timeframe read.\n\n"
                "Write three sentences: what the weekly says, what the daily says, what the "
                "four-hour says. If they disagree, state which one you would act on given a "
                "one-month holding period, and why.\n\n"
                "4. A written prediction.\n\n"
                "In two sentences, state what you expect over the next two weeks and — this is the "
                "important half — what price would prove you wrong. Date it. Do not change it "
                "later.\n\n"
                "5. Review your candles.\n\n"
                "Find one long-wicked candle at a level you marked. Write what happened in that "
                "period in terms of buyers and sellers, and what happened next."
            ),
        ),
    ],
)
