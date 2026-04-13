[0.00 --> 7.00]  If I'm blocking Angelica's pull request and I leave a bunch of comments and some of them are like, great job, this is really cool.
[7.00 --> 10.22]  And some of them are style and some of them are actually questions.
[10.22 --> 13.82]  And then some of them are actual blocking like requests for changes.
[13.82 --> 24.48]  It helps kind of narrow to those and like create more of a clear checklist in a way of what you're expecting to be changed before being asked to re-review the code.
[24.48 --> 35.54]  So I just think it's helpful, even if you are formally like blocking the pull request to communicate like what things you expect to be changed before you think that it could be merged.
[35.92 --> 44.88]  Gotcha. I don't know if I was just projecting my own fear, like seeing the email where it says this has been like changes have been requested and oh no, what did I do wrong?
[45.22 --> 46.18]  I need to do that.
[46.80 --> 49.76]  Don't worry, we all do stuff wrong in our pull requests all the time.
[50.14 --> 51.46]  That's part of being an engineer.
[54.48 --> 60.84]  This episode is brought to you by Sourcegraph with the launch of their Code Insights product.
[60.84 --> 63.84]  Teams can now track what really matters in their code base.
[64.16 --> 70.46]  Code Insights instantly transforms our code base into a queryable database to create visual dashboards in seconds.
[70.94 --> 73.90]  And I'm here with Joel Cortler, the product manager of Code Insights for Sourcegraph.
[74.36 --> 84.06]  Joel, the way teams can use Code Insights seems to pretty much be limitless, but a particular problem every engineering team has is tracking versions of languages or packages.
[84.58 --> 87.26]  How big of a deal is it actually to track versions for teams?
[87.72 --> 89.46]  Yeah, it's a big deal for a couple of reasons.
[89.64 --> 91.46]  The first is, of course, just compatibility.
[91.46 --> 95.58]  You don't want things to break when you're testing locally or to break on your CI systems or test systems.
[96.06 --> 102.24]  You need to have some sort of level of like version unification, minimum version support, and all of that needs to be compatible forward.
[102.24 --> 116.38]  But the other thing we learned was that for a lot of customers, especially, you know, engineering organizations that are pretty established, they have older versions of things or even older versions of like SaaS tools they don't use anymore that they haven't fully removed because they're like not sure if it's still in use or they, you know, lost focus on that.
[116.38 --> 119.50]  And they're spinning up old virtual machines that they're still paying for.
[119.62 --> 123.62]  They're using, you know, old SaaS subscriptions they're afraid to cancel because they're not sure if anyone's actually using it.
[123.74 --> 137.00]  And so getting off of those versions not just like saves you the headaches and the risks and the vulnerabilities of being on old versions, but also literally the money of, you know, older systems running more slowly or the build times or, you know, virtual machines and SaaS tools that you're no longer using.
[137.00 --> 139.22]  Before you had this ability, we talked to teams.
[139.52 --> 140.90]  There are basically three ways you could do this.
[141.18 --> 144.62]  You could slack a million people and ask for just like an update point in time.
[144.88 --> 153.88]  You could have sort of one human in one spreadsheet where like it's somebody's job every Friday or every two weeks to just like search all the code and find all the versions and write it down in a Google sheet.
[154.12 --> 158.40]  Or there were a couple of companies I came across with in-house systems that were sort of complicated.
[158.60 --> 161.52]  You had to know, you know, maybe Kotlin, but you didn't know Kotlin.
[161.52 --> 168.80]  But if you want to use this system, you had to learn Kotlin and you'd have to sort of build the whole world from scratch and run basically a tool like this with a pretty steep learning curve.
[169.18 --> 176.72]  And now for all three of those, you could replace it with a single line source graph search, which is basically just the name of the thing you're trying to track and the version string in the right format.
[176.98 --> 180.24]  And then we have templates that will help you get started if you're not sure what that format is.
[180.36 --> 183.50]  And then it'll automatically track all the different versions for you, both historically.
[183.68 --> 185.84]  So even if you start using it today, you can see your historical patterns.
[185.96 --> 187.30]  And then, of course, going forward.
[187.90 --> 188.10]  Very cool.
[188.16 --> 188.56]  Thank you, Joel.
[188.56 --> 193.10]  So right now there is a treasure trove of insights just waiting for you.
[193.44 --> 199.96]  Living inside your code base right now, teams are tracking migrations, adoption, deprecations.
[200.28 --> 203.14]  They're detecting and tracking versions of languages and packages.
[203.14 --> 207.10]  They're removing or ensuring the removal of security vulnerabilities.
[207.48 --> 209.06]  They understand their code by team.
[209.14 --> 210.84]  They can track their code smells and health.
[210.84 --> 215.40]  And they can visualize configurations and services and so much more with code insights.
[215.40 --> 222.02]  A good next step is to go to about.sourcegraph.com slash code dash insights.
[222.30 --> 224.84]  See how other teams are using this awesome feature.
[225.08 --> 229.90]  Again, about.sourcegraph.com slash code dash insights.
[230.16 --> 231.92]  This link is in the show notes.
[231.92 --> 248.04]  Let's do it.
[248.80 --> 249.70]  It's go time.
[250.44 --> 255.52]  Welcome to Go Time, your source for diverse discussions from all around the Go community.
[256.04 --> 257.14]  Subscribe to the pod.
[257.14 --> 260.82]  If you haven't yet, head to go time.fm for all the ways.
[261.16 --> 263.54]  And if you dig the show, please do tell your friends.
[263.70 --> 264.48]  That'd be pretty cool.
[264.92 --> 269.40]  Special thanks to our partners at Fastly for shipping all of our pods super fast to wherever
[269.40 --> 270.00]  you listen.
[270.22 --> 271.94]  Check them out at fastly.com.
[272.04 --> 273.90]  And to our friends at fly.io.
[274.40 --> 276.50]  Post your app servers close to your users.
[276.72 --> 277.66]  No offs required.
[278.10 --> 279.40]  Learn more at fly.io.
[279.70 --> 280.60]  Okay, here we go.
[282.36 --> 286.32]  Hello and welcome to Go Time.
[286.32 --> 290.08]  Today we're going to be talking about PRs.
[290.36 --> 291.50]  What makes a good PR?
[292.06 --> 294.22]  How do you do the best PR review?
[294.80 --> 299.72]  Is there such thing as a PR that is too small, too big, too filled with emojis?
[300.20 --> 305.22]  We'll be debating all the details and trying to help our fellow gophers master the art of
[305.22 --> 305.62]  the PR.
[306.18 --> 309.40]  Today I'm joined by three wonderful PR pros.
[309.40 --> 316.78]  First, we have the wonderful Jeff Hernandez, who is a associate software engineer at the
[316.78 --> 317.44]  New York Times.
[317.88 --> 318.52]  Hello, Jeff.
[318.62 --> 319.34]  How are you today?
[319.80 --> 321.26]  Hi, doing well.
[321.36 --> 322.28]  Thanks for having me back.
[322.50 --> 323.74]  Thank you for joining us again.
[324.58 --> 329.04]  Next up, we have Sarah Duncan, who's a staff software engineer at the New York Times.
[329.04 --> 333.62]  She also teaches an introductory programming course at a high school.
[333.86 --> 335.00]  So thank you for joining us.
[335.04 --> 336.78]  I know you're a first time Go Time guest.
[336.94 --> 338.22]  So lovely to have you.
[338.72 --> 339.58]  Yeah, thanks for having me.
[339.94 --> 345.56]  And last, but certainly not least, we have Natasha Dykes, who is a senior software engineer
[345.56 --> 349.10]  at the New York Times and happens to be a cycling enthusiast.
[349.46 --> 349.64]  Hi.
[349.92 --> 350.70]  Thanks for having me.
[351.04 --> 351.44]  Hiya.
[351.76 --> 352.98]  Thank you for being here.
[352.98 --> 360.58]  And we have the beautiful, the wonderful, the incomparable Natalie, who is my co-host.
[361.02 --> 361.28]  Hello.
[361.84 --> 362.68]  Hi, Angelica.
[362.74 --> 365.16]  I think it's very smooth you skip pronouncing my last name.
[365.22 --> 366.50]  I would probably do the same thing.
[366.58 --> 368.10]  It's so complicated.
[368.84 --> 370.56]  I haven't been on in a hot second.
[370.56 --> 375.48]  So I'm kind of trying to minimize the amount of babbling and mistakes I get myself into.
[376.74 --> 377.60]  Great strategy.
[378.06 --> 380.34]  Yeah, we'll see if that persists throughout the episode.
[380.34 --> 383.62]  I might just get overexcited and fumble over my words.
[384.12 --> 385.94]  But thank you all for joining me today.
[386.14 --> 388.90]  I'm extremely excited to talk about PRs.
[389.12 --> 391.02]  So we're going to start with the very basics.
[391.66 --> 394.40]  What is a PR and why do we even do them?
[394.86 --> 398.76]  So I'm going to pass over to you, Sarah, when you're talking to your wonderful high school
[398.76 --> 400.92]  students and they go, what is a PR?
[401.06 --> 402.00]  Like, what is this thing?
[402.42 --> 403.46]  How do you explain it to them?
[403.82 --> 404.04]  Sure.
[404.04 --> 411.88]  Well, PR stands for a pull request and it is typically used to refer to somebody who's
[411.88 --> 416.90]  been making changes to a shared code base, making a request to add those changes back
[416.90 --> 419.94]  into the common main.
[420.50 --> 422.22]  Typically, it's like a branching situation.
[422.36 --> 424.26]  So it's the main branch of that code base.
[424.70 --> 429.90]  And that also typically corresponds to moving that code into production if it's a production
[429.90 --> 430.38]  system.
[430.38 --> 438.02]  So it's a way to get a review on your work and basically ask to add code to the main
[438.02 --> 438.42]  system.
[439.08 --> 439.90]  And why is it useful?
[440.14 --> 441.78]  Why is this something that we want to be doing?
[442.14 --> 446.08]  Is that something that maybe, I don't know, like Jeff, do you find PRs useful?
[446.56 --> 450.18]  I mean, coming from like, at the times, at least I'm an associate software level.
[450.24 --> 451.42]  So I'm kind of like the entry level.
[451.90 --> 457.46]  So it's a great way to get feedback from my senior engineers and basically get a lot of
[457.46 --> 462.42]  kind of feedback from them in terms of like what I can be doing better or like kind of
[462.42 --> 464.56]  like code structure, how that could be improved.
[464.90 --> 468.26]  Or even like tiny little like optimizations.
[468.66 --> 473.74]  Or maybe there's a certain way that, for instance, Go likes to do things because as we all know,
[473.78 --> 474.70]  Go is very opinionated.
[475.48 --> 480.42]  So it's just it's like a way to tap into that resource from our senior engineers.
[480.42 --> 485.78]  I feel like it's a great tool, especially for someone that's coming into a new team,
[486.16 --> 490.54]  kind of getting the lay of the land, getting the norms that you typically might not get
[490.54 --> 492.52]  like in through other forms of documentation.
[493.72 --> 494.16]  No, for sure.
[494.66 --> 500.38]  And in terms of assessing PRs, is there such thing as a good PR review?
[500.48 --> 502.86]  Is there such thing as a bad PR review?
[502.86 --> 509.14]  I would love to hear how you assess going about either putting in a PR or reviewing a PR.
[509.76 --> 515.52]  Maybe Natasha, like when you're putting in a PR, how do you decide whether it's time to go
[515.52 --> 518.18]  or whether you need to wait and do some more work?
[518.26 --> 521.34]  Like at what point do you feel like, no, this is ready to be reviewed by my peers?
[521.84 --> 526.16]  I think for me, it's helpful when I review like a ticket.
[526.30 --> 529.40]  Usually it's for a feature or something that I'm working towards.
[529.40 --> 534.22]  Sometimes I review to see if like the work that I've done actually meets the requirements.
[534.68 --> 537.80]  And at that point, I can either say like, okay, it's ready to go.
[538.12 --> 543.84]  I've cleaned up any notes for myself or made sure I did like go format, all of those small
[543.84 --> 544.28]  things.
[544.40 --> 545.46]  And then I'll open up a PR.
[545.80 --> 551.02]  But I would say like, you can even open up a PR before you're ready, like ready to merge.
[551.12 --> 553.18]  Sometimes it's good to just get that early feedback.
[553.60 --> 556.08]  So it really depends on the work that I'm doing.
[556.08 --> 559.72]  And Natalie, I see your intake of breath.
[560.02 --> 561.32]  Do you have something you'd like to add?
[561.70 --> 561.96]  Yeah.
[562.12 --> 564.72]  You asked earlier, what is a PR?
[564.98 --> 567.80]  And it's interesting also to compare PR and CR.
[568.10 --> 569.80]  And why is it even pull, right?
[570.12 --> 573.22]  So PR, as Sarah said, stands for pull request.
[573.74 --> 576.28]  So let's split that into two questions.
[576.76 --> 577.36]  Why pull?
[577.52 --> 578.20]  Why not push?
[578.30 --> 579.10]  Why not merge?
[579.14 --> 580.68]  Or some other thing?
[580.68 --> 584.70]  And what is the difference or what do you prefer?
[585.12 --> 589.20]  CR, which stands for code review or PR as pull request.
[589.64 --> 591.02]  It's an interesting question to discuss.
[591.12 --> 595.08]  It's also interesting, even a little bit in the concept of like, what does that represent?
[595.56 --> 596.94]  Curious to hear everyone's thoughts.
[597.52 --> 602.74]  I think code review is more semantically correct for like the work that I'm typically doing.
[602.74 --> 608.32]  But I think the changes that you could potentially make don't necessarily need to touch code.
[608.88 --> 610.50]  It could be like a readme update.
[610.62 --> 616.88]  It could be some other stuff that's like kind of supporting the repository versus just the code.
[617.54 --> 619.72]  I don't know why it's called pull request though.
[619.98 --> 620.84]  Never really thought of that.
[620.98 --> 623.46]  So curious to hear what others think.
[623.88 --> 631.64]  Now this gets me kind of wanting to go to Wikipedia and kind of learn about where pull request came from and like that whole background.
[631.64 --> 639.20]  That's one of the things I'm like interested about, like just like where everything came from in terms of like software engineering best practices and naming conventions.
[639.20 --> 648.54]  Because once you're in the industry, you know, it's just something we know, you know, but it's not something that like, at least it's like, it's a term that's used across the whole industry.
[648.54 --> 653.12]  But it's not something that we as a team or something that we choose to use.
[653.14 --> 656.42]  It's just kind of like a shared language among software engineers.
[656.58 --> 656.70]  Right.
[656.70 --> 659.96]  So I was super cheeky and I did Google it just now.
[659.96 --> 669.10]  And it says that the name pull request comes from the idea that you're requesting the project to pull changes from your fork.
[669.70 --> 677.60]  That might not encompass all ways that we now use it in our language, but that's what Google's telling me on the top line.
[678.52 --> 679.52]  Yeah, it is interesting, right?
[679.56 --> 680.78]  You have this project.
[680.88 --> 683.26]  I mean, most of us use Git in some way.
[683.46 --> 688.66]  GitHub, GitLab, or I don't know too many other personal variations, but I'm sure that exists as well.
[688.66 --> 702.32]  So we're all kind of eventually are used to the concept of like having a main branch and then making branching kind of your changes from that and then asking to merge that back, whether frequent or not frequent.
[702.32 --> 705.52]  And yeah, like we all say PR.
[705.80 --> 711.76]  I've been always saying PR, but then recently I had to work with a ticketing system that is called ClickUp.
[711.76 --> 716.04]  And there they said that the label was code is in CR.
[716.62 --> 718.22]  And that was kind of interesting.
[718.76 --> 721.86]  Probably the first time I remember, let's say, encountering this.
[722.00 --> 726.34]  So I also went to dive a little into the semantics of that.
[726.86 --> 731.94]  Then there's also merge request, which kind of makes sense, but actually also not really in use.
[732.30 --> 736.20]  I've also heard it called like a changelog or CL.
[736.20 --> 738.78]  So there's a lot of different terms for it.
[739.18 --> 741.76]  What are you familiar with, you know, changelog to be?
[742.14 --> 747.94]  It's the same thing as like a pull request, but that's the certain companies call it a changelog.
[748.16 --> 749.78]  So you're submitting a changelog?
[750.00 --> 752.00]  Yeah, that's what I've understood it to be.
[752.16 --> 753.94]  It's just like something I heard in passing.
[754.70 --> 764.58]  Yeah, I've seen that in like in the Go repository, like in references to like the actual like the GitHub Go repo and like issues, people referring to changelogs.
[764.58 --> 765.90]  Yeah, it's a Google thing.
[766.12 --> 766.84]  It's a Google thing.
[766.92 --> 769.70]  Yeah, we'd totally be interested in learning more about that.
[770.20 --> 776.68]  That was me thinking that like the most basic of questions, what is a PR was just me doing my due diligence for the newbies.
[776.70 --> 778.30]  But now I see it's a whole debate.
[779.34 --> 781.22]  So many different words to use.
[781.22 --> 782.12]  This is great.
[782.24 --> 787.82]  We're opening up a Pandora's box of PR words and ways to think about code.
[788.04 --> 788.62]  I mean, right.
[788.74 --> 790.12]  Software is all about naming things.
[790.70 --> 791.78]  It starts this early.
[791.78 --> 800.84]  Okay, so when you're thinking about a PR, like I've heard many people complain about, oh, this PR is too long or this PR is so short.
[800.92 --> 802.36]  Why didn't you put it in one big PR?
[802.60 --> 805.86]  Is there such thing as a too long or a too short PR?
[805.98 --> 806.86]  Too big, too small?
[807.00 --> 812.42]  Or is it really just down to like dealer's choice, whatever that team is happy to review?
[812.42 --> 822.44]  If you're happy to review a thousand line PR or a five line PR, I'd love to hear anyone's view on kind of the length of the PR and how big it should be.
[822.44 --> 832.18]  Yeah, I definitely think that pull requests or merge requests or code reviews, these can be too long.
[832.58 --> 834.54]  Sometimes a pull request is too large.
[834.78 --> 847.36]  And my benchmark for helping set that norm on my team for what is an appropriate size pull request is really around like how well the pull request can be reviewed.
[847.36 --> 861.14]  So if you do have like a thousand line pull request, another common adage about engineers, like we're lazy and we're not probably not going to review a thousand line pull request as in depth as we would a 20 line pull request.
[861.56 --> 868.46]  So I think it's about thinking about how you can best set up your reviewers to give you a quality, thorough review.
[868.46 --> 881.84]  So I have some thoughts around like how to set that norm, but I'd love to hear from others like what you think about a length of a PR and whether a pull request can be too big or too small.
[882.36 --> 888.96]  Yeah, I don't think a pull request can necessarily be too small because it just takes one character to make a bug.
[888.96 --> 891.28]  So you're going to have to make that change.
[891.66 --> 894.50]  But I do think that I agree with you.
[894.62 --> 906.18]  It could be too long to kind of have a reviewer to actually sit down and understand all the changes, especially if they're not as familiar with you or with the code as you are.
[906.40 --> 916.32]  So I don't necessarily have the best strategy, but I think just like encapsulating certain functionalities, I think helps instead of just like an entire feature.
[916.32 --> 919.90]  Because it might be broken down into different kind of core parts.
[920.32 --> 922.62]  So that's typically how I lean on it.
[923.62 --> 924.86]  Now, Jeff, you have any thoughts?
[925.50 --> 929.98]  Yeah, I think that's it's totally like depending on what you're working on at the current moment.
[930.16 --> 930.38]  Right.
[930.46 --> 939.06]  So if you're building a new API from the ground up, like setting up the handling for the JSON, the payload, maybe that can be a PR.
[939.24 --> 941.38]  And then the actual business logic can be a separate thing.
[941.44 --> 942.68]  You're building up as you go.
[942.74 --> 942.90]  Right.
[942.90 --> 955.74]  And that's kind of something that I've learned from other people on the team because I have been guilty of this extremely large PR is where the ticket is done, but it's all in one PR and no one wants to review it.
[955.78 --> 960.92]  So you're going to maybe get a review if my next week, if you keep pinging people and bothering them.
[961.04 --> 963.46]  But otherwise, no one's going to want to touch that.
[963.46 --> 972.06]  And then you don't ever want to get in a situation where you have to offer to kind of go step by step with the reviewers.
[972.70 --> 975.28]  Like I've made this change because of this reason, like on a call.
[975.40 --> 980.22]  I feel like that's the worst case scenario where you have to actually walk them through it.
[980.56 --> 984.62]  Sometimes it's necessary, but it's something I would avoid.
[984.98 --> 986.10]  And I don't know.
[986.16 --> 988.10]  It's just it's kind of like a walk of shame.
[988.10 --> 992.28]  I mean, like you have to go through the whole thing with them, but they can definitely be too big.
[992.38 --> 996.02]  Walk of shame or you can like walk through the glory of your coding.
[997.38 --> 998.12]  I guess.
[999.76 --> 1000.70]  I'm just teasing.
[1000.90 --> 1002.08]  It's all how you think about it, right?
[1002.44 --> 1008.70]  Look at this beautiful PR that I constructed over many months that you now have to review with me.
[1009.22 --> 1011.84]  Look at this clever naming convention I did.
[1011.96 --> 1013.38]  Look at this great function.
[1014.04 --> 1015.62]  Don't you love this go routine?
[1018.52 --> 1024.94]  Also, so we talked a little bit about what you alluded to, Sarah, like being cognizant of the people who are reviewing your PR.
[1025.40 --> 1030.90]  So I'd love to hear a little bit about kind of how many people should review your PR before you merge it.
[1031.24 --> 1032.08]  Is it one person?
[1032.18 --> 1032.86]  Is it two people?
[1032.94 --> 1034.36]  Is it the entire team?
[1034.36 --> 1042.90]  What are the thoughts around like reviewing the PR and how many people need to know about this great work you've done before it's in the world?
[1043.38 --> 1044.30]  Natalie, you're smiling.
[1045.18 --> 1046.50]  I'm sorry I'm doing this again.
[1046.58 --> 1048.20]  I want to bring back to the previous question.
[1049.92 --> 1050.70]  Do it.
[1051.10 --> 1053.66]  So when you say too long or too short, what do we measure?
[1054.34 --> 1058.94]  Number of lines, number of commits, number of files.
[1058.94 --> 1062.30]  It can be depending on many things.
[1062.64 --> 1064.40]  The answers can vary in the same PR.
[1065.00 --> 1069.44]  Like it can be one PR where you removed one file, but that's like many lines.
[1069.90 --> 1070.40]  Is that long?
[1070.46 --> 1070.84]  Is that short?
[1071.44 --> 1072.58]  This is my thought now.
[1072.76 --> 1076.98]  But whoever listens doesn't know that Angelica can see me thinking out loud like that.
[1077.24 --> 1079.36]  So I'm guessing there's a question coming up.
[1079.36 --> 1085.62]  So you have to trust her psychic abilities as a product manager to kind of look at the engineers in front of her and like, you want to say something?
[1085.84 --> 1086.02]  Speak.
[1086.54 --> 1088.44]  That's the secret superpower of product managers.
[1088.66 --> 1089.42]  I can see it.
[1089.56 --> 1093.16]  Also, I'm learning like now, actually, just as a go time host.
[1093.28 --> 1097.94]  Every time I ask a question, I should pause and defer to Natalie and be like, do you have a follow up question?
[1099.88 --> 1101.06]  That is a great question.
[1101.14 --> 1102.42]  I'm very glad that you asked it.
[1103.22 --> 1104.40]  That definitely makes sense.
[1104.50 --> 1105.30]  Asked it.
[1106.06 --> 1106.78]  Really babbling.
[1107.32 --> 1108.36]  Do you have a view on that?
[1108.94 --> 1109.30]  Yes.
[1110.12 --> 1110.48]  Wonderful.
[1110.66 --> 1111.66]  I'd love to hear it.
[1112.16 --> 1114.72]  But we're here to hear other people's opinions.
[1114.94 --> 1118.94]  So I am curious to hear the crowd's opinions more than I am interested in sharing.
[1119.14 --> 1121.76]  I mean, I'm also happy to share mine, but I'm more curious about others.
[1122.44 --> 1124.80]  Is there like a convention in your team, for example?
[1124.96 --> 1127.14]  How do you, would you say this is too much?
[1127.20 --> 1128.04]  Like, what would you look at?
[1128.20 --> 1131.94]  Yeah, I'm really curious about hearing more about Sarah's like the team standard.
[1131.94 --> 1139.26]  But at least from me, if I'm reviewing something, the first thing I look at is the number of files that were changed.
[1139.80 --> 1141.22]  That's just like the easiest thing to look at.
[1141.28 --> 1145.86]  If it's like a long list, I am going to go to lunch maybe and then come back to it later.
[1146.18 --> 1153.84]  It's definitely easier to just see, to review something that's like a couple files versus something that's touching multiple directories at a time.
[1153.84 --> 1159.08]  And then because I have to go back and forth referencing things and seeing how it might affect other things.
[1159.54 --> 1162.72]  It's just definitely files would be my number thing, number one thing.
[1162.80 --> 1165.24]  And then typically the norm on our team is one commit.
[1165.38 --> 1167.72]  So it's not something like one commit per PR.
[1167.90 --> 1171.30]  So it's not something that gives much information for us.
[1171.78 --> 1174.76]  Yeah, I definitely think files are a good initial indicator.
[1174.76 --> 1190.76]  And sometimes that can be misleading because you could have a bunch of files only have one line change or you moved a folder into a subfolder and that changed like a bunch of files and you can just check all those off as okay.
[1191.24 --> 1197.12]  But I think that it's a good question, Ali, because I think it's a hard thing to actually measure well.
[1197.12 --> 1210.02]  And the analogy I try to use and that I recently used at the New York Times to kind of explain like how to break down your PRs ties into your question, Angelica, about the number of reviewers.
[1210.44 --> 1222.32]  But my analogy is that if my ticket is to bake a cake and let's say it's chocolate cake, we've got some buttercream frosting, little raspberry layer in there.
[1222.38 --> 1223.12]  It's a nice cake.
[1223.12 --> 1235.10]  Like if I go and bake the cake and come back and Angelica, you're a frosting expert and Jeff, you are a cake expert and Natasha, you are the absolute queen of fillings.
[1235.64 --> 1236.42]  It's harder.
[1236.66 --> 1243.78]  I have to get all of you in a room and cut a slice of cake and like you have to pick it apart and like be an expert on your piece.
[1244.04 --> 1249.18]  And it takes more work to give feedback and it takes more work for me to go fix something.
[1249.18 --> 1256.18]  So if I'm trying to perfect the chocolate cake and Jeff, you're like, this cake is too dry.
[1256.42 --> 1260.14]  Like you have to go back and make it make it less dry.
[1260.52 --> 1265.12]  That is so much more work for me to reconstruct that cake all over again.
[1265.78 --> 1273.98]  But if I break that down and first I make my my chocolate sponge, Jeff, you taste that you give me feedback on it.
[1273.98 --> 1279.08]  I make my filling that I'm going to use Natasha, I get your input on that Angelica.
[1279.28 --> 1284.08]  I ask you for your input on the frosting and kind of perfect those individual pieces.
[1284.08 --> 1290.08]  And then I assemble that final assembled cake is going to be a lot more successful.
[1290.08 --> 1302.04]  So I like to think about it as like breaking it down so that I ideally one person could review it and maybe like one subject matter expert could review that part.
[1302.98 --> 1306.42]  And then when we get to the assembly piece, you're judging me on the assembly.
[1306.56 --> 1311.56]  You already know that the individual components are what we're on the same page about what those components are.
[1311.56 --> 1319.30]  So I think I think it's a hard thing to measure because even just that like, oh, one subject matter expert is not like a hard and fast rule.
[1319.52 --> 1324.60]  This is one of the things I think is something that comes more with experience and intuition.
[1325.00 --> 1332.98]  It's like a skill that you're able to hone as you gain more experience around like what the right size to ask for feedback on is.
[1332.98 --> 1344.78]  But that's my my analogy is that if you're baking a cake and you're asking for a review on it, it's easier to get the individual components reviewed first and then bake your cake or assemble your cake.
[1347.68 --> 1349.28]  That was so great.
[1350.30 --> 1353.58]  It's the teacher in me, you know, we got to bring in the fun things.
[1355.96 --> 1356.98]  That was wonderful.
[1357.26 --> 1358.62]  I feel like I've learned so much.
[1358.72 --> 1362.78]  Genuinely, I will never think of could be ours and construction of a.
[1362.78 --> 1363.42]  Now they're cake.
[1363.42 --> 1364.74]  Feature again in the same way.
[1365.20 --> 1367.14]  Like, can I see the frosting, please?
[1367.24 --> 1367.46]  Please.
[1368.12 --> 1369.38]  Let me check the topping.
[1369.58 --> 1369.74]  Yeah.
[1369.90 --> 1371.10]  How moist is the cake?
[1371.86 --> 1373.30]  How moist is this cake?
[1373.60 --> 1378.02]  I'm going to be very careful who I say that to because some people don't really like the word moist.
[1378.74 --> 1381.00]  I don't particularly, but it's fine.
[1381.74 --> 1382.48]  Judge your audience.
[1382.68 --> 1382.84]  Yeah.
[1383.64 --> 1384.48]  Judge your audience.
[1384.48 --> 1385.58]  Good perception.
[1386.54 --> 1391.46]  So flipping over kind of to the other side of a PR.
[1391.46 --> 1395.44]  How do you go about reviewing a PR?
[1396.00 --> 1396.76]  I'm going to pause.
[1397.12 --> 1403.68]  Natalie, would you like to talk about putting in a PR in any more detail before we switch over?
[1403.90 --> 1404.30]  No, no.
[1404.38 --> 1404.62]  Sorry.
[1404.72 --> 1406.76]  I'll go back to being German and sticking to the schedule.
[1408.30 --> 1408.88]  No, no, no.
[1408.88 --> 1409.66]  Please don't.
[1409.96 --> 1410.24]  I was.
[1410.52 --> 1413.10]  That came across like I was being a little bit sassy.
[1413.24 --> 1413.76]  No, no, no, no.
[1413.78 --> 1415.24]  But it was a genuine question.
[1415.24 --> 1417.40]  I love making German jokes.
[1417.52 --> 1417.74]  Anything.
[1419.18 --> 1421.06]  I should have made it a German chocolate cake.
[1421.14 --> 1421.90]  I'm so sorry, Natalie.
[1421.98 --> 1422.96]  I missed that opportunity.
[1423.14 --> 1423.86]  Oh, my gosh.
[1424.22 --> 1424.62]  Eskule.
[1425.50 --> 1426.46]  This is Austrian.
[1426.66 --> 1430.52]  Natalie will be the final, like once the beautiful cake has been constructed.
[1430.64 --> 1432.34]  She is the ultimate SMA.
[1432.40 --> 1433.72]  Wait, did you use sugar or salt?
[1433.88 --> 1435.12]  The ultimate taste tester.
[1435.12 --> 1456.70]  This episode is brought to you by our friends at Fire Hydrant.
[1457.10 --> 1459.74]  Fire Hydrant is a reliability platform for every developer.
[1460.24 --> 1462.72]  Incidents are a win, not an if situation.
[1462.72 --> 1467.24]  And they impact everyone in the organization, not just SREs.
[1467.34 --> 1470.86]  And I'm here with Robert Ross, founder and CEO of Fire Hydrant.
[1471.26 --> 1473.52]  Robert, what is it about teams getting distracted by incidents
[1473.52 --> 1476.84]  and not being able to focus on the core product that upsets you?
[1477.22 --> 1481.16]  I think that incidents bring a lot of anxiety and sometimes fear
[1481.16 --> 1485.36]  and maybe even a level of shame that can cause this paralysis
[1485.36 --> 1488.02]  in an organization from progress.
[1488.02 --> 1494.44]  And when you have the confidence to manage incidents at any scale of any variety,
[1494.76 --> 1496.72]  everyone just has this breath of fresh air
[1496.72 --> 1499.50]  that they can go build the core product even more.
[1499.86 --> 1502.88]  I don't know if anyone's had the opportunity, maybe is the word,
[1502.98 --> 1504.40]  to call the fire department.
[1504.60 --> 1507.24]  But no matter what, when the fire department shows up,
[1507.34 --> 1510.26]  it doesn't matter if the building is hugely on fire.
[1510.40 --> 1511.88]  They are calm, cool, and collected
[1511.88 --> 1513.94]  because they know exactly what they're going to do.
[1513.94 --> 1517.14]  And that's what Fire Hydrant is built to help people achieve.
[1517.14 --> 1518.52]  Very cool. Thank you, Robert.
[1518.64 --> 1522.90]  If you want to operate as a calm, cool, collected team
[1522.90 --> 1525.28]  when incidents happen, you got to check out Fire Hydrant.
[1525.60 --> 1528.22]  Small teams, up to 10 people can get started for free
[1528.22 --> 1531.20]  with all the features, no credit card required to sign up.
[1531.50 --> 1533.18]  Get started at firehydrant.com.
[1533.52 --> 1535.52]  Again, firehydrant.com.
[1535.52 --> 1548.40]  Great. So you are going to review a PR.
[1548.82 --> 1553.50]  What are the almost like unspoken rules of PR review?
[1553.50 --> 1556.60]  Are there actual rules of PR review?
[1557.18 --> 1561.22]  Love to hear like, how do you approach reviewing your colleagues' PRs?
[1561.22 --> 1565.28]  I think it goes a long way if you lead with empathy,
[1565.72 --> 1567.32]  kind of like go through the PR,
[1568.02 --> 1571.02]  address anything that you think could be updated,
[1571.24 --> 1573.76]  but not in a way that you're talking down to people,
[1574.36 --> 1578.34]  having a willingness to learn, a willingness to teach.
[1578.92 --> 1583.74]  I mean, these are all like core factors of doing a good PR review.
[1584.22 --> 1586.00]  And then you can get into the nitty gritties
[1586.00 --> 1590.82]  of like your team's specific strategy and patterns and all of that.
[1590.82 --> 1592.06]  And like the correctness of the code.
[1592.12 --> 1594.10]  But I think that first part is really key.
[1594.88 --> 1595.90]  Yeah, I totally agree.
[1596.00 --> 1600.26]  And I think there are a lot of small behaviors
[1600.26 --> 1601.82]  that we as engineers can adopt
[1601.82 --> 1604.98]  to be more empathetic in our code reviews.
[1605.22 --> 1607.50]  I really enjoy some of the resources
[1607.50 --> 1611.06]  that other people have already written and shared around this.
[1611.18 --> 1613.84]  I particularly like Alex Hill's The Art of Giving
[1613.84 --> 1617.22]  and Receiving Code Reviews Gracefully.
[1617.34 --> 1618.06]  It's something like that.
[1618.06 --> 1624.00]  And that idea of giving a code review gracefully,
[1624.08 --> 1626.08]  I think ties into the empathy thing
[1626.08 --> 1627.06]  that you're talking about, Natasha.
[1627.34 --> 1629.94]  And just like putting yourself in the position
[1629.94 --> 1631.86]  of the person who's receiving the feedback.
[1632.24 --> 1634.56]  Ultimately, a pull request,
[1634.70 --> 1637.18]  like this code review is feedback
[1637.18 --> 1641.94]  and is collaboration in like our everyday as engineers.
[1641.94 --> 1644.80]  And so some of the simple things,
[1645.26 --> 1648.32]  like instead of saying you, saying we.
[1648.56 --> 1651.64]  And instead of making a statement, asking a question.
[1652.22 --> 1653.92]  So for example, instead of saying like,
[1654.78 --> 1657.86]  oh, like you should use this other function,
[1657.96 --> 1659.52]  it already does what you're doing here.
[1660.62 --> 1664.08]  Asking, oh, like can we use this other function here?
[1664.18 --> 1665.72]  Like is there something that we can reuse?
[1665.72 --> 1670.64]  And that gives the opportunity because you could be wrong.
[1670.72 --> 1672.34]  I'm a staff engineer and I'm wrong all the time.
[1672.66 --> 1676.68]  So if I'm just coming into a code review and saying like,
[1676.74 --> 1678.60]  oh, you should have done this and you should have done that.
[1678.68 --> 1681.54]  Like that not only is not giving feedback
[1681.54 --> 1683.38]  in a way that will be easily received,
[1683.38 --> 1689.08]  but it's really like assuming that I always know the answer
[1689.08 --> 1690.52]  and I always know what's best.
[1690.52 --> 1694.50]  And I think remembering that the person who's coming in
[1694.50 --> 1698.62]  with the pull request has spent so much time,
[1698.78 --> 1701.26]  presumably on this problem that yes,
[1701.30 --> 1702.88]  the fresh pair of eyes is really helpful
[1702.88 --> 1704.98]  and you might see something that they didn't,
[1705.28 --> 1708.22]  but also giving acknowledgement to the work
[1708.22 --> 1710.30]  that they've put in on this pull request
[1710.30 --> 1713.04]  and that they might have like thought through that problem
[1713.04 --> 1715.50]  and that there might be something that you're missing
[1715.50 --> 1717.16]  because you haven't spent as much time
[1717.16 --> 1718.56]  thinking about the solution.
[1719.32 --> 1720.50]  So that empathy is really important.
[1720.52 --> 1721.20]  Yeah.
[1721.50 --> 1722.28]  Check your ego.
[1724.02 --> 1727.06]  I would totally plus a thousand they've said so far.
[1727.24 --> 1728.14]  It's definitely like for,
[1728.56 --> 1730.76]  it's not just like it's a one side street, right?
[1730.78 --> 1731.24]  It's two sides.
[1731.32 --> 1734.76]  You can take something back from the review
[1734.76 --> 1736.10]  and then they can take something forward.
[1736.46 --> 1738.48]  It's always an opportunity to learn something new,
[1738.80 --> 1742.10]  especially from people who have way more experience
[1742.10 --> 1742.60]  than you do.
[1743.14 --> 1745.46]  And it's just an opportunity to ask questions,
[1745.60 --> 1747.98]  especially like, oh, why did you do this way
[1747.98 --> 1749.62]  versus some other way, right?
[1749.62 --> 1752.72]  And it's definitely a great opportunity
[1752.72 --> 1754.86]  to kind of, you know,
[1754.86 --> 1757.52]  just learn more about what they're working on
[1757.52 --> 1758.94]  and learn more about the system.
[1759.48 --> 1760.92]  There always has to be an eye for,
[1761.16 --> 1763.08]  oh, is this like what we're trying to achieve
[1763.08 --> 1764.34]  with this particular ticket?
[1764.88 --> 1766.60]  But definitely leading with empathy
[1766.60 --> 1768.70]  is something that's great.
[1768.70 --> 1770.46]  I also want to look up that article now
[1770.46 --> 1771.56]  because I've never read that,
[1772.26 --> 1773.48]  the Alex Hill one, so.
[1774.12 --> 1774.84]  It's really great.
[1775.02 --> 1776.84]  I'll make sure I put it in the episode notes.
[1777.80 --> 1779.12]  And it is a great article.
[1780.94 --> 1782.68]  So when you're thinking about reviewing,
[1782.80 --> 1785.08]  are you predominantly reviewing for functionality
[1785.08 --> 1787.06]  and like, does this thing work?
[1787.32 --> 1789.86]  Or are you also commenting slash what are the,
[1790.04 --> 1792.64]  I guess, rules around commenting on like style?
[1793.04 --> 1794.66]  Like how the code has been written,
[1794.82 --> 1796.82]  the stylistic choices that have been made?
[1796.82 --> 1798.16]  I think a bit of both.
[1798.80 --> 1800.00]  Yeah, definitely.
[1800.44 --> 1802.84]  And not to over-reference this article,
[1803.30 --> 1805.80]  but one of the things I think is like
[1805.80 --> 1807.68]  one of my key takeaways from this was
[1807.68 --> 1811.62]  that there are those kinds of like code style things
[1811.62 --> 1813.64]  that can be automated.
[1814.30 --> 1816.08]  So having a team norm of like,
[1816.18 --> 1818.80]  oh, we're all using this linter for this code base.
[1818.82 --> 1820.10]  We're using this formatter.
[1820.66 --> 1821.76]  Pre-commit hook,
[1821.84 --> 1824.44]  those have to pass before you can make this pull request.
[1824.44 --> 1827.46]  It just automates away a lot of the things
[1827.46 --> 1829.30]  we can be kind of nitpicky over.
[1830.14 --> 1834.42]  But sometimes there are more like code patterns
[1834.42 --> 1836.46]  and those are harder to automate,
[1836.86 --> 1839.94]  but they can be like a source of contention
[1839.94 --> 1842.18]  because there can be a lot of very strong opinions
[1842.18 --> 1845.04]  around how, what patterns we're following
[1845.04 --> 1846.42]  and how code should be structured.
[1846.42 --> 1851.00]  That's where I think having a set of norms on your team
[1851.00 --> 1855.42]  that you regularly revisit when somebody new joins,
[1855.64 --> 1858.36]  when you have a new, like a new repo you're working in,
[1858.72 --> 1862.28]  those norms will help smooth that conversation
[1862.28 --> 1864.94]  because if you have all already agreed,
[1865.10 --> 1866.64]  like, oh, we're going to make sure
[1866.64 --> 1869.00]  we follow dry practices or whatever,
[1869.20 --> 1871.76]  like those kinds of agreements
[1871.76 --> 1876.60]  make it a lot easier to have that code review conversation
[1876.60 --> 1880.22]  because that's like a shared expectation that you have.
[1880.32 --> 1882.68]  And it's the same thing for giving interpersonal feedback.
[1882.80 --> 1884.88]  If you have a shared expectation and a shared goal,
[1885.10 --> 1887.30]  then you can easily use that as a reference point
[1887.30 --> 1888.10]  and be like, hey, like,
[1888.28 --> 1890.30]  since this is something that we've agreed on as a team,
[1890.48 --> 1892.04]  I'm noticing this here.
[1892.12 --> 1894.36]  Do you think we could reshape this
[1894.36 --> 1895.56]  so that it follows this practice
[1895.56 --> 1897.76]  that we have agreed to use for this repo?
[1897.76 --> 1901.62]  And that's a much easier conversation to have
[1901.62 --> 1904.48]  than like, oh, I don't like how this is styled.
[1904.60 --> 1906.24]  I think we should do it this way instead.
[1906.54 --> 1909.14]  And kind of like bringing your perspective into it.
[1909.42 --> 1911.42]  It's a lot easier to bring like a team norm
[1911.42 --> 1912.66]  that you've already all agreed on
[1912.66 --> 1914.68]  that's like the team's perspective on this
[1914.68 --> 1917.72]  and the team's perspective on how to move forward.
[1918.46 --> 1919.28]  It's really important,
[1919.34 --> 1920.82]  like having that team understanding, right?
[1920.94 --> 1922.10]  At least in my previous company,
[1922.10 --> 1924.88]  we had like shared standards as to how things,
[1924.88 --> 1926.52]  we had like pillars and everything,
[1926.52 --> 1928.30]  that we had like a standards committee
[1928.30 --> 1929.80]  that we were trying to do
[1929.80 --> 1932.14]  for like code style and stuff like that.
[1932.70 --> 1934.86]  But just like on the other side of the coin,
[1935.04 --> 1936.00]  I'm kind of like,
[1936.44 --> 1938.72]  sometimes if I see a spelling mistake,
[1938.72 --> 1940.14]  I will point that out in the PR
[1940.14 --> 1941.98]  just because it's like,
[1942.10 --> 1943.92]  if it's already committed and I see it,
[1944.08 --> 1946.30]  I wish someone had called it out in the PR
[1946.30 --> 1947.42]  and I will put in like,
[1947.88 --> 1949.20]  in my PR, I will fix it.
[1949.48 --> 1951.06]  So it's just like those little tiny things
[1951.06 --> 1955.08]  that kind of add to your personality as a reviewer.
[1955.08 --> 1956.92]  Like you might be known as that person
[1956.92 --> 1959.72]  that calls out your grammar mistakes,
[1959.72 --> 1962.54]  which I feel like I used to be
[1962.54 --> 1965.02]  and I'm not as much these days,
[1965.16 --> 1966.62]  but when I see it,
[1966.70 --> 1968.24]  I will sometimes call it out.
[1968.46 --> 1969.90]  I think I've gotten that feedback
[1969.90 --> 1971.00]  on my review from you.
[1971.36 --> 1974.68]  So my PR can attest.
[1976.76 --> 1977.50]  I'm intrigued.
[1977.62 --> 1978.98]  Do you review differently
[1978.98 --> 1982.08]  depending on the level of the person
[1982.08 --> 1983.74]  that put in the PR?
[1984.06 --> 1985.36]  I like, if you're going in
[1985.36 --> 1987.64]  and you're reviewing like a staff engineer's PR
[1987.64 --> 1990.46]  versus a associate engineer's PR,
[1990.66 --> 1991.68]  do you approach it differently?
[1992.30 --> 1994.12]  The reason I ask is that,
[1994.40 --> 1995.70]  maybe this is a leading question,
[1996.22 --> 1997.58]  say you're a staff engineer
[1997.58 --> 1998.94]  and you're reviewing the PR
[1998.94 --> 2001.16]  of someone you know is like preferably new.
[2001.54 --> 2004.14]  Would you approach that slightly differently
[2004.14 --> 2005.98]  in that you might add more comments,
[2005.98 --> 2008.56]  maybe more detail as to why you've suggested it
[2008.56 --> 2010.20]  because you know this person's still learning
[2010.20 --> 2012.88]  or agnostic of level,
[2013.08 --> 2015.10]  you approach every PR in the same way.
[2015.74 --> 2016.86]  I like to summarize,
[2017.08 --> 2018.66]  does it matter who put the PR in?
[2019.48 --> 2020.36]  I think it could help.
[2020.56 --> 2022.16]  Like if I know that someone
[2022.16 --> 2024.62]  is more new to the company
[2024.62 --> 2025.54]  or to the team,
[2025.58 --> 2028.98]  I usually kind of pepper my review comments
[2028.98 --> 2031.42]  with links or like context
[2031.42 --> 2034.24]  or even ask like if they want to kind of like
[2034.24 --> 2035.10]  jump on a call
[2035.10 --> 2036.74]  and we can talk through certain things
[2036.74 --> 2038.92]  if they have more like follow-up questions
[2038.92 --> 2040.70]  just so it's a little bit more synchronous
[2040.70 --> 2041.98]  conversation wise
[2041.98 --> 2044.08]  instead of like kind of all over the place.
[2044.52 --> 2047.36]  But I also try to leave like good feedback
[2047.36 --> 2050.02]  even if like there's a person who's above me
[2050.02 --> 2052.58]  and you know run laps on me
[2052.58 --> 2054.16]  with like the work that they do.
[2054.48 --> 2056.56]  I like to just say like this is great,
[2056.56 --> 2058.44]  I learned a lot or you know praise
[2058.44 --> 2059.64]  some of the work that they've done
[2059.64 --> 2061.32]  because I think it can be easy
[2061.32 --> 2065.26]  to just not get that type of feedback as often
[2065.26 --> 2066.42]  because you're kind of expected
[2066.42 --> 2067.96]  to do that kind of work.
[2068.58 --> 2072.40]  So being the least senior person on the team,
[2072.72 --> 2075.40]  it's difficult not to like feel intimidated
[2075.40 --> 2078.80]  by other engineers when they ask for reviews
[2078.80 --> 2079.66]  because you're like,
[2079.76 --> 2082.00]  oh, I just I'm early in my career.
[2082.10 --> 2084.20]  What do I have to offer to someone else
[2084.20 --> 2085.70]  who's been working for like 10, 15 years?
[2085.70 --> 2089.36]  But I try not to think of it as that as much anymore.
[2089.92 --> 2092.60]  Try to think of it with my current understanding of things.
[2092.86 --> 2095.10]  I try to give the best feedback I can to that person
[2095.10 --> 2097.60]  because it's always nice to have a second pair of eyes
[2097.60 --> 2099.44]  even if they're less experienced.
[2099.58 --> 2101.26]  It's always nice to have like fresh pair
[2101.26 --> 2103.10]  and then you might see something that you've missed
[2103.10 --> 2105.34]  and take it as a learning opportunity
[2105.34 --> 2106.50]  at the same time for myself.
[2106.98 --> 2107.34]  Definitely.
[2107.96 --> 2109.04]  It's a fresh pair of eyes,
[2109.16 --> 2112.02]  but also like there might be some very,
[2112.12 --> 2113.04]  very senior engineer
[2113.04 --> 2115.46]  who's been doing the same thing for many, many years
[2115.46 --> 2117.24]  and therefore has got into a habit
[2117.24 --> 2118.68]  of doing things a certain way
[2118.68 --> 2122.42]  and you fresh bunny rabbit that you are
[2122.42 --> 2125.38]  coming in with all the new technological lingo
[2125.38 --> 2127.26]  and new open source.
[2127.44 --> 2129.32]  Like you might be way more engaged
[2129.32 --> 2131.56]  and be way much more on top of the new technologies
[2131.56 --> 2132.82]  and ways of doing things.
[2132.82 --> 2134.82]  So you might be able to come in and be like,
[2134.98 --> 2136.38]  hey, have you considered this new style
[2136.38 --> 2138.12]  that you haven't done in 20 years,
[2138.12 --> 2139.30]  but maybe it'll be useful
[2139.30 --> 2141.00]  and you can teach them something.
[2141.56 --> 2141.78]  Exactly.
[2141.92 --> 2143.64]  And I usually, when I do make like,
[2143.82 --> 2144.86]  oh, you should try it this way.
[2144.92 --> 2147.26]  I usually have links to support what I'm saying
[2147.26 --> 2148.64]  just to be like,
[2148.74 --> 2151.00]  see, like these other people are doing it this way as well.
[2151.24 --> 2151.86]  It's not just me.
[2152.70 --> 2152.90]  Yeah.
[2152.94 --> 2156.06]  And I think the value of a fresh perspective
[2156.06 --> 2158.60]  also is in like challenging assumptions.
[2158.84 --> 2160.44]  So I know as a,
[2160.88 --> 2161.86]  like I'm a staff engineer,
[2161.86 --> 2163.34]  but there are definitely things that,
[2163.82 --> 2164.44]  to your point, Angelica,
[2164.54 --> 2165.54]  like I've gotten used to
[2165.54 --> 2166.96]  or I've gotten into the habit of.
[2166.96 --> 2169.92]  And sometimes that does lead me to make assumptions.
[2169.92 --> 2171.98]  And I, I work to check myself,
[2172.06 --> 2175.00]  but having teammates being able to ask questions
[2175.00 --> 2175.90]  and check assumptions,
[2175.90 --> 2179.30]  I think leads to really valuable conversation
[2179.30 --> 2182.34]  because maybe that will lead us in a different direction.
[2182.34 --> 2185.28]  Maybe I can explain more about something
[2185.28 --> 2186.96]  that I've done in my work.
[2187.32 --> 2189.62]  But I actually think when I'm approaching reviews
[2189.62 --> 2192.04]  and when I'm asking to be reviewed,
[2192.38 --> 2196.12]  I think of it more as like the subject matter expertise
[2196.12 --> 2197.24]  in a code base
[2197.24 --> 2199.96]  because I recently switched teams
[2199.96 --> 2201.84]  and I'm coming onto my new team
[2201.84 --> 2202.64]  and I have a lot,
[2203.00 --> 2205.10]  I have a lot of wealth of knowledge
[2205.10 --> 2206.12]  in terms of architecture
[2206.12 --> 2208.32]  and some of the things that I'm bringing from my past team,
[2208.50 --> 2211.40]  but I'm actually learning some of these languages
[2211.40 --> 2213.14]  for the first time.
[2213.44 --> 2217.36]  And so even though I have a big picture idea
[2217.36 --> 2218.30]  around our architecture
[2218.30 --> 2220.18]  and I'm doing a lot of things
[2220.18 --> 2221.88]  as the tech lead for my team,
[2222.12 --> 2224.14]  some of my teammates actually know these languages
[2224.14 --> 2226.04]  and the language patterns
[2226.04 --> 2229.42]  that come with these repos better than I do.
[2230.12 --> 2232.64]  And so I actively look for them
[2232.64 --> 2235.98]  to be critical of the code that I'm putting forth
[2235.98 --> 2238.00]  because that allows me to learn
[2238.00 --> 2241.82]  the same way that if they were putting in a PR in Python
[2241.82 --> 2243.40]  and I'm more expert in Python,
[2243.40 --> 2245.60]  I would want to teach them some of the things
[2245.60 --> 2247.84]  that I have picked up about Python along the way.
[2247.84 --> 2249.74]  So I think it's,
[2249.88 --> 2251.52]  I actually think this is an area
[2251.52 --> 2252.76]  where I would,
[2253.10 --> 2254.42]  I hope leveling doesn't matter.
[2254.58 --> 2256.84]  It's more about like the subject matter expertise
[2256.84 --> 2257.38]  in a repo
[2257.38 --> 2259.74]  and like helping that person
[2259.74 --> 2261.66]  level up their expertise
[2261.66 --> 2263.14]  like a little bit further
[2263.14 --> 2266.30]  and anybody can help anybody else
[2266.30 --> 2268.06]  level up their expertise more.
[2268.62 --> 2270.72]  It's interesting to hear from me all the answers.
[2270.94 --> 2273.00]  I guess you're all US-based
[2273.00 --> 2276.64]  and you all mostly work with American colleagues.
[2277.00 --> 2278.38]  Is my assumption correct?
[2278.46 --> 2281.60]  Or would you say your teams are kind of with also,
[2281.76 --> 2282.54]  or you get to work,
[2282.68 --> 2284.36]  let's say with people from other people
[2284.36 --> 2285.26]  who are not Americans?
[2285.88 --> 2289.84]  Yeah, I've worked with like non-native English speakers
[2289.84 --> 2291.38]  before on my current team.
[2291.46 --> 2293.42]  I'm working with mostly native English,
[2293.50 --> 2295.22]  all the engineers are native English speakers,
[2295.22 --> 2296.98]  but one of my teammates even
[2296.98 --> 2300.16]  was recently working with some of our engineering teams
[2300.16 --> 2302.70]  that are working out of other countries as well.
[2303.14 --> 2305.36]  So we have some international work.
[2306.16 --> 2307.38]  Would you say your experience
[2307.38 --> 2310.00]  of feeling comfortable to correct
[2310.00 --> 2311.00]  and to be corrected
[2311.00 --> 2313.08]  is the same as with people
[2313.08 --> 2314.38]  from the same background as you?
[2314.80 --> 2317.44]  Or is it different in any way
[2317.44 --> 2319.64]  when you like review the code
[2319.64 --> 2320.92]  or get reviewed by people
[2320.92 --> 2322.84]  who are wherever they're based,
[2322.92 --> 2324.80]  like just grew up in other places?
[2325.56 --> 2326.72]  Yeah, that's a really great question.
[2327.42 --> 2328.62]  I definitely think that
[2328.62 --> 2331.66]  I have an easier time giving grace
[2331.66 --> 2333.10]  to somebody who's giving me a review
[2333.10 --> 2334.84]  if English isn't their first language
[2334.84 --> 2339.24]  because tone is a hard thing to pick up.
[2339.76 --> 2341.68]  So both I've worked with
[2341.68 --> 2344.08]  whether like English is not their first language
[2344.08 --> 2348.22]  or whether somebody has issues with tone
[2348.22 --> 2349.18]  for some other reason,
[2349.36 --> 2351.86]  like some kind of like mental like illness
[2351.86 --> 2354.70]  or disability is probably the better term
[2354.70 --> 2357.18]  for thinking through
[2357.18 --> 2358.94]  like how something is going to be perceived.
[2359.06 --> 2360.08]  I've worked with colleagues
[2360.08 --> 2361.88]  who are like on the spectrum
[2361.88 --> 2363.24]  and that's not always like something
[2363.24 --> 2365.92]  that they have an easy time interpreting
[2365.92 --> 2368.34]  and figuring out how tone is going to come across.
[2368.84 --> 2370.10]  So in those situations,
[2370.10 --> 2370.74]  I have a lot,
[2371.54 --> 2373.14]  it's easier for me to give empathy
[2373.14 --> 2374.06]  to that person
[2374.06 --> 2375.06]  when they're giving me a review,
[2375.18 --> 2375.46]  being like,
[2375.56 --> 2377.02]  oh, they didn't mean that to hurt my feelings.
[2377.02 --> 2378.24]  They're just giving me feedback.
[2379.24 --> 2381.74]  But sometimes because we are a big company,
[2382.38 --> 2383.38]  like sometimes you're getting a review
[2383.38 --> 2384.80]  from somebody you don't know.
[2384.94 --> 2386.80]  And so you don't always know if that's the case.
[2387.16 --> 2388.58]  So I think it's easier
[2388.58 --> 2389.76]  when you're working with somebody you know.
[2390.38 --> 2391.96]  If English isn't their first language,
[2392.16 --> 2393.60]  I always have an easier time being like,
[2393.66 --> 2394.58]  oh, they didn't mean it.
[2394.64 --> 2395.94]  Like in a way that hurts my feelings.
[2397.62 --> 2398.88]  Sometimes that's harder for me
[2398.88 --> 2400.34]  to like get to that point
[2400.34 --> 2402.64]  if it's somebody who isn't
[2402.64 --> 2403.86]  like a native English speaker.
[2403.86 --> 2405.80]  And it's one of those things
[2405.80 --> 2408.12]  I think is easy to make assumptions around,
[2408.12 --> 2408.94]  which is why I brought up
[2408.94 --> 2410.56]  like working with somebody
[2410.56 --> 2411.90]  who is like neurodivergent.
[2412.06 --> 2412.54]  It's just like,
[2413.22 --> 2414.04]  that's not always something
[2414.04 --> 2415.36]  you can tell right away.
[2415.50 --> 2416.88]  And so it's easier to tell
[2416.88 --> 2418.98]  when English isn't somebody's first language.
[2419.42 --> 2421.64]  But I try to like take that empathy
[2421.64 --> 2423.08]  that I learned working with those colleagues
[2423.08 --> 2424.92]  and bring it to all my other colleagues as well.
[2425.32 --> 2426.94]  It's also interesting to think of that.
[2427.22 --> 2429.48]  I mean, yes, English is not native language.
[2429.48 --> 2431.32]  That's like a very good differentiator.
[2431.70 --> 2433.44]  And also different cultures
[2433.44 --> 2436.68]  have different relationship with feedback
[2436.68 --> 2438.02]  or even saying somebody,
[2438.22 --> 2438.96]  you did something wrong.
[2440.34 --> 2441.90]  Yeah, that's a good point.
[2442.38 --> 2444.32]  Being the only person who is not in the US,
[2444.72 --> 2446.06]  I would actually love to hear
[2446.06 --> 2447.86]  like your perception on this.
[2447.94 --> 2448.64]  I know you keep on saying
[2448.64 --> 2449.76]  we need to hear from the guests.
[2449.82 --> 2451.44]  And I agree, these wonderful guests.
[2451.92 --> 2453.38]  But I would love to hear your experience.
[2453.48 --> 2454.56]  I mean, I got culture shock
[2454.56 --> 2455.52]  moving to the US,
[2455.54 --> 2457.36]  but I wasn't reviewing PRs in London.
[2457.36 --> 2458.50]  And you are a native speaker.
[2458.98 --> 2460.12]  Yes, and I am a native speaker.
[2460.36 --> 2461.66]  So I have those two things
[2461.66 --> 2463.90]  which make it slightly easier coming in.
[2463.90 --> 2466.18]  But I would love to hear your perception
[2466.18 --> 2467.06]  and kind of what you've heard
[2467.06 --> 2468.04]  from colleagues, friends,
[2468.54 --> 2469.32]  and your experience.
[2469.86 --> 2471.78]  Almost all the teams that I worked in
[2471.78 --> 2472.88]  are quite mixed
[2472.88 --> 2474.48]  because Europe is a lot easier
[2474.48 --> 2476.86]  for work relocations.
[2477.68 --> 2478.90]  The green card and so on
[2478.90 --> 2480.10]  exists in the US,
[2480.22 --> 2481.54]  but it's quite harder
[2481.54 --> 2483.32]  than just the work visa in Germany
[2483.32 --> 2484.52]  or other European countries.
[2484.70 --> 2486.36]  So I don't remember the last time
[2486.36 --> 2488.18]  I worked in a team
[2488.18 --> 2489.66]  where everybody comes from the same country.
[2489.86 --> 2491.84]  Or we had like more than 10%
[2491.84 --> 2493.06]  native English speakers.
[2493.06 --> 2495.16]  Although English is always the main language
[2495.16 --> 2497.24]  because you need to have something
[2497.24 --> 2498.58]  that is not the programming language.
[2499.32 --> 2500.58]  And I think in the beginning,
[2500.82 --> 2503.06]  I used to have some kind of misunderstandings
[2503.06 --> 2505.68]  exactly because what was said,
[2506.08 --> 2508.96]  like understanding empathy,
[2509.16 --> 2510.70]  understanding they did not mean that,
[2510.80 --> 2511.60]  they meant this,
[2512.06 --> 2514.12]  coming across myself
[2514.12 --> 2515.82]  sometimes as a bit more,
[2516.32 --> 2517.92]  why don't you say that in a nicer way?
[2518.04 --> 2518.54]  And so on.
[2518.54 --> 2522.36]  And so definitely there is all sorts of bounds
[2522.36 --> 2523.16]  there to strike.
[2523.32 --> 2526.04]  And it's very interesting to hear
[2526.04 --> 2527.90]  how people cope with that.
[2527.96 --> 2529.76]  And it's also obviously written
[2529.76 --> 2533.10]  is even less easy to understand,
[2533.26 --> 2534.32]  like written communication
[2534.32 --> 2535.46]  in comparison to speaking,
[2535.94 --> 2536.92]  to spoken communication.
[2537.10 --> 2537.86]  And even in spoken,
[2537.98 --> 2540.00]  you can easily get lost and so on.
[2540.58 --> 2542.72]  And intonations mean different things.
[2542.72 --> 2545.08]  It's the thing about cultures that say
[2545.08 --> 2547.92]  that sometimes it's kind of impolite
[2547.92 --> 2548.64]  either to correct
[2548.64 --> 2550.30]  or even to just say no to someone.
[2550.80 --> 2553.84]  So I had to learn and actively practice
[2553.84 --> 2556.26]  that when I propose some idea,
[2556.36 --> 2557.90]  I have to start with something like,
[2558.10 --> 2559.94]  feel free to reject that
[2559.94 --> 2562.24]  or there might be better alternatives,
[2562.44 --> 2562.64]  but,
[2563.20 --> 2565.16]  and sometimes it's still,
[2565.38 --> 2566.30]  depending on the context,
[2566.30 --> 2568.26]  it sounds sort of foreign,
[2568.26 --> 2569.30]  but I think it's fine
[2569.30 --> 2570.74]  that it sounds foreign
[2570.74 --> 2572.74]  because it's kind of like a standard
[2572.74 --> 2575.06]  across all the different cultures
[2575.06 --> 2576.20]  you'll get to work with
[2576.20 --> 2577.62]  that this is a,
[2578.12 --> 2581.16]  be nicer over being not nice enough.
[2581.68 --> 2582.28]  Yeah, definitely.
[2582.74 --> 2584.58]  My comment is going to be very like,
[2585.12 --> 2586.20]  less, slightly less serious,
[2586.32 --> 2587.00]  but it came to mind
[2587.00 --> 2587.90]  and it sounded like something
[2587.90 --> 2588.76]  that I would love to do.
[2589.30 --> 2592.50]  Can you like attach voice notes to PRs?
[2592.50 --> 2594.42]  You have looms in Git pull requests.
[2594.90 --> 2595.22]  Yeah,
[2595.22 --> 2597.08]  because I feel like I would love it
[2597.08 --> 2598.74]  if someone made like a suggestion
[2598.74 --> 2601.36]  and then I could like have a little voice note
[2601.36 --> 2602.06]  where they could say,
[2602.14 --> 2602.68]  this is why,
[2602.80 --> 2604.00]  because then you hear the tone
[2604.00 --> 2606.42]  and you hear them explaining it
[2606.42 --> 2609.50]  and then you could do like a verbal readout
[2609.50 --> 2610.74]  of your very long PR.
[2611.42 --> 2612.44]  That might be cool.
[2614.06 --> 2615.86]  Do emojis help with that?
[2616.16 --> 2617.58]  Like I find it really difficult
[2617.58 --> 2620.80]  to communicate through my words
[2620.80 --> 2622.38]  without emojis.
[2622.50 --> 2624.84]  Like I use emojis to help me
[2624.84 --> 2626.44]  more accurately portray
[2626.44 --> 2629.20]  the intention behind my comments.
[2629.36 --> 2630.66]  I, when I say something like,
[2631.04 --> 2632.54]  oh, I'm not sure about this.
[2632.64 --> 2634.12]  I'll do like a thinky emoji
[2634.12 --> 2636.40]  and like a funny like tongue emoji
[2636.40 --> 2637.56]  to show that it's like,
[2637.94 --> 2639.34]  not like a, what is this?
[2639.88 --> 2641.98]  Because I feel like words are not enough,
[2642.04 --> 2642.78]  which is why,
[2642.92 --> 2644.52]  and those of you who interact with me regularly,
[2645.10 --> 2645.76]  I think you'll be,
[2645.88 --> 2647.90]  it'll be very hard for you to find any space
[2647.90 --> 2650.18]  where I haven't put an emoji after my message
[2650.18 --> 2652.38]  or some kind of imagery,
[2652.38 --> 2653.80]  whether it be a meme or a GIF
[2653.80 --> 2657.50]  to try and kind of level up my communication
[2657.50 --> 2658.58]  from just being words
[2658.58 --> 2660.90]  to having that extra layer of like emotion.
[2661.40 --> 2666.46]  Is it appropriate to add many emojis to your PR?
[2666.58 --> 2668.74]  I know that you can like add the emoji reactions,
[2668.98 --> 2669.64]  but within it,
[2669.92 --> 2672.42]  is that a useful tool that in fact could be used
[2672.42 --> 2674.64]  to try and alleviate that risk
[2674.64 --> 2677.20]  of being misconstrued via just written word?
[2677.20 --> 2679.52]  So you mean the pull request description
[2679.52 --> 2680.70]  or actually each commit?
[2682.32 --> 2684.42]  I mean, open to views on either.
[2685.00 --> 2686.72]  Yeah, I recommend using emojis
[2686.72 --> 2690.34]  and like setting up norms around emoji use
[2690.34 --> 2692.06]  and like code review norms.
[2692.34 --> 2693.58]  It's like one of the suggestions
[2693.58 --> 2696.12]  that some of the other staff engineers
[2696.12 --> 2700.06]  and I put together in the norms template
[2700.06 --> 2702.54]  that we shared out with internally at the times.
[2702.54 --> 2706.24]  And I think it's the way that we use emojis
[2706.24 --> 2709.02]  in that template is around communicating
[2709.02 --> 2711.16]  the intention behind a review comment.
[2711.96 --> 2715.40]  So one of the things that is really hard to tell
[2715.40 --> 2718.78]  based on just the written word in terms of tone
[2718.78 --> 2721.28]  is like whether that piece of feedback
[2721.28 --> 2722.62]  is blocking or not.
[2723.28 --> 2726.26]  So is this just a stylistic thing
[2726.26 --> 2729.48]  that you think will help me level up my skills?
[2729.48 --> 2732.50]  Is this something that I actually need to do
[2732.50 --> 2734.42]  before merging in this code?
[2735.16 --> 2737.78]  That kind of communication can sometimes be hard
[2737.78 --> 2742.20]  and especially I think within different levels.
[2742.34 --> 2743.78]  Like I know when I was more entry level
[2743.78 --> 2746.20]  I had a hard time just like coming out
[2746.20 --> 2746.76]  and asking like,
[2746.86 --> 2747.98]  do I actually have to do that though?
[2749.00 --> 2752.28]  So we use emojis as a way
[2752.28 --> 2754.26]  of kind of categorizing the comment.
[2754.64 --> 2756.14]  So if it is blocking,
[2756.68 --> 2758.16]  you can communicate that being like,
[2758.16 --> 2760.90]  oh, like this will cause implications in this way.
[2761.46 --> 2762.06]  And you kind of,
[2762.34 --> 2764.10]  it's a good prompt for the reviewer
[2764.10 --> 2765.46]  to think about why it's blocking
[2765.46 --> 2766.84]  and communicate that.
[2767.22 --> 2770.12]  But it's also ways of sharing
[2770.12 --> 2771.52]  like stylistic feedback
[2771.52 --> 2772.72]  in a way that's not blocking
[2772.72 --> 2773.18]  and say like,
[2773.26 --> 2775.78]  oh, like I see that you did it this way.
[2775.86 --> 2777.34]  Like typically when I approach this problem,
[2777.38 --> 2779.04]  I do it this other way.
[2779.70 --> 2782.20]  Just different styles, sharing my style.
[2783.04 --> 2784.20]  So I think it helps
[2784.20 --> 2785.98]  to kind of categorize the intention
[2785.98 --> 2786.98]  to your point Angelica
[2786.98 --> 2789.94]  around what the comment
[2789.94 --> 2791.88]  is supposed to be communicating.
[2792.06 --> 2794.00]  It like adds a little bit of color,
[2794.10 --> 2796.48]  I think to just the plain text otherwise.
[2797.24 --> 2798.56]  But curious if others
[2798.56 --> 2799.66]  have different opinions on it.
[2799.76 --> 2801.16]  Maybe you find them annoying.
[2802.34 --> 2803.74]  Follow up to that.
[2803.92 --> 2806.30]  So I'm 100% pro emoji
[2806.30 --> 2808.94]  as people on my team can attest to.
[2809.06 --> 2811.26]  I am always using emojis in Slack
[2811.26 --> 2813.02]  sometimes in GitHub.
[2813.02 --> 2815.42]  But I guess for that,
[2815.96 --> 2817.34]  if it's kind of meant to convey
[2817.34 --> 2818.60]  blocking versus not blocking
[2818.60 --> 2819.96]  as your example,
[2820.76 --> 2822.08]  is that like a way to kind of
[2822.08 --> 2824.70]  not have to use the actual
[2824.70 --> 2825.92]  like supported GitHub feature
[2825.92 --> 2827.96]  where it's like you want,
[2828.04 --> 2829.02]  you're requesting changes
[2829.02 --> 2831.44]  and kind of blocking the merge
[2831.44 --> 2832.76]  like full stop?
[2832.88 --> 2833.90]  Because I don't know
[2833.90 --> 2834.92]  how people perceive that,
[2834.96 --> 2835.94]  but maybe it could come off
[2835.94 --> 2836.54]  a little harsh,
[2836.78 --> 2838.70]  like actually using that feature
[2838.70 --> 2839.76]  and maybe like emojis
[2839.76 --> 2841.56]  isn't a nicer way to say that.
[2841.64 --> 2843.50]  But like if it's really blocking,
[2843.84 --> 2844.98]  shouldn't we just be using
[2844.98 --> 2846.34]  that specific feature
[2846.34 --> 2847.32]  to prevent it
[2847.32 --> 2848.18]  from actually going through?
[2848.48 --> 2849.92]  I think in that scenario,
[2849.92 --> 2852.22]  like you still do request changes
[2852.22 --> 2854.16]  and kind of formally block
[2854.16 --> 2854.98]  the pull request.
[2855.20 --> 2856.72]  But I know as a reviewer,
[2856.78 --> 2858.36]  if I get like changes requested
[2858.36 --> 2858.98]  on my PR
[2858.98 --> 2861.08]  and I go in and there are like 20 comments,
[2861.34 --> 2863.86]  it's hard for me to maybe initially
[2863.86 --> 2865.34]  like sift through those comments
[2865.34 --> 2866.40]  to figure out which ones
[2866.40 --> 2867.66]  are the ones that are causing
[2867.66 --> 2869.20]  the PR to be blocked.
[2869.54 --> 2870.74]  So it helps like streamline
[2870.74 --> 2872.08]  the communication in that way
[2872.08 --> 2873.90]  where if I'm blocking
[2873.90 --> 2875.36]  Angelica's pull request
[2875.36 --> 2877.28]  and I leave a bunch of comments
[2877.28 --> 2878.16]  and some of them are like,
[2878.34 --> 2879.16]  great job, you,
[2879.32 --> 2880.12]  this is really cool.
[2880.28 --> 2881.86]  And some of them are style
[2881.86 --> 2884.14]  and some of them are actually questions
[2884.14 --> 2886.50]  and then some of them are actual blocking
[2886.50 --> 2887.80]  like requests for changes.
[2887.80 --> 2890.38]  It helps kind of narrow to those
[2890.38 --> 2891.98]  and like create more of,
[2892.14 --> 2894.92]  I think like a clear checklist
[2894.92 --> 2896.14]  in a way of like what,
[2896.40 --> 2897.74]  you're expecting to be changed
[2897.74 --> 2899.10]  before being asked
[2899.10 --> 2900.12]  to re-review the code.
[2900.50 --> 2901.58]  So I just think it's helpful
[2901.58 --> 2903.46]  even if you are formally
[2903.46 --> 2904.90]  like blocking the pull request
[2904.90 --> 2908.38]  to communicate like what things
[2908.38 --> 2909.34]  you expect to be changed
[2909.34 --> 2911.76]  before you think that it could be merged.
[2912.42 --> 2912.52]  Gotcha.
[2912.62 --> 2913.68]  I don't know if I was just projecting
[2913.68 --> 2914.54]  my own fear,
[2914.64 --> 2915.28]  like seeing the,
[2915.38 --> 2916.78]  like the email where it says
[2916.78 --> 2917.86]  this has been like,
[2918.06 --> 2918.98]  changes have been requested
[2918.98 --> 2920.10]  and oh no,
[2920.16 --> 2921.10]  what did I do wrong?
[2921.42 --> 2922.40]  I need to do that.
[2922.98 --> 2923.54]  Don't worry.
[2923.60 --> 2924.68]  We all do stuff wrong
[2924.68 --> 2925.94]  in our pull requests all the time.
[2926.40 --> 2927.60]  That's part of being an engineer.
[2927.60 --> 2956.08]  This episode is brought to you by Honeycomb.
[2956.08 --> 2957.48]  Don't find your most perplexing
[2957.48 --> 2958.56]  application issues.
[2958.86 --> 2961.68]  Honeycomb is a fast analysis tool
[2961.68 --> 2962.58]  that reveals the truth
[2962.58 --> 2963.88]  about every aspect
[2963.88 --> 2965.78]  of your application in production.
[2966.20 --> 2967.26]  Find out how users experience
[2967.26 --> 2968.54]  your code in complex
[2968.54 --> 2970.24]  and unpredictable environments.
[2970.50 --> 2971.28]  Find patterns
[2971.28 --> 2972.28]  and outliers
[2972.28 --> 2973.90]  across billions of rows of data
[2973.90 --> 2975.50]  and definitively solve your problems.
[2975.86 --> 2976.62]  And we use Honeycomb
[2976.62 --> 2977.36]  here at Change.
[2977.40 --> 2977.48]  Well,
[2977.48 --> 2978.02]  that's why we welcome
[2978.02 --> 2979.42]  the opportunity to add them
[2979.42 --> 2981.22]  as one of our infrastructure partners.
[2981.22 --> 2982.22]  In particular,
[2982.22 --> 2983.12]  we use Honeycomb
[2983.12 --> 2984.86]  to track down CDN issues recently,
[2984.86 --> 2986.60]  which we talked about at length
[2986.60 --> 2987.84]  on the Kaizen edition
[2987.84 --> 2989.06]  of the Ship It podcast.
[2989.32 --> 2989.98]  So check that out.
[2990.24 --> 2990.72]  Here's the thing.
[2990.96 --> 2992.18]  Teams who don't use Honeycomb
[2992.18 --> 2993.32]  are forced to find
[2993.32 --> 2994.20]  the needle in the haystack.
[2994.32 --> 2995.34]  They scroll through
[2995.34 --> 2996.44]  endless dashboards
[2996.44 --> 2997.48]  playing whack-a-mole.
[2997.70 --> 2998.88]  They deal with alert floods,
[2999.10 --> 2999.70]  trying to guess
[2999.70 --> 3000.74]  which one matters.
[3001.12 --> 3002.06]  And they go from tool
[3002.06 --> 3002.92]  to tool to tool
[3002.92 --> 3003.74]  playing sleuth,
[3004.00 --> 3004.60]  trying to figure out
[3004.60 --> 3005.72]  how all the puzzle pieces
[3005.72 --> 3006.34]  fit together.
[3006.68 --> 3007.94]  It's this context switching
[3007.94 --> 3009.04]  and tool sprawl
[3009.04 --> 3009.94]  that are slowly killing
[3009.94 --> 3011.00]  teams effectiveness
[3011.00 --> 3012.36]  and ultimately hindering
[3012.36 --> 3013.00]  their business.
[3013.40 --> 3013.90]  With Honeycomb,
[3014.00 --> 3014.98]  you get a fast,
[3015.30 --> 3015.84]  unified,
[3016.12 --> 3017.62]  and clear understanding
[3017.62 --> 3019.02]  of the one thing
[3019.02 --> 3020.16]  driving your business.
[3020.42 --> 3020.84]  Production.
[3021.36 --> 3021.94]  With Honeycomb,
[3022.04 --> 3022.90]  you guess less
[3022.90 --> 3023.84]  and you know more.
[3024.22 --> 3024.90]  Join the swarm
[3024.90 --> 3026.70]  and try Honeycomb free today
[3026.70 --> 3028.30]  at honeycomb.io
[3028.30 --> 3029.44]  slash changelog.
[3029.74 --> 3030.14]  Again,
[3030.28 --> 3031.38]  honeycomb.io
[3031.38 --> 3033.06]  slash changelog.
[3033.28 --> 3034.26]  And by our friends
[3034.26 --> 3034.98]  at Chronosphere,
[3035.46 --> 3036.18]  scaling cloud native
[3036.18 --> 3037.08]  is complicated
[3037.08 --> 3038.42]  and Chronosphere helps teams
[3038.42 --> 3039.20]  take back control
[3039.20 --> 3040.36]  of observability,
[3040.76 --> 3041.74]  tame rampant data growth,
[3042.04 --> 3043.18]  reduce cloud native complexity,
[3043.64 --> 3044.48]  and increase confidence
[3044.48 --> 3045.36]  of the business.
[3045.82 --> 3046.68]  And I'm here with Mark Mow,
[3046.76 --> 3047.86]  co-founder and CEO
[3047.86 --> 3048.38]  of Chronosphere.
[3048.86 --> 3049.38]  Mark, when it comes
[3049.38 --> 3050.62]  to cloud native observability,
[3051.02 --> 3052.10]  what are the pain points
[3052.10 --> 3052.76]  of Kubernetes
[3052.76 --> 3053.96]  and making sure
[3053.96 --> 3054.68]  it's reliable?
[3055.20 --> 3055.34]  You know,
[3055.36 --> 3056.02]  I think the shift
[3056.02 --> 3056.52]  to Kubernetes
[3056.52 --> 3057.78]  has really changed
[3057.78 --> 3059.94]  the way we design applications.
[3060.26 --> 3061.80]  It's changed the way we,
[3062.04 --> 3063.26]  it's changed our infrastructure
[3063.26 --> 3063.74]  as well.
[3063.78 --> 3064.22]  So it's introduced
[3064.22 --> 3065.02]  a lot of change,
[3065.08 --> 3065.48]  I would say,
[3065.54 --> 3066.10]  and that's probably
[3066.10 --> 3067.02]  why it's causing
[3067.02 --> 3068.28]  a lot of issues
[3068.28 --> 3069.64]  in the observability space.
[3069.96 --> 3070.56]  I think one thing
[3070.56 --> 3071.10]  we're finding
[3071.10 --> 3073.46]  is that a lot of companies
[3073.46 --> 3073.90]  out there
[3073.90 --> 3074.98]  are focused on
[3074.98 --> 3076.70]  producing a lot more data
[3076.70 --> 3077.52]  and there's a lot of focus
[3077.52 --> 3078.78]  on more metrics,
[3078.94 --> 3079.48]  more traces,
[3079.64 --> 3080.28]  more logs,
[3080.40 --> 3081.52]  because these environments
[3081.52 --> 3082.70]  we're trying to monitor
[3082.70 --> 3083.80]  are far more complex
[3083.80 --> 3084.44]  these days.
[3084.56 --> 3085.38]  I think that's maybe
[3085.38 --> 3086.24]  one of the mistakes
[3086.24 --> 3087.58]  the industry is running into
[3087.58 --> 3088.42]  and it's interesting
[3088.42 --> 3089.54]  because obviously
[3089.54 --> 3090.68]  for all the solutions
[3090.68 --> 3091.00]  out there,
[3091.02 --> 3091.80]  the vendors out there,
[3091.90 --> 3092.74]  the more data
[3092.74 --> 3093.48]  that gets produced,
[3093.56 --> 3094.36]  the better it is
[3094.36 --> 3095.38]  for all the vendors
[3095.38 --> 3095.88]  out there.
[3095.88 --> 3097.26]  But what's interesting
[3097.26 --> 3098.28]  is that along with
[3098.28 --> 3099.64]  that increased volume
[3099.64 --> 3100.10]  of data,
[3100.30 --> 3101.02]  people aren't actually
[3101.02 --> 3102.50]  getting better outcomes
[3102.50 --> 3103.08]  out of it.
[3103.40 --> 3104.50]  People's number
[3104.50 --> 3104.98]  of incidents
[3104.98 --> 3105.70]  that people are running
[3105.70 --> 3106.76]  to are still rising,
[3107.28 --> 3108.30]  people's MTTRs,
[3108.36 --> 3109.12]  MTTDs,
[3109.18 --> 3110.26]  meantime to detection
[3110.26 --> 3111.00]  and resolutions
[3111.00 --> 3112.04]  actually getting higher
[3112.04 --> 3113.08]  as opposed to lower.
[3113.24 --> 3114.06]  So I think this is
[3114.06 --> 3114.82]  the common state
[3114.82 --> 3115.88]  that a lot of companies
[3115.88 --> 3116.76]  find themselves in
[3116.76 --> 3117.42]  and of course
[3117.42 --> 3118.06]  with the increased
[3118.06 --> 3119.20]  volume of data,
[3119.52 --> 3120.68]  folks' bills increase
[3120.68 --> 3121.36]  and the problem
[3121.36 --> 3122.28]  actually gets harder.
[3122.48 --> 3122.72]  So I think
[3122.72 --> 3123.96]  that's a common state
[3123.96 --> 3124.62]  we find a lot
[3124.62 --> 3125.26]  of companies into
[3125.26 --> 3125.84]  and this is probably
[3125.84 --> 3126.88]  why it's top of mind
[3126.88 --> 3127.58]  for a lot of companies
[3127.58 --> 3128.00]  out there.
[3128.44 --> 3128.74]  Very cool.
[3128.82 --> 3129.34]  Thank you, Martin.
[3129.46 --> 3129.72]  All right,
[3129.74 --> 3130.32]  the next step
[3130.32 --> 3131.12]  is to head to
[3131.12 --> 3132.10]  chronosphere.io
[3132.10 --> 3133.28]  to explore the platform
[3133.28 --> 3134.32]  and get a demo.
[3134.54 --> 3134.88]  Again,
[3135.00 --> 3136.10]  chronosphere.io.
[3136.10 --> 3164.30]  So I just have
[3164.30 --> 3165.28]  one more question.
[3165.28 --> 3166.82]  because we are running
[3166.82 --> 3168.04]  out of time regrettably
[3168.04 --> 3170.60]  but my question is
[3170.60 --> 3172.42]  like can you teach people
[3172.42 --> 3174.72]  how to do a good PR,
[3174.94 --> 3176.34]  how to review PRs?
[3176.88 --> 3178.40]  Like is there truly an art
[3178.40 --> 3180.36]  to reviewing a PR
[3180.36 --> 3181.54]  or is it really just us
[3181.54 --> 3183.08]  all like bumbling through,
[3183.72 --> 3184.88]  learning as we go,
[3185.28 --> 3186.92]  trying to do the best we can
[3186.92 --> 3188.62]  and really you're never
[3188.62 --> 3190.48]  the kind of PR pro.
[3190.82 --> 3191.70]  You're always going to have
[3191.70 --> 3192.42]  more to learn about
[3192.42 --> 3194.34]  how to create a PR better,
[3194.48 --> 3195.46]  review a PR better.
[3195.86 --> 3196.38]  Like are you ever
[3196.38 --> 3196.88]  going to be like,
[3196.96 --> 3197.54]  right, I'm done.
[3197.66 --> 3198.76]  I am the PR pro.
[3199.38 --> 3199.74]  Amazing.
[3199.74 --> 3202.82]  I think there is an art to it.
[3203.00 --> 3203.96]  You're kind of balancing
[3203.96 --> 3205.52]  the empathy
[3205.52 --> 3207.62]  of giving this person feedback
[3207.62 --> 3209.24]  and acknowledging
[3209.24 --> 3209.90]  how much work
[3209.90 --> 3211.00]  they've put into it
[3211.00 --> 3211.92]  but at the same time
[3211.92 --> 3212.50]  you have to,
[3212.74 --> 3212.90]  you know,
[3212.94 --> 3213.50]  you kind of,
[3213.94 --> 3214.50]  if you're like,
[3215.12 --> 3216.30]  if this is like a critical service,
[3216.42 --> 3217.42]  you're going to be the one
[3217.42 --> 3217.80]  that's,
[3218.28 --> 3219.04]  that might be paged
[3219.04 --> 3219.94]  during the middle of the night
[3219.94 --> 3221.06]  if something goes wrong
[3221.06 --> 3221.88]  and all you see that,
[3222.10 --> 3222.52]  this commit
[3222.52 --> 3224.66]  is what's causing the issue.
[3225.18 --> 3226.20]  But also you,
[3226.26 --> 3227.86]  you kind of have to balance
[3227.86 --> 3229.60]  that with the time,
[3229.72 --> 3229.90]  you know,
[3229.94 --> 3231.56]  you still have to get things done.
[3232.00 --> 3233.20]  It's a big balancing act
[3233.20 --> 3234.12]  of how much,
[3234.46 --> 3234.68]  like,
[3235.12 --> 3235.98]  is something like,
[3236.16 --> 3236.86]  is this critical
[3236.86 --> 3238.20]  that this needs to get changed
[3238.20 --> 3238.86]  even though it's like
[3238.86 --> 3239.82]  a stylistic thing
[3239.82 --> 3241.02]  that goes against
[3241.02 --> 3242.70]  like our team norms
[3242.70 --> 3244.32]  but it's imperative
[3244.32 --> 3245.70]  that this gets through
[3245.70 --> 3247.34]  or maybe they've already
[3247.34 --> 3248.34]  spent a lot of time on it.
[3248.66 --> 3249.68]  So it's definitely like
[3249.68 --> 3251.80]  the art of like juggling
[3251.80 --> 3252.94]  or balancing,
[3253.16 --> 3253.30]  so.
[3253.90 --> 3255.22]  I think just experience
[3255.22 --> 3256.32]  goes a long way.
[3256.62 --> 3257.60]  Like learn by doing.
[3257.84 --> 3258.66]  You can kind of
[3258.66 --> 3260.32]  experience a lot of things
[3260.32 --> 3261.12]  that you want to emulate
[3261.12 --> 3262.64]  or things that you're like,
[3262.70 --> 3262.82]  wow,
[3262.88 --> 3263.46]  that didn't make,
[3263.84 --> 3264.54]  leave me feeling
[3264.54 --> 3265.76]  really good about myself
[3265.76 --> 3267.36]  so I know not to do this
[3267.36 --> 3268.02]  in the future.
[3268.28 --> 3269.56]  But also like
[3269.56 --> 3271.46]  just getting more experienced
[3271.46 --> 3273.34]  in whatever language
[3273.34 --> 3274.54]  that you're working on
[3274.54 --> 3276.36]  to then make those
[3276.36 --> 3277.34]  suggestions
[3277.34 --> 3278.98]  that can make the code
[3278.98 --> 3279.58]  better
[3279.58 --> 3281.08]  and more performant.
[3281.18 --> 3282.18]  That's like another layer
[3282.18 --> 3283.88]  of doing a PR review
[3283.88 --> 3285.30]  but still something
[3285.30 --> 3286.58]  that comes with more time.
[3287.12 --> 3287.22]  Yeah,
[3287.30 --> 3287.76]  and I think
[3287.76 --> 3288.60]  from the perspective
[3288.60 --> 3289.96]  like authoring a PR
[3289.96 --> 3291.08]  and asking for a review
[3291.08 --> 3291.78]  that's also
[3291.78 --> 3293.46]  something that
[3293.46 --> 3294.52]  is like a skill
[3294.52 --> 3295.90]  that can be honed
[3295.90 --> 3296.38]  and taught
[3296.38 --> 3297.62]  and improved
[3297.62 --> 3298.50]  at any level
[3298.50 --> 3299.06]  because
[3299.06 --> 3300.58]  figuring out like
[3300.58 --> 3302.12]  when a PR is done,
[3302.26 --> 3303.26]  how big it is,
[3303.62 --> 3305.20]  but also in some situations
[3305.20 --> 3306.96]  maybe you're introducing
[3306.96 --> 3307.94]  a change
[3307.94 --> 3309.80]  and maybe you have
[3309.80 --> 3310.44]  to like write up
[3310.44 --> 3311.10]  like why
[3311.10 --> 3312.48]  you think that change
[3312.48 --> 3313.18]  is the right path
[3313.18 --> 3313.80]  to move forward
[3313.80 --> 3314.56]  and there's always
[3314.56 --> 3316.16]  room to improve on
[3316.16 --> 3317.10]  like making
[3317.10 --> 3318.86]  a concise argument.
[3318.86 --> 3319.86]  I think that's
[3319.86 --> 3320.84]  something that
[3320.84 --> 3321.98]  we can always improve on
[3321.98 --> 3322.52]  is how to make
[3322.52 --> 3323.16]  a concise,
[3323.32 --> 3323.80]  clear argument
[3323.80 --> 3324.78]  for the change
[3324.78 --> 3326.12]  that you're introducing
[3326.12 --> 3327.62]  or how to best
[3327.62 --> 3328.12]  like walk
[3328.12 --> 3329.00]  your reviewer
[3329.00 --> 3330.40]  through the pull request
[3330.40 --> 3332.04]  and just based
[3332.04 --> 3333.84]  on your PR ask.
[3333.84 --> 3335.16]  There's a lot of skills
[3335.16 --> 3336.20]  that can be honed
[3336.20 --> 3337.24]  in this whole process
[3337.24 --> 3337.98]  on both sides.
[3338.38 --> 3339.20]  Well, thank you.
[3339.86 --> 3340.34]  Regrettably,
[3340.48 --> 3341.08]  we've babbled
[3341.08 --> 3342.22]  all our time away
[3342.22 --> 3343.50]  so we are going
[3343.50 --> 3344.50]  to move into
[3344.50 --> 3346.06]  our unpopular
[3346.06 --> 3347.42]  opinion time.
[3347.42 --> 3365.16]  Right, so
[3365.16 --> 3366.72]  get ready guests
[3366.72 --> 3367.34]  we're going to jump
[3367.34 --> 3368.16]  right on in.
[3368.66 --> 3369.04]  Jeff,
[3369.44 --> 3370.38]  what is your
[3370.38 --> 3371.46]  unpopular opinion?
[3372.10 --> 3372.48]  I don't know
[3372.48 --> 3373.12]  how I'm going to top
[3373.12 --> 3374.64]  my last unpopular
[3374.64 --> 3375.06]  opinion
[3375.06 --> 3375.88]  but
[3375.88 --> 3376.84]  I don't know
[3376.84 --> 3377.20]  I feel like
[3377.20 --> 3378.14]  I'll just spark
[3378.14 --> 3378.46]  a,
[3378.72 --> 3379.52]  it's not a big
[3379.52 --> 3380.22]  unpopular opinion
[3380.22 --> 3380.64]  but it's like
[3380.64 --> 3381.44]  it'll start
[3381.44 --> 3382.16]  like a war
[3382.16 --> 3383.12]  kind of like
[3383.12 --> 3383.48]  you know
[3383.48 --> 3384.22]  PS3
[3384.22 --> 3384.56]  or like
[3384.56 --> 3385.06]  PlayStation
[3385.06 --> 3385.74]  versus Xbox
[3385.74 --> 3386.44]  I'm going to go
[3386.44 --> 3387.28]  with like
[3387.28 --> 3388.18]  dogs are the
[3388.18 --> 3388.68]  better pet
[3388.68 --> 3389.54]  than cats.
[3389.86 --> 3390.16]  I know there's
[3390.16 --> 3391.06]  lots of
[3391.06 --> 3391.58]  cat people.
[3392.18 --> 3393.70]  I mean
[3393.70 --> 3394.42]  so it'll be
[3394.42 --> 3395.02]  the unpopular
[3395.02 --> 3396.00]  opinion in this
[3396.00 --> 3396.58]  group but
[3396.58 --> 3397.72]  I have three
[3397.72 --> 3398.10]  dogs.
[3398.58 --> 3398.80]  Okay.
[3399.60 --> 3400.14]  So fighting
[3400.14 --> 3400.46]  words.
[3401.40 --> 3401.94]  Just wait
[3401.94 --> 3402.38]  for your next
[3402.38 --> 3402.70]  PR.
[3403.06 --> 3403.26]  Yeah,
[3403.32 --> 3405.30]  they're fighting
[3405.30 --> 3405.62]  words,
[3405.70 --> 3405.88]  you know,
[3405.92 --> 3406.22]  I know.
[3406.22 --> 3407.58]  I got your
[3407.58 --> 3407.84]  back,
[3407.96 --> 3408.12]  Jeff.
[3408.22 --> 3408.58]  I'm team
[3408.58 --> 3408.88]  dog.
[3409.24 --> 3409.66]  Team dog
[3409.66 --> 3410.06]  all the way,
[3410.14 --> 3410.32]  yeah.
[3412.42 --> 3412.86]  Sarah,
[3413.12 --> 3413.76]  what is your
[3413.76 --> 3414.28]  unpopular
[3414.28 --> 3414.76]  opinion?
[3415.46 --> 3415.70]  Yeah,
[3415.72 --> 3416.00]  I'll be
[3416.00 --> 3416.54]  interested to
[3416.54 --> 3417.32]  see how
[3417.32 --> 3417.80]  unpopular
[3417.80 --> 3418.48]  this is or
[3418.48 --> 3419.02]  not but
[3419.02 --> 3419.78]  I think
[3419.78 --> 3420.92]  aspiring
[3420.92 --> 3421.36]  software
[3421.36 --> 3421.82]  engineers
[3421.82 --> 3422.20]  would be
[3422.20 --> 3422.64]  better off
[3422.64 --> 3422.98]  taking
[3422.98 --> 3424.04]  more
[3424.04 --> 3425.52]  writing and
[3425.52 --> 3425.94]  philosophy
[3425.94 --> 3426.78]  courses and
[3426.78 --> 3427.40]  fewer
[3427.40 --> 3428.52]  computer science
[3428.52 --> 3429.26]  theory courses.
[3429.26 --> 3430.60]  yes.
[3432.16 --> 3432.72]  Interesting.
[3433.22 --> 3433.58]  No,
[3433.60 --> 3433.78]  that's
[3433.78 --> 3434.16]  intriguing.
[3434.94 --> 3435.42]  Why is
[3435.42 --> 3435.62]  that?
[3435.68 --> 3435.92]  Can we
[3435.92 --> 3436.36]  dig one
[3436.36 --> 3437.00]  level deeper?
[3437.74 --> 3437.92]  Yeah,
[3437.94 --> 3438.58]  I think a
[3438.58 --> 3439.20]  lot about
[3439.20 --> 3439.64]  being a
[3439.64 --> 3439.98]  successful
[3439.98 --> 3440.46]  software
[3440.46 --> 3441.28]  engineer is
[3441.28 --> 3441.84]  kind of this
[3441.84 --> 3442.76]  ability to
[3442.76 --> 3443.66]  be able to
[3443.66 --> 3444.88]  make a
[3444.88 --> 3445.26]  concise
[3445.26 --> 3445.66]  argument,
[3446.04 --> 3446.46]  be able to
[3446.46 --> 3447.10]  understand other
[3447.10 --> 3447.74]  arguments and
[3447.74 --> 3448.44]  perspectives and
[3448.44 --> 3449.30]  incorporate it
[3449.30 --> 3451.18]  and use that
[3451.18 --> 3452.58]  to kind of
[3452.58 --> 3453.32]  revise your
[3453.32 --> 3454.18]  opinion and put
[3454.18 --> 3454.74]  forth another
[3454.74 --> 3455.42]  concise argument.
[3455.54 --> 3456.06]  We see this in
[3456.06 --> 3457.00]  architecture documents
[3457.00 --> 3457.60]  all the time.
[3458.14 --> 3458.90]  I was on the
[3458.90 --> 3459.58]  architecture review
[3459.58 --> 3460.00]  board at the
[3460.00 --> 3460.90]  Times for a
[3460.90 --> 3461.40]  long time and
[3461.40 --> 3461.86]  I chaired it
[3461.86 --> 3462.36]  for a while.
[3462.52 --> 3463.24]  I know Natasha
[3463.24 --> 3463.82]  has been on the
[3463.82 --> 3464.40]  architecture review
[3464.40 --> 3465.20]  board as well and
[3465.20 --> 3466.60]  we see so many
[3466.60 --> 3468.36]  long, long
[3468.36 --> 3469.40]  documents that
[3469.40 --> 3470.32]  could be half the
[3470.32 --> 3470.90]  size that they
[3470.90 --> 3472.08]  are and I
[3472.08 --> 3472.88]  think a lot of
[3472.88 --> 3474.70]  engineers don't
[3474.70 --> 3476.18]  use the
[3476.18 --> 3476.94]  theory classes
[3476.94 --> 3477.78]  that they took
[3477.78 --> 3479.10]  in college or
[3479.10 --> 3480.52]  assuming that
[3480.52 --> 3481.80]  if you are
[3481.80 --> 3482.78]  studying computer
[3482.78 --> 3483.16]  science in
[3483.16 --> 3483.56]  college, I
[3483.56 --> 3484.00]  think a lot of
[3484.00 --> 3484.60]  those classes are
[3484.60 --> 3485.80]  not put to
[3485.80 --> 3486.26]  use as a
[3486.26 --> 3486.98]  practical software
[3486.98 --> 3488.00]  engineer but
[3488.00 --> 3489.86]  the area where
[3489.86 --> 3490.58]  I see a lot of
[3490.58 --> 3491.24]  software engineers
[3491.24 --> 3491.98]  kind of having to
[3491.98 --> 3492.74]  improve on the
[3492.74 --> 3493.84]  job is in their
[3493.84 --> 3494.72]  ability to make a
[3494.72 --> 3496.32]  concise argument and
[3496.32 --> 3497.74]  my sister is
[3497.74 --> 3499.12]  getting her PhD in
[3499.12 --> 3499.80]  English so I'm
[3499.80 --> 3500.58]  maybe a little
[3500.58 --> 3501.56]  biased because I
[3501.56 --> 3502.34]  see how much
[3502.34 --> 3503.06]  work she has
[3503.06 --> 3503.80]  like put into
[3503.80 --> 3504.90]  this skill but
[3504.90 --> 3506.40]  and I myself
[3506.40 --> 3508.06]  was my major
[3508.06 --> 3508.86]  was in the
[3508.86 --> 3509.62]  philosophy department
[3509.62 --> 3510.26]  even though it
[3510.26 --> 3511.24]  was a logic and
[3511.24 --> 3512.08]  computer science
[3512.08 --> 3513.28]  interdisciplinary degree
[3513.28 --> 3515.32]  so I used the
[3515.32 --> 3515.92]  skills that I
[3515.92 --> 3516.96]  got from
[3516.96 --> 3517.34]  from my
[3517.34 --> 3518.22]  humanities classes
[3518.22 --> 3520.24]  more than a
[3520.24 --> 3520.82]  number of the
[3520.82 --> 3521.42]  computer science
[3521.42 --> 3522.28]  theory classes that
[3522.28 --> 3522.94]  I had to take in
[3522.94 --> 3523.30]  college
[3523.30 --> 3526.06]  okay Jeff I
[3526.06 --> 3526.54]  didn't know you
[3526.54 --> 3527.42]  renamed yourself
[3527.42 --> 3528.28]  Natasha Jeff
[3528.28 --> 3529.42]  I was just gonna say
[3529.42 --> 3530.02]  that sounds like a
[3530.02 --> 3531.10]  good go time
[3531.10 --> 3532.66]  episode debating the
[3532.66 --> 3533.40]  value of like a
[3533.40 --> 3534.04]  computer science
[3534.04 --> 3534.96]  degree versus like a
[3534.96 --> 3536.26]  dedicated software
[3536.26 --> 3536.92]  engineering because
[3536.92 --> 3537.54]  they're like two
[3537.54 --> 3538.66]  different fields
[3538.66 --> 3539.46]  essentially right
[3539.46 --> 3540.40]  invite me back for
[3540.40 --> 3540.86]  that one
[3540.86 --> 3542.34]  shameless plug I
[3542.34 --> 3543.00]  think we did
[3543.00 --> 3543.80]  one that was
[3543.80 --> 3544.58]  beating around the
[3544.58 --> 3545.38]  bush of that I
[3545.38 --> 3546.56]  say a few maybe
[3546.56 --> 3547.30]  it was years ago
[3547.30 --> 3548.36]  a few months ago
[3548.36 --> 3549.40]  me and Chris
[3549.40 --> 3550.06]  Brando who's
[3550.06 --> 3550.74]  another go time
[3550.74 --> 3551.60]  hosted one around
[3551.60 --> 3552.08]  like English
[3552.08 --> 3552.80]  literature and its
[3552.80 --> 3553.50]  value to software
[3553.50 --> 3555.48]  engineering but I
[3555.48 --> 3555.86]  think that was a
[3555.86 --> 3556.72]  while ago so
[3556.72 --> 3557.80]  absolutely let's do
[3557.80 --> 3558.82]  another one but
[3558.82 --> 3560.20]  again certainly not
[3560.20 --> 3561.96]  least Natasha what
[3561.96 --> 3562.60]  is your unpopular
[3562.60 --> 3564.16]  opinion my unpopular
[3564.16 --> 3565.66]  opinion I think
[3565.66 --> 3568.14]  might be accepted in
[3568.14 --> 3569.16]  computer science like
[3569.16 --> 3569.86]  this kind of circle
[3569.86 --> 3571.22]  but who knows I feel
[3571.22 --> 3572.10]  like the world doesn't
[3572.10 --> 3573.56]  need another superhero
[3573.56 --> 3574.90]  movie there's too
[3574.90 --> 3575.94]  many of them already
[3575.94 --> 3578.10]  I'm done with it
[3578.10 --> 3578.90]  like there's so many
[3578.90 --> 3579.68]  other stories we
[3579.68 --> 3581.44]  could tell so yeah
[3581.44 --> 3582.98]  just let's end that
[3582.98 --> 3584.52]  at least take a break
[3584.52 --> 3585.54]  for a couple years
[3585.54 --> 3586.62]  there are so many
[3586.62 --> 3587.80]  more bugs that need
[3587.80 --> 3588.76]  to be superheroes
[3588.76 --> 3590.52]  we gotta have like
[3590.52 --> 3592.02]  beetle man lady
[3592.02 --> 3593.04]  bird lady
[3593.04 --> 3595.24]  caterpillar
[3595.24 --> 3596.66]  kazam
[3596.66 --> 3597.58]  there's so many
[3597.58 --> 3598.48]  opportunities
[3598.48 --> 3599.08]  you could do
[3599.08 --> 3599.64]  something with the
[3599.64 --> 3601.20]  gopher like gopher
[3601.20 --> 3601.98]  man or something
[3601.98 --> 3602.50]  that could be
[3602.50 --> 3604.30]  go for woman
[3604.30 --> 3605.22]  okay yes
[3605.22 --> 3609.16]  Sarah I loved what
[3609.16 --> 3610.04]  you said you gave
[3610.04 --> 3611.12]  me an idea to see
[3611.12 --> 3612.42]  my next time I have
[3612.42 --> 3613.34]  some free time to
[3613.34 --> 3614.22]  hack I'm gonna use
[3614.22 --> 3615.58]  something like GPT3
[3615.58 --> 3616.58]  to just create a
[3616.58 --> 3618.36]  plugin for github
[3618.36 --> 3619.48]  that will just run
[3619.48 --> 3620.26]  whatever you want to
[3620.26 --> 3621.76]  say through that to
[3621.76 --> 3622.94]  sound more empathetic
[3622.94 --> 3624.82]  and more something I
[3624.82 --> 3625.82]  don't know but I
[3625.82 --> 3626.50]  love that by the time
[3626.50 --> 3627.38]  this episode is out
[3627.38 --> 3628.04]  maybe it will be on
[3628.04 --> 3628.52]  the marketplace
[3628.52 --> 3629.72]  incredible this will
[3629.72 --> 3630.42]  be really really
[3630.42 --> 3632.18]  useful for everyone
[3632.18 --> 3633.04]  yeah send it my
[3633.04 --> 3633.42]  way
[3633.42 --> 3636.18]  action item for
[3636.18 --> 3636.94]  everyone listening
[3636.94 --> 3638.70]  make it happen
[3638.70 --> 3640.02]  come on put our
[3640.02 --> 3640.66]  heads together we
[3640.66 --> 3641.44]  can make it happen
[3641.44 --> 3643.08]  well it has been an
[3643.08 --> 3645.18]  absolute joy talking
[3645.18 --> 3646.22]  to you all genuinely
[3646.22 --> 3646.96]  I can't wait to get
[3646.96 --> 3647.96]  you all back I have
[3647.96 --> 3649.26]  so many more episode
[3649.26 --> 3650.64]  ideas I'm sure you
[3650.64 --> 3652.50]  do too Natalie I
[3652.50 --> 3652.94]  hope you have a
[3652.94 --> 3653.76]  wonderful rest of
[3653.76 --> 3654.82]  your days but for
[3654.82 --> 3657.00]  now adios and
[3657.00 --> 3657.52]  goodbye
[3657.52 --> 3663.66]  all right that is
[3663.66 --> 3664.32]  go time for this
[3664.32 --> 3665.24]  week thanks for
[3665.24 --> 3667.00]  listening now is the
[3667.00 --> 3667.68]  best time to
[3667.68 --> 3668.62]  subscribe if you
[3668.62 --> 3669.88]  haven't yet head to
[3669.88 --> 3671.18]  go time dot fm for
[3671.18 --> 3672.70]  all the ways and if
[3672.70 --> 3673.96]  you are a regular go
[3673.96 --> 3675.10]  time listener check out
[3675.10 --> 3676.10]  our membership program
[3676.10 --> 3677.42]  directly support our
[3677.42 --> 3679.00]  work save yourself some
[3679.00 --> 3679.92]  time by ditching the
[3679.92 --> 3681.34]  ads and get bonuses
[3681.34 --> 3682.86]  like exclusive content
[3682.86 --> 3684.82]  and free stickers check it
[3684.82 --> 3686.50]  out at changelog.com
[3686.50 --> 3687.58]  slash plus plus
[3687.58 --> 3689.12]  thanks again to our
[3689.12 --> 3690.58]  partners at fastly for
[3690.58 --> 3692.32]  CD ending for us to
[3692.32 --> 3694.02]  fly.io for serving up
[3694.02 --> 3694.96]  our app to the
[3694.96 --> 3696.00]  mysterious breakmaster
[3696.00 --> 3696.98]  cylinder for these
[3696.98 --> 3698.44]  dope beats and to you
[3698.44 --> 3699.44]  for being part of the
[3699.44 --> 3700.74]  go time community we
[3700.74 --> 3702.34]  appreciate you that is
[3702.34 --> 3703.54]  all for this week we'll
[3703.54 --> 3705.24]  talk to you next time on
[3705.24 --> 3705.90]  go time
[3705.90 --> 3724.42]  hello
