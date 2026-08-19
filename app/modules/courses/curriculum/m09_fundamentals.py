"""Module 9 — Fundamental Analysis & Tokenomics."""

from app.modules.courses.curriculum.spec import LessonSpec, ModuleSpec, homework
from app.modules.courses.models import CourseLevel, CoursePhase

MODULE = ModuleSpec(
    slug="fundamentals-and-tokenomics",
    title="Fundamental Analysis & Tokenomics",
    summary=(
        "Judging whether an asset is worth owning at all: supply schedules, value accrual, real "
        "traction, incentives, and the red flags that disqualify a project quickly."
    ),
    level=CourseLevel.INTERMEDIATE,
    phase=CoursePhase.ANALYSIS,
    lessons=[
        LessonSpec(
            title="What fundamental analysis means here",
            minutes=8,
            body=(
                "In equities, fundamental analysis means estimating the cash a business will "
                "produce and comparing it to the price. Most crypto assets have no cash flows and "
                "no claim on any, so importing the framework directly produces nonsense — which is "
                "why some conclude fundamentals do not exist in this market. They do; they are "
                "just different questions.\n\n"
                "The useful ones are:\n\n"
                "- What is this for, and does anyone use it? Real usage, measured in transactions, "
                "active addresses, fees paid or value settled.\n"
                "- Does the token capture any of that value, or is it decorative? This is the "
                "single most important question and the most commonly skipped.\n"
                "- What is the supply schedule, and who is going to sell? Dilution is a headwind "
                "you can measure precisely.\n"
                "- Who controls it, and what are their incentives?\n"
                "- What would have to be true for demand to persist in three years?\n\n"
                "Fundamentals do not tell you what happens next month. Crypto is driven by flows, "
                "narratives and leverage in the short term, and an asset with excellent "
                "fundamentals can fall 80% in a bear market while a worthless one multiplies. What "
                "fundamentals give you is a survival filter and a reason to hold through "
                "drawdowns. Over a full cycle the assets with genuine usage tend to recover and "
                "the ones without tend not to, and the difference between a temporary 80% decline "
                "and a permanent one is entirely a fundamental question.\n\n"
                "The practical output of this module is a repeatable research template. Not a "
                "valuation model — those are largely false precision here — but a structured set "
                "of questions that disqualifies most things quickly and leaves you with a small "
                "number you can defend in writing."
            ),
        ),
        LessonSpec(
            title="Reading the documentation",
            minutes=8,
            body=(
                "Every project publishes material designed to be persuasive. Reading it "
                "productively means knowing which parts are load-bearing and which are "
                "decoration.\n\n"
                "Start with the plainest question: what problem does this solve, and who currently "
                "has that problem? If the answer requires three paragraphs of jargon, that is "
                "usually because there is no crisp answer. Genuinely useful projects can be "
                "described in a sentence.\n\n"
                "Then look for specifics. Vague claims — 'revolutionary', 'next-generation', "
                "'infinitely scalable' — are not statements; they are atmosphere. What you want "
                "are numbers with methodology, named trade-offs, and honest acknowledgement of "
                "limits. A technical document that admits what the design gives up is far more "
                "credible than one that claims to have solved everything, because every real "
                "design gives something up.\n\n"
                "Specific things to extract:\n\n"
                "- The token's role. Precisely what it is required for. If the system would work "
                "identically without it, the token is a fundraising instrument.\n"
                "- The supply schedule and distribution, with percentages and dates.\n"
                "- Governance: who can change what, and how quickly. Look for admin keys, upgrade "
                "authorities and multisig thresholds.\n"
                "- Security assumptions: what has to hold for user funds to be safe.\n\n"
                "Then read outside the project's own material. Look at the code repository — is "
                "there real, ongoing development or a burst of activity around launch? Read "
                "critical analyses, not just supportive ones. Search the project name alongside "
                "'exploit', 'lawsuit' and 'criticism'. And read the community channels: whether "
                "hard questions get answered or the person asking gets attacked is genuinely "
                "diagnostic, and takes five minutes."
            ),
        ),
        LessonSpec(
            title="Tokenomics: supply, emissions and unlocks",
            minutes=9,
            body=(
                "Tokenomics is the economics of the token itself, and it is where the most "
                "avoidable losses in crypto are made — because the information is public, precise, "
                "and routinely ignored.\n\n"
                "Start with the supply picture. Circulating supply is liquid today. Total supply "
                "includes locked tokens. Maximum supply is the eventual cap, if there is one. The "
                "ratio between circulating and total is the first number to check: a project with "
                "15% circulating has 85% of its supply arriving over time, and every one of those "
                "tokens is a potential seller.\n\n"
                "Then the distribution. Who received the initial allocation, at what price, and "
                "with what lock-up? Early investors who paid a tenth of the current price behave "
                "very differently from people who bought on the open market. A distribution where "
                "insiders hold a majority is a structure where your exit liquidity is someone "
                "else's plan.\n\n"
                "Then the schedule. Vesting cliffs release large tranches at once, and prices "
                "frequently weaken into them as the market positions ahead. Unlock calendars are "
                "published; checking the next twelve months takes minutes and changes the timing "
                "of many decisions.\n\n"
                "Then emissions. Many protocols pay ongoing rewards to stakers or liquidity "
                "providers. That is newly created supply. An advertised yield of 20% while supply "
                "inflates 25% annually is a loss dressed as an income. Always compare the yield to "
                "the emission rate.\n\n"
                "Finally, burns and sinks. Some protocols destroy tokens with fees, offsetting "
                "issuance. Whether net supply is rising or falling is calculable, and it matters "
                "more than either figure alone.\n\n"
                "The summary question: if demand stayed exactly constant for two years, what would "
                "the supply schedule alone do to the price? For many assets the honest answer is "
                "'halve it', and that is worth knowing before you buy."
            ),
        ),
        LessonSpec(
            title="Value accrual: does the token capture anything?",
            minutes=9,
            body=(
                "A protocol can be enormously successful while its token goes nowhere. These are "
                "separate questions, and conflating them is the most expensive analytical error in "
                "the sector.\n\n"
                "The question is mechanical: is there a mechanism connecting the protocol's "
                "activity to demand for, or supply of, the token? The real mechanisms are a short "
                "list:\n\n"
                "- Fee burn. A portion of fees destroys tokens, so activity reduces supply. "
                "Directly measurable.\n"
                "- Fee distribution. Revenue paid to stakers or lockers. Check whether it is real "
                "revenue from users or newly issued tokens, because the second is not income.\n"
                "- Required usage. The token must be spent or staked to use the network, creating "
                "structural demand proportional to usage.\n"
                "- Staking for security, where locking tokens removes them from liquid supply and "
                "is paid for by the network.\n"
                "- Collateral demand, where the asset is widely used to back positions "
                "elsewhere.\n\n"
                "And the non-mechanisms, which are presented as though they were:\n\n"
                "- Governance rights alone. The right to vote on parameters has repeatedly proven "
                "close to worthless unless it controls a meaningful treasury or cash flow.\n"
                "- 'The token will appreciate as the ecosystem grows.' This is a hope with no "
                "mechanism attached.\n"
                "- Fee discounts, which cap the token's value at the discount's worth.\n"
                "- Partnerships and integrations, which affect the protocol, not the token.\n\n"
                "The test to apply: write one sentence describing exactly how increased usage "
                "translates into token demand or reduced supply. If you cannot write it without "
                "using the word 'should', there is no mechanism. That does not make the asset "
                "untradeable — plenty of things without value accrual have risen enormously on "
                "narrative — but it does mean you are holding a sentiment position, and it should "
                "be sized as one."
            ),
        ),
        LessonSpec(
            title="Team, funding and incentives",
            minutes=8,
            body=(
                "The people behind a project and how they are paid tell you more about its likely "
                "path than the technology does, because incentives persist after enthusiasm "
                "fades.\n\n"
                "On the team: are they public? Anonymous teams are not automatically fraudulent — "
                "Bitcoin's founder is anonymous — but anonymity removes accountability, and the "
                "base rate for anonymous teams handling user funds is poor. Look for verifiable "
                "history: prior work you can check, code contributed under the same identity, "
                "conference appearances. Then look at whether the people listed are actually still "
                "working on it; advisor sections are frequently decorative, and departures are "
                "rarely announced.\n\n"
                "On funding: who invested, at what valuation, and on what terms? Reputable "
                "investors provide a modest signal of diligence, but their more important role is "
                "as future sellers. An investor who bought at a hundredth of today's price and "
                "whose lock-up expires next quarter is a structural fact about your position, "
                "regardless of what they say publicly.\n\n"
                "On treasury: how much runway does the project have, and in what? A treasury "
                "denominated entirely in its own token is not a runway — it evaporates in exactly "
                "the conditions where it is needed. Treasuries holding stablecoins can fund "
                "development through a bear market; ones holding only their own token generally "
                "cannot.\n\n"
                "On incentives, the questions that matter: does the team's compensation vest over "
                "a period long enough to align them with holders? Do they have the ability to mint "
                "or unlock unilaterally? Have they sold, and did they disclose it?\n\n"
                "The pattern to watch for is a team whose financial outcome is already secured "
                "regardless of what happens next. Once insiders have realised their return, the "
                "energy behind a project tends to decline sharply, and that decline is usually "
                "visible in commit activity months before it is visible in price."
            ),
        ),
        LessonSpec(
            title="Traction: what real usage looks like",
            minutes=9,
            body=(
                "Usage is the closest thing to a fundamental in this sector, and almost all of it "
                "is public. The skill is distinguishing genuine activity from activity "
                "manufactured to look genuine.\n\n"
                "Metrics worth tracking, and how each is gamed:\n\n"
                "- Active addresses. Real signal, but addresses are free to create. Look at trends "
                "over months rather than levels, and be sceptical of spikes coinciding with "
                "reward programmes.\n"
                "- Transaction count. Cheap chains attract automated spam. Weight by value "
                "transferred to see whether transactions are economically meaningful.\n"
                "- Fees paid. The hardest metric to fake, because it costs real money. If users "
                "pay meaningful fees, they are getting something they value. This is the single "
                "best usage metric available.\n"
                "- Total value locked. Widely quoted and widely misleading: TVL rises when the "
                "price of deposited assets rises, and mercenary capital chasing incentives leaves "
                "the moment rewards stop. Look at TVL denominated in a stable unit, and at what "
                "happened when incentives were reduced.\n"
                "- Revenue. Increasingly available from analytics platforms. Compare it to market "
                "cap for a rough multiple, and compare that multiple across similar protocols.\n"
                "- Retention. The most valuable and least published: do users come back? A "
                "protocol whose users are all new every month is not growing, it is churning.\n\n"
                "The core discriminator is whether activity survives the removal of incentives. "
                "Enormous amounts of crypto 'usage' is people farming rewards, and it disappears "
                "the day the rewards do. Look specifically for periods where a project reduced "
                "emissions and check what happened to its metrics — that natural experiment tells "
                "you more than any amount of current data.\n\n"
                "Finally, compare against peers rather than in isolation. A protocol with 20,000 "
                "monthly users means nothing until you know whether the leader has 30,000 or "
                "three million."
            ),
        ),
        LessonSpec(
            title="Competition, moats and the pace of obsolescence",
            minutes=8,
            body=(
                "Crypto is the most competitive software environment that has ever existed. The "
                "code is public, forking is trivial, and users have no switching costs. Any "
                "advantage that can be copied will be, quickly.\n\n"
                "So the question is not whether something works, but what stops the next team from "
                "doing the same thing with better economics. The durable answers are few:\n\n"
                "- Network effects. Liquidity attracts traders, which attracts liquidity. This is "
                "the strongest moat in the sector, and it explains why leading venues stay leading "
                "even when forks offer better terms.\n"
                "- Integration depth. When many other protocols depend on yours, replacing you "
                "means coordinating everyone.\n"
                "- Brand and trust, which take years and cannot be forked. Particularly powerful "
                "for anything holding user funds.\n"
                "- Regulatory position, where licences create genuine barriers.\n"
                "- Genuinely difficult engineering that a small team cannot replicate, though this "
                "erodes faster than teams expect.\n\n"
                "What is not a moat: being first, having a good idea, a partnership announcement, "
                "or a technical benchmark. All of these have been overturned repeatedly.\n\n"
                "Practically, map the competitive set before deciding anything. List the three "
                "closest alternatives, compare usage and fees across them, and check the trend — "
                "is the asset you are considering gaining or losing share? Losing share while the "
                "sector grows is often invisible in absolute numbers and is one of the more "
                "reliable warnings available.\n\n"
                "Also account for obsolescence at the category level. Whole categories have been "
                "displaced within a cycle. Ask what would make this entire category irrelevant, "
                "and whether that is plausible within your holding period. It is a sobering "
                "question, and it correctly disqualifies a great deal."
            ),
        ),
        LessonSpec(
            title="Red flags",
            minutes=9,
            body=(
                "A disqualification list is faster and more reliable than a scoring model. Any one "
                "of these is reason to look much harder; several together is reason to walk away, "
                "and walking away costs nothing.\n\n"
                "On returns and promises:\n\n"
                "- Guaranteed or fixed returns. There is no such thing, and the phrase itself "
                "identifies the scheme.\n"
                "- Yields far above the market with no explanation of where they come from. If you "
                "cannot identify who is paying, the answer is usually new depositors.\n"
                "- Referral rewards for recruiting others, which is the defining structure of a "
                "pyramid.\n\n"
                "On supply and control:\n\n"
                "- Insiders holding a majority of supply, or unclear distribution.\n"
                "- Contracts that can mint unlimited tokens, pause transfers, or blacklist "
                "addresses, controlled by a single key.\n"
                "- Liquidity that is not locked, meaning it can be removed at will.\n"
                "- Large unlocks imminent with no corresponding demand driver.\n\n"
                "On conduct:\n\n"
                "- Marketing that emphasises price over product, and celebrity or influencer "
                "promotion as the primary channel.\n"
                "- Hostility to questions. Communities that ban criticism are managing sentiment, "
                "not building.\n"
                "- Artificial urgency: closing windows, limited allocations, countdowns.\n"
                "- Unverifiable claims of partnerships, audits or users.\n"
                "- Anonymous teams combined with custody of user funds.\n\n"
                "On technicals:\n\n"
                "- No audit, or an audit whose findings were never addressed.\n"
                "- A code repository with little genuine activity outside launch.\n"
                "- A whitepaper that is largely copied, or that describes no mechanism.\n\n"
                "The meta-rule: the presence of urgency plus the absence of verifiable detail is "
                "the signature of every scheme in this sector, from the crudest to the most "
                "sophisticated. Nothing legitimate requires you to decide today."
            ),
        ),
        LessonSpec(
            title="A research template you will actually use",
            minutes=8,
            body=(
                "Research is only useful if it is repeatable and written down. A template forces "
                "you to answer the same questions every time, which is what makes comparisons "
                "meaningful and stops you from researching until you find a reason to buy.\n\n"
                "One page per asset, with these sections:\n\n"
                "- Summary. What it is, in one sentence, in your own words. If you cannot, stop "
                "here.\n"
                "- Usage. Three metrics with current values and their trend over six months.\n"
                "- Tokenomics. Circulating and total supply, next major unlock, annual emission "
                "rate, net supply direction.\n"
                "- Value accrual. One sentence on the mechanism, or an explicit note that there is "
                "none.\n"
                "- Competition. The three closest alternatives and whether share is being gained "
                "or lost.\n"
                "- Team and treasury. Public or anonymous, runway, notable investors and their "
                "unlock dates.\n"
                "- Red flags. From the previous lesson, explicitly listed.\n"
                "- The bear case. Three specific ways this loses most of its value. Written by "
                "you, not sourced from critics.\n"
                "- Thesis. Why demand should exist in three years, in two sentences.\n"
                "- Invalidation. What observable event would make you sell — not a price, an "
                "event.\n\n"
                "That last pair is what separates research from rationalisation. A thesis without "
                "a stated invalidation cannot be wrong, which means it cannot be right either.\n\n"
                "Date every note and revisit quarterly. Compare what you wrote against what "
                "happened. Over a year this becomes the most valuable document you own: not "
                "because the notes were right, but because the pattern of how you are wrong is "
                "consistent and correctable."
            ),
        ),
        homework(
            title="Week 9 homework — research one asset properly",
            minutes=12,
            body=(
                "Pick one asset you already hold or seriously intend to buy. Complete the full "
                "template. Give it an hour of genuine work.\n\n"
                "1. Fill in every section.\n\n"
                "Summary, usage metrics with trends, tokenomics with the next unlock date, value "
                "accrual mechanism, competitive position, team and treasury, red flags, bear case, "
                "thesis, invalidation. Leave nothing blank — 'could not find' is itself a "
                "finding, and an important one.\n\n"
                "2. Do the dilution arithmetic.\n\n"
                "Calculate: with demand exactly constant, what would the next twelve months of "
                "emissions and unlocks do to the price? Write the number.\n\n"
                "3. Write the bear case first, properly.\n\n"
                "Three specific scenarios in which this asset loses 80% and does not recover. If "
                "they feel forced, you have not looked hard enough — every asset has three.\n\n"
                "4. Then decide.\n\n"
                "Having written all of it, state in one sentence whether you would buy it today, "
                "and at what size relative to your maximum loss number from Module 1. If your "
                "answer changed while doing the work, note what changed it.\n\n"
                "5. Set a review date.\n\n"
                "Three months out, in your calendar, with a link to this note. The habit of "
                "revisiting your own reasoning is the one that compounds."
            ),
        ),
    ],
)
