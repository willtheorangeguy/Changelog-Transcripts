[0.00 --> 3.22]  The goal of any technology is to basically support humans, right?
[3.26 --> 3.94]  Not replace them.
[4.18 --> 8.18]  Wherever it can help automate and kind of de-bias human decision-making, we want to
[8.18 --> 9.64]  support that and not replace that.
[9.64 --> 14.48]  But at the same time, we want to make sure that we're not replacing human judgment.
[14.78 --> 18.84]  I think that the challenge that we have in our world, I don't know that we will have
[18.84 --> 24.68]  that choice, meaning that we don't have a person sitting in every kind of like critical
[24.68 --> 28.06]  decision junction and making that critical human judgment.
[28.48 --> 29.26]  It doesn't scale.
[30.00 --> 35.24]  Big thanks to our partners, Linode, Fastly, and LaunchDarkly.
[35.46 --> 36.18]  We love Linode.
[36.26 --> 37.68]  They keep it fast and simple.
[37.68 --> 40.16]  Check them out at linode.com slash changelog.
[40.28 --> 42.46]  Our bandwidth is provided by Fastly.
[42.82 --> 46.36]  Learn more at Fastly.com and get your feature flags powered by LaunchDarkly.
[46.62 --> 48.36]  Get a demo at LaunchDarkly.com.
[51.16 --> 54.62]  This episode is brought to you by me, myself, and AI.
[55.04 --> 59.06]  It's a podcast on artificial intelligence and business and it's produced by our friends
[59.06 --> 62.28]  at MIT Sloan Management Review and Boston Consulting Group.
[62.58 --> 66.74]  The question is, why do only 10% of companies succeed with artificial intelligence?
[67.24 --> 69.20]  That's the question they aim to answer with this podcast.
[69.80 --> 73.34]  Here's Google Cloud's Will Grannis on an unusual AI challenge.
[73.34 --> 88.20]  When I think about what AI is, I find the algorithms mathematically fascinating, but I find the use of the algorithms far more fascinating because from a technical perspective, we're finding correlations in extremely high dimensional nonlinear spaces.
[88.52 --> 90.72]  It's statistics at scale in some sense, right?
[90.72 --> 93.22]  We're finding these correlations between A and B.
[93.22 --> 96.76]  And those algorithms are really interesting and I'm still teaching those now and they're fun.
[97.22 --> 101.42]  But what's more interesting to me is what do those correlations mean for the people?
[102.02 --> 102.22]  All right.
[102.30 --> 106.92]  Me, myself, and AI is a collaboration between MIT Sloan Management Review and Boston Consulting Group.
[107.22 --> 108.66]  It's available wherever you get your podcasts.
[108.78 --> 111.10]  Just search me, myself, and AI.
[111.10 --> 136.76]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive, and accessible to everyone.
[136.76 --> 141.16]  This is where conversations around AI, machine learning, and data science happen.
[141.42 --> 147.54]  Join the community and Slack with us around various topics of the show at changelaw.com slash community and follow us on Twitter.
[147.68 --> 149.00]  We're at Practical AI.
[155.56 --> 158.74]  Welcome to another episode of Practical AI.
[159.10 --> 160.78]  This is Daniel Whitenack.
[160.78 --> 169.70]  I'm a data scientist with SIL International, and I'm joined as always by my co-host, Chris Benson, who is a tech strategist at Lockheed Martin.
[170.26 --> 170.92]  How are you doing, Chris?
[171.08 --> 171.86]  Doing very well.
[171.92 --> 172.68]  How are you today, Daniel?
[172.92 --> 173.88]  I'm doing well.
[174.06 --> 183.08]  I think this episode will release in the new year, but there's a lot of sort of year-end stuff happening to tie up loose ends and project plan for next year.
[183.24 --> 187.04]  So all good things, but yeah, trying to do all that stuff.
[187.04 --> 190.54]  The end of year time warp here, even though everyone's hearing it after the fact.
[190.54 --> 191.80]  Right, exactly.
[192.20 --> 192.98]  I'm pretty excited.
[193.36 --> 207.54]  I know that you and I have talked many different times on the podcast about where AI models can fail or go wrong, either in terms of data or in terms of their behavior.
[208.12 --> 216.90]  But maybe we haven't talked as much about ways to mitigate that problem, practically, and how people are approaching that.
[216.90 --> 224.48]  And we're really excited today because we have Jaron Singer with us, who is CEO of Robust Intelligence.
[225.30 --> 231.28]  And of course, they know all about how AI models fail and how to do something about it.
[231.42 --> 233.66]  So welcome to the show, Jaron.
[234.20 --> 235.08]  Yeah, great to be here.
[235.30 --> 236.64]  Thanks for having me, Daniel and Chris.
[237.42 --> 238.46]  I'm a big fan.
[238.46 --> 242.26]  I think I've listened to pretty much all the episodes.
[242.56 --> 244.02]  So it's great to be here.
[244.08 --> 244.36]  Oh, wow.
[244.54 --> 245.98]  Yeah, that's great.
[246.20 --> 248.02]  Well, it's wonderful to have you on the show.
[248.50 --> 263.02]  Could you maybe just start out by getting us up to speed, maybe for those that are out there that aren't really aware of the different ways in which AI models might fail and the sort of risk associated with that?
[263.02 --> 274.38]  Could you give us a little bit of an intro to maybe some of the highlights from that and either things you've seen or things in the community that kind of motivated you to think about this problem?
[274.80 --> 275.18]  Absolutely.
[275.58 --> 278.96]  You know, when we say that AI models fail, what do we mean, right?
[279.00 --> 282.40]  Like failure can come in all these sort of like different shapes and forms.
[282.86 --> 289.06]  You know, so maybe we, you know, we kind of like start with some examples that, you know, I think a lot of us in the AI community are familiar with.
[289.06 --> 301.26]  One example that's been like kind of a very famous one was the Microsoft chatbot example where Microsoft kind of like developed this, this chatbot, this AI chatbot that was really great technology.
[301.84 --> 308.10]  And, you know, but what they did is they basically, you know, the idea was this for this chatbot to like kind of mimic actual human conversation.
[308.46 --> 317.18]  And the way that they did that is they actually use, you know, kind of like data from Twitter, right, kind of to have, you know, train that bot.
[317.18 --> 328.56]  And when people figure that out, what they actually did is they actually, you know, kind of fed all sort of like kind of weird different things to the chatbot to the point where they realized that they can actually make this chatbot racist, right?
[328.62 --> 342.40]  So at the end, what you got is that kind of pretty quickly, I think within, you know, a few, I think it was like 36 hours after it was kind of released, you know, you had this chatbot that was kind of like spinning out all these sort of like awful racial slurs and Microsoft ended up shutting it down, right?
[342.40 --> 346.98]  So, you know, it's just kind of like one example where you have this like really elite technology, right?
[347.30 --> 358.86]  And once it falls into, you know, the wrong hands, right, it can obviously, you know, it can kind of be led astray and kind of be manipulated and all these kind of weird ways that we, you know, we never expected and intended.
[358.86 --> 362.48]  So there are all these sort of ways that, you know, that AI models fail.
[362.68 --> 382.82]  And, you know, even like kind of as of recent, like we've all read about, or some of us have read about, you know, Zillow's example, where if you went on Wired and you read like in June 15th, there's like kind of this beautiful headline about how Zillow is going to like improve its, you know, its predictive pricing, like on housing using kind of sophisticated neural networks.
[382.82 --> 392.16]  But then if you kind of read Wired again in November, it explained to you why Zillow failed with its AI pricing, AI based pricing, right?
[392.28 --> 402.74]  And basically, they kind of like let go, I think of like 25% of the, you know, of Zillow's kind of like employees and had huge kind of like economic implications for Zillow.
[402.74 --> 409.94]  So, and basically, you know, there, the failure came because of changing conditions and specifically it was because of the pandemic.
[410.28 --> 421.90]  So the models were trained using old data and then they applied them and then, you know, on, you know, on the world, which, you know, was experiencing a pandemic and that data was, you know, was very different.
[422.10 --> 426.36]  So this is what, you know, we call distributional drift and we saw failure of the AI models there.
[426.36 --> 439.56]  So these are just kind of like two, I think, kind of one famous example and one of the more recent examples, but of different, you know, totally different ways of in which AI systems can, you know, can just completely fail for different reasons.
[440.04 --> 440.20]  Yeah.
[440.28 --> 444.64]  So, so those are kind of like some examples and, and the implications are, you know, are obvious, right?
[444.82 --> 449.92]  You know, either, you know, we have like kind of very bad reputation, very bad risk.
[449.92 --> 452.46]  We're putting kind of people's safety at risk.
[452.46 --> 454.70]  So those are kind of big problems of experiencing.
[454.70 --> 470.66]  I definitely see on the one hand, you've sort of got these like behavioral problems of models where like, depending on what data you feed them or train them on or update them with, you kind of get this non-ideal behavior in, in one way or another.
[470.92 --> 481.46]  I'm curious about your perspective now, sort of being in this, this field and seeing how clients are using AI models, maybe more and more over time.
[481.46 --> 499.86]  What is the sort of, from your perspective, is there an increasing risk in the way in which people are using models, like the tasks that they're applying to, applying models to in business use cases where like the chat bot one is, is interesting and, you know, is bad PR for Microsoft.
[499.86 --> 512.68]  But like, are people starting to maybe apply AI models and maybe more risky business use cases versus sort of more toy problems or research type of settings?
[513.40 --> 514.08]  That's a great question.
[514.20 --> 525.80]  I think in general, right, regardless of like one organization or another, like we are in a world that is adopting algorithmic decision making that is completely based on AI.
[525.80 --> 531.40]  And this world is adopting this, this sort of automated decision making at an exponential, right, exponential pace.
[531.78 --> 536.72]  And some examples are examples that, you know, have been there out there for a while that we know, right.
[536.92 --> 552.20]  But it goes for, you know, things that are, you know, as simple as AI models being used for determining, you know, basically insurance rates, right, for home insurance, right, for, you know, home insurance and car insurance, but also for health insurance, right.
[552.20 --> 559.58]  And when these AI models can, you know, can have these sort of different failure points, right, failure modes that that has huge ramifications.
[560.06 --> 561.50]  Same with, with lending.
[561.72 --> 570.78]  So AI is used a lot in lending and deciding like, who gets a loan, you know, who gets a house loan, who doesn't get a house loan, who gets a car loan, who doesn't, and you know, and how much they have to pay.
[570.78 --> 584.94]  And we also see this in things like, you know, predictive policing, right, where police departments across the country are using AI models to basically decide on, you know, whether, you know, where they're going to be putting more, more forces, right.
[584.94 --> 589.36]  And all these things are, I think, kind of like the intentions are good, right.
[589.40 --> 596.32]  People want to, you know, want to make good decisions, and they want to do this in a fair way and automate, you know, that process somehow.
[596.64 --> 602.10]  But at the same time, with everything that we know about AI and its physical nature, you know, the risk is enormous.
[602.80 --> 610.66]  And I got a question about that is we've talked about some of these use cases, and you kind of think of maybe divide them up a little bit on the Microsoft side.
[611.14 --> 614.32]  There's failure that is intentional in nature.
[614.32 --> 623.26]  There's sort of these, for lack of a better word, adversaries out there, and they're taking advantage of the weakness of a model and seeing what they can do with the chatbot.
[623.64 --> 630.08]  And then you have these kind of environmental influences, such as the Zillow thing, where the world changed out from under you.
[630.22 --> 635.78]  It was no one person's intention to do that, but nonetheless, it had the same effect.
[636.02 --> 643.42]  Does the intentional and the unintentional, does that matter as you're dealing with these failure situations?
[643.42 --> 653.04]  Does it change the way that you approach the problem, or does that intention or lack thereof, you know, just because it happened, is that a factor in things?
[653.20 --> 654.58]  That's a very good question, right?
[654.70 --> 667.08]  Like, does it matter whether, you know, whether the AI failures are due to an adversary that's trying to create, you know, these failure modes, or they just sort of like happen because of, you know, changing natural conditions or whatnot?
[667.08 --> 670.44]  So I think the answer to that is, you know, yes and no.
[670.66 --> 672.52]  It like kind of, it matters and it does not matter.
[672.78 --> 676.94]  And in our approach, you know, and that's sort of like kind of the approach that we have in our company, right?
[677.24 --> 686.28]  In our company, the part where we think it does not matter, right, is where basically we put all these things under the category of risk, right?
[686.28 --> 700.40]  Where what we look at is we basically, we abstract that, like kind of, we abstract the root cause of the risk, right, away from, you know, we sort of say, well, it doesn't really matter, you know, kind of what has caused that model to fail, right?
[700.42 --> 704.92]  The important thing is that, you know, that the model does not fail for, you know, whatever, you know, whatever reason.
[704.92 --> 725.26]  So in that sense, we're kind of like, we take an approach where we're agnostic, right, to whether it was an adversary that fooled the model, whether it was the pandemic that changed the conditions, right, whether it was whether somebody really intended to, you know, misfeed, to put in like racial slurs, or it's just something that, you know, for whatever reason, you know, was picked up from the internet.
[725.62 --> 728.72]  So somehow like the root cause does not really matter, right?
[728.72 --> 740.92]  What's important is that we somehow are able to reduce it, right, from a technical perspective, right, to kind of like understand it and being able to protect the models from, you know, from this.
[741.38 --> 753.76]  Now, yes, it does matter, right, in the sense of, you know, kind of like the algorithms, you know, that you end up using to, you know, kind of protect models from, you know, one kind of failure to like another kind of failure, right?
[753.76 --> 769.66]  So, you know, the algorithms that you would use to protect the model from what we call like a distributional drift, like kind of changing in conditions like due to the pandemic are different from the algorithms that we use, right, to protect the model from being kind of handed kind of like adversarial input.
[769.66 --> 778.18]  On that point, are you seeing like, as you're engaging with clients and companies, are you seeing, I guess, two questions?
[778.30 --> 788.58]  One is, what is their perception of the main category of risk in those two cases, the adversarial or the sort of data drift and distributional change types of things?
[788.58 --> 804.08]  And what maybe from your perspective is the sort of reality, I guess, I guess maybe some companies have a natural, naturally a higher risk vector for adversarial parties coming against them just because of what they do or whatever.
[804.54 --> 806.48]  But yeah, I don't know if you have any thought on that.
[806.88 --> 808.66]  Yeah, I think that's a really interesting question.
[808.66 --> 818.50]  I think that it really depends on, you know, the company, but not only the company, you know, it actually, you know, like even, you know, different teams within a company can have different concerns.
[818.58 --> 825.26]  Right. You can imagine that you have a company where they have a team and that team is responsible for fraud detection in that team.
[825.36 --> 829.00]  Right. So the team that's dealing with fraud detection in the company.
[829.48 --> 838.34]  Right. They are constantly dealing with adversarial input and they very much care about protecting their AI from the thread vectors of adversarial input.
[838.34 --> 845.06]  Right. The same company can have another team and that team is dealing with forecasting, forecasting of different events.
[845.36 --> 847.78]  Right. And, you know, forecasting different events.
[847.78 --> 850.82]  Like they don't care about, you know, they don't think about adversarial input.
[850.82 --> 853.60]  They worry about, you know, rainy days changing.
[854.00 --> 858.14]  You know, if you're thinking about maybe like a company that's doing ride sharing or things like that.
[858.18 --> 864.82]  Right. So they care about the underlying, you know, the continuously kind of changing conditions and how that affects the models and predictions.
[864.82 --> 869.52]  And if you want to do this well. Right. Then you want to be able to kind of build a system.
[869.86 --> 874.38]  Right. That protects models from both these types of cases. Right.
[874.38 --> 881.10]  The cases where there's like, you know, there are adversaries that are like really just trying to change and manipulate, you know, financial transactions.
[881.10 --> 885.46]  Right. As well as the thread vector of just changing conditions.
[885.46 --> 892.06]  Right. With no adversary in place, but just sort of like changing conditions that can change with the predictions to the models.
[892.06 --> 914.04]  Change log plus plus is the best way for you to directly support practical AI.
[914.04 --> 924.96]  Join today and unlock access to a private feed that makes the ads disappear, gets you closer to the metal and help sustain our production of practical AI into the future.
[925.76 --> 934.04]  Simply follow the change log plus plus link in your show notes or point your favorite web browser to change log dot com slash plus plus.
[934.38 --> 938.22]  Once again, that's change log dot com slash plus plus.
[939.64 --> 941.96]  Change log plus plus is better.
[944.04 --> 974.02]  Change log plus is better.
[974.02 --> 975.50]  And so I just found anotheracción or PC and Microsoft Fun empez.
[975.50 --> 976.04]  Say you can see something wrong.
[976.04 --> 977.64]  The software and I'm always saying, you go for all the tools that are coming and then workflow and digital content.
[977.64 --> 999.26]  You can see those ideas
[999.26 --> 1006.94]  automation and human in the loop element of this, where like, if you're planning on creating an
[1006.94 --> 1013.26]  application, for example, with the OpenAI API, it's considered much higher risk if it's to
[1013.26 --> 1017.30]  automate something, right? And there's not going to be any sort of human in the loop to review
[1017.30 --> 1024.16]  things. As someone who kind of works to kind of manage and mitigate the risk in these types of
[1024.16 --> 1031.04]  scenarios, how do you view, I guess, as the industry gets more sophisticated at handling the
[1031.04 --> 1037.72]  risk, are we going to be able to automate things more? Or maybe is it that we deploy our models and
[1037.72 --> 1043.06]  we have monitoring infrastructure that helps us know when things are going wrong, but it's, you
[1043.06 --> 1048.50]  know, still automated? I'm wondering how you kind of view this shifting over time and view this
[1048.50 --> 1052.50]  need for humans in the loop in terms of the output of models.
[1052.50 --> 1056.96]  I think this is really important and really interesting, right? And I think that what
[1056.96 --> 1062.10]  you're saying from OpenAI, it just echoes what we're saying from, you know, from leading
[1062.10 --> 1066.52]  companies and platform in general. When you look at the state of the art, it's all going towards
[1066.52 --> 1071.54]  automation, right? So if you're using Databricks today, you can already, you're essentially kind
[1071.54 --> 1075.06]  of in Databricks notebooks, you can have the option of retraining your models automatically,
[1075.38 --> 1079.84]  right? So, and in general, that's kind of where the world is going. And I think that like within,
[1079.84 --> 1085.30]  I want to be careful with my predictions here, but like we're a few years away from basically
[1085.30 --> 1091.52]  having most of the retraining tasks being done automatically, meaning without a human in the loop,
[1091.76 --> 1097.20]  right? And that's generally where I think AI is going, right? If you kind of want to think about
[1097.20 --> 1101.94]  where I was going to be like kind of, you know, three years from now, look at where AI was, you know,
[1102.02 --> 1107.02]  five or seven years ago. If you think about kind of like where we were seven years ago,
[1107.02 --> 1111.86]  this is like, it predates scikit-learn, predates TensorFlow, predates PyTorch, right?
[1112.30 --> 1116.10]  Where if you wanted to like, you know, if you heard about AI and you thought, oh, maybe that
[1116.10 --> 1120.36]  could have an advantage for my business or my organization, you would basically need to hire
[1120.36 --> 1127.46]  a PhD from some top school to like code up and see an SVM. That's kind of what they would do.
[1127.74 --> 1131.80]  The thought of that today seems like kind of very, right? We're kind of like, we're laughing about
[1131.80 --> 1135.84]  that, but that's really how it used to be just like in what, in 2014, right? 2015.
[1135.84 --> 1140.88]  There's been a lot of automation since then. And I think that where we're going is we're going
[1140.88 --> 1145.30]  towards more and more and more of this automation, especially when, you know, if you meet a company
[1145.30 --> 1150.06]  now and that company has just a handful of models, you know, talk to that company again, a year from
[1150.06 --> 1153.86]  now, they'll probably have like hundreds of models, right? And if you met a company now that has
[1153.86 --> 1157.08]  hundreds of models, you know, a year from now, they'll probably have thousands of models.
[1157.70 --> 1163.08]  So in order to do that and scale, it's all automation. So that's, that's kind of like our perspective
[1163.08 --> 1170.24]  and philosophy in the company that the world of AI is going towards automation. And as the world of
[1170.24 --> 1176.24]  AI is going towards automation, we're trying to really think and understand how do we ensure an
[1176.24 --> 1183.12]  organization that is using AI, especially kind of in an automated way is really making sure that is
[1183.12 --> 1188.44]  not taking on any risk, that it really eliminates all the risks that AI has, especially with assuming
[1188.44 --> 1193.46]  that it does automated retraining of models and all that. I think automation definitely presents
[1193.46 --> 1198.22]  an additional, you know, dimension of risk. And it's really important to like understand
[1198.22 --> 1201.58]  that that risk that we're taking on, right, and be thoughtful about it.
[1201.84 --> 1205.90]  I get a follow up question to that. When is Daniel was asking that last one, it popped to mind,
[1205.94 --> 1209.86]  and you've started addressing it already. And I want to explore it a little bit. And that is,
[1210.24 --> 1217.02]  if you're thinking about this journey, from kind of where we are now, and having human in the loop on
[1217.02 --> 1222.64]  lots of critical tasks and lots of industries, especially for retraining and things. But if we
[1222.64 --> 1228.00]  agree that we're generally moving toward full automation, there's risks associated with both
[1228.00 --> 1233.84]  of those scenarios. And there's also risks associated with that kind of in between, where it's human
[1233.84 --> 1239.14]  automation collaboration, often said, like, in the industry, I'm in man-done-man teaming, that kind
[1239.14 --> 1244.52]  of concept. All of those two poles, plus the journey in the middle, all have a discrete set of risks
[1244.52 --> 1249.24]  associated with them. How do you see that? How do you look at those risk sets? And how do you
[1249.24 --> 1254.68]  decide what matters? You know, how do you evaluate that? Because I think that's a really tough question
[1254.68 --> 1259.38]  that I end up talking with folks that are grappling with is, is, well, there's problems with having
[1259.38 --> 1264.08]  humans. We're not perfect. We screw up. And we sometimes talk about it in the sense of having a
[1264.08 --> 1269.18]  human bring safety, but not always. And there are other times, you know, you can go argue the other
[1269.18 --> 1270.70]  way. What's your perspective on that?
[1270.70 --> 1275.44]  Yeah, there's an inevitable trade-off, right? That's what you're saying. I'm of the opinion
[1275.44 --> 1280.16]  that the goal of any technology is to basically, you know, support humans, right? Not replace them.
[1280.52 --> 1285.14]  On the one hand, we want to support human decision-making. Wherever it can help automate
[1285.14 --> 1290.28]  and kind of de-bias human decision-making, we want to support that and not replace that. But at the same
[1290.28 --> 1296.04]  time, we want to make sure that we're not replacing human judgment. I think that the challenge that we
[1296.04 --> 1302.54]  have in our world, I don't know that we will have that choice. Meaning that we don't have a person
[1302.54 --> 1309.00]  sitting in every kind of like critical decision junction and making that critical human judgment,
[1309.26 --> 1314.26]  it doesn't scale. And that's the biggest challenge that we have. So with that in mind, I think that
[1314.26 --> 1318.76]  like, what we need to do is we need to make sure that it's never going to be perfect, but we need to,
[1318.86 --> 1324.90]  we need to know that we're making every possible effort to make sure that it is as safe and risk-free
[1324.90 --> 1330.28]  as much as possible. That's a very thoughtful answer. Thank you. Yeah. This whole time I've sort of been
[1330.28 --> 1336.24]  thinking and through these sort of wider, you know, broader issues and thinking through my own use
[1336.24 --> 1342.50]  cases. And as Chris knows, eventually I always get to the point where I'm like, okay, well, I understand
[1342.50 --> 1349.54]  the point here. Like, what can we do practically to address these things and mitigate them? I'm wondering
[1349.54 --> 1357.36]  if you could like maybe walk us through like your journey to robust intelligence in terms of how you
[1357.36 --> 1365.44]  kind of came to, I guess, understand what you wanted to focus on in terms of, in terms of what you wanted
[1365.44 --> 1372.32]  to build and offer to the community, because there are so many problems and so much to address. And,
[1372.42 --> 1376.28]  you know, obviously you have to focus on, on something to start with. So how did,
[1376.28 --> 1380.18]  how did you get to that point and how did things kind of get started?
[1380.80 --> 1386.36]  So my journey into this has been through like a lot of AI practitioners, I think it started in
[1386.36 --> 1393.76]  academia. So I was a PhD student at Berkeley and then I worked at Google and then I spent seven or
[1393.76 --> 1398.40]  eight years at Harvard. I've been, I'm a professor of computer science and applied math at Harvard.
[1398.70 --> 1403.62]  And basically what I've been working on at Harvard is exactly this topic, the vulnerability,
[1403.62 --> 1407.96]  the sensitivity and the failure modes of machine learning models, right? So a little bit before my
[1407.96 --> 1411.96]  time at Google, and then while I was at Google, I've worked on machine learning models and basically
[1411.96 --> 1417.38]  algorithmic decision that is based on machine learning models. And when you do that and you
[1417.38 --> 1422.38]  start to kind of like do the theory behind it and you try to prove theorems, you start realizing
[1422.38 --> 1429.16]  that we have very little foundations for kind of like algorithmic decision-making given machine
[1429.16 --> 1433.76]  learning input. And there's a good reason for why we have like very little theoretical understanding
[1433.76 --> 1437.52]  is because it's pretty terrible to be honest. And that's kind of what I started studying. And
[1437.52 --> 1441.88]  specifically like kind of, I've been looking at, you know, really the, the sort of the, whether we
[1441.88 --> 1446.28]  can make good algorithmic decisions given input from machine learning models. And the answer is,
[1446.34 --> 1449.92]  you know, mathematically, no sort of like, and this has been my, my focus at Harvard.
[1449.92 --> 1455.74]  And so when you say terrible, you sort of mean terrible in the sense that you can't get to a
[1455.74 --> 1461.40]  point where you can prove in many cases that algorithmic decision-making is a good idea.
[1461.84 --> 1465.62]  Yes, exactly. You actually prove it mathematically. You know, we have like kind of mathematical
[1465.62 --> 1469.72]  definitions of what it means to learn and what it means to like kind of make good decisions. And you
[1469.72 --> 1475.00]  can, we have like kind of very, very rigorous kind of models and statements. And, and when you kind
[1475.00 --> 1479.24]  of use these rigorous, and these are the kind of like the rigorous, you know, models and statements
[1479.24 --> 1482.84]  that kind of make machine learning work, when you kind of try to apply a little bit more complex
[1482.84 --> 1486.38]  decision-making on top of these results of machine learning models, it all starts to work.
[1486.80 --> 1491.48]  So we've been kind of like proving these theorems about like how much data you would need in order
[1491.48 --> 1495.68]  to, to make what we call good decisions. And it turns out that, you know, the data is like
[1495.68 --> 1500.14]  exponential in the dimension of the input, which is really bad. And kind of like we studied the
[1500.14 --> 1504.50]  sensitivities of, you know, of models and to like kind of very, very small errors and very,
[1504.58 --> 1508.90]  very kind of like small failures. And again, like kind of like infinitely small errors in,
[1508.90 --> 1513.68]  you know, in models can lead to errors that are arbitrarily like kind of that. It's quite
[1513.68 --> 1517.90]  horrible and quite bad. And I've actually spent some time, you know, in my academic career trying
[1517.90 --> 1522.04]  to kind of like convince people of this, right. And giving talks about an inconvenient truth about
[1522.04 --> 1525.40]  algorithms in the air of machine learning. If you look at that title up, you'll see like a bunch
[1525.40 --> 1528.86]  of lectures coming up and, you know, and seminars across.
[1529.04 --> 1532.38]  I'm sure it produces some awkward conversations at conferences.
[1533.02 --> 1536.92]  Absolutely. Absolutely. It does. Right. Especially in a time where kind of like machine learning is on
[1536.92 --> 1540.24]  the rise and on the boom. And, you know, and your department is like, you know,
[1540.56 --> 1544.00]  this gun hole about like hiring more people in machine learning. And now they have like this
[1544.00 --> 1549.36]  professor who's like, you know, kind of proves all these weird theorems about why it's not working.
[1549.76 --> 1554.36]  I'm sitting in the same department as Les Valiant, who created the foundations of machine learning,
[1554.48 --> 1557.66]  right. Who's been, by the way, like the most receptive person to like, you know,
[1557.66 --> 1562.80]  this sort of criticism and whatnot. And he's been so supportive. So it's definitely like a lot of
[1562.80 --> 1566.76]  some papers took like, you know, three, four years to get published, but they got published.
[1567.06 --> 1571.40]  And then they got kind of like very good recognition. But we started from, you know,
[1571.48 --> 1575.10]  the theories about the impossibilities. And then we moved to algorithms. And, you know,
[1575.24 --> 1579.88]  my group developed a lot of basically focused on algorithms for, you know, noise robust algorithms
[1579.88 --> 1583.04]  for these types of problems and kind of like focusing on what is that we can do.
[1583.44 --> 1587.20]  As we kind of proved all these impossibility theorems and, you know, kind of like focus on what
[1587.20 --> 1591.44]  is it the algorithms would be able to do? Like a very big idea that came up was like decoupling.
[1591.44 --> 1598.02]  So what we realized that one needs to do is basically decouple the part about model building
[1598.02 --> 1605.26]  from model security or model safety. Meaning that if you try to like build, just train a model
[1605.26 --> 1610.06]  that is going to be robust to, you know, let's say adversarial input, we talked about that.
[1610.36 --> 1614.52]  I think kind of the best result known, and I think that result is now from like two or three years ago.
[1614.90 --> 1620.10]  It turns out that if you want to like make your model just by retraining it to make it more robust
[1620.10 --> 1624.86]  to like adversarial input, I think an image classification, you're going to take the
[1624.86 --> 1632.56]  accuracy of the model from 98% to 37%, right? In order to get any sort of reasonable robustness,
[1632.92 --> 1636.98]  which is a trade-off that is just unacceptable, right? If you're going to come up to like a company
[1636.98 --> 1642.14]  and tell them, Hey, you know how your model like has 98% accuracy. Well, in order to make it robust
[1642.14 --> 1649.70]  to like the 0.001% of input that is bad, I'm going to take that model to accuracy to like 37%.
[1649.70 --> 1654.08]  Would there be an analogy there to kind of in the software world, having a separation of concerns?
[1654.30 --> 1654.66]  Absolutely.
[1655.18 --> 1657.44]  Yeah. Okay. For any listeners that are not software people,
[1657.62 --> 1661.42]  you want to address the problem you're trying to address, but at the same time,
[1661.48 --> 1664.68]  the ancillary things like security that are very important need to be addressed,
[1664.76 --> 1667.18]  but you address them separately to maximize both.
[1667.64 --> 1671.04]  Absolutely. Whenever I talk to people for the first time about this, I tell them, you know,
[1671.04 --> 1675.14]  look, there are two considerations. One is the mathematical consideration and mathematically,
[1675.54 --> 1681.06]  if you wanted to make your model robust, quote unquote, by retraining it to like adversely input,
[1681.54 --> 1686.12]  it means that you're going to like take accuracy from something like 98% to 37%. It's kind of like,
[1686.18 --> 1690.96]  it's just a mathematical fact. Now there's another aspect of it, which is the product aspect of it,
[1690.98 --> 1695.46]  right? Right. Or the kind of like the engineering aspect of it. And the engineering aspect of it is,
[1695.46 --> 1699.56]  it's exactly what you're talking about, Chris, right? Where if you're an engineer that's building a
[1699.56 --> 1704.42]  system, you probably, we should not be the one who's also responsible for like protecting that
[1704.42 --> 1709.02]  system. You know, we can just all imagine the nightmare. If every time that we wrote software,
[1709.14 --> 1714.50]  we'd also have to write the antivirus and the firewall, right? For that software. So in software,
[1714.58 --> 1719.76]  like kind of, we've seen such tremendous success exactly because of this decoupling, right? And kind
[1719.76 --> 1723.16]  of like layering of different systems, right? And components that know how to work together,
[1723.16 --> 1728.28]  right? And almost like this agnostic way. And I think that what we're trying to do in the company
[1728.28 --> 1733.40]  and robust intelligence is mimic that kind of decoupling. So specifically what we do is we
[1733.40 --> 1740.70]  build an AI firewall. And an AI firewall is a piece of software that wraps around an AI model
[1740.70 --> 1747.96]  to protect it from making mistakes. So it kind of like, it's a one line of code that you add so that
[1747.96 --> 1753.88]  that one line of code can basically stands between the data and the model. And it can, once the data
[1753.88 --> 1760.66]  comes in, it monitors, tests, and can even correct it. So basically the data point does not fool the
[1760.66 --> 1766.50]  model, does not cause the model to make the sort of mistake, right? Or a bad prediction. And that's
[1766.50 --> 1771.58]  the sort of like this decoupling process where we're not trying to build a better model. All we're
[1771.58 --> 1777.64]  trying to do is we're trying to be basically be able to catch bad data. So it's reducing it to like
[1777.64 --> 1778.88]  a much, much simpler task.
[1778.88 --> 1785.54]  I definitely resonated with your example around the sort of firewall and antivirus. I know in my own
[1785.54 --> 1792.96]  sort of building software career, anytime I felt like I, you know, I start poking holes in a firewall
[1792.96 --> 1799.18]  to open up ports and like configure things, I start feeling like extremely uncomfortable because I have
[1799.18 --> 1805.96]  no idea what I'm doing. So that definitely resonates with me. We talked about that firewall component,
[1805.96 --> 1811.64]  this AI firewall component kind of wrapping around the model, sort of between the data and the model.
[1812.02 --> 1819.52]  In that firewall, are you looking at sort of like out of distribution data that's coming in or maybe
[1819.52 --> 1826.74]  particular, are there other ways that like some data is more particularly risky than others? So I guess
[1826.74 --> 1833.04]  my question is like, how do you know as data comes in, if it's risky data or if it's not risky data?
[1833.04 --> 1839.80]  Yes, that's a good question. So what we do is basically we test the models, we have a process of stress
[1839.80 --> 1845.00]  testing the models. And we do that either implicitly, if you just install the AI firewall, if you just put the
[1845.00 --> 1850.80]  line of code, we basically do that in the background, we do that implicitly. Or sometimes, you know, when
[1850.80 --> 1856.26]  there are companies where we start from stress testing, and then we kind of graduate to AI firewall. And stress
[1856.26 --> 1861.80]  testing, basically, what that means for us is, we run a series of tests on the model, you know, some of the
[1861.80 --> 1865.60]  tests can be, how does the model respond to distributional drift? How does the model respond
[1865.60 --> 1870.84]  to unseen categoricals? How does the model, you know, just all these sort of different scenarios,
[1871.02 --> 1876.54]  right, and different inputs. And then we were measuring the response of the models, right, to
[1876.54 --> 1880.94]  kind of like all these bad things that could happen. And as we're measuring them, right, we're getting a
[1880.94 --> 1886.60]  sense, basically, of we're basically training our own AI firewall. So my understanding kind of like,
[1886.60 --> 1891.78]  how different input can affect the model in different ways, when new input comes in, we know
[1891.78 --> 1897.28]  whether that input is going to lead to, like, some sort of prediction error, some sort of prediction
[1897.28 --> 1902.34]  change. So let me give you like, you know, like a silly example, right? Suppose that your model, you
[1902.34 --> 1907.82]  have like, some sort of AI model, and maybe that AI model is trying to predict whether, you know, somebody's
[1907.82 --> 1914.24]  going to earn above $100,000 next year. So whenever we take that input, like we check all the different
[1914.24 --> 1918.52]  features. And when we sort of see like, how the changes in different features can affect the
[1918.52 --> 1923.10]  prediction of the model, right? So maybe like, you know, for example, we look at like, how does age,
[1923.46 --> 1928.66]  right, affect the prediction of the model? And now suppose that like kind of, you know, data comes in,
[1929.04 --> 1935.10]  and somebody has accidentally replaced age with year of birth, right? So age is like, you know,
[1935.10 --> 1942.04]  maybe from like, I don't know, 36, age was changed into like 1985, or 1986, or whatever, you know.
[1942.04 --> 1947.48]  So that's basically some sort of like human error, or like kind of error in, you know, kind of like
[1947.48 --> 1953.14]  in feeding in the data. And by that point, the AI firewall is trained that it knows that, you know,
[1953.18 --> 1957.54]  this feature, change in this feature can really affect the model prediction. And certainly kind
[1957.54 --> 1961.90]  of like, it understands what the right distribution of age is, it understands that age needs to be
[1961.90 --> 1967.10]  something between, you know, probably, it's seen data from like 10 to like 90, or something like
[1967.10 --> 1972.20]  that, right. So it understands whenever it sees like a big number, like 1985, right, there's something
[1972.20 --> 1977.24]  wrong here. And then what it can do is basically, it can alert, and it can prevent that mistake from
[1977.24 --> 1982.60]  happening by kind of even replacing, you know, 1985 by the mode of the distribution or something like
[1982.60 --> 1986.44]  that, right, to kind of put out output like a better, better prediction.
[1987.00 --> 1991.74]  I'm curious, it's an interesting approach that you have here, if you are already kind of building your
[1991.74 --> 1995.88]  models, and you're deploying them out into production, you know, whatever industry you're in,
[1995.88 --> 2003.32]  and you have your MLOps pipeline in place. And on the software side, kind of your DevOps or DevSecOps
[2003.32 --> 2009.28]  is it's kind of evolving into a place, how do you integrate this together? How do you take what
[2009.28 --> 2015.78]  you're talking about, and put into your integrate into your existing pipeline, so that you gain the
[2015.78 --> 2021.34]  benefit of what you're what you're describing, and yet not kind of breaking your approach, so to speak,
[2021.34 --> 2024.44]  in terms of how you're already doing that? How does all that work together?
[2024.44 --> 2031.06]  Great. So our approach is that the best integration is no integration. And that's why we have one way
[2031.06 --> 2035.58]  to integrate the product is like, kind of we call this like a light integration, is where basically,
[2035.58 --> 2041.82]  we're not integrating with the model at all, all we do is we just take prediction logs, right? So if you
[2041.82 --> 2046.74]  have like a model that's running, and you store prediction logs somewhere, kind of like meaning that
[2046.74 --> 2052.24]  you have like input, and the output of the model, and that's stored in some sort of CSV file, then
[2052.24 --> 2058.74]  basically, our product just basically just just sits there and runs a CI CD process, and just
[2058.74 --> 2064.50]  continuously reads, you know, that CSV file, whenever you dump in, you know, a new kind of like log file,
[2064.68 --> 2068.68]  and it just reads it, and that's it. And it just continuously tested. And we call this continuous
[2068.68 --> 2074.60]  testing. So we continuously test, you know, the model, right, without ever being in the critical path,
[2074.60 --> 2080.96]  with basically zero integration. So it literally is like, in production, it's like a two hour
[2080.96 --> 2085.18]  integration with Kubernetes. Because again, it doesn't stand in the critical path of anything
[2085.18 --> 2089.96]  like that. When we're doing something like AI firewall, this is where we're integrating on the
[2089.96 --> 2094.38]  again, it's like a single line of code that we're integrating on the on the actual model server.
[2094.76 --> 2099.72]  And that involves some, you know, some libraries and things like that. But again, it uses that same
[2099.72 --> 2104.24]  principle where ultimately, it throws data in the form of like prediction logs in the background.
[2104.24 --> 2109.04]  So that it doesn't stand in the critical path of, you know, anything really in the system.
[2109.58 --> 2113.68]  So that's something that's that's really important. And a lot of it we do, we do for customers on
[2113.68 --> 2119.94]  premise. Because having your data leave the organization is a huge pain. It's sensitive,
[2120.32 --> 2125.00]  you know, there's like a lot of kind of compliance involved and things like that. So on premise is
[2125.00 --> 2126.52]  actually something that is very important.
[2127.08 --> 2132.84]  I want to follow up a little bit on what you're talking about, sort of this continuous testing,
[2132.84 --> 2138.50]  I think, I think is what you called it, which is, is a really cool idea that I like. And probably,
[2138.50 --> 2143.42]  I don't know if that's less scary to AI people than a word like monitoring or something, you know,
[2143.42 --> 2148.42]  something. But I like that idea of continuous testing. I'm wondering, you kind of give the
[2148.42 --> 2154.42]  simple example of like, maybe this distribution of age in the model or something like that. And I'm
[2154.42 --> 2161.30]  thinking, there are likely these, maybe these categories, sensitive categories, like, you know,
[2161.42 --> 2167.86]  personal details of age, or, you know, race, or whatever it is that you're giving examples of
[2167.86 --> 2175.74]  like the police scenarios, and that sort of thing, where these might be categories in which variation
[2175.74 --> 2183.52]  in that category should necessarily produce invariance in the in the output, at least if if you're
[2183.52 --> 2190.36]  monitoring those well. What's your perspective on that in terms of how to approach those sensitive
[2190.36 --> 2197.02]  categories? And is that something you can kind of program to both in terms of variation and maybe
[2197.02 --> 2199.32]  things that should be invariant with change?
[2199.32 --> 2206.30]  So basically, like in our paradigm, one of the kind of the basic building blocks is the building
[2206.30 --> 2211.56]  block of tests, basically, what you know, you discover whatever it is that you test for,
[2211.88 --> 2217.12]  right? If you're not going to test for bias, you're not going to discover bias. But if this is something
[2217.12 --> 2221.24]  that you care about, and I think that a lot of practitioners and organizations should very much
[2221.24 --> 2226.58]  care about bias, right, then you test for it. And whenever whenever it exists, you find it.
[2226.58 --> 2231.06]  And that's actually a suite of tests that we have embedded in the product that is actually
[2231.06 --> 2236.58]  very important, right? So what we do is we automatically test the model, we just automatically
[2236.58 --> 2240.88]  go through like all the different categories. And we test like whether there's whether there's
[2240.88 --> 2244.60]  bias in prediction, whether there's bias in UC, whether there's bias in false positives,
[2244.74 --> 2249.32]  false negatives, like all these different things across different categories, right? And that's when
[2249.32 --> 2252.72]  people discover like all these biases that they had in the model that they never knew about.
[2252.72 --> 2257.12]  Some of it is protected categories. And some of it is just, you know, just other categories that
[2257.12 --> 2260.96]  they, you know, that they didn't know that they found out that their model is just like,
[2261.30 --> 2265.10]  they're not training their models on the right data set, or they should do kind of different
[2265.10 --> 2268.86]  sampling of the data, right, in order to make sure that the model is not even like kind of
[2268.86 --> 2273.36]  performance biased, right? So I think that's cool. Testing for bias is such a critical thing
[2273.36 --> 2276.32]  that basically all AI practitioners should do.
[2276.32 --> 2282.08]  This has been a fascinating exploration and definitely a topic that we have not gotten
[2282.08 --> 2288.32]  really into at any point in any previous episode. As we wind up, where do you see the future going,
[2288.54 --> 2295.08]  both with robust intelligence as your enterprise, as your company that is doing things, but also
[2295.08 --> 2301.56]  within the larger world of robust intelligence, the larger effort in the industry to drive forward
[2301.56 --> 2305.96]  and the evolution, what we won't hold you to any predictions. But if you were to make some
[2305.96 --> 2310.52]  predictions on where, where you think it will go, or where you would like to see it go, I'd love to
[2310.52 --> 2310.88]  hear that.
[2311.36 --> 2316.10]  Sure. So I think like, let's start by the things that are not interesting, right? What we all know is we
[2316.10 --> 2320.00]  all know that the world is kind of like AI is eating the world, right? Like it's, we're going to be
[2320.00 --> 2325.06]  hard pressed to find an organization that is not adopting AI in a serious way in just a couple of years,
[2325.06 --> 2330.32]  I think, right? So okay, that's not interesting. So let's put that aside. But I think when it comes to
[2330.32 --> 2336.12]  our little part of the world, when it comes to like AI risk, we think that within just a few years,
[2336.34 --> 2342.74]  there are two things. I think that any organization that uses AI in a way that can affect people is
[2342.74 --> 2346.72]  going to have to like go through some sort of stress testing by third party. I think that's
[2346.72 --> 2350.24]  going to be mandatory. I don't think that it's going to be up to like the director of data science
[2350.24 --> 2354.72]  in that company. That's just going to be regulation. That's number one. And number two,
[2355.12 --> 2360.10]  also on regulation and best practice, I think just a few years from now, in the same way,
[2360.10 --> 2365.28]  I think we're going to be hard pressed to find a company that is not protecting its models with
[2365.28 --> 2369.86]  an AI firewall, not necessarily robust intelligence, right? I don't know if any other companies are
[2369.86 --> 2374.78]  making AI firewalls. But I think that like within a few years, we're going to have this conversation
[2374.78 --> 2378.88]  again, three years from now, we'll go back and remind ourselves like, hey, do you remember that,
[2378.96 --> 2383.36]  you know, three years ago, you know, companies were actually deploying AI models without an AI firewall.
[2383.70 --> 2388.62]  How crazy was that? Right? I think that's what we're going to find three years from now.
[2388.62 --> 2391.36]  That's where we're going kind of like, in my part of the world.
[2391.72 --> 2395.12]  And you should consider that an invitation, by the way, for three years out to come back,
[2395.18 --> 2396.26]  and we'll have that conversation.
[2396.50 --> 2400.82]  The data is going to be easy to remember, because I think that we're like the last podcast of the
[2400.82 --> 2407.20]  year, right? So as we go into 2025, it'll be good to sort of like, check, you know, where we were
[2407.20 --> 2407.84]  with our predictions.
[2408.14 --> 2408.48]  Absolutely.
[2408.94 --> 2414.74]  Yeah, for sure. And hopefully sooner than that as well. It's been an absolute pleasure to talk
[2414.74 --> 2420.30]  through these things with you. And as for myself, and I'm guessing Chris as well, we appreciate
[2420.30 --> 2427.52]  your work in this space and pushing these ideas forward and being that voice that has occasional
[2427.52 --> 2433.12]  awkward conversations at AI conferences. It's much needed and appreciate your perspective. So
[2433.12 --> 2434.06]  thanks for joining us.
[2434.30 --> 2435.24]  Awesome, guys. Thank you.
[2435.24 --> 2443.70]  All right, that's Practical AI for this week. Thanks for listening. If this is your first time
[2443.70 --> 2449.92]  with us, subscribe now at practicalai.fm. Or simply search for Practical AI in your favorite
[2449.92 --> 2454.78]  podcast app. We're in there. And if you're a longtime listener, do us a solid by recommending
[2454.78 --> 2460.18]  the show to a friend. Word of mouth is still the number one way people find new podcasts they love.
[2460.18 --> 2465.40]  Special thanks to our partners for supporting our work, Fastly, LaunchDarkly, and Linode. We
[2465.40 --> 2469.86]  appreciate it. And to the mysterious Breakmaster Cylinder for cranking out new beats for us all
[2469.86 --> 2472.96]  the time. That's all for now. We'll talk to you again next week.
[2490.18 --> 2494.04] ーン
[2494.04 --> 2501.36]  it
[2501.36 --> 2503.28]  you
[2503.28 --> 2505.44]  you
