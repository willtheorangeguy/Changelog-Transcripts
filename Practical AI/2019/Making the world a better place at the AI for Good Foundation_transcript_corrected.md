[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.84] Learn more at Fastly.com.
[5.08 → 8.16] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.98] Check them out at Rollbar.com.
[10.22 → 12.40] And we're hosted on Linde cloud servers.
[12.76 → 14.74] Head to linode.com slash Changelog.
[15.72 → 20.34] This episode is brought to you by DigitalOcean, the simplest cloud platform out there.
[20.46 → 25.10] And we're excited to share they now offer dedicated virtual droplets.
[25.10 → 29.04] And unlike standard droplets, which use shared virtual CPU threads,
[29.04 → 32.88] their two performance plans, general purpose and CPU optimized,
[33.40 → 36.08] they have dedicated virtual CPU threads.
[36.42 → 40.86] This translates to higher performance and increased consistency during CPU intensive processes.
[41.34 → 45.20] So if you have build boxes, CI, CD, video encoding, machine learning, ad serving,
[45.50 → 49.98] game servers, databases, batch processing, data mining, application servers,
[50.18 → 54.92] or active front end web servers that need to be full duty CPU all day every day,
[55.14 → 57.92] then check out DigitalOcean's dedicated virtual CPU droplets.
[57.92 → 61.26] Pricing is very competitive starting at 40 bucks a month.
[61.66 → 66.38] Learn more and get started for free with a $100 credit at do.co slash Changelog.
[66.64 → 69.02] Again, do.co slash Changelog.
[69.02 → 86.38] Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[86.78 → 88.56] productive, and accessible to everyone.
[88.94 → 93.44] This is where conversations around AI, machine learning, and data science happen.
[93.92 → 98.20] Join the community and Slack with us around various topics of the show at changelog.com slash community.
[98.20 → 99.38] Follow us on Twitter.
[99.48 → 100.96] We're at Practical AI FM.
[101.46 → 102.28] And now onto the show.
[106.72 → 109.98] Welcome to another episode of the Practical AI podcast.
[110.48 → 116.78] We are the podcast that tries to make artificial intelligence practical, productive, and accessible to everyone.
[116.78 → 118.46] I am Chris Benson.
[118.66 → 122.52] I am Chief AI Strategist at Lockheed Martin RMS APA Innovations.
[122.84 → 128.68] And with me today is Daniel Whiten ack, my co-host, who is a data scientist with SIL International.
[128.82 → 129.42] How's it going, Daniel?
[129.66 → 130.76] It's going well.
[130.98 → 135.38] A little bit of jet-lagged at the moment, but happy to be talking.
[136.26 → 137.88] So I know you've been travelling.
[138.34 → 139.46] Where are you at this point?
[140.10 → 143.60] I'm in the Netherlands, so I'm meeting with a few different teams that I collaborate with.
[143.60 → 144.04] Great.
[144.26 → 145.06] Sounds good.
[145.46 → 147.92] Well, I am very excited about this episode.
[148.54 → 157.02] So anyone who has been listening to us for a while knows that you and I are very, very passionate about using AI for good.
[157.12 → 158.66] We're always talking about AI for good.
[158.88 → 159.50] Most definitely.
[159.50 → 161.72] Yeah, it comes up in many episodes.
[162.16 → 165.84] And so today we're going to end up kind of really dedicating that.
[166.00 → 172.32] I know that, you know, before we dive in, I know that I have some stuff that I do in that space.
[172.66 → 173.60] And so do you.
[173.66 → 179.18] I know for me at work, I work on humanitarian assistance and disaster relief, applying AI to those areas.
[179.36 → 184.06] And my own personal project, everyone that listens to me knows that I love animals.
[184.18 → 185.44] I'm always talking about that.
[185.44 → 191.96] And so I'm trying to use convolutional neural networks to detect dogfighting rings and puppy mills.
[192.02 → 198.34] And I know that you do some stuff in terms of AI for minority language community stuff, if I'm right.
[198.60 → 199.42] Did I get that right, Daniel?
[199.68 → 200.00] Yeah.
[200.00 → 202.08] So I actually work for a nonprofit.
[202.26 → 207.46] So SIL is a nonprofit, and I'm working on AI for minority language communities.
[207.46 → 214.30] And so, you know, things like Google Translate are only available in like, you know, 50 or so languages.
[214.30 → 220.18] But the world has about 7,111 languages at last count.
[220.52 → 225.64] And there are a lot of places that need humanitarian assistance.
[226.18 → 231.92] Most of the time, those places that have that need have just a lot of language diversity.
[232.10 → 235.00] So working on some of those problems.
[235.00 → 235.56] Great.
[235.72 → 242.64] Well, you know, not long ago, I have a friend named Paul Fees, who he used to work at Thomson Reuters.
[242.86 → 247.64] And we'd actually met, he actually interviewed me for an article that he wrote at Thomson Reuters.
[248.12 → 250.94] And we've kept up with each other ever since then.
[250.98 → 256.24] And so he was talking about the fact that he had just come to the AI for Good Foundation.
[256.24 → 263.50] And when we were talking, I asked him if I could interview James Hudson, who is the CEO for AI for Good Foundation.
[263.50 → 266.16] And we have the good fortune of James joining us today.
[266.30 → 266.86] Welcome, James.
[267.10 → 267.78] Thank you very much.
[267.90 → 269.26] I'm very happy to be here.
[269.36 → 277.38] We're excited about this because we're actually able to have a conversation about the work that you do and really have an entire episode just about AI for Good.
[277.38 → 278.74] So this is going to be a good one.
[279.10 → 289.76] I was wondering if you'd just kind of start us off, kind of telling us a little bit about your background, kind of how did you get interested in AI, and what's the story that led to this organization at a personal level?
[290.02 → 291.54] That's a great place to start.
[291.60 → 297.08] Now, I think obviously one episode for AI for Good is probably not sufficient to cover everything.
[297.08 → 300.12] But I guess we'll see how far we can get.
[300.50 → 303.28] So the organization itself started in 2015.
[303.60 → 305.92] So we're not a particularly old organization.
[306.28 → 311.18] But it was started with a lot of the machine learning and AI research behind it.
[311.48 → 323.16] It started specifically out of a set of workshops at Stanford University in 2014, where we were trying to think what the big challenges would be over the next 10, 15 years.
[323.16 → 327.74] That as AI researchers, we should be dedicating our time towards.
[328.38 → 334.64] And this set of workshops was attended by many of the big names in artificial intelligence that you would recognize.
[335.38 → 352.36] And one of the mandates that really came out of everybody there is that we need to get more of the research community and more of the practitioner community thinking about how they can use their skills and the methodologies that are now becoming so widespread.
[352.36 → 356.06] And other business areas for social challenges.
[356.06 → 362.06] And we don't exactly lack social challenges at the moment where we could be applying these technologies.
[362.50 → 367.34] Now, from my personal perspective, I've been working in artificial intelligence for about 15 years.
[367.90 → 371.28] I actually started similarly in machine translation.
[371.80 → 378.94] So I was working on low resource languages and on machine translation for the European Parliament.
[378.94 → 385.12] And this was at the German National Research Centre for Artificial Intelligence back in 2008, 2009.
[385.62 → 388.52] I also spent some time in industry proper.
[388.74 → 401.36] I was managing the AI research lab at Bloomberg for some time in New York, which allowed also to explore some aspects of attempting to use a technology for social impact.
[401.36 → 406.30] Obviously, as you can imagine, in an industry setting, that's not the primary goal always.
[406.74 → 415.82] But as you know, the Bloomberg Foundation and many projects in the oceans and climate and other areas that Michael Bloomberg in particular feels very strongly about.
[416.20 → 426.82] So there was certainly some precursor to the organization that started out of ideas with the Bloomberg Foundation and with various projects that we did in collaboration with academia back then.
[426.82 → 440.30] But the turning point in 2015 was really this set of workshops and the realization that the types of technology that we're developing today can have an enormous impact on these social challenges.
[440.76 → 446.60] But the question that remained was which social challenges should we really be attacking first?
[447.18 → 448.74] Which ones are most important?
[449.00 → 450.98] Where can AI have an impact?
[450.98 → 457.22] And the fortuitous answer that we came to was that the United Nations had already done this work for us.
[457.46 → 469.96] And the United Nations built the Sustainable Development Goals, which is a set of 17 goals, 16 that are thematic and one that involves building infrastructure that is strategic across the entire set.
[469.96 → 485.54] And they cover problems like removing poverty and ensuring that everybody has access to clean water and ensuring that everybody has enough food to eat and ensuring that we don't damage the environment on our planet to the point where it's ungivable.
[485.54 → 501.58] All things that, all things that, if we don't think about them long and hard, very, very quickly and take big steps are going to make certainly some people's lives much, much worse than they could be and ultimately make our entire planet harder to live on.
[502.16 → 509.76] Whether that's through geopolitical actions or through the actions of individuals on the environmental health of the planet.
[509.76 → 539.74] So that's where we began.
[539.76 → 569.74] We began.
[569.76 → 579.02] We don't exclude anybody, of course, but we do try to build a strong membership community of supporters and donors who will support us year after year.
[579.42 → 594.52] And in lieu of that, for this particular conversation, I was able to secure with our operational team that any listeners who are interested in becoming members of our organization can do so with a 50% reduction from our normal membership rate.
[594.68 → 595.10] Oh, awesome.
[595.22 → 595.52] Fantastic.
[595.70 → 595.74] Yeah.
[595.74 → 597.94] And how would they go about doing that?
[597.94 → 607.50] So on our website, if they sign up for membership, they just put in the coupon code practical AI is one word, and that will allow them to sign up for half the normal price.
[607.50 → 607.94] Awesome.
[608.16 → 613.36] We'll definitely post a link to the website in our show notes.
[613.36 → 617.44] So I would really encourage our listeners to look into that.
[617.64 → 619.48] We really appreciate that opportunity.
[619.48 → 628.52] I was wondering, so you talked a little bit about the origins of the AI for Good Foundation and the workshops that were run at Stanford.
[628.52 → 642.90] How did you go about, so I mean, it's one thing to recognize kind of the problems and the goals listed by the UN and also hold a workshop and understand that we can and should address these.
[642.90 → 655.56] But, you know, there's obviously certain things preventing AI practitioners or researchers from really going after these things wholeheartedly or else more would be going after these things wholeheartedly.
[655.56 → 669.28] So how did you decide, you know, what is preventing people from addressing these challenges and how to incentivize people, you know, busy researchers, busy practitioners to put their time into these things?
[669.74 → 669.84] Right.
[670.00 → 672.02] So that's the perfect question, really.
[672.12 → 673.78] That's the question that we started with.
[674.04 → 679.88] The incentive mechanisms for researchers are really skewed towards publication, right?
[679.88 → 687.74] Publication is, especially at top universities, the only metric that really matters for tenure.
[688.20 → 693.54] And tenure is the only thing that really matters to junior researchers if they want to have a job in the future.
[693.66 → 703.46] So the easiest thing if you want publications is to find a good source of funding and data, right, and to publish your work using that funding and that data.
[703.46 → 714.74] The problem with sustainable development goals like those of the United Nations is that they tend to be in areas that neither have funding nor have data.
[715.24 → 728.42] And as a result, very few people have the time to spend, right, in the five or six years they might have before they come up for review at their universities to actually explore ways of getting money,
[728.42 → 746.60] potentially from foundations and grant-making institutions and find ways of unlocking data from companies or government agencies and so on that might be holding data or potentially even go out and crawl or scrape or build sensor networks in order to get specialized new type of data.
[746.60 → 749.60] So that's one side of this issue.
[750.12 → 753.48] And that's where we decided we could have the biggest impact.
[753.48 → 765.46] It was essentially to build the capacity for the researchers and also practitioners within companies who have time to dedicate to this separately from their main job.
[765.46 → 775.72] Or maybe there are ways that they can make it part of their main job as well by providing the access to data resources, providing access to infrastructure,
[775.72 → 787.40] and building bridges between the organizations that need this work to be done in the field and the community that has the appetite and ability to do it.
[787.40 → 796.80] If you ask researchers at Stanford, at Carnegie Mellon, at Columbia, Princeton, anywhere, do you want your work to be used for social good?
[797.06 → 799.78] I have never received the answer, no.
[799.78 → 803.46] I've always received the answer, yes, but.
[804.14 → 813.40] And that but is usually that it takes too long to figure out how to do that effectively in a way that mixes with their normal career.
[813.40 → 829.26] So would it be fair to say you're essentially providing them with an alternate incentive path that they can follow so that they can achieve the output that they're producing specifically toward a good purpose that they have in mind, bettering the world?
[829.56 → 830.98] Is that a fair way of looking at it?
[831.26 → 831.62] Exactly.
[831.82 → 840.30] Now, so we are partners with the United Nations on defining how technology gets used for the sustainable development goals.
[840.30 → 856.30] And that means that we have connections into the various UN agencies like UNESCO, right, that deal with these challenges directly, as well as a whole set of nonprofits that operate in this area, government agencies around the world.
[856.30 → 874.20] And what we can do very quickly is, as you mentioned, plug the researchers in to a community that already wants their input and already has data that they can use and is very willing to invest additionally in order to make things happen.
[874.20 → 888.50] Because you can have a huge impact with very limited new types of models on data that previously has been unexploited because there are so few people working on this aspect of the humanitarian intervention.
[888.50 → 909.74] So if I'm a researcher, maybe I'm an associate professor or whatever it is, or I'm in a research R&D lab in industry, and I'm interested kind of in exploring this route, could you describe kind of what it's like to engage with the AI for Good Foundation?
[909.74 → 916.74] So is that kind of like becoming a member and then kind of starting those conversations around what is my expertise?
[917.22 → 919.32] And then how does that match up with the problems?
[919.50 → 924.16] And then you kind of match me up with these organizations and other things?
[924.24 → 926.86] How does that process typically go?
[926.96 → 929.52] Or maybe it starts at a workshop or a conference or something?
[929.94 → 931.46] The answer is, of course, a combination.
[931.74 → 935.68] But we primarily work with research labs in academia.
[935.68 → 940.88] So we build strategic partnerships with labs at certain universities where we have presence.
[941.28 → 946.68] And those universities are starting to number in kind of the several dozens at this point.
[947.14 → 963.26] So if there are people at universities, then we're very happy to get them involved in those communities and actually go out there and organize kind of workshops on the university campuses, get people involved, understanding what we do, what the opportunities are, and build that way.
[963.26 → 967.40] We also have what we call our global volunteer force.
[967.88 → 973.38] Now, this is a database, if you will, of people across industry, academia.
[973.66 → 989.56] So it includes anybody from master's and undergraduate students through postdoctoral fellows, researchers in academia, researchers in industry, practitioners in industry, programmers who maybe don't usually work on artificial intelligence but are interested in the area.
[989.56 → 997.22] And we build strategic task forces out of this volunteer set for particular projects.
[997.74 → 1017.10] So we will, when we identify, say, with UNESCO, that there is a need for looking into tracking student behaviour in certain types of classes in India, then we will go and identify five, six individuals from the global volunteer force in order to get involved in that project.
[1017.10 → 1047.08] With the task force in order to get involved with the task force in order to get involved in the project.
[1047.08 → 1066.26] My experience in kind of involving volunteers and nonprofit tech related stuff is a lot of times there's kind of this, you know, initial excitement on these, you know, these really exciting and meaningful projects and maybe an initial great effort at a hackathon or something like that.
[1066.26 → 1070.26] And then basically always the project dies out because there's no structure around it.
[1070.36 → 1075.84] So in terms of what you're talking about, it sounds like the, you know, I don't know, is that something you've seen?
[1075.92 → 1085.12] And maybe having the AI for good foundation as a backbone and managing, putting these mentors in place helps with that.
[1085.18 → 1088.26] But I was wondering if that's an issue you see, if that's something you're fighting.
[1088.26 → 1096.12] Yeah, the mentorship structure was built specifically in order to mitigate the concerns that you raised.
[1096.26 → 1099.10] Some of the initial projects that we did suffer a lot.
[1099.68 → 1108.80] And we had some disappointed nonprofits and government agencies because it seemed like people were very interested in the beginning.
[1109.00 → 1110.80] Everybody would attend kickoff calls.
[1110.94 → 1114.26] Everybody would even come to maybe a first onsite.
[1114.26 → 1117.24] But then other priorities would come up.
[1117.58 → 1120.26] So we're very careful now in two senses.
[1120.52 → 1125.98] We ask a lot of questions before we qualify people to go on the global volunteer force.
[1126.60 → 1135.46] And that includes the number of hours they're willing to put in, the timeframe over which they're willing to do it, the specific skills that they think they can contribute.
[1135.46 → 1143.76] And we vet those people to make sure that when we build teams, they will be teams that have the capacity to actually build something reasonable.
[1144.16 → 1147.34] The faculty mentor obviously is not a manager, right?
[1147.36 → 1152.82] It's not somebody who's going to manage the psychological well-being of the people on the team.
[1153.14 → 1156.76] But it does help a lot in terms of setting kind of a pace.
[1156.76 → 1178.76] And also people really enjoy being able to work with top researchers from academia in order to get kind of a taste of their work and also be able to cross-pollinate the types of things happening on the academic side with the types of things happening in industry, which we all know are two completely different worlds otherwise, which hardly interact.
[1178.76 → 1187.14] So, James, I know when we started the conversation, you made reference to the United Nations Sustainable Development Goals.
[1187.50 → 1192.86] And I was looking across some of the program of activities that you guys offer on your website.
[1193.30 → 1198.40] And just to enumerate some of them for our listeners, there were workshops and conferences.
[1198.40 → 1200.22] There was education outreach.
[1200.40 → 1207.76] There were standards and guidelines, tools and platforms, research program funding and support, and local chapters.
[1207.76 → 1217.40] I was wondering if you would – you've kind of talked a little bit about how these volunteers can kind of start engaging, become members, and start trying to do that.
[1217.46 → 1225.08] Could you talk about it in the context of some of the programs that you guys offer and maybe give some examples, a little bit of case study about what you've done?
[1225.46 → 1225.80] Absolutely.
[1225.96 → 1227.26] I'd be very happy to.
[1227.80 → 1234.26] So, there are two case studies that I think would be interesting to talk briefly about.
[1234.26 → 1244.86] So, the first big program that we ran with a network of universities and companies and nonprofits and the government was around food security.
[1245.36 → 1248.34] And we call this the Food Security AI Challenge.
[1248.34 → 1264.54] And what we did in the first instance was gone to many different companies that were operating in this section, whether it's the actual agricultural output side, so farmers, farming conglomerates, seed producers, and so on.
[1264.54 → 1279.48] The logistics side, so people who actually go out to the farms, purchase the goods, move them from one warehouse to another, eventually move them into refining and other plants that they need to go through in order to make it to market.
[1279.48 → 1286.50] The markets themselves and then finally kind of food waste size, so the consumption side of that equation.
[1287.22 → 1296.66] And we gathered data sets, and we tried to bring people on board with a view to contributing the information that they had about their part of that puzzle.
[1296.66 → 1313.00] Now, we then made those data sets available, so climate data, phenotypic, genotypic data about seed varieties, growing data, supply chain data, so where food was being consumed, when, and so on, to a community of people who signed up.
[1313.08 → 1315.10] And those people came from industry.
[1315.82 → 1324.96] So, we had entrants from all over the world, but especially from US, Canada, Europe, China, Australia, and South America.
[1324.96 → 1333.62] And what we were looking for was for people to apply on this data interesting metrics to help us first understand the whole landscape.
[1334.10 → 1336.84] We then brought people together for a series of workshops.
[1337.04 → 1342.56] We held workshops at the Santa Fe Institute, and we held workshops also at several AI conferences.
[1343.10 → 1352.40] In particular, we have a very close relationship with the ACM Conference on Knowledge Discovery and Data Mining, which is one of the largest machine learning conferences in the world.
[1352.40 → 1355.94] It's about 5,000 people, and it takes place in August of each year.
[1356.56 → 1368.60] And we partner there in order to build continuous topical workshops and theme days around the SDGs and how researchers and practitioners can get involved.
[1369.00 → 1372.14] And we glued all of these pieces together.
[1372.14 → 1390.10] And one of the outputs that we got from the models that we built was actually the ability to improve the seed yield of particular varieties of seed that are purchased, especially across the US Midwest regions, by an additional 50% per year.
[1390.16 → 1390.62] Oh, wow.
[1390.82 → 1393.26] In terms of the yield improvement.
[1393.26 → 1410.72] So yield improvement is around 1% a year on average, based on the enormous amounts of resources and research that seed production companies put into growing seeds, testing them, splicing them, regrowing them, keeping track of test fields.
[1411.24 → 1418.16] Everything is done in the traditional method since GMO has been criticized for many years.
[1418.48 → 1422.02] So seed manufacturers have gone back to more traditional types of splicing.
[1422.02 → 1425.98] And they get roughly a 1% improvement per year.
[1426.32 → 1437.76] Now, just through the data science aspect of this, just through looking at it through machine learning eyes, if you will, they were able to push that up by, so to 1.5%.
[1437.76 → 1451.42] Now, to give you an idea of the effect that that can have, right, if implemented across the board, is that if we don't come up with a way of doubling our productive capacity, then by 2050, we basically run out of food.
[1451.42 → 1461.98] And that's based on fairly conservative population projections and also based on the fact that the African population in particular is going to be exploding over the next 20 years.
[1462.44 → 1468.22] Now, that doesn't even account for climate change scenarios and changes in agricultural land use.
[1468.22 → 1470.26] So we need to make a change here.
[1470.36 → 1472.80] And this is one way that we can contribute towards it.
[1472.80 → 1473.76] Yeah, I'm curious.
[1474.16 → 1475.96] Obviously, that's super exciting.
[1476.22 → 1481.32] And I'm so happy to hear that this process happened and the outcome.
[1481.54 → 1489.00] I was wondering about your perspective on, you kind of mentioned at some point, you know, if implemented, what effect this would have.
[1489.00 → 1501.18] So once you have this outcome from one of these efforts, what is the process to get that information and those techniques back into the hands of people that kind of can do the implementation?
[1501.64 → 1505.30] Is that through the organizations that you have connections to through the UN?
[1505.48 → 1515.98] So how would that actually get back into the hands of the seed producers or the researchers in industry that could actually kind of work towards those implementations?
[1516.16 → 1516.68] Right.
[1516.86 → 1518.36] It's a very good question.
[1518.36 → 1525.02] Again, so we try to involve the full life cycle of stakeholders throughout the process.
[1525.02 → 1537.44] That means bringing the government representatives and the NGO representatives and even sort of farming representatives into the room for our workshops.
[1537.76 → 1545.90] It also means going and having specific meetings in strategically located areas where this can have the biggest impact.
[1545.90 → 1558.14] Now, the US Midwest is a huge growing region of global significance, as are large parts of Brazil, as are large parts of Eastern and Southeastern Europe.
[1558.56 → 1568.02] And so we actually go out and talk to people in those areas and help them to understand how the technology might be integrated with their current practices.
[1568.02 → 1582.14] This is hard because often the biggest barrier is not that the technology is not available, but it's the fact that there is no mechanism by which to get people to shift the way that they're currently doing things to use the technology.
[1582.38 → 1584.38] Sometimes involves a cultural shift as well.
[1584.58 → 1585.18] It sure does.
[1585.18 → 1585.78] Exactly.
[1585.78 → 1585.80] Exactly.
[1586.10 → 1587.64] And that's the hardest part.
[1587.78 → 1590.48] And we're still learning how to do that effectively.
[1590.58 → 1594.50] And I think everybody's still learning how to do this really effectively, right?
[1594.50 → 1607.16] There are reasons why, despite billions of dollars in aid over the last 30, 40, 50 years to certain countries, we still haven't been able to shift the quality of life of individuals in those countries.
[1607.16 → 1612.14] And it's not because there wasn't enough money, and it's not because there weren't enough people wanting to do it.
[1612.14 → 1622.44] But it's because the reality of this area is that there are certain societal frictions and cultural frictions, as you mentioned, that make implementation hard.
[1622.74 → 1626.04] You know, we're ultimately a market-based economy, right?
[1626.12 → 1628.54] And it's about supply, and it's about demand.
[1628.72 → 1633.20] And you can't always shape everything just by having the technology available.
[1633.20 → 1646.76] This episode is brought to you by O'Reilly Open Source Conference in Portland, Oregon, July 15th through 18th.
[1646.78 → 1647.70] We'll be there, by the way.
[1647.70 → 1652.56] As you know, OZ CON has been ground zero for the open source community for 20 years.
[1652.86 → 1656.64] And this year, they're expanding to become a software development conference.
[1656.88 → 1660.38] Because in 2019, software development is open source.
[1660.38 → 1663.38] At OZ CON, you get to see what's shaping the future of software development.
[1663.56 → 1670.86] The program covers everything from open source, AI, infrastructure, blockchain, edge computing, architecture, and emerging languages.
[1671.38 → 1676.86] Hear from industry leaders like Holden Caro, RPA Dmitri, Julian Simon, and Allison McCauley.
[1677.30 → 1680.70] Learn more and register at OZCON.com slash changelog prices.
[1680.88 → 1685.32] Start at just $925 when you register before April 19th.
[1685.34 → 1686.96] After that, the price is going to go up.
[1686.96 → 1692.20] Plus, you can use our code changelog20 to get 20% off your bronze, silver, or gold passes.
[1692.68 → 1695.04] Once again, our code is changelog20.
[1695.48 → 1698.72] And head to ozcon.com slash changelog to learn more and register.
[1698.72 → 1719.54] So, I've been looking across your projects page, too.
[1719.62 → 1721.80] And I saw that you covered kind of the food.
[1722.28 → 1724.76] And that's a very inspirational use case as well.
[1724.84 → 1726.90] You know, in terms of being able to do that with food.
[1726.90 → 1746.82] Allison, just to share with the audience, you have projects in ocean life protection, education, urban development, traffic safety, media bias, carbon sequestration, health energy, I'm sorry, health, sleep, and nutrition, and also transparency in government and corruption and such.
[1746.96 → 1750.32] Do you have any other use cases that you can also share with us along the way?
[1750.32 → 1756.26] Yeah, a big area where we're really trying to have an impact now is climate change.
[1756.50 → 1762.92] But this is an area where you can't really just dive in the same way as many of the others.
[1763.08 → 1768.76] There are many climate scientists and environmental scientists working on the question of climate change, right?
[1768.76 → 1771.66] It's a huge area of research right now.
[1772.34 → 1785.76] And the IPCC, which is the main international body that publishes research on findings relating to climate change and predictions about what would likely happen in the future if we don't or do change our behaviour.
[1786.08 → 1788.60] They're the main body that deals with this.
[1788.60 → 1794.74] And as a result, the machine learning researchers have not had much of an impact in this area.
[1795.06 → 1795.80] Let's put it that way.
[1795.84 → 1806.16] If you look at the latest IPCC report, there are almost no citations to machine learning research or AI-related research.
[1806.66 → 1811.12] And what are some of the inhibiting factors that is making that the reality currently?
[1811.12 → 1824.30] The main factor is because you have a very strong research community that is not an AI research community, there has been no reason for them, perceived reason for them to reach out and want to get involved with this.
[1824.38 → 1832.18] Now, some of those papers may include some machine learning methodology, but actually very, very, very few of them.
[1832.18 → 1841.92] And the reason is they have their own science-based modelling techniques, which they have been developing fairly independently for decades.
[1842.94 → 1848.46] And as a result, there just isn't much cross-pollination between these research areas.
[1849.24 → 1860.42] And if you go to industry, there also isn't very much cross-pollination between the for-profit motivated companies that may benefit from one or the other area, right?
[1860.42 → 1868.52] There are hardly any machine learning startups in the solar energy space, for instance, or in any other energy space.
[1869.02 → 1878.54] So is that when you've been making efforts in that area, and you have identified this as a major barrier, how would you go about getting those communities to talk?
[1878.66 → 1884.06] Is that part of kind of the workshop and conference projects that you have going on?
[1884.18 → 1886.94] Or how have you been making strides in that area?
[1886.94 → 1890.86] So we've got two prongs on this particular area right now.
[1890.96 → 1898.10] The first is that we are organizing what we're calling the Earth Day Summit in Alaska, in Anchorage, in August.
[1898.66 → 1907.32] And this will bring together machine learning researchers, machine learning practitioners, scientists who work with the IPCC,
[1907.32 → 1917.42] scientists from NSF, from various other large international or national grant-making organizations that work in this area.
[1917.42 → 1932.36] And that's the first time that we're going to see an organized and large-scale set of conversations exactly on the topic of how machine learning can help with the various climate change-related challenges that we face.
[1932.36 → 1938.54] Now, many people don't realize, but most datasets used by the IPCC are tiny.
[1938.90 → 1945.00] They're on the order of tens of samples because you can't take more than tens of samples of ice cores.
[1945.50 → 1954.82] And you can't look at testing gas concentrations in more than 10 or 20 different locations globally without it becoming cost-prohibitive.
[1954.82 → 1958.48] So many of the problems aren't big data problems.
[1958.74 → 1965.44] But if we're talking about practical AI, there's no reason why machine learning has to be a big data problem, right?
[1965.46 → 1968.20] This is a new myth that has been generated.
[1968.40 → 1970.84] We have methods for dealing with small data, too.
[1971.24 → 1973.86] And some problems converge faster than others.
[1973.86 → 1981.36] And some problems require less data in order to achieve the same performance, depending upon how you go about finding solutions.
[1981.36 → 1993.98] And so we're all about starting those types of conversations and not kind of hiding behind the stereotype of machine learning as being large convolutional neural nets with millions of samples.
[1994.44 → 2003.18] I have a little bit of a kind of side question that occurred to me as you were talking in particular about your Earth Day Summit in Alaska in August.
[2003.18 → 2018.38] And if you think of me as a podcaster with a hammer trying to find my nail, how can those of us that are in some form or fashion part of the media or do podcasts or other similar things, bloggers, how can we help?
[2019.86 → 2031.72] Considering that you have these challenges that are cultural often and changing attitudes and saying, hey, we have some great tools that can be applied to the great problems of our time.
[2031.72 → 2040.10] How can we help at large in terms of getting the word out and starting to change minds and how people are perceiving these situations?
[2040.46 → 2050.82] We are all about getting the media and people who have an audience to share what we do and also to come and experience what we do directly.
[2050.82 → 2063.58] So we do have, for example, media passes to all of these events where we get people into the room and try to record as much of it as possible for dissemination.
[2064.36 → 2078.74] Many of our workshops and conferences are freely available to view either through our website or on videolectures.net, which is the largest platform for graduate level and above content in the sciences.
[2078.74 → 2079.40] Oh, great.
[2079.52 → 2081.58] Including computer science and machine learning.
[2081.72 → 2083.26] And we'll have a link to that in the show notes.
[2083.62 → 2086.58] So, you know, we definitely want to get the word out.
[2086.70 → 2092.88] We want you guys to come and be part of the conversation as much as possible so that you can offer that gateway to your listeners.
[2092.88 → 2100.06] We also want your listeners to come to the, you know, the conferences and workshops and be part of that directly.
[2100.32 → 2101.90] All of our events are open.
[2102.42 → 2107.10] Even our board of director meetings are open, right?
[2107.10 → 2111.80] We have minutes of what we talk about on every aspect of our organization.
[2112.06 → 2122.22] And as a result, we hope that that helps create a culture of wanting to get hands dirty, wanting to get involved and ultimately having a bigger impact down the road.
[2122.46 → 2128.92] And I have one follow up back over to the data side that you're mentioning in terms of having small data sets.
[2128.92 → 2137.98] That is something I mentioned at the top of the show that at work, I'm working on humanitarian assistance, disaster relief, and certainly the lack of data in certain areas.
[2137.98 → 2139.32] That being one of them.
[2139.46 → 2143.68] But I imagine there are many different areas where AI for good can be applied.
[2144.38 → 2155.16] How much of your focus is on generating data sets versus, you know, having the luxury of going right in and trying to model a situation into improvement?
[2155.16 → 2158.66] Do you have a large focus on data set generation by chance?
[2158.92 → 2159.02] Yeah.
[2159.12 → 2161.60] So we do have to get involved in this area.
[2161.72 → 2171.14] As somebody who works in artificial intelligence and listeners will also know that having data is often a red herring, right?
[2171.14 → 2176.46] Because if you look at medical data, for instance, it's collected in a particular way.
[2176.58 → 2178.68] It's collected for a particular purpose.
[2179.18 → 2195.42] And often when you take somebody else's data that's been collected for a different purpose, you're missing key information about the assumptions that were made during the collection process, about the method of storage, about the method of just collecting the information, right?
[2195.46 → 2196.88] How accurate were the sensors?
[2196.88 → 2206.36] Did you decide to kind of fudge together two variables because you couldn't really be bothered to measure where one begins and where the other one begins or ends?
[2206.70 → 2221.40] And as a result, it's often the case that we find that the data sets that look like they might be useful in the beginning are just not because the margin of error on the key variables of interest is too high for our particular use case.
[2221.40 → 2231.12] Unfortunately, especially in the research world, but in many places, people ignore the aspect of understanding the data appropriately before jumping in.
[2231.76 → 2238.40] And this leads to results that look good on paper, but don't really convert into something that's usable on the ground.
[2238.40 → 2255.48] And we have to be very careful about this because we only have one chance with certain stakeholders and people will never trust us again if we promise that we give them an improvement, and it doesn't pan out because we weren't careful about what type of data we were using to infer a particular decision for them.
[2255.48 → 2269.12] I love what you said about, you know, in this whole discussion about small data and certain techniques that, you know, maybe the AI community as a whole isn't so focused on.
[2269.12 → 2279.66] I think that, you know, we're oftentimes kind of blinded by building a bigger language model with more text data and all the data that we can get.
[2279.78 → 2285.34] But that at the same time, that kind of steers us away from a lot of research areas that are really valuable.
[2285.34 → 2309.60] And I'm just curious, you know, in these sorts of challenges that you're providing and the data that people are working on, are they finding sort of new, interesting techniques that, you know, others maybe, you know, have not run across or have not explored because the problem doesn't involve a lot of data or the, you know, researchers aren't focused on these issues.
[2309.60 → 2320.90] It just seems like we could, in addition to solving really important problems, we could stumble on really important technical discoveries as well because we're exploring a larger variety of problems.
[2320.90 → 2347.74] Yes, that's precisely what happens. I'm actually really glad that you brought this up because I feel like over the last 10 years or so, right, as artificial intelligence has gained a new meaning and as more and more people have associated with the area in one way or another, right, whether it's to raise money for their startup or to watch cool on TV shows or however, you know, the underlying reason might be,
[2347.74 → 2354.26] we've kind of lost track of the fact that there are some problems that you could consider them solved, right?
[2354.34 → 2365.56] Once you've achieved a certain threshold of ability to recognize a cat in an image, the problem of cat identification is fairly well solved.
[2366.00 → 2377.38] Okay, you can get, you know, you can improve it by half a percent, maybe even 5%, but improving it by 5% doesn't open up any new use cases that previously were not accessible.
[2377.38 → 2386.80] Right, so once you've had a breakthrough, the further work doesn't make it possible to do things that you couldn't do before, it just maybe gives you a slight improvement in the ability to do it.
[2387.04 → 2394.84] What we're focused on as an organization is solutions to problems that currently don't have any viable solution.
[2394.84 → 2399.30] And that's an important thing to think about from an AI research perspective.
[2399.46 → 2410.08] Would you rather be spending your time, as you said, right, in a machine translation context, improving your blue score by 0.1 on French to English, right?
[2410.08 → 2427.66] Or would you rather have a breakthrough on kind of that under-resourced language that, by the way, has 350 million people using it in underprivileged areas around the world, where now all of a sudden you gave them access to the internet and all the knowledge on it, right?
[2427.96 → 2432.18] Which of those problems is more impactful for you to be working on, right?
[2432.18 → 2433.34] One of them is already solved.
[2433.44 → 2435.30] You can get an easy publication out of it.
[2435.38 → 2437.08] There are 10 journals that will accept it.
[2437.28 → 2441.64] And the other one will be a harder sell, but it's going to ultimately have a bigger impact.
[2441.96 → 2445.80] And that problem is actually going to be worth something in the real world.
[2446.02 → 2447.50] That's what we're trying to do.
[2447.78 → 2450.96] We're trying to get people to work on the latter, not the former.
[2450.96 → 2455.66] And you segued right into where I was about to go next, which has to do with impact.
[2455.84 → 2461.10] And I guess I wanted to kind of wind up asking kind of a two-prong question.
[2461.52 → 2468.30] So if you made the generous membership offer earlier, and definitely we're encouraging our listeners to go check that out.
[2468.30 → 2480.14] If someone has a passion for a particular area within the larger AI for Good space, and they want to join, is there a way they can bring a project into the organization or sponsor it?
[2480.14 → 2481.80] How do you make those choices?
[2482.12 → 2494.02] And the other side that I'll go ahead and impose is if they're not part of the foundation itself, but they're just kind of out there on their own, do you have any guidance on how they might drive their own passions for AI for Good forward there?
[2494.02 → 2494.46] Yes.
[2494.84 → 2509.64] We don't really make a difference between people who are members of our organization and working on AI for Good or people who are out there by themselves trying to do something good with the techniques that they know and the data sets that they have available.
[2509.64 → 2513.40] And their passion as inclusive as we can possibly be.
[2514.18 → 2518.66] And as I said, whether people choose to become a member or not is irrelevant to the work that we do.
[2518.72 → 2521.62] We kind of need money, obviously, like any other organization.
[2521.62 → 2535.44] But if there are people out there that need support, right, where there is a connection that we could potentially help them make that will drive forward their project, that will make it, you know, a little bit more likely that it will get picked up and used for something beneficial.
[2535.44 → 2537.52] We want to hear about it, right?
[2537.90 → 2544.92] You can write to us through the website or, you know, at info at AI for good.org, or you can reach out to me directly.
[2544.92 → 2557.50] And we're always going to be interested in having those conversations, regardless of whether it ends up being considered an AI for good foundation project or something that is being done entirely separately.
[2557.50 → 2559.56] And that can be anywhere around the world.
[2559.64 → 2568.88] And we're especially interested in focusing on areas that currently don't have as much of the resources of AI practitioners.
[2569.20 → 2574.92] Places that are maybe not the first places you would think about hosting a conference, like in Kiev in Ukraine, for instance.
[2575.32 → 2575.50] Right.
[2575.50 → 2580.30] Or in Dhaka in Bangladesh or even in São Paulo in Brazil.
[2580.78 → 2581.06] Right.
[2581.10 → 2585.68] There are many places around the world that are not New York and San Francisco or London.
[2585.68 → 2595.16] And those are the places where we can also have a big impact by bringing kind of more focus and energy towards solving these challenges.
[2595.96 → 2599.72] And, so please do get in touch, right, no matter what you're working on, if we can help.
[2599.72 → 2606.64] Because you do need a network in order to get projects from a prototype phase to actually being deployed.
[2607.08 → 2609.30] And there's no point duplicating the effort.
[2609.64 → 2609.74] Right.
[2609.76 → 2610.64] That's why we exist.
[2611.00 → 2613.64] That's more inspiring than I can express.
[2613.88 → 2616.94] It's on behalf of everyone listening to the show.
[2617.08 → 2623.02] I would like to thank you very much for the work that you and the foundation are doing in this space.
[2623.02 → 2638.16] And I would also like to challenge our listeners in turn that if you are a practitioner in the AI and ML space and, you know, take your expertise, pick some sort of side project where you think you can make a difference and use AI for good.
[2638.40 → 2645.22] So, James, thank you so much for coming on and kind of sharing what you're doing and giving us some guidance on how we can do it ourselves.
[2645.54 → 2646.34] Really appreciate it.
[2646.48 → 2647.18] Thank you, guys.
[2647.18 → 2650.92] It's a fantastic opportunity for us to be able to talk to your listeners.
[2651.32 → 2652.52] And it was very enjoyable.
[2652.52 → 2653.10] Thank you.
[2653.28 → 2653.68] Thank you.
[2655.96 → 2656.46] All right.
[2656.52 → 2659.14] Thank you for tuning into this episode of Practical AI.
[2659.40 → 2660.86] If you enjoyed the show, do us a favour.
[2660.98 → 2661.56] Go on iTunes.
[2661.70 → 2662.34] Give us a rating.
[2662.62 → 2664.50] Go in your podcast app and favourite it.
[2664.58 → 2667.32] If you are on Twitter or social network, share a link with a friend.
[2667.40 → 2669.76] Whatever you got to do, share the show with a friend if you enjoyed it.
[2670.06 → 2672.72] And bandwidth for Changelog is provided by Vastly.
[2672.84 → 2674.26] Learn more at Fastly.com.
[2674.26 → 2677.68] And we catch our errors before our users do here at Changelog because of Rollbar.
[2677.88 → 2680.28] Check them out at Rollbar.com slash Changelog.
[2680.28 → 2683.10] And we're hosted on Linde cloud servers.
[2683.44 → 2685.06] Head to Linode.com slash Changelog.
[2685.16 → 2685.60] Check them out.
[2685.68 → 2686.50] Support this show.
[2686.92 → 2690.08] This episode is hosted by Daniel Whiten ack and Chris Benson.
[2690.54 → 2692.60] The music is by Break master Cylinder.
[2692.98 → 2696.44] And you can find more shows just like this at Changelog.com.
[2696.62 → 2698.58] When you go there, pop in your email address.
[2698.86 → 2704.90] Get our weekly email keeping you up to date with the news and podcasts for developers in your inbox every single week.
[2705.26 → 2706.06] Thanks for tuning in.
[2706.18 → 2706.98] We'll see you next week.
[2717.06 → 2718.36] Winner, winner, chicken dinner.
[2718.52 → 2720.06] You are today's winner.
[2720.34 → 2723.06] Because you stuck in here all the way to the end of the show.
[2723.32 → 2725.62] Here's another preview of our upcoming show called Brain Science.
[2726.08 → 2727.96] This podcast is for the curious.
[2727.96 → 2735.52] We explore the inner workings of the human brain to understand behaviour change, habit formation, mental health, and the complexities of the human condition.
[2735.90 → 2741.74] It's hosted by myself, Adam Stachowiak, and my good friend, Muriel Reese, a doctor in clinical psychology.
[2742.28 → 2748.00] It's about brain science applied, not just how the brain works, but how we apply what we know about the brain to better our lives.
[2748.58 → 2748.94] Here we go.
[2748.94 → 2755.62] One of the things that's fundamental, I would say, to being human is change, right?
[2755.74 → 2762.84] And so sometimes people come in and are really key in our life for a period of time, and then things change.
[2762.90 → 2772.64] Either we grow or they grow, or they change in a different direction, and then the relationship changes or that feedback loop gets modified in some way.
[2772.64 → 2774.48] That isn't always a bad thing.
[2775.00 → 2783.20] It's just going, my sense of choice actually is a critical component when it comes to feeling good about my life.
[2783.32 → 2801.20] If I feel like everything is sort of outside of me and I don't have any charge over it, like I didn't choose to work in a more remote location, or I didn't choose to go to school, or I didn't choose this person, then it feels far more oppressive, as opposed to I actually participated in the outcome.
[2801.20 → 2802.70] That I'm actually experiencing.
[2803.28 → 2808.02] So I then also have more charge over whether I want to change it.
[2808.82 → 2816.46] I think this feedback loop process that we're talking about here is super common to developers.
[2817.10 → 2824.70] You know, from people who write code to people who plan and to engineer and to manage and lead.
[2824.94 → 2828.72] Like there's no one in the software process that doesn't understand the feedback loop.
[2828.72 → 2834.34] And the reason why is that in product development, they have this concept of agile.
[2834.96 → 2849.74] And basically it means you produce something, you put it out there, and you expect the feedback loop to happen in order to gain insights and course correction to then release another version of it that continually and iteratively becomes more and more improved.
[2849.74 → 2854.60] So this whole process in day-to-day work in software is normal.
[2855.08 → 2863.08] And I think it's interesting how we're going to apply to their lives and people's lives, you know, to take the same importance of a feedback loop, for example, and apply it.
[2863.54 → 2863.66] Right.
[2863.66 → 2872.28] Well, so this is very much how it goes in relationship, which is why there is an importance when it comes to sort of things resonating.
[2872.42 → 2878.58] You ever walk into a room or an interaction with a couple other people and like something just feels wonky or off?
[2878.94 → 2881.68] You're like, I can't put my finger on it.
[2881.82 → 2882.88] Definitely been there.
[2882.88 → 2883.32] Right.
[2883.32 → 2883.88] Right.
[2884.64 → 2896.96] Well, and so to be able to identify that in relationships and even go, wow, I need to – I'm experiencing this person in my world with the limited interactions that I have with them.
[2897.10 → 2899.22] It hasn't really resonated with me.
[2899.48 → 2901.24] And so I don't get good feedback.
[2901.24 → 2907.06] So now I'm going to be more defensive because I feel as though there's a threat.
[2907.28 → 2909.48] It doesn't necessarily mean the person is threatening.
[2909.64 → 2912.98] However, my brain is going to tell me, hey, we need to be more protective.
[2913.40 → 2917.72] We need to do some strategies so that you're not fully exposed.
[2917.72 → 2933.54] You know, one way I look at scenarios like this, I would say as of late, is because if you ever watched a TV show or a movie where the narration, the storytelling part of it, they expose a character in a certain light.
[2933.76 → 2936.02] And you may dislike that.
[2936.10 → 2938.12] They may be a villain or villainess, right?
[2938.46 → 2938.80] Sure.
[2938.80 → 2950.82] But the moment they turn the story to their backstory and why they are the way they are or why they're acting the way they're acting, you then kind of fall in love with them, and you're almost rooting for them.
[2951.14 → 2951.26] Right.
[2951.30 → 2967.80] I feel like that's the same thing that happens day to day to our lives is that, you know, there are people who seem villainous or not for us, but we don't understand their backstory and why they are the way they are for us to have and employ that empathy that's required to have this dance.
[2967.80 → 2970.22] This dance, as you say, this iteration of relationship.
[2970.90 → 2977.78] You know, we just assume they are who they are, and we project, you know, our worst fears onto them and they become true.
[2978.64 → 2980.12] Yes, you got it.
[2980.12 → 2992.24] This is why in the absence of, you know, a face, I don't really get to engage with people in the same sort of humanness that we are all in.
[2992.70 → 2994.30] And so you're exactly right.
[2994.30 → 3000.50] I mean, over and over and over again, because you can identify and go, oh, that's why they're harsh.
[3001.00 → 3009.56] Or, you know, I recently had an interaction I had shared with someone that I was a competitive gymnastics coach for a number of years.
[3009.56 → 3015.78] And so somebody thought that my response to them when they were really struggling was kind of harsh.
[3016.02 → 3019.94] But they remembered that I had told them I was a coach for so long.
[3019.98 → 3023.98] And they're like, oh, this is just another side of her coming out.
[3024.06 → 3024.36] Right.
[3024.54 → 3027.54] And I'm not sure if I prefer it, but I get it.
[3027.60 → 3030.08] And then it switched for their reaction.
[3030.08 → 3032.86] Because then they're like, oh, wait, we're on the same team.
[3033.76 → 3037.50] She's not trying to, like, oppress me or fight back against me.
[3037.58 → 3041.08] She actually is helping me, trying to get me to where I want to go.
[3041.08 → 3045.02] That's a preview of Brain Science.
[3045.02 → 3052.68] If you love where we're going with this, email us to get on the list to be notified the very moment this show gets released.
[3053.00 → 3056.14] Email us at editors at changelog.com.
[3056.24 → 3061.68] In the subject line put in all caps, Brain Science with a couple bangs if you're really excited.
[3062.14 → 3066.44] You can also subscribe to our master feed to get all of our shows in one single feed.
[3066.44 → 3072.36] Head to changelog.com slash master or search in your podcast app for Changelog Master.
[3072.50 → 3073.10] You'll find it.
[3073.42 → 3077.54] Subscribe, get all of our shows and even those that only hit the master feed.
[3077.68 → 3079.68] Again, changelog.com slash master.
[3096.44 → 3096.54] Earned by
[3096.54 → 3102.44] www.gadjalakast.com slash master.
[3104.50 → 3105.02] Go, go, go.
[3105.04 → 3105.40] Go, go.
[3105.46 → 3105.60] Go, go.
[3105.68 → 3106.34] Go, go.
[3106.58 → 3107.40] Go, go.
[3107.44 → 3107.64] Go, go.
[3107.64 → 3108.26] Go, go, go.
[3108.26 → 3108.58] Go, go.
[3108.58 → 3109.22] Go, go.
[3109.22 → 3109.26] Go, go.
[3109.26 → 3109.48] Go, go, go.
[3109.48 → 3109.52] Go, go, go.
[3109.52 → 3110.48] Go, go, go.
[3110.48 → 3110.62] Go, go.
[3110.62 → 3112.44] Go, go, go, go.
[3112.70 → 3113.72] Go, go, go.
[3113.72 → 3114.50] Go, go, go.
[3114.52 → 3114.74] Go, go.
[3114.74 → 3116.86] Go, go, go.
[3116.86 → 3118.38] Go, go, go, go.
[3118.48 → 3119.94] Go, go, go.
[3119.94 → 3120.86] Go, go.
[3120.86 → 3122.56] Go, go, go.
[3122.96 → 3125.90] Go, go, go, go.
