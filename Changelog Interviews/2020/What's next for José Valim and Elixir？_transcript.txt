[0.00 --> 2.76]  I haven't seen it, but there's a recent documentary on Netflix.
[3.34 --> 6.98]  And I think like one of the discussions points that there was somebody who played with Jordan
[6.98 --> 9.62]  that was very important for the whole team to function.
[9.96 --> 10.56]  Oh, yeah.
[11.04 --> 11.72]  Do you know?
[11.98 --> 13.30]  I don't know anything about that.
[13.30 --> 13.82]  Scotty Pippen.
[14.10 --> 14.64]  Scotty Pippen.
[14.72 --> 15.28]  Yeah, of course.
[15.66 --> 16.02]  Okay.
[16.24 --> 16.42]  Yeah.
[16.48 --> 17.36]  I don't know enough, right?
[17.38 --> 17.76]  They're a pair.
[17.94 --> 18.14]  Yeah.
[18.28 --> 18.80]  So, you know.
[18.84 --> 19.18]  He's short.
[19.26 --> 19.64]  He's tall.
[20.04 --> 20.98]  Yeah, they're both pretty tall.
[21.18 --> 22.52]  Well, I mean, he's shorter than Jordan.
[23.82 --> 25.50]  I think he's actually taller.
[26.74 --> 28.82]  Regardless, they were definitely a one-two punch.
[28.82 --> 32.26]  And Scottie, you know, Jordan was the superstar, but Scotty Pippen was the glue.
[34.96 --> 37.64]  Bandwidth for Changelog is provided by Fastly.
[38.02 --> 39.90]  Learn more at Fastly.com.
[40.14 --> 43.22]  We move fast and fix things here at Changelog because of Rollbar.
[43.36 --> 45.04]  Check them out at Rollbar.com.
[45.28 --> 47.46]  And we're hosted on Linode cloud servers.
[47.80 --> 49.80]  Head to linode.com slash Changelog.
[52.48 --> 55.14]  This episode is brought to you by DigitalOcean.
[55.66 --> 56.06]  Droplets.
[56.38 --> 57.18]  Managed Kubernetes.
[57.18 --> 58.38]  Managed databases.
[58.82 --> 59.50]  Spaces.
[59.74 --> 60.70]  Object storage.
[60.92 --> 62.18]  Volume block storage.
[62.42 --> 65.90]  Advanced networking like virtual private clouds and cloud firewalls.
[66.10 --> 72.36]  Developer tooling like the robust API and CLI to make sure you can interact with your infrastructure the way you want to.
[72.78 --> 76.26]  DigitalOcean is designed for developers and built for businesses.
[76.96 --> 83.32]  Join over 150,000 businesses that develop, manage, and scale their applications with DigitalOcean.
[83.68 --> 87.10]  Head to do.co slash changelog to get started with a $100 credit.
[87.10 --> 89.60]  Again, do.co slash changelog.
[89.60 --> 98.62]  All right.
[98.68 --> 99.30]  Welcome back, everyone.
[99.50 --> 105.78]  This is the Change Local podcast featuring the hackers, the leaders, and the innovators in the world of software.
[105.78 --> 109.08]  I'm Adam Stachowiak, editor-in-chief here at Change Log.
[109.38 --> 112.30]  On today's show, we're joined again by Jose Valim.
[112.36 --> 127.70]  It's been a bit since we talked to him, but we're talking about the recent acquihire slash acquisition of Plata Formatech by Newbank, a fintech company in Brazil, and what that means for the Elixir language and what that means for Jose.
[127.70 --> 136.88]  We also talk about Dashbit, a new three-person organization he started as part of some of the work that came from Plata Formatech around the Elixir language.
[137.58 --> 148.72]  And lastly, we talk about a kind of crazy, kind of big, kind of awesome idea Jose has called BytePack that helps you to package and deliver software products to developers and enterprises.
[148.72 --> 155.80]  It's pretty interesting, but as with anything, there's also some complexity that comes with that, so we talk through all the details.
[161.86 --> 164.02]  So we're joined by Jose Valim.
[164.20 --> 165.72]  Jose, we thought it was just a couple of years ago.
[165.82 --> 168.44]  Turns out, four years since you've been on the Change Log.
[168.50 --> 169.34]  Welcome back, my friend.
[170.06 --> 170.40]  Thank you.
[170.44 --> 171.24]  I'm glad to be back.
[171.98 --> 173.48]  We're glad to have you.
[173.48 --> 177.26]  We want to catch up with you and with Dashbit and with Elixir.
[177.26 --> 180.34]  Big news coming out back in January.
[180.60 --> 191.16]  Plata Formatech, the company that you co-founded and the Elixir company for all those years, was acquihired by Nubank, a fintech company in Brazil.
[191.30 --> 191.96]  Tell us that story.
[192.66 --> 193.16]  Oh, sure.
[193.52 --> 197.78]  It feels like such a long time ago because this year has been so crazy so far.
[198.78 --> 202.22]  So Nubank, they acquihired Plata Formatech.
[202.22 --> 210.36]  They were, when the whole thing happened, they were, you know, in, since it's a acquihire, they were interested in our talent.
[210.88 --> 223.62]  And it's interesting because I think for the, let's say, to everybody outside Brazil, Plata Formatech was really known because of its open source work.
[223.62 --> 228.88]  Started back in Rails with Devise and Simple Form and then later with Elixir.
[229.48 --> 231.02]  And that was one of the reasons.
[231.14 --> 233.12]  We always had a very good technical team.
[233.70 --> 235.90]  And that was one of the reasons for the acquihire.
[235.90 --> 243.24]  But in Brazil, Plata Formatech was really known because of the way we manage projects and our processes.
[243.58 --> 249.90]  I'm doing air quotes when I say processes, but, you know, the whole way we would do project management and work with clients.
[250.64 --> 256.66]  And that was also one, another very important aspect behind the acquihire.
[256.94 --> 258.64]  It's actually a part that I'm not super involved.
[258.64 --> 261.52]  So I don't know how to explain everything we did.
[261.92 --> 262.04]  Sure.
[262.32 --> 268.44]  In Brazil, you know, when we would work with clients, it was like one of the big reasons why they want to work with us besides the technology aspect.
[269.52 --> 273.88]  So, yeah, that was basically why it happened.
[274.60 --> 284.90]  But I think what is more interesting for us to talk about from the change log perspective, I guess, is about how does that affect all the open source that we have been doing?
[285.04 --> 285.68]  Does that make sense?
[286.04 --> 286.36]  Absolutely.
[286.36 --> 287.04]  Yeah.
[287.04 --> 293.42]  So as soon as the acquihire was announced, we knew that there would be a lot of questions.
[293.56 --> 302.98]  What it meant for, you know, device, simple form, which were still under Plata Formatech's responsibility and also to Elixir.
[303.44 --> 304.94]  And there are many aspects to it, right?
[304.94 --> 316.96]  So the thing that we did immediately was that we told everybody that because those efforts, they were mostly community efforts, we would be giving all the assets back to the community.
[317.56 --> 317.70]  Right.
[317.70 --> 323.20]  So we reached out to the device maintainers and we say, you know, all the assets, they are now yours.
[323.52 --> 323.86]  Right.
[323.96 --> 325.64]  You are now responsible for the project.
[325.88 --> 331.00]  We want to be here like overseeing or holding control like of the logo and this kind of things.
[331.00 --> 333.12]  So we did that for our projects.
[333.12 --> 335.56]  And so we transferred to the maintainers.
[335.88 --> 341.74]  And for Elixir itself, we transferred everything to the Elixir team.
[341.74 --> 346.16]  And that's me and other four or five.
[346.30 --> 347.64]  My math is not good right now.
[347.78 --> 350.26]  But yeah, so to the Elixir core team.
[350.90 --> 352.80]  And that was one of the things that we need to do.
[352.84 --> 353.00]  Right.
[353.06 --> 355.46]  You know, like who controls the code base.
[355.54 --> 355.74]  Right.
[355.80 --> 356.62]  The assets and everything.
[356.62 --> 369.82]  But also something that people, they worried a lot at the beginning is like what that meant also meant in terms of, you know, who is going to be continue developing Elixir and the other open source projects.
[370.18 --> 375.56]  And I said since the beginning, like, you know, I'll be involved in the project in the same capacity.
[376.36 --> 379.66]  And, you know, at the beginning, people were still like, I'm not sure.
[379.76 --> 379.98]  Right.
[380.02 --> 381.98]  Like, is that going to be true?
[381.98 --> 385.28]  But now we are five, six months after everything happened.
[385.72 --> 386.30]  It's true.
[386.30 --> 387.48]  So we continue involved.
[387.78 --> 390.12]  I continue involved in the same way as before.
[390.36 --> 392.44]  Parts to Dashbit, which is my new company.
[392.64 --> 394.58]  And we can talk about it soon.
[394.96 --> 397.24]  But yeah, so the whole process, I think it's normal.
[397.56 --> 402.90]  When there was the record hire in terms of open source, a lot of people were worried what that meant.
[403.02 --> 406.64]  And if it meant like less people working on Elixir or not.
[406.64 --> 411.96]  But I think besides this initial concern, everything went really smooth.
[412.18 --> 416.08]  And I think in practical terms, nothing changed, you know.
[416.30 --> 416.82]  Yeah.
[417.32 --> 423.32]  So to be super clear, Nubank, Aqua hired the consulting company you ran, not Elixir.
[423.32 --> 425.40]  Yes, yes.
[425.60 --> 429.60]  And Nubank, what is really interesting is that they understand, right?
[429.60 --> 431.92]  They understand how important it's open source, right?
[431.92 --> 432.64]  And they understand.
[433.02 --> 441.18]  And they really supported us in this decision because they understand that, you know, we need to continue leading Elixir with our vision.
[441.18 --> 446.42]  And it doesn't make sense for them, you know, to impose a vision of how the language should be.
[446.80 --> 452.86]  So when we're having discussions, they're like, well, we want to give open source back to the people who actually maintain it.
[452.98 --> 455.74]  Everybody that was on the table, everybody agreed immediately.
[456.20 --> 456.32]  Sure.
[456.32 --> 461.64]  How much did Plataforma take bankroll Elixir development?
[462.24 --> 473.48]  You know, so when in the acquisition mentioned by Nubank, they say that we're confident that the language, its contributors and projects will keep growing and developing independently from Nubank.
[473.48 --> 483.96]  But, you know, it kind of depends on how much Elixir was really depending upon, you know, funding or bankrolling, in air quotes, without air quoting, the language.
[484.12 --> 485.12]  That's a very good question.
[485.78 --> 491.26]  So they basically, Plataforma Tech, they funded me working on Elixir.
[491.84 --> 495.10]  Initially, it was part-time when I started back in 2012.
[495.74 --> 500.92]  But I would say like from 2014 or so, I have been like full-time.
[500.92 --> 509.66]  So the cost, right, if you don't factor in the opportunity cost, but the cost would be a developer full-time for like eight years or so.
[510.16 --> 513.82]  At the end, we can talk about this when we talk about Dashbit.
[514.08 --> 519.02]  We had more developers working on Elixir, but most of it was me full-time.
[519.54 --> 527.02]  And that's the thing, like one of the things that I have always been careful and all of my co-founders, we agreed with these decisions since the beginning,
[527.02 --> 534.24]  is that, you know, it cannot be seen like as a company effort.
[534.58 --> 537.88]  We always need to have the community involved since the beginning.
[538.36 --> 542.58]  So it's like Plataforma Tech was sure we were like the creator, the catalyst.
[542.58 --> 551.06]  But as soon as it didn't depend on us, on Plataforma Tech as a company for the language to evolve, that would be the best, right?
[551.12 --> 554.44]  Because what I like to say is like, it's not the best way to think about it.
[554.44 --> 558.66]  But just for as an example, if you think about programming languages today, right?
[558.74 --> 561.40]  Like and programming languages competing for market share.
[561.48 --> 562.60]  I'm doing air quotes again.
[562.60 --> 569.12]  We are talking about like Swift from Apple, Rust from Mozilla, Go from Google, right?
[569.22 --> 570.18]  F-sharp from Microsoft.
[570.66 --> 578.14]  So, you know, how can a company that had like 70, 80 employees compete at this level, right?
[578.30 --> 581.98]  So we knew that it needs to be a community effort.
[582.74 --> 589.02]  So I think the first person who was Eric, he joined the core team in 2014.
[589.02 --> 592.00]  And since then, the core team has been growing.
[592.30 --> 597.76]  And I was like, so when it comes to Elixir, I was the only person that was really bankrolled at Plataforma Tech, right?
[597.78 --> 599.98]  It was not like half of the core team.
[599.98 --> 603.34]  It was one-sixth, one-fifth of the core team was bankrolled.
[603.70 --> 604.64]  And I think that's great, right?
[604.68 --> 607.74]  Because there's always the buzz number factor as well.
[607.82 --> 608.92]  I don't want things depending on me.
[609.04 --> 612.20]  So like if I die, does it mean the project's over, for example?
[612.94 --> 618.64]  So Elixir was not really dependent on Plataforma Tech and not on me as a person.
[618.64 --> 621.86]  And sure, some of the people in the core team, they work on their full-time.
[622.24 --> 629.04]  Other developers like Eric, he's sponsored by Brex, you know, the credit card company to work on Elixir full-time.
[629.70 --> 633.72]  So, you know, it has become like, is it correct to say stakeholders?
[633.86 --> 641.92]  There are like many stakeholders now, people involved in investing in the language in the ecosystem and not a single entity anymore.
[641.92 --> 649.88]  Or it's kind of how it was planned to be early on, because I don't think we would be able to grow otherwise or to get to the place where we are right now.
[649.88 --> 659.74]  So if we were to put me into a time machine and give me a billion dollars, send me back to the mid-90s, I might buy the Chicago Bulls.
[660.56 --> 663.22]  But I wouldn't buy the Chicago Bulls and not get Michael Jordan.
[664.64 --> 666.04]  So let's talk about Nubank.
[666.14 --> 669.00]  They aqua hire Plataforma Tech, but they don't get Jose Valim.
[669.70 --> 670.98]  That's a blunder, isn't it?
[670.98 --> 677.34]  Oh, so I think there are like two aspects to this, like in the part of the aqua hire.
[677.56 --> 680.80]  So remember, like one of the reasons, like there were two factors, right?
[680.82 --> 690.36]  So one was our technical team and the other one was everything that we do in terms of methodologies, in terms of projects, which I don't contribute at all.
[691.62 --> 696.52]  And that was, I believe it's very important for them because they are really growing like very fast.
[696.52 --> 700.00]  They start in Brazil, they're expanding to Latin America and everything.
[701.00 --> 706.62]  So, you know, like I think there is a recent, like I haven't seen it, but there is a recent documentary on Netflix.
[707.36 --> 713.58]  And I think like one of the discussions points that there was somebody who played with Jordan that was very important for the whole team to function.
[714.28 --> 714.52]  Oh, yeah.
[715.00 --> 715.68]  Do you know?
[715.96 --> 717.38]  I don't know anything about that.
[717.38 --> 717.78]  Scotty Pippen.
[718.06 --> 718.60]  Scotty Pippen.
[718.68 --> 719.24]  Yeah, of course.
[719.48 --> 719.62]  I mean.
[719.74 --> 720.04]  Okay.
[720.18 --> 720.38]  Yeah.
[720.40 --> 721.30]  I don't know enough, right?
[721.32 --> 721.70]  They're a pair.
[721.90 --> 722.10]  Yeah.
[722.22 --> 722.76]  So, you know.
[722.76 --> 723.64]  He's short, he's tall.
[724.00 --> 724.94]  Yeah, they're both pretty tall.
[724.94 --> 726.50]  Well, I mean, he's shorter than Jordan.
[727.76 --> 729.46]  I think he's actually taller.
[730.66 --> 736.20]  Regardless, they were definitely a one-two punch and Scotty, you know, Jordan was the superstar, but Scotty Pippen was the glue.
[736.56 --> 736.72]  Yeah.
[736.80 --> 744.78]  So you can say like there were, you know, maybe Jordan did not go according to your metaphor, but there were like three Scotty going there and helping them.
[744.78 --> 744.86]  Yeah.
[745.08 --> 750.88]  And the other point is that they are mostly using Clojure, I believe.
[751.34 --> 751.62]  Oh, really?
[751.62 --> 752.86]  And they are public about it.
[753.06 --> 759.90]  They are one of the most, they are one of the biggest cases of, you know, companies, large companies using Clojure at a really large scale.
[760.14 --> 768.16]  So it's actually interesting to hear about everything they are doing with Clojure and the interesting cases and how they are using the Clojure stack.
[768.22 --> 769.02]  And they write about it.
[769.08 --> 769.66]  They give talks.
[769.72 --> 771.30]  So it's very interesting to check that out.
[771.30 --> 777.84]  So in that sense, you know, if they brought me, maybe they would be bringing Michael Jordan to play soccer.
[778.14 --> 778.36]  Right.
[778.56 --> 780.30]  And that's not going to be a good fit.
[780.38 --> 780.58]  Right.
[781.42 --> 782.28]  Well said.
[782.28 --> 788.34]  So, you know, but in any way, it could be Michael Jordan to play soccer.
[788.34 --> 797.34]  But one of the things to talk about as well is because I like to say Elixir has like three major influences, which are Erlang, Ruby and Clojure.
[797.66 --> 797.86]  Right.
[797.98 --> 804.40]  So, you know, a lot of the ways of thinking about problems are shared between Elixir and Clojure.
[804.56 --> 809.30]  And that's definitely something that hopefully was important as part of the acquisition as well.
[809.90 --> 811.86]  But yeah, for me, it was very important.
[811.86 --> 817.36]  Like personally speaking, to continue involved with Elixir, it's what I wanted to be doing.
[817.76 --> 825.40]  And as I said, like, you know, when we said about the importance of Elixir and of the open source projects, everybody agreed with that and understood that.
[825.98 --> 826.90]  Were you ready to move on?
[827.64 --> 829.10]  Was it good timing for you?
[829.22 --> 837.90]  Was it, were you done with, you know, so to speak, platformer tech and focus more on Elixir and what your next big idea might be since you were so focused on Elixir?
[838.34 --> 839.94]  That's a very good question.
[839.94 --> 845.18]  I feel like personally speaking, it's a yes or no.
[845.62 --> 845.78]  Okay.
[845.88 --> 848.02]  I'll explain why it's a yes or no.
[848.36 --> 856.32]  I mean, let's say when you build something and you have an experience, in our case, platformer tech was, I think, 12 years or maybe 13 years.
[856.32 --> 862.98]  And you work with a bunch of amazing people and you work with your founders for that period of time.
[862.98 --> 866.66]  You know, there is always that feeling like, oh, it's changing, right?
[866.66 --> 868.00]  Like the relationship is changing.
[868.12 --> 871.72]  Those are not going to be the people I talk to every day and this kind of stuff.
[871.72 --> 887.12]  But there is also like the relationship of like, you know what, like we've did this and we've built this and it went well and we feel accomplished by that terminating, which is not a feeling that you may get if that's ongoing.
[887.28 --> 887.40]  Right.
[887.40 --> 895.20]  So sometimes you feel a lot of accomplishment by saying that something has stopped and has reached a dot, has reached a stop.
[895.70 --> 895.92]  Right.
[896.02 --> 897.44]  So that's why it's yes and no.
[897.50 --> 901.16]  So I think like being able to say, oh, this was our journey that we shared together.
[901.26 --> 902.02]  This is what we built.
[902.10 --> 902.70]  We are proud.
[902.82 --> 904.60]  I think that's great.
[904.60 --> 908.12]  But of course, I miss the people that I work with.
[908.22 --> 915.06]  I mean, I still talk a lot with my co-founders and we still exchange ideas, but it's definitely a different dynamic.
[915.96 --> 918.00]  But the other aspect as well is that.
[918.16 --> 920.98]  So let's start heading a little bit into Dashbit.
[921.24 --> 922.16]  So Dashbit is my.
[922.24 --> 924.58]  Let me give an introduction for those who are not familiar.
[925.12 --> 927.06]  Dashbit is my new company.
[927.06 --> 930.72]  It's the company that I founded after Platform Attack.
[930.72 --> 936.00]  And what we do is that we offer a service called Elixir Development Subscription.
[936.60 --> 943.20]  And the idea is that we help companies like startups and big corporations to adopt Elixir.
[943.74 --> 946.98]  And we do that together with open source.
[947.18 --> 947.28]  Right.
[947.34 --> 952.46]  So we try to build this virtual cycle where we have companies working with us.
[952.56 --> 956.80]  We get positive feedback and we put that back into our open source work.
[956.80 --> 962.46]  And that hopefully leads to more companies adopting Elixir, which, you know, and then we have the cycle going.
[963.04 --> 964.24]  That's the vision with Dashbit.
[964.86 --> 971.26]  And the thing is that this vision, it has been running inside Platform Attack since 2018.
[972.20 --> 981.16]  So in 2018, basically, I had a conversation with my co-founders like, you know, like we have been investing in Elixir, mostly me, for six years.
[981.16 --> 984.12]  So since 2012, 2018, six years.
[984.38 --> 987.90]  And I would love to have more people working on Elixir together.
[988.38 --> 989.36]  That would be fantastic.
[989.86 --> 991.84]  That's something we always tried.
[991.98 --> 996.74]  But it's always hard to make that dynamic work in a consultancy.
[996.90 --> 997.08]  Right.
[997.12 --> 1002.58]  Because what you do, like maybe somebody is outside of a project for two months and then they can do open source.
[1002.80 --> 1004.44]  But then they go back to a project.
[1004.62 --> 1007.08]  So what about the work that they worked on two months?
[1007.16 --> 1007.36]  Right.
[1007.36 --> 1010.94]  So it requires more like long term investment.
[1011.42 --> 1018.16]  So when we launched the Elixir development subscription was, can we think a way that we can help companies adopt Elixir?
[1018.62 --> 1028.70]  And that can be a kind of recurrent way, a recurrent revenue for us to continue investing on open source and for us to grow our team.
[1029.10 --> 1031.90]  So this experiment has started inside Platform Attack.
[1032.46 --> 1033.52]  And it worked out well.
[1033.52 --> 1037.24]  So it started only with me and then Wojtek joined our team.
[1037.40 --> 1041.54]  So Wojtek, he worked on Ecto, a way to communicate with the database in Elixir.
[1041.66 --> 1042.98]  He works on the Hacks Package Manager.
[1043.76 --> 1045.82]  And then later, Marlos joined my team.
[1046.18 --> 1055.20]  And Marlos is involved on things like the Elixir Sense, which is like if you're using Elixir and you're using an editor and you have auto-completion, Elixir Sense helps with that.
[1055.20 --> 1066.26]  So we were able to grow the team and we were able to multiply a lot what we have been producing in terms of open source since this effort started.
[1066.76 --> 1075.24]  And what is really interesting as well is that I believe this idea, the Elixir development subscription, it has really resonated with our clients as well.
[1075.24 --> 1083.72]  Because what we would do before as a consultant is that somebody would say, hey, Jose, can you come here, stay with our team for like three days?
[1084.00 --> 1085.90]  We are kind of going to go over everything.
[1086.48 --> 1088.00]  And then it disappeared, right?
[1088.00 --> 1090.34]  So it's like a basic consultant gig.
[1091.16 --> 1092.74]  So I would do that, right?
[1092.78 --> 1094.00]  And then I would give the feedback.
[1094.18 --> 1095.00]  I would write a report.
[1095.00 --> 1101.96]  And then it would be like a month or two months later that they would then actually start working on that report.
[1102.36 --> 1104.86]  And then they're like, hey, we need help again, right?
[1104.90 --> 1107.62]  But now we are no longer under our contract.
[1107.72 --> 1108.98]  Maybe I wasn't another client.
[1109.48 --> 1117.84]  So the idea with the subscription is that you are in contact with our team all the time and we are helping you review code, discuss changes and so on.
[1118.42 --> 1122.62]  And this constant feedback, this constant communication is very important.
[1122.84 --> 1123.64]  And that's what resonated.
[1123.64 --> 1126.00]  So we started this inside Platform Attack.
[1126.42 --> 1134.26]  So when Platform Attack, the work we hire process started, I knew, and that's why I said, I just could not announce at the time.
[1134.60 --> 1138.24]  That's what I said in the blog post that I will continue involved in the same way.
[1138.42 --> 1144.40]  Because I knew that me and my team, Marlos and Voitek, we would just, you know, we already have the infrastructure running.
[1144.48 --> 1145.30]  We already have everything running.
[1145.36 --> 1147.18]  We're just going to put up a new front.
[1147.18 --> 1151.52]  But everything inside that shop, everything is how it was working before.
[1152.20 --> 1155.54]  And we will continue working with our clients.
[1156.00 --> 1158.24]  And we will continue being involved on open source.
[1158.24 --> 1170.98]  This episode is brought to you by our partners at Algolia.
[1171.30 --> 1176.08]  Make every search lightning fast and deliver the results your customers want every single time.
[1176.38 --> 1185.02]  Algolia's search as a service and full suite of APIs allow teams like ours and teams like yours to easily develop super fast search and discovery experiences.
[1185.02 --> 1190.34]  And best of all, and this will be love, Algolia obsesses over developer experience.
[1190.72 --> 1196.46]  Their mission is to give development teams the building blocks necessary to create a fast, relevant search experience.
[1197.00 --> 1202.30]  And this includes extensive documentation and guides and active community and 24-7 support.
[1202.72 --> 1206.62]  Algolia is secure, it's reliable, and best of all, it's scalable.
[1207.08 --> 1210.44]  Get started at Algolia.com and tell them Chineson sent you.
[1210.44 --> 1214.32]  That's A-L-G-O-L-I-A.com.
[1215.02 --> 1237.26]  So the Elixir development subscription, which was created inside PlatformerTech,
[1237.26 --> 1245.98]  really becomes the major first feature of your new company, Dashbit, with your two collaborators, Huitech and Marluz.
[1247.28 --> 1249.36]  Is it pretty much the exact same thing?
[1250.34 --> 1254.30]  And did you also get to take over existing clients as part of the shift over?
[1254.40 --> 1259.00]  Did Dashbit get a leg up because you had some people already doing this, or did you have to start from scratch?
[1259.68 --> 1263.50]  No, we definitely got a leg up, and it's pretty much the same thing.
[1263.66 --> 1268.96]  So really what we did was just we made the website and we went public about it because that's the other thing.
[1269.20 --> 1275.78]  Because at the beginning, when we started inside PlatformerTech 2018 with this idea, we didn't know if the idea was going to work.
[1276.22 --> 1279.12]  We didn't know if it was going to work in terms of finances.
[1279.28 --> 1281.68]  We didn't know if it was going to work in terms of dynamics.
[1281.68 --> 1287.34]  Can we actually help those companies adopt Elixir while still being involved in open source?
[1287.96 --> 1290.86]  And being involved in open source, it's really important for us.
[1290.88 --> 1293.08]  It's why we were trying this.
[1293.34 --> 1299.96]  So if I would have to spend like 80% of my time not on open source, that would not be a good deal for me.
[1299.96 --> 1304.72]  So we have been kind of like stealth doing this inside PlatformerTech.
[1305.14 --> 1308.62]  And I would mention this on Elixir Events, but I did not have a website.
[1308.90 --> 1312.82]  Like nowhere you could go to PlatformerTech website and know about this.
[1312.98 --> 1315.92]  It's a hidden feature people had to find, pretty much.
[1316.66 --> 1321.72]  Yeah, but people came to PlatformerTech to us for projects and this kind of stuff.
[1322.02 --> 1326.80]  And then depending on what they needed, we were like, oh, you want to hear more about the subscription?
[1326.80 --> 1337.10]  And that's mostly how we grew for the first, like, say, a year or a year and a half just from the incoming, like, let's say, sales pipeline.
[1337.26 --> 1343.34]  And it was good because we were able to grow, like, you know, very slowly, right?
[1343.38 --> 1346.52]  We were able to take our time and make sure that everything is in place.
[1347.00 --> 1347.26]  So, yeah.
[1347.34 --> 1350.58]  So when Dashbit came, it was literally like, hey, this is our website.
[1351.14 --> 1354.54]  Everything else was, you know, pretty much how it was before.
[1354.54 --> 1357.00]  So we definitely got a leg up.
[1357.80 --> 1359.46]  That means revenue was in place potentially.
[1360.24 --> 1371.60]  So you really were able to, I guess, navigate this acquisition, this acquihire, knowing that, you know, I'm sure you got some sort of payout yourself as part of it.
[1371.64 --> 1380.98]  But then also the next thing in to continue to be able to invest in Elixir, it's sort of, I can imagine how that would make you feel pretty secure about your next steps.
[1381.80 --> 1382.00]  Yeah.
[1382.44 --> 1383.44]  Is that pretty accurate what I said?
[1383.44 --> 1384.90]  Yeah, I think so.
[1385.00 --> 1386.54]  It goes back to the thing I was saying.
[1386.70 --> 1391.10]  You know, everybody understood what was the importance of this, right?
[1391.28 --> 1393.08]  That's why everybody was on page.
[1393.32 --> 1406.10]  Like, you know, all my followers, like we have followers that, you know, they are not technical ones, but they are really proud of us building Elixir, you know, and being able to create the software that there are a bunch of people using.
[1406.10 --> 1411.44]  So, you know, all of us had all the time Elixir best interest at heart.
[1411.44 --> 1419.40]  And that's why it was, let's say, very easy for me to do this transition because I was really supported by everybody along the way.
[1419.86 --> 1420.98]  Everybody supported it.
[1420.98 --> 1423.78]  I love the goal that's listed here on Y-Bit.
[1423.88 --> 1429.18]  The goal is to advance the Elixir ecosystem through continuous adoption and sustainable open source development.
[1429.38 --> 1437.70]  Like that, to me, the Jose I know, that's more your heart than the heart where you're doing consulting, where I guess you're still doing that through the subscription.
[1437.70 --> 1443.68]  But that goal being an overarching goal of this shift for you is super cool.
[1444.42 --> 1446.20]  Are there any other setups like this?
[1446.50 --> 1448.46]  I mean, we talked about some of the other popular languages.
[1448.72 --> 1451.36]  Most are bankrolled by major tech firms.
[1452.54 --> 1456.36]  Others are somewhat, they're just smaller or more niche.
[1457.22 --> 1459.10]  Some are started inside a company.
[1459.82 --> 1466.84]  This development, subscription, and the fact that it could just transition right out of platformer tech right into a brand new thing and still be,
[1466.84 --> 1473.44]  I would say, from my perspective as a member of the Elixir community, was like, this didn't bother me.
[1473.48 --> 1474.26]  This didn't worry me.
[1474.36 --> 1475.06]  This didn't bother me.
[1475.12 --> 1481.28]  The announcement, a lot of times when there's an announcement like this, it's a shakeup and people wonder, do I need to start looking for, like, what's going to happen?
[1482.32 --> 1484.48]  I mean, even just NPM acquired by GitHub.
[1484.66 --> 1486.12]  Like, well, it's going to happen, right?
[1486.92 --> 1490.64]  But from my perspective, I always kind of like looked at this and I was like, oh, cool.
[1490.74 --> 1492.82]  I hope that was a, you never know with an acquihire.
[1492.92 --> 1494.74]  Is this a congratulations or an I'm sorry?
[1494.74 --> 1497.40]  You know, I think it was a congratulations here in the story.
[1497.82 --> 1499.10]  So congrats to the whole team.
[1499.64 --> 1501.34]  And I'm not worried about Elixir's future.
[1501.48 --> 1504.34]  That was just my own personal response to the announcement.
[1504.50 --> 1508.24]  Is that, when you say everybody who's been behind you, has that been kind of the community reaction?
[1508.40 --> 1513.00]  Has there been any pushback or worries or fears stated to you about Elixir's future?
[1513.10 --> 1514.14]  Yeah, definitely worries.
[1514.14 --> 1517.94]  And I think they're natural, like, to be very fair.
[1518.06 --> 1527.10]  Like, there are always some people, like, the only thing that bothered me in this whole experience was that I could not prove the guarantees.
[1527.54 --> 1530.14]  Like, I said, like, I'll continue involved in the same way.
[1530.70 --> 1531.94]  Like, that's my word.
[1532.28 --> 1535.34]  And some people, they wanted proof of my word.
[1535.44 --> 1537.30]  That rubbed me in the wrong way, right?
[1537.40 --> 1540.22]  Like, because the implication is that I was lying, right?
[1540.72 --> 1541.16]  Right.
[1541.16 --> 1541.28]  Right.
[1542.24 --> 1543.80]  And you can't prove it without time.
[1543.96 --> 1545.00]  Like, you need time to prove that.
[1545.52 --> 1545.70]  Yeah.
[1545.84 --> 1547.50]  I needed time to launch Dashbit.
[1547.82 --> 1550.68]  And even if I could announce there, I think it was not a long period.
[1550.78 --> 1555.54]  I think it was a two weeks or three weeks period between we announced the Elixir and we announced Dashbit.
[1556.10 --> 1559.10]  But I also think it was a very good exercise, right?
[1559.34 --> 1563.52]  Like, you know, how the community is going to react to such a change.
[1563.82 --> 1569.60]  And it can help, like, let's say, find flaws or gaps in the community, right?
[1569.60 --> 1576.30]  Like, you know, as I said, Platform Attack was never really the big company behind Elixir.
[1576.38 --> 1576.98]  We created it.
[1577.12 --> 1579.02]  But today, it's a community project.
[1579.10 --> 1580.28]  It belongs to everybody, right?
[1580.72 --> 1583.84]  So, you know, why were people still having this impression?
[1583.98 --> 1585.96]  Why we need to improve our communication, right?
[1585.96 --> 1604.50]  So, it was still a useful exercise to see where people would feel uncomfortable and skeptical and see how we can improve the communication around those areas to make sure that, again, like, you know, if I die, right, it's not going to necessarily translate, oh, Elixir is dead, right?
[1604.50 --> 1605.56]  And this kind of thing.
[1606.00 --> 1611.40]  So, there was definitely a little bit of pushback, a little bit of things that, some things that were made the wrong way.
[1611.48 --> 1621.58]  But I feel like with the announcement that we did that we continue to invest in open source, most people, they were already reasonably comfortable or comforted, anyway, by it.
[1621.58 --> 1634.36]  And when Dashbit came along and, you know, people saw that I was involved in the same way, my team was there with me, I feel like 99% of the remaining reservations people had probably dissipated.
[1635.02 --> 1638.80]  So, since transitioning over to Dashbit, you got it launched out there a couple weeks later.
[1639.72 --> 1641.10]  Some things transferred over.
[1641.30 --> 1646.30]  For example, you mentioned Marlu's works on Broadway, which was a platformer tech project.
[1646.30 --> 1648.66]  Now it's on Dashbit Co. on GitHub.
[1648.86 --> 1651.34]  Of course, there's things inside the official Elixir.
[1651.50 --> 1654.52]  Is it Elixir-lang or the Elixir org?
[1655.50 --> 1657.22]  And then there's Ecto has its own org.
[1657.28 --> 1658.62]  So, things are kind of spread out.
[1659.34 --> 1663.32]  First of all, tell us what Broadway is for those who haven't heard of it because it's pretty cool.
[1663.38 --> 1664.36]  And we haven't talked about it before.
[1664.44 --> 1665.60]  What's this Broadway project?
[1666.20 --> 1673.10]  Yeah, so Broadway, it's a library for doing data ingestions and data pipelines in Elixir.
[1673.10 --> 1694.06]  So, you know, if you want to consume data from SQS or RabbitMQ or Google Cloud Publensub or Kafka in a very efficient way, utilizing all the cores in your machine and doing batching, automatic acknowledgments, all those kind of things that you expect from a robust data processing pipeline or data ingestion.
[1694.62 --> 1696.86]  Broadway is exactly for that.
[1696.86 --> 1703.40]  And you know what's the coolest thing about Broadway is how and why we created it.
[1703.92 --> 1709.42]  And that goes directly to what Adam was saying about, you know, like the heart of the company.
[1709.42 --> 1718.48]  So, when we started the subscription, this is still back at Platform Attack, we were working with different clients and they were using a library called GenStage.
[1718.72 --> 1720.86]  So, Broadway is built on top of GenStage.
[1721.26 --> 1725.66]  And it's called Broadway exactly because it coordinates these stages for you.
[1725.78 --> 1727.08]  That's kind of the pun in the name.
[1727.08 --> 1735.82]  So, we had a lot of companies building GenStage and they wanted, we're using GenStage, our clients, and they were building those complex pipelines.
[1736.22 --> 1740.44]  And we were seeing our clients making the same mistakes over and over again.
[1740.58 --> 1742.66]  So, we would work with them, improve.
[1742.66 --> 1750.78]  And then it came upon us like, wait, if everybody's building these and everybody is making the same mistakes, there's probably something that we can do about it.
[1750.84 --> 1753.92]  Or maybe there is a higher level of abstraction, right?
[1754.00 --> 1755.60]  So, we started working on Broadway.
[1755.68 --> 1757.38]  That's how Broadway came to be.
[1757.90 --> 1767.60]  And, you know, and it was really nice later working with those clients where they were getting their old code and they would ping us in the PRs like, we have removed like 600 lines of code.
[1767.92 --> 1771.56]  And we are adding like 50 lines of code thanks to Broadway, right?
[1771.56 --> 1783.38]  So, it was really the cycle, you know, like work with the client, see exactly where it's wrong, where it's lacking, getting that energy, putting back into open source, and then going through this whole cycle of getting this feedback.
[1783.90 --> 1785.12]  But yeah, that's Broadway in a nutshell.
[1785.88 --> 1786.22]  Super cool.
[1786.28 --> 1789.62]  So, how many of these subscriptions have you done or are doing?
[1789.74 --> 1793.80]  Is it the kind of thing where there's just like one development subscription at a time?
[1793.84 --> 1796.18]  Or since there's three of you, can you get three of them going?
[1796.46 --> 1798.50]  And what kind of projects do you work on?
[1798.50 --> 1806.46]  Yeah, so I can probably not go a lot into that just because, you know, clients, you know, confidentiality with clients.
[1807.04 --> 1807.16]  Sure.
[1807.76 --> 1814.94]  We have worked with more than 20 companies and we have multiple companies going with us at the same time.
[1814.94 --> 1821.98]  So, we are at a point where we are kind of like being very slow with taking new clients right now.
[1822.46 --> 1827.28]  Exactly because, you know, we are in a comfortable place and it always goes back, right?
[1827.30 --> 1833.28]  Like if we start having a lot of clients, we cannot reply to them or work with them in a positive way.
[1833.42 --> 1834.56]  Everything starts to go slow.
[1834.70 --> 1835.80]  So, the quality is worse.
[1836.26 --> 1838.42]  And it also goes back to open source, right?
[1838.42 --> 1846.74]  Like if we have a lot of clients and we are working all the time, we can't do open source and we are really in this because of the open source.
[1847.54 --> 1850.52]  But, yeah, we have worked with more than 20 different companies.
[1850.96 --> 1853.86]  A lot of different companies work with us at the same time.
[1854.34 --> 1858.04]  So, we're working with big companies that have like more than 100 engineers.
[1858.04 --> 1863.12]  So, it wouldn't make sense for us to review the code like produced by 100 engineers.
[1863.24 --> 1864.24]  It would never work out.
[1864.40 --> 1876.96]  So, usually the way it works is that you have a subset of your team or when it's such a big corporation like that, you have the technical leaders or people that are focusing on more or somebody that is tackling a new important product.
[1877.16 --> 1880.86]  Then, a new important project inside the company.
[1881.02 --> 1882.40]  Then, they are working with us.
[1882.40 --> 1889.46]  So, we work with different clients and with relatively small teams, let's say from like two to five.
[1890.64 --> 1895.70]  And I guess before I asked you too many questions in a row, because you skipped one of mine, which was, is there anybody else doing this?
[1896.42 --> 1898.44]  Oh, is anybody else doing this?
[1898.92 --> 1903.64]  Like you can't get a Perl development subscription or can you get a Ruby development subscription?
[1904.24 --> 1907.56]  Well, I know they are like support subscriptions, right?
[1907.56 --> 1910.92]  For many things, like databases, for example.
[1912.40 --> 1916.32]  When we started it, I've seen examples of other companies doing this.
[1916.44 --> 1921.12]  But, you know, if you go like to most like database providers, they do have kind of like support thing.
[1921.94 --> 1923.24]  Like MariaDB, for example.
[1924.02 --> 1925.40]  Yes, another example.
[1925.70 --> 1934.18]  So, and I know there are like open source projects where their model for sustainability is based on top of support as well.
[1934.18 --> 1937.36]  So, it's definitely there.
[1937.64 --> 1939.72]  You know, there are definitely other people doing this.
[1940.22 --> 1953.56]  I don't know if there are other people doing the mixture that we do today, which is, it's not really about support, but work with your team, being together in code reviews and participating in decisions.
[1953.56 --> 1957.26]  I don't know if there is that mix.
[1957.40 --> 1965.98]  I assume that, you know, if I hire like MariaDB and I'm going to design something, I can probably jump on a meeting with them in the support and talk about this stuff.
[1966.54 --> 1966.66]  Yeah.
[1966.74 --> 1973.54]  But for us, something that is very important and that's how we actually work with our clients most of the time, it's actually through code reviews.
[1973.54 --> 1975.84]  I mean, it comes down to the goal, really.
[1976.04 --> 1984.22]  The goal is to, one, advance the Elixir ecosystem and then, two, sustain the open source development of it.
[1984.32 --> 1989.26]  If that's your goals, then the reason why you're doing this is so that it can achieve those goals.
[1989.44 --> 1993.72]  So, the question is, is this a model that other teams can adopt?
[1994.18 --> 1996.94]  One question you said, Jer, was are there others doing it?
[1996.98 --> 1999.04]  But I think the bigger question is, could they?
[1999.20 --> 2001.82]  And is this working to do those two goals?
[2001.82 --> 2001.94]  Yes.
[2002.54 --> 2004.30]  Yeah, is that a question for me?
[2004.82 --> 2005.76]  Yeah, is it working?
[2006.42 --> 2007.08]  Is it working?
[2007.08 --> 2007.34]  Yeah.
[2007.88 --> 2008.44]  Oh, yeah.
[2008.62 --> 2010.08]  And is it reproducible by somebody else?
[2010.24 --> 2011.08]  I'll be very honest.
[2011.12 --> 2012.76]  I have no idea if it's reproducible.
[2013.32 --> 2015.58]  Not that because what we are doing is hard.
[2016.14 --> 2021.24]  It's just that I don't want to give anybody the impression that it's reproducible and be responsible for it.
[2021.72 --> 2021.90]  Right?
[2021.96 --> 2023.68]  It's like, it may be reproducible.
[2023.80 --> 2024.22]  I don't know.
[2024.30 --> 2026.50]  I did it just once and I don't know of anybody.
[2026.50 --> 2028.58]  Step one, make a programming language.
[2028.94 --> 2031.24]  Step two, make it extremely popular.
[2032.54 --> 2033.48]  Step three, profit.
[2034.66 --> 2035.94]  No, step three is question marks.
[2036.18 --> 2037.30]  And then step four is profit.
[2037.92 --> 2038.18]  Right.
[2038.34 --> 2041.50]  Or profit just the amount necessary so I can continue investing.
[2041.64 --> 2043.02]  Just enough to stay alive.
[2043.18 --> 2043.72]  Yeah, exactly.
[2044.92 --> 2045.12]  Yeah.
[2045.12 --> 2048.20]  Do you feel like this is working for you, like personally in your life?
[2048.84 --> 2049.04]  Totally.
[2049.48 --> 2049.62]  Yeah.
[2049.72 --> 2052.56]  I don't know usually how big are our cycles.
[2052.90 --> 2058.24]  Like, you know, when you start a new journey, how big working journey, how long it is supposed to last.
[2058.24 --> 2061.88]  But we have been doing this for two years with the team as well.
[2062.34 --> 2063.18]  We are close.
[2063.28 --> 2064.30]  We talk a lot about this.
[2064.56 --> 2066.34]  Like, you know, we are taking decisions together.
[2066.52 --> 2073.00]  So when we say, okay, let's go easy a little bit and not take new clients so we can continue comfortable.
[2073.00 --> 2074.24]  What's the decision we take together?
[2074.78 --> 2077.78]  And we are always asking ourselves, like, are we enjoying this?
[2077.86 --> 2078.80]  Like, is this working?
[2078.90 --> 2084.00]  So to answer a question directly, when we ask ourselves this question, the answer is generally yes.
[2084.00 --> 2085.00]  Like, this is working.
[2085.00 --> 2085.56]  We are happy.
[2085.68 --> 2087.56]  We are happy to work with our clients.
[2087.80 --> 2093.30]  We can work with them through interesting and challenging problems that it's always rewarding on its own.
[2093.88 --> 2100.68]  And we can continue investing on open source and doing the things that we love and see our work affect the community directly.
[2101.40 --> 2106.56]  So answering more directly, it's definitely working for us.
[2106.68 --> 2108.36]  But how much can we reproduce it?
[2108.58 --> 2109.66]  That's a very good question.
[2109.80 --> 2112.62]  And people, I guess, will have to try and we'll see.
[2112.74 --> 2114.56]  I think you'd find that out at scale.
[2114.56 --> 2120.98]  So I think if it's working and we've already identified the goals, it's personally working for you.
[2121.36 --> 2124.32]  However, there is a bottleneck in the fact that it's the three of you.
[2124.58 --> 2129.70]  So you have to sort of take on clients or subscriptions using your terminology.
[2130.74 --> 2135.82]  You have to scrutinize them more because does it take you away from the open source, you said.
[2136.38 --> 2143.68]  So I guess the question is, is this something that you could scale, desire to scale, or plan to scale?
[2144.56 --> 2154.32]  Meaning bring in more Elixir developers to sort of take your seat in the seats metaphor and enable you to add more and grow even further?
[2154.48 --> 2155.80]  Like, is that part of the plan?
[2155.80 --> 2160.06]  So right now, the answer is no.
[2160.14 --> 2163.60]  I don't want to grow our team beyond us three.
[2164.26 --> 2174.22]  And I feel like if we could grow our team, it could have a really good positive outcome, which is now we are three people working on the Elixir community and projects.
[2174.22 --> 2175.30]  What if we are five?
[2175.36 --> 2177.14]  What if we are 10 and everybody's contributing?
[2177.86 --> 2181.68]  I feel like that would be great if we could have 10.
[2182.40 --> 2191.90]  But I am worried what is going to happen with me if I am the person who is making it grow.
[2191.90 --> 2198.10]  Maybe if we are 10 and then I can come back on the show and then you ask, like, hey, Jose, is it working for you personally?
[2198.26 --> 2202.52]  Maybe my answer would be no, because I'm like, no, man, I'm not doing open source anymore.
[2202.72 --> 2205.38]  And that's why I was doing this thing in the first place.
[2205.92 --> 2214.18]  So maybe it can scale if somebody else, you know, comes and wants to make it scale and work with that part of the business.
[2214.18 --> 2216.32]  So I don't have to.
[2216.86 --> 2224.60]  But at the same time, like right now, you know, it's like when you find the perfect temperature in the AC and you're like, don't change it.
[2224.70 --> 2225.36]  Don't touch it.
[2225.68 --> 2225.86]  Right.
[2226.06 --> 2226.42]  Right.
[2227.70 --> 2230.94]  But what if you did change it and it was amazing?
[2231.32 --> 2231.98]  It's even better.
[2232.16 --> 2232.58]  Right.
[2232.82 --> 2233.88]  You never know, right?
[2234.42 --> 2235.14]  That's risk.
[2235.68 --> 2236.12]  Yeah.
[2236.28 --> 2236.92]  At its best.
[2237.54 --> 2239.82]  Not curious to find out at the moment.
[2240.00 --> 2242.98]  Maybe in the future, my mind will change or, you know.
[2242.98 --> 2247.54]  But at the moment, I am enjoying like, you know, staying small.
[2247.96 --> 2251.10]  You know, I was at a company where we were 70 to 80 employees.
[2251.54 --> 2253.28]  I kind of seen how that works.
[2253.60 --> 2257.22]  I want to celebrate staying small for now and enjoying that.
[2257.32 --> 2258.68]  And it may change in the future.
[2268.16 --> 2268.86]  Hey there.
[2268.96 --> 2269.70]  Are you curious?
[2269.70 --> 2273.46]  Because if you are, I have a podcast recommendation for you.
[2273.84 --> 2277.08]  One of the best ways to find new podcasts is to be recommended one.
[2277.18 --> 2278.38]  And that's what I'm here to do.
[2278.76 --> 2280.08]  So you may have heard this before.
[2280.14 --> 2281.66]  We have a show called Brain Science.
[2281.86 --> 2283.78]  It is literally for the curious.
[2284.20 --> 2291.76]  We're exploring the human brain to understand things like behavior change, habit formation, mental health, and really what it means to be human.
[2291.76 --> 2296.18]  So here's a preview of a recent episode 23 on Brain Science.
[2296.34 --> 2297.86]  It's called Your Brain Can Change.
[2298.20 --> 2302.84]  It's an exploration of genes, epigenetics, and neuroplasticity.
[2303.42 --> 2305.22]  And this is a skeptic of me out there, too.
[2305.32 --> 2307.88]  It's like, I don't want to give my blood to people I don't know.
[2309.22 --> 2309.58]  You know what I mean?
[2309.62 --> 2312.76]  Like, that's why I can't do the whole, what's it, three and me or something like that?
[2312.80 --> 2313.22]  What is it?
[2313.80 --> 2314.02]  Yeah.
[2314.40 --> 2317.04]  Maybe I'm advocating for something I can't even get on board with.
[2317.08 --> 2317.66]  I don't even know.
[2317.70 --> 2318.76]  I'm not trying to advocate for it.
[2318.76 --> 2321.54]  I'm just saying, be curious, so if you're cool with that, do it.
[2321.84 --> 2327.66]  But, I mean, I have a hard time giving my blood to people I just don't know because, like, your blood is a representation of you.
[2327.86 --> 2332.96]  I mean, if you were into cloning, you could rebuild an atom probably from my blood.
[2333.02 --> 2333.52]  I don't know.
[2333.62 --> 2336.16]  But that's the weirdo in me that thinks about that.
[2336.22 --> 2337.02]  But there you go.
[2337.10 --> 2337.80]  Let's end that part.
[2338.06 --> 2338.76]  I want to recognize you.
[2338.76 --> 2339.58]  I was going to say, we're going to turn.
[2339.76 --> 2340.02]  We're going to go.
[2340.04 --> 2340.50]  Unless we don't know.
[2340.86 --> 2341.42]  Let's turn.
[2341.42 --> 2346.90]  So what we're talking about, though, is conceptually neuroplasticity.
[2346.90 --> 2354.48]  What it is is literally the brain's ability to reorganize itself by forming new neural connections throughout your life.
[2355.12 --> 2366.68]  So neuroplasticity allows neurons, which are nerve cells in the brain, to compensate for injury and diseases and adjust their activities in response to new situations or changes.
[2366.68 --> 2374.14]  One way in which I could say that it would be helpful to sort of know your genes is relative to, like, autoimmune issues.
[2374.38 --> 2374.58]  Yeah.
[2374.70 --> 2384.40]  Because we've talked about stress as it relates to our immune system and going, hey, if I know that I've got a long line or even multiple people.
[2384.40 --> 2384.80]  All right.
[2384.82 --> 2394.94]  To keep listening, head to changelog.com slash brainscience slash 23 or search for brainscience in Apple Podcasts, Spotify, or wherever you listen to podcasts.
[2395.38 --> 2404.24]  Look up episode 23 titled Your Brain Can Change, where we talk about epigenetics, genes, neuroplasticity, and a story of hope and an opportunity for change.
[2404.60 --> 2410.08]  Again, changelog.com slash brainscience slash 23 or subscribe in your favorite podcast app.
[2410.36 --> 2411.18]  We'd love to have you as a listener.
[2414.40 --> 2433.88]  So you weren't busy enough and you had another big idea, which is BytePack, which I'm reading on the website was actually a yak shave from another idea.
[2433.88 --> 2439.04]  So you got things working at Dashbit in addition to the development subscription.
[2439.28 --> 2441.94]  Tell us about BytePack and what you've been working on on the side.
[2441.94 --> 2445.58]  Yeah, so BytePack, yeah, it was a yak shave.
[2445.86 --> 2450.22]  And it's a very funny story because we were working on our own software product.
[2450.38 --> 2457.82]  So something that it's not fully decided yet, but you can think like probably something based on the open core model where we would release a new project.
[2457.82 --> 2461.98]  And then there would be advanced features on top of it that would be paid.
[2462.54 --> 2465.08]  So we were working on this idea on this product.
[2465.22 --> 2471.98]  And the reason why we're working on the product is that we didn't want to build a SaaS, right?
[2472.10 --> 2476.20]  Because building a SaaS now means that, you know, maybe someone needs to be in page or dirty.
[2476.46 --> 2478.08]  Things need to be working all the time.
[2478.08 --> 2483.36]  We were working on the software product idea that people would install somehow, right?
[2483.40 --> 2489.88]  It would be an Elixir project, but maybe you would install it or as an Elixir package or as a Docker image.
[2490.24 --> 2493.54]  So we were working on this and then we figured out, okay, like, sure.
[2493.78 --> 2496.80]  But when we have this ready, what is the next step?
[2496.88 --> 2499.14]  People need to be able to buy it, right?
[2499.46 --> 2501.06]  People need to be able to buy a license.
[2501.06 --> 2504.44]  So we need to manage licenses for them.
[2504.86 --> 2507.36]  Then they need to be able to download the latest version.
[2507.52 --> 2509.98]  So we need to integrate with whatever tooling they are using.
[2510.56 --> 2514.40]  And then we'll have to create a landing page for this product.
[2514.92 --> 2518.84]  And then there are other things that I learned along the way, like things regarding taxes.
[2519.52 --> 2524.94]  I learned that if you're selling a digital good, you're actually, you may be liable for taxes in any country in the world.
[2524.94 --> 2527.34]  If some person buys from that country.
[2527.34 --> 2527.38]  Okay.
[2527.94 --> 2538.54]  So when we started looking to it and they're like, oh my God, like to put our software product like that, we need to run a service for supporting this distribution of the software product.
[2538.76 --> 2545.24]  And then we started talking to people and people do like, yeah, you know, people that were running their own software product.
[2545.56 --> 2549.18]  They already have something that they are selling to other developers.
[2549.30 --> 2551.08]  They're like, yeah, that's what I had to do.
[2551.08 --> 2554.92]  And I basically like, I MacGyver the whole solution here.
[2555.04 --> 2557.16]  Like I connect this service with the service.
[2557.34 --> 2559.42]  That brings the service that gives a token.
[2560.12 --> 2563.14]  And, you know, somehow things work together.
[2563.74 --> 2566.16]  Or, you know, sometimes it still needs.
[2566.36 --> 2570.12]  So if somebody can sell the subscription, I need to remove the token manually.
[2570.54 --> 2573.74]  And they're like, you know, it took me a lot of time, a lot of effort.
[2573.90 --> 2578.96]  And then we would actually talk to some people where they were like, I want to launch my software product.
[2579.38 --> 2581.94]  But I know I have to solve those things.
[2581.94 --> 2585.28]  And I don't know how or I don't want to.
[2585.72 --> 2598.24]  So the X-Shave came when we said like, well, what if instead of solving this problem just for us, can we solve this problem in a general way that is going to be useful to other people as well?
[2598.24 --> 2601.58]  So our goal is to still have something that works for us.
[2601.94 --> 2605.96]  But if we can help other people along the way, that's going to be fantastic.
[2605.96 --> 2615.14]  So the idea of BytePack is that we help you sell, package, and deliver software products to other developers and to companies, to enterprises.
[2615.96 --> 2616.04]  Right?
[2616.12 --> 2628.06]  So the idea is that if you are a developer and, you know, you want to sell like a pro version of a NPM package, for example, you will be able to do that for BytePack.
[2628.18 --> 2630.04]  You're going to push the package to BytePack.
[2630.14 --> 2632.06]  Your clients, they are going to receive the versions.
[2632.30 --> 2633.48]  They can audit the versions.
[2633.48 --> 2634.22]  They can control.
[2634.54 --> 2635.56]  They can download it.
[2635.92 --> 2637.90]  So that's what we started working on.
[2637.90 --> 2644.98]  And I think maybe two or three weeks ago, we launched a landing page to collect feedback on our idea.
[2645.70 --> 2648.84]  And we have a beta that we're already using internally.
[2649.12 --> 2653.28]  But, you know, what are the features that people think we should focus first and value first?
[2653.36 --> 2654.92]  What are people are most interested on?
[2655.40 --> 2655.92]  And so on.
[2655.92 --> 2656.80]  Hmm.
[2657.98 --> 2671.96]  So it's kind of like an app store, like iOS app store, where Apple handles all of the nitty gritty, the distribution, the payments, the spammers and scammers, all that kind of stuff, taxes, etc.
[2671.96 --> 2677.16]  And you just upload your binary to Apple and let them distribute it with BytePack.
[2677.26 --> 2682.92]  You just kind of send your package to BytePack and set some pricing or whatever.
[2683.12 --> 2685.52]  And then folks just install it from there.
[2685.58 --> 2687.00]  Is that in a nutshell?
[2687.86 --> 2690.42]  Yeah, that's one way to phrase it.
[2690.42 --> 2701.88]  But the thing about the app store, it doesn't necessarily give a lot of visibility to the team and the person who maintain or create that product.
[2702.28 --> 2703.66]  It's software first.
[2703.82 --> 2705.90]  And then the team is, there's a byline.
[2706.02 --> 2707.04]  There's like a author.
[2707.48 --> 2709.24]  Yeah, it's a footnote in there, right?
[2709.24 --> 2713.94]  And for us, especially if you're thinking about our perspective, right?
[2714.04 --> 2725.38]  Like we feel like if we launch a software product on any platform, one of the appeals of the software product is that it's going to be the Dashbit team behind it, right?
[2725.60 --> 2725.82]  Okay.
[2725.82 --> 2739.52]  So with the app store model, it's like it wouldn't work in that sense because we want to give visibility to the team because we think the team that is behind it, it's really going to be the kind of the soul of the product that you're selling.
[2739.72 --> 2741.50]  And we would not want to take it away.
[2741.78 --> 2745.04]  A lot of times, you know, it's like when you're working with Dashbit, right?
[2745.10 --> 2748.14]  When you're working with Dashbit, you know, sure, you like our team.
[2748.30 --> 2753.96]  But part of the reason is probably because, you know, you're also vested in the future of the Elixir community.
[2753.96 --> 2761.76]  And when you buy something that is like open core or dual license or something like that project, you know, you have that interest as well, right?
[2761.94 --> 2763.34]  You want to see that project succeeding.
[2763.72 --> 2766.18]  And it's one of the reasons why you're moving forward.
[2767.30 --> 2772.08]  I think it's very good with the app store, but there is a line we need to draw there.
[2772.64 --> 2778.40]  And recently I learned that this line even have like legal complications, for example.
[2778.40 --> 2784.22]  So one of the things that we have been exploring with BytePack is being responsible for handling taxes and so on.
[2784.84 --> 2791.78]  But that's only possible if we indeed hide who is selling the thing, if it's not a big deal.
[2791.78 --> 2800.82]  But if you want to put the people who are, you know, like if you want to make it very clear, like, oh, you are buying this because you're supporting this team and this product.
[2800.96 --> 2802.88]  And this is not something from BytePack.
[2803.00 --> 2808.88]  We actually cannot say that we are, you know, the liability for taxes may change depending on the legislation.
[2809.50 --> 2815.54]  So it has been like really interesting, like to maybe not interesting, but it has really been like.
[2815.54 --> 2821.38]  Yeah, it's a mixture of, you know, like, oh, this is annoying, but at the same time, it's interesting.
[2821.64 --> 2822.06]  It's weird.
[2822.80 --> 2829.26]  Of like, you know, navigating those waters and try to find a way where we can position BytePack.
[2829.48 --> 2831.84]  So it's most helpful for everybody.
[2832.78 --> 2835.24]  Yeah, I kind of went on a tangent there with the taxes.
[2835.24 --> 2846.68]  That note there makes me think about your goals personally with Dashbit and what we talked about there and thinking about like global tax compliance.
[2847.34 --> 2851.34]  I can't imagine personally that's something that interests you.
[2851.66 --> 2852.50]  What do you think about that?
[2853.04 --> 2853.34]  Right.
[2853.48 --> 2854.86]  So that's a good point.
[2854.86 --> 2871.36]  And I am torn on something like that, because in one side, if we can help people be successful in the platform, and that's one of the features that people are valuing it, and they think they are getting a lot of value out of it, then that can be great.
[2872.04 --> 2872.22]  Right.
[2872.46 --> 2878.60]  So that's why we put the landing page out to see on what things people are actually interested on and see what they need.
[2878.90 --> 2879.38]  Right.
[2879.38 --> 2883.46]  Because part of the goal with BytePack is exactly to help people.
[2883.46 --> 2890.04]  I like to say it's to allow people to play with the numbers, especially when you're talking about sustaining open source.
[2890.84 --> 2890.96]  Right.
[2891.14 --> 2896.66]  Because a lot of the times when you're talking to people about sustainable open source, it's a numbers game.
[2896.94 --> 2910.30]  Like if you are a really big project, then, you know, and if you want to be sustainable, if you're like really popular, you know, if you have a good onboarding experience for contributors and so on, you're going to have a lot of people contributing and joining the team.
[2910.74 --> 2912.56]  And that's going to happen like naturally.
[2912.56 --> 2915.22]  And you can achieve sustainability for that.
[2915.60 --> 2915.80]  Right.
[2915.88 --> 2925.20]  But when you consider the long tail, right, or, you know, if you're a big project and you're going for donations, sure, you're going to get a lot of donations, potentially get a lot of donations.
[2925.20 --> 2930.90]  But when you look at the long tail, right, I want to allow people to play with the possibilities.
[2931.44 --> 2933.30]  Well, you know, which one is easier?
[2933.48 --> 2938.00]  Is it easier to find a thousand people who are going to donate $5 per month?
[2938.00 --> 2947.08]  Or is it easier to find a hundred companies that would pay, you know, $50 per month to use a pro version of my product?
[2947.62 --> 2957.54]  So if doing everybody's taxes, which sounds horrible, if doing everybody's taxes can help with that, then I think that can be really, really cool.
[2957.54 --> 2961.76]  But, you know, maybe that's not where most of our value is going to be.
[2961.92 --> 2965.02]  And that's something we will have to figure out.
[2965.42 --> 2967.80]  Well, the other side of that, too, is license compliance.
[2967.80 --> 2981.22]  You know, based on the one, two, three on the, at least currently on BytePack.io, you know, step two is developers and enterprises buy this license, you know, directly through BytePack.
[2981.32 --> 2985.72]  And then they download the product using the same standard tooling, NPM, you know, whatever.
[2986.50 --> 2990.76]  Then I'm wondering if you've got to, like, somehow verifying and do license compliance, too.
[2990.76 --> 2999.80]  Right. So I think license compliance is going to be basically, what is the, I think they call it, like, honor system, basically.
[3000.28 --> 3005.86]  A lot of the people, like, who sell software products today, where they are serving through NPM and RubyGems.
[3006.32 --> 3013.30]  So if they have something that is per user, they trust you to be following the license, like, legally.
[3013.74 --> 3018.22]  And they trust you because there is actually no way for us to enforce it.
[3018.22 --> 3021.50]  Like, because if we do things, like, we could phone home.
[3021.74 --> 3027.64]  But if we phone home, I'm pretty sure it would be a no deal for a lot of big, big enterprises, right?
[3028.18 --> 3031.92]  Yeah, totally. It's going to break some sort of, like, the whole purpose. Yeah.
[3032.16 --> 3041.26]  Right. Especially because when you're installing, like, a Hex package, a RubyGems NPM package, they are usually running within your software.
[3041.26 --> 3044.36]  So if you are phoning home, I can, like, send your database credentials.
[3044.54 --> 3047.14]  I can send your client information, right?
[3047.14 --> 3056.88]  And again, if it's an NPM package or a Hex package or RubyGems, nobody's going to run, like, compiled code or obfuscated code, right?
[3056.90 --> 3061.40]  Because again, like, the person could be doing anything with that.
[3061.84 --> 3071.06]  So I feel like the nature of this module, it needs to be based on, I think it's Honor Sister or something like that, where, you know, you are putting it, like, there.
[3071.16 --> 3074.38]  And if you say, hey, you need to buy per user, but not everything's per user.
[3074.38 --> 3076.28]  Some people just say, hey, it's a teen license, right?
[3076.48 --> 3080.28]  But let's say, oh, if you're using one person as a single license, otherwise it's a teen license.
[3080.62 --> 3088.76]  And then there's basically a kind of trust situation that you are doing those things and you're going to follow those rules.
[3089.12 --> 3092.64]  And the other thing is, like, most companies, they will do that, right?
[3092.64 --> 3097.26]  Because nobody wants to have a legal trouble because they are not following certain license.
[3097.26 --> 3103.74]  And the people that they are not going to follow the license, they are probably the people that would not be interested in paying for our software in the first place.
[3104.28 --> 3106.84]  So there are those things to balance.
[3107.20 --> 3116.56]  But yeah, so with license, we are going to do a lot for, we are going to do a lot to make sure, oh, you know, if it's through license, we are going to have the UI to manage that.
[3116.56 --> 3119.42]  And, you know, for the organization, it's also great, right?
[3119.46 --> 3129.82]  Because if you're a big organization and somebody is removed from the organization, you need to make sure they did not have access for those packages and this kind of stuff because it can be a liability, right?
[3129.88 --> 3135.72]  So if somebody gets some paid software out of a company, it's actually the responsibility of that company to make sure that doesn't happen.
[3135.72 --> 3141.00]  So the corporations are also interested in making sure that all of this works together.
[3141.64 --> 3145.82]  But a lot of it will be, yeah, you know, that's what we have.
[3146.10 --> 3157.16]  And again, it goes back to the idea we're supporting the team, supporting the open source project, and everybody understanding those goals and making the correct decisions and the legal decisions as well.
[3157.16 --> 3173.62]  So would an ideal customer for BytePack be Mike Parham with Sidekick and Sidekick Pro, where you have an open source free version and then you have a freemium or an upgradable, I guess it's an open core, basically, where the additional features are then distributed via BytePack.
[3173.72 --> 3180.82]  So maybe I use Sidekick and it's hosted on rubygems.org, and then I use Sidekick Pro and it's hosted on BytePack's infrastructure.
[3180.82 --> 3187.00]  Yeah, Mike Parham would be a great example and, you know, similar ideas.
[3187.28 --> 3192.22]  Like, I like to give examples about, like, admin dashboards, for example.
[3192.34 --> 3196.92]  Sometimes, you know, depending on your framework, you want to have an admin dashboard.
[3197.60 --> 3201.66]  And I've seen in my life, like, a lot of people are starting those kind of dashboards.
[3201.66 --> 3210.04]  And then with time, the project goes and maintain because, like, it's a huge effort, like, make an admin thing that works for everybody.
[3210.04 --> 3214.42]  And most of it starts with somebody doing something that works for them.
[3214.90 --> 3220.56]  And then it starts, like, they scope, like, it starts the feature creep, right, and then becomes very complex, right?
[3220.92 --> 3226.48]  So, you know, maybe something like BytePack can actually be a way for those tools to actually exist.
[3226.58 --> 3231.76]  Because the worst scenario is when the tool is no longer there, right, because it's un-maintained.
[3232.12 --> 3235.04]  And then, you know, there is nobody maintaining that.
[3235.14 --> 3236.32]  They do not have fun.
[3236.62 --> 3238.38]  There is no tool for people to use.
[3238.38 --> 3251.78]  So, yeah, I think there are a bunch of potential ideas of things that would work for BytePack and some ideas that maybe they can find a more sustainable model when it comes to complexity and growing with time.
[3251.78 --> 3269.22]  So, essentially, if somebody has the hurdle in front of them, they're not selling something, you know, like a digital product, like a software product like this that fits this model because they don't want to deal with the essential headaches that come with tax implications that we're talking about.
[3269.78 --> 3273.60]  They would be a great candidate for the platform you're trying to build.
[3273.60 --> 3288.08]  Yeah, all the things you need to do, like setting up payments, you know, managing the licenses, and then maybe running your own version of RubyGems and, you know, making sure that that is up to date all the time or own version of NPM.
[3288.60 --> 3292.18]  If you don't want to have to do any of that, right, that's the model.
[3292.18 --> 3302.24]  But one of my hopes is just that, like, I think there are people that they don't even consider this option just because the barrier to entry is too high.
[3302.24 --> 3306.64]  And I think just reducing that is going to make more people consider it.
[3306.86 --> 3316.88]  So, it's not necessarily only about the people who have thought about this, right, and they were, like, kind of demotivated, but maybe we can make more people think about it and try different ideas.
[3316.94 --> 3319.26]  Like I said, like, try with the numbers, right, you know.
[3319.76 --> 3330.90]  And again, like, maybe BytePack doesn't work for a lot of projects as well, but if you want to find a way to make things work, having one extra option out there for you to consider and try out and explore
[3330.90 --> 3332.50]  is going to be great.
[3332.80 --> 3342.98]  I think even Mike Parham that, you know, you mentioned, he talked like he actually had to try a couple things out before he figured out what worked for him, right?
[3343.46 --> 3347.00]  You know, maybe BytePack is what's going to work for some people, maybe it isn't.
[3347.22 --> 3354.70]  But it would be interesting to see, you know, what people are going to try and if it can have a positive outcome in general or not.
[3356.30 --> 3359.34]  So BytePack's cut is on a transaction basis then.
[3359.34 --> 3364.80]  You guys are basically just taking a fee per payment as the way that you're making money.
[3365.48 --> 3367.24]  We are not sure yet, to be very honest.
[3367.68 --> 3367.82]  Okay.
[3368.22 --> 3370.70]  It can be a fee, it can be a flat fee.
[3370.92 --> 3379.68]  I think a lot of it is going to, so since we launched the page, and the page is out there, so if people want to try it out and still submit feedback, there is a form where you can say if you're interested.
[3380.22 --> 3383.88]  We are talking to a lot of people and see what works for them.
[3384.28 --> 3386.84]  Like, I don't want, so you mentioned like the App Store, right?
[3386.84 --> 3391.96]  The other thing is like the App Store has, what is it, like 30%, which is just absurd.
[3392.38 --> 3392.70]  Yeah.
[3392.94 --> 3397.08]  And I can never charge something like that because I also don't control the means, right?
[3397.18 --> 3400.42]  So like the benefits of a monopoly, let's say, right?
[3400.68 --> 3402.60]  So we are still considering that.
[3402.68 --> 3410.12]  And I really want to find something that feels like, you know, for both parties, they feel comfortable.
[3410.12 --> 3414.34]  So people are going to say like, oh my God, like they are, you know, really going after me.
[3414.50 --> 3416.24]  I want to find something that's going to work with everybody.
[3416.48 --> 3418.74]  So that's going to depend a lot.
[3419.24 --> 3429.86]  Like I personally, like I don't think, I'm not starting BytePack because I want to make it a big company, because I want to maybe, you know, get VC and then sell it later.
[3429.86 --> 3433.54]  That's not the reason, like I'm doing this to sell my own products.
[3433.54 --> 3435.50]  That's like the most important goal.
[3436.00 --> 3441.98]  So I'm not worried about creating BytePack to try to make as much money as possible for people that are using the platform.
[3442.26 --> 3443.48]  I just want it to be fair.
[3443.58 --> 3446.84]  I want to be something where I feel like, hey, this is working for me.
[3447.20 --> 3450.16]  Like I'm not losing money over this, for example, right?
[3450.16 --> 3461.68]  And, you know, we can maintain the team, continue improving the platform without being something that, you know, we are like bleeding out our, you know, the people that are selling or buying for the platform.
[3461.90 --> 3466.22]  And that's going to depend if what works best fits a flat fee or percentage.
[3467.22 --> 3469.72]  Yeah, it's still TBD to be defined.
[3470.66 --> 3471.40]  That's clear too.
[3471.60 --> 3474.70]  That's the real reason why the app store comparison falls short.
[3474.80 --> 3476.80]  You're like, hey, don't associate us with that 30%.
[3476.80 --> 3477.54]  Come on now.
[3477.76 --> 3478.56]  Yeah, right.
[3478.56 --> 3478.92]  Yeah.
[3479.16 --> 3479.36]  Yeah.
[3479.36 --> 3482.66]  Well, Apple's also or any app store out there.
[3482.82 --> 3484.54]  That's the Apple app store out there you're mentioning.
[3484.70 --> 3487.64]  But anything like that is totally a gatekeeper.
[3487.78 --> 3499.26]  But, you know, based on your current documentations and the FAQs, you're proving what you're saying by saying, you know, you're going to build directly on their payment provider account, not your own.
[3499.42 --> 3505.18]  So the subscriptions and sales will be managed by BytePack, but not the actual transaction.
[3505.18 --> 3510.86]  So currently supporting Stripe and you're giving complete access to their data and their customers.
[3510.86 --> 3514.62]  You're not, you know, you're not sort of gatekeeping these things.
[3514.62 --> 3518.94]  This is just simply by solving the problem, not so much gatekeeping the data from them.
[3518.94 --> 3519.94]  Yeah, exactly.
[3519.94 --> 3526.62]  I really don't want to be like those kind of companies, you know, especially because, like, I am an open source developer.
[3526.62 --> 3529.20]  I am a person who builds software, who writes software.
[3529.20 --> 3535.04]  I don't want to put people exactly like me in this awkward position.
[3535.24 --> 3538.52]  Like, oh, I want to leave BytePack, but they have all my customers, right?
[3538.64 --> 3547.20]  And all they give me is a CSV file that I'll have to import and manage somewhere else, you know?
[3547.36 --> 3548.14]  So, yeah.
[3548.26 --> 3555.96]  And because we are building for ourselves, I really think, you know, me as a customer, what I would be happy to use and what I would be happy to do.
[3555.96 --> 3565.72]  And making sure that me as one of the customers, that I would be happy and proud and be something that I would support and want to work with.
[3566.12 --> 3566.64]  What's the state?
[3566.82 --> 3571.74]  Is the only customer you at this point, since you mentioned your motivation was selling your own products?
[3572.52 --> 3574.00]  Is this vaporware at this current state?
[3574.16 --> 3574.84]  Where are we at?
[3575.16 --> 3579.76]  We have, like, a prototype that we are running, let's say, staging somewhere.
[3579.90 --> 3581.02]  So it's not in prod yet.
[3581.02 --> 3588.16]  And we have two other, let's say, companies or developers trying things out, uploading their packages, getting things done.
[3588.42 --> 3592.00]  But it's still in a, it's not ready to be out yet.
[3592.22 --> 3597.54]  So we are focusing a lot on, let's say, the seller workflow, people that are going to sell things on the platform.
[3597.54 --> 3600.54]  Because if we don't have sellers, there's nothing for people to buy.
[3600.70 --> 3602.40]  So that needs to be the first thing.
[3602.58 --> 3606.12]  And then next we'll start worrying about the onboarding process.
[3606.12 --> 3610.94]  But we are starting with HacksPM support because that's what we know best.
[3611.18 --> 3612.56]  It's the one for the elixir community.
[3613.32 --> 3614.98]  And because that's what we're going to use.
[3615.30 --> 3623.38]  And what's going to come after that is basically depending on who wants to get, like, jump on the train with us next.
[3624.06 --> 3626.88]  So it's definitely not vaporware.
[3626.88 --> 3630.98]  It's definitely more in, like, we are getting to beta soon.
[3631.68 --> 3637.12]  And it's already beta for some of our, let's say, our user base or our user personas.
[3638.08 --> 3646.18]  But we still need to work a little bit more to be something that we can say, like, hey, you know, you can start onboarding your buyers now.
[3646.24 --> 3648.26]  And they can download things for BytePack.
[3648.26 --> 3653.26]  So you have the form out there for people to fill out if they have some interest.
[3653.62 --> 3659.46]  And you also have the option to sign up for your launch email on BytePack.io.
[3660.36 --> 3663.02]  So if anybody's listening to this and they're thinking, like, I'm on.
[3663.30 --> 3664.20]  You have me at hello.
[3664.84 --> 3666.94]  Let me beta this thing with you.
[3667.54 --> 3671.82]  You know, is that the best route, submitting this form or getting that email subscription?
[3672.04 --> 3675.96]  Or is there a more faster route to get in touch?
[3675.96 --> 3678.12]  The form is the best.
[3678.26 --> 3679.96]  We are following the form every day.
[3680.30 --> 3687.32]  And right now we are basically using it to see what people are interested next and those kind of features.
[3688.34 --> 3693.54]  So, you know, like, apparently not a lot of people, they are interested in the landing page feature.
[3693.78 --> 3694.82]  And I think that makes sense.
[3694.90 --> 3696.84]  Like, people, they can set up their own landing pages.
[3697.38 --> 3704.18]  So, you know, we are using that to prioritize internally and also prioritize, like, which package manager we're going to support next.
[3704.18 --> 3706.18]  And then depending on...
[3706.70 --> 3712.06]  So people that have reached out to us and they're like, hey, I want to use Hex because that's kind of what we have working.
[3712.58 --> 3714.10]  We are reaching out to them immediately.
[3714.56 --> 3720.72]  And then the next is going to be as we onboard the next stages and figure out.
[3720.88 --> 3725.36]  But I'm also, like, reaching out to people who have filled in and having conversations with them.
[3725.36 --> 3738.88]  And it has been, like, really, really nice, like, just talking to people and learning MacGyver in their solution or what they struggle with and their opinion on all those different topics and how to best shape the product.
[3738.98 --> 3740.74]  It's something that I have never done in my life.
[3740.98 --> 3741.94]  And it's really cool.
[3742.04 --> 3742.68]  It's really nice.
[3742.68 --> 3745.50]  Here's a nice note from the FAQ.
[3745.70 --> 3748.78]  It says here that BytePack is 100% written in Rust.
[3751.14 --> 3751.90]  Just kidding.
[3753.80 --> 3758.46]  I assume you're still loving Elixir just like you were the first day you conceived of it, I should say.
[3758.86 --> 3759.48]  Yeah, yeah.
[3759.72 --> 3761.68]  So BytePack, we are...
[3762.30 --> 3763.94]  Yeah, it's, of course, in Elixir.
[3764.16 --> 3766.98]  And we are even implementing the other registries.
[3768.52 --> 3770.46]  We did some proof of concepts internally.
[3770.46 --> 3773.38]  So we are implementing, like, NPM in Elixir.
[3773.64 --> 3776.10]  And it has been fun, like RubyGems in Elixir.
[3776.46 --> 3776.76]  Huh.
[3778.22 --> 3787.02]  Because, you know, we need to have, like, some kind of access controls that, let's say, the official ones or the open source ones, because they're almost all open source that they don't have.
[3787.26 --> 3788.76]  So we are building our own.
[3788.84 --> 3790.06]  And it has been very fun.
[3790.68 --> 3792.50]  That sounds a lot more fun than global taxes.
[3793.26 --> 3793.58]  Right?
[3794.52 --> 3794.92]  Yes.
[3795.08 --> 3795.38]  Yeah.
[3795.70 --> 3796.96]  We're doing everything with Elixir.
[3796.96 --> 3800.08]  If we do a cargo, we may actually build it in Elixir.
[3800.46 --> 3802.58]  And the nice thing is that we are building everything with LiveView.
[3802.58 --> 3808.70]  So for those who are not familiar, like, LiveView is this new way of...
[3808.70 --> 3814.08]  It's Phoenix LiveView that came from the Phoenix App Framework for building interactive and real-time applications.
[3814.08 --> 3821.34]  And it has been also, like, super nice to, you know, to be building something very concrete with LiveView.
[3821.64 --> 3834.24]  And we have been using it to drive, like, some of the features that in LiveView, in the recent versions, it was driven by our needs, things that we feel are necessary to build the product.
[3834.24 --> 3837.92]  So it has been a really good experience so far.
[3839.00 --> 3841.74]  Ask me again in two years, and we'll see if it's to the same.
[3842.04 --> 3845.74]  But, you know, right now, at the very beginning, it's going great.
[3845.80 --> 3851.16]  And we are very excited with all those different things that we are not doing two years ago.
[3851.86 --> 3851.96]  Yeah.
[3852.24 --> 3853.16]  That's a good thing.
[3853.36 --> 3854.80]  Let's not wait four years.
[3854.92 --> 3856.90]  Let's wait two years, maybe.
[3856.94 --> 3857.66]  I'd say one.
[3857.66 --> 3861.66]  And hopefully this is out of beta and out there kicking butt before two years from now.
[3861.88 --> 3862.10]  Yeah.
[3862.24 --> 3865.22]  If you want, yeah, I can be back when it's out of beta.
[3865.74 --> 3866.08]  And, you know...
[3866.08 --> 3866.50]  Let's do it.
[3866.58 --> 3867.24]  Let's earmark it.
[3867.44 --> 3869.44]  Let's hear what the next step is.
[3869.74 --> 3873.18]  And, you know, audience, if you're listening, is thinking, like, gosh, I want to try this.
[3873.34 --> 3875.98]  BytePack.io is how you check it out.
[3876.12 --> 3876.80]  Reach out to Jose.
[3876.98 --> 3877.76]  He'll help you out.
[3878.54 --> 3882.10]  And Jose, thanks for being so dedicated to open source.
[3882.10 --> 3885.94]  And there's a lot of people out there that are very dedicated, and you're definitely one of them.
[3885.94 --> 3891.58]  To create a language, to be so inspired by Ruby, to create a language, which we use here at ChangeLog.
[3891.58 --> 3897.26]  If you haven't checked that out yet, our entire code base is Elixir, Phoenix Framework, etc.
[3897.40 --> 3898.72]  Jared, you can riff on that, but...
[3898.72 --> 3899.18]  That's right.
[3899.68 --> 3902.14]  We're appreciative of all your hard work, Jose.
[3902.34 --> 3903.48]  And it's great to talk to you again.
[3903.82 --> 3904.14]  Thank you.
[3904.16 --> 3904.78]  I appreciate it.
[3904.90 --> 3905.84]  Thanks for having me.
[3906.34 --> 3906.74]  Anytime.
[3909.22 --> 3911.18]  So awesome to catch up with Jose again.
[3911.18 --> 3917.12]  If you want to catch up with him as well, the easy way, one of the easy buttons, at least, is to comment on this episode.
[3917.52 --> 3920.82]  This is episode 402, but no payment is required for comment.
[3921.14 --> 3926.96]  You can drop your comment at changelog.com slash 402, or head to the show notes and click discuss on ChangeLog News.
[3927.06 --> 3927.84]  We'd love to hear from you.
[3928.18 --> 3930.48]  Of course, huge thanks to our partners who get it.
[3930.92 --> 3933.34]  Linode, Fastly, and Rollbar.
[3933.34 --> 3937.50]  And also, huge thanks to that Beat Freak Breakmaster Cylinder for making all of our beats.
[3937.56 --> 3938.20]  We love them.
[3938.40 --> 3939.18]  Hope you love them, too.
[3939.74 --> 3942.34]  And last but not least, subscribe to our master feed.
[3942.46 --> 3944.24]  Head to changelog.com slash master.
[3944.68 --> 3947.86]  Or search for ChangeLog Master in your favorite podcast app and subscribe.
[3948.00 --> 3948.70]  You'll find us.
[3949.02 --> 3950.86]  It is one feed of all of our podcasts.
[3951.18 --> 3954.14]  Get everything we ship in one single feed.
[3954.42 --> 3956.14]  Again, changelog.com slash master.
[3956.68 --> 3957.96]  Thanks again for tuning in this week.
[3957.96 --> 3958.96]  We'll see you next week.
[3963.34 --> 3993.32]  We'll see you next week.
