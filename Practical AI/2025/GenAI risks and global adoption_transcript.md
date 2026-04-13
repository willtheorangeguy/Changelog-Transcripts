[0.00 --> 8.74]  Welcome to the Practical AI Podcast, where we break down the real-world applications
[8.74 --> 13.64]  of artificial intelligence and how it's shaping the way we live, work, and create.
[13.88 --> 19.14]  Our goal is to help make AI technology practical, productive, and accessible to everyone.
[19.48 --> 23.54]  Whether you're a developer, business leader, or just curious about the tech behind the
[23.54 --> 25.12]  buzz, you're in the right place.
[25.12 --> 29.84]  Be sure to connect with us on LinkedIn, X, or Blue Sky to stay up to date with episode
[29.84 --> 33.02]  drops, behind-the-scenes content, and AI insights.
[33.36 --> 35.88]  You can learn more at practicalai.fm.
[36.00 --> 37.52]  Now, on to the show.
[48.74 --> 52.20]  Welcome to another episode of the Practical AI Podcast.
[52.20 --> 54.30]  This is Daniel Whitenack.
[54.30 --> 60.48]  I am CEO at Prediction Guard, and I am joined, as always, by my co-host, Chris Benson, who
[60.48 --> 63.58]  is a Principal AI Research Engineer at Lockheed Martin.
[63.84 --> 64.52]  How are you doing, Chris?
[64.74 --> 66.02]  Hey, doing great today, Daniel.
[66.08 --> 66.86]  How's it going with you?
[67.14 --> 68.24]  It's going great.
[68.36 --> 74.12]  I traveled a bit over the weekend to run a mini-marathon, which was fun, but I am back
[74.12 --> 75.02]  safe at home.
[75.34 --> 82.82]  And, of course, safety is something that hopefully we can talk a little bit about today with our
[82.82 --> 90.66]  guests, who are Rick Kabayashi, who is co-founder and CEO at Citadel AI, and Kenny Song, who is
[90.66 --> 93.36]  co-founder and CTO at Citadel AI.
[93.56 --> 93.82]  Welcome.
[94.46 --> 95.34]  Thank you for having us.
[95.66 --> 95.84]  Yeah.
[95.92 --> 96.24]  Thank you.
[96.24 --> 98.76]  Yeah, it's great to have you both here.
[99.02 --> 101.36]  Good to get introduced to you both.
[101.50 --> 107.94]  I'm really excited about this conversation because, of course, security and safety related
[107.94 --> 111.10]  to AI is very close to my own work.
[111.20 --> 114.98]  And so it's always great to connect with people in this space.
[114.98 --> 122.20]  And, yeah, I'm also interested to hear a little bit, and I even saw some things on your website,
[122.60 --> 130.04]  you know, talking a little bit about some of the AI in Japan, some of the, I guess, regulations
[130.04 --> 132.68]  or guidelines for businesses that have come out there.
[132.78 --> 139.02]  So maybe before we get into the nature of what you're building and what you're doing, any
[139.02 --> 145.64]  thoughts on, for those out there that might be in the US or in Europe and be constantly
[145.64 --> 151.12]  exposed to the things that are going on in AI in those jurisdictions, any thoughts about,
[151.22 --> 156.70]  you know, what is the same or what stands out about what's happening with AI in Japan?
[157.28 --> 157.76]  So, yeah.
[157.82 --> 159.44]  Anyway, thank you very much for joining us.
[160.22 --> 161.82]  And my name is Rick.
[161.82 --> 169.94]  And as for the Japanese conditions, basically, I'm afraid to say it's around one, two years
[169.94 --> 173.10]  behind the US situation, basically up to now.
[173.72 --> 181.20]  But on the other hand, surprisingly, as for Gen AI, I think that Japan is one of the most
[181.20 --> 188.16]  advanced countries, not the development of the foundation models, but the utilization of
[188.16 --> 189.86]  the Gen AI applications.
[189.86 --> 197.72]  And probably it might be related to kind of Japanese kind of animation or cartoon.
[198.30 --> 205.04]  So, you know, like there are lots of, say, robot or some of the, say, animations which specify
[205.04 --> 207.38]  some of the AI or robot technologies.
[207.94 --> 211.66]  And, you know, Doraemon or there are lots of animation over there.
[212.30 --> 218.84]  And people are very, it's like getting familiar with such a kind of, say, talking with robot or
[218.84 --> 221.74]  some of these, say, advanced computers from the childhood.
[222.40 --> 229.66]  So, in that sense, I think that many people do not have any hesitation to work with or talk
[229.66 --> 232.44]  with like a chatbot or any Gen AI.
[232.78 --> 239.66]  So, in that sense, the huddle to introduce LNM or Gen AI in Japan is very low in that compared
[239.66 --> 241.90]  with the US or other countries.
[241.90 --> 247.88]  So, in that sense, development side or technology side, frankly speaking, Japan is behind the
[247.88 --> 248.76]  US situation.
[249.00 --> 256.20]  But as for the usage of such a kind of a Gen AI, I think, I hope Japan is one of the most
[256.20 --> 257.12]  advanced countries.
[257.68 --> 264.38]  Yeah, that's really interesting to hear the sort of perception side of things.
[264.38 --> 272.72]  And, of course, with more, maybe even more adoption or adoption that's ahead of maybe other places
[272.72 --> 280.36]  in the world, it could be that, you know, users or usage of the technology has hit some
[280.36 --> 288.36]  bumps along the road or has hit some problems, which I know is a lot of what you all are working
[288.36 --> 288.84]  on.
[288.84 --> 297.42]  What has been the situation in Japan around kind of regulation and business usage of AI?
[297.90 --> 306.76]  Is it on the sort of more regulated side or less regulated side in terms of the government and, I guess,
[307.74 --> 312.78]  regulation in terms of security or safety, privacy, these sorts of things?
[313.52 --> 318.04]  I think Japan is in the middle between the EU and the US situation.
[318.04 --> 321.58]  So, they say that it's a soft approach.
[321.84 --> 327.68]  So, there is no strict, say, regulation in Japan, but there are lots of kind of guidance
[327.68 --> 328.34]  in Japan.
[329.18 --> 336.62]  And people are, say, have already noticed some of the issues on the security side or safety
[336.62 --> 337.50]  side of AI.
[337.50 --> 344.56]  And on top of that, because they are, say, trying to introduce LLM applications for, like,
[345.32 --> 347.28]  contact center applications.
[347.64 --> 354.80]  So, they are concerned about more, say, kind of reputational risks rather than security risks.
[354.80 --> 362.34]  So, in that sense, they understood the importance of the safety of the AI or trustworthy of the AI,
[362.88 --> 367.84]  but more, say, concerned about reputational risks rather than security risks.
[367.84 --> 373.46]  I'm curious, as we're kind of talking about the adoption and the environment around that,
[373.82 --> 378.98]  is you kind of mentioned that in Japan, it's very, you know, people are really getting into
[378.98 --> 382.70]  the utilization of LLMs and generative AI.
[383.24 --> 390.08]  Do you have any kind of thoughts around, you know, what is it that's driving that, you know,
[390.12 --> 392.50]  compared to other countries that you've observed?
[392.50 --> 397.68]  If you're looking at that kind of adoption in Japan versus the U.S. or versus Europe or whatever,
[398.24 --> 399.44]  any thoughts around that?
[399.50 --> 405.56]  Because I had observed that as someone in the U.S. that Japan seemed to be implementing.
[405.80 --> 410.74]  And I was kind of curious if there was, you know, what was kind of the driving force there that
[410.74 --> 417.06]  got the utilization up, especially among just, you know, your typical average everyday folks there,
[417.16 --> 419.18]  not, you know, outside of the AI industry.
[419.80 --> 421.44]  I would love your thoughts about that.
[421.44 --> 429.82]  I'm not so sure the background reasons why Japan is more aggressive to introduce such a kind of
[429.82 --> 431.12]  LLM applications.
[431.80 --> 438.12]  Probably, as I said, people have lower, say, risk of perception, I may say.
[438.58 --> 445.80]  In some cases, in Japan, like a chatbot or kind of, say, new technology might be a kind of friend
[445.80 --> 446.58]  in a sense.
[447.04 --> 447.26]  Sure.
[447.26 --> 453.04]  But in U.S. side, such a kind of a new AI is kind of an enemy of a human.
[453.30 --> 458.86]  So there's kind of a little bit of a cultural difference in terms of how that openness to
[458.86 --> 459.80]  adoption and stuff.
[460.26 --> 461.80]  So, yeah, that would make sense.
[461.90 --> 462.86]  That would make sense to me.
[463.20 --> 463.42]  Yeah.
[463.42 --> 470.08]  And I guess sometimes your friends can potentially hurt you, even if they're not trying, which
[470.08 --> 478.10]  I know you all are kind of involved in both, you know, the evaluation of these systems,
[478.34 --> 484.58]  you know, running metrics against these systems and kind of building trust in a very real way.
[484.58 --> 490.68]  Kenny, I'm wondering if we bring you in here and maybe just, you know, safety and security
[490.68 --> 498.84]  around AI is such a broad topic now with so many people addressing it from so many different
[498.84 --> 499.64]  perspectives.
[500.02 --> 506.94]  I'm wondering if you could help us zero in on maybe the kinds of problems that you all are
[506.94 --> 513.44]  exploring and how those fit kind of more generally into the landscape of, I guess, security risks
[513.44 --> 516.34]  or threats as related to AI.
[516.86 --> 517.18]  Definitely.
[517.54 --> 517.70]  Yeah.
[517.76 --> 519.54]  So thank you for having us on the podcast.
[519.68 --> 520.24]  My name is Kenny.
[520.38 --> 522.72]  I'm the co-founder and CTO of Citadel AI.
[523.32 --> 529.84]  So what we do at Citadel is we build software tools to help organizations test, monitor and
[529.84 --> 531.68]  govern their AI systems.
[531.68 --> 539.24]  And in the world of LLMs, when customers come to us, they usually have some proof of concept
[539.24 --> 540.94]  that they've been developing internally.
[541.52 --> 543.48]  So they've been using some foundation model.
[543.66 --> 546.00]  They're building some chatbot or some agentic workflow.
[546.80 --> 551.04]  And they come to us when they want to make that proof of concept production ready.
[551.84 --> 556.68]  And usually their main problem is they want to mitigate some of the risks that they see.
[556.68 --> 563.10]  So things like hallucinations, toxicity, or users trying to prompt inject the system.
[563.70 --> 566.66]  They're looking for a solution to these types of problems.
[566.94 --> 569.86]  And that's where we come in as a tool provider.
[570.50 --> 570.60]  Yeah.
[570.82 --> 576.74]  And how does that, I guess, how are you seeing when you're interacting with your customers
[576.74 --> 578.56]  or they're coming to you with these problems?
[578.70 --> 584.90]  What is the impact of those problems like hallucination or injection?
[584.90 --> 590.78]  Is that something that is causing real problems or something that they've sort of heard about
[590.78 --> 594.60]  that they're concerned about, but it's maybe not causing a real problem?
[594.60 --> 599.08]  Or what are you seeing there in terms of, I guess, the impact?
[599.32 --> 602.84]  Let's say I just want to throw caution to the wind and ignore these things.
[603.34 --> 612.00]  What's the bad side of this that could happen were I to kind of take that more loose approach?
[612.84 --> 613.36]  Any thoughts?
[613.36 --> 616.20]  Yeah, I think it's usually a mix of both.
[616.72 --> 622.86]  And it also depends on the sort of the risk appetite of the company that's developing the system.
[623.58 --> 629.82]  And typically our customers are larger enterprise companies, both inside of Japan and outside of Japan.
[630.38 --> 633.58]  And so they have very mature risk management practices.
[633.58 --> 640.82]  And before they launch these POCs into a production service, whether that's internal facing or external facing,
[641.40 --> 646.70]  they want to make sure that they have appropriate controls in place to manage the risk.
[646.82 --> 654.20]  And they've properly identified the potential risks, reputational data, security, and so on.
[654.20 --> 660.18]  So yeah, I think for the customers we talk to, it's generally a big concern for them.
[660.44 --> 667.64]  And they come to us with the problem of mitigating some of these risks that they've already identified.
[667.64 --> 675.26]  I'm curious, as you've kind of identified, you know, what that kind of the strata of customers that you're looking at there,
[675.90 --> 686.56]  what is kind of, is there something that definitively kind of separates that kind of mature, larger organization from some of the smaller ones?
[686.56 --> 689.82]  Do they have a different set of problems that they're coping with?
[689.96 --> 695.62]  Or maybe just haven't gotten far enough along in terms of maturity and risk management?
[696.66 --> 703.08]  At what point do you see the uptake kind of falling off within maybe smaller organizations?
[703.50 --> 707.94]  You know, what does that look like as you move from that upper strata into the mid-tier?
[708.68 --> 715.08]  I think my general perspective is that there's two ends of the spectrum of like startups to enterprise company.
[715.08 --> 721.32]  And for startups, the risk is fairly low because you don't have a brand to protect.
[721.46 --> 723.32]  You don't have an existing business to think about.
[723.96 --> 729.28]  And so you can just launch these POCs out to your customers very quickly and you can iterate quickly.
[729.58 --> 733.62]  For enterprise customers, they tend to be more guarded.
[734.36 --> 737.70]  They have a closer eye on potential risks to the business.
[737.70 --> 751.70]  And those are the customers that sort of really want pretty robust testing before deployment and also monitoring and potentially real-time guardrails sort of filtering after deployment.
[752.34 --> 754.50]  Yeah, I think it depends a bit on the size of the company.
[755.26 --> 760.48]  Yeah, I'm wondering with that, like as you're kind of looking to those types of organizations,
[760.48 --> 764.40]  I'm curious a little bit of the backstory of Citadel.
[765.22 --> 774.12]  Maybe, Rick, you could tell us a little bit of kind of how you came to these problems because you seem like you have customers now.
[774.22 --> 775.94]  You've developed some of these things.
[776.14 --> 777.18]  When did that happen?
[777.32 --> 781.32]  How early was that in kind of was that before Gen.AI?
[781.68 --> 784.78]  Was that, you know, as Gen.AI was coming up?
[784.78 --> 794.18]  And how did things develop in terms of your thinking around these problems and how you would bring something to the market in terms of addressing them?
[794.52 --> 797.44]  So in that sense, it was before Gen.AI.
[797.76 --> 803.64]  And actually, the person who came up with such a kind of idea is not me, but Kenny.
[804.00 --> 807.32]  So Kenny has worked in Google Brains.
[807.82 --> 811.22]  And he was one of the core members of the TensorFlow team.
[811.22 --> 824.42]  So he's taking a leadership to develop most advanced AI technologies in Google and found that there should be a lot of risk about the trustworthiness or safety of the AI.
[825.20 --> 829.62]  And he believes that probably he is the best person to explain by himself.
[829.62 --> 849.90]  But anyway, he reached the idea that some of the tools which protect that kind of safety or security issues would be, say, should become popular, especially in the enterprise companies where they may not have, say, a bunch of AI engineers inside.
[850.40 --> 851.46]  So that is a background.
[851.86 --> 857.54]  And our company name, Citadel itself, is, say, shown what we are focusing.
[857.54 --> 862.04]  So Citadel is, as you know, saying like a vault or castle.
[862.30 --> 866.84]  So we are the company to, say, protect such a kind of risk.
[867.02 --> 874.96]  I mean, human from AI risk, such kind of a concept is, say, based on our company name.
[875.46 --> 875.90]  Yeah.
[875.94 --> 877.04]  Anything to add there, Kenny?
[877.34 --> 879.62]  Yeah, that's a pretty good overview of the background.
[880.04 --> 883.36]  When we started the company, it was at the end of 2020.
[883.36 --> 886.44]  So it was before the era of large language models.
[886.92 --> 896.88]  And we were initially really focused on helping organizations monitor their traditional predictive AI models, so tabular models, vision models, that kind of thing.
[897.60 --> 903.52]  And about two years ago, we started getting a lot more interest from our customers in LLMs.
[903.52 --> 908.24]  And how do we, you know, reliably test this new technology?
[908.40 --> 912.12]  How do we integrate it into our workflows and our business applications?
[912.92 --> 919.32]  And so these days, I think a lot of our new customers come to us with LLM types of questions.
[919.82 --> 924.80]  And then we still have a lot of existing customers that work more on the predictive AI side.
[924.80 --> 928.08]  So, Kenny, I'd like to follow up.
[928.14 --> 940.10]  As you guys were kind of developing the idea, going back to that a moment for the company, and Rick mentioned that you had been there at Google Brain and that you were on the TensorFlow team.
[940.32 --> 951.96]  I'm curious, you know, for me, as someone who's used TensorFlow a bit, and so that was like, oh, wow, you know, one of the people who helped put that together.
[951.96 --> 965.46]  I'm curious what parts of the experiences you had there led into the formation of Citadel in your mind as you had some of the insights that you might have developed in your previous employment.
[965.76 --> 970.98]  Did any of that, you know, how did that lead to what Citadel does?
[971.40 --> 974.66]  How did that kind of bring forward when you and Rick started the company up?
[975.18 --> 975.32]  Sure.
[975.54 --> 978.62]  So a bit more about my personal background.
[978.62 --> 989.60]  So in 2017 to 2020, I was working at Google Brain as a product manager, and my team was responsible for building machine learning infrastructure at Google.
[990.10 --> 999.96]  So this included TensorFlow and also other platforms like TFX, TensorFlow Extended, and some of the work on Google Cloud's AI platforms and so on.
[1000.02 --> 1004.46]  So sort of the software foundations that power a lot of Google's machine learning applications.
[1004.46 --> 1009.84]  And I think Google tends to be pretty ahead of the curve in AI adoption.
[1010.24 --> 1013.52]  And I think back then it was more called machine learning rather than AI.
[1013.82 --> 1021.72]  But basically what we worked on was making models at Google more reliable at Google production scale.
[1021.72 --> 1031.26]  And that usually meant building these pretty sophisticated pipelines that not only target training the models, but also serving them in production.
[1031.94 --> 1041.66]  So we had pretty robust systems for monitoring data drift and validating data that enters production models, monitors the output of these models.
[1041.66 --> 1048.62]  And, you know, you know, it's very important to use and you know, you know, you know, at Google, you can afford to have hundreds of platform engineers build out this kind of infrastructure to use internally.
[1049.28 --> 1054.96]  But for most other types of organizations, they can't make that level of investment in internal platforms.
[1054.96 --> 1061.92]  and we felt that there was an opportunity to sort of build some of these model monitoring
[1061.92 --> 1065.28]  and data validation tools for other companies.
[1066.22 --> 1069.12]  And so that's where the idea of Citadel AI kind of started.
[1069.84 --> 1078.52]  And when we started the company originally, we focused a lot on adversarial attacks, actually,
[1078.52 --> 1081.50]  back in 2020, since it was a very hot research topic.
[1081.50 --> 1089.40]  So basically, you know, designing noise and images and other types of input data to trick models into making the wrong predictions.
[1089.68 --> 1095.12]  We sort of found that after a few months, this wasn't really a problem that companies were interested in.
[1095.34 --> 1098.52]  It's like a very interesting research problem, but less interesting commercially.
[1099.26 --> 1104.24]  So after that, we pivoted towards more observability and testing of these predictive models.
[1104.94 --> 1108.80]  And these days, we focus a lot more on LLM testing and monitoring.
[1108.80 --> 1113.74]  Right. And maybe you could just give us, you know, going back to you, Rick,
[1113.80 --> 1119.94]  maybe you could just give us a few examples that stand out of kinds of companies
[1119.94 --> 1125.32]  and the kinds of models that they're running and the way that or that some of the things
[1125.32 --> 1129.80]  that they would be interested in tracking or detecting or observing.
[1129.80 --> 1136.80]  A few concrete examples might help our audience kind of grasp some of the cases that you're working with.
[1137.10 --> 1142.66]  One of the largest customers in Japan is the financial industry, surprisingly.
[1143.52 --> 1151.96]  So like banks or insurance companies or security companies are very aggressive to introduce LLM applications
[1151.96 --> 1158.86]  into their core operations, such as like a contact center or internal applications.
[1159.90 --> 1169.68]  And when they say they can go through POC stage and when they get into commercial operations,
[1169.96 --> 1174.44]  they start caring about some of the kind of safety issues.
[1174.44 --> 1180.78]  So because those financial industry is governed by the government itself.
[1180.78 --> 1188.74]  So in that sense, different from regulation-related AI, they have already been kind of regulated
[1188.74 --> 1192.58]  by traditional, say, financial regulations.
[1193.40 --> 1201.34]  So if, say, LLM applications behave badly, that damages their core businesses.
[1201.34 --> 1212.94]  So to introduce such a kind of AI application is to differentiate or advance their services compared with their competitors.
[1213.58 --> 1224.04]  But by introducing new technologies, if their core business is damaged, that would be very, say, huge negative impact.
[1224.04 --> 1235.62]  So, and also, if the AI behave badly, as I said, their, say, the Japanese government may, say, in some cases, call or punish them.
[1235.84 --> 1243.16]  So that is one of the most largest risks for them to introduce LLM-gen AI applications.
[1243.82 --> 1252.20]  So what we are doing is to making sure that such kind of, say, bad behavior will not happen in their application or not.
[1252.20 --> 1257.50]  And making sure that they can safely introduce, say, go into commercial operation.
[1257.94 --> 1264.82]  So some of the leading bank company or insurance company is our, say, our customers.
[1265.64 --> 1265.72]  Gotcha.
[1265.82 --> 1268.14]  I'm curious if I could follow up on that for a second.
[1268.78 --> 1276.02]  With, when you're, we've kind of talked about the notion of risk management in general that that industry is dealing with.
[1276.02 --> 1301.94]  How do they, given the risks for a large, you know, organization to implement LLMs, do you have any insight into how they're making the risk management judgment on the benefits of implementing maybe a new chat bot versus the potential downside where, you know, as you pointed out, could be damage to brand, damage to core operations, damage from a regulatory standpoint.
[1301.94 --> 1306.98]  I mean, that's, as I'm listening to you, that does sound very risky, you know, from that perspective.
[1307.58 --> 1310.70]  How do they make, how do they evaluate that?
[1310.78 --> 1314.06]  Like, say that they know that they want to come to Citadel and get that help.
[1314.28 --> 1324.30]  What, do you have a sense from your customers what a typical balance on that is of the benefit of the LLM utilization versus the downside of if things go off?
[1324.36 --> 1326.70]  How do they, what are they thinking when they come to you in that way?
[1326.70 --> 1331.72]  So, in that sense, they fully understand that balancing is very important.
[1332.04 --> 1340.26]  So, to protect the risk so much may, say, delay the, say, the service advancement.
[1340.92 --> 1350.14]  On the other hand, say, without having any security or safety test, they may get into bad situation.
[1350.14 --> 1355.12]  So, they need to, how to balance such a kind of risks and benefit.
[1355.98 --> 1363.76]  And they have set up several, like, internal organizations to manage such a kind of risk inside.
[1364.42 --> 1371.32]  So, yeah, as you can easily imagine, financial industries, they are a very structured company.
[1371.32 --> 1376.22]  So, there are some, like, risk management department inside.
[1376.80 --> 1382.92]  And in some cases, there are, like, AI governance team inside or something like that.
[1383.20 --> 1388.22]  So, they jointly work together and try to manage such a kind of a risk.
[1388.48 --> 1396.36]  And at the same time, they try to, say, introduce the advanced system so that they can differentiate themselves from others.
[1396.36 --> 1402.36]  And especially, as for the contact center, probably the same situation in the U.S.
[1402.76 --> 1412.88]  But when the consumer, end user, try to reach out to banks or insurance company and call it a free dial,
[1413.46 --> 1418.06]  in many cases, they can't easily, say, reach to the contact center person.
[1418.30 --> 1421.10]  They have to wait 30 minutes or something like that.
[1421.10 --> 1430.72]  So, because of that situation, they are so aggressive to introduce such a kind of application into contact center and the internal purposes.
[1431.50 --> 1440.36]  And I'm just thinking about this scenario where you have the contact center, you're introducing whatever it is, a chatbot, a voice assistant, that sort of thing.
[1440.36 --> 1451.88]  And then I'm thinking back to what Kenny was talking about, about kind of how the company started evaluating models that were not Gen.AI models yet.
[1452.08 --> 1461.54]  And I'm wondering, Kenny, if you could help us think about what needs, because if I'm understanding part of what you all are doing,
[1461.64 --> 1466.28]  part of it is evaluating the risks of a particular model or system.
[1466.28 --> 1471.64]  And part of it is observing those and monitoring those in real time.
[1472.40 --> 1479.84]  And if I think about like a traditional model, let's say a model that detects tumors in medical imagery, right?
[1479.88 --> 1484.56]  I can have a very nice sort of ground truth data set.
[1485.02 --> 1490.22]  And, you know, maybe it's hard to get because there's some privacy concerns, but I can still get it.
[1490.22 --> 1491.68]  I need to get it to train my model.
[1492.28 --> 1500.06]  And I, you know, have very specific metrics, right, around whatever it is, accuracy, F1 score, etc.
[1500.28 --> 1507.64]  I can sort of grasp what the, you know, performance of that model is, maybe even compare it to human performance.
[1507.64 --> 1517.78]  With something like a call center, in some ways, people might struggle to connect that to real metrics that make sense, right?
[1517.78 --> 1522.76]  Because it's like, oh, well, people could say anything, right, to the chatbot.
[1522.84 --> 1530.96]  How do I know one what's going to come in, you know, either from a normal usage or malicious usage or whatever?
[1531.10 --> 1534.28]  And how do I connect that to any sort of metric around a model?
[1534.40 --> 1540.98]  So I think sometimes people struggle with this idea of metrics and Gen AI models or Gen AI systems.
[1540.98 --> 1555.26]  Could you help maybe clarify, like, what are some of the relevant metrics that people could think about in terms of these systems that might help them understand, you know, how the systems are behaving?
[1555.96 --> 1557.88]  Sure. Yeah, that's a very spot on question.
[1558.24 --> 1561.80]  I guess before I talk about specific metrics, I'll just take a step back first.
[1561.80 --> 1567.70]  And if we sort of think at a high level, what is the same between predictive AI and generative AI?
[1568.28 --> 1574.10]  I think the structure of how you maintain reliability is basically the same, right?
[1574.12 --> 1578.04]  You need testing before deployment and you need monitoring after deployment.
[1578.88 --> 1584.88]  And it's also very similar to, like, traditional software applications, right, where you have automated tests and automated monitoring.
[1584.88 --> 1588.00]  And so I think that part is the same.
[1588.68 --> 1599.94]  But the part that's much trickier for generative AI is that usually, as you mentioned, you don't have ground truth in the same way that you do for a classification data set, for example.
[1600.42 --> 1605.46]  And so the metrics that you used for evaluation are not as well defined.
[1605.46 --> 1609.00]  So you can't measure accuracy, you can't measure precision or recall.
[1609.78 --> 1616.96]  And the output of a generative AI model is also much more complex than just, like, a probability score.
[1617.70 --> 1626.48]  And so in that environment, it's very hard to determine how do we actually evaluate these things in a quantitative and objective way.
[1626.48 --> 1635.98]  So the approach that most of our customers take and most of the industry has gone in is basically using LLM as a judge.
[1636.44 --> 1645.52]  So you can craft these evaluation prompts that ask an LLM to evaluate some quality of some generated text.
[1645.90 --> 1648.88]  So it could be, you know, a very simple example is sentiment.
[1649.18 --> 1652.92]  So you evaluate the sentiment of some text.
[1652.92 --> 1657.24]  You could do that with traditional, like a sentiment classifier as well.
[1657.92 --> 1670.54]  But there are more sophisticated metrics such as, you know, detecting hallucinations against some ground truth document or measuring the relevance of the answer relative to the question.
[1670.84 --> 1677.48]  Or you might have more, we call them custom metrics that are sort of designed to be domain specific.
[1677.48 --> 1688.18]  So if you have, like, a refund chatbot, you can design a metric that measures if the chatbot adheres to your company's refund policy.
[1688.96 --> 1694.74]  And so these metrics, they're very flexible because you can design the evaluation prompt in natural language.
[1694.74 --> 1700.44]  And in our tools and our open source libraries, we have a set of built-in metrics.
[1700.70 --> 1702.74]  It's like a library of metrics you can choose from.
[1703.26 --> 1709.64]  But for many of our customers, they also extend those built-in metrics to customize them to fit their business applications.
[1709.64 --> 1730.72]  So, Kenny, you were mentioning this sort of idea of LM as a judge, which is, you know, using a model to evaluate the model in some sort of axis of performance or some quality, which definitely seems like a flexible option.
[1730.72 --> 1740.56]  But also, some people, you know, some people might be thrown off by this sort of circular using a model to evaluate a model.
[1740.90 --> 1745.86]  Also, there's sort of this, you know, you then have a model that's evaluating the model.
[1745.98 --> 1748.74]  So how do you evaluate the model that evaluates the model?
[1748.92 --> 1751.38]  And you kind of get in this.
[1751.38 --> 1765.84]  How have you all navigated that side of things, both kind of in terms of using the larger model, making sure that the evaluations are sound and also kind of transferable, you know, one model to the other?
[1766.42 --> 1773.94]  And, you know, maybe benchmarking the system over time, because also the models you might want to use as evaluators might change over time.
[1775.00 --> 1776.42]  Yeah, also a very good question.
[1776.66 --> 1780.12]  And it's a question that we get from our customers quite a lot as well.
[1780.12 --> 1793.50]  And the way that we generally approach the evaluation workflow, which includes designing these metrics, is not usually human judgment and taste is treated as the gold standard.
[1793.84 --> 1801.28]  But the problem with having humans evaluate every experiment with your LLM system is that it's very expensive and it's very slow.
[1802.06 --> 1807.48]  And so in the ideal world, you would design these LLM as a judge metrics that can mimic human preferences.
[1807.48 --> 1814.76]  And so in our software tooling, this is what we design specific workflows to help users to do.
[1815.18 --> 1823.42]  Usually when a customer starts on an evaluation project, they'll, you know, of course, think about the evaluation criteria that's important.
[1823.42 --> 1827.50]  But then they'll also have humans do a small set of that evaluation.
[1828.02 --> 1832.08]  So maybe like 50 to 100 of these manual annotations.
[1833.08 --> 1841.72]  And from there, you can design LLM automated metrics and measure their correlation and accuracy against the human judgment.
[1842.12 --> 1848.76]  You usually need to iterate a few times to get that custom LLM metric as close as possible to the human judgment.
[1848.76 --> 1852.00]  But then once you have that, it's very powerful, right?
[1852.08 --> 1856.56]  You have this automated metric that is a very good proxy for human judgment.
[1856.96 --> 1859.62]  And it's automated, which means you can run it at scale.
[1860.02 --> 1864.36]  You can deploy it during evaluation, but also in monitoring as well.
[1864.72 --> 1868.82]  And you can also potentially use that as a production guardrail in our firewall.
[1868.82 --> 1878.86]  Rick, I was wondering, I know we've kind of alluded to it that, you know, the two sides of the equation in terms of testing the models and then monitoring.
[1879.42 --> 1892.60]  Could you talk a little about Citadel Lens and Citadel Radar, how you bring them to customers and what the relationship is between those two products that you're bringing to your customers?
[1892.60 --> 1903.52]  And, you know, how do you present them when somebody is interested in being able to bring this level of security to the models that they're interested in?
[1904.16 --> 1904.46]  Sure.
[1905.04 --> 1910.14]  First of all, now we are merging radar features into Lens.
[1910.60 --> 1916.38]  So Lens can provide both testing function and monitoring functions together at this stage.
[1916.38 --> 1932.34]  And as for the balancing or difference between testing and monitoring, as Kenny mentioned, especially in the case of LLM, how to customize human, say, setting back.
[1932.60 --> 1943.10]  So our system is in the concept that the system should follow the human rather than human has to follow the system.
[1943.10 --> 1957.74]  In essence, we set the human annotation or human judge as a first priority and try to our metrics to be customized to the human judge.
[1958.16 --> 1960.70]  So that is a very important point.
[1960.70 --> 1974.74]  And to make it happen, we need to, or the customer need to go through testing phase first so that all the, say, metrics should be aligned with the human judgment.
[1975.48 --> 1984.40]  So that, and we can make use of the same custom metrics during the, say, the monitoring phase or firewall stage.
[1984.40 --> 1999.10]  So in essence, even though final goal might be a monitoring or firewall, but before going to that stage, how to test and customize the metrics is very important.
[1999.26 --> 2005.22]  I mean, very critical to protect the safety and security and reputational risks.
[2005.50 --> 2011.04]  So we recommend, strongly recommend to start from testing phase first.
[2011.04 --> 2018.54]  So testing phase is not just testing, but customize your metrics into your, say, professional, the persons.
[2019.08 --> 2020.36]  So that is a testing phase.
[2020.56 --> 2023.90]  And after that, they can go into monitoring phase.
[2024.04 --> 2026.70]  So that is our approach to the customers.
[2027.36 --> 2037.82]  And I'm wondering, you know, either one of you could answer this, but why is it, and this may be obvious to maybe more of the software engineering type crowd,
[2037.82 --> 2053.62]  but maybe less so to some others outside of that crowd, why is it important to, once you've tested your model, to actually monitor it online for maybe the things that are potentially problematic inputs,
[2053.62 --> 2068.26]  whether that's a security thing like a prompt injection or maybe something outside of the, you know, some type of input that you want to filter out, like IP going in or something that doesn't fit your policy?
[2068.74 --> 2074.52]  Why is it important to have that monitoring piece and not just the testing piece?
[2074.52 --> 2082.62]  Because if I test my model and I convince myself that it can't be prompt injected, which I'm saying that sort of in jest,
[2082.76 --> 2088.80]  because, you know, as you all know, every model, there's no perfectly aligned model.
[2089.00 --> 2091.40]  There's no, every model is vulnerable to various things.
[2091.40 --> 2096.52]  But let's say that I convince myself of high performance in one of these areas.
[2096.52 --> 2103.60]  Why then is it useful and necessary then to monitor that over time or in real time?
[2104.32 --> 2107.76]  Technically, probably Kenny is also, again, the best person.
[2107.76 --> 2121.30]  But even if the customers can go through the testing phase, the market condition or say, kind of say, the human reaction may change over time.
[2121.30 --> 2134.42]  So if we are safe right now, but if anything, say something new happens today, what we say guaranteed today may not apply tomorrow.
[2134.42 --> 2136.90]  So it's a very general thing.
[2136.90 --> 2145.22]  But say, in that sense, the key monitoring is very important to protect our customers,
[2145.22 --> 2151.02]  even if the market condition or the world condition change or economic condition change.
[2151.30 --> 2156.76]  Yeah. And just to give a concrete example of why you may want monitoring.
[2156.94 --> 2162.72]  So we really view them as complementary and you'd really need both if you want to make a system reliable.
[2163.62 --> 2170.86]  So, for example, if you have like an answer quality metric that measures how high quality an answer is,
[2171.30 --> 2175.94]  you should, of course, use that for testing to make sure that it meets some like, you know, 80, 90 percent bar.
[2175.94 --> 2182.48]  But then in monitoring, you actually want to measure quality of the real answers that your chatbot is giving to real customers.
[2182.98 --> 2188.86]  Right. So from a quality perspective, it makes a lot of sense from like a safety and risk reduction perspective.
[2188.86 --> 2197.48]  Another example is that, you know, as you mentioned, Dan, during testing, you might test a bunch of prompt injections against your system.
[2197.68 --> 2201.22]  But then in deployment, you have real users.
[2201.38 --> 2204.36]  Some of them are adversarial. Some of them are actually trying to prompt inject.
[2204.80 --> 2207.38]  They may do it in creative ways that you haven't tested before.
[2207.38 --> 2214.60]  Right. And so you may want some some kind of guardrail that will automatically detect those attempts and filter them out,
[2214.60 --> 2219.72]  even if you're sure that the model is robust to, you know, 90 percent of these attacks.
[2220.20 --> 2224.68]  I'm curious. You guys have some open source available out there.
[2224.90 --> 2227.98]  I know one of the tools is LangCheck.
[2228.36 --> 2231.54]  Can you talk a little bit about your approach to open source?
[2231.54 --> 2242.80]  For context, LangCheck is a is our open source Python library that contains a suite of metrics that are built in that you can use for evaluating the quality of text.
[2243.04 --> 2251.90]  One of our motivations for creating this library is that I think we launched it in October of 2023, roughly.
[2252.26 --> 2260.86]  And around that time, there weren't a lot of sort of industry standard metrics and practices for evaluating text.
[2260.86 --> 2263.94]  Particularly in non-English languages as well.
[2264.50 --> 2267.88]  So there was some focus on, you know, these metrics in English.
[2268.08 --> 2274.50]  But we work with a lot of customers that have Japanese texts or Chinese or German and these other languages.
[2274.50 --> 2278.72]  And we wanted to make a library of these metrics that anyone can use.
[2279.26 --> 2282.46]  And we view this as a as a pretty good starting point.
[2282.70 --> 2287.26]  Right. So if you're if you just need like one or two metrics, you're comfortable writing code.
[2287.26 --> 2291.92]  You can use LangCheck and integrate that into your test pipeline or your monitoring system.
[2292.52 --> 2299.94]  But then if you want something production scale and you want an easy workflow to design custom metrics and test them against manual annotations.
[2300.42 --> 2302.56]  That's where our commercial product comes in.
[2302.56 --> 2310.08]  Makes sense. Yeah. And as we get a little bit closer to the end here, there's so many things.
[2310.28 --> 2321.82]  And this is such a in, you know, so many in-depth areas to go in, which is why it's great that there's, you know, wonderful people like yourselves exploring the topic.
[2321.82 --> 2335.70]  But I'm wondering if we could maybe talk just a little bit as we close out here about what you're excited about, about kind of, yes, Citadel, but maybe the kind of general ecosystem that you're a part of.
[2335.70 --> 2342.66]  As you look to the future, you know, what's what's exciting to each of you about how the ecosystem is developing?
[2343.06 --> 2345.48]  What's becoming possible with the technology?
[2346.16 --> 2350.96]  Yeah. What's inspiring to you or what are you thinking about in terms of the future?
[2350.96 --> 2352.68]  Maybe I'll start with you, Rick.
[2353.24 --> 2357.78]  Okay. So, yeah, now the chat GPT-5 is released.
[2358.22 --> 2371.10]  But when we, say, look back today from, say, five years later, I believe that, oh, this is a very premature, say, model or something like that.
[2371.10 --> 2377.92]  So in that sense, the technology advancement in the AI field is so rapid.
[2377.92 --> 2382.62]  And in that sense, yeah, there may be a lot of risks coming in.
[2382.90 --> 2387.28]  But on the other hand, there are mostly infinite opportunities.
[2387.28 --> 2410.56]  So you can find a huge, say, variety of possibilities, not only just, say, the AI directory-related technologies, but I believe some of the material products or machines or anything will change maybe within five or ten years.
[2410.56 --> 2421.02]  So in that sense, we are in the midst of the, say, period where anything can change, in that sense, especially technology-related.
[2421.02 --> 2428.22]  So there are lots of, say, risks may coming, and we like to protect such a kind of risk as a company.
[2428.72 --> 2435.40]  But on the other hand, people can find many possibilities, opportunities for you to try.
[2435.40 --> 2450.84]  So I strongly believe that we, so even though there are lots of issues in the world, but people can enjoy or, say, can, say, make best use of this opportunity, everybody.
[2451.50 --> 2451.58]  Yeah.
[2451.82 --> 2452.48]  Yeah, that's great.
[2452.64 --> 2453.70]  What about yourself, Kenny?
[2453.70 --> 2467.00]  Yeah, I think as a consumer of AI, in both my personal life and work, from a consumer perspective, it's really exciting to benefit from all the advancements in these new AI tools and models.
[2467.40 --> 2472.46]  I really loved O3 as a model in ChatGPT, and I love using Cursor.
[2472.70 --> 2477.00]  And I'm excited for these tools to become more and more agentic over time.
[2477.18 --> 2479.20]  And I think that's sort of the trend that you see.
[2479.20 --> 2489.46]  If you just look at ChatGPT, originally, it was just like 3.5 and GPT-4 that just answer a question based on a forward path of the model.
[2489.64 --> 2494.80]  But now these models will search the internet, and it'll sort of reason and think about what to search next.
[2495.22 --> 2498.98]  And as a result, the outputs have become a lot better.
[2499.74 --> 2504.20]  So really excited for that to improve even more from a consumer perspective.
[2504.20 --> 2516.26]  And then from a business perspective, I'm really excited to help bring these capabilities to our business customers and help them use AI more reliably and more effectively in their business.
[2516.64 --> 2517.48]  That's great.
[2517.74 --> 2517.96]  Yeah.
[2518.08 --> 2522.40]  Well, thank you both for taking time to chat with us today.
[2522.40 --> 2531.30]  And thank you both for the work and thought that you're putting into the tools that you're building and the open source projects that you're putting out there.
[2531.40 --> 2535.94]  It's a great benefit to the community and to the business world, of course.
[2536.20 --> 2538.12]  So thank you for the work that you're doing.
[2538.72 --> 2548.24]  And yeah, we'll look forward to keeping an eye on what you evaluate and protect us from next.
[2548.48 --> 2551.58]  So appreciate you both and hope you have a great evening.
[2551.58 --> 2552.50]  Thank you for joining.
[2552.86 --> 2553.72]  Thank you very much.
[2554.08 --> 2555.12]  Thank you for the conversation.
[2562.26 --> 2562.88]  All right.
[2563.06 --> 2564.48]  That's our show for this week.
[2564.84 --> 2571.74]  If you haven't checked out our website, head to practicalai.fm and be sure to connect with us on LinkedIn, X or Blue Sky.
[2572.02 --> 2577.74]  You'll see us posting insights related to the latest AI developments, and we would love for you to join the conversation.
[2577.74 --> 2582.00]  Thanks to our partner, Prediction Guard, for providing operational support for the show.
[2582.34 --> 2584.34]  Check them out at predictionguard.com.
[2584.76 --> 2588.36]  Also, thanks to Breakmaster Cylinder for the beats and to you for listening.
[2588.72 --> 2589.52]  That's all for now.
[2589.78 --> 2591.54]  But you'll hear from us again next week.
[2591.54 --> 2599.82]  We'll be right back.
[2599.88 --> 2600.22]  We'll be right back.
[2600.28 --> 2600.44]  Bye.
