"""Module 15 — Portfolio Construction, Tax & Your 90-Day Plan."""

from app.modules.courses.curriculum.spec import LessonSpec, ModuleSpec, homework
from app.modules.courses.models import CourseLevel, CoursePhase

MODULE = ModuleSpec(
    slug="portfolio-and-ninety-day-plan",
    title="Portfolio Construction, Tax & Your 90-Day Plan",
    summary=(
        "Putting it together: allocation, rebalancing, a profit-taking framework, yield done "
        "sensibly, record-keeping for tax, and a concrete ninety-day plan to run from here."
    ),
    level=CourseLevel.ADVANCED,
    phase=CoursePhase.PRACTICE,
    lessons=[
        LessonSpec(
            title="Core and satellite",
            minutes=9,
            body=(
                "Portfolio construction is the decision about how much of each thing to hold, and "
                "it explains far more of your eventual result than asset selection does. Getting "
                "the structure right with mediocre picks beats excellent picks in a badly built "
                "portfolio.\n\n"
                "The core-satellite structure is the standard answer, and it works because it "
                "separates two genuinely different activities.\n\n"
                "The core is the majority of your crypto allocation, held in the largest, most "
                "liquid assets, accumulated on a schedule and intended to be held through a full "
                "cycle. It is not traded. Its purpose is exposure to the asset class, and its "
                "defining property is that you will hold it through an 80% drawdown — which means "
                "it has to be sized so that you actually would.\n\n"
                "Satellites are smaller positions in higher-risk assets, each researched with the "
                "template from Module 9 and each sized so that a total loss is genuinely "
                "irrelevant to your outcome. They are where your active work happens, and where "
                "you should expect most of them to fail.\n\n"
                "A common shape is roughly 70–80% core and 20–30% satellites, with no single "
                "satellite above a few percent of the total. The exact numbers matter less than "
                "two properties: the core dominates, and no satellite can hurt you.\n\n"
                "Then there is cash, which most people treat as an absence of a position rather "
                "than a position. It is neither idle nor wasted: it reduces portfolio volatility, "
                "it is the only asset that reliably rises in relative terms during a decline, and "
                "it is what lets you act when prices fall. A meaningful cash weight is the "
                "difference between a decline being an opportunity and a decline being something "
                "that happens to you.\n\n"
                "Write the target weights down. An allocation that exists only as an intention "
                "drifts into whatever the market's last move made it."
            ),
        ),
        LessonSpec(
            title="Deciding your allocation",
            minutes=9,
            body=(
                "How much crypto should you hold at all? This question comes before any question "
                "about which assets, and it is answered from your circumstances rather than from "
                "your market view.\n\n"
                "Work through it in order:\n\n"
                "- Emergency fund first. Several months of expenses in cash, outside any "
                "investment. Crypto held by someone with no buffer will be sold at the worst "
                "possible time, because life will require it.\n"
                "- High-interest debt next. No speculative return is reliable enough to justify "
                "carrying expensive debt against it.\n"
                "- Then your total investable assets, and crypto's share of that. For most people "
                "a single-digit percentage is appropriate; for those with high risk tolerance, "
                "stable income and a long horizon, more can be defensible. The honest test is the "
                "one from Module 1: what could go to zero without changing how you live?\n"
                "- Then the split within crypto: core, satellites, cash.\n\n"
                "Three factors that should genuinely move the number: your time horizon, since "
                "volatility matters less over decades than over months; the stability and "
                "correlation of your income, since someone employed in the sector already has "
                "exposure; and your demonstrated behaviour in a drawdown, which you now have data "
                "on from this programme.\n\n"
                "That last one deserves emphasis. If a small position produced anxiety, that is "
                "information about the right size for you, not a weakness to overcome. The "
                "correct allocation is the one you can hold through the worst case without "
                "abandoning it — a smaller position held through a cycle beats a larger one sold "
                "at the bottom, every time.\n\n"
                "Write your target allocation as percentages, with a date, and note what would "
                "cause you to change it. Then check it against what you actually hold today."
            ),
        ),
        LessonSpec(
            title="Rebalancing",
            minutes=9,
            body=(
                "Rebalancing means periodically returning your portfolio to its target weights. It "
                "sounds like housekeeping and is actually one of the few mechanical processes that "
                "systematically improves outcomes.\n\n"
                "The mechanism is that it forces you to sell what has risen and buy what has "
                "fallen — which is exactly the behaviour that is emotionally hardest and "
                "historically rewarded. It also keeps risk under control: an asset that triples "
                "becomes a far larger share of your portfolio than you chose, and without "
                "rebalancing your allocation is set by the market rather than by you.\n\n"
                "Two approaches, and one of them is better in practice.\n\n"
                "Calendar rebalancing happens on a fixed schedule — quarterly is common. Simple, "
                "and it removes judgment entirely.\n\n"
                "Threshold rebalancing happens when a holding drifts beyond a band, say five "
                "percentage points from target. This is generally more efficient: it acts when "
                "there is something to act on and stays quiet otherwise, producing fewer "
                "transactions and fewer taxable events.\n\n"
                "A hybrid works well: check quarterly, act only if something is outside its "
                "band.\n\n"
                "Practical considerations that matter more than the theory. Each rebalance is a "
                "taxable event in most jurisdictions, so over-frequent rebalancing loses to tax "
                "and fees. Rebalancing with new contributions rather than by selling — directing "
                "new money to whatever is underweight — avoids both, and is the best method "
                "available to anyone still accumulating. And there is a real tension with "
                "momentum: rebalancing out of a strong performer early in a trend reduces returns, "
                "which is why bands should be wide rather than tight.\n\n"
                "Write your rule down, including the bands and the schedule, and follow it. The "
                "value of rebalancing comes entirely from doing it when you least want to."
            ),
        ),
        LessonSpec(
            title="A framework for taking profits",
            minutes=9,
            body=(
                "Most people plan entries in detail and never plan exits. Then the market rises, "
                "they wait for more, it falls, they wait for the recovery, and a substantial gain "
                "becomes nothing. This is the single most common way crypto wealth is not "
                "realised.\n\n"
                "The core problem is that no exit rule feels right in the moment. Selling into "
                "strength feels premature; selling into weakness feels like capitulation. So the "
                "rule has to be written when you have no position at the level in question.\n\n"
                "Approaches that work, and can be combined:\n\n"
                "- Price-target laddering. Decide in advance to sell a defined portion at each of "
                "several levels — for example 20% at each of five levels spaced well apart. You "
                "never sell everything at the top and never sell nothing.\n"
                "- Percentage-based. Take a fixed portion off after any move of a defined size, "
                "which adapts to whatever the market does.\n"
                "- Allocation-based. Sell whatever is required to return a holding to its target "
                "weight. This is rebalancing doing the work, and it requires no price forecast at "
                "all.\n"
                "- Goal-based. Sell when you reach a real-world objective — a defined sum, a "
                "specific purpose. This is underrated: the point of investing is eventually to "
                "have money, not a larger number.\n"
                "- Cycle-based, using the signals from Module 11 to scale exposure down as "
                "conditions become euphoric.\n\n"
                "Two rules that make any of them work. Recover your original capital early — "
                "selling enough to return your initial stake at a substantial gain converts the "
                "remainder into a position that cannot lose you money, and the psychological "
                "effect is large. And always leave something on the table: accept explicitly that "
                "you will not sell the top. Anyone who did was lucky, and planning around luck is "
                "not planning.\n\n"
                "Write the ladder now, with prices, while you have no urgency about them."
            ),
        ),
        LessonSpec(
            title="Yield, staking and lending",
            minutes=9,
            body=(
                "Yield in crypto is real, and it is always compensation for a risk. The discipline "
                "is identifying which risk you are being paid for, and whether the payment is "
                "adequate.\n\n"
                "Where yield genuinely comes from:\n\n"
                "- Staking rewards, paid by the protocol for securing the network. Partly funded "
                "by new issuance, so compare the yield against the inflation rate — a 6% yield "
                "with 5% issuance is a 1% real return, not 6%.\n"
                "- Lending interest, paid by borrowers. Real, and its level tells you about "
                "demand for leverage.\n"
                "- Liquidity provision fees, paid by traders. Real, but accompanied by impermanent "
                "loss — if the two assets in the pool diverge in price, you end up with less value "
                "than simply holding them, and in volatile pairs this frequently exceeds the "
                "fees.\n"
                "- Incentive emissions, paid in newly created tokens to attract capital. This is "
                "not income; it is dilution redistributed, and it stops when the programme "
                "ends.\n\n"
                "The risks you are being paid for: smart contract failure, which has drained "
                "audited protocols; counterparty failure, in the case of centralised lending "
                "products, several of which have taken customer assets to zero; liquidation risk "
                "if the yield involves borrowing; lock-up and unbonding periods during which you "
                "cannot exit; and the risk that the token you are paid in falls faster than the "
                "yield accrues.\n\n"
                "Practical rules. Treat any yield well above the market rate as a signal of risk "
                "rather than opportunity, and identify who is paying it before you participate — "
                "if you cannot, the answer is usually new depositors. Cap total exposure to any "
                "single protocol. Prefer simple, long-established mechanisms over complex ones. "
                "And never take yield on assets you could not afford to lose entirely, because "
                "the failure mode is not a lower return, it is zero."
            ),
        ),
        LessonSpec(
            title="Records and tax",
            minutes=9,
            body=(
                "Tax rules differ substantially by country and change often, so this lesson covers "
                "the structure of the problem and the records you need, not advice for your "
                "jurisdiction. Get that from a qualified professional — the cost is small relative "
                "to the penalties for getting it wrong.\n\n"
                "What is generally taxable is broader than people expect. In most jurisdictions "
                "the events include: selling crypto for fiat, trading one crypto for another "
                "(which surprises people constantly and is the largest source of unexpected "
                "bills), spending crypto on goods, and receiving crypto as income, staking rewards "
                "or airdrops. Moving assets between your own wallets is generally not a taxable "
                "event, but it must still be documented or it looks like a disposal.\n\n"
                "The records you need, for every transaction: date and time, what was disposed of "
                "and what was acquired, quantities, the value in your local currency at the time, "
                "fees, and the venue or wallet. Missing historical price data is the single most "
                "common problem, and it is far harder to reconstruct years later than to record "
                "at the time.\n\n"
                "Practical approach:\n\n"
                "- Use portfolio tracking software that imports from exchanges and wallets, and "
                "set it up now rather than in the year you need it.\n"
                "- Export exchange statements periodically. Venues fail, and their records go with "
                "them.\n"
                "- Keep records of transfers between your own accounts, clearly labelled.\n"
                "- Note the cost basis method your jurisdiction requires and apply it "
                "consistently.\n"
                "- Set aside an estimated tax reserve as you realise gains, in stable value. "
                "People who leave the reserve in crypto and see it fall before the bill arrives "
                "end up owing tax on gains they no longer have — this is a genuinely common and "
                "avoidable disaster.\n\n"
                "Do this from the start. Reconstructing three years of trades across four venues "
                "is a week of misery, and the records are often simply gone."
            ),
        ),
        LessonSpec(
            title="Operational review",
            minutes=8,
            body=(
                "Everything in Modules 2 and 3 decays. Devices change, habits slip, and a security "
                "setup that was sound two years ago may not be now. A scheduled review keeps it "
                "current.\n\n"
                "Twice a year, work through:\n\n"
                "Custody. Where is everything held, and does the split still match the tier plan "
                "from Module 3? Balances drift upward on exchanges without anyone deciding they "
                "should.\n\n"
                "Backups. Are your seed phrase copies where you think they are, legible, and in "
                "separate locations? Test a restore if you have not in a year. Confirm nothing has "
                "become digital.\n\n"
                "Accounts. Review 2FA on every exchange and on the email behind it. Confirm "
                "withdrawal allowlists and time locks are active. Check for old API keys and "
                "revoke any you no longer use — abandoned keys with withdrawal permissions are a "
                "known and quiet risk.\n\n"
                "Approvals. Review token approvals granted to smart contracts and revoke those you "
                "no longer need. This takes ten minutes and closes a real attack path.\n\n"
                "Counterparties. Is any single venue holding more than you would accept losing? "
                "Has anything changed about its standing?\n\n"
                "Documents. Update the inventory and the instructions from Module 3. Confirm "
                "someone appropriate knows the inventory exists.\n\n"
                "Records. Confirm your transaction data is complete and exported.\n\n"
                "None of this is interesting, and all of it protects the returns everything else "
                "in this programme was designed to produce. The pattern worth noticing is that "
                "operational losses are almost always preceded by a period of not looking."
            ),
        ),
        LessonSpec(
            title="The traps, one last time",
            minutes=8,
            body=(
                "A closing checklist of the specific ways people who know better still lose money. "
                "Read it now and again in six months.\n\n"
                "- Position sizes that grow after a winning run, until one loss undoes a year.\n"
                "- Holding a losing position because selling would confirm the loss, while the "
                "capital could have funded a better idea.\n"
                "- Buying something you have not researched because it is rising quickly and "
                "someone confident is talking about it.\n"
                "- Treating a trade that went wrong as a long-term investment.\n"
                "- Leaving large balances on an exchange because moving them is inconvenient.\n"
                "- Chasing yield without identifying who pays it.\n"
                "- Signing transactions you do not understand.\n"
                "- Adding leverage to recover a loss.\n"
                "- Skipping the journal during the period you most need the record.\n"
                "- Concentrating everything into the one asset that has worked recently.\n"
                "- Assuming this cycle will repeat the last one on the same schedule.\n"
                "- Failing to plan an exit, and watching a large gain round-trip.\n"
                "- Not setting aside tax on realised gains.\n"
                "- Acting on urgency someone else manufactured.\n"
                "- Believing that because you have studied, you are exempt from any of the "
                "above.\n\n"
                "That last one is the reason this list exists. Knowledge does not confer immunity; "
                "structure does. Every item here is prevented by something you have already "
                "written during this programme — a sizing rule, a checklist, a circuit breaker, a "
                "storage plan, a profit ladder.\n\n"
                "The difference between the people who keep their gains and the people who do not "
                "is almost never analytical ability. It is whether the rules written in calm "
                "conditions still get followed in uncomfortable ones."
            ),
        ),
        LessonSpec(
            title="Your next ninety days",
            minutes=9,
            body=(
                "Finishing a course produces a temporary sense of capability that fades within "
                "weeks unless it is converted into scheduled action. This lesson is that "
                "conversion.\n\n"
                "Days 1–30: consolidate.\n\n"
                "Finish your trading plan document if any section is still vague. Complete the "
                "security and custody review. Set up your record-keeping properly. Run your "
                "routines daily and weekly without exception. Trade at minimum size or on paper "
                "only — this month is about proving you execute the process, not about returns. "
                "Target: thirty journal entries, and an adherence rate you can measure.\n\n"
                "Days 31–60: measure.\n\n"
                "Continue forward testing at small size. At day 45, run your first full review: "
                "expectancy by setup, adherence rate, and the comparison between rule-following "
                "and improvised trades. Revise your setup criteria based on what your losing "
                "trades had in common — one change only. Complete a research template for one new "
                "asset.\n\n"
                "Days 61–90: scale carefully.\n\n"
                "If your adherence rate is high and your expectancy is positive over a meaningful "
                "sample, increase size — modestly, once, and not by more than double. If it is "
                "not, stay at current size and repeat the previous month. That decision rule is "
                "the point of the whole ninety days.\n\n"
                "Throughout: contribute to your core on schedule regardless of what the market "
                "does, review your macro map monthly, and re-read your Module 1 homework at day "
                "90. Compare what you wrote then with what you believe now.\n\n"
                "Then set the next ninety days. The programme ends; the process does not, and the "
                "results come from the process."
            ),
        ),
        homework(
            title="Final homework — your complete plan",
            minutes=15,
            body=(
                "This is the capstone. It should take an hour and produce documents you will use "
                "for years.\n\n"
                "1. Portfolio construction.\n\n"
                "Write your target allocation: crypto as a percentage of investable assets, then "
                "core, satellites and cash within it, with specific assets and weights. State the "
                "maximum weight for any single satellite. Compare against what you hold today and "
                "write the specific trades that would close the gap.\n\n"
                "2. Rebalancing and profit rules.\n\n"
                "Your rebalancing schedule and bands. Your profit ladder with actual price levels "
                "and the portion sold at each. Your capital-recovery rule.\n\n"
                "3. Tax and records.\n\n"
                "Set up tracking software and import your history. Identify the taxable events in "
                "your jurisdiction and your cost basis method. Decide your tax reserve percentage "
                "and where it will be held.\n\n"
                "4. Operational review.\n\n"
                "Complete every item in the operational review lesson. Schedule the next one for "
                "six months out.\n\n"
                "5. The ninety-day plan.\n\n"
                "Write the three phases with dates in your calendar, including the day-45 review "
                "and the day-90 scaling decision with its explicit criteria.\n\n"
                "6. Look back.\n\n"
                "Re-read your Module 1 homework — your objective, your maximum loss, your "
                "schedule. Rewrite all three with what you now know, and note what changed. Then "
                "file both versions together."
            ),
        ),
    ],
)
