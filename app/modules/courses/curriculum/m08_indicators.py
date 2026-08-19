"""Module 8 — Indicators, Momentum & Volatility."""

from app.modules.courses.curriculum.spec import LessonSpec, ModuleSpec, homework
from app.modules.courses.models import CourseLevel, CoursePhase

MODULE = ModuleSpec(
    slug="indicators-and-momentum",
    title="Indicators, Momentum & Volatility",
    summary=(
        "The small set of indicators worth using, what each one actually measures, and how to "
        "combine them without stacking eight views of the same number."
    ),
    level=CourseLevel.INTERMEDIATE,
    phase=CoursePhase.ANALYSIS,
    lessons=[
        LessonSpec(
            title="What an indicator is, and what it is not",
            minutes=7,
            body=(
                "Every indicator is a formula applied to price and volume. It contains no "
                "information that was not already in the chart; it reorganises what is there so a "
                "particular property becomes easier to see.\n\n"
                "That single fact resolves most of the arguments about indicators. They cannot "
                "predict, because they are computed from data that has already happened. They lag "
                "by construction — an average of the last twenty closes cannot tell you anything "
                "about the twenty-first. And adding more of them does not add information, because "
                "they share their inputs.\n\n"
                "What they do usefully is make comparisons objective. 'Momentum is weakening' is a "
                "feeling; 'RSI made a lower high while price made a higher high' is a fact you can "
                "test, journal and apply consistently. Indicators also normalise across assets and "
                "time — a reading of 70 means the same thing on any chart, which lets you build "
                "rules rather than impressions.\n\n"
                "Three principles for using them well:\n\n"
                "- Price first, indicator second. If the indicator says one thing and structure "
                "says another, structure wins. The indicator is derived from price, not the "
                "reverse.\n"
                "- Fewer is better. Two or three indicators measuring genuinely different "
                "properties — trend, momentum, volatility — beat eight measuring momentum.\n"
                "- Understand the formula. If you do not know what an indicator computes, you "
                "cannot know when it will mislead you, and every indicator has conditions where it "
                "reliably does.\n\n"
                "Finally, be sceptical of optimised settings. A parameter tuned to produce "
                "beautiful signals on past data is describing that data, not the market. Default "
                "settings have one genuine advantage: enough participants watch them that they "
                "carry a small self-fulfilling weight."
            ),
        ),
        LessonSpec(
            title="Moving averages",
            minutes=9,
            body=(
                "A moving average is the mean price over the last N periods, redrawn each period. "
                "Its job is to strip short-term noise so the underlying direction is legible.\n\n"
                "Simple moving averages weight every period equally. Exponential moving averages "
                "weight recent periods more, so they respond faster and whipsaw more. Neither is "
                "better; faster suits shorter holding periods.\n\n"
                "The period length is the real decision, and it should follow your timeframe. "
                "Short averages (10–20) track swings. Medium (50) is the standard trend reference "
                "for swing trading. Long (200) describes the primary trend and is watched widely "
                "enough that it produces reactions on its own.\n\n"
                "Four practical uses:\n\n"
                "- Trend filter. Price above a rising 200-period average is an uptrend by "
                "definition. Many traders take long setups only in that condition, and that single "
                "filter improves most strategies by removing counter-trend trades.\n"
                "- Dynamic support and resistance. Strong trends often pull back to a specific "
                "average repeatedly, giving pullback entries with obvious invalidation.\n"
                "- Crossovers. A short average crossing a long one signals a change in trend — "
                "reliably late, and prone to repeated false signals in ranges. Useful as "
                "confirmation, poor as a trigger.\n"
                "- Extension. Price a long way from its average is stretched and tends to revert. "
                "Measuring that distance in percentage terms gives you an objective "
                "over-extension read.\n\n"
                "The failure mode is universal and worth stating plainly: moving averages work in "
                "trends and generate constant false signals in ranges, which is where markets "
                "spend most of their time. Always establish which regime you are in — from "
                "structure, not from the average — before acting on one."
            ),
        ),
        LessonSpec(
            title="RSI and momentum oscillators",
            minutes=9,
            body=(
                "The Relative Strength Index compares the size of recent gains to recent losses "
                "and expresses the result from 0 to 100. It measures the character of momentum, "
                "not the direction of price.\n\n"
                "The conventional reading — above 70 overbought, below 30 oversold — is the least "
                "useful thing about it, and acting on it mechanically is one of the more reliable "
                "ways to lose money. In a strong uptrend RSI can sit above 70 for weeks while "
                "price doubles. 'Overbought' means momentum is strong, which in a trend is a "
                "reason to stay in, not a reason to sell.\n\n"
                "The genuinely useful readings:\n\n"
                "- Divergence. Price makes a higher high while RSI makes a lower high: the new "
                "extreme was achieved with less force. This is the most valuable RSI signal, and "
                "it gets its own lesson later in this module.\n"
                "- Range shifts. In an uptrend, RSI tends to find support around 40–50 and reach "
                "70+; in a downtrend it caps around 50–60 and reaches 30. Where RSI stops "
                "retracing to tells you which regime you are in, often before price structure "
                "confirms it.\n"
                "- Failure swings. RSI turning back down without reaching its prior high indicates "
                "momentum is not being restored.\n"
                "- Extremes in ranges. In a genuine range, 70 and 30 do work as boundaries — the "
                "conventional reading is fine, provided you have first established that you are "
                "ranging.\n\n"
                "Standard settings use 14 periods. Shorter is more sensitive and noisier. Other "
                "oscillators — stochastic, CCI, Williams %R — measure similar things with "
                "different formulas; running several is repetition, not confluence. Pick one, "
                "learn its behaviour on the assets you trade, and use it consistently."
            ),
        ),
        LessonSpec(
            title="MACD",
            minutes=8,
            body=(
                "MACD measures the distance between two exponential moving averages, usually 12 "
                "and 26 periods, then plots a 9-period average of that distance as a signal line. "
                "The histogram shows the gap between the two.\n\n"
                "What it actually captures is the rate of change of the trend. When the fast "
                "average pulls away from the slow one, momentum is accelerating; when they "
                "converge, it is fading. It is a trend indicator expressed as momentum, which is "
                "why it behaves differently from RSI.\n\n"
                "The readings worth using:\n\n"
                "- The zero line. MACD above zero means the fast average is above the slow one — "
                "the trend is up. Crossings of zero are slower and more meaningful than signal "
                "line crossings.\n"
                "- Signal line crossovers. The traditional trigger. Frequent, and unreliable "
                "alone; useful as confirmation of something structure already suggested.\n"
                "- Histogram direction. The histogram shrinking while price still advances is "
                "early evidence the move is losing force — often the first visible sign, before "
                "any crossover.\n"
                "- Divergence, exactly as with RSI.\n\n"
                "MACD's weakness is inherited from its inputs: it is built from moving averages, "
                "so it is late, and it produces continuous whipsaw in sideways markets. It is at "
                "its best on higher timeframes in trending conditions, where its lag matters less "
                "and its signals are fewer.\n\n"
                "A note on using it alongside RSI: both are momentum measures, so treating "
                "agreement between them as confluence overstates your evidence. If you want a "
                "second opinion, take it from a different domain — volume, structure, positioning "
                "— rather than from a second oscillator."
            ),
        ),
        LessonSpec(
            title="Bollinger Bands and volatility regimes",
            minutes=8,
            body=(
                "Bollinger Bands plot a moving average with bands two standard deviations above "
                "and below. Because standard deviation is a volatility measure, the bands widen "
                "when the market is moving and contract when it is quiet.\n\n"
                "The most common misuse is treating a touch of the upper band as a sell signal. In "
                "a strong trend price walks along the band for extended periods; selling every "
                "touch means fighting the trend continuously. A band touch says 'this move is "
                "large relative to recent volatility', which is a description, not an "
                "instruction.\n\n"
                "The genuinely useful readings:\n\n"
                "- The squeeze. Bands contracting to an unusually narrow width means volatility "
                "has compressed. Volatility is mean-reverting — quiet periods are followed by "
                "active ones — so a squeeze indicates an expansion is coming. It says nothing "
                "about direction, which is exactly why it pairs well with a structural read that "
                "does.\n"
                "- Band width as a regime indicator. Comparing current width to its own history "
                "tells you whether you are in a quiet or violent period, which should change your "
                "position sizing and your stop distances.\n"
                "- Walking the band as trend confirmation. Repeated closes outside the band in one "
                "direction indicate a genuinely strong trend rather than an extreme.\n"
                "- Failure to reach the opposite band on a pullback, indicating the trend is "
                "holding.\n\n"
                "The underlying idea is more important than the indicator: volatility clusters and "
                "cycles. Calm follows storm and storm follows calm. Most traders think only about "
                "direction, but sizing a position without knowing the current volatility regime is "
                "how a normally sensible position becomes an oversized one — which is the subject "
                "of the next lesson."
            ),
        ),
        LessonSpec(
            title="ATR and sizing to volatility",
            minutes=8,
            body=(
                "Average True Range measures how much an asset typically moves in a period, "
                "including gaps. It has no directional content whatsoever, which is what makes it "
                "one of the most practically valuable numbers on a chart.\n\n"
                "Its first use is stop placement. A stop closer than one ATR from entry will "
                "usually be hit by ordinary noise regardless of whether your idea was right. "
                "Placing stops at a multiple of ATR — commonly 1.5 to 3 — beyond your structural "
                "invalidation adapts automatically: wider when the market is violent, tighter when "
                "it is calm. This solves the problem of a fixed percentage stop being far too "
                "tight in one regime and far too loose in another.\n\n"
                "Its second use is position sizing, and this is where it changes outcomes. If you "
                "risk a fixed fraction of capital per trade and your stop is set from ATR, then "
                "position size falls automatically as volatility rises. You take smaller positions "
                "in wild conditions and larger ones in quiet conditions, without having to make a "
                "judgment call in the moment. Module 12 works through the arithmetic.\n\n"
                "Its third use is target setting. A target three ATR away is a very different "
                "proposition from one half an ATR away, and expressing both risk and reward in ATR "
                "terms makes setups comparable across assets. A 5% move on a stable major and a 5% "
                "move on a small cap are not the same event.\n\n"
                "It also gives you an honest reality check. Multiply daily ATR by your position "
                "size and you have the amount your position will typically move in a day. If that "
                "figure is uncomfortable to read, the position is too large — that discomfort is "
                "information, and it is much cheaper to receive it now than at 3 a.m."
            ),
        ),
        LessonSpec(
            title="Volume indicators",
            minutes=8,
            body=(
                "Volume is the one input that is not derived from price, which makes volume-based "
                "indicators genuinely additive rather than repetitive.\n\n"
                "Volume moving average. The simplest and most useful: plot an average of volume "
                "and compare each bar to it. This converts 'high volume' from an impression into a "
                "measurement, and it is the filter that separates real breakouts from noise.\n\n"
                "On-Balance Volume. Adds volume on up periods and subtracts it on down ones, "
                "producing a cumulative line. Its value is in divergence: if price makes a new "
                "high but OBV does not, the advance is not supported by participation.\n\n"
                "VWAP — volume-weighted average price. The average price weighted by volume, "
                "usually over a session. Institutions use it as an execution benchmark, which "
                "gives it real behavioural weight: price above VWAP means buyers since the anchor "
                "point are in profit. Anchored VWAP, started from a significant event such as a "
                "major low or a listing, is particularly useful because it tells you the average "
                "cost of everyone who has traded since something that mattered.\n\n"
                "Money flow measures combine price and volume into an oscillator, essentially RSI "
                "weighted by volume.\n\n"
                "The principles that make these usable:\n\n"
                "- Rising price on rising volume is confirmation; rising price on falling volume "
                "is a warning.\n"
                "- Volume spikes at extremes often mark exhaustion — the last participants acting "
                "at once.\n"
                "- Breakouts without volume expansion fail at a much higher rate.\n\n"
                "One caveat specific to crypto: reported volume varies in quality by venue, and "
                "some is fabricated. Prefer aggregated data from sources that filter, or use "
                "volume from the specific venue you trade on."
            ),
        ),
        LessonSpec(
            title="Divergence",
            minutes=9,
            body=(
                "Divergence occurs when price and a momentum indicator disagree about the strength "
                "of a move. It is the most useful signal that oscillators provide, and it is worth "
                "learning precisely because it is easy to see incorrectly.\n\n"
                "Bearish divergence: price makes a higher high, the oscillator makes a lower high. "
                "The new peak was reached with less momentum than the previous one — buyers are "
                "still winning, but with less force. Bullish divergence is the mirror: a lower low "
                "in price with a higher low in the oscillator, meaning selling pressure is "
                "diminishing even as price makes a new extreme.\n\n"
                "What divergence actually tells you is deceleration, not reversal. A car "
                "decelerating is still moving forward. This is why divergence used as a standalone "
                "entry signal performs poorly: in strong trends it appears repeatedly and resolves "
                "by the trend simply continuing. Traders who short every bearish divergence in a "
                "bull market lose consistently, and the pattern looked correct every time.\n\n"
                "How to use it properly:\n\n"
                "- As a warning, not a trigger. Divergence is a reason to tighten stops, take "
                "partial profits, or decline to add — not a reason to reverse.\n"
                "- With location. Divergence at a major higher-timeframe level is a serious "
                "signal; divergence mid-range is noise.\n"
                "- With confirmation. Wait for a structural break — a lower low after bearish "
                "divergence — before acting on it. This costs you part of the move and removes "
                "most of the false signals.\n"
                "- On higher timeframes. Daily and weekly divergences are far more meaningful than "
                "intraday ones, which appear constantly.\n\n"
                "One honest caution: divergence is easy to see in hindsight and easy to imagine in "
                "real time. Mark the two peaks you are comparing explicitly, and require them to "
                "be comparable swings rather than any two points that support your view."
            ),
        ),
        LessonSpec(
            title="Building a chart you can actually read",
            minutes=8,
            body=(
                "The final skill in this module is subtraction. A chart carrying eight indicators "
                "will produce a signal for any decision you feel like making, which means it "
                "produces no discipline at all.\n\n"
                "A working setup needs one indicator per question, and there are only three "
                "questions:\n\n"
                "- What is the trend? A moving average, or simply marked structure.\n"
                "- Is momentum supporting it? One oscillator, RSI or MACD, not both.\n"
                "- What is the volatility regime? ATR, or Bollinger band width.\n\n"
                "Plus volume, which is a separate input rather than a derived one, and a small "
                "number of marked levels.\n\n"
                "That is the whole chart. Everything else should be removed, and the removal is "
                "not aesthetic — each additional indicator increases the probability that "
                "something on screen agrees with whatever you already want to do.\n\n"
                "Practical workflow:\n\n"
                "- Save a template so every chart opens identically. Consistency across assets "
                "makes comparison possible and makes anomalies visible.\n"
                "- Keep separate templates per timeframe if your settings differ, rather than "
                "adjusting on the fly.\n"
                "- Do the higher timeframe read first, always, before looking at your trading "
                "timeframe.\n"
                "- Mark levels once per week rather than continuously, so your levels are not "
                "drawn to justify today's idea.\n\n"
                "A useful test: screenshot your chart and ask whether someone else could state "
                "your read from it in one sentence. If the answer is buried under indicator "
                "panels, the chart is working against you. The goal is a chart that makes it "
                "obvious when there is no trade — because most of the time, there is not."
            ),
        ),
        homework(
            title="Week 8 homework — strip the chart down and measure",
            minutes=12,
            body=(
                "1. Build your template.\n\n"
                "Create one chart layout with at most: one moving average, one oscillator, ATR or "
                "band width, and volume. Save it as your default. Delete everything else. Apply it "
                "to three assets and confirm it is readable on all of them.\n\n"
                "2. ATR reality check.\n\n"
                "For the asset you hold or intend to hold, find the daily ATR and express it as a "
                "percentage of price. Then calculate: if I held a $5,000 position, how much would "
                "it typically move in a day? Write the number down. Then write whether that figure "
                "is comfortable.\n\n"
                "3. Hunt divergence honestly.\n\n"
                "On the daily chart of one asset, find three historical divergences. For each, "
                "mark the two swings you are comparing and record what happened next — reversal, "
                "continuation, or nothing. Note how many resolved as a reversal.\n\n"
                "4. Volume filter test.\n\n"
                "Find five breakouts on a daily chart. Record whether volume on the break exceeded "
                "its 20-period average, and whether the breakout held a week later. Look at the "
                "relationship.\n\n"
                "5. Write your indicator rules.\n\n"
                "Two sentences per indicator on your template: what it measures, and what you will "
                "and will not do based on it. Add these to your setup catalogue from Module 7."
            ),
        ),
    ],
)
