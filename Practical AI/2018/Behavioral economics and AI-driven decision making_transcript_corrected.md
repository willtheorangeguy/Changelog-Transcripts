[0.00 → 6.70] Bandwidth for Changelog is provided by Vastly. Learn more at Fastly.com. We move fast and fix
[6.70 → 11.42] things here at Changelog because of Rollbar. Check them out at Rollbar.com. And we're hosted
[11.42 → 17.66] on Linde servers. Head to linode.com slash Changelog. This episode of Practical AI is
[17.66 → 23.28] brought to you by Hired. One thing people hate doing is searching for a new job. It's so painful
[23.28 → 28.32] to search through open positions on every job board under the sun. The process to find a new
[28.32 → 33.94] job is such a mess. If only there was an easier way. Well, I'm here to tell you there is. Our
[33.94 → 38.64] friends at Hired have made it so that companies send you offers with salary, benefits, and even
[38.64 → 44.04] equity up front. All you have to do is answer a few questions to showcase who you are and what type
[44.04 → 48.90] of job you're looking for. They work with more than 6,000 companies from startups to large publicly
[48.90 → 53.88] traded companies in 14 major tech hubs in North America and Europe. You get to see all of your
[53.88 → 58.88] interview requests. You can accept, reject, or make changes to their offer even before you talk
[58.88 → 62.68] with anyone. And it's totally free. This isn't going to cost you anything. It's not like you have
[62.68 → 66.52] to go there and spend money to get this opportunity. And if you get a job through Hired, they're even
[66.52 → 70.46] going to give you a bonus. Normally it's $300, but because you're a listener of Practical AI,
[70.82 → 75.74] it's $600 instead. Even if you're not looking for a job, you can refer a friend and Hired will send
[75.74 → 81.48] you a check for $1,337 when they accept the job. As you can see, Hired makes it too easy.
[81.48 → 84.72] Get started at Hired.com slash Practical AI.
[97.92 → 103.32] Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[103.76 → 109.26] productive, and accessible to everyone. This is where conversations around AI, machine learning,
[109.26 → 113.38] and data science happen. Join the community and snag with us around various topics of the show
[113.38 → 119.22] at changelog.com slash community. Follow us on Twitter. We're at Practical AI FM. And now onto the show.
[123.62 → 130.46] Well, this is Daniel, a data scientist creating AI for good. And I'm joined here by Chris Benson,
[130.70 → 136.80] my co-host, who's a digital transformation strategist, which is very exciting. How are you doing,
[136.80 → 143.94] Chris? Doing great today. How's it going, Daniel? It's going well. And speaking of strategy,
[143.94 → 150.84] I think you're going to really like today's guest. We have Mike Regime with us today. And when I met
[150.84 → 156.06] Mike, I was really intrigued by his story. First, some of the things that he's worked on in the
[156.06 → 163.12] past, but also just the experience in kind of guiding a company all the way through the process
[163.12 → 170.62] of kind of defining and implementing data analytics and AI strategy within the company. And so today,
[170.80 → 176.68] we're going to talk to him about all of those things. So the culture of AI and the operations of AI
[176.68 → 182.66] and, you know, strategy around that and when and how you can find AI use cases. So I think it's going
[182.66 → 188.58] to be really great. Welcome, Mike. Hello. Yeah. So why don't you tell us a little bit about yourself?
[188.58 → 196.96] So hello, I'm Mike Regime. I'm an all-around data evangelist and a consultant working with
[196.96 → 201.84] organizations, trying to help them find value in this wonderful asset that everybody's so excited
[201.84 → 209.92] about, working with them with identifying AI solutions, working machine learning problems and
[209.92 → 214.94] so forth. And all of them seem to be really interested in building some fascinating algorithm for
[214.94 → 221.02] them and the whole spectrum of AI. And formerly, before I started working as a consultant,
[221.50 → 227.72] I was the chief analytics officer for justgiving.com, a UK-based company that also happens to be
[227.72 → 235.06] the world's largest online social giving platform. Oh, wow. That's amazing. So I know I wasn't super
[235.06 → 241.24] familiar with just giving, but it's really large, right? I think we're bigger than a lot of people
[241.24 → 247.82] sort of initially think. We are a for-profit organization that operates in the non-profit space.
[248.60 → 254.66] And so to date, they've raised more than $3 billion for great causes out there. I suppose I should
[254.66 → 258.94] explain a little bit about how it works for the audience because it might not be so familiar.
[259.34 → 266.24] So just getting started in around the year 2000, 2001, essentially what they are is a digitized form
[266.24 → 271.28] of the paper form that we used to take around when we were doing an event for charity. So let's say we
[271.28 → 275.76] were running the marathon for charity. We would take a paper form to our colleagues and our friends
[275.76 → 281.18] and say, would you sponsor me for this particular charity that I'm running for? I may be running for
[281.18 → 286.34] Cancer Research UK, for example. I've picked that because someone in my family has been affected by
[286.34 → 291.82] cancer, and I'm really passionate about them eradicating the disease. So I take this paper form and I go
[291.82 → 295.98] around to different people, and they sponsor me. Some people would say they'll give you a pound a mile,
[296.24 → 301.76] some people just throw in 50 quid, which is 50 pounds, or even more than that. And then companies
[301.76 → 306.62] tend to match that as well. So if you raise 500 pounds, companies will also add 500 pounds to that
[306.62 → 311.84] form. And what Just Giving did is quite ingeniously actually, is they took that paper form and they
[311.84 → 316.78] digitized it so that they could reach effectively more people. As we were becoming a much more connected
[316.78 → 322.26] world, digitally at least, we were able to take that form and spread it around to lots of other people
[322.26 → 325.86] who would then come onto that new page, which we called a fundraising page.
[325.86 → 331.38] And they'd be able to donate directly to your page, and then you'd raise the money for charity
[331.38 → 336.58] and then do the event. And that was, if you like, the mainstay of the organization. As we
[336.58 → 345.78] progressed into late 2014, 2013, around that time, we also started building a sort of individual giving
[345.78 → 350.40] platform where people could raise money for whatever course they wanted. So it didn't have to be a formal
[350.40 → 357.04] charity. It would be things like, let's say, someone needed to travel to South America to see
[357.04 → 362.56] their grandmother before she passed and needed to raise funds to for the plane ticket, for example.
[362.80 → 366.64] And they'd create the same page, reach out to their friends, their friends would come and donate,
[366.96 → 371.92] their friends or people they knew. And then that individual would be able to take that those funds
[371.92 → 376.16] and carry out the for good mission that they had initially raised the money for.
[377.20 → 383.76] That's awesome. It's great to hear about how Just Giving has really empowered that sort of
[383.76 → 390.08] giving. I know you can only reach so many people giving them a physical form, right?
[390.08 → 390.32] Yeah.
[390.32 → 396.24] But our digital networks are so much larger now. So that's so great.
[396.24 → 401.44] It is also one of those ideas that you think, well, why didn't I think of that? It's so simple
[401.44 → 407.60] in the concept, but it works so well. And as I said, they've raised more than $3 billion for
[408.16 → 411.60] perfect causes today. Yeah. Very exciting.
[411.60 → 412.64] That's awesome.
[412.64 → 413.20] That's amazing.
[413.20 → 420.16] You, uh, I've, I've seen you, uh, post some, some stuff, uh, related to, uh, to animal charities
[420.16 → 422.64] and stuff. Chris, you'll have to look into this.
[422.64 → 427.04] Oh, you just, yeah, you just piqued my interest when I'm not talking AI and data science.
[427.84 → 429.68] I'm all about animal advocacy. So,
[429.68 → 430.72] Oh, great. Great.
[430.72 → 431.52] That's awesome. Yeah.
[431.52 → 434.16] Well, you, now you have, now you have Just Giving.
[434.16 → 440.00] Exactly. Exactly. And, and, and, and, well, I think one of the great things about that is, uh,
[440.00 → 445.20] it, it really, uh, begins to democratize the whole idea of giving, you know, moving on from
[445.20 → 449.28] the traditional ways that haven't changed very much, to be honest, where, uh, charities would
[449.28 → 455.12] sort of solicit, uh, ask requests from individuals, or you have the what we call huggers on the street
[455.12 → 460.00] who are walking around with those tins asking for money here. It's really connecting people to the
[460.00 → 465.68] causes that they care about, and then also connecting people to other people. So it's, uh, some really
[465.68 → 470.48] interesting AI concept, AI use cases, if you like, that come out of that as well.
[470.48 → 471.92] Yeah. Looking forward to talking about those.
[471.92 → 476.88] Yeah. Yeah. That's, that's awesome. I'd be interested to hear just a few more details on
[476.88 → 481.84] that front as far as, because this will, I think, give some context for the rest of our conversation
[481.84 → 488.08] in terms of, you know, when you came on with Just Giving and how it's grown, if it's, you know,
[488.08 → 491.76] international at this point, I know you've been, I think it was acquired, right?
[491.76 → 492.16] Yes.
[492.16 → 498.16] Um, so kind of how, how, when you came on and what the state was then versus kind of now and
[498.16 → 504.00] how it's grown in terms of like the markets that it's in and size and, and all of that.
[504.00 → 512.24] Uh, yeah. So I think we, we, I joined in 2010 and at that point, I would say, uh, the organization
[512.24 → 517.68] was very much in its infancy in regard to how they would work with data. They had a lot of the
[517.68 → 521.92] traditional elements in place in terms of having a data warehouse and collecting
[521.92 → 526.00] some of the information, but culturally there was a long way that they needed to go.
[526.00 → 531.76] It was a team of one when I joined, which was essentially myself with the founders main objective
[531.76 → 535.76] saying they've got this valuable data, and it is a valuable data set. If you think about it, you've
[535.76 → 541.92] got in excess of 20 million individuals from more than, you know, uh, a hundred or so different
[541.92 → 547.44] countries that have, uh, very clearly stated that they're interested in a particular cause.
[547.44 → 552.72] And more importantly, they've also said why. So for example, I'm, I'm doing this for prostate
[552.72 → 557.28] cancer because of what my grandfather went through or something like that. Uh, or I'm
[557.28 → 560.88] from a particular country where there's been an earthquake. So you can see there's a clear
[560.88 → 566.96] relationship. So millions of people, uh, connecting to thousands, uh, hundreds of thousands of causes
[566.96 → 571.44] telling us why they've connected to those causes. And then you have an additional million people
[571.44 → 576.32] coming to support those causes and leaving, or those individuals leaving comments that give us
[576.32 → 581.36] an even greater indication of other people that might be interested in those causes or
[581.36 → 585.84] why they're supporting you. It's just a breadth of information that was just sat there in that
[585.84 → 594.08] database. Yeah, that's crazy. It seems like that is like, as a data person that really excites me. And then
[594.08 → 600.40] also I definitely see how you could leverage it for, for good purposes and, and also for somewhat nefarious
[600.40 → 606.16] purposes as well. Yeah. Sadly, that's true with almost any, any, any organization or any data set.
[606.16 → 609.76] It's, uh, that ethical boundary of, uh, what do you actually use it for?
[610.56 → 615.20] Yeah. So, so that begs the question, especially given the fact that you've been there as long as you
[615.20 → 621.44] have. So, you know, when you're coming into the organization, and you're trying to, to drive the
[621.44 → 627.20] decision-making process based on data at the organization and build that up, um, how you go about
[627.20 → 631.28] doing that, what, what is the best way to proceed? Can you kind of share some of your experience there?
[631.28 → 636.96] Sure. Yeah, absolutely. And I will start by saying with difficulty and, uh, that's,
[636.96 → 643.52] that's not just a good disclaimer. And that's not just for, you mean there's, there's not a secret sauce.
[643.68 → 650.80] Well, actually, so, um, I've, I've put together what I believe to be a secret formula that helps us,
[650.80 → 654.08] uh, helps organizations understand how they can generate value from,
[654.08 → 657.68] Oh yeah. Is this, uh, you're, you're writing a book, right?
[657.68 → 659.60] Indeed. Yes. Um, and, uh,
[659.60 → 663.44] Ah, tell, before you jump into Chris's question, tell us a little bit about your book. I'd love to
[663.44 → 663.60] hear.
[663.60 → 667.84] Sure. I actually think the book help is, is aligned to Chris's question. So I'll sort of
[667.84 → 672.48] put them all together in, in, and bunch them all in my response just now, but the, the book is called
[672.48 → 678.32] solving the data puzzle primarily because, uh, it is, it's different for every organization,
[678.32 → 684.00] um, but it has an end state picture and end state game, but it has many pieces that need to be put
[684.00 → 689.04] down in a specific order sometimes in order for you to eventually get the picture that you're after.
[689.60 → 694.96] And I think the nuances are very, very important, like the shapes of the jigsaw puzzle pieces and so
[694.96 → 699.36] forth. So that's what the title of the book is called. And essentially what it does is it highlights
[699.36 → 705.60] the simplifies the whole problem that we have in the data space and simplifies it to five keys that
[705.60 → 712.08] you need in order to truly begin to see value from data. And this is built from both my experience
[712.08 → 718.24] at Just Giving and the organizations I worked in prior to that, as well as, um, fortunately at Just Giving,
[718.24 → 723.28] just as an aside, I, um, had the opportunity to consult with a lot of other organizations at the
[723.28 → 727.60] same time. I had a perfect relationship with the founders of Just Giving that enabled me to do that.
[727.60 → 733.84] And, um, as part of that got to test this, these five keys to see what was required to be
[733.84 → 738.40] successful and also working with some of the larger organizations out there, such as the likes of
[738.40 → 744.64] Facebook and, and, uh, um, uh, Google and so forth, working with individuals at those, at those
[744.64 → 751.52] organizations to really begin to just see what's, what's working, uh, for them. And, uh, um, and it
[751.52 → 755.76] all comes down to those five ingredients essentially. So I think the question, if you, Chris, do your mind
[755.76 → 761.36] reminded me what that question was that you had asked earlier? Sure. Just kind of, as you are coming into
[761.36 → 765.68] the organization, you're trying to figure out the best way to, to build and drive a culture
[765.68 → 770.56] of good decision-making that's based on the data that you're collecting. How do you go about that
[770.56 → 776.08] process? Great. So I think where you started is, is, is a real indication of some of the problems that
[776.08 → 781.68] we, we suffer commercially. Let's say, um, you, you immediately said, how do we get into,
[781.68 → 785.60] I'll just sort of paraphrase, how do we get into the habit of good decision-making within an organization?
[785.60 → 790.80] The first task that I had was to get the organization to understand that decision-making
[791.84 → 797.76] was an area that we needed to focus on. So the things that happen with data is people get very
[797.76 → 802.32] excited about what it can do. And we hear a lot of, you know, like we hear about Facebook's edge
[802.32 → 806.96] rank and Google's page rank, get very excited about this sort of things. And you're, you begin
[806.96 → 811.68] looking for, okay, what's, what's our big algorithm that we're going to talk about? And in, in just giving,
[811.68 → 816.56] we ended up coining it give rank, which is, you know, not very creative, but you know,
[816.56 → 820.72] you just get a lot of people just excited about what algorithm can we build forgetting,
[820.72 → 825.60] just completely forgetting that the main use case for data, and it'd be useful to see if you can
[825.60 → 831.52] challenge this main use case for data, whether you're playing with data science or AI is for
[831.52 → 837.52] decision-making, right? And decision-making beyond just your organization, it's internal decision-making
[837.52 → 841.52] and external decision-making. Take, for example, the two algorithms that I talked about,
[841.52 → 848.56] Facebook's edge rank, it's, its purpose is to decide what content to show in order to maximize
[849.20 → 857.04] the chances of somebody coming back or enjoying their time on, on, on Facebook or Google's page rank.
[857.84 → 864.24] That addresses the decision of what content should I serve or return based on the query that was sent.
[864.24 → 869.84] So these are decisions that we could do manually, but they've been automated and had some mathematical
[869.84 → 875.28] algorithm placed on top of them. So with data, data's main use case being decisions, you can now
[875.28 → 878.96] begin to see that organizations that need to take some time to try and understand, well, what, what are
[878.96 → 885.44] the key decisions we have within our product, within our operations internally, or even with the users that
[885.92 → 888.00] use the product? Am I making any sense there?
[888.00 → 888.40] Yeah.
[888.40 → 889.04] Total sense.
[889.04 → 889.36] Yeah, definitely.
[889.76 → 894.24] And not only that, but I, I, when you talk about whether that could be challenged,
[894.24 → 899.52] I don't think it can. I think it really comes down to, to decision-making can occur in different types
[899.52 → 904.64] of contexts, whether, whether it's, you know, supporting humans or whether it's automating a decision or
[904.64 → 909.68] whatever. But I, I don't think that, I think that your, your, your basis is, is really firm there.
[909.68 → 916.56] Yeah. And I think that part of my struggle in the past at a, at a couple of places where I've worked
[916.56 → 923.12] is maybe, you know, I, I can get people to the point of thinking about the decisions that they
[923.12 → 929.52] make on a daily basis, maybe in sales or, or in operations or whatever it is, but I have a harder
[929.52 → 937.44] time motivating them to understand that those decisions can be augmented or even, you know,
[937.44 → 945.68] levelled up in some way by, by data. They, they kind of have this kind of mindset that they,
[945.68 → 952.36] they have the knowledge in their head to make the decisions, but they have a harder time kind of
[952.36 → 958.92] crossing into that realm of understanding how, how data or algorithms actually interface with those
[958.92 → 963.36] decisions. Could, could you kind of comment on that? And if that's something you've seen as well,
[963.36 → 965.42] or, or am I totally?
[965.42 → 968.42] No, no, no, no. You've hit the nail on the head there. I think that's a see,
[968.50 → 973.86] the most interesting thing about data is that the, the individuals that tend to be the experts at it
[973.86 → 979.88] are also the individuals that are poorest at interacting with people. Right. And, uh,
[979.88 → 985.08] and the whole problem really here is it's a people problem, not a data problem. Right. Um,
[985.08 → 991.38] what you've described there is the natural human tendency to overestimate or, or give more credibility
[991.38 → 996.88] to their own opinions, right. Uh, which is fraught with biases. I mean, there are hundreds of books
[996.88 → 1002.54] that are written on that right now. You can look at Daniel Kahneman or Dan Ariely, people who talk
[1002.54 → 1007.52] about the, the frailties in human decision-making, right. Where, where we're just surrounded by so
[1007.52 → 1012.96] many natural biases. I think there's over 120 different cognitive biases that influence our
[1012.96 → 1016.98] decision-making. And I play a lot of tricks on some of the audiences when I'm speaking to them,
[1016.98 → 1022.36] you know, I, I do like, there's one that I do, for example, I would ask people, uh, does the
[1022.36 → 1029.50] population of Rwanda, small African country, is that bigger or smaller than, um, 80 million?
[1029.78 → 1035.80] Right. And you see naturally there, what I'm playing with is, is anchoring. And, uh, uh, most people
[1035.80 → 1041.24] would give an answer that isn't too far away from 80 million either side. Right. But the population
[1041.24 → 1046.90] may actually be less than 10, but because I've said 80, they're anchored on, on that. So we have a lot
[1046.90 → 1051.26] of those things that humans making correct decisions with. So what we did at Just Giving,
[1051.40 → 1054.84] interestingly, was we spent a lot of time on behavioural economics, spent a lot of time in
[1054.84 → 1058.70] just bringing the organization up to speed and understanding the frailties in human decision
[1058.70 → 1065.06] making. So that, that's a pretty new term to me. Could you explain kind of what behavioural economics,
[1065.06 → 1070.38] um, kind of entails? Yeah, it's a it's a it's a field. I, I'm not too sure when, when it began,
[1070.38 → 1074.76] but the, the, the sort of key names when you type in behavioural economics are people like Dan Ariely
[1074.76 → 1082.02] and Daniel Kahneman that looks at human beings as irrational beings. So whereas if you look at
[1082.02 → 1086.44] economics and the, the decision-making from an economic standpoint, it looked as human beings
[1086.44 → 1091.22] as very rational beings who were always seeking to maximize payoff with each of the decisions that
[1091.22 → 1096.90] they made. But I think as research continued to, to carry on, uh, they found that we weren't always
[1096.90 → 1102.42] behaving that way, and we were actually behaving almost irrationally. And it was because of these sort
[1102.42 → 1107.38] of biases that came into, into play. Just like with the, the example that I gave you, because I said
[1107.38 → 1112.90] 80 million, most people were anchored at, at that number, right? Which is a bit irrational because a
[1112.90 → 1117.70] rational, a rational econ, if you like, would have thought through a different process. They wouldn't
[1117.70 → 1122.52] have been nudged by that number, but we are human beings and this is how this just works. Right. And so
[1122.52 → 1127.24] the field of behavioural economics, I believe came into play to try and understand research and explain
[1127.24 → 1133.52] how we are nudged or, um, how, um, how those biases affect our decision-making.
[1133.68 → 1138.90] Yeah. It's, it's been really popular lately. I've, I've read a bit on it, uh, recently, and I know it's,
[1138.98 → 1144.70] it's very much on the rise and trying to kind of fix some of the, uh, the, the fallibility and,
[1144.70 → 1149.42] and traditional economic thought. Um, but I think it's pretty fascinating that you had the foresight
[1149.42 → 1154.68] to bring it into the organization and, and train people, uh, in the field, uh, enough so that they could,
[1154.68 → 1158.06] uh, they could get the benefit of it. I think one of the things that I would say it did,
[1158.12 → 1162.66] and this wasn't deliberate, but it seems to have, have, have, have worked is I find in a lot of
[1162.66 → 1167.88] organizations, whilst people get very excited about data, there are a lot of people who get very
[1167.88 → 1173.12] nervous about it as well, because you'll be looking at as a date scientist, you look at data in a way
[1173.12 → 1177.92] that no one else has looked at before. You're able to find things that people haven't seen before.
[1177.92 → 1183.72] And therefore you're, you're, you're challenging things with an example is imagined going to a CRM
[1183.72 → 1190.14] manager who's been, whose job it is to send emails to an audience to try and get them to come back to
[1190.14 → 1194.68] your platform. Let's say for example, and the traditional methods for that are using things
[1194.68 → 1200.46] like recency, frequency, and monetary values as a simple equation. And then you come up to them and
[1200.46 → 1205.92] you say, well, I have an algorithm that can, has a 90% improvement on your approach and in bringing
[1205.92 → 1211.56] people back. And they'd be like, well, I've been 20 years in the game. So why would I listen to some
[1211.56 → 1216.88] mathematical formula that, you know, it becomes a very personal thing for some people. So you have
[1216.88 → 1221.34] that human challenge of them being threatened by data as well as being excited by data.
[1222.14 → 1228.00] Yeah. So that, that's actually leads right into what I was just thinking, which was what kind of
[1228.00 → 1236.54] strategy can you put into place to express to people their kind of built-in irrational thought,
[1236.54 → 1245.10] while at the same time, not negating their, their, uh, you know, background and their expertise and,
[1245.10 → 1249.24] you know, giving them, giving them some light at the end of the tunnel that this is going to,
[1249.54 → 1252.42] you know, this is actually going to improve what you're doing. You're going to be able to make,
[1252.42 → 1258.32] you know, more sales or whatever it is versus just kind of, um, you know, telling them that
[1258.32 → 1262.94] they're irrational, which maybe they are, but you know, probably no one likes to hear it.
[1262.94 → 1269.04] That's a high wire act right there. I think the, the example, so a lot of the examples we were,
[1269.12 → 1276.18] we were giving them was the interplay between, uh, gut, uh, gut driven, or a gut informed decision,
[1276.58 → 1282.02] experience informed decision, and a data informed decision. And what we did is not only did we show
[1282.02 → 1287.80] the frailties of human gut making decisions, but we also showed the frailties of data because data
[1287.80 → 1292.62] itself is also limited. It's, it's, it's limited by the data that's captured. You can add
[1292.62 → 1296.60] 10 more data sources to an algorithm, and suddenly it'll give you a very different answer.
[1297.06 → 1301.54] You can just add more data of the same, uh, um, labels that you had previously,
[1301.54 → 1306.64] and you will also get a different answer. So data as well has its problems. So what we were trying to
[1306.64 → 1313.06] do was look for the balance, essentially the balance that is not fully leaning on either side.
[1313.06 → 1317.62] So it's not fully data driven, and it's not fully gut based driven, but it's really a combination
[1317.62 → 1323.58] of the two. It's how we understand and are, um, aware of our, let's say the things that don't work
[1323.58 → 1328.90] very well in human decision-making and where data can supplement and improve that. But at the same
[1328.90 → 1333.56] time, not neglecting their gut and experience, because we as human beings, interestingly enough,
[1333.56 → 1339.02] are one of the best data machines out there. We take data from a range of sources, not just our five
[1339.02 → 1343.86] sensors. I think there, there talk, there's people who talk about a whole range of sensors. I think in
[1343.86 → 1348.50] excess of, in excess of 10, I think I've read where, you know, take for example, how you can
[1348.50 → 1354.00] close your eyes and still point at your nose. That's a sense that, uh, is, is it's not touched.
[1354.10 → 1357.62] It's not taste. It's not any of those, but it's some sort of directional sense that we have
[1357.62 → 1362.82] automatically. Right. So we, we, we're perfect data machines. So we shouldn't ignore our gut
[1362.82 → 1367.02] at all. And that was a big message that we were saying is that listen, there's something in that
[1367.02 → 1372.76] because we probably captured more data than the machines have, um, for now. Um, so it was getting that
[1372.76 → 1379.90] balance, right? Yeah. So would you say that like in, in, in that light, a good guiding principle
[1379.90 → 1387.86] is to kind of frame things for people in the sense of, you know, augmenting their valuable capabilities
[1387.86 → 1394.62] rather than, you know, replacing everything that, that they've done. Right. But, um, but kind of
[1394.62 → 1401.60] utilizing their, their amazing capabilities, their, their skill, their background, but augmenting them to,
[1401.60 → 1406.84] you know, make them more, more effective or bring new things to light or, or whatever that might be
[1406.84 → 1413.04] is, is that, uh, an okay way to frame it? Yeah. I wish we, we, we had your, um, language to begin
[1413.04 → 1417.96] with. It might've made things, the journey smoother. Um, yeah. Augmenting, I think is the way you should
[1417.96 → 1423.46] say it because there you're, you're giving credit to, uh, to their own decision-making rather than
[1423.46 → 1428.66] dismissing it. And all you're saying is you, you, you bring something to the table, but what we want to do
[1428.66 → 1434.22] is enhance it. So how do you, when, when you're considering that, and you're kind of educating
[1434.22 → 1440.28] them, uh, and getting them into the right, uh, mode of thinking about, about this, um, and,
[1440.38 → 1447.36] and bringing those practices into the organization's culture and accounting for the fact that you have,
[1447.36 → 1453.14] uh, behavioural econ, and then you have more of the traditional data strategy. How do you build a
[1453.14 → 1459.92] strategy out of all of these desperate parts into a coherent message that everybody can understand
[1459.92 → 1467.18] and follow with? Yeah, that's a that's a fantastic question. And you, you'll see there that you,
[1467.18 → 1471.60] one of the things about data is that a good friend of mine describes it as a team sport.
[1471.74 → 1477.24] The data team alone cannot do that. The strategy needs buy-in from the entire organization.
[1477.48 → 1482.42] It's one of the reasons why I think I always push for the lead of the, the data team to be part of the
[1482.42 → 1487.62] exec team because they need to span across the, the entire organization. But, um, uh, in order to
[1487.62 → 1491.12] develop the strategy, there are several things you need. Firstly, you need to make sure you understand
[1491.12 → 1495.76] the organizational strategy. And by that, I mean, you need to know the, the objectives of the
[1495.76 → 1501.70] organization, this, the boundaries of scope and the approach. And usually those sorts of organizational
[1501.70 → 1506.90] strategies are hidden in rim reams and reams of documentation. And you've got to just try and
[1506.90 → 1513.52] simplify it because data also needs an objective to work, work towards. So when building the strategy,
[1513.52 → 1518.18] the first thing that we did was make sure that we could disseminate the organizational, uh, strategy
[1518.18 → 1524.00] into a sentence that everybody could understand. And also that, you know, could be easy. It could,
[1524.10 → 1529.38] we could work very easily with data. So it was a little more discreet in its numbers. It had very
[1529.38 → 1535.54] clear numerical objectives, a timeline for it, which it was working with a bounded scope. So it wasn't just
[1535.54 → 1541.32] any free idea, uh, and, uh, um, and also a clear advantage that we were using. So for example,
[1541.32 → 1545.54] at just giving the advantage that we had is that we had millions of causes on the site,
[1545.54 → 1549.44] you know, so, and nobody else had that. So we had to work with that piece of content,
[1549.44 → 1554.04] you know, rather than just coming up with something arbitrary at the time. So getting the business
[1554.04 → 1558.06] strategy right was one of the most critical things we needed to do in order to get the data strategy.
[1558.28 → 1562.28] It was then from there that we went on to start looking at the possible use cases.
[1562.28 → 1567.32] And those use cases were really disseminating those decisions. As I said, to try and understand
[1567.32 → 1572.84] what are the decisions we're making operationally, for example, sending an email about a new
[1572.84 → 1577.50] campaign. Let's say there was an earthquake, and they were like, for example, we had the, uh,
[1577.50 → 1582.46] earthquake in Haiti a while ago, you know, so who exactly are we going to send that email to?
[1582.60 → 1586.58] Because every time you send an email, as with any decisions, there are trade-offs. So
[1586.58 → 1590.18] something happens, you send the email, there are people who will unsubscribe.
[1590.18 → 1594.58] That means there are fewer people available for us to email for the next cause. So we needed to be
[1594.58 → 1598.46] personal. So we needed, that was a decision that we had to make. Who do we send that email to?
[1598.58 → 1603.64] And that's where we could apply AI. So that helps with the use cases. And then also looking at the
[1603.64 → 1608.10] decisions that are being made externally by, by our audience. So when someone comes onto the site,
[1608.10 → 1612.62] are they deciding how much they want to give? Are they deciding who they want to give to?
[1612.82 → 1618.56] Are they making a decision on whether they want to come just read or absorb content? So trying to
[1618.56 → 1623.24] understand those and support those decisions. Uh, and the last thing actually, so I said the
[1623.24 → 1628.80] strategy, uh, the use cases. So the last thing in the data strategy was, um, understanding where you
[1628.80 → 1633.96] are as an organization. So, uh, looking at it on almost two spectrums. The first spectrum is what
[1633.96 → 1638.56] capabilities do we have to develop any of these data solutions? Are we at the stage where we can only
[1638.56 → 1643.08] say what's happened and why it's happened, or can we build, build algorithms that can predict what's
[1643.08 → 1647.60] happening and even prescribe? And the second spectrum was, we were looking at was, um, how
[1647.60 → 1651.98] well do we know our decisions? And once we get an indication of where we are, you almost have a game
[1651.98 → 1657.32] plan or a roadmap of how you're going to get to the desired destination. There was a lot there. So
[1657.32 → 1663.16] let me know if I need to go through. Yeah. No, I appreciate that. That, that gives a ton of,
[1663.16 → 1670.62] of great, great context. Okay, Mike. So I, I definitely have learned a ton about implementing,
[1670.62 → 1677.50] you know, uh, data driven strategies, um, and a strategy towards decision-making in, in a, in a,
[1677.76 → 1684.28] in a company culture. Um, but after all this is practical AI. So, um, if we get to that point of
[1684.28 → 1691.22] kind of scoping out certain decisions that we want to tackle within a, within a company in terms of
[1691.22 → 1698.54] data driven decisions, how then do we make the leap to considering AI and machine learning efforts?
[1698.54 → 1702.22] Um, was that something that you considered, you know, right off the bat as, as you were
[1702.22 → 1706.02] implementing the strategy or, or did that come somewhere down the line? Yeah. You know what?
[1706.06 → 1710.50] It's something we had in our, in our back pocket the whole time. We knew we did have to take the
[1710.50 → 1714.80] organization on a journey, but there was some of these that were, I've mentioned this a few times
[1714.80 → 1720.72] that, that email example was one that was so obvious to us very early on. We, we needed a machine
[1720.72 → 1726.56] driven way to very quickly identify who was interested in what cause, because we, no matter how,
[1726.56 → 1731.06] how intelligent we thought we were as humans, we just couldn't figure that out. Um, whereas there
[1731.06 → 1735.78] were a lot of clues hidden within the data, but we needed to go through that, that journey of
[1735.78 → 1741.38] getting the strategy understood and the use cases of which this one was one of those. The other thing
[1741.38 → 1745.94] that we needed to do quite practically, and this is this, it depends on where the organization is,
[1746.04 → 1750.94] but you needed to get an indication of what the payback was, right? So as a result of doing this,
[1750.94 → 1756.44] what's the cost versus the corresponding payback if it works. Uh, and so there are some calculations
[1756.44 → 1761.86] that we had to do there, uh, which makes the, um, the case for investment much easier.
[1762.24 → 1766.80] And, and once you've got to that stage, this is where data becomes, it continues to be a bit of
[1766.80 → 1771.86] a puzzle. You're not done yet. So you can have your game plan. You can have the areas for which you,
[1772.22 → 1776.84] you know, exactly where you're going to apply some algorithms. You can get a team deployed on starting
[1776.84 → 1782.68] to think about, you know, you know, are we going to use a collaborative filter or a genetic algorithm
[1782.68 → 1787.16] and get really excited about that. But there is nothing worse than spending all that time building,
[1787.42 → 1791.88] you know, your, your really sophisticated algorithm, and it sits on the shelf, and it never gets used.
[1792.44 → 1798.90] Ultimately, this has to be deployed either to some level on some level of production or given to a
[1798.90 → 1804.46] team for them to actually use it. So your biggest challenge after that is getting the culture of the
[1804.46 → 1810.62] organization, getting them into, to value and to have new behaviours for where these algorithms
[1810.62 → 1817.70] actually get used. You're speaking, you're speaking our language here at practical AI. So, uh, so you're,
[1817.70 → 1822.62] you're helping us make it, make it practical, you know, in term, in terms of that, uh, like,
[1822.70 → 1828.36] is that something that you just kind of like, you know, in, in building up this strategy,
[1828.36 → 1832.88] is that something you instilled in people from the start of a project that like the real value comes,
[1832.88 → 1837.28] you know, once things are operationalized and deployed, not, you know, when things are
[1837.28 → 1843.22] conceptualized or, or when a model is trained in a Jupiter notebook or something, is that something
[1843.22 → 1848.36] that you instilled in early in, in that mindset? Or is that something you learned? Uh, I mean, I think
[1848.36 → 1855.16] where I learned that is by lots of painful scenarios where it wasn't the case.
[1855.54 → 1861.30] We, we had a lot of, I don't know how to get away from the painful scenarios, uh, because culture
[1861.30 → 1866.26] change, you know, behaviour change is very difficult to, to sort of instill. And I imagine being a
[1866.26 → 1872.18] a data type individual for which we are where, you know, you, uh, our interests aren't in how do we
[1872.18 → 1876.90] change people's behaviour? You know, personally, I mean, they're, they're psychologists that have
[1876.90 → 1881.56] that as a profession. So, you know, for us to try and jump into that, it's always going to be difficult.
[1882.04 → 1888.14] I'm definitely not a psychologist. Maybe Chris is, uh, no, my wife can verify I'm not.
[1888.14 → 1894.46] Sure. So I think, uh, but, uh, this is why there's, there are lots of other pieces that need
[1894.46 → 1899.84] to come into play. So for example, if you have the buy-in of the exec team, that helps, uh, because
[1899.84 → 1904.12] then working with each of the individual teams, you can begin to make sure that they, they get into
[1904.12 → 1909.64] the, uh, it changed the reward of, of value base for using some of these. What I found, I found a
[1909.64 → 1913.66] really simple equation to help sort of summarize behaviour change from the culture side of things.
[1913.66 → 1919.92] It was by a champ called, uh, BJ Fogg. Um, he does a lot of, uh, product behavioural design
[1919.92 → 1929.84] stuff. And, uh, he, he has a formula called, um, which is B equals M A T. Um, and that's B is for
[1929.84 → 1936.78] behaviour is equal to motivation, ability, and triggers. And it's the, the, the multiplication of
[1936.78 → 1940.78] the product of each of those three things, which means if any of those don't exist, you don't get a
[1940.78 → 1948.74] change in behaviour. So by motivation, you've got to get the organization in, in a sort of, a
[1948.74 → 1953.82] behavioural approach where they are motivated to use the algorithm. So there's something,
[1953.98 → 1957.78] they've got skin in the game. There's something interesting there for them as well. And you can't
[1957.78 → 1962.82] do that without working collaboratively with the teams. Uh, and, uh, that's a key thing that the
[1962.82 → 1969.12] the leadership team has a huge amount of involvement in. You cannot do that alone as a, as a, as a data
[1969.12 → 1973.18] team, uh, the motivational structures for doing that. If they're, if they don't exist, and I've
[1973.18 → 1977.84] seen this, and I have experience of this where, you know, you can build something really amazing.
[1978.32 → 1983.02] Um, well, we'll show an uplift, all the math adds up, you know, it's definitely something worth
[1983.02 → 1987.86] doing, uh, and you've built it, but it just doesn't get used because there is, there is no
[1987.86 → 1992.46] motivation to do so, you know, and, and if individuals are rewarded by doing something else,
[1992.56 → 1998.54] they would really struggle to sort of go off-piste. So motivation is a big one ability. That's massive.
[1998.54 → 2005.02] One of the things we forget as, um, data individuals is we don't speak English to the rest of the
[2005.02 → 2010.92] organization. So we almost limit their ability or create this, this environment where we just
[2010.92 → 2018.00] look like really brainy eggheads, and we're not so accessible. So a good example is how you can,
[2018.12 → 2023.54] you can build that algorithm, but it's not designed in a way that your, your, your team can use your CRM
[2023.54 → 2029.76] team or your customer service team have to be able to have the ability to, to use it and understand it.
[2029.76 → 2035.96] So we, as, as data individuals have a lot of work to make what we do more accessible and the output of
[2035.96 → 2041.24] what we do to be way more accessible. And that's there in the ability. If it's difficult and there's
[2041.24 → 2046.94] so many brain cycles required to even process, you know, the output, uh, ability goes down and then
[2046.94 → 2051.56] it, that breaks that equation straight away. And the last one is triggers. The other thing that I've
[2051.56 → 2056.56] seen and also been privy to is we can build some amazing things and never shout about it. And I
[2056.56 → 2062.84] remember being a frustrated analyst many, many years ago, sitting there thinking, how come all the
[2062.84 → 2068.30] marketing teams get all the accolades, and we've got all this amazing stuff here. And then you find out,
[2068.46 → 2073.62] you know, your CEO would come and say, well, you never told me about it. Right. So that's what the
[2073.62 → 2078.74] triggers is just, we need to work on our communication. And in fact, at Just Giving, we took the whole data
[2078.74 → 2084.28] team and taught them how to communicate, how to share some of the stuff that they're doing in
[2084.28 → 2089.18] English and a language that the rest of the organization can understand. And we began to
[2089.18 → 2094.28] slowly see some real changes in behaviour when we took this equation and intentionally addressed every
[2094.28 → 2099.54] single one of those aspects. You mean the rest of the world doesn't communicate in Python and data
[2099.54 → 2110.10] change? You mean there's another way? There is. I need, I apparently need to learn a few more things.
[2110.50 → 2114.06] I mean, the fact that you guys are running a podcast is pretty amazing. I've got to tell you,
[2114.10 → 2118.90] I've got, I've got a great story about an analyst who, when we took the team off site and one of the
[2118.90 → 2123.08] things we did first was to do some sort of one of those psychological evaluation tests to see,
[2123.08 → 2127.88] you know whether you're a blue type individual, red type individual, or some of those, you know,
[2128.58 → 2134.70] Myers-Briggs type things. And the whole team came out exactly the same. We were all very blue,
[2135.18 → 2140.28] introverted type individuals. And you could see immediately where the problem was, because we
[2140.28 → 2144.20] had no one who is like yellow or green to communicate with the rest of the organization.
[2144.66 → 2150.30] And a classic example was, we had one analyst who used to start a sentence when he was talking to the
[2150.30 → 2155.84] business by, with the following words, let me explain to you how stupid you are. And then carry,
[2155.94 → 2164.32] he'd carry on his sentence. Oh, you know, that's not effective. No, Daniel, that's not effective.
[2166.40 → 2168.36] I am learning so much.
[2171.36 → 2177.56] Okay. So I have been learning so much as well, especially as we've dived into, um, behavioural
[2177.56 → 2181.86] economics, because we, I don't think we've ever touched at that on that in any of these episodes
[2181.86 → 2186.86] that we've had to date. Um, and I'm pretty fascinated by how you've, how you've taken
[2186.86 → 2191.88] strategy and, and added that in and, and kind of all the various facets that you've been talking
[2191.88 → 2198.92] about. What I'm wondering is, could you tell us what you think makes a good AI use case to dive into?
[2198.92 → 2205.82] And if you have a specific example that you're able to share and kind of talk about how you made it
[2205.82 → 2211.58] real at a nuts and bolts level, I would love to hear that kind of like, you know, pedal to the
[2211.58 → 2217.50] metal kind of, kind of thought process. Uh, yeah, I think, um, uh, I'm now reaching my head. I
[2217.50 → 2223.24] actually had an approach that helped you. Okay. So I think what we were thinking about was when
[2223.24 → 2227.48] there are lots of decisions that take place within an organization, right? You have some operational,
[2227.48 → 2233.34] you have some strategic, a good AI use cases is a decision that is typically quite is, uh, is
[2233.34 → 2239.68] repeatable, right? So it happens more than once. And whenever it happens, it's relatively the same
[2239.68 → 2245.26] questions asked. So I keep deferring to that email example. There's the one that's on top of my head.
[2245.26 → 2250.00] Um, well, let's take, let's take Amazon, for example, uh, whenever somebody has put something in their
[2250.00 → 2256.42] shopping basket, there is always the decision of, uh, what else could we, could we serve them, uh, in
[2256.42 → 2261.96] order to, to increase the basket size, right? So you get that recommendation at the bottom. That decision
[2261.96 → 2266.68] is a repeatable decision. It's, it's one we're making every, and it's a repeatable decision in
[2266.68 → 2272.64] a specific point in time. And that point in time is very clear. So every time someone puts something
[2272.64 → 2277.02] in their basket, you know, you have the opportunity to upsell them so that you can increase their basket
[2277.02 → 2282.86] size. That decision happens all the time. And so the questions you'd ask is, um, can the organization
[2282.86 → 2288.84] identify when that decision will be made? Yes. Can they, uh, decide, uh, or have an indication of
[2288.84 → 2293.50] what information is considered every time that decision takes place? And it's, it's the same
[2293.50 → 2299.14] information and, uh, the possible actions that they could take consistent. So it's relatively the
[2299.14 → 2306.08] same, the same ones. And, um, then next you say, uh, can the outcome be measured? One of the most
[2306.08 → 2311.20] valuable things about working in AI and machines is, is how measurable those, the outcomes of the
[2311.20 → 2317.10] algorithm are because ultimately it's an investment. Data scientists are not cheap. Um, cloud computing
[2317.10 → 2321.92] costs, although most say they are, they should be cheaper. They, I always feel to some extent,
[2321.92 → 2326.36] they can be more expensive than on-prem, but then also your costs can go through the roof with the
[2326.36 → 2331.38] amount of compute and the amount of data that's available. So looking at some repeatable decisions
[2331.38 → 2336.34] that are relatively complex, but they are measurable. That's the sort of lens that, uh, we would look for
[2336.34 → 2343.54] a good AR use case. Yeah. And so when you, you already mentioned kind of, uh, you know, data scientists
[2343.54 → 2349.54] are expensive, you know, one big piece of this that's really tough is actually building up your
[2349.54 → 2356.42] team for, you know, AI and the operations around that and the, uh, you know, the building of the
[2356.42 → 2362.50] models, but the operational, operationalizing of them and the monitoring of them, um, in terms of
[2362.50 → 2368.44] your experience at just giving or, or maybe other places, have you taken a strategy of kind of building
[2368.44 → 2375.38] up software engineers that are existing within a company into kind of, you know, AI engineers or
[2375.38 → 2382.10] machine learning engineers, or kind of just brought in fresh AI and data science people, or has it been
[2382.10 → 2387.02] a mix of both? And do you see, do you see advantages or disadvantages to one or the other?
[2387.18 → 2394.00] Yeah. All right. So, um, I think it's, it's a mix of both. I'll answer this by going through the
[2394.00 → 2397.76] roles that I think were really critical for our team, and we're building the team.
[2397.76 → 2401.32] And they were essentially four key roles that we were looking for. So the first was
[2401.32 → 2406.80] your traditional business analyst. So this is the individual that is perhaps more communicative.
[2406.94 → 2410.98] They've come from a consulting background. They're almost your, the front facing ones. They're the
[2410.98 → 2416.22] ones you take out of the basement, right. And allow them to speak to users. Um, these are quite
[2416.22 → 2421.06] important because, excuse me, um, data always needs a face. And this is a representation,
[2421.06 → 2425.50] representation of that, but we want them to be able to speak some of the languages of the rest of
[2425.50 → 2430.84] the T the rest of the business, um, go native if they need to, but really understand the decisions
[2430.84 → 2437.12] and the key needs. Then, uh, we've got the engineers. So one of the things we stumbled across,
[2437.12 → 2443.18] uh, which was very interesting is when wrangling with large amounts of data, um, and making it
[2443.18 → 2449.32] available for data scientists, what we found was, you know, that rule that Parity rule that 80% of your
[2449.32 → 2454.64] time is spent on getting the data ready and only 20% on building the algorithm. We thought we would
[2454.64 → 2460.08] try and turn that on its head and reduce the time that a data scientist spent on data preparation.
[2460.38 → 2468.24] So we built a team of data engineers whose sole purpose was to make data go really smoothly from
[2468.24 → 2473.88] the source all the way to being available for whatever algorithm was going to be built so that
[2473.88 → 2479.18] the data scientist time was not spent on getting the data correct. And the majority of the time was
[2479.18 → 2484.60] spent on just making sure it was, it was in the usable format for whatever approach they were going
[2484.60 → 2491.34] to use, whether let's say they needed to do, um, uh, you know, it's a logistic regression, for example,
[2491.82 → 2496.88] uh, the data engineers would make sure that that data was set up so that you literally just had to run
[2496.88 → 2502.58] the logic command in, in whether it is R or whatever it is that you were using and spend more time on the
[2502.58 → 2507.38] results and perhaps consider a different approach to, you know, whether you wanted to move it through
[2507.38 → 2513.68] to a decision tree, for example, or a random forest, but to try and take away the expense that was being
[2513.68 → 2518.20] paid on, uh, working on the data side of things. So we had data engineers who could do that.
[2518.68 → 2525.10] And I think that sounds like a good way to, uh, both make things efficient and to keep data scientists
[2525.10 → 2530.50] happy. Yes, exactly. Yeah. Um, and of course there's the mix and match because, uh, the data scientist
[2530.50 → 2535.82] ultimately is the, is the hero role that everybody wants to be. So we had to just make sure they could
[2535.82 → 2541.88] all, they had their strengths. So the data engineers typically came from strong ETL backgrounds, but they
[2541.88 → 2546.42] were coders to some extent as well, because a lot of the data that needs to be moved around, sometimes
[2546.42 → 2553.72] it's easier just to write, um, some, some, you know, uh, some code to rather than build the traditional
[2553.72 → 2559.92] ETL funnels that we used to have. So spark jobs, for example. So those are data engineers had the
[2559.92 → 2564.76] capability of doing those. And then finally, the we found that the data scientists couldn't
[2564.76 → 2569.64] build production ready algorithms. So, you know, you could run it in R, get the results.
[2569.84 → 2574.60] You still needed to build the model to work in real time for when a user came, if it was one of those,
[2574.70 → 2579.98] or at least to have the calculations available and the results available so that the automatic
[2579.98 → 2586.06] decision could take place. Um, uh, a quick example would be when a user comes to the site,
[2586.06 → 2591.28] uh, which charities should we show them and in which order is a calculation that needed to take
[2591.28 → 2595.50] place overnight. But then we found that it was changing every hour as soon as there were different
[2595.50 → 2600.00] interactions that were taking place. So the data scientists couldn't build the solution for a
[2600.00 → 2605.96] robust solution, at least to work in, in real time. We needed engineers to do that. So we needed
[2605.96 → 2611.18] engineers who could understand the language that the data scientists were using, but then who were
[2611.18 → 2616.16] experts at building production ready systems. So you can see all of these roles, they, they need to
[2616.16 → 2621.06] have the same fundamental skills, but then they have their areas of expertise. So the engineers,
[2621.24 → 2626.02] we were training into machine learning so that they could understand what was taking place, but
[2626.02 → 2630.48] really what they were good at was engineering. The data engineers, really what they were good at was
[2630.48 → 2635.34] working with large sets of data, but they still needed to have machine learning training and so forth.
[2635.58 → 2640.78] The data scientists, we reduced their work on, on the data prep and made them focus more on,
[2640.78 → 2643.76] on, on, on, uh, machine learning. Does that make sense?
[2644.20 → 2649.10] Yeah, that makes, that makes a lot of sense. I know, um, you know, that, that can be a hard road
[2649.10 → 2653.46] to navigate and, but I think you, you've expressed it well in the sense that you want to, you want to
[2653.46 → 2658.86] build up people's skills, but also build up people's skills into what they're, they're interested in and
[2658.86 → 2665.54] what they, they're, uh, they do well in, right. And, uh, as, as already established on another, uh,
[2665.54 → 2670.32] episode, I, I actually really liked data mugging and cleaning. So maybe I would actually fit
[2670.32 → 2678.30] more into the, uh, into the, uh, data engineering, uh, part, part, um, there's a sickness that Daniel has in this.
[2678.66 → 2679.10] Yeah.
[2682.10 → 2686.04] Yeah. I, uh, it is what it is. I won't deny it.
[2686.04 → 2691.84] Um, that's a good place you've come to the way that, that, you know, you've, you've, you've looked
[2691.84 → 2698.00] in inward and you, you can see what you enjoy most about the whole data science process, if you like,
[2698.08 → 2704.04] because some people needed some convincing, uh, sadly, because you know, the, the most famous
[2704.04 → 2709.12] of all those three roles, four roles are the data scientists, which a lot of the team are aspiring to.
[2709.12 → 2714.70] So for some, uh, we just called them a data scientist, but we knew they were data engineers.
[2715.32 → 2720.98] Right. So. Gotcha. Yeah. So I guess having gone through all this process over, uh, eight years,
[2721.00 → 2729.84] I guess, if looking back, um, at, at challenges that you've had, uh, are there any standout lessons
[2729.84 → 2736.20] learned, uh, or, or things that if you could do a do-over that you might do differently? Um,
[2736.20 → 2739.22] is I thought that might be a good one of winding the conversation up.
[2739.38 → 2747.34] Yeah, absolutely. Um, I think I really wish I educated the organization as a whole on what
[2747.34 → 2754.16] data was and what it can do this. And I wish I'd started at that point because I found those
[2754.16 → 2760.16] explaining that, you know, to different individuals at different points in time. Whereas if we had done a
[2760.16 → 2765.12] a, a bigger exercise on, you know, almost like a transformational exercise and just saying,
[2765.12 → 2770.28] look, the whole organization needs to be educated on this. I think we would have had fewer problems.
[2770.28 → 2773.94] Not, not saying we would have had, we won't have had any, but we would have had fewer problems.
[2774.06 → 2778.94] This became even clearer to me when I remember, um, uh, speaking to someone at Facebook and they
[2778.94 → 2784.04] were telling me that the whole organization goes to a data Academy for two weeks. And a small part of
[2784.04 → 2790.88] that is understanding how to work with SQL, but a larger part of that is understanding how to ask the
[2790.88 → 2797.64] right question. And, and this really just hit home to me because if we had done more in educating the
[2797.64 → 2803.10] organization, you know, we, we would remove a lot of redundant work as well, where people were asking
[2803.10 → 2807.20] things because they were just interested, or they weren't really asking the right question. And
[2807.20 → 2812.78] sometimes data teams can be quite literal. So if they get a request from the business, they would do
[2812.78 → 2817.70] exactly what's been requested. But if you dug down the real question was something else,
[2817.70 → 2822.90] you know, and that's a fault on both sides. So, uh, I loved hearing that, um, there, you know,
[2822.90 → 2826.94] there, there are other businesses that are creating what they call data universities, where they put the
[2826.94 → 2832.98] whole organization through just to get them up to speed primarily on what is this thing called data?
[2833.34 → 2838.98] Let's demystify some of the terms that have come around and confused a lot of people. And, um, why is it,
[2839.04 → 2845.54] uh, you know, something that we can make more democratic, and you don't have to be technical to understand
[2845.54 → 2850.68] what data is and how it works because we use it every day. We use information to make decisions
[2850.68 → 2856.04] all the time and just demystifying that whole process for the organization. I wish we had done
[2856.04 → 2860.72] more of that. I think we would have got a lot further. Furthermore, I think we would, we developed some amazing
[2860.72 → 2866.94] stuff, but I think it, the road would have been much smoother. Awesome. Well, I know that I have
[2866.94 → 2872.18] learned a ton today. Um, I've really enjoyed our conversation. Thank you so much for joining us, Mike,
[2872.18 → 2877.28] and we'll put in the show notes, a link to, to Mike's information online, but also he's got this
[2877.28 → 2881.96] book coming out. You've heard a lot of great principles today, but I think that's going to be
[2881.96 → 2887.16] the, you know, a really great, uh, resource for people that are trying to create this sort of
[2887.16 → 2893.24] culture in a company. And, uh, and so we'll put the link, uh, in our show notes as soon as that's
[2893.24 → 2897.14] available. I know it's still in the works, but we'll put, put it there once it is available.
[2897.14 → 2902.14] And, um, just, thank you. Thank you so much, Mike. Uh, really appreciate you walking us through this
[2902.14 → 2906.72] process. Thank you very much. Thank you as well, very much. Thank you so much for the invite. It's,
[2906.78 → 2911.60] uh, it's great to be able to talk about this stuff. And me personally, I am really motivated
[2911.60 → 2917.62] by organizations getting this to work. There's a lot of, uh, hype around it, but equally, you know,
[2917.72 → 2922.68] there are a lot of organizations that are just struggling to, to, to get the value that they can,
[2922.68 → 2928.38] the game changing value that data promises. So we can all, um, sort of evangelize this a bit more
[2928.38 → 2933.14] than I think we can, we can really see some, some, some big things happen, you know, not just for
[2933.14 → 2938.86] commercial gain, but even for us as, as people in an intensely information world that we can,
[2938.86 → 2944.74] uh, you know, data help us get smarter, live healthier lives and so forth. So, um, I'm very
[2944.74 → 2949.72] excited about what could happen. Awesome. Yeah. That's super, super inspiring. Making, uh,
[2949.72 → 2958.60] making AI practical since 2018 here on, uh, here on practical AI. Um, yeah. Uh, thanks Mike. And
[2958.60 → 2963.16] really looking forward to the book. Um, hope to, hope to talk again soon. Great. Thank you. Thank
[2963.16 → 2970.30] you very much. Thanks. Bye-bye. Bye. All right. Thank you for tuning into this episode of practical AI.
[2970.46 → 2975.02] If you enjoyed this show, do us a favour, go on iTunes, give us a rating, go in your podcast app and
[2975.02 → 2979.16] favourite it. If you are on Twitter or a social network, share a link with a friend, whatever you got to do,
[2979.16 → 2983.24] share the show with a friend, if you enjoyed it and bandwidth for change log is provided by
[2983.24 → 2987.92] quickly learn more at facet.com, and we catch our errors before our users do here at change law
[2987.92 → 2993.50] because of roll bar, check them out at robot.com slash change log. And we're hosted on Linde cloud
[2993.50 → 2999.30] servers at a Linode.com slash change log. Check them out, support this show. This episode is hosted
[2999.30 → 3004.94] by Daniel Whiten ack and Chris Benson. Editing is done by Tim Smith. The music is by Break master
[3004.94 → 3010.08] Cylinder. And you can find more shows just like this at change law.com. When you go there,
[3010.14 → 3014.94] pop in your email address, get our weekly email, keeping you up to date with the news and podcasts
[3014.94 → 3019.78] for developers in your inbox every single week. Thanks for tuning in. We'll see you next week.
[3020.70 → 3021.88] Bye.
[3021.88 → 3023.88] You
