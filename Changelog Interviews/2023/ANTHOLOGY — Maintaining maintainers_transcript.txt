[0.00 --> 8.42]  This week on The Change Law, we're continuing our Maintainer Month series by taking you back
[8.42 --> 15.20]  to the hallway track of the Linux Foundation's Open Source Summit North America 2023 in Vancouver,
[15.38 --> 21.44]  Canada. Today's anthology episode features Stormy Peters, VP of Communities at GitHub,
[22.20 --> 29.10]  Dr. Don Foster, Director of Open Source Community Strategy at VMware, and Angie Byron, Drupal
[29.10 --> 35.24]  Core Product Manager and Community Director at Avon. On this episode, we talk about the core issues
[35.24 --> 41.84]  of open source software maintainers, finding balance, understanding project health, identifying
[41.84 --> 47.22]  new contributors, getting funding and support, knowing when to step back, healthy succession
[47.22 --> 52.82]  plans for leaders, and even a dash of choosing the right license. Learn more about Maintainer
[52.82 --> 59.08]  Month at maintainermonth.github.com. Special thanks to our friends at GitHub for sponsoring
[59.08 --> 64.52]  us to attend this conference as part of Maintainer Month. And also a big thanks to our friends
[64.52 --> 70.16]  and partners at Fastly and Fly. Our pods are fast to download globally because Fastly is
[70.16 --> 75.76]  fast globally. Check them out at fastly.com. And our friends at Fly help us put our app and
[75.76 --> 81.02]  our database close to our users all over the world. And they'll do it for you too, with no
[81.02 --> 83.90]  ops. Check them out at fly.io.
[95.14 --> 100.56]  Well, I'm here with Richard Moot, the API design lead for all of Square. And we're talking about the
[100.56 --> 106.62]  GraphQL API that is now in OpenAlpha looking for feedback. So Richard, what's the story with this API?
[106.62 --> 114.14]  So we've announced this at Unbox last year, and we've been just incrementally adding parts to
[114.14 --> 121.10]  our GraphQL API. It's been a big ask from developers within our community because it makes using Square's
[121.10 --> 126.30]  platform so much easier for particular things. You're no longer having to, let's say, call like
[126.30 --> 131.38]  three or four different APIs to like pull together, you know, a bunch of different data. And so we've just
[131.38 --> 136.46]  been trying to learn more and more like how developers are planning on using this and making sure that we get
[136.62 --> 140.90]  right before we actually transition to the next phase and its release.
[141.42 --> 148.48]  So you have the orders API out there, the catalog API, the customers API, the merchants API, the
[148.48 --> 155.40]  payments API, the refunds API, and the inventory API out there. And you also have the GraphQL
[155.40 --> 160.18]  Explorer out there. Tell me, what are you expecting from developers? What feedback do you want? What are
[160.18 --> 160.64]  your expectations?
[161.32 --> 166.34]  I think our expectations is to find out all the different ways that you're using it and that we can
[166.34 --> 171.20]  make it better for you. I mean, right now, you know, we've gotten really good feedback. We have,
[171.50 --> 176.80]  I mean, as soon as I announced the update to our docs that we recently did, the very first question
[176.80 --> 181.70]  that I got on Twitter from someone was like, when is this going out of alpha? And so like, we're really
[181.70 --> 186.46]  happy to see that. But we also are still wanting to hear from developers like, you know, you're
[186.46 --> 191.30]  implementing this, you're trying to build something. What is causing you angst? Like, what is,
[191.30 --> 198.06]  is it issues with like constraints around query depths or a number of queries? Is it fast enough
[198.06 --> 203.16]  for you? Are you trying to use it in a particular mobile app or electron app or something? And like,
[203.24 --> 207.96]  you know, what, what issues are you kind of coming across and like, what, how can we make it better?
[208.20 --> 212.36]  And I would definitely say that like anything that you come across when you come and you try it out,
[212.42 --> 217.66]  whether it's in the GraphQL Explorer, in your command line, in your app, we want you to reach out to us
[217.66 --> 223.62]  on our Slack or our forums. Those would be great. You can also tweet at us. I will definitely be
[223.62 --> 228.12]  keeping an eye on that. But I will probably still always say like, hey, like the forums are a great
[228.12 --> 232.22]  resource because we have a lot of questions that are already asked there. And we really just want
[232.22 --> 238.50]  to like funnel all that feedback to the team so that we can get this into there in time to make
[238.50 --> 243.52]  this ready for the next phase. Very cool. Okay. So if you want to check this API out yourself,
[243.52 --> 250.56]  go to developer.squareup.com. Again, developer.squareup.com. It is an open alpha. They're
[250.56 --> 255.78]  looking for feedback. Hit them up on Slack, head to the forums, whatever works for you. Once again,
[255.86 --> 257.60]  developer.squareup.com.
[273.52 --> 281.98]  GitHub Sponsors. What is the state of GitHub Sponsors?
[282.60 --> 288.68]  So GitHub Sponsors is now generally available for companies as well as individuals to donate money
[288.68 --> 293.40]  to maintainers or give money to maintainers, not donate. It's been a journey. You've had a couple
[293.40 --> 297.68]  people in charge of it. The last time we talked to Jessica Lord, she was, this was about a year and a
[297.68 --> 302.24]  half ago, was it? Probably. She came back to GitHub. She was a boomerang. Yeah. She did.
[302.46 --> 304.76]  She loves GitHub so much. I'm glad she came back. Yeah. She's awesome.
[306.20 --> 309.12]  Is she still in charge? She's not still in charge of GitHub Sponsors, right?
[309.12 --> 314.22]  She's not doing sponsors now. Okay. Is anyone in charge of it? Who is in charge of it? How's it work?
[314.32 --> 316.88]  We actually have an open job rec right now. Is that right?
[316.88 --> 320.06]  If you would like to be in charge of it, you can apply. Gosh, I could slay that.
[321.18 --> 326.86]  It's actually for a team that's going to be looking at how to change the open source ecosystem so that
[326.86 --> 332.86]  we fund maintainers in ways that aren't just a paycheck. Yeah. It's a tough job. Who could do
[332.86 --> 338.46]  that job well? What would they have done beforehand to do that job well? It's been kind of fun trying
[338.46 --> 343.20]  to recruit. We really want someone who's passionate about open source software, who has some kind of
[343.20 --> 344.16]  background in it. We love open source. You know that right.
[344.16 --> 351.26]  Yeah. We could pair up on that job, Jared. I've also interviewed people who were in insurance before
[351.26 --> 356.08]  and just in insurance models. I've interviewed people that were in venture capital money. We're just
[356.08 --> 359.86]  kind of experimenting with who can bring new ideas to the space.
[360.46 --> 365.74]  It has to begin with a desire. What is GitHub optimizing for when it comes to sponsors? What
[365.74 --> 370.88]  does GitHub want with sponsors in general? What are the possibilities?
[371.78 --> 376.36]  Our ultimate goal is to make open source software successful. That means providing ways for
[376.36 --> 381.66]  maintainers to have time and energy to invest in open source software. Part of that solution
[381.66 --> 387.42]  is helping companies understand what dependencies they have and making sure that software is secure
[387.42 --> 392.06]  and reliable. Some of them know they have dependencies on open source software. They
[392.06 --> 395.94]  really want to help make sure it's reliable. They need someone to help them if it goes down.
[395.94 --> 396.20]  Yeah.
[396.44 --> 401.18]  They understand money is part of that solution. How do we help them provide that? How do we help
[401.18 --> 403.80]  maintainers say, here I am. Here's how I can help you.
[403.98 --> 408.26]  Right. That sounds like a challenge. You said it's now available to companies.
[408.26 --> 413.22]  It was always available to companies, but until recently they had to pay via credit card,
[413.78 --> 417.52]  which how many people at a company can put a couple hundred thousand dollars on their credit
[417.52 --> 422.58]  card. Right. So we added things like invoices and normal corporate things. I see. So you
[422.58 --> 428.80]  grease the skids, as they say, for companies to be able to actually give at a higher clip than
[428.80 --> 432.22]  they could with some sort of corporate credit card. Yep. This has been an effort in the making
[432.22 --> 436.74]  because I know when we talked to Jessica, that was the plan to get there and you're saying
[436.74 --> 442.72]  now it's available. Yep. Okay. How has that changed things? Like has the giving or supporting
[442.72 --> 449.66]  gotten easier? Has the amounts increased? What are the stats behind this new feature being there
[449.66 --> 456.34]  for sponsors? Yeah. I think it's worth looking at before we were generally available in just our
[456.34 --> 460.84]  beta program. We already had like $30 million flow through the program. So obviously there was like
[460.84 --> 465.32]  a high demand for it. Yeah. And we just GA'd a couple of weeks ago. So I don't have numbers,
[465.32 --> 470.08]  but I can tell you that there are new companies signing up for it. Okay. Okay. Can you speak to
[470.08 --> 473.94]  the excitement then? I mean, there's no traction net or to compare at least. Oh, there's traction.
[474.18 --> 478.12]  Oh, I mean, what do you mean by that? Is it so new? There's not a lot of details you can share yet
[478.12 --> 482.86]  because it's fresh. What's the response from those chomping at the bit to get access to this? It's like,
[483.20 --> 489.84]  is it a lot of companies desiring this? I think a lot of companies want to make sure the software they use
[489.84 --> 496.36]  is reliable, secure, and that they recognize that they use it, that it's kind of, I think the people
[496.36 --> 500.12]  at companies want to make sure they're fair. I always say like companies aren't people and they
[500.12 --> 502.04]  aren't motivated like people are. Right.
[502.14 --> 505.36]  If I'm like, say I go out of town. There's no emotion.
[505.92 --> 511.48]  Or there's no sense of like give and take the same way people have it. Like say I go out of town and I
[511.48 --> 516.10]  ask my neighbor to like come feed the cat every day. And when I get back into town, I'm like, oh,
[516.10 --> 519.64]  she did me a huge favor. So like I'm going to take her some apples from my apple trees.
[520.32 --> 524.78]  And so I take apples over to her and she goes, wow, this was like a lot of apples just for feeding
[524.78 --> 528.36]  the cat. So I'm going to make an apple pie. And she like brings me back an apple pie. And there's
[528.36 --> 534.28]  like this give and take that we take for granted as humans. Yeah. Who in a company, someone in a
[534.28 --> 539.12]  company has to do that because a company doesn't do that. Right. Our profit generating machines.
[539.38 --> 544.06]  And so the people have to like step out of the norm in order to do that. But people do want to.
[544.06 --> 548.44]  So we're trying to give them tools like here's your dependencies. Here's the dependencies of
[548.44 --> 553.42]  your dependencies. Okay. So all that stuff exists now inside of, is it like inside the sponsors
[553.42 --> 558.58]  dashboard or is it just inside of GitHub's like various tools have it. So we can help you
[558.58 --> 562.18]  with sponsors. We also have an Ospo dashboard for corporations where they can see what they're
[562.18 --> 568.56]  using and what they're contributing to. That's cool. And so what's a, what's a typical give
[568.56 --> 573.80]  out of a corporation these days? Companies would also like to know that because we actually had
[573.80 --> 577.54]  one company that came and said, I want to make sure that I don't look like I'm giving
[577.54 --> 581.12]  too little. Right. And so they didn't want to give, and they were willing to give a couple
[581.12 --> 585.58]  hundred thousand dollars, but they were afraid it would look like too little. Yeah. So I
[585.58 --> 589.94]  think we need to establish some norms. Right. So it's still kind of playing out. We don't
[589.94 --> 594.30]  know what a norm is. We don't know. The best indicator of that has been the FOSS Contributor
[594.30 --> 600.50]  Fund to some degree. Yes. And we just talked to Chad Whitaker, the show's out there. As part
[600.50 --> 605.72]  of this episode we did with Maintainer Month and whatnot, and essentially he did some back
[605.72 --> 611.16]  of the napkin math and it was like 2K per engineer to the software that they depend on essentially.
[611.38 --> 616.14]  So if they have 50 engineers, this is a round number, 2K, you do the math.
[616.56 --> 619.28]  Yeah. You could look at it in a number of ways. You could look at how many engineers does your
[619.28 --> 623.92]  company have? How many, how much money do you make off the software you build on it?
[624.00 --> 624.26]  Right.
[624.26 --> 630.10]  Like how many different software projects do you use? Like you could offer up a whole bunch
[630.10 --> 634.08]  of formulas and I think we probably just need to pick one and suggest something.
[634.58 --> 634.66]  Yeah.
[634.72 --> 639.12]  We had this entire conversation, Stormy. I really wish you would hear it. I'm going to paraphrase
[639.12 --> 646.08]  it. We talked about this idea of a pricing page that a SaaS company might have for them. You got
[646.08 --> 650.46]  the free tier, you got the pro plan, you got the business plan, you got the enterprise. And essentially
[650.46 --> 657.60]  we need an on-ramp to fair funding of open source, whether I'm an individual or a small
[657.60 --> 663.98]  team or a larger enterprise. The idea of fairness, I think they ask you all, get up sponsors, hey,
[664.04 --> 668.18]  what is fair, right? What is, what should I give? What's too little? What's too much? There's
[668.18 --> 673.84]  no real, I guess, documentation out there of what fair is. You know, if you're in this realm,
[674.32 --> 678.78]  maybe 2K per month is too much for you, but it's at least a good place to start. Maybe 2K per
[678.78 --> 684.78]  month or sorry, whatever the number is, 2K per developer. Maybe it's more like 500 or
[684.78 --> 688.24]  what is a fair number that makes sense for you? How do you quantify that? Give them some
[688.24 --> 693.80]  sort of, you know, algorithms basically to sort of figure out what fair really is for
[693.80 --> 694.00]  them.
[694.60 --> 700.70]  And it also depends on what the maintainer wants to, wants to be responsible for or commit
[700.70 --> 704.20]  to. I'm not quite sure the right word there. Like what if I wrote it last summer, I had a
[704.20 --> 708.18]  month off and I wrote this really cool library that solved a need for me and I put it out
[708.18 --> 712.94]  there and like, I'm done with it, right? Like I did it, I put it out there. If you tell
[712.94 --> 716.56]  me like it's being used in hospitals and someone's dying, I'm going to come back and help you.
[716.68 --> 721.58]  But like, I have another job, I have a family, like I'm not working on it anymore. That's
[721.58 --> 725.54]  a really different scenario than someone who's trying to make a living off of it, develop
[725.54 --> 729.68]  the library, wants to keep improving it, wants to hear feedback, wants to like help
[729.68 --> 732.52]  you however you're using it. You know, I talked to someone last night at dinner and he's
[732.52 --> 737.12]  like, I have a job, but like they're using my software and like I try to help them. I,
[737.28 --> 741.28]  you know, I, I look at their pull requests, I send them emails. Like he's in a very active
[741.28 --> 742.26]  role in his project.
[742.48 --> 742.56]  Right.
[742.90 --> 744.18]  That's, those are different scenarios.
[744.64 --> 745.38]  Maintainer guilt.
[746.02 --> 746.34]  Yeah.
[746.42 --> 750.34]  Not guilt. It's like you, you want to help solve the, you're solving a problem for the
[750.34 --> 750.60]  world.
[750.60 --> 752.06]  He wants to do it.
[753.24 --> 756.98]  But he, he would probably have more time to do it if he got compensated more.
[757.30 --> 757.40]  Right.
[757.60 --> 761.78]  But also he wants to do it right now, but three, four or five years from now, his life
[761.78 --> 765.40]  changes. He doesn't want to do it anymore. Now he gets the maintainer guilt of like, well,
[765.40 --> 769.12]  all these people rely upon me. I'm burning out. I don't want to do this. I got a baby
[769.12 --> 770.26]  now or whatever it is.
[770.54 --> 770.86]  Right.
[771.00 --> 774.80]  That's been a theme. That's a theme for maintainer month. And it's also was a talk yesterday
[774.80 --> 776.42]  about how do you do succession planning?
[777.34 --> 777.56]  Yeah.
[777.82 --> 779.12]  How do you do succession planning?
[779.12 --> 782.82]  I'm definitely not the expert. I could find you the speaker of that talk.
[782.94 --> 783.84]  We have talked about that.
[784.04 --> 785.16]  We asked a few people that question.
[785.36 --> 788.94]  It's like, uh, it's like, it's like getting a room. There's just so many rows to get there.
[789.50 --> 793.94]  Yeah. I think it definitely is building out your community and building trusts along the
[793.94 --> 799.52]  way. Like, yeah, you have to build, you have to put other people in positions of trust.
[800.12 --> 802.06]  So there's someone to fill your shoes when you leave.
[802.20 --> 802.72]  But it's really hard.
[802.72 --> 807.12]  That's the easy way to do it. I mean, not the easy way, but that's like the right way to
[807.12 --> 811.58]  do it, I guess, versus like one day being like, okay, I need a successor. Right.
[812.04 --> 812.32]  Right.
[812.36 --> 817.54]  But I haven't been preparing for this day at all. And, but I need one right now. And so
[817.54 --> 822.98]  what I put out a post on my socials and I was like, someone please take over this project.
[822.98 --> 827.30]  I think we could learn a lot from nonprofits in this space. I think they have the same
[827.30 --> 827.84]  problem.
[828.04 --> 828.76]  Okay. How so?
[829.56 --> 833.24]  So a lot of nonprofits don't have people on salary, like a lot of the smaller ones. And
[833.24 --> 837.50]  so if the person, volunteers, yeah. If the person running wants to like leave or go do
[837.50 --> 840.32]  something else, they have to have a succession plan as well.
[840.52 --> 840.82]  Okay.
[841.48 --> 845.74]  Well, we talked about having terms of service, uh, to some degree, like a, if you want to
[845.74 --> 849.52]  be a maintainer, et cetera, or you are a maintainer, or you want to bring on a contributor,
[849.52 --> 853.16]  a term of service. So what you're saying is if you need to leave or you need to step
[853.16 --> 861.66]  away, the social construct should be plan for successor, invite a successor, have some
[861.66 --> 864.90]  sort of plan, like just don't leave your station abandoned.
[865.62 --> 866.48]  And I agree with that.
[866.56 --> 866.80]  Right.
[867.00 --> 869.70]  That would be great if you didn't abandon, especially if other people are using it.
[870.24 --> 874.14]  But I agree with that as well. Like it's much easier to get people to step up to positions
[874.14 --> 876.18]  in your project if you're clear about what they are.
[876.46 --> 876.60]  Right.
[876.86 --> 877.06]  Yeah.
[877.06 --> 882.56]  Hey, if you submit five pull requests and I, you know, I pretty much accepted them unchanged
[882.56 --> 887.16]  and you're always there when I send you an email or a DM, like then I'm willing to consider
[887.16 --> 888.46]  you for this role.
[888.90 --> 894.48]  Right. And if you accept it when you leave, which is cool, please help me find somebody
[894.48 --> 895.26]  who might be suitable.
[895.90 --> 896.64]  That would be a good cause.
[896.64 --> 899.92]  And the please might be more you have to versus just simply please.
[900.14 --> 901.12]  Can you say that though?
[901.12 --> 907.62]  Well, I, well, what I'm asking, I guess, is like, should we, there's, there's no perfect
[907.62 --> 913.46]  way to do this, but maybe the version that gets deployed in most cases, like if you accept
[913.46 --> 919.14]  the position on a project that has, I don't know, some usefulness, some threshold of usefulness
[919.14 --> 923.70]  and you are a crucial person because you've accepted a role as a maintainer.
[923.70 --> 924.00]  Yeah.
[924.50 --> 926.94]  Maybe you agree to mentor a certain number of people or something.
[927.34 --> 928.08]  Yeah, exactly.
[928.70 --> 934.38]  Something, something that says I care about my team, my other maintainers and this project
[934.38 --> 936.96]  enough to accept the role because I like it.
[936.96 --> 943.78]  But also if I need to step away, some sort of responsibility to ensure non-breakage, you
[943.78 --> 943.96]  know?
[944.20 --> 948.20]  So one of our, our GitHub students, you know, the students that's in GitHub education shared
[948.20 --> 953.60]  with me a tip that he learned yesterday, which was instead of write, you know, someone submits
[953.60 --> 958.74]  an issue instead of just writing code and solving it and doing your own pull request and closing
[958.74 --> 958.98]  it.
[959.26 --> 963.50]  They suggested writing out like the whole problem and how you saw the solution.
[963.50 --> 966.80]  And they say it would take as long as just solving it, but writing it up and describing
[966.80 --> 971.04]  it and then putting it out there for someone else to be able to pick up is a good way to
[971.04 --> 972.16]  like grow your project.
[973.02 --> 973.98]  Don't repeat yourself.
[974.16 --> 978.98]  That's so forward thinking though, you know, it's just like it requires discipline and forethought.
[979.24 --> 981.94]  It's hard to do that all the time where you're just like, well, I could just fix it real
[981.94 --> 982.20]  quick.
[982.38 --> 984.42]  Especially if you like writing code and you like your project.
[985.22 --> 986.26]  I like to write code.
[986.36 --> 988.18]  I do not like to write prose very much.
[988.66 --> 990.20]  I started this because I like coding.
[990.66 --> 991.94]  I'm just going to code this up real quick.
[991.94 --> 994.76]  But you do that over and over and over again.
[994.86 --> 998.40]  Eventually it's just a recipe for disaster, you know, as your, as your life changes, as
[998.40 --> 999.44]  your desires change.
[1001.02 --> 1005.04]  But you can write prose for the problems that are kind of boring to you and then save the
[1005.04 --> 1006.30]  interesting ones for yourself.
[1006.86 --> 1007.08]  Yeah.
[1007.76 --> 1009.12]  Just don't tell anybody that's what you're doing.
[1010.80 --> 1012.30]  Here's a bunch of boring issues, guys.
[1012.42 --> 1013.36]  You guys handle those.
[1013.42 --> 1014.36]  I'll take all the fun stuff.
[1014.38 --> 1015.00]  I'll take the fun stuff.
[1015.50 --> 1017.52]  It might not work to grow your project.
[1017.52 --> 1023.86]  Companies can now contribute to open source via GitHub sponsors in new ways, not just credit
[1023.86 --> 1024.26]  cards.
[1024.92 --> 1026.54]  POs, larger checks, et cetera.
[1027.84 --> 1030.78]  What's the state, I guess, the next major thing for sponsors?
[1030.90 --> 1031.64]  What are you working on?
[1031.72 --> 1035.76]  What is the sponsors team or this new leadership?
[1036.04 --> 1037.94]  What's the next plan for GitHub sponsors?
[1037.94 --> 1038.38]  Yes.
[1038.74 --> 1038.98]  Yes.
[1038.98 --> 1041.32]  I think there's still features we can add in the products.
[1041.48 --> 1045.26]  Like we talked about, like being able to see all your dependencies and all those dependencies
[1045.26 --> 1047.50]  and, you know, contribute with like one click.
[1047.64 --> 1048.88]  You know, there's things like that we can add.
[1049.18 --> 1052.04]  But we also have a couple other programs that we're experimenting with and we're bringing
[1052.04 --> 1053.32]  them into, you know, one group.
[1053.92 --> 1057.70]  So we have, we have a accelerator program that's going on right now.
[1057.78 --> 1058.82]  It's a 10 week program.
[1059.02 --> 1061.92]  We have 20 people in it in this round, $2,000 a week.
[1062.18 --> 1063.70]  And they meet a couple times a week.
[1063.74 --> 1064.84]  They get like mentorship.
[1065.16 --> 1066.22]  They get to meet each other.
[1066.22 --> 1068.98]  And these are people that want to take their project to the next level.
[1069.50 --> 1071.88]  And so we're, we're figuring out like, what do they need?
[1071.98 --> 1073.02]  What can we offer them?
[1073.02 --> 1077.40]  And then hopefully what can we build into sponsors and the GitHub product to help all
[1077.40 --> 1079.44]  maintainers who want to take their project to the next level?
[1079.64 --> 1079.74]  Yeah.
[1080.30 --> 1084.62]  We also have GitHub funds because it's really hard to get venture capital money when you
[1084.62 --> 1088.06]  are writing your, your company's code in open source.
[1088.52 --> 1090.72]  Venture capitalists like to think you have secret sauce.
[1091.26 --> 1096.18]  And so we have GitHub fund that actually funds open source software projects that
[1096.18 --> 1097.74]  are companies, startup companies.
[1098.34 --> 1101.72]  And that's GitHub proper that funds it or they're pulling together other people's money?
[1101.84 --> 1102.16]  How does it work?
[1102.16 --> 1105.18]  It's a partnership with Microsoft's M12 venture capital fund.
[1105.54 --> 1105.90]  Okay.
[1106.24 --> 1107.76]  How do those projects get selected?
[1107.90 --> 1109.04]  Is it an application?
[1109.30 --> 1111.52]  Is it, who gets funded?
[1111.62 --> 1112.16]  How do they get funded?
[1112.36 --> 1112.88]  Most stars.
[1112.88 --> 1117.22]  The accelerator program is, yeah, most stars.
[1117.48 --> 1119.90]  The accelerator program is an application.
[1120.18 --> 1123.80]  So someone who's interested in taking their project to the next level applies and we selected
[1123.80 --> 1124.08]  them.
[1124.90 --> 1129.52]  On the GitHub fund, we actually try to source them and find them and then we reach out.
[1130.16 --> 1134.72]  They could also reach out, but we actually do a lot of, a lot of research to try to find
[1134.72 --> 1134.88]  them.
[1135.52 --> 1139.66]  Will you do the accelerator package or process as part of like batches?
[1139.66 --> 1144.70]  I'm thinking like YC, for example, like you have YC batch X and maybe this is a version
[1144.70 --> 1148.26]  for open source where the accelerator, is it called accelerate?
[1148.70 --> 1149.10]  Accelerator.
[1149.62 --> 1150.02]  Accelerator.
[1150.24 --> 1155.98]  This accelerator program that, you know, maybe this first batch is like, hey, we've helped
[1155.98 --> 1158.56]  these maintainers level up their projects.
[1159.28 --> 1163.98]  Maybe the GitHub fund is right after that for them potentially to like throw some money in
[1163.98 --> 1164.88]  there or whatever it might be.
[1164.88 --> 1167.08]  Is there a thought around that process?
[1168.02 --> 1169.98]  I hope with all the things.
[1170.28 --> 1171.52]  Yeah, we'll definitely repeat it.
[1171.68 --> 1175.88]  I hope with all the things that we do that we learn and iterate and I'd love to see us
[1175.88 --> 1179.24]  build more and more into the products so that we could make it available to everybody.
[1179.40 --> 1179.76]  Right.
[1179.84 --> 1183.94]  So like maybe when you reach 5,000 stars, I know we were joking about it before, but
[1183.94 --> 1187.98]  when you reach 5,000 stars, we know you really need, it would be really helpful if
[1187.98 --> 1191.84]  you knew about GitHub sponsors and had a list of tips and tricks that work really well
[1191.84 --> 1194.36]  with it and so we somehow surfaced that.
[1194.78 --> 1194.90]  Right.
[1195.34 --> 1198.86]  Behind the scenes where we're hearing that like a lot of the activity on GitHub is done
[1198.86 --> 1204.04]  by like 1% of the repos and that's kind of part of like funding open source.
[1204.14 --> 1209.48]  Like there's a lot of activity in GitHub around open source and maintainers and whatnot that's
[1209.48 --> 1210.74]  in like a very small percentage.
[1210.88 --> 1214.70]  Is that, how as part of GitHub sponsors, do you have active reach out to this kind of
[1214.70 --> 1214.90]  folks?
[1214.90 --> 1217.66]  Like are you looking at the 1% that's got a lot of activity?
[1218.22 --> 1222.02]  How do you kind of quantify or narrow down who to help and how to help them?
[1222.54 --> 1226.38]  So GitHub sponsors, individuals and companies are deciding who they want to sponsor.
[1226.72 --> 1226.88]  Right.
[1226.94 --> 1233.02]  We can, we can obviously like offer suggestions, but ultimately it's down to like you deciding
[1233.02 --> 1235.02]  that you want to give Jared like $10 this month.
[1235.02 --> 1236.34]  So you're handing out shovels and picks.
[1236.54 --> 1237.58]  You're not giving maps.
[1238.30 --> 1239.52]  We're trying to provide maps.
[1239.68 --> 1243.58]  We're not providing rules and saying you must turn right here.
[1243.58 --> 1243.94]  Yeah.
[1244.22 --> 1250.64]  Well, when you said at 5,000 stars, you may be, so that made me think you might have
[1250.64 --> 1252.96]  some proactive outreach as part of sponsors.
[1252.98 --> 1254.66]  I would love to start doing that.
[1254.98 --> 1255.06]  Right.
[1255.34 --> 1260.14]  But what I wanted to say when you asked what's next, I hope we learn from the accelerator this
[1260.14 --> 1266.12]  round and learn, you know, who is interested, who came, what did they learn, what was most
[1266.12 --> 1270.38]  valuable for them, what kind of problems are they encountering, like, and we iterate.
[1271.04 --> 1271.20]  Yeah.
[1271.20 --> 1276.30]  But in terms of the sponsors, the product, it's pretty much what it is until we get this
[1276.30 --> 1278.12]  new person to come run product, right?
[1278.60 --> 1281.90]  We have a team working on sponsors, but we're hiring a new lead.
[1282.16 --> 1282.94]  A lead for the team.
[1283.04 --> 1284.52]  For sponsors and accelerator together.
[1284.68 --> 1288.20]  Because I know like when we spoke with Devin Zugel originally, when she was finished with
[1288.20 --> 1292.22]  her work there, and probably when we talk about with Jessica as well, you know, there's
[1292.22 --> 1298.82]  other ideas of ways of providing funding for open source through sponsors, the product
[1298.82 --> 1300.82]  that's not money.
[1301.42 --> 1306.76]  Well, no, it's money, but maybe you have like for, so bug bounties is one idea of like,
[1306.82 --> 1308.06]  well, we have issues, right?
[1308.08 --> 1310.08]  We have all these things through sponsors.
[1310.18 --> 1312.46]  Maybe we could also provide funding through bug bounties.
[1312.46 --> 1315.48]  And I remember asking Devin about that and she had her ideas on it.
[1315.54 --> 1317.32]  And then I think Jessica had her ideas.
[1317.96 --> 1325.20]  But in terms of like changing the product dramatically or like adding to it, you're looking for a
[1325.20 --> 1325.60]  new leader.
[1326.20 --> 1326.94]  Is that fair?
[1327.04 --> 1328.00]  Or you're like, are you?
[1328.42 --> 1329.36]  We're still working on the product.
[1329.54 --> 1329.64]  Okay.
[1329.78 --> 1330.90]  And we're hiring a new leader.
[1331.00 --> 1331.22]  Okay.
[1331.22 --> 1334.92]  And I would hope with things like bug bounty that what we're doing is making it possible
[1334.92 --> 1336.92]  for you to host a bug bounty if you want to.
[1337.18 --> 1339.84]  Not that you have to have a GitHub bug bounty to sign up for.
[1341.00 --> 1344.32]  No, I mean, the idea there is like, well, you could just build it right into issues.
[1344.72 --> 1349.18]  And so you open an issue and say, hey, I would love for this issue to be addressed.
[1349.58 --> 1350.82]  Here's $1,000.
[1351.56 --> 1352.90]  Or maybe we could all bid on it.
[1353.00 --> 1355.14]  We could all say, I'll throw $10 into the pot.
[1355.34 --> 1355.80]  Yeah, exactly.
[1355.98 --> 1356.50]  Yeah, for sure.
[1356.50 --> 1356.72]  Pool the money.
[1356.72 --> 1360.66]  So like those kinds of ideas, maybe good idea, maybe not a good idea.
[1360.66 --> 1364.10]  But ultimately, like the sponsor's team has to decide what's going to be worked on.
[1364.66 --> 1368.12]  And so I was just wondering if the product's moving forward in the meantime while you're
[1368.12 --> 1369.44]  looking for someone to lead that team.
[1369.48 --> 1370.74]  And it sounds like they're still working on stuff.
[1370.88 --> 1371.20]  They are.
[1371.44 --> 1375.76]  But this accelerator thing is super cool, by the way.
[1376.14 --> 1379.38]  I remember covering it in ChangeLog News and seeing a bunch of projects get money.
[1379.60 --> 1380.66]  And they're all excited.
[1380.88 --> 1382.24]  And they get mentorship too, right?
[1382.36 --> 1382.50]  Yep.
[1383.36 --> 1383.98]  So hopefully.
[1384.94 --> 1386.44]  They get mentorship and a cohort.
[1386.60 --> 1386.92]  Yeah.
[1387.04 --> 1390.54]  I mean, hopefully that whole deal really helps them.
[1390.54 --> 1393.52]  And then we can learn from it, like you said, and do it again.
[1394.26 --> 1398.26]  Because when I started in open source, it was definitely like everyone's dream was to
[1398.26 --> 1400.00]  get a paid job working in open source software.
[1400.40 --> 1402.42]  And everyone that got one, it's like, how'd you do that?
[1402.46 --> 1403.16]  How'd you convince them?
[1403.18 --> 1403.90]  What are you working on?
[1404.18 --> 1404.34]  Yeah.
[1404.42 --> 1406.20]  And that's been great.
[1406.34 --> 1407.24]  And it's expanded.
[1407.40 --> 1408.96]  And many of us get paid to work in open source.
[1409.36 --> 1411.58]  But I think there's more models that we could add to it.
[1411.74 --> 1412.00]  Absolutely.
[1412.00 --> 1415.18]  Is there a maintainer dashboard?
[1415.72 --> 1417.46]  Or a place that a maintainer can go?
[1417.78 --> 1422.92]  Or something where they can go see, here's what GitHub Sponsors has available to me.
[1423.44 --> 1427.94]  And I'm thinking like beyond just a place to get educated on how GitHub Sponsors can help
[1427.94 --> 1429.46]  them sustain their project.
[1429.52 --> 1431.70]  Whether it's through donations, through sponsors.
[1431.70 --> 1437.22]  I'm thinking about even there's a lot of, I guess, SaaS companies, service dev tooling
[1437.22 --> 1441.24]  that give away their tool for free to open source contributors or to maintainers.
[1442.12 --> 1445.94]  And like, is there a dashboard to go on and say, okay, I can go get Century for free because
[1445.94 --> 1446.90]  I'm in open source.
[1446.98 --> 1452.12]  Or there's XYZ program where they may be spending their dollars on this stuff and they could be
[1452.12 --> 1452.86]  getting it for free.
[1452.94 --> 1457.48]  Like some way to say, here's my access to the maintainer kingdom that GitHub Sponsors has
[1457.48 --> 1458.32]  orchestrated for me.
[1458.62 --> 1460.24]  A dashboard that says I can do sponsors.
[1460.34 --> 1461.36]  I can get money from here.
[1461.36 --> 1462.24]  I can get support there.
[1462.32 --> 1463.80]  I can get cohorts here.
[1463.84 --> 1465.76]  I can learn about Accelerator here.
[1466.00 --> 1467.06]  Is there a place for that?
[1467.82 --> 1473.62]  So there is a, you can go read about GitHub Sponsors and maintainers and GitHub Funds now.
[1473.82 --> 1477.88]  We don't offer maintainers free software, but if you are a student interested in open source
[1477.88 --> 1481.66]  software and you sign up for GitHub Education, there's a whole student pack of free software
[1481.66 --> 1482.36]  that you can get.
[1483.30 --> 1488.58]  There's a repo that you can find, something along the lines of free stuff.
[1489.08 --> 1490.68]  Yeah, it's like free for open source.
[1490.68 --> 1491.32]  Awesome.
[1491.64 --> 1492.70]  It's an awesome list.
[1493.08 --> 1494.00]  It is an awesome list.
[1494.00 --> 1494.80]  And it's just community maintained.
[1495.16 --> 1499.34]  And it's a list of sentries and bit buckets.
[1499.54 --> 1500.00]  I just made that.
[1500.20 --> 1501.62]  I don't know about, is bit buckets still out there?
[1502.16 --> 1502.56]  Yeah.
[1502.88 --> 1503.48]  Other things.
[1503.64 --> 1505.86]  Things that have a free plan for open source maintainers.
[1505.86 --> 1508.40]  And that would be one place people could go.
[1508.58 --> 1510.16]  But just throwing that in there.
[1510.82 --> 1514.64]  Well, to me, it seems like you will have the great opportunity to connect dots.
[1515.36 --> 1516.24]  The dots are on GitHub.
[1516.56 --> 1517.36]  That's in a repo.
[1518.14 --> 1518.24]  Right?
[1518.24 --> 1519.94]  It's in disparate places.
[1520.36 --> 1522.50]  We're always looking for new ideas.
[1522.50 --> 1522.52]  We're always looking for new ideas.
[1522.52 --> 1523.12]  Bring it together.
[1523.40 --> 1524.36]  A maintainer dashboard.
[1524.74 --> 1526.26]  That needs to be your next big thing.
[1526.66 --> 1530.02]  Where can I go as a maintainer to find out what's available to me to sustain?
[1530.84 --> 1533.66]  Funding, people, free services.
[1534.96 --> 1535.54]  I don't know.
[1535.90 --> 1540.50]  So when you say maintainer dashboard, what I always think about is when I talk to maintainers,
[1540.56 --> 1543.10]  they tell me they're not asking what they get for free.
[1543.10 --> 1546.12]  What they're asking is, how do I know who contributes to my projects?
[1546.24 --> 1548.98]  And how do I know who this person is?
[1548.98 --> 1550.76]  And the last time they were active.
[1551.30 --> 1555.90]  And did they submit this code on behalf of GitHub or Microsoft?
[1556.28 --> 1557.94]  Or are they an individual?
[1558.46 --> 1558.70]  Right.
[1558.70 --> 1562.56]  That would definitely be a good thing to put in that dashboard, too.
[1563.62 --> 1564.24]  A lot of things.
[1564.48 --> 1565.18]  A lot of things.
[1565.34 --> 1566.46]  Well, isn't...
[1566.46 --> 1567.24]  We could create a project.
[1567.58 --> 1567.80]  Yeah.
[1568.38 --> 1570.22]  There's kind of two sides to an open source project, though.
[1570.24 --> 1573.56]  There's the running of it and the creating of the software and managing the community,
[1574.12 --> 1581.46]  potentially finding contributors, or identifying three-time contributors who may get an opportunity
[1581.46 --> 1584.90]  to become a full-time or core team member, whatever it might be.
[1584.90 --> 1590.38]  And then the somewhat lesser-known business side of it, where it's not really the business
[1590.38 --> 1592.48]  side, but it's not development.
[1593.04 --> 1593.12]  Right?
[1593.20 --> 1595.78]  It's more admin-type stuff.
[1596.04 --> 1599.68]  That's what I think this dashboard should maybe have, is where it's like, as an admin
[1599.68 --> 1602.82]  of this project, what's available to me to sustain this thing?
[1602.82 --> 1604.80]  Not only just that, but those things, too.
[1605.24 --> 1611.14]  That, and I think we need to make sure developers and maintainers have tools to do their job
[1611.14 --> 1617.22]  well and to get funding, whether it's through Accelerator or GitHub Fund or sponsors, in a
[1617.22 --> 1620.80]  way that doesn't require them to become marketing and social media experts.
[1621.46 --> 1621.70]  Yeah.
[1621.70 --> 1624.28]  I kind of feel this way about all small businesses, not just software.
[1624.48 --> 1624.76]  Right.
[1624.88 --> 1629.26]  If you have a really awesome hairdresser or massage therapist, should they have to become
[1629.26 --> 1630.54]  business experts as well?
[1630.70 --> 1632.20]  In our current model, they do.
[1632.92 --> 1633.08]  Yeah.
[1633.86 --> 1635.24]  Same thing with writing code, right?
[1635.32 --> 1639.82]  How do we, for the open source software developer community, how do we help them be successful
[1639.82 --> 1643.68]  businesses, in a sense, without having to go be marketing people?
[1643.90 --> 1644.00]  Yeah.
[1644.18 --> 1644.52]  Right.
[1644.90 --> 1645.30]  Precisely.
[1645.30 --> 1650.18]  To a certain extent, that's being built through the dependency graph, right?
[1650.22 --> 1651.34]  So you have the distribution.
[1652.24 --> 1655.22]  Of course, there's different kinds of open source, but let's just talk about libraries,
[1655.74 --> 1655.98]  right?
[1656.04 --> 1662.24]  Where I write a library, maybe it's really fast JSON parsing, and everybody starts using
[1662.24 --> 1662.48]  it.
[1662.56 --> 1663.98]  Now I'm in their dependency graph.
[1664.78 --> 1669.36]  And now when these companies come to GitHub sponsors, and they say, we got 300 grand for
[1669.36 --> 1671.78]  the year, here's the invoice, right?
[1671.86 --> 1674.28]  It goes into my, I'm sure I get a wallet or something.
[1674.28 --> 1678.16]  I got a stash of fake money there that represents the money that I put there.
[1678.54 --> 1682.40]  And now I can divvy that out, and you're showing them like, okay, you're using this project.
[1682.52 --> 1685.68]  That project's using super fast JSON library by Jared.
[1686.38 --> 1687.78]  He's available on GitHub sponsors.
[1688.00 --> 1689.92]  And so trickle down in that way, right?
[1690.00 --> 1691.08]  Like, that's what you're trying to build.
[1691.22 --> 1693.34]  Or do you guys, is that there today?
[1693.54 --> 1694.40]  Like, can you do that today?
[1694.88 --> 1695.16]  Yes.
[1695.44 --> 1698.10]  It's not as simple as just clicking a button, but you can do it.
[1698.26 --> 1699.06]  You can see it at least.
[1699.20 --> 1699.72]  And that's the goal.
[1699.72 --> 1703.40]  Like, you as a creator should get some kind of compensation for the thing you created
[1703.40 --> 1705.40]  that is now powering businesses around the world.
[1705.56 --> 1705.92]  Exactly.
[1706.08 --> 1708.36]  So all these businesses, maybe they don't rely directly on me.
[1708.48 --> 1710.80]  They rely on this framework that uses me.
[1711.92 --> 1715.04]  And the framework gets, you know, 10 bucks.
[1715.10 --> 1716.62]  And for every 10 bucks they get, I get a buck.
[1716.88 --> 1717.08]  Yep.
[1717.18 --> 1717.90]  Or whatever it is.
[1718.58 --> 1720.54]  Or maybe you get 10 cents if they use 100 libraries.
[1720.88 --> 1723.78]  But once a thousand companies use it, that adds up.
[1723.92 --> 1724.14]  Right.
[1724.14 --> 1728.18]  And so now you have distribution of your software, but you also have distribution of your sponsorship
[1728.18 --> 1730.18]  along that same graph.
[1730.76 --> 1735.28]  I think that's one way to do it without being like, hey, I'm on Twitter talking about my
[1735.28 --> 1736.64]  fast JSON parsing library.
[1736.96 --> 1739.38]  We do have someone who shames people on Twitter.
[1739.78 --> 1740.98]  They talk about using his product.
[1741.12 --> 1742.78]  He goes and says, oh, that's great.
[1742.92 --> 1744.46]  Would you like to contribute on GitHub sponsors?
[1744.90 --> 1746.62]  And he's actually pretty successful at it.
[1746.78 --> 1747.04]  Okay.
[1747.26 --> 1748.04]  So there's a hack.
[1748.20 --> 1748.52]  Yeah.
[1748.58 --> 1749.12]  I like that.
[1749.12 --> 1751.22]  But if you don't want to be that guy or gal.
[1751.98 --> 1754.10]  You can just write a bot so you don't have to deal with it every time.
[1754.48 --> 1755.20]  There you go.
[1755.80 --> 1756.94]  There's always a bot for that.
[1756.94 --> 1757.32]  Yeah.
[1757.44 --> 1757.84]  Bot Adam.
[1758.92 --> 1762.62]  Maybe one more facet is how do maintainers get paid?
[1762.78 --> 1767.86]  How easy is it for them to extract the dollars from the donation from GitHub sponsors?
[1768.48 --> 1770.02]  It's a Stripe payment in the background.
[1770.02 --> 1770.24]  Okay.
[1771.04 --> 1773.00]  So they have to maintain a Stripe account.
[1773.14 --> 1773.28]  Yep.
[1774.12 --> 1775.42]  Deal with taxes, of course.
[1775.94 --> 1776.48]  Is that a struggle?
[1777.34 --> 1779.72]  Is it a struggle that you all care about, I suppose?
[1780.46 --> 1781.70]  I'm sure you do, but like.
[1781.74 --> 1783.00]  We're always looking for.
[1783.00 --> 1787.46]  We're always listening to people and asking them how they'd like to receive money.
[1787.58 --> 1788.44]  So right now it's Stripe.
[1788.78 --> 1792.20]  Seems to work for a majority of the people, but the majority of the people that we're listening
[1792.20 --> 1793.30]  to are the people that have signed up.
[1793.46 --> 1793.70]  Sure.
[1793.80 --> 1798.32]  We're also looking at partnerships with other funding methods to see what else we can add.
[1798.66 --> 1798.88]  Yeah.
[1799.62 --> 1800.08]  Well, cool.
[1800.52 --> 1801.90]  Big problems to solve, Stormy.
[1802.24 --> 1802.52]  Fun.
[1802.94 --> 1803.56]  Fun problems.
[1803.68 --> 1803.88]  Yeah.
[1804.56 --> 1805.08]  Thank you.
[1805.26 --> 1805.60]  Yeah, thanks.
[1805.60 --> 1806.84]  Thank you.
[1821.78 --> 1826.60]  So in the sponsor of Minnesota, here in the breaks, I'm here with Tom Hu, dev advocate
[1826.60 --> 1828.76]  at Sentry on the CodeCov team.
[1828.76 --> 1832.08]  So Tom, tell me about Sentry's acquisition of CodeCov.
[1832.40 --> 1835.62]  And in particular, how is this improving the Sentry platform?
[1836.14 --> 1840.76]  When I think about the acquisition, when I think about how does Sentry use CodeCov, or
[1840.76 --> 1842.90]  conversely, how does CodeCov use Sentry?
[1843.14 --> 1846.26]  Like I think of CodeCov and I think of the time of deploying.
[1846.54 --> 1849.44]  When you're a software developer, you have your listicle, you write your code, you test
[1849.44 --> 1853.20]  your code, you deploy, and then your code goes into production and then you sort of fix
[1853.20 --> 1853.66]  the bugs.
[1853.66 --> 1857.26]  And I sort of think of that split in time as like when you actually do that deploy.
[1858.00 --> 1861.10]  Now, where CodeCov is really useful is before deploy time.
[1861.40 --> 1862.96]  It's when you are developing your code.
[1863.14 --> 1865.62]  It's when you're saying, hey, like, I want to make sure this is going to work.
[1865.84 --> 1867.90]  I want to make sure that I have as few bugs as possible.
[1868.24 --> 1871.64]  I want to make sure that I've thought of all the errors and all the edge cases and whatnot.
[1872.18 --> 1874.24]  And Sentry is the flip side of that.
[1874.48 --> 1877.20]  It says, hey, what happens when you hit production, right?
[1877.22 --> 1880.86]  When you have a bug and you need to understand what's happening in that bug, you need to understand
[1880.86 --> 1881.80]  the context around it.
[1881.80 --> 1885.06]  You need to understand where it's happening, what the stack trace looks like, what other
[1885.06 --> 1888.82]  local variables exist at that time so that you can debug that.
[1889.18 --> 1891.50]  And hopefully you don't see that error case again.
[1891.76 --> 1896.18]  When I think of like, oh, what can Sentry do with CodeCov or what can CodeCov do for Sentry?
[1896.60 --> 1900.86]  It's sort of taking that entire spectrum of the developer lifecycle of, hey, what can we
[1900.86 --> 1905.26]  do to make sure that you ship the least buggy code that you can?
[1905.66 --> 1910.18]  And when you do come to a bug that is unexpected, you can fix it as quickly as possible, right?
[1910.18 --> 1913.24]  Because, you know, as developers, we want to write good code.
[1913.36 --> 1916.34]  We want to make sure that people can use the code that we've written.
[1916.66 --> 1919.50]  We want to make sure that they're happy with the product, they're happy with the software,
[1919.50 --> 1921.16]  and it works the way that we expect it to.
[1921.52 --> 1926.58]  If we can build a product, you know, the Sentry plus CodeCov thing to make sure that you are
[1926.58 --> 1932.72]  de-risking your code changes and de-risking your software, then, you know, we've hopefully
[1932.72 --> 1935.16]  done the developer community as service.
[1935.16 --> 1938.66]  So, Tom, you say bring your tests and you'll handle the rest.
[1938.76 --> 1939.42]  Break it down for me.
[1939.48 --> 1942.90]  How does a team get started with CodeCov?
[1943.36 --> 1947.58]  You know, what you bring to the table is like testing and you bring your coverage reports.
[1948.00 --> 1951.88]  And what CodeCov does is we say, hey, give us your coverage reports, give us access to
[1951.88 --> 1956.40]  your code base so that we can, you know, overlay code coverage on top of it and give us access
[1956.40 --> 1957.16]  to your CICD.
[1957.16 --> 1963.24]  And so with those things, what we do and what CodeCov is really powerful at is that it's
[1963.24 --> 1965.28]  not just, hey, like this is your code coverage number.
[1965.68 --> 1970.82]  It's, hey, here's a code coverage number and your viewer also knows and other parts of your
[1970.82 --> 1972.20]  organization know as well.
[1972.32 --> 1975.72]  So it's not just you dealing with code coverage and saying, I don't really know what to do
[1975.72 --> 1976.18]  with this.
[1976.46 --> 1980.88]  Because we take your code coverage, we analyze it and we throw it back to you into your
[1980.88 --> 1981.64]  developer workflow.
[1982.20 --> 1985.16]  And by developer workflow, I mean your pull request, your merge request.
[1985.16 --> 1989.58]  And we give it to you as a comment so that you can see, oh, great, this was my code coverage
[1989.58 --> 1989.96]  change.
[1990.34 --> 1993.94]  But not only do you see this sort of information, but your viewer also sees it.
[1994.06 --> 1997.00]  And they can tell, oh, great, you've tested your code or you haven't tested your code.
[1997.44 --> 2001.84]  And we also give you a status check, which says, hey, like you've met whatever your team's
[2001.84 --> 2005.66]  decision on what your code coverage should be, or you haven't met that goal, whatever it
[2005.66 --> 2006.26]  happens to be.
[2006.54 --> 2011.30]  And so CodeCov is particularly powerful in making sure that code coverage is not just a thing
[2011.30 --> 2015.12]  that you're doing on your own island as a developer, but that your entire team
[2015.12 --> 2017.28]  can get involved with and can make decisions.
[2017.90 --> 2018.10]  Very cool.
[2018.16 --> 2018.66]  Thank you, Tom.
[2018.80 --> 2022.04]  So, hey, listeners, head to Sentry and check them out.
[2022.18 --> 2025.76]  Sentry.io and use our code changelog.
[2026.10 --> 2031.82]  So the cool thing is, is our listeners, you get the team plan for free for three months.
[2032.10 --> 2035.38]  Not one month, not two months, three months.
[2035.38 --> 2035.86]  Yes.
[2035.86 --> 2036.10]  Yes.
[2036.42 --> 2038.10]  The team plan for free for three months.
[2038.32 --> 2039.38]  Use the code changelog.
[2039.46 --> 2042.22]  Again, Sentry.io.
[2042.48 --> 2045.90]  That's S-E-N-T-R-Y.io.
[2046.28 --> 2047.74]  And use the code changelog.
[2047.86 --> 2050.68]  Also check out our friends over at CodeCov.
[2050.80 --> 2053.02]  That's CodeCov.io.
[2053.36 --> 2055.96]  Like code coverage, but just shortened to CodeCov.
[2056.44 --> 2057.60]  CodeCov.io.
[2057.60 --> 2058.56]  Enjoy.
[2058.56 --> 2058.72]  Enjoy.
[2058.72 --> 2058.78]  Enjoy.
[2058.78 --> 2058.82]  Enjoy.
[2058.82 --> 2058.84]  Enjoy.
[2058.84 --> 2059.32]  Enjoy.
[2059.32 --> 2059.72]  Enjoy.
[2059.72 --> 2060.72]  Enjoy.
[2060.72 --> 2062.72]  Enjoy.
[2062.72 --> 2063.72]  Enjoy.
[2063.72 --> 2082.68]  So we're here with Dawn Foster from VMware.
[2082.94 --> 2083.32]  How are you doing?
[2083.70 --> 2084.42]  I'm good, thanks.
[2084.50 --> 2085.10]  Thanks for having me.
[2085.46 --> 2088.34]  What do you enjoy about conferences like these?
[2088.44 --> 2089.18]  What's your favorite part?
[2089.56 --> 2090.34]  Oh, my God, it's the people.
[2090.34 --> 2093.74]  So you get to run into people that you've known for years.
[2093.92 --> 2095.28]  You get to meet new people.
[2095.50 --> 2095.72]  Yeah.
[2095.94 --> 2097.08]  You get to reconnect with people.
[2097.16 --> 2098.32]  You get to have interesting conversations.
[2098.92 --> 2103.62]  And, you know, when we were all virtual through, you know, the pandemic and lockdowns and things,
[2103.66 --> 2104.56]  it just wasn't the same.
[2104.56 --> 2105.20]  It wasn't the same.
[2105.66 --> 2108.14]  Because you don't get those serendipitous conversations, right?
[2108.14 --> 2108.50]  That's right.
[2108.50 --> 2109.16]  You don't.
[2109.22 --> 2112.66]  You know, Kara's not going to, like, drag me across the room to do this podcast.
[2112.76 --> 2113.04]  Right.
[2113.04 --> 2114.08]  On a virtual environment, right?
[2114.08 --> 2114.94]  I never went to drag.
[2115.12 --> 2115.68]  That's not quite.
[2115.70 --> 2116.32]  But did she drag you?
[2116.34 --> 2116.92]  No, she didn't drag me.
[2116.92 --> 2119.86]  She very kindly asked me if I would like to do one right now.
[2119.86 --> 2120.86]  You were a willing party.
[2121.82 --> 2126.56]  So Kara was telling me that your PhD had something to do with the Linux kernel.
[2127.38 --> 2129.46]  And I was like, tell me more.
[2129.60 --> 2130.64]  And that's all I got so far.
[2130.72 --> 2131.60]  So can you tell me more?
[2132.16 --> 2132.76]  Yeah, absolutely.
[2133.02 --> 2136.92]  So a few years ago, I decided for my midlife crisis, I was going to move to London on a
[2136.92 --> 2139.02]  student visa and get a PhD.
[2139.02 --> 2144.00]  And so I found a university I liked, the University of Greenwich in London.
[2144.00 --> 2146.68]  And they had a center for business network analysis.
[2147.50 --> 2151.96]  And I pitched them an idea to do network analysis and study the people networks within the Linux
[2151.96 --> 2152.24]  kernel.
[2152.72 --> 2153.66]  They said yes.
[2153.86 --> 2154.70]  They let me do it.
[2155.20 --> 2159.36]  And so I spent three and a half years studying the Linux kernel.
[2159.58 --> 2161.22]  And so I gathered a bunch of data.
[2161.24 --> 2161.98]  Three and a half years.
[2162.06 --> 2162.42]  Yeah, yeah.
[2162.46 --> 2163.58]  Because that's what a PhD takes.
[2163.78 --> 2164.36]  Okay, wow.
[2164.64 --> 2165.56]  Or it can take more.
[2165.66 --> 2166.52]  But I did it in three and a half.
[2166.52 --> 2170.16]  But yeah, so I looked at collaboration within the Linux kernel.
[2170.54 --> 2173.36]  I looked mostly at mailing lists because that's how the Linux kernel works.
[2173.54 --> 2174.86]  Like they don't use GitHub.
[2175.06 --> 2175.86]  It's not pull requests.
[2176.04 --> 2178.88]  It's patch diffs mailed back and forth on the mailing list.
[2179.64 --> 2181.48]  So yeah, so I looked at mailing list data.
[2181.78 --> 2184.16]  I looked at some source code data as well.
[2184.24 --> 2185.80]  But I just did a whole bunch of analysis.
[2186.16 --> 2186.74]  What'd you learn?
[2187.62 --> 2188.76]  So it's interesting.
[2188.90 --> 2189.22]  You talked.
[2189.32 --> 2191.32]  I also did interviews with some of the kernel developers.
[2192.26 --> 2196.34]  And one of the things that they'll tell you is that time zones don't matter.
[2196.34 --> 2198.12]  It doesn't matter where you're located or on the world.
[2199.70 --> 2200.92]  It just doesn't matter.
[2201.42 --> 2202.30]  And it turns out that's true.
[2202.46 --> 2205.18]  Like that's what the data showed was that it didn't, I didn't collaborate.
[2205.30 --> 2207.52]  I wouldn't collaborate more with you because we were in the same time zone.
[2208.70 --> 2211.30]  You, it just, for whatever reason, it wasn't significant.
[2212.70 --> 2213.62]  And it was interesting.
[2213.74 --> 2217.98]  Also, one of the things I found interesting is that two people who work at the same organization
[2217.98 --> 2222.04]  were also more likely to interact with each other on the mailing lists.
[2222.04 --> 2226.46]  Which, which I found, I was surprised by that.
[2226.70 --> 2228.66]  But, but I really like it.
[2228.72 --> 2233.42]  So I like that companies are interacting in public on the mailing list instead of just,
[2233.52 --> 2236.66]  you know, sending each other Slack messages, walking over to somebody's desk and talking
[2236.66 --> 2237.20]  about something.
[2237.48 --> 2237.60]  Yeah.
[2237.60 --> 2239.74]  So I found that, I found that kind of interesting.
[2240.06 --> 2243.40]  I wonder if there's something about public mailing lists.
[2243.50 --> 2248.98]  I guess maybe they, they allow this research to even take place because a lot of other forms
[2248.98 --> 2253.84]  of communication potentially may have not been reachable by you as an outside analyst, right?
[2254.16 --> 2254.74]  Yeah, exactly.
[2254.98 --> 2257.84]  So, so that's one of the beauties of open source, right?
[2257.86 --> 2260.90]  Is that you, you've got all of the data because it's all, it's all in the public.
[2260.90 --> 2265.64]  I mean, now, so I do some work within the chaos project and, and outside of the chaos
[2265.64 --> 2266.32]  project as well.
[2266.40 --> 2271.32]  But I spent a lot of time in the GitHub API and just, you know, pulling, pulling out data
[2271.32 --> 2275.44]  on open source projects and looking at, looking at what's what and just trying to get a feel
[2275.44 --> 2277.84]  for, for different aspects of the project.
[2279.06 --> 2280.30]  Poking and prodding.
[2280.64 --> 2281.14]  That's so cool.
[2281.18 --> 2281.48]  Poking and prodding.
[2281.68 --> 2281.94]  Yes.
[2282.88 --> 2286.12]  So chaos, this is community health.
[2286.22 --> 2287.02]  Help me out with the rest.
[2287.16 --> 2289.54]  Community health analytics for open source software.
[2289.54 --> 2291.82]  So chaos with two S's.
[2291.92 --> 2292.64]  Two S's.
[2294.08 --> 2294.44]  Chaos.
[2294.78 --> 2295.18]  Chaos.
[2296.24 --> 2296.64]  Yeah.
[2296.74 --> 2299.30]  So we basically, I'll give you an overview of what chaos is.
[2299.46 --> 2302.90]  We, we are a project and we're focused on kind of, kind of two things.
[2302.90 --> 2304.02]  We're focused on metrics.
[2304.02 --> 2308.78]  So defining metrics so that we can be, when we talk about a certain, a certain metric
[2308.78 --> 2311.88]  that we can be consistent about what it is and have a definition that we can point people
[2311.88 --> 2312.10]  to.
[2312.18 --> 2315.88]  And we say, when we're talking about, you know, numbers of lines of code, that's, that's what
[2315.88 --> 2316.34]  this means.
[2316.34 --> 2321.48]  If we're talking about, you know, the bus factor, which is, you know, how many people
[2321.48 --> 2325.46]  you have contributing to a project that we measure that kind of the same, same way.
[2325.70 --> 2328.36]  So we do metrics definitions and then we do software.
[2328.60 --> 2331.48]  So we have two pieces of software within the chaos projects.
[2331.62 --> 2332.84]  We have Augur and Grimoire lab.
[2332.84 --> 2337.76]  And those are both, they're basically software projects that go out and they gather a bunch
[2337.76 --> 2339.74]  of data from various sources.
[2340.06 --> 2346.22]  So GitHub, obviously Slack, other, other things that you can, basically anything with an API
[2346.22 --> 2351.66]  that you can get access to the data from and allow people to analyze that using software.
[2352.20 --> 2352.52]  Very cool.
[2352.52 --> 2358.88]  So do you have some sort of a score or how does it, how do you quantify health?
[2359.58 --> 2360.98]  That is an excellent question.
[2361.28 --> 2361.94]  Thank you.
[2363.64 --> 2365.00]  No, we don't have a score.
[2365.20 --> 2365.36]  Okay.
[2365.48 --> 2368.44]  And I am, I am anti, anti health scores.
[2368.66 --> 2368.86]  Okay.
[2368.96 --> 2373.46]  So what, what I like to look at when I'm looking at project health is I like to look at trends.
[2373.46 --> 2376.80]  So, you know, are you closing more of your pull requests?
[2377.78 --> 2380.64]  Is your pull request backlog getting bigger or smaller?
[2380.98 --> 2386.10]  Are you responding to pull requests and issues more, more quickly or is it taking you more
[2386.10 --> 2386.52]  time?
[2386.64 --> 2391.46]  So I like to look at trends over time and I like to look at metrics in the context of
[2391.46 --> 2397.66]  projects because individual projects have, you know, certain ways of working and certain
[2397.66 --> 2399.46]  things that impact the metrics.
[2399.46 --> 2401.56]  And unless you're part of the project, you don't know.
[2401.56 --> 2408.66]  So, you know, for example, if I work on a project and it's, you know, we're cutting a huge release
[2408.66 --> 2412.52]  that, you know, has a bunch of breaking changes, there's probably going to be some weird things
[2412.52 --> 2413.90]  in the metrics associated with that.
[2414.04 --> 2418.20]  So, you know, pull requests are getting the backlog while you get everything together for
[2418.20 --> 2419.26]  the release, for example.
[2420.18 --> 2425.86]  I was talking to a friend at Google, Sophia Vargas, and she does a lot of analysis on things
[2425.86 --> 2426.92]  like Kubernetes.
[2426.92 --> 2432.34]  And some of the metrics that she was looking at it made just no sense because the way Kubernetes
[2432.34 --> 2434.80]  works is you've got bots that do all the things, right?
[2434.90 --> 2437.58]  So like you have bots that respond to things automatically.
[2437.88 --> 2442.28]  The bots close the issues automatically after a certain amount, you know, they go stale,
[2442.36 --> 2442.94]  they close them.
[2443.32 --> 2446.88]  So there's all this like bot activity that she was looking at data and she's like, this
[2446.88 --> 2447.54]  makes no sense.
[2447.74 --> 2450.38]  And she went and talked to some people and they were like, oh yeah, because that's the
[2450.38 --> 2450.70]  bots.
[2450.90 --> 2451.50]  That's what they do.
[2451.50 --> 2451.86]  Yeah.
[2452.76 --> 2453.66]  It's normal to them.
[2453.78 --> 2457.30]  But unless you understand that, you can't interpret like the, it doesn't tell you anything
[2457.30 --> 2460.34]  about the health of the project unless you understand what's going on within the project.
[2460.66 --> 2460.86]  Yeah.
[2461.34 --> 2464.70]  So it's a hard job then, I guess, to quantify.
[2465.62 --> 2470.18]  And so when you say you like to look at trends, you're basically measuring the health of the
[2470.18 --> 2472.70]  project relative to its past health.
[2474.66 --> 2475.72]  Why is that beneficial?
[2475.72 --> 2482.68]  I guess just to see where they're headed or, um, I guess who, I don't want to say who
[2482.68 --> 2485.10]  cares, but like who's actually, who, who cares?
[2485.78 --> 2491.84]  Who's the person who, or the org or the entity that says, I care about the future health of
[2491.84 --> 2493.14]  this, this project.
[2493.34 --> 2494.94]  Is it foundations?
[2495.28 --> 2496.06]  Is it individuals?
[2496.22 --> 2499.26]  Like I would come to it as an individual and think this is why I'd want to score.
[2499.26 --> 2503.40]  Or it's because like my, my question is, do I want to get involved in this project?
[2503.48 --> 2504.74]  Do I want to use this thing?
[2505.44 --> 2506.64]  How's the health of the community?
[2506.76 --> 2513.42]  You know, I look at the, uh, GitHub pulse tab, the insights, not super useful, but it's
[2513.42 --> 2513.76]  there.
[2513.94 --> 2514.30]  Right.
[2514.34 --> 2518.08]  Cause I'm trying to gauge, is this a dependency that I'm willing to take on perhaps?
[2518.26 --> 2522.76]  So that'd be like one angle into caring about the community health of a project, overall
[2522.76 --> 2523.14]  health.
[2523.54 --> 2528.30]  And so I would like to see like, well, I mean, trends would be useful, but if it's starting
[2528.30 --> 2534.04]  from a really bad place and it's trending up, but it's like still maybe not the nicest
[2534.04 --> 2534.84]  place to hang out.
[2534.84 --> 2535.20]  Yeah.
[2536.52 --> 2537.60]  Long winded question.
[2538.28 --> 2540.78]  Like who are the users of your information?
[2540.78 --> 2541.22]  I guess.
[2541.26 --> 2541.96]  Who's the end user?
[2542.68 --> 2542.84]  Yeah.
[2542.90 --> 2543.66]  So it depends.
[2543.82 --> 2546.78]  I think, I think all of those people are end users of metrics.
[2546.78 --> 2547.20]  Right.
[2547.20 --> 2552.44]  And so, so part of the reason that I look at trends is because, um, from, let's just
[2552.44 --> 2553.86]  talk about from a VMware perspective, right?
[2553.86 --> 2554.82]  From a company perspective.
[2554.98 --> 2555.18]  Sure.
[2555.30 --> 2560.66]  I want our maintainers to look at the projects and use the project health metrics to decide
[2560.66 --> 2562.56]  where they need to improve.
[2563.12 --> 2567.96]  So, you know, if they're responding to pull requests really quickly, um, then that's,
[2568.00 --> 2568.42]  that's great.
[2568.56 --> 2571.82]  But if they're never closing any of those pull requests, maybe that's where they need
[2571.82 --> 2572.26]  to focus.
[2572.26 --> 2575.06]  So it gives them, it gives them a place to focus.
[2575.20 --> 2575.50]  Sure.
[2575.50 --> 2579.68]  And the reason I like to focus on trends is because what I don't want is somebody getting
[2579.68 --> 2583.82]  all hung up because they're, you know, their number is going down, but maybe it's going
[2583.82 --> 2587.16]  down less quickly or it's, it's improving in some way.
[2587.24 --> 2590.60]  So they're already, they've already made some improvement and I don't want people getting
[2590.60 --> 2595.08]  hung up on just like the number because the numbers less than it was last month or whatever.
[2595.30 --> 2597.78]  I want them to think about whether they're already improving.
[2597.94 --> 2599.84]  Is there something else they can do to improve?
[2599.84 --> 2604.04]  And then I think, you know, when you're new to a community and you're trying to decide
[2604.04 --> 2607.34]  whether you want to participate in a community, I think those are a whole different set of
[2607.34 --> 2607.92]  health metrics.
[2608.12 --> 2612.32]  Like, yeah, I mean, I think that's things like, is anybody actually using this thing?
[2612.56 --> 2612.74]  Right.
[2612.78 --> 2614.42]  I don't want to contribute to something nobody uses.
[2614.76 --> 2614.86]  Right.
[2615.14 --> 2618.82]  Um, are there lots of other people contributing to all of those contributors work at the same
[2618.82 --> 2620.52]  company and I don't work for that company?
[2620.54 --> 2622.18]  Am I even going to be welcome in this project?
[2622.44 --> 2626.40]  So I think there's a lot of things that you look at depending on, on what your goals are as
[2626.40 --> 2629.70]  a contributor and depending on what kind of project you want to contribute to.
[2629.84 --> 2631.08]  How do you represent this data?
[2631.24 --> 2636.60]  Is it on a website and I can go to like a certain domain and a certain org name and a
[2636.60 --> 2637.42]  certain project name?
[2637.56 --> 2640.16]  Like, is it like GitHub URL structure to get to this data?
[2640.52 --> 2644.30]  How do you, how can I go and find my projects that I'm interested in as data?
[2644.40 --> 2645.38]  How can I find that information?
[2646.04 --> 2646.54]  Um, yeah.
[2646.60 --> 2650.38]  So you, you kind of have to, if you're talking about it from a chaos perspective, you kind
[2650.38 --> 2654.36]  of have to use one of the tools and, and load your project's data into it.
[2654.36 --> 2656.72]  Um, and then you can, then you can access it.
[2656.72 --> 2657.10]  I guess better questions.
[2657.18 --> 2657.72]  How does it work?
[2658.24 --> 2659.16]  How do I use chaos?
[2659.66 --> 2659.82]  Yeah.
[2659.86 --> 2660.02]  Yeah.
[2660.10 --> 2661.76]  So, so we have two tools.
[2661.84 --> 2666.20]  So we have, we have Augur, which I use within, within VMware myself.
[2666.76 --> 2670.86]  Um, so the way Augur works is it's, it's a, on the backend, it's a Postgres database.
[2671.32 --> 2675.12]  So basically what it does is it pulls, it has a bunch of workers that pull data from
[2675.12 --> 2678.80]  GitHub, for example, and puts it in a very nicely structured Postgres database.
[2678.80 --> 2681.86]  And then there's also, they're doing some work on the front end.
[2681.96 --> 2683.96]  So they're kind of making some changes in the front end.
[2684.02 --> 2685.70]  It's a little bit less, less mature.
[2686.08 --> 2689.90]  But the reason I picked Augur was because there were four metrics that I wanted to measure
[2689.90 --> 2691.60]  that I wanted our maintainers to look at.
[2691.80 --> 2695.76]  And so because it's just a Postgres database in the backend, I can just write a whole bunch
[2695.76 --> 2698.26]  of Python scripts that generate the four charts that I want.
[2698.66 --> 2700.20]  And then we display those internally.
[2700.20 --> 2702.86]  We have a little internal dashboard that we use for that.
[2703.16 --> 2703.30]  Yeah.
[2703.74 --> 2706.10]  And then we also, we also use the Paturgia.
[2706.86 --> 2707.46]  Say what?
[2707.46 --> 2712.56]  So it's Grimoire Lab is one of the, and there's a company called Paturgia that does a lot
[2712.56 --> 2713.58]  of the work on Grimoire Lab.
[2713.76 --> 2713.90]  Okay.
[2713.92 --> 2715.14]  So that's the other piece of software.
[2715.58 --> 2718.22]  And it's, it uses the elk stack.
[2718.34 --> 2725.08]  So basically Elasticsearch, although they're migrating to OpenSearch and a fork of Kibiter.
[2725.52 --> 2730.14]  So it's, it's more, more of that style.
[2730.20 --> 2731.24]  So it's not a relational database.
[2731.24 --> 2733.22]  It's like a, you know, an elastic database.
[2733.42 --> 2737.10]  So you, you can run, you can run queries, but it's got like really big dashboards.
[2737.46 --> 2738.48]  That people can use.
[2739.04 --> 2743.04]  So that I think is great for community managers who really want to dig in on their individual
[2743.04 --> 2745.32]  project and want to know every little bit about it.
[2745.56 --> 2748.36]  Because the dashboards have all this, all this stuff already in them.
[2748.36 --> 2750.40]  And then you can write custom queries around it.
[2750.40 --> 2754.90]  So like Augur is more powerful if you want to write like Postgres database queries and display
[2754.90 --> 2755.52]  stuff yourself.
[2755.88 --> 2758.40]  Although they are working on the front end and it's looking really, really cool.
[2758.56 --> 2761.60]  So like, don't, I don't want to diss the Augur front end because there's some awesome stuff
[2761.60 --> 2761.90]  happening.
[2762.58 --> 2767.26]  And then the other one has like a more, more robust dashboard, but it's, it's confusing for
[2767.26 --> 2767.68]  a lot of people.
[2767.68 --> 2770.78]  Like they don't know how to write those queries because they're not relational database queries.
[2770.92 --> 2771.50]  They're different.
[2771.50 --> 2774.00]  Um, so it just kind of depends on what you want.
[2774.36 --> 2776.28]  How did you get to those four metrics?
[2776.50 --> 2778.46]  Why are those the ones that are important to your team?
[2778.94 --> 2779.34]  Yeah.
[2779.48 --> 2780.26]  So I picked them.
[2780.48 --> 2782.24]  Recount them for us and then why?
[2782.78 --> 2783.12]  Yeah, sure.
[2783.66 --> 2784.06]  Yeah.
[2784.12 --> 2790.32]  So the four metrics are response time for, uh, I picked pull requests, uh, response time
[2790.32 --> 2790.96]  for pull requests.
[2791.30 --> 2796.56]  And so our guideline internally is that if someone submits a pull request, we should have a human
[2796.56 --> 2798.08]  respond to it within two business days.
[2798.08 --> 2802.34]  So I exclude the bots and then I look at how many business days it took us to respond.
[2802.80 --> 2804.30]  And then I chart that over time.
[2805.10 --> 2814.60]  Um, and then I look at, um, change request closure ratio, which is, is basically, um, in
[2814.60 --> 2820.14]  a given month, there are a total of a hundred open pull requests during that month.
[2820.28 --> 2821.94]  Did you close 90 of them?
[2822.06 --> 2823.42]  Did you close 50 of them?
[2823.52 --> 2827.54]  And how big is the gap between the number of pull requests and the number of pull requests
[2827.54 --> 2827.88]  you close?
[2827.88 --> 2832.22]  So this is kind of the pull request backlog and whether you're keeping up with pull requests.
[2832.60 --> 2837.90]  So, so response time is good because like new, new contributors want a response to their
[2837.90 --> 2838.36]  contribution.
[2838.64 --> 2840.18]  Everybody wants a response to their contribution.
[2840.84 --> 2845.00]  Um, the pull request backlog is good because it shows that people are either merging pull
[2845.00 --> 2846.74]  requests or closing them without merge.
[2846.74 --> 2846.84]  It's like throughput.
[2846.84 --> 2847.68]  Yeah.
[2847.68 --> 2847.74]  Yeah.
[2848.26 --> 2850.32]  Because you don't want a huge backlog of pull requests.
[2850.52 --> 2851.62]  I look at release frequency.
[2851.62 --> 2857.50]  So I want to make sure that the, when they release bug fixes and security fixes that they actually
[2857.50 --> 2859.12]  land in a release in a timely manner.
[2859.12 --> 2862.46]  So those are not just like big releases, but like individual point releases.
[2862.46 --> 2867.52]  And then I also look at contributor risk, which is kind of a bus factor type metric.
[2867.52 --> 2873.38]  So I look at, does a project, and these are VMware owned projects that we run these metrics on.
[2873.38 --> 2880.24]  Um, I look at, you know, are there three people who are contributing 50% of the contributions to the project?
[2880.24 --> 2885.28]  Or is it one person who's contributing like 98% in which case that's, that's not good.
[2885.36 --> 2895.44]  But if you have a large number of people who are contributing across the project, then if one person left the company or retired or decided they didn't want to do it anymore, then the project can more easily continue.
[2895.84 --> 2900.70]  So I picked those because I thought it was a representative sample of, of things that a lot of people care about.
[2900.84 --> 2906.00]  And then what I want the projects to do and the maintainers to do is then drill down and have other metrics.
[2906.00 --> 2910.20]  So like I said, we have a team using the Grimoire Lab tools for their metrics.
[2910.80 --> 2917.48]  And then we have other teams that are doing like, you know, custom stuff out of the GitHub API, for example, to measure other things that they want to care about.
[2917.82 --> 2919.38]  What metrics hit your cutting room floor?
[2919.74 --> 2922.56]  What metrics was important, but didn't make the cut?
[2923.14 --> 2923.70]  That's a good question.
[2923.78 --> 2925.26]  I didn't really, I didn't really approach it that way.
[2925.32 --> 2927.24]  I just picked the four that I thought were important.
[2927.64 --> 2928.52]  So you just only chose four.
[2928.64 --> 2929.22]  I chose four.
[2929.50 --> 2930.52]  Drill was the first time.
[2930.52 --> 2931.04]  No requirements.
[2931.28 --> 2932.72]  I am, I am, I'm focused.
[2932.96 --> 2933.20]  Okay.
[2933.82 --> 2934.10]  Focused.
[2934.10 --> 2939.50]  It seems like the importance of those metrics is, trying to paraphrase, contributor.
[2939.78 --> 2949.28]  You want, if I give a pull request, I want as a human who spent my time and effort to give you the project some value, whether it's X or Y, some sort of feedback.
[2949.84 --> 2959.76]  But the other one where I think you were talking about the pull request backlog, and you mentioned Jared throughput, I got to imagine that tells you, should we increase our team size?
[2959.76 --> 2961.08]  Or should we decrease?
[2961.14 --> 2962.10]  Because we're just closing them fast.
[2962.18 --> 2964.18]  Maybe we have, maybe we're just fast.
[2964.32 --> 2965.72]  Or, hey, we're slow this time.
[2965.90 --> 2967.36]  Or three months consecutively.
[2967.54 --> 2968.82]  Do we need to add a team member?
[2968.92 --> 2971.80]  Should we incubate a new core team member, et cetera?
[2971.86 --> 2972.80]  Is that kind of how you look at it?
[2972.84 --> 2974.96]  It's like, it helps you identify risk.
[2975.00 --> 2977.40]  It helps you communicate with the community really well.
[2977.40 --> 2981.14]  But it also helps you grow or shrink the team as necessary based upon this feedback.
[2981.14 --> 2984.14]  And do you recruit more contributors from outside the company?
[2984.36 --> 2988.24]  So do you get more people involved in the project because you're not keeping up with the contributions?
[2989.12 --> 2991.56]  How well is this idea used by other projects?
[2991.70 --> 2994.50]  This seems to be like a very good idea.
[2994.50 --> 3002.78]  And how many people are using Chaos and Augur to kind of dig in like you have to showcase his health?
[3003.38 --> 3005.16]  So lots of companies, actually.
[3006.12 --> 3013.88]  So I think lots of the big companies that have open source program offices have at one time or another used some of the Chaos tools.
[3017.00 --> 3020.70]  Yeah, I hate to name names because I can't remember which ones I can talk about, which ones I can't.
[3020.70 --> 3027.68]  But most of the big open source program offices at the big companies have used the Chaos tools and are involved in the Chaos Project.
[3027.86 --> 3033.38]  So if you look at the people who are coming to meetings and being involved in the Chaos Project right now,
[3033.76 --> 3040.16]  we see people from Bloomberg and Microsoft and Google and Red Hat and all of the big tech companies.
[3040.92 --> 3043.18]  More specifically, why did you not score?
[3044.02 --> 3048.96]  Like, why did you not establish maladaptive, healthy, a score of 50?
[3048.96 --> 3050.96]  Like, why the pushback against the scoring?
[3051.08 --> 3052.62]  Like, is it too concrete?
[3052.94 --> 3056.98]  Do you need to be a bit more ambiguous in terms of, like, that true health?
[3057.12 --> 3058.74]  No, it's because every project's different.
[3058.94 --> 3059.10]  Okay.
[3059.18 --> 3069.02]  So how do you compare a Kubernetes and give that, like, any algorithm that you could put together that would score something like Kubernetes
[3069.02 --> 3075.70]  and then compare it to a project that has, like, two contributors and, you know, 10 pull requests a month?
[3076.42 --> 3083.72]  Like, any metric that you could score would give you wildly different results because those are very different sizes of projects.
[3083.94 --> 3085.10]  And they have different automation.
[3085.38 --> 3086.60]  They have different, like, release schedules.
[3086.74 --> 3087.74]  Every project's different.
[3087.74 --> 3092.96]  So I want the project themselves to think about what do these metrics mean to me for my project
[3092.96 --> 3096.86]  and interpret it in light of the other stuff that's going on with their project.
[3097.26 --> 3099.12]  Like, you know, like a release window, for example.
[3099.76 --> 3104.92]  Or, you know, KubeCon comes up and you see a drop across the board on, like, CNCF projects,
[3105.00 --> 3107.50]  like the week leading up to KubeCon where everyone's writing their talks.
[3108.20 --> 3111.04]  And during KubeCon and then, you know, you see it go back up.
[3111.54 --> 3111.68]  Right.
[3111.68 --> 3114.00]  So there's lots of stuff that can impact that.
[3114.32 --> 3120.70]  If it's a mostly European-based project, you see a big dip in July because we're all on vacation.
[3121.22 --> 3123.44]  Does it answer the question, are we healthy or not?
[3124.30 --> 3127.02]  Is that, what is it, what's the question specifically that it answers?
[3127.26 --> 3127.62]  Community health.
[3128.00 --> 3133.86]  Yeah, like, is it, because, like, you can score health and say we are healthy or we're healthy-ish
[3133.86 --> 3138.20]  and it can be specific to your repo and I can understand why, you know, if it's a European team,
[3138.20 --> 3140.00]  why July might be less so.
[3140.00 --> 3146.22]  And it's not like, even as an ASPO, I might be like, are my projects healthy or are they less healthy?
[3146.52 --> 3149.88]  And if it says less healthy, oh, because it's July and that makes sense.
[3150.56 --> 3150.88]  Yeah.
[3150.96 --> 3153.94]  I mean, I think the question I like to ask is where can I improve?
[3154.60 --> 3159.66]  So that is where I try to focus on the metrics is being able to look at where I can improve.
[3159.96 --> 3164.08]  But you can use it as kind of a gut check for whether it's healthy or not healthy.
[3164.08 --> 3167.02]  So I do do that within the VMware projects.
[3167.02 --> 3170.94]  There's an arbitrary threshold that I've set where it's, like, healthy and at risk.
[3171.20 --> 3172.84]  So I don't define something as unhealthy.
[3172.96 --> 3174.70]  I define it as at risk.
[3174.90 --> 3180.98]  And then, you know, maybe we look at those a little more closely if they've moved from healthy to at risk.
[3181.18 --> 3189.76]  And then we have other projects that are at risk simply because they're very large and my threshold is arbitrary and doesn't suit them well because they're a really big project.
[3189.76 --> 3194.32]  And my thresholds work really well for the average size projects that we have.
[3195.08 --> 3197.58]  So, yeah, it just depends on the project.
[3198.12 --> 3198.62]  Makes sense.
[3198.68 --> 3199.80]  One last question for you.
[3199.94 --> 3204.98]  You said at a certain point it might be time to recruit an outside contributor.
[3206.56 --> 3207.90]  What does that look like?
[3208.42 --> 3209.28]  Like, how do you do that?
[3209.28 --> 3212.16]  Again, it depends on the project.
[3212.36 --> 3215.30]  But a good place to start is by looking at the people that are adopting it.
[3215.74 --> 3223.84]  And so if you have people who are using your project, that's a good place to start to talk to some of them to see if any of them are interested in contributing.
[3224.76 --> 3227.38]  You know, sometimes you have people who've contributed a little bit.
[3227.48 --> 3229.06]  They've made, you know, a pull request or two.
[3229.18 --> 3230.26]  They filed a few issues.
[3230.26 --> 3234.58]  Maybe encouraging them to contribute a little bit more to the project.
[3234.96 --> 3239.32]  But it depends on what the project's like, who's adopting it, who's using it.
[3240.62 --> 3241.44]  And what do you say?
[3241.50 --> 3249.22]  Do you say we have a core team member slot opening up because, you know, we recognize we have a lack and we have more space for another team member?
[3249.44 --> 3253.56]  And you suggest to these adopters, hey, we have a slot opening up.
[3254.60 --> 3256.96]  Submit a request to fill it.
[3256.98 --> 3258.20]  Or do you have anybody available?
[3258.20 --> 3260.14]  How do you ask specifically?
[3260.62 --> 3261.78]  Like, how do you engage specifically?
[3262.26 --> 3262.42]  Yeah.
[3262.54 --> 3265.36]  So we don't, I don't really look at it as like a spot opening up.
[3265.48 --> 3269.26]  Like you're, if you're, if you have an open source project, you're always looking for contributors.
[3269.26 --> 3271.48]  So you're always looking for more people to get involved.
[3272.44 --> 3278.44]  And ideally, your governance documentation will give you some guidelines for how you recruit new contributors.
[3278.76 --> 3285.14]  So a lot of projects have, you know, governance so that the existing maintainers recruit the new maintainers, right?
[3285.14 --> 3288.18]  So they get to decide who gets to come in and maintain the project.
[3288.30 --> 3289.88]  So it depends a lot on your governance model.
[3289.88 --> 3290.74]  It depends on your project.
[3290.88 --> 3293.22]  It depends on what kind of contributions you're looking for.
[3293.70 --> 3295.82]  Are those governance documents different per project?
[3295.94 --> 3299.58]  Or is it sort of VM or at large government documents or governance documents?
[3299.78 --> 3300.54]  That's how it works?
[3301.14 --> 3301.54]  No.
[3301.74 --> 3304.08]  They're, they're different depending on the, on the project.
[3304.08 --> 3304.38]  Okay.
[3304.38 --> 3309.54]  And I also work with a bunch of, so I spent a lot of time in the CNCF contributor strategy technical advisory group.
[3309.54 --> 3312.84]  And one of the things that we work on for CNCF projects is governance templates.
[3313.28 --> 3317.32]  So we have, we have three different governance templates that we use for, for CNCF projects.
[3317.32 --> 3321.16]  And we encourage them to use those, but they're individual projects.
[3321.16 --> 3322.58]  They can use whatever governance they want.
[3322.66 --> 3323.84]  Sometimes they'll pick something else.
[3324.78 --> 3331.08]  But, but yeah, it varies, it varies widely across, across projects, even within the same company or within the same foundation.
[3331.08 --> 3334.30]  If someone's out there saying, wow, chaos sounds awesome.
[3334.96 --> 3337.08]  I run an OSPO and I've never heard of it.
[3337.14 --> 3337.66]  What should they do?
[3337.94 --> 3341.44]  They should go to chaos with two S's dot community, which is our website.
[3342.04 --> 3345.18]  And we have, we have loads of regular project meetings.
[3345.18 --> 3348.28]  We have working groups you can get involved in.
[3348.54 --> 3352.52]  And so I would say poke around there and there's information on how to participate.
[3352.80 --> 3355.84]  And we're very welcoming to new community members.
[3356.16 --> 3358.16]  What's your time to pull request closure ratio?
[3358.28 --> 3358.68]  What's that?
[3359.00 --> 3359.70]  Yeah, that's a good question.
[3359.76 --> 3360.40]  I have no idea.
[3360.40 --> 3361.68]  No idea.
[3362.28 --> 3363.66]  Well, thanks for joining us today.
[3363.76 --> 3364.18]  This is cool.
[3364.48 --> 3364.82]  Thank you, Don.
[3364.84 --> 3365.46]  Yeah, thanks for having me.
[3379.28 --> 3387.32]  Hey friends, I'm here with one of our partners and sponsors, Jason Bosco, co-founder and CEO of TypeSense.
[3387.32 --> 3391.94]  You may remember Jason from episode 505 of the change law.
[3392.00 --> 3395.42]  We talked about TypeSense being truly open source search.
[3395.82 --> 3400.86]  And that's kind of where we got interested in TypeSense because we've been hitting bottlenecks and issues with Algolia.
[3400.86 --> 3404.62]  And so I reached out to Jason and said, hey, Jason, we'd love to work with you and partner with you.
[3404.62 --> 3409.32]  But Jason, tell the listeners here why you all build TypeSense.
[3409.40 --> 3409.96]  What do you believe?
[3409.96 --> 3419.92]  So we believe that fast search as you type experiences need to be widely available and adopted by as many sites and apps as possible.
[3420.02 --> 3427.98]  And what I mean by search as you type is you type in a letter and it returns results right away in, say, less than 50 milliseconds or 100 milliseconds.
[3427.98 --> 3433.34]  And we've tried building experiences like this in the past with other products.
[3433.82 --> 3436.78]  You know, there's solar, there's Elasticsearch, there's Algolia.
[3437.14 --> 3449.08]  And all of them are good in different respects, but they either are very complex to deploy or they're hard to scale or they're very expensive to use even for moderate scale.
[3449.08 --> 3451.54]  So that's why we built TypeSense.
[3451.86 --> 3452.98]  We open sourced it.
[3453.24 --> 3459.50]  We made sure that you can run TypeSense locally or if you don't want to worry about infrastructure, we also have TypeSense Cloud.
[3460.00 --> 3468.36]  So you have cloud and you have open source and you ship binaries in your open source that you actually use in your cloud with extra features, of course.
[3468.52 --> 3472.00]  But what was making you think that you should build cloud in the first place?
[3472.24 --> 3477.36]  Based on what users have told us over the last several years, many folks wanted us to host the search service.
[3477.36 --> 3478.78]  So we started building TypeSense Cloud.
[3479.16 --> 3486.14]  So whether you're self-hosted or use TypeSense Cloud, it is the same binary that we run in TypeSense Cloud that we also publish open source.
[3486.28 --> 3488.18]  So the feature set is identical.
[3488.58 --> 3491.24]  But in TypeSense Cloud, of course, we manage the service for you.
[3491.30 --> 3492.50]  So you don't have to worry about infrastructure.
[3493.06 --> 3495.30]  And then we give you a nice UI to manage your data.
[3495.48 --> 3499.90]  And then we give you tool-based access control, the single sign-on, more collaboration aspects.
[3500.36 --> 3506.86]  But regardless of whether you self-hosted or use TypeSense Cloud, we want to bring this technology to as broad an audience as possible.
[3506.86 --> 3509.16]  Without having to worry about cost.
[3509.44 --> 3514.60]  And that's one of the reasons we decided to partner with you, Adam, and talk about TypeSense here.
[3514.72 --> 3519.36]  Yeah, I love the idea of getting this into as many developers' hands as possible.
[3519.70 --> 3523.88]  The fact that you have blazing fast in-memory search like you do that's open source,
[3523.98 --> 3529.46]  that competes with the likes of Elasticsearch or Algolia, that you can just host yourself if you want to.
[3529.52 --> 3530.24]  That's so awesome.
[3530.60 --> 3532.22]  Of course, we're excited to partner with you.
[3532.22 --> 3538.94]  We're using TypeSense Cloud, which is awesome and very fortunate to have a chance to work with you on this project.
[3539.08 --> 3543.54]  Obviously, we have so much more in store for our search feature, so we're barely scratching the surface.
[3543.96 --> 3549.36]  But hey, listeners, check out TypeSense at typesense.org or at cloud.typesense.org.
[3549.70 --> 3552.18]  I think Jason's awesome and he has an awesome team.
[3552.58 --> 3555.60]  And of course, we're using TypeSense, so we think you should check it out too.
[3555.60 --> 3560.18]  Again, typesense.org or cloud.typesense.org.
[3585.60 --> 3587.78]  Drupal is still a big deal, right?
[3588.42 --> 3589.34]  Is Drupal still a big deal?
[3589.42 --> 3589.94]  I would think so.
[3590.10 --> 3591.72]  I would say Drupal is still a big deal, yeah.
[3592.12 --> 3593.98]  So I know somebody who is big into Drupal.
[3594.68 --> 3596.42]  Well, I don't know him, know him, but I know him.
[3597.02 --> 3597.92]  His name is Jeff Geerling.
[3598.14 --> 3598.70]  You know Jeff Geerling?
[3598.92 --> 3599.08]  Yeah.
[3599.32 --> 3601.88]  He's a big Drupal guy and he's moving his stuff off of Drupal.
[3601.90 --> 3602.14]  You're Drupal, right?
[3602.82 --> 3604.90]  On to, I believe, WordPress, if I last look.
[3605.06 --> 3605.92]  Oh, he's moving off Drupal?
[3606.24 --> 3608.32]  Yeah, like he would self-host and do a bunch of stuff.
[3608.32 --> 3610.24]  So I think he was a big Drupal person.
[3610.32 --> 3612.96]  But I just wonder, like, is the tide shifting away from Drupal?
[3613.04 --> 3613.84]  Is it still a big deal?
[3613.84 --> 3614.90]  Do you know?
[3615.18 --> 3620.30]  I think what I would say about that is Drupal has kind of shifted where, you know, what
[3620.30 --> 3623.70]  it's really targeting at this point is, like, ambitious digital experience is sort of what
[3623.70 --> 3624.04]  we say.
[3624.10 --> 3626.76]  It's an open source data platform for all that kind of stuff.
[3627.18 --> 3631.60]  And what that means is if what you're doing is running a personal blog, Drupal is probably
[3631.60 --> 3634.18]  going to be a really frustrating platform to run that on, to be honest.
[3634.18 --> 3638.46]  But if you're building, for example, a university website where all of the different departments
[3638.46 --> 3641.38]  need to have the same functionality but look different from each other and have different
[3641.38 --> 3643.58]  access control, it's really great for stuff like that.
[3643.84 --> 3643.98]  Right.
[3644.26 --> 3644.44]  Yeah.
[3644.88 --> 3645.56]  Access control.
[3645.68 --> 3647.98]  So do you plug into, like, SSOs and stuff like that now?
[3648.02 --> 3648.82]  Is there plugins for that?
[3649.08 --> 3649.46]  Oh, yeah.
[3649.50 --> 3650.42]  There's plugins for everything.
[3650.74 --> 3650.90]  For sure, right?
[3650.90 --> 3651.06]  Yeah.
[3651.16 --> 3652.18]  Plugging into SSO.
[3652.32 --> 3655.98]  If you want different functionality and features, you click buttons for that, that kind of stuff.
[3656.50 --> 3656.82]  Gotcha.
[3657.38 --> 3658.48]  Are you still in the Drupal community?
[3658.66 --> 3660.28]  Like, what's your state?
[3660.50 --> 3660.78]  Yeah.
[3661.04 --> 3661.32]  So...
[3661.32 --> 3662.00]  It's been a while since we talked to you.
[3662.00 --> 3662.82]  It has been a while since.
[3662.88 --> 3663.28]  I know.
[3663.40 --> 3663.44]  Yeah.
[3663.58 --> 3665.28]  2018, the last time Angie's been on the show.
[3665.40 --> 3665.90]  So it's been...
[3665.90 --> 3666.26]  Five years.
[3666.32 --> 3667.38]  ...essentially a lifetime ago.
[3667.70 --> 3667.82]  Essentially.
[3667.96 --> 3668.08]  Yeah.
[3668.14 --> 3668.86]  In tech especially.
[3669.02 --> 3670.62]  It's like, that was like seven lifetimes ago.
[3670.62 --> 3671.10]  What's happened?
[3671.16 --> 3671.82]  Are you still involved?
[3671.94 --> 3672.76]  What's your state?
[3672.76 --> 3672.78]  Yeah.
[3672.78 --> 3672.94]  Yeah.
[3673.14 --> 3680.82]  So I ended up departing Acquia in 2021 or so because I kind of had gotten to the point
[3680.82 --> 3682.80]  where it's like, okay, I kind of saw Drupal through.
[3682.92 --> 3687.28]  It's like, you know, it's a toddler banging itself on the furniture kind of stages and up
[3687.28 --> 3690.74]  until now it's an adult with a stable apartment and all this kind of stuff.
[3690.96 --> 3690.98]  Right.
[3690.98 --> 3691.76]  Paying their bills.
[3691.76 --> 3692.06]  Yeah.
[3692.18 --> 3694.56]  You know, the releases are coming out on time.
[3694.70 --> 3697.36]  We're not having security vulnerabilities, like these kinds of things.
[3697.36 --> 3701.28]  So it kind of felt like, okay, I beat this level of my career kind of thing.
[3701.32 --> 3701.48]  Yeah.
[3701.76 --> 3703.44]  And then I started getting into data platforms.
[3703.66 --> 3708.76]  So I went into MongoDB and now I'm at Ivan, which is a startup around open source data stuff.
[3708.82 --> 3713.10]  So they run Kafka, Postgres, MySQL, Cassandra, a bunch of other things.
[3713.28 --> 3713.38]  Yeah.
[3713.56 --> 3713.80]  Wow.
[3714.82 --> 3715.02]  Yeah.
[3715.14 --> 3717.54]  So I would say like I'm less involved in the day-to-day of Drupal.
[3717.54 --> 3720.22]  Like I used to know literally everything that was going on.
[3720.28 --> 3721.34]  I was on top of every issue.
[3721.48 --> 3723.52]  I was on top of every new contributor, that kind of stuff.
[3723.52 --> 3727.32]  But what I do get pulled in for Drupal now is like the kind of big strategic decisions, you know,
[3727.42 --> 3730.14]  like Drupal 7 end of life or, you know,
[3730.20 --> 3733.84]  things like if the Dries node is going to create a different strategic direction,
[3733.96 --> 3737.76]  they'll call me in to talk about that or core maintainership stuff, that sort of stuff.
[3737.88 --> 3742.62]  So it's kind of nice because I get to still be knowledgeable and involved of the big decisions in Drupal,
[3742.70 --> 3746.16]  but I don't have to like bike shed what color buttons are anymore, which is kind of nice.
[3746.72 --> 3750.60]  Well, I have to say that I really, really enjoyed the episode we did with you way back when.
[3750.66 --> 3751.48]  Yeah, that was fun.
[3751.48 --> 3752.72]  Episode 321, if you're listening to this.
[3752.72 --> 3754.76]  Back in October of 2018.
[3754.76 --> 3755.52]  That's a great number.
[3755.68 --> 3756.04]  321.
[3756.30 --> 3759.02]  I just love the energy you brought to that community.
[3759.20 --> 3761.84]  Like Jared and I are very much departed from Drupal.
[3761.94 --> 3763.08]  We're not involved really at all.
[3763.24 --> 3770.04]  And I feel like you gave us the best 30,000 foot, maybe 12,000 foot view of that world.
[3770.40 --> 3771.32]  And you just had so much passion.
[3771.62 --> 3772.16]  You really just did.
[3772.26 --> 3773.54]  I mean, you represented Drupal very well.
[3773.78 --> 3774.50]  And I still do.
[3774.58 --> 3776.50]  I love Drupal, you know, and I love that community.
[3776.96 --> 3781.94]  The software is really interesting, especially for kind of like those big projects that have a lot of different moving parts.
[3781.94 --> 3785.96]  Or I used to say Drupal is great if your client has no idea what they want.
[3786.12 --> 3788.86]  Because it can do all of the different things that you need it to do, you know.
[3788.86 --> 3790.86]  But again, it's not such a good platform.
[3791.00 --> 3796.60]  If you know exactly what you need as a blog or what you need as a shopping cart or something like that, there are other platforms that are good.
[3796.60 --> 3802.12]  So we're here as part of Maintainer Month along with GitHub and celebrating this community and open source maintainers.
[3802.26 --> 3804.06]  So it's been a bit since we caught up.
[3804.14 --> 3805.48]  So what's your maintainer story now?
[3805.56 --> 3808.58]  Like if you were giving a fresh view of your maintainer story, what is it?
[3808.72 --> 3815.22]  I think my maintainer story has moved to the point where I'm trying to sort of empower more people.
[3815.22 --> 3825.74]  So if you think about building out a leadership bench of your maintainership so that you're not solely dependent on individual contributors that have been with the project for a long time and have a lot of historical knowledge.
[3825.98 --> 3833.02]  But really clearing the way so that folks newer to the project or have new interesting ideas can come in and can take a leadership role in the project.
[3833.12 --> 3840.86]  So I'd say that's more the point where I'm at is sort of shepherding in new leaders, providing some mentorship to some of the incoming product managers for Drupal, that kind of thing.
[3840.86 --> 3842.90]  So what's involved in that?
[3843.02 --> 3844.20]  Like is there documentation involved?
[3844.28 --> 3845.24]  Are you writing syllabuses?
[3845.66 --> 3846.74]  Gosh, I should.
[3846.92 --> 3849.38]  How are you educating and on-ramping this leadership?
[3849.76 --> 3856.80]  It seems like just proving ground for documentation to some degree because you can document the process and usher them in.
[3856.80 --> 3861.68]  I mean, when we set up the governance structure originally, because originally it was me and Dries.
[3861.80 --> 3866.40]  We were the two maintainers for Drupal 7, and that was not going to scale as we built out.
[3866.40 --> 3877.16]  So we started by creating like a core governance where we, you know, had kind of different types of committers that would focus in different areas, product managers, framework managers, this kind of thing, release managers.
[3878.10 --> 3881.02]  And so that stuff, the distinction between those is documented.
[3881.18 --> 3883.92]  And that way you don't have to be someone that can cut across all of those areas.
[3883.98 --> 3885.82]  You can sort of focus on one area or another.
[3886.56 --> 3892.24]  So what my involvement has been is a lot more ad hoc, just kind of like having one-off conversations with people.
[3892.24 --> 3892.74]  But you're right.
[3892.82 --> 3897.96]  I should start documenting some of this stuff because, yeah, it's good information for people to know.
[3897.96 --> 3899.00]  You probably repeat yourself a lot.
[3899.56 --> 3900.52]  Well, I don't know.
[3900.62 --> 3901.86]  I enjoy repeating myself a lot.
[3901.86 --> 3904.58]  Positively, I mean that in the most best case possible.
[3904.78 --> 3904.94]  Yeah.
[3905.06 --> 3906.76]  So I find that I repeat myself a lot too.
[3906.94 --> 3914.84]  And I've learned that I have limited bandwidth and I have to begin to jot down and put down things that I do, particularly for our organization.
[3914.84 --> 3921.68]  And I've been executing on that and getting that positive feedback loop from that effort too.
[3922.00 --> 3923.58]  So maybe you repeat yourself a lot.
[3923.68 --> 3925.96]  So maybe it's time to document the process.
[3925.96 --> 3926.26]  Do some thought leadership.
[3927.02 --> 3927.54]  Well, you know.
[3927.54 --> 3927.70]  Yeah.
[3927.82 --> 3928.50]  But no, you're right.
[3928.58 --> 3928.88]  You're right.
[3928.96 --> 3929.46]  It is true.
[3929.64 --> 3934.94]  Because otherwise the stuff that you're imparting kind of stays within that one conversation when it could be out there for benefit of everybody.
[3934.94 --> 3936.50]  But talking is so much more fun than writing.
[3936.64 --> 3937.30]  It really is.
[3937.44 --> 3937.88]  It is.
[3938.04 --> 3938.16]  Yeah.
[3938.28 --> 3939.54]  I like writing too, honestly.
[3939.74 --> 3940.14]  But yeah.
[3940.38 --> 3941.42]  I just never shut up.
[3941.48 --> 3942.92]  So it'll be like 4,000 words.
[3943.00 --> 3943.72]  It could have been in 20.
[3943.72 --> 3946.04]  You could transcribe yourself, which is what we do.
[3946.18 --> 3946.96]  Oh, interesting.
[3947.04 --> 3947.38]  For our shows.
[3947.46 --> 3947.72]  Yeah.
[3948.10 --> 3949.50]  This is being transcribed right now.
[3949.72 --> 3949.96]  Okay.
[3950.06 --> 3950.58]  Not right now.
[3950.58 --> 3951.28]  Better watch.
[3951.28 --> 3952.12]  Literally right now.
[3952.34 --> 3952.48]  Eventually.
[3952.98 --> 3954.10]  And this is on the record.
[3954.36 --> 3956.48]  There is a buffer between now and the transcribed.
[3956.58 --> 3956.80]  Okay.
[3956.84 --> 3957.18]  Right on.
[3957.52 --> 3962.64]  And then you could give it to your favorite language model and say, turn this into documentation.
[3963.14 --> 3963.78]  That's cool.
[3964.10 --> 3964.38]  All right.
[3964.38 --> 3964.86]  I'm going to think.
[3964.94 --> 3965.40]  There's an idea.
[3965.54 --> 3965.68]  Yeah.
[3965.78 --> 3966.70]  Here's a question for you.
[3966.80 --> 3969.48]  So going back to 21, you said you felt like you beat that level.
[3969.74 --> 3971.40]  You're ready for your next adventure.
[3971.40 --> 3975.26]  How do you decide what's next?
[3975.34 --> 3976.70]  Like, how did you decide what's next?
[3976.76 --> 3979.32]  How did you pick this area of work?
[3979.40 --> 3980.10]  And what drew you here?
[3980.66 --> 3985.70]  Well, so Drupal had this amazing community, but largely consisted of web developers.
[3986.08 --> 3988.38]  Web developers who could stand PHP specifically.
[3988.62 --> 3989.78]  So that's like a pretty small.
[3989.78 --> 3989.94]  Right.
[3989.94 --> 3990.92]  It's a niche inside a niche.
[3990.98 --> 3992.50]  It's a little bit of a niche inside of a niche.
[3992.50 --> 3992.60]  Yeah.
[3992.60 --> 3992.94]  Exactly.
[3993.40 --> 3998.82]  So what appeals to me about data platforms is that any kind of developer can use them
[3998.82 --> 3999.98]  in any kind of language.
[4000.58 --> 4000.72]  Right?
[4000.72 --> 4000.82]  Right.
[4000.82 --> 4004.66]  So you can be, you know, I have C++ developers doing embedded systems.
[4004.78 --> 4006.62]  You can have folks doing AI and ML.
[4006.80 --> 4007.94]  You can have web developers.
[4008.20 --> 4008.46]  Sure.
[4008.62 --> 4008.84]  Right?
[4008.92 --> 4009.92]  And all these kinds of things.
[4009.92 --> 4014.14]  And what interests me from a community management perspective, because that's kind of my deal.
[4014.30 --> 4015.36]  I'm director of community.
[4015.70 --> 4021.84]  I love getting people together and just like making awesome things happen, is cracking
[4021.84 --> 4022.72]  that code.
[4022.82 --> 4023.40]  Do you know what I mean?
[4023.40 --> 4025.30]  Around those different language frameworks.
[4025.54 --> 4029.40]  How do you, what's the Venn diagram of things that these people have in common?
[4029.58 --> 4029.84]  Right.
[4029.96 --> 4031.04]  Where is the common thread?
[4031.28 --> 4032.02]  Yeah, exactly.
[4032.46 --> 4032.74]  Okay.
[4032.74 --> 4036.84]  And Ivan is really interesting because it's the common thread among many open source projects.
[4037.34 --> 4040.74]  A MySQL developer and a Postgres developer don't necessarily have a lot in common.
[4041.08 --> 4043.60]  Like they won't go to the same user groups necessarily.
[4043.80 --> 4044.00]  Right.
[4044.10 --> 4047.38]  But if you pull it up a level to open source data infrastructure, now all of a sudden we
[4047.38 --> 4048.26]  do have a lot in common.
[4048.66 --> 4052.66]  So it's been a really interesting thing to kind of get involved in all these different communities,
[4052.66 --> 4057.08]  see how they each do governance and how they do different approaches to, you know,
[4057.14 --> 4058.88]  kind of the common things that maintainers deal with.
[4058.94 --> 4061.36]  How do you triage incoming stuff without overwhelming people?
[4061.36 --> 4065.40]  How do you make sure you're keeping the platform stable, but also adding innovation?
[4065.78 --> 4069.52]  And, you know, seeing that as a bird's eye view across many different open source projects
[4069.52 --> 4070.50]  is really fascinating.
[4071.36 --> 4073.70]  How did that opportunity present itself?
[4074.96 --> 4081.14]  Well, the MongoDB opportunity presented itself because I know a guy named Jono Bacon, who is
[4081.14 --> 4082.78]  big in the community leadership space.
[4083.00 --> 4083.18]  Yeah.
[4083.54 --> 4083.98]  He's great.
[4084.30 --> 4084.74]  We know Jono.
[4084.94 --> 4085.10]  Yeah.
[4085.24 --> 4089.44]  And I kind of just, you know, we've kept in touch and I, you know, kind of subtly was
[4089.44 --> 4093.12]  like, Hey, you know, I'm not actively like looking, but if you know of anything, just
[4093.12 --> 4094.00]  pass it along my way.
[4094.00 --> 4095.08]  And yeah, he passed it along.
[4095.12 --> 4096.86]  And I was like, wow, this is really cool.
[4096.98 --> 4100.06]  And so I got to kind of meet the different, you know, leadership at MongoDB.
[4100.26 --> 4101.56]  And I was like, these people are awesome.
[4101.56 --> 4103.44]  Like they really believe in this.
[4103.44 --> 4104.94]  And like the, the story is amazing.
[4104.94 --> 4107.04]  And there's a lot of good I can do here.
[4107.04 --> 4107.36]  Yeah.
[4107.86 --> 4112.94]  And I feel like I did do a lot of good there, but you know, it gets into a lot of like,
[4113.10 --> 4117.26]  I don't know how much you get into legal, you know, philosophy debates around licensing
[4117.26 --> 4119.26]  and stuff, but MongoDB is not open source.
[4119.44 --> 4120.40]  It is SSPL.
[4121.12 --> 4121.76]  We covered this.
[4121.90 --> 4122.20]  Yeah.
[4122.22 --> 4128.16]  Well, not Mongo directly, but all the peripherals around the BSL, the SSPL.
[4128.50 --> 4128.64]  Yeah.
[4128.74 --> 4128.94]  Right.
[4129.04 --> 4129.56]  All the.
[4129.60 --> 4130.82]  Mostly with a view into Elastic.
[4130.82 --> 4131.44]  All the nuance.
[4131.60 --> 4131.68]  Yeah.
[4131.94 --> 4132.20]  Elastic.
[4132.20 --> 4135.24]  It's interesting because like the OSI hasn't quite cracked this yet.
[4135.24 --> 4135.58]  Right.
[4136.04 --> 4140.58]  Because if you look objectively at open source projects that have adopted these open-ish
[4140.58 --> 4143.10]  licenses, except if you're going to run your own service.
[4143.26 --> 4143.48]  Right.
[4143.78 --> 4145.98]  It becomes a stable funding model for them.
[4146.24 --> 4150.32]  Like, you know, MongoDB's revenue went boom, boom, boom, boom, you know, and the open source,
[4150.46 --> 4152.78]  true open source communities do not have that.
[4153.22 --> 4157.86]  And Amazon or somebody can take their product, productize it on their own thing, charge a bazillion
[4157.86 --> 4160.98]  dollars, and they don't have any obligation to give back anything to the project.
[4161.08 --> 4162.04]  So it's a huge challenge.
[4162.20 --> 4162.30]  Yeah.
[4162.50 --> 4163.24]  So I appreciate that.
[4163.32 --> 4164.34]  It has restrictions though, right?
[4164.42 --> 4168.00]  Like the SSPL and the BSL both have restrictions, which I think is the sticking point.
[4168.00 --> 4169.64]  And that's why they're not open source licenses.
[4169.64 --> 4169.72]  Right.
[4169.72 --> 4169.92]  Exactly.
[4170.10 --> 4172.06]  It's obvious why there is this sticking point.
[4172.14 --> 4174.28]  It's not like, oh, well, we just can't call them open source.
[4174.48 --> 4174.76]  Yeah.
[4175.04 --> 4179.50]  Because eventually open source is not open source necessarily.
[4179.82 --> 4179.98]  Exactly.
[4179.98 --> 4184.00]  Now, there will be people out there who will argue that, as you may know, and those people
[4184.00 --> 4188.26]  may even operate those companies who run that software that is BSL or SSPL licensed.
[4188.64 --> 4189.18]  And that's cool.
[4189.42 --> 4191.06]  And I'm not, but it is restricted.
[4191.06 --> 4194.78]  So by the nature of restriction, it is not open.
[4195.42 --> 4195.82]  Exactly.
[4196.10 --> 4201.44]  But it is an interesting thing in that absent of having a sustainable recurring revenue model
[4201.44 --> 4203.46]  that you can build off a service for on your thing.
[4203.56 --> 4203.90]  Right.
[4203.90 --> 4207.30]  You kind of have to do one-off projects or you have to beg for money from big corporate.
[4207.30 --> 4209.50]  Like your funding options are much more limited.
[4209.68 --> 4209.94]  For sure.
[4210.06 --> 4214.40]  So I respected MongoDB a lot that they went after a solution to that problem.
[4214.70 --> 4215.10]  Right.
[4215.10 --> 4220.06]  Even if it's not in keeping with the full spirit of open source, it was like, it's creative.
[4220.20 --> 4221.10]  I give you credit for that.
[4221.10 --> 4228.28]  I think the community accepts the SSPL and the BSL licensed solutions you're talking about,
[4228.34 --> 4229.04]  though, quite well.
[4229.74 --> 4231.16]  You know, one in particular is a sponsor of us.
[4231.16 --> 4232.64]  It depends on the part of the community.
[4232.64 --> 4234.06]  Which part of the community you're talking about.
[4234.20 --> 4234.34]  Yeah.
[4234.34 --> 4234.82]  Yeah.
[4234.94 --> 4238.26]  But I mean, I guess what I mean by that is that it's not like, oh, you chose that,
[4238.34 --> 4242.98]  so you're there for your bad because you decided to go a route that funded your business or
[4242.98 --> 4243.98]  made your business sustainable.
[4244.32 --> 4247.56]  I think the sustainable side more so than the funding side is the part that you have
[4247.56 --> 4253.02]  to have empathy on because particularly Century would not be a company and be as profitable
[4253.02 --> 4255.32]  as it is if it was not BSL licensed.
[4255.42 --> 4258.74]  If it was originally, I believe, Apache VO2, I could be wrong.
[4258.74 --> 4265.98]  But if it was not BSL licensed, it would not have the funding model it has, nor be giving
[4265.98 --> 4266.70]  back to open source.
[4266.76 --> 4268.74]  So there's all these positives to that.
[4268.74 --> 4273.74]  And they're also very, you know, open source centric and very giving in a lot of cases out
[4274.32 --> 4274.68]  there in the community.
[4274.78 --> 4275.74]  There's a lot of good that's done.
[4276.26 --> 4276.66]  Definitely.
[4277.10 --> 4277.78]  But you have to.
[4277.90 --> 4278.12]  I think there's a spectrum.
[4278.18 --> 4281.14]  But they're not calling themselves open source necessarily.
[4281.36 --> 4281.86]  No, they're not.
[4282.42 --> 4288.34]  That's where it gets icky is like, if you're BSL, okay, shout it proud, right?
[4288.34 --> 4291.26]  If you're open source officially, shout it proud.
[4291.58 --> 4295.64]  But don't play the game that's in the middle because now we're getting to where it's like,
[4295.76 --> 4295.92]  eh.
[4296.22 --> 4298.14]  And then there's people who really don't care.
[4299.18 --> 4300.56]  And there's people who really do care.
[4300.74 --> 4304.02]  And then in between, we all find ourselves, which way do you lean?
[4305.04 --> 4308.62]  And so it's hard to say the community accepts that because I think there's plenty of people
[4308.62 --> 4310.82]  in the community who don't, but there are plenty who are.
[4311.20 --> 4312.48]  And then there's those of us in between.
[4312.58 --> 4316.08]  I tend to be like slightly over there to be like, well, it's better than nothing.
[4316.24 --> 4317.78]  I'm kind of on the sustainability side myself.
[4317.78 --> 4320.80]  It's like, well, this is what I think is a good thing.
[4321.14 --> 4325.32]  And we would not have this good thing if it weren't for this particular circumstance
[4325.32 --> 4326.62]  that they chose.
[4327.24 --> 4329.88]  Maybe they could have chose something different and it would be okay.
[4330.00 --> 4331.00]  But this is what they chose.
[4331.32 --> 4332.56]  I'd rather have that than nothing.
[4333.24 --> 4334.02]  And so, okay.
[4334.08 --> 4338.92]  I think eventually open source is kind of cool, but open source right now is cooler.
[4339.60 --> 4341.24]  But maybe that thing wouldn't exist if there wasn't.
[4341.24 --> 4341.56]  It's true though.
[4341.80 --> 4343.80]  People apply different value frameworks, right?
[4343.80 --> 4343.98]  Yeah.
[4344.02 --> 4345.40]  Like what do you value changes?
[4345.40 --> 4349.28]  And then there's other people who are like, no, it has to be OSI compatible.
[4349.50 --> 4353.44]  And then there's obviously the FOSS side of things that has to be copy left, etc.
[4353.56 --> 4353.76]  So.
[4354.34 --> 4357.86]  And it's interesting because that's why these arguments can get kind of fractious because
[4357.86 --> 4359.14]  no one's wrong, right?
[4359.16 --> 4360.84]  It's like everybody has a defensible position.
[4360.90 --> 4361.14]  Right.
[4361.34 --> 4362.66]  In this whole thing.
[4363.16 --> 4366.08]  But this goes back to Adam Jacobs' war for the soul of open source, right?
[4366.08 --> 4366.38]  For sure.
[4366.60 --> 4368.18]  It goes back to what do you value?
[4368.48 --> 4368.70]  Yep.
[4368.82 --> 4369.72]  And what is open?
[4369.80 --> 4370.92]  Why do you come here?
[4371.16 --> 4371.36]  Yeah.
[4371.36 --> 4371.60]  Right?
[4372.40 --> 4372.62]  Yeah.
[4372.68 --> 4373.96]  And we all have to kind of answer that ourselves.
[4374.12 --> 4374.60]  I don't know.
[4374.64 --> 4375.90]  What are your thoughts on these things?
[4376.82 --> 4385.34]  My thoughts on these things are I think the OSI needs some solution to this.
[4385.60 --> 4390.06]  Someone else can productize your service and make a bazillion dollars and you see nothing
[4390.06 --> 4390.82]  of a problem.
[4391.04 --> 4392.16]  Because I do think it's a problem.
[4392.40 --> 4392.50]  Yeah.
[4392.50 --> 4395.16]  It creates an issue since we're talking about maintainer month.
[4395.28 --> 4395.54]  Right.
[4395.62 --> 4399.76]  You know, where the actual maintainers upon which these millions of dollars are built are
[4399.76 --> 4401.26]  slogging it out on nights and weekends.
[4401.26 --> 4401.30]  Exactly.
[4401.50 --> 4401.72]  Right?
[4401.80 --> 4404.34]  Ignoring their families while you're making a billion dollars.
[4404.44 --> 4405.44]  Like that's a problem.
[4405.44 --> 4407.88]  I get that it's tricky though, right?
[4407.96 --> 4408.04]  Right.
[4408.04 --> 4411.44]  Because the whole ethos behind open source project is there is no restrictions.
[4411.64 --> 4412.52]  Do whatever you want with it.
[4412.52 --> 4412.72]  It's free.
[4412.72 --> 4413.68]  Do whatever you want, right?
[4413.78 --> 4417.80]  Including make money off the backs of that one guy in Nebraska, right?
[4417.84 --> 4419.08]  Who's maintaining like the base.
[4419.42 --> 4419.58]  Yeah.
[4419.58 --> 4421.04]  So I don't know.
[4421.22 --> 4422.86]  I can see all angles on it.
[4423.10 --> 4427.62]  But I do think that it's a clever way to make your open source or, you know, your open
[4427.62 --> 4431.98]  source enough project, open source-ish product sustainable.
[4432.54 --> 4435.12]  Because the, you know, the financial speak for itself.
[4435.26 --> 4435.44]  Yeah.
[4435.70 --> 4435.96]  Yeah.
[4436.62 --> 4441.40]  So you think that OSI needs to either expand the definition to include some of these or
[4441.40 --> 4448.30]  one of these or come up with some other license or model that is inside of its own definition
[4448.30 --> 4453.62]  but allows for maintainers to thrive under this one circumstance that's really kind of crushing
[4453.62 --> 4455.08]  certain maintainers.
[4455.08 --> 4455.12]  Yeah.
[4455.20 --> 4456.88]  I just think it needs to be grappled with.
[4457.00 --> 4457.16]  Yeah.
[4457.26 --> 4458.28]  And I'm sure it has been.
[4458.40 --> 4462.64]  But I think it really needs to be grappled with because just being like, nope, this is
[4462.64 --> 4464.80]  the definition, this one little box and that's it.
[4464.88 --> 4466.88]  It's like that isn't working in 2023.
[4467.20 --> 4467.46]  Yeah.
[4467.46 --> 4472.32]  And what you're seeing like actually like abandonment of open source licenses for things like BSL
[4472.32 --> 4473.14]  or SSPL.
[4473.36 --> 4473.52]  Right.
[4473.52 --> 4475.34]  Because there's no open source solution.
[4475.78 --> 4479.36]  So in the same way we have different variations of Creative Commons, for example, that allow,
[4480.02 --> 4483.36]  you know, require attribution, are non-commercial, that kind of thing.
[4483.36 --> 4483.46]  Totally.
[4483.46 --> 4488.30]  It feels like we need some model like that for open source licenses with whatever asterisks
[4488.30 --> 4489.24]  and disclaimers are needed.
[4489.24 --> 4489.54]  Right.
[4489.72 --> 4492.82]  But without having informal framework for that, this is going to continue happening is my view.
[4492.82 --> 4495.40]  You almost need a spectrum to address the spectrum, right?
[4495.50 --> 4495.84]  Yeah.
[4496.62 --> 4496.84]  Right?
[4496.88 --> 4501.04]  Like a spectrum of licenses that move from one side to the other that allow you to slot in where
[4501.04 --> 4501.82]  it matters for you.
[4501.92 --> 4502.18]  Sure.
[4502.18 --> 4508.18]  Do you pay attention much to the OSI's, I guess, news, so to speak?
[4508.24 --> 4511.80]  The last time I checked, they were like, the SSPL is not open source.
[4511.90 --> 4513.96]  And that was like a, the title of the blog post.
[4514.10 --> 4518.12]  That was back in 2020, I think when we did the, I don't know when we did the episode,
[4518.26 --> 4518.60]  2021.
[4520.00 --> 4524.34]  It was an elastic search and that debate they had between them and AWS.
[4524.84 --> 4525.02]  Yeah.
[4525.64 --> 4527.48]  I don't think their position has changed.
[4527.52 --> 4528.56]  And again, it's a defensible position.
[4528.56 --> 4530.18]  What I mean is how they addressed it by any means.
[4530.18 --> 4536.08]  Have they gone back to the SSPL conversation and said, okay, worst case, here's the positive
[4536.08 --> 4541.14]  size to the SSPL or BSL license organizations that are doing this.
[4541.26 --> 4544.88]  I mean, if they're not going to call it open source, which is, you know, totally, you know,
[4544.92 --> 4550.38]  at their discretion and the committee's discretion who gets voted in and runs the board and stuff
[4550.38 --> 4552.98]  like that, which is peer led.
[4553.10 --> 4553.80]  It's a peer vote.
[4553.96 --> 4554.20]  Correct.
[4554.30 --> 4559.74]  You know, so it's not like some randos are just running the OSI, you know, ragged or whatever.
[4559.88 --> 4560.94]  It's, they're voted in.
[4561.28 --> 4566.32]  But they're voted in by folks that are way more on the, this is the pure definition.
[4566.42 --> 4568.28]  Because that's why the OSI was created, right?
[4568.28 --> 4568.42]  Right.
[4568.42 --> 4569.54]  To defend the definition.
[4569.62 --> 4569.94]  Exactly.
[4570.18 --> 4570.40]  Right.
[4570.48 --> 4570.70]  Exactly.
[4570.70 --> 4575.08]  So it's sort of a self replicating machine because it's like the people who are voting
[4575.08 --> 4578.42]  are going to vote for people who still believe, you know, I don't know though, in my defense,
[4578.50 --> 4584.24]  in their defense, I, I wouldn't call myself an avid keeper upper on top of OSI breaking
[4584.24 --> 4584.44]  news.
[4584.44 --> 4584.72]  That was my question primarily.
[4585.06 --> 4586.50]  Neither are we, which is why we're asking.
[4586.50 --> 4587.76]  That's why I'm asking you.
[4587.98 --> 4592.66]  And then the question, I guess then, if you were, was when have they last addressed BSL
[4592.66 --> 4593.22]  or SSPL?
[4593.40 --> 4596.16]  Have, has there been any positive and or negative?
[4596.94 --> 4597.82]  Maybe we can go back and.
[4597.82 --> 4598.08]  Yeah.
[4598.12 --> 4599.66]  Again, not to my knowledge, but I mean.
[4599.80 --> 4601.86]  And they're like, I'm looking it up right now, you idiots.
[4602.24 --> 4602.60]  Yeah.
[4602.60 --> 4608.00]  Well, if, Hey, if anyone from the OSI is listening, please tell us because yeah, if, if there is
[4608.00 --> 4612.74]  something in the works around like, or already happening around this, this funding sustainability
[4612.74 --> 4613.46]  issue.
[4613.58 --> 4613.86]  Right.
[4614.02 --> 4614.30]  Great.
[4614.48 --> 4616.62]  So where does Ivan fall in this world?
[4616.90 --> 4617.26]  Oh yeah.
[4617.34 --> 4618.32]  Is it purely open source or?
[4618.42 --> 4618.68]  Yeah.
[4618.74 --> 4623.16]  So the reason I like Ivan is because all of the underlying data technologies are actual open
[4623.16 --> 4624.82]  source with a capital O and capital S.
[4624.82 --> 4625.14]  Right.
[4625.42 --> 4627.80]  So they got streaming services built off Kafka or.
[4627.82 --> 4628.50]  It's not even built off.
[4628.60 --> 4629.88]  It's like you get Kafka.
[4630.06 --> 4634.68]  We manage it for you so that you don't have to panic because Kafka is apparently a nightmare
[4634.68 --> 4636.76]  to manage is what I'm reading out of like things.
[4636.90 --> 4637.36]  And so it's like.
[4637.36 --> 4641.18]  That's the key to having an awesome open source infrastructure project to build businesses
[4641.18 --> 4641.54]  around.
[4641.64 --> 4641.96]  Yeah.
[4642.02 --> 4645.26]  Is it has to be really valuable and really hard to manage on your own.
[4645.26 --> 4645.40]  Yeah.
[4645.40 --> 4645.64]  Yeah.
[4645.64 --> 4646.06]  Exactly.
[4646.20 --> 4649.52]  I just had a conversation with Red Panda's founder, which is probably in your neck of the
[4649.52 --> 4652.88]  woods because they essentially are a better version of Kafka.
[4653.14 --> 4653.38]  Yeah.
[4653.46 --> 4653.70]  Okay.
[4653.70 --> 4654.10]  Right on.
[4654.28 --> 4654.80]  In their terms.
[4654.80 --> 4655.08]  Yeah.
[4655.08 --> 4655.14]  Yeah.
[4655.78 --> 4655.94]  Yeah.
[4656.04 --> 4660.32]  No, I like Ivan because they don't, they don't want, they legit don't want vendor lock-in.
[4660.42 --> 4664.32]  Like if you, if Ivan makes you angry, you can take your Kafka and move it to Confluent
[4664.32 --> 4666.90]  or whoever you, I'm probably not supposed to say that word, but anyway, you know what I
[4666.90 --> 4667.04]  mean?
[4667.04 --> 4671.52]  Like, it's like, it's fine because we're selling, you know, what we're trying to sell is like,
[4671.58 --> 4673.78]  Hey, we're the security layer on top of your thing.
[4673.78 --> 4674.90]  We're going to do the updates for you.
[4674.90 --> 4675.86]  Like this kind of stuff.
[4675.90 --> 4676.18]  Right.
[4676.30 --> 4677.54]  So that you can then be like, great.
[4677.60 --> 4678.40]  I don't have to worry about that.
[4678.42 --> 4680.44]  I can just write the stuff my business cares about.
[4680.44 --> 4682.30]  Cause they don't care if I'm running a Kafka cluster.
[4682.30 --> 4683.52]  Like they don't care about that.
[4683.76 --> 4683.96]  Right.
[4683.96 --> 4685.78]  They care about the results that they're going to get.
[4685.86 --> 4686.00]  Right.
[4686.26 --> 4689.88]  The other thing I like about them is, you know, a lot of companies will try to make
[4689.88 --> 4690.86]  money off of open source.
[4690.98 --> 4693.20]  Like that's, you know, why we're all here.
[4693.20 --> 4693.42]  Right.
[4693.48 --> 4696.36]  It's like this conference is, you know, very enterprise profit.
[4696.56 --> 4696.84]  Yeah.
[4696.92 --> 4697.52]  How do we profit?
[4697.52 --> 4703.12]  But they have an open source programs office, for example, and they hire like Kafka core
[4703.12 --> 4706.44]  maintainers to make sure that the software that we're selling to our customers stays well
[4706.44 --> 4706.80]  maintained.
[4706.80 --> 4710.74]  So that's why, that's what kind of drew me there is it aligns really well with my values.
[4710.92 --> 4715.48]  And I still love MongoDB, still love Drupal, but that idea of like building something that
[4715.48 --> 4720.34]  can really be used to build anything and all powered off, you know, open source, like true
[4720.34 --> 4721.16]  open source stuff.
[4721.42 --> 4722.02]  That's awesome.
[4722.16 --> 4722.82]  So that's why I'm there.
[4723.04 --> 4724.36]  So what is it you do there then?
[4724.48 --> 4724.76]  Particularly.
[4725.20 --> 4725.48]  Yeah.
[4725.58 --> 4725.72]  Yeah.
[4725.84 --> 4726.34]  I'm not.
[4726.48 --> 4726.64]  Yeah.
[4726.64 --> 4727.84]  I'm director of community.
[4728.02 --> 4728.28]  Okay.
[4728.56 --> 4731.68]  So that means that we're, you know, handling meetups.
[4731.78 --> 4735.48]  We're doing things like our community forums, our real time communities, that kind of thing.
[4735.52 --> 4739.92]  Trying to bring together practitioners of open source data infrastructure broadly, whether
[4739.92 --> 4744.24]  we offer it on our platform or not, to kind of come together and talk about the problems
[4744.24 --> 4747.16]  that they're having and some of their pain points and some of their tips and tricks and
[4747.16 --> 4747.72]  stuff like that.
[4747.76 --> 4750.32]  Because it's a really fascinating thing to be part of.
[4750.86 --> 4754.54]  And, you know, a lot of people don't realize that there are open source alternatives for like
[4754.54 --> 4756.56]  data warehousing or some of these other challenges.
[4756.64 --> 4757.14]  So, yeah.
[4757.30 --> 4758.14]  So that's why I'm in it.
[4758.48 --> 4760.30]  Do you interface with the Ospo by any chance?
[4760.56 --> 4760.76]  Yeah.
[4761.06 --> 4761.24]  Yeah.
[4761.32 --> 4761.50]  Okay.
[4761.60 --> 4761.74]  Yeah.
[4761.78 --> 4764.16]  I mean, with the caveat, I'd only been there like three weeks.
[4764.28 --> 4764.80]  So like, who knows?
[4764.90 --> 4765.20]  But yeah.
[4765.56 --> 4765.76]  Yeah.
[4765.80 --> 4767.08]  The Ospo people are amazing.
[4767.22 --> 4770.46]  And it reminds me a lot of the work that we did at Acquia around Drupal, right?
[4770.46 --> 4774.12]  It wasn't called an Ospo, but it was very much like, what's the best thing for this
[4774.12 --> 4774.72]  project?
[4775.22 --> 4775.48]  Right.
[4775.66 --> 4779.58]  That's the thing we have to focus on, whether or not it's good for the business as a whole,
[4779.70 --> 4782.72]  because those are, they're separate, but hopefully there's a Venn diagram, but they
[4782.72 --> 4784.30]  could be separate and competing concerns.
[4784.88 --> 4786.84]  Every Ospo has a level of maturity.
[4786.94 --> 4788.28]  What do you think yours is at?
[4788.32 --> 4792.38]  Without calling it immature, like what level are they fighting against?
[4792.38 --> 4795.46]  Honestly, I don't know if I'm qualified to say that, but I mean, they're in the to-do
[4795.46 --> 4795.84]  group.
[4796.24 --> 4797.70]  They're a member of the OpenSSF.
[4797.76 --> 4800.16]  So I feel like they are, they're doing the right things.
[4800.22 --> 4801.34]  They're contributing in the right ways.
[4801.56 --> 4801.62]  Right.
[4801.74 --> 4804.66]  And they're also employing, you said, Kafka maintainers and stuff like that.
[4804.74 --> 4804.90]  Yeah.
[4805.00 --> 4805.20]  Yeah.
[4805.30 --> 4805.56]  Yeah.
[4805.86 --> 4809.44]  And yeah, there's like Postgres, a couple of people, there's like, you know, from different,
[4809.72 --> 4814.14]  like, you know, again, they want to make sure that the technologies that we rely on for
[4814.14 --> 4815.12]  our customers stick around.
[4815.48 --> 4815.66]  Right.
[4815.68 --> 4818.74]  And I think that that's really awesome because not, they wouldn't have to do that, right?
[4818.74 --> 4822.02]  They could just sell the stuff and not give back, but they're choosing to do it.
[4822.12 --> 4822.48]  So, yeah.
[4823.36 --> 4823.64]  Cool.
[4823.96 --> 4827.68]  But on the maintainership thing, yeah, I do think that that is a general problem.
[4827.70 --> 4831.80]  That people need to think about is like right now you're in this, you love it.
[4832.16 --> 4835.86]  You know, you could do this the rest of your life, but realistically your life's going to
[4835.86 --> 4837.26]  change over the course of your life, right?
[4837.26 --> 4837.46]  Right.
[4837.72 --> 4840.60]  You maybe, you know, get, you know, different hobbies.
[4840.72 --> 4842.56]  Maybe your interest in technology's changed.
[4842.62 --> 4843.78]  Maybe you have a kid, whatever.
[4844.22 --> 4844.42]  Yeah.
[4844.50 --> 4847.38]  And so it's really important to think about that as you're maintaining your product
[4847.38 --> 4850.60]  and your project to make sure that you're, you're thinking about who's going to take
[4850.60 --> 4853.78]  that on when you have to step away so that you can step away when you need to.
[4854.04 --> 4854.18]  Yeah.
[4854.18 --> 4854.48]  Yeah.
[4854.48 --> 4858.54]  One of the themes for me, I didn't put it in my notes actually.
[4858.62 --> 4863.50]  One of the themes for maintainer or for maintainer month and maintainers, I believe, is like
[4863.50 --> 4867.82]  essentially finding a way to step back, finding a way to have succession planning and stuff
[4867.82 --> 4868.26]  like that.
[4868.46 --> 4871.92]  Do you, as part of your leadership, talk at all about that?
[4872.22 --> 4876.74]  Like that kind of maturity of a maintainer and supporting folks that, to anti-burnout essentially.
[4876.74 --> 4877.14]  Yeah.
[4877.14 --> 4877.26]  Yeah.
[4877.58 --> 4877.94]  Yeah.
[4878.06 --> 4883.10]  So we, we do things like have what are called, oh my God, what is the word?
[4883.40 --> 4884.12]  This is so bad.
[4885.62 --> 4886.66]  Ah, provisional.
[4886.80 --> 4887.20]  That's the word.
[4887.30 --> 4888.20]  Provisional maintainers.
[4888.34 --> 4892.70]  So we find people that are kind of active and doing the right things in the right subsystems.
[4892.80 --> 4896.58]  We'll kind of find those people, pull them in and say, hey, would you like to become
[4896.58 --> 4897.44]  a provisional maintainer?
[4897.44 --> 4902.06]  A provisional maintainer doesn't get commit access necessarily, but they are allowed to
[4902.06 --> 4906.32]  like make, okay, this RTBC, sorry, reviewed and tested by community patch.
[4906.38 --> 4908.02]  It's like, it's gone through the review process.
[4908.26 --> 4911.66]  This patch is good to go and they can escalate it to committer to actually commit it.
[4911.74 --> 4914.64]  And after they've done that for a little bit of time, then we do give them commit access,
[4914.90 --> 4917.58]  but maybe just to their own subsystem and not the whole of core.
[4917.78 --> 4919.40]  And then later they kind of grow into that.
[4919.40 --> 4920.72]  So we have like a progression model.
[4921.18 --> 4926.34]  What we're also exploring is the idea of term limits on a committer as well.
[4926.34 --> 4929.78]  Um, because, uh, terms and term limits, I should say.
[4929.88 --> 4933.70]  So terms meaning you're not signing up to something for life necessarily.
[4933.90 --> 4938.06]  Why don't you sign up for something for say three years and we stagger it so that not all
[4938.06 --> 4941.72]  of the committers come on at the three year mark and then now there's no, right.
[4941.72 --> 4942.06]  Right.
[4942.12 --> 4945.72]  But like stagger it so that, you know, there's still a group of people to help bring on the
[4945.72 --> 4946.20]  new folks.
[4946.42 --> 4950.18]  But then it's a lot easier to make a commitment or for your business to make a commitment.
[4950.18 --> 4954.78]  If you're employed by somebody to say, okay, we can pay you for say 20% of your time
[4954.78 --> 4955.38]  for three years.
[4955.38 --> 4959.48]  That's an investment we can make versus 20% of your time indefinitely is a lot harder
[4959.48 --> 4959.98]  to ask.
[4960.50 --> 4965.16]  Um, and then we're talking also about term limits, which means once you've done, let's
[4965.16 --> 4969.08]  say two, three year rotations, then you have to take a year off.
[4969.08 --> 4972.60]  And you know, if you want to come back great, but otherwise like we're going to make you
[4972.60 --> 4977.54]  go out there, build some stuff, you know, and get, get familiar with what the field is
[4977.54 --> 4977.76]  doing.
[4977.86 --> 4978.24]  That kind of thing.
[4978.24 --> 4980.34]  See if this is still what makes you passionate in the summer.
[4980.36 --> 4981.42]  It's probably forced vacation.
[4981.92 --> 4982.18]  Yeah.
[4982.38 --> 4983.76]  In a way it is.
[4983.76 --> 4985.76]  Yeah.
[4985.76 --> 4986.76]  Yeah.
[4986.76 --> 4987.76]  Yeah.
[4987.76 --> 4988.76]  Yeah.
[4988.76 --> 4992.08]  And they just keep working through it and some companies allow that, but this is kind
[4992.08 --> 4993.36]  of like, it's kind of like that.
[4993.44 --> 4994.04]  It's forced vacation.
[4994.18 --> 4994.32]  It is.
[4994.36 --> 4996.48]  And it's, it's coming from a place of love.
[4996.54 --> 4996.88]  You know what I mean?
[4996.88 --> 4999.84]  It's like, it's coming from a place of, you're probably not going to do this unless you're
[4999.84 --> 5003.34]  forced to, but forcing you to really gives you that, huh?
[5003.46 --> 5003.70]  Okay.
[5003.70 --> 5005.76]  Like I don't need that responsibility anymore.
[5005.76 --> 5009.54]  Or, and then if I want to go back willingly, I'm able to, but we're not stuck with people
[5009.54 --> 5012.74]  who maybe should have moved on a while ago.
[5012.84 --> 5013.06]  Yeah.
[5013.54 --> 5017.18]  And just feel like they can't because they're like, everyone's depending on me, you know,
[5017.18 --> 5017.72]  that kind of thing.
[5017.92 --> 5017.94]  So.
[5018.02 --> 5021.28]  Well, they feel like that, but it's not, it's kind of true, but it's kind of not true.
[5021.32 --> 5023.34]  They're like, that person should really take a break.
[5023.70 --> 5023.94]  Yeah.
[5023.94 --> 5024.56]  But they will not.
[5024.70 --> 5024.90]  So.
[5025.72 --> 5025.92]  Yeah.
[5025.92 --> 5026.68]  I mean, that was the thing.
[5026.68 --> 5030.28]  Like I stepped away and I was super active, but it's like Drupal's still fine.
[5030.44 --> 5030.96]  You know what I mean?
[5031.08 --> 5033.28]  Like, it's like Drupal's doing fine.
[5033.90 --> 5035.32]  Everybody's still getting their stuff done.
[5035.60 --> 5039.84]  And you know, it's, it, it proves that out that it's like, even if someone is like neck
[5039.84 --> 5042.64]  deep in everything, you know, it's fine.
[5042.74 --> 5043.62]  Like step away.
[5043.62 --> 5045.94]  If you need to step away, the project will figure it out.
[5046.16 --> 5047.66]  I had this epiphany a while back.
[5047.68 --> 5051.02]  Cause I listened to and read Seth Godin's book, Lynchpin.
[5051.26 --> 5051.56]  Okay.
[5051.66 --> 5053.30]  And if you read, have you read that book or know of it?
[5053.74 --> 5055.38]  Well, Lynchpin essentially is like your crucial.
[5055.38 --> 5058.98]  The Lynchpin in a wagon wheel was what kept the wheel on the thing.
[5059.18 --> 5063.96]  So if you're the Lynchpin, you've got to be there to do the job so that the wagon wheel
[5063.96 --> 5065.62]  stays on the wagon and the wagon keep moving.
[5066.04 --> 5070.36]  And I learned a long time ago, I'd rather be a cog because at some point somebody else
[5070.36 --> 5073.32]  is going to like be better or be more hungry than I am.
[5073.46 --> 5075.94]  And I'm not really the Lynchpin I thought I was.
[5076.32 --> 5079.66]  So might as well just be a very purposeful cog.
[5079.92 --> 5080.80]  I do my job well.
[5080.84 --> 5083.12]  I serve my team well, and I don't have to be a Lynchpin.
[5083.14 --> 5084.02]  I can be very important.
[5084.02 --> 5087.84]  I can have an important role and play a crucial role, but I'm not a Lynchpin.
[5088.04 --> 5092.56]  I'm more of a cog in a better machine as opposed to get the things done.
[5092.74 --> 5094.26]  Let me give you a slightly different analogy.
[5094.32 --> 5094.44]  Sure.
[5094.58 --> 5098.80]  Because yes and, think of yourself as like, you're like the drummer in the band, right?
[5098.96 --> 5099.16]  Right.
[5099.22 --> 5102.94]  The drummer in the band kind of sits back, just kind of does his thing or her thing,
[5103.18 --> 5105.88]  and makes sure that the beat's going on and this kind of thing.
[5106.04 --> 5110.86]  And then you let someone else be the lead singer and the guitarist, you know, like doing that kind of stuff.
[5110.86 --> 5113.40]  You know, because you still have a really important role to play.
[5113.50 --> 5116.40]  And I don't think calling yourself a cog is like doing service to that, you know?
[5116.44 --> 5116.98]  Because it's like...
[5116.98 --> 5118.78]  Every once in a while, you have a drum solo.
[5119.10 --> 5119.76]  Yeah, yeah, yeah.
[5119.76 --> 5119.78]  Every once in a while.
[5119.78 --> 5121.06]  But not the whole time, right?
[5121.22 --> 5121.68]  Like let other people shine.
[5121.68 --> 5123.78]  No, if it's the whole time, people start walking.
[5124.00 --> 5125.80]  Tiny symbol crash just noise, you know?
[5125.86 --> 5127.36]  You can't have a whole thing be a drum solo.
[5127.36 --> 5131.52]  The reason I think I came up with cog was there was an analogy between linchpin and cog.
[5131.72 --> 5131.98]  Oh, all right.
[5131.98 --> 5135.50]  Because the cog is like the thing that is just part of the bigger clock, you know?
[5135.52 --> 5138.70]  But the clock wouldn't work if one or two of the cogs broke, right?
[5139.10 --> 5140.50]  It wouldn't take time the same way.
[5140.76 --> 5143.06]  Not to nitpick your analogy, but while we're doing this.
[5143.12 --> 5143.82]  Sure, please.
[5144.20 --> 5145.64]  This is Jared's MO, please.
[5145.64 --> 5146.68]  It's a different way.
[5146.80 --> 5147.70]  Well, Jared, let's go.
[5147.70 --> 5149.22]  I cannot wait to hear this.
[5149.82 --> 5152.36]  If you pull a cog out of something, it's still going to bust.
[5153.16 --> 5155.10]  So isn't each cog in its own way a linchpin?
[5155.36 --> 5155.76]  Ooh.
[5155.76 --> 5158.68]  I think the yes.
[5159.30 --> 5159.74]  Okay.
[5160.06 --> 5160.98]  To use Andy's.
[5161.04 --> 5161.72]  Yes and.
[5162.30 --> 5166.42]  So a linchpin is like it all breaks if I break.
[5166.52 --> 5167.46]  It all rests on my shoulders.
[5167.58 --> 5171.78]  There's far more superiority to some degree, so much more pressure.
[5172.08 --> 5176.68]  Whereas if you're just a cog, you can be replaced with another cog that's similar.
[5176.68 --> 5177.00]  Oh, I see.
[5177.12 --> 5181.78]  Whereas a linchpin is like there's only one of me, and if I break, everything breaks, and there's no replacing me.
[5181.90 --> 5182.16]  Okay.
[5182.32 --> 5183.58]  So you can't buy another linchpin.
[5183.58 --> 5184.30]  It's challenging.
[5184.38 --> 5185.44]  Well, linchpins are hard to come by.
[5185.44 --> 5185.84]  Okay.
[5186.64 --> 5188.98]  I didn't know that part, so I think the analogy holds better.
[5189.06 --> 5191.42]  I figure in linchpin, you just got another one somewhere else.
[5191.66 --> 5192.44]  Shove it in there.
[5193.08 --> 5194.28]  Maybe a stick if you need to.
[5194.60 --> 5194.98]  I don't know.
[5195.34 --> 5195.72]  You could.
[5196.10 --> 5197.34]  The stick might break eventually.
[5197.40 --> 5198.66]  Just MacGyver something in there.
[5198.92 --> 5199.96]  Some duct tape and some safety pins.
[5199.96 --> 5202.28]  We'll have to actually get Seth to talk us through this because.
[5202.30 --> 5202.50]  Okay.
[5202.56 --> 5203.88]  Because he uses that exact analogy.
[5204.06 --> 5204.98]  The whole book's called linchpin.
[5204.98 --> 5206.06]  He tells you to be a cog, though?
[5206.60 --> 5206.76]  No.
[5206.82 --> 5207.66]  He says be a linchpin.
[5207.90 --> 5208.16]  Okay.
[5208.44 --> 5208.68]  Oh.
[5208.68 --> 5210.92]  That part I get, but the cog, you pulled the cog in.
[5211.26 --> 5212.10]  I said the cog.
[5212.16 --> 5212.34]  Okay.
[5212.34 --> 5212.74]  This is me.
[5212.82 --> 5213.50]  I made this up.
[5213.60 --> 5213.82]  Okay.
[5213.82 --> 5215.34]  I'm like, I love that book.
[5215.42 --> 5219.26]  I love the idea of that book, but I don't want to be so focused on my importance that
[5219.26 --> 5220.62]  I have to be this linchpin with all this pressure on me.
[5220.62 --> 5221.86]  He tells you to be the linchpin?
[5222.02 --> 5222.28]  Yes.
[5222.28 --> 5223.28]  He tells you to be the linchpin.
[5224.22 --> 5227.78]  Well, I guess there's job security in that, but it seems like I'd rather be a cog.
[5228.64 --> 5231.16]  It's a lot of pressure and a lot of responsibility.
[5231.40 --> 5232.32]  I'd rather be a drummer.
[5232.76 --> 5233.08]  Yeah.
[5233.52 --> 5234.14]  Keep the beat.
[5234.24 --> 5234.60]  Keep the beat.
[5234.62 --> 5234.78]  Yeah.
[5234.82 --> 5235.24]  Keep the beat.
[5235.60 --> 5239.88]  Because, you know, it's like linchpins are great for a business, but they sure do get
[5239.88 --> 5240.64]  divorced a lot.
[5240.74 --> 5241.10]  You know what I mean?
[5241.14 --> 5242.28]  It's just like, you know what I mean?
[5242.28 --> 5243.22]  It's like the 10Xers.
[5243.34 --> 5243.62]  Yeah.
[5243.62 --> 5244.68]  It's like the linchpins.
[5244.94 --> 5245.82]  Be the 1Xer.
[5245.82 --> 5246.46]  1Xer.
[5246.62 --> 5248.36]  You know, that might run things poorly.
[5249.40 --> 5251.58]  You know, it's the, I'm very important.
[5251.58 --> 5252.56]  I can't be replaced.
[5252.74 --> 5253.56]  I'm super crucial.
[5254.26 --> 5259.64]  And yeah, there's unhealthy balances, I'm sure, that ensue as a result of calling yourself
[5259.64 --> 5260.06]  a linchpin.
[5260.14 --> 5264.90]  Whereas if you're a very purposeful cog, that's where I fight for.
[5265.00 --> 5269.26]  Like if I know my purpose and I can deliver that purpose and I'm 14, because a cog is not
[5269.26 --> 5272.22]  an individual or it's, a cog is not, yeah, not an individual.
[5272.36 --> 5273.18]  It's a part of a larger whole.
[5273.22 --> 5273.40]  Exactly.
[5273.58 --> 5275.78]  So if you understand the working system, you're part of the working system.
[5275.86 --> 5278.72]  But if you're a linchpin, it's like, well, it doesn't work unless I work.
[5278.80 --> 5279.10]  I see.
[5279.12 --> 5279.40]  You know what I mean?
[5279.40 --> 5280.72]  There's a difference in psychology there.
[5280.72 --> 5281.02]  Yeah.
[5281.02 --> 5281.56]  In my opinion.
[5282.04 --> 5282.48]  I like it.
[5282.70 --> 5285.86]  As long as you have some spare cogs, because otherwise you pull a cog out, the whole thing
[5285.86 --> 5286.26]  falls apart.
[5286.36 --> 5286.76]  For sure.
[5287.08 --> 5287.90]  Especially on a watch.
[5289.56 --> 5289.78]  Anyway.
[5290.40 --> 5290.88]  All right, Angie.
[5291.04 --> 5291.48]  Well, thank you.
[5291.62 --> 5292.08]  Thank you.
[5292.18 --> 5292.32]  Yeah.
[5292.36 --> 5293.78]  It was wonderful catching up with you guys again.
[5293.90 --> 5294.54]  It's always fun.
[5294.74 --> 5295.06]  Okay.
[5295.06 --> 5301.34]  You know, I really have to agree with Dr. Don Foster.
[5301.34 --> 5302.34]  That catching up with people.
[5302.34 --> 5305.34]  That catching up with people is really, really good.
[5305.34 --> 5308.18]  Jared and I really enjoy this hallway track series.
[5308.18 --> 5308.58]  We do.
[5308.58 --> 5313.80]  When we go to conferences like this, it really takes a lot out of us, but it also puts a lot
[5313.80 --> 5314.80]  right back into us.
[5314.80 --> 5321.84]  Because we get to do shows like this, to have an anthology episode like this with many voices,
[5321.84 --> 5328.08]  many perspectives on how to open source, how to maintain open source, how to support open
[5328.08 --> 5332.82]  source, how to love and support open source software maintainers.
[5332.82 --> 5335.64]  This is why we do what we do.
[5335.98 --> 5343.06]  Because like you, our lives depend on open source software and therefore open source software
[5343.06 --> 5344.14]  maintainers.
[5344.42 --> 5353.34]  So if you haven't yet, head to maintainermonth.github.com and find ways to participate and celebrate
[5353.34 --> 5354.52]  Maintainer Month.
[5354.74 --> 5360.50]  They've got news, a schedule, and a library of resources to tap into.
[5360.50 --> 5363.86]  Again, maintainermonth.github.com.
[5363.86 --> 5370.62]  And also thank you again to our friends at GitHub for helping us get to open source summit
[5370.62 --> 5371.84]  2023 this year.
[5372.04 --> 5373.78]  It was an absolute blast.
[5373.90 --> 5378.52]  We met so many people and it was an awesome experience recording all these episodes.
[5378.90 --> 5386.32]  And once again, a big thank you to our friends at Fastly, Fly, and also Type Sense.
[5386.78 --> 5387.90]  But that is it.
[5387.96 --> 5388.86]  This show is done.
[5388.86 --> 5390.86]  We will see you on Friday.
