[0.00 → 5.80] The answer is it depends, but I think it depends on your role on this pull request, right?
[5.88 → 11.92] So imagine that I maintain an open source, and I'm taking something in from a person that's not from the repo.
[12.18 → 16.20] I would be extra careful, so perhaps I would try to run the code.
[16.20 → 26.70] Usually, I don't really test the code, but again, if it's something that I feel that's really critical, and I want to be sure that's 100% working, I might test it.
[30.00 → 34.38] This episode is brought to you by Source graph.
[34.86 → 39.30] Source graph is universal code search to let you move fast, even in big code bases.
[39.38 → 46.54] Here's CTO and co-founder, Bing Lu, explaining how Source graph helps you to get into that ideal state of flow in coding.
[46.72 → 51.70] The ideal state of software development is really being in that state of flow.
[51.70 → 62.04] It's that state where all the relevant context information that you need to build whatever feature or bug that you're focused on building or fixing at the moment, that's all readily available.
[62.20 → 67.58] Now, the question is, how do you get into that state where you don't know anything about the code necessarily that you're going to modify?
[67.96 → 70.24] That's where Source graph comes in.
[70.50 → 73.60] And so what you do with Source graph is you jump into Source graph.
[73.70 → 77.04] It provides a single portal into that universal code.
[77.04 → 80.68] You search for the string literal, the pattern, whatever it is you're looking for.
[80.80 → 83.86] You dive right into the specific part of code that you want to understand.
[84.24 → 97.00] And then you have all these code navigation capabilities, jump to definition, find references that work across repository boundaries that work without having to clone the code to your local machine and set up and mess around with editor config and all that.
[97.12 → 102.46] Everything is just designed to be seamless and to aid in that task of, you know, code spelunking or source diving.
[102.46 → 110.64] And once you've acquired that understanding, then you can hop back in your editor, dive right back into that flow state of, hey, all information I need is readily accessible.
[110.86 → 115.32] Let me just focus on writing the code that influenced the feature or fixes the bug that I'm working on.
[115.68 → 117.82] All right. Learn more at Sourcegraph.com.
[117.92 → 125.94] And also check out their bi-monthly virtual series called DevToolTime covering all things DevTools at Sourcegraph.com slash DevToolTime.
[132.46 → 142.08] Let's do it.
[142.74 → 143.72] It's Go Time.
[144.42 → 149.56] Welcome to Go Time, your source for diverse discussions from all around the Go community.
[150.08 → 152.04] Subscribe to the pod if you haven't yet.
[152.18 → 154.86] Head to GoTime.fm for all the ways.
[155.12 → 157.56] And if you dig the show, please do tell your friends.
[157.74 → 158.50] That'd be pretty cool.
[158.50 → 164.04] Special thanks to our partners at Vastly for shipping all of our pods superfast to wherever you listen.
[164.26 → 165.98] Check them out at Fastly.com.
[166.20 → 167.96] And to our friends at Fly.io.
[168.42 → 170.54] Host your app servers close to your users.
[170.76 → 171.68] No ops required.
[172.12 → 173.42] Learn more at Fly.io.
[173.74 → 174.62] Okay, here we go.
[176.10 → 179.42] Good part of the day to everyone wherever you're joining from.
[179.98 → 181.36] And here's Angelica and I.
[181.44 → 183.78] We are back to talk about pull requests.
[184.12 → 184.86] Hi, Angelica.
[184.90 → 185.36] How are you doing?
[186.20 → 187.58] I'm very, very well.
[187.58 → 188.20] Thank you.
[188.20 → 194.26] I didn't think the PRs would take two episodes, but I'm surprised and excited that they will.
[194.68 → 197.94] As everything about pull requests always takes a bit longer than expected, huh?
[198.48 → 199.06] That's true.
[200.32 → 202.56] Today we are joined by Anderson.
[202.98 → 203.32] Hello.
[203.60 → 204.74] Hi, how are you doing, Anderson?
[205.18 → 206.26] I'm really, perfect.
[206.34 → 207.68] I'm really happy to be here.
[208.04 → 208.58] Thank you.
[208.86 → 211.46] And you are joining us from the UK.
[212.24 → 212.76] Exactly.
[213.26 → 214.28] What are you doing in the UK?
[214.76 → 216.00] I'm at the Gopher Con UK.
[216.00 → 218.66] So I'm a Brazilian that's based in Berlin.
[219.16 → 222.62] But now I'm here in London, directly from a hotel room.
[222.82 → 223.76] How are you liking it?
[224.22 → 224.98] Oh, it's perfect.
[225.20 → 225.42] Yeah.
[225.80 → 227.66] And you're not just saying that because I'm on the call.
[228.36 → 228.88] No, no.
[229.10 → 229.62] Okay, good.
[229.74 → 230.48] I love the UK.
[230.80 → 233.48] I did an exchange program here for one year and a half in Glasgow.
[233.72 → 234.12] Oh, awesome.
[234.22 → 234.86] So, yeah.
[235.28 → 235.84] I really like it.
[236.18 → 238.12] I mean, I prefer Edinburgh to Glasgow.
[238.64 → 239.44] Unpopular opinion.
[239.68 → 240.46] Yeah, true.
[240.70 → 242.26] I mean, Edinburgh Castle is so incredible.
[242.40 → 243.86] Wait, no, that's the end of the show.
[244.26 → 244.80] Oh, I'm sorry.
[244.86 → 246.06] Getting ahead of myself, Natalie.
[246.14 → 246.48] I'm sorry.
[246.58 → 246.96] I'm sorry.
[249.46 → 251.82] It's fun to go back to in-person conferences, huh?
[252.52 → 253.54] Yeah, that's true.
[253.60 → 254.40] It's really, perfect.
[254.76 → 257.18] Last time that I was here in London, my brother was here.
[257.18 → 262.12] We were like, okay, the place here is going to be small to go for call UK at some point,
[262.32 → 264.76] but then the pandemic, and now I think it's smaller.
[265.40 → 266.10] So, yeah, let's see.
[267.26 → 267.70] Okay.
[268.18 → 270.16] So, Anderson, tell us about yourself.
[270.24 → 270.88] You're doing Go.
[271.50 → 276.20] Yeah, I'm doing Go since a bit before going to Berlin.
[276.44 → 278.66] So, I think about five years now.
[279.20 → 282.34] I did before many Java was a lot of Java.
[282.34 → 289.02] I started with C, actually, some Python, JavaScript in the back end, and now Go.
[289.08 → 289.56] I love it.
[289.68 → 292.06] And then it chooses my language to specialize.
[292.74 → 294.26] And you're working at Elastic.
[294.70 → 295.04] Exactly.
[295.58 → 296.96] I work with the Elastic agent.
[297.32 → 301.80] Which is the head product for all the products that we know and love, like Elasticsearch.
[302.18 → 302.82] Yeah, exactly.
[303.20 → 303.38] Yeah.
[303.86 → 305.64] Formerly known as the ilk stack.
[306.32 → 306.62] Yeah.
[306.94 → 308.12] Now the Elastic stack.
[308.26 → 308.40] Yeah.
[308.78 → 309.50] Lots of goes there.
[309.50 → 311.50] I love this stack.
[312.34 → 313.02] Fun.
[313.38 → 315.96] And so, as part of the jobs, you do pull requests.
[316.46 → 316.86] Of course.
[317.22 → 319.00] Do you also do merge requests?
[319.64 → 321.06] We call everything pull requests.
[321.94 → 322.34] Yeah.
[322.52 → 325.22] Are you going to do the same thing you did last time, where you caught us all off guard,
[325.34 → 326.40] with the many different...
[326.40 → 327.08] Just for those.
[327.34 → 329.94] The many different ways to refer to it.
[330.06 → 333.40] It's crazy how many ways there, how many names are there for this.
[333.54 → 333.70] Yeah.
[334.00 → 336.92] For those who are listening now and have not listened to the previous episode,
[336.92 → 340.84] to the art of pull requests part one, Angelica and I were discussing,
[340.84 → 345.72] among other things, also the many different names and what concepts that represent.
[346.36 → 350.46] So, Anderson, we asked you if you're doing lots of pull requests, but then we started talking about other things.
[350.88 → 351.34] Yeah.
[351.52 → 351.78] Do you?
[352.12 → 352.66] I do.
[353.24 → 355.70] Do you review more or do you write more?
[355.70 → 357.14] Now, I write more.
[357.28 → 359.92] My past job, I read a lot more code.
[360.52 → 361.84] A lot of pull requests.
[362.58 → 365.76] And funnily enough, I've never worked in a company that didn't have pull requests.
[365.86 → 371.04] To me, software development as a professional means pull requests and code review.
[371.86 → 372.80] That's my standard.
[373.40 → 376.74] Why did you do more reading in your past job?
[376.80 → 378.78] Is it just a very different area you were working in?
[378.78 → 379.18] No.
[379.40 → 385.42] My past company, I joined, among other things, to help to lead the transition to Go.
[385.56 → 385.88] Right.
[385.98 → 390.12] So, they were pretty much a ruby shop, and they decided to migrate to Go.
[390.56 → 395.40] They were migrating, but they needed someone with expertise in Go, you know, to bring back
[395.40 → 396.54] practice, how to do.
[396.54 → 403.20] So, as that, I did a lot of workshops and, you know, kind of teaching mentoring and involved
[403.20 → 406.20] a lot of the teams would come to me with pull requests.
[406.78 → 412.22] So, I do like a really extensive review, not only code practice functionality, but also
[412.22 → 417.30] as an opportunity to teach Go and the standards, the conventions, the best practices.
[418.10 → 420.36] And then now you've moved to somewhere where Go is bigger.
[420.58 → 423.50] So, therefore, you don't have to play such a big kind of reviewer role.
[423.70 → 424.04] Exactly.
[424.04 → 428.78] And now I am as a soft engineer, right, as a senior, but there I was like a tech lead.
[429.40 → 433.82] Yeah, I think when you go above senior and in tech lead and stuff, you start coding less,
[433.92 → 435.58] reading more, writing more, right?
[435.78 → 436.16] Okay.
[436.64 → 439.36] I mean, writing more specifications and documentations.
[440.04 → 446.88] So, do you feel like there's a direct correlation between seniority and how much reading of PR
[446.88 → 449.04] versus writing you do?
[449.04 → 454.86] Like if we were to plot it on a graph, how much you read PRs, how much you write, could
[454.86 → 459.56] we like to generalize the industry say that the more senior you are, the less you're going
[459.56 → 461.62] to be writing PRs and the more you're going to be reviewing them?
[462.00 → 467.22] I think the more you're a senior, you're going to look for more things, right?
[467.22 → 471.54] So, because you're going to be able to evaluate, if you're good in the language, you can evaluate
[471.54 → 473.24] the language, the conventions, right?
[473.28 → 476.04] You can evaluate the general soft architecture, right?
[476.38 → 480.36] When you're in a role that as a senior, you are also a mentor, there is a lot of like
[480.36 → 481.68] mid and juniors in the team.
[481.76 → 485.52] I think we're reading a lot because you have this responsibility with the team, with the
[485.52 → 485.94] product.
[485.94 → 492.68] But if you're in a company where everyone's senior, senior, in Berlin, definitely the titles
[492.68 → 493.26] are inflated.
[493.78 → 499.10] So, you know, perhaps everyone doesn't need this level of attention and mentoring or teaching
[499.10 → 501.66] that happens a lot through PRs.
[502.12 → 503.12] That's an interesting question.
[503.22 → 503.32] Yeah.
[503.36 → 507.34] Because some time ago, they added this like graph of contributions that is no longer just
[507.34 → 510.90] the squares, but also what type do you read more?
[510.98 → 511.90] Do you make more issues?
[512.06 → 513.16] Do you review and so on?
[513.16 → 517.22] So if you can look at that, then you kind of know what people's roles are or see how
[517.22 → 518.68] it changes over time or something.
[519.00 → 522.82] If I showed you a load of graphs, would you be able to guess the seniority of that engineer?
[523.30 → 523.74] Perhaps.
[524.12 → 527.42] I think I looked quickly at mine, and now it was 50-50.
[527.76 → 528.16] Nice.
[528.38 → 528.64] Okay.
[528.70 → 529.16] Pretty much.
[529.48 → 532.56] Do you think that that's the balance that most engineers would like?
[533.16 → 537.36] Or do you think that there is such thing as someone who prefers to be reviewing more than
[537.36 → 537.74] writing?
[538.40 → 542.86] I think when you think as a soft engineer that the passion is about writing, writing,
[543.16 → 545.12] right, they rather write code.
[545.64 → 551.38] I think at least either you want or you need to pass knowledge forward, right?
[551.42 → 554.10] So you're going to need to write, to read.
[554.46 → 557.06] I really like to review code for both reasons, right?
[557.14 → 562.02] One, because I have a passion for code, and I am a quite method person.
[562.02 → 565.44] So I like to ensure that the code is good.
[566.20 → 567.84] The conventions are there.
[568.22 → 570.60] I'm super picky about proper error handling.
[571.32 → 575.72] So these are some things that if you're not handling the errors properly, or you're really
[575.72 → 578.64] bad at the conventions, I'm going to be commenting there.
[579.08 → 584.58] But I have a special of commenting to ensure that I'm not overwhelming the other person or
[584.58 → 587.58] to feel like just complaining, saying that your job's bad.
[587.58 → 589.92] So you say you try to give feedback.
[590.26 → 592.04] You don't want to overwhelm the person.
[592.62 → 593.58] How do you do that?
[593.66 → 597.80] Like, is it that you limit yourself to, OK, I'm only going to put six comments?
[598.04 → 601.00] Is it the way in which you phrase your review?
[601.12 → 603.00] How do you make sure that you're not overwhelming?
[603.96 → 607.14] Yeah, I learn to experience any feedback.
[607.32 → 608.48] I put tags, right?
[608.52 → 613.74] So I start with PR with like suggestion, or sometimes I put question, but a question is
[613.74 → 614.28] a question, right?
[614.28 → 619.62] You know, so it feels a bit redundant, but I put, and then I have blocker, right?
[619.66 → 622.56] And sometimes like suggestion slash go convention, right?
[622.70 → 628.56] Or depending on the repo, blocker slash go convention, you know?
[628.64 → 633.00] So I try to categorize suggestion, question, and blocker.
[633.12 → 634.34] I put blockers.
[634.48 → 638.84] So basically blocker is either I see there is a problem in the code, right?
[638.84 → 644.96] So it needs a change, or I believe there is a problem, or I don't believe that this implementation
[644.96 → 645.64] is good.
[645.76 → 648.16] So at least you need to answer that, right?
[648.20 → 649.44] You can say like, it's agree with you.
[649.82 → 650.28] That's fine.
[650.36 → 652.46] But I need an explanation, right?
[652.48 → 653.66] So these are the blockers.
[654.32 → 655.48] Suggestion is exactly that.
[655.54 → 657.06] Like, I believe it can be better.
[657.32 → 662.14] If I were writing this code, I would do different, but you don't have to take it.
[662.14 → 664.60] Sometimes I put like a nit.
[665.00 → 669.78] It can be, you know, just erase this blank line between the function call and the error
[669.78 → 670.84] handling, right?
[670.88 → 671.78] This is a nit, right?
[671.98 → 672.82] Or typo.
[673.28 → 674.04] So these things.
[674.24 → 680.60] And then if I've never reviewed a PR from this person, or perhaps I see there's a lot
[680.60 → 685.78] of comments, I go to the person or even the PR, I put, look, there is these three categories.
[685.90 → 687.54] The only thing that's really important are the blockers.
[687.54 → 692.98] So the blockers, please comment or change the suggestions are suggestions.
[693.30 → 696.46] And as always, you're free to disagree a hundred percent, right?
[697.02 → 698.98] Just answer the blockers and talk to me.
[699.28 → 700.32] That's how I do.
[700.76 → 705.28] So you said that in some situations, it kind of makes sense to just speak in person instead
[705.28 → 708.14] of writing a lot, for example.
[708.72 → 709.56] Sometimes it's easier.
[710.18 → 712.36] I think sometimes speaking is better.
[712.50 → 714.42] Sometimes writing is better.
[714.42 → 719.04] And on pull requests, writing the pull requests is a lot slower, right?
[719.08 → 722.62] So sometimes it's worth jumping on a Slack chat.
[722.78 → 723.54] Is that right enough?
[723.86 → 724.82] Sometimes we talk.
[725.46 → 731.06] I think nowadays at Elastic, because we are distributed, it's a lot more through Slack
[731.06 → 733.00] rather than really a call.
[733.66 → 737.88] But sometimes I have jumped on a call for small things.
[738.36 → 741.48] And how do you decide when it's better to do this and when it's better to not?
[741.48 → 744.26] Do you have a thumb rule or is it all just feeling?
[744.90 → 748.98] If there is a lot of back and forth, it's easier to jump on a call or something that
[748.98 → 750.18] I really want to understand.
[751.06 → 755.72] But most of the time, I guess, I always could handle the chat.
[756.18 → 758.32] Now, Elastic is a distributed company, right?
[758.36 → 760.42] So we write a lot more.
[760.96 → 764.48] So it's a lot more common just to write than jump on a call.
[764.48 → 766.98] I think jumping on a call is more personal.
[767.86 → 771.58] So I feel if you're close to someone, it's easier.
[771.88 → 773.92] You know, it feels more natural to jump on a call.
[774.12 → 779.00] And if you don't know the person so well or something, you kind of end up just chatting.
[779.50 → 783.10] So you say there's actually three types of kind of giving feedback.
[783.26 → 785.28] One, writing in the pull request.
[785.72 → 787.58] Two, writing on Slack.
[787.72 → 789.28] And three, hopping on a call.
[789.90 → 790.16] Yeah.
[790.66 → 793.62] But on Slack, I use more to clarify.
[793.62 → 794.74] Right?
[795.38 → 798.16] Because it's specific about the code I'd rather have on the pull request.
[798.64 → 800.60] It's kind of documented anyway, right?
[801.28 → 801.64] It's right.
[801.70 → 804.44] I was sure to explain why, what I'm saying.
[805.16 → 811.08] Like, as I said, in my past company, I was really with this job to teach, to mentor and go.
[811.22 → 813.52] I would link a lot of reference, right?
[814.08 → 815.94] Also, because I learned in another company.
[816.26 → 820.34] I remember my colleague and would review a pull request of your new joiner.
[820.72 → 822.48] You know, and say like, oh, yeah, this function is too long.
[822.48 → 823.64] This function is too complex.
[824.04 → 824.14] Right?
[824.16 → 824.58] This happens.
[824.80 → 827.58] And the guy was like, why?
[827.90 → 829.56] Why did you butcher my pull request?
[829.74 → 830.44] Are you guessing?
[830.58 → 831.44] This is your opinion.
[832.00 → 834.02] And I was like, that's true, right?
[834.04 → 836.66] We don't have like a metric to say that.
[837.08 → 839.58] But also it was a common sense between us.
[839.58 → 841.62] So yeah, this is too big, you know, in the company.
[841.74 → 843.08] But this guy was a new joiner.
[843.08 → 844.28] So everything was different from him.
[845.06 → 849.00] So I guess, yeah, clarifications, I can't do outside the pull request.
[849.14 → 853.20] But I think it's important to document what's happening in the code there.
[853.20 → 853.92] Mm-hmm.
[854.22 → 857.30] In the code itself to kind of document, to make it self-explanatory.
[857.70 → 858.10] Exactly.
[858.66 → 862.38] So in terms of kind of, you talked about kind of giving feedback, not overwhelming.
[863.26 → 868.44] Do you feel like PRs are also a good place to kind of, especially for more junior engineers,
[869.00 → 871.24] give them like props on things they're doing well?
[871.44 → 873.68] Like, oh, I really like the way you did this thing.
[873.84 → 875.14] Or, oh, this is great.
[875.24 → 877.36] Or this function is structured really well.
[877.84 → 881.08] Do you feel like PRs are also a way to give positive feedback?
[881.08 → 882.96] Yeah, I think it is.
[883.14 → 884.10] It is important.
[884.90 → 888.24] And it's something that I would like to do more as well.
[888.74 → 893.22] I mean, I never go to a pull request to looking for errors or to try to diminish someone's job.
[893.54 → 897.62] But at the same time, I go to a pull request looking for errors so they don't go to production.
[898.22 → 898.40] Right?
[898.86 → 904.94] At the end of the day, we are looking for problems and issues to prevent things bad going to production.
[905.04 → 905.20] Right?
[905.24 → 910.22] But I think it's super important to do the praise, to assert when someone does something nice.
[910.22 → 914.26] Sometimes someone just fix something a bit random, but, you know, it's the same function.
[914.46 → 917.24] It's not really going away from the aim of the pull request.
[917.38 → 920.32] And then this is perfect to praise, at least a thumbs up.
[920.66 → 926.04] So we said that there are some stages that you escalate the communication to some way.
[926.42 → 933.98] And definitely you want to include more like positive feedback that is not the correctness and so on or explain yourself.
[933.98 → 941.14] What other changes would you make to the PR process based on pain points you have with the flow?
[941.48 → 945.92] It's a really slow process because you write the code, and then you submit the PR.
[946.76 → 946.78] Right?
[946.88 → 951.50] And then someone else's, sometimes more than WordPress, they have to stop and read it.
[951.80 → 953.38] And how do you synchronize that?
[953.38 → 956.54] And then I think it's going to depend on a lot how companies do.
[956.76 → 958.58] I've worked with a different process.
[959.22 → 959.34] Right?
[959.38 → 962.34] Some process, they ensure that the pull request would be reviewed.
[962.50 → 963.44] Some not so often.
[964.12 → 964.30] Right?
[964.82 → 968.08] Now I'm definitely overwhelmed by GitHub notifications.
[969.20 → 973.36] So sometimes it just, it slips through some PRs.
[973.42 → 975.40] And then I get like days later, someone tag me.
[975.52 → 977.58] And so can you give me a review?
[977.70 → 978.68] Like, oh my God, sorry.
[979.24 → 981.64] Because it's something that's kind of a bit of a ping pong?
[982.02 → 984.38] Or does it happen more with new pull requests?
[984.70 → 986.20] And that is when you have to re-review, right?
[986.24 → 988.36] You do the first review and then you have to look again.
[988.64 → 988.90] Yeah.
[989.24 → 989.44] Right?
[989.48 → 992.32] So to get the proper ping, it's hard.
[992.76 → 995.40] And the other thing that, at least on GitHub, right?
[995.54 → 998.32] I have used a bit of Bit buck as well.
[998.78 → 1002.52] I submit one, perhaps two PRs should go to the Gripper.
[1002.52 → 1003.80] So we've got it.
[1004.80 → 1006.80] But on GitHub, it's really hard.
[1006.80 → 1009.54] But when you do the first review, we ask you for changes.
[1009.78 → 1014.48] And then if people do changes to see exactly what changed, right?
[1014.50 → 1017.22] To get an MBA book, okay, I'm going to review just the changes.
[1017.48 → 1018.34] Isn't this a new comment?
[1018.36 → 1019.68] And if someone just forced.
[1019.70 → 1020.50] Oh, forced push.
[1020.58 → 1020.78] Okay.
[1021.26 → 1023.48] If someone's a forced push, right?
[1023.98 → 1029.00] So sometimes it's hard to get like just the bit that they have to re-review.
[1029.48 → 1030.40] That's our main point.
[1030.40 → 1030.80] Yeah.
[1030.94 → 1034.34] I had a Twitter poll the other day on the what do you do when the pull request stretches
[1034.34 → 1037.54] so much and there's 1 million comments that lead to 1 million commits?
[1037.68 → 1038.88] Do you squash that or not?
[1038.98 → 1043.64] And I think the answer that I liked most was during the pull request, have as many commits
[1043.64 → 1044.02] as needed.
[1044.14 → 1048.92] And once it's good to go merged, then squash it all into a readable one or two commits or
[1048.92 → 1050.74] however many logically needed.
[1051.00 → 1055.08] But exactly to allow the proper review, like you say, as many commits as needed.
[1055.34 → 1055.58] Yeah.
[1056.22 → 1056.44] Yeah.
[1056.44 → 1057.60] Definitely good practice.
[1058.04 → 1060.48] So you kind of chatted a little bit about your love of Go.
[1060.56 → 1066.00] This is a Go podcast, but I would love to hear a little bit about your approach to PRs
[1066.00 → 1066.82] in other languages.
[1067.12 → 1067.50] I.e.
[1067.64 → 1071.72] does the way that you review PRs differ depending on the language you're reviewing?
[1072.30 → 1077.64] I think they do differ most because of the expertise, right?
[1077.64 → 1082.80] I'm quite comfortable in Go to understand the language and understand what's happening,
[1083.06 → 1083.28] right?
[1083.74 → 1088.06] To know some caveats, some catches, and also to talk about conventions.
[1089.00 → 1090.58] In other languages, not so much.
[1091.34 → 1096.46] So I guess in other languages, I am going to focus more on general software architecture
[1096.46 → 1099.74] because this is a general frame thing and functionality.
[1100.48 → 1105.98] And of course, try to use as much as I know from the language convention, right?
[1105.98 → 1107.56] I think that's another thing.
[1107.66 → 1110.30] True requests are great, great to learn language conventions.
[1110.54 → 1115.72] So I've learned so much about conventions in Go and the other language through true requests.
[1116.34 → 1117.16] And then that's it.
[1117.24 → 1122.74] If I'm not so expert, I'm going to try to put in point the best that I know.
[1123.18 → 1124.50] But I know that I'm not the expert.
[1124.70 → 1128.26] And a lot of the times, it's probably not really my repo, right?
[1128.32 → 1130.56] So I'm not there to enforce anything.
[1130.96 → 1133.44] So they're going to be more on the suggestion side.
[1133.44 → 1139.64] I mean, taking it kind of one step more granular, are there things that are more important
[1139.64 → 1146.32] for Go when you're reviewing, i.e. like stylistic choices, almost principles that you might adhere
[1146.32 → 1149.90] to more closely than you would in other languages?
[1150.72 → 1152.14] I mean, Go is opinionated.
[1152.40 → 1153.60] You have to use Go Fund.
[1153.88 → 1159.04] You have to format the code properly, even though we still have some space to discuss [1159.04 → 1159.58] how to format.
[1159.58 → 1161.48] But I think that's the first thing.
[1161.92 → 1167.06] I would usually like to be super strict about how the imports are sorted, but I am not.
[1167.54 → 1172.12] Wait, if the rep is consistent, I think it's a lot easier to enforce this thing.
[1172.20 → 1174.04] If it isn't, not so much.
[1174.24 → 1176.72] And all the language, they don't have so much.
[1176.78 → 1180.34] So it's going to be more about team convention rather than the language.
[1180.48 → 1183.38] And in Go, you get a lot from the language.
[1183.38 → 1190.88] I haven't seen so much, but because Go, they're so focused, let's say, right, in concurrence.
[1191.34 → 1196.60] Sometimes people try to either sneak in concurrence when they shouldn't, or they are not using
[1196.60 → 1198.60] the right tools.
[1199.18 → 1201.76] Also because, you know, ah, concurrence, let's use channels.
[1201.92 → 1203.74] No, channels, they're for something.
[1203.98 → 1205.34] In Mute, they're for other things.
[1205.74 → 1207.24] Weight groups, they're for other things, right?
[1207.24 → 1212.78] So this is another thing that I would say, okay, no, perhaps we can do different or we
[1212.78 → 1213.92] can do better, right?
[1213.98 → 1217.14] Or this is too complex to understand.
[1217.52 → 1220.86] If you use, I don't know if you remove this channel, you put in a weight group, it's a
[1220.86 → 1221.24] lot easier.
[1221.76 → 1225.06] And you will, do you want to barrier weight group, right?
[1225.64 → 1227.08] Channels, probably not.
[1227.24 → 1228.48] So I think these things.
[1229.14 → 1235.68] When there are new features and new things released in Go, do we see an uptick in people
[1235.68 → 1237.22] using those and PRs?
[1238.24 → 1241.18] I feel like you just get like, you just get overexcited, like, oh, generics.
[1241.64 → 1243.36] Every PR now has generics.
[1243.68 → 1248.90] I always wanted to push the new things and use the new as soon as possible.
[1249.48 → 1253.50] I think in general, if you're working with microservices, it's a lot easier, right?
[1253.50 → 1257.70] Because you can just update the version and redeploy and even something breaks, you can
[1257.70 → 1258.56] roll back a lot easier.
[1258.92 → 1263.32] Now at Elastic that you're distributing binaries that you're going to go to, I don't know how
[1263.32 → 1265.32] many clients in the whole world.
[1265.32 → 1268.82] So our, we have a release cycle, right?
[1268.88 → 1272.46] So we have to choose, okay, let's change the version.
[1272.70 → 1277.02] We have several reply that use Go and you try to keep everyone in the same version.
[1277.12 → 1278.82] So it's a slower process.
[1279.44 → 1285.60] But as much as I can and as much as I know, all right, what's coming up, I try to incorporate
[1285.60 → 1286.80] if I can.
[1287.78 → 1292.34] Oh, on that topic, have you folks started to use any instead of the empty interface?
[1292.34 → 1295.56] It could be an interesting poll to write.
[1296.18 → 1298.84] I don't know if you can phrase that as an unpopular opinion somehow.
[1299.02 → 1300.32] Don't use that or something.
[1300.58 → 1304.10] It can be one more unpopular opinion for your stash.
[1304.16 → 1305.90] Your library that we're soon going to have.
[1305.90 → 1310.88] I think I saw the first use of it today in the workshop with Bill Kennedy.
[1311.24 → 1313.12] So he, his code had an any.
[1313.20 → 1314.38] I was like, oh yeah, right.
[1314.46 → 1315.42] We can use any now.
[1316.20 → 1317.62] What was the use case that he used?
[1318.16 → 1320.78] Was a map for logger?
[1321.24 → 1321.50] Okay.
[1321.76 → 1323.54] The map string empty interface.
[1323.54 → 1326.02] I think it was in a log or something.
[1326.34 → 1326.52] I know.
[1326.60 → 1328.06] I think he was parsing a JSON.
[1328.72 → 1333.10] And so instead of map string empty interface was map string any.
[1333.52 → 1333.80] Okay.
[1334.08 → 1337.58] Well, we can do the poll and then tag Bill and be like, please tell us.
[1338.70 → 1341.58] Give us the example so we can all understand how you use this.
[1341.74 → 1341.98] Yeah.
[1342.14 → 1344.52] He was asking everyone to have Go 18 because of that.
[1344.64 → 1346.72] He was like, okay, you're going to use any, so please.
[1346.72 → 1363.26] This episode is brought to you by our friends at Fire Hydrant.
[1363.68 → 1366.32] Fire Hydrant is a reliability platform for every developer.
[1366.82 → 1369.32] Incidents are a win, not an if situation.
[1369.78 → 1373.80] And they impact everyone in the organization, not just Sees.
[1373.80 → 1377.44] And I'm here with Robert Ross, founder and CEO of Fire Hydrant.
[1377.78 → 1380.10] Robert, what is it about teams getting distracted by incidents
[1380.10 → 1383.42] and not being able to focus on the core product that upsets you?
[1383.72 → 1387.72] I think that incidents bring a lot of anxiety and sometimes fear
[1387.72 → 1391.94] and maybe even a level of shame that can cause this paralysis
[1391.94 → 1394.60] in an organization from progress.
[1395.18 → 1398.10] And when you have the confidence to manage incidents
[1398.10 → 1401.02] at any scale of any variety,
[1401.02 → 1403.30] everyone just has this breath of fresh air
[1403.30 → 1406.08] that they can go build the core product even more.
[1406.44 → 1408.42] I don't know if anyone's had the opportunity,
[1408.72 → 1410.98] maybe is the word, to call the fire department.
[1411.18 → 1413.70] But no matter what, when the fire department shows up,
[1413.90 → 1416.84] it doesn't matter if the building is hugely on fire.
[1417.00 → 1418.46] They are calm, cool, and collected
[1418.46 → 1420.50] because they know exactly what they're going to do.
[1420.78 → 1423.70] And that's what Fire Hydrant is built to help people achieve.
[1424.18 → 1424.48] Very cool.
[1424.56 → 1425.10] Thank you, Robert.
[1425.10 → 1429.48] If you want to operate as a calm, cool, collected team
[1429.48 → 1431.86] when incidents happen, you got to check out Fire Hydrant.
[1432.18 → 1434.82] Small teams, up to 10 people can get started for free
[1434.82 → 1437.78] with all the features, no credit card required to sign up.
[1438.08 → 1439.76] Get started at firehydrant.com.
[1440.12 → 1442.12] Again, firehydrant.com.
[1452.42 → 1456.32] What do you do when you have a very large pull request?
[1456.68 → 1458.96] Lots of files, lots of comments, lots of lines.
[1458.96 → 1460.18] I sit and cry.
[1460.38 → 1461.84] How do you get on top of that?
[1462.64 → 1463.30] No, I...
[1463.96 → 1464.78] That's a tough one.
[1465.42 → 1467.42] I try to review at once.
[1468.14 → 1469.36] Sometimes it's not possible.
[1470.68 → 1472.90] I think there's no magic.
[1473.08 → 1474.70] You just have to go through it, right?
[1475.12 → 1477.28] Do you review everything on a high level?
[1477.42 → 1479.16] Kind of, you know, see the list of the commits
[1479.16 → 1481.62] if they tell some story or maybe look at the list of the files?
[1481.76 → 1483.24] Or do you just dive to the first one
[1483.24 → 1486.02] and one by one until it starts making sense?
[1486.02 → 1487.98] I never look at the commits.
[1488.16 → 1491.74] I don't know if because when I'm coding and committing,
[1491.94 → 1493.76] I'm going to squash everything before morning.
[1493.94 → 1494.52] Like, first things first.
[1494.62 → 1497.30] So to me, the commits itself, they don't matter so much.
[1497.38 → 1500.62] I try to put in a way if I need to revert something, right?
[1500.70 → 1501.24] I do.
[1501.50 → 1503.46] But at the end of the day, there's a good chance
[1503.46 → 1505.04] that I'm going to just do one commit.
[1505.04 → 1506.72] So I never look at the...
[1506.72 → 1508.64] Neither the rep commit history,
[1508.82 → 1511.02] only if I need to understand why it happened.
[1511.52 → 1513.72] But in a pull request, I never look at the commit history.
[1513.90 → 1514.78] Just look at the diff.
[1515.36 → 1516.76] And it's always on GitHub.
[1517.22 → 1519.54] And look at the files by the name, basically.
[1519.82 → 1521.64] The big ones are just, you know, go clicking.
[1521.74 → 1522.46] I've seen this file.
[1522.60 → 1523.24] I've seen this file.
[1524.18 → 1526.22] So just by the order of appearance.
[1526.22 → 1529.92] Because sometimes it's not always the correct flow, kind of.
[1529.92 → 1530.36] Yeah.
[1530.86 → 1533.56] If it's hard to understand, I get the code.
[1533.68 → 1536.32] I check out the feature branch.
[1537.00 → 1537.76] And I go to see.
[1537.92 → 1541.50] Because also sometimes you'll see, you know,
[1541.54 → 1543.12] there are more stuff going on.
[1543.20 → 1543.84] You want to jump.
[1543.98 → 1546.34] You want to understand how it was called or something.
[1546.66 → 1549.56] And then it's easier on an IDE when you have the code.
[1550.06 → 1552.24] And also if you want to suggest a change.
[1553.02 → 1555.12] So either it's something really simple.
[1555.20 → 1556.56] I'm 100% sure that it works.
[1556.56 → 1560.38] Or I'm going to probably write it in the code itself.
[1560.52 → 1561.50] And it might test it.
[1561.62 → 1562.02] Right.
[1562.10 → 1564.28] To not suggest something that it's broken.
[1564.88 → 1566.36] Maybe even a few steps, Mac.
[1566.48 → 1569.40] When you go to read the review of pull request.
[1569.48 → 1570.88] Do you start by reading the issue?
[1571.42 → 1573.18] So the first thing you do is read the issue.
[1573.60 → 1573.80] Yeah.
[1573.96 → 1575.48] I have to understand what's happened there.
[1575.88 → 1581.00] Then do you review it, the diff, you know, on GitHub or in your IDE?
[1581.72 → 1582.30] No, on GitHub.
[1583.08 → 1585.32] So you go kind of file by file on GitHub.
[1585.32 → 1586.06] I never.
[1587.34 → 1588.20] No, you know, because.
[1588.62 → 1589.40] Philosophical questions.
[1589.80 → 1590.22] Good point.
[1590.54 → 1592.64] Because to me, the review.
[1593.38 → 1595.32] Actually, going back to the other episode.
[1595.66 → 1596.64] We are doing code review.
[1596.76 → 1598.12] It's not the pull request so much, right?
[1598.58 → 1599.14] What's happening?
[1599.80 → 1601.72] You have to comment on it, right?
[1601.76 → 1603.64] So it's really hard to comment on it.
[1604.02 → 1605.64] At least for the tools that I use.
[1605.72 → 1607.44] That's GitHub and the IDE.
[1608.10 → 1609.62] It's hard to comment on the code.
[1609.62 → 1612.98] If it's something that for some reason.
[1613.54 → 1620.14] You know, when you do either a Greenfield project or the pull request is a huge refactor.
[1620.46 → 1621.70] You know, everything changed.
[1621.76 → 1623.20] So pretty much new code.
[1623.20 → 1629.02] So on that rare occasions, I might open the code itself, right?
[1629.38 → 1632.94] Because then I can read in like an execution order, let's say.
[1633.68 → 1637.54] And then my comments, they are probably going to be comments on the code itself.
[1638.22 → 1641.40] And then I've done it, I don't know, once or twice.
[1641.40 → 1644.90] And then I create my branch out of this branch.
[1645.12 → 1647.62] And then I open a pull request for this branch.
[1647.76 → 1651.96] So the person can see my comments in the code without having to look for it.
[1652.34 → 1657.68] But this is pretty much in either Greenfield projects, you know, when you start something new.
[1658.20 → 1661.70] Or when you're just adding so much new code.
[1662.64 → 1666.16] That the pull request itself, it's hard because it's completely out of road and everything.
[1666.34 → 1667.44] And there's a lot to comment on.
[1667.80 → 1669.10] Yeah, that's the hardest ones, right?
[1669.10 → 1671.64] When there's so much to handle there.
[1672.22 → 1672.46] Yeah.
[1672.96 → 1678.14] Do you sometimes find yourself rereading the whole thing to kind of once to read it and second time to make sense?
[1678.94 → 1679.24] Oh, yeah.
[1679.30 → 1680.00] No, yeah, definitely.
[1680.18 → 1680.42] Definitely.
[1680.52 → 1686.26] I think, yeah, going back to like old goal time when they talk about documentation and reading documentation.
[1686.56 → 1687.76] I have the perseverance.
[1688.14 → 1692.06] If I'm not understanding, I'm going to read it over and over and over again.
[1692.06 → 1694.08] And I'm going to do my best to understand.
[1694.40 → 1696.64] If I don't, I'm going to ask, right?
[1696.64 → 1703.36] But I think if someone thinks puzzling me, then I'm probably going to blog say, look, I think this is important.
[1703.48 → 1704.06] I don't get it.
[1704.12 → 1704.88] Please explain.
[1705.34 → 1705.48] Yeah.
[1705.82 → 1707.14] Do you comment as you go?
[1707.24 → 1712.86] Or do you read through fully, digest and then go through and do all your comments?
[1713.62 → 1714.06] No, no.
[1714.18 → 1716.36] I comment as I go, like as I stream.
[1716.48 → 1716.68] Okay.
[1716.68 → 1720.98] And then when I get down there, I was like, oh, yeah, that's the why.
[1721.10 → 1722.40] So I go back and delete the comments.
[1722.54 → 1722.96] Oh, okay.
[1723.16 → 1725.12] You know, it's like, dude, does it make sense?
[1725.24 → 1726.52] You know, something like that.
[1727.00 → 1727.36] Why?
[1727.48 → 1728.32] How does it work?
[1728.38 → 1729.08] And then you read it.
[1729.56 → 1729.64] Oh.
[1730.84 → 1732.98] And then I go back, delete and edit the comments.
[1733.18 → 1733.60] Go back.
[1733.66 → 1734.34] Oh, I'm so sorry.
[1734.42 → 1734.92] Never mind.
[1735.84 → 1738.30] I mean, on GitHub, you don't submit the review, right?
[1738.48 → 1738.70] Yeah.
[1739.02 → 1740.44] So I just delete.
[1740.58 → 1741.84] But the feeling is exactly that.
[1741.92 → 1743.90] I'm apologizing for asking something stupid.
[1743.90 → 1752.16] When you're going over a PR, do you feel like, or any reviewer should test the changes?
[1753.06 → 1758.40] And to what extent should you test the changes if you think that they should be tested by the reviewer?
[1758.86 → 1760.90] I think that's the $1 million question.
[1761.24 → 1762.06] Give us the answer.
[1762.20 → 1762.66] We're ready.
[1762.94 → 1764.32] Maybe another popular opinion.
[1764.32 → 1768.14] No, I think the answer is it depends, right?
[1768.26 → 1768.38] Right.
[1768.72 → 1770.44] We say a lot of that at the last take.
[1770.44 → 1774.30] But I think it depends on your role on this pull request, right?
[1774.38 → 1783.40] So if imagine that I maintain an open source, and I'm taking something from a person that's not from the repo, I would be extra careful.
[1783.64 → 1786.42] So perhaps I would try to run the code.
[1786.84 → 1790.78] Usually I don't really test the code, right?
[1790.78 → 1798.74] But again, if it's something that I feel that's really critical, and I want to be sure that's 100% working, I might test it.
[1799.38 → 1800.42] But it's rare cases.
[1801.12 → 1801.26] Okay.
[1801.70 → 1806.50] And does the length of the PR or the scope of the change that opinion?
[1807.06 → 1807.34] Yeah.
[1807.66 → 1807.92] Okay.
[1808.10 → 1809.84] I think the length, not so much.
[1810.26 → 1810.88] Let's be honest.
[1811.12 → 1815.28] The longer the PR, the less detailed is the review.
[1816.04 → 1816.62] We are humans.
[1816.70 → 1817.18] We get tired.
[1817.44 → 1817.62] Yeah.
[1817.90 → 1818.24] Come on.
[1818.28 → 1823.22] Like, if you're reviewing like 15, 20 files, the last one, you're tired.
[1823.34 → 1824.98] Like, it's just a human thing, right?
[1825.76 → 1827.82] And then it's something that I've done a few times.
[1828.10 → 1829.74] I don't like it, but it happens.
[1829.88 → 1832.56] Like, the longest PRs, I review and then I submit.
[1833.04 → 1835.48] And then when I'm doing the re-review, I find new things.
[1835.52 → 1837.86] I'm like, I can't let it pass.
[1837.86 → 1844.16] I'm going to have to put a comment where there wasn't a comment, and it was not changed because now I saw it, right?
[1844.98 → 1845.74] That's the thing.
[1846.20 → 1850.94] So, given that, what is a reasonable time to expect a PR review?
[1851.36 → 1857.40] If you, like, put in a PR today, is it the next hour, like, by end of day, the next day, a week?
[1857.92 → 1858.78] Does it depend?
[1859.44 → 1861.04] The real answer is it depends.
[1861.52 → 1862.84] I got ahead of you there, I knew.
[1862.84 → 1863.32] Yeah.
[1863.98 → 1866.28] My first job, we...
[1866.28 → 1867.52] Did we use Jira?
[1868.02 → 1868.62] I don't know, whatever.
[1868.70 → 1869.76] We used columns, right?
[1869.90 → 1870.44] We used columns.
[1870.60 → 1872.46] So, there was the column PR review.
[1872.64 → 1874.76] So, the open PRs were there for review.
[1875.26 → 1877.66] And then there could be, I think we were three people.
[1877.82 → 1881.02] So, there could be only two PRs on review.
[1881.36 → 1882.88] So, do you want to put something for review?
[1882.98 → 1884.22] We have to take something to review.
[1885.02 → 1885.20] Right?
[1885.26 → 1889.56] So, this happened, helped to keep the, you know, the process running, everyone reviewing.
[1890.76 → 1892.82] Nowadays, like, I think it's a lot of people.
[1892.82 → 1897.06] I think when you're really running a Jira startup, microservice, you know, just deploy,
[1897.46 → 1901.30] you usually expect something in the next day to get an answer.
[1902.10 → 1905.66] Not elastic, within the week, I'd say.
[1906.18 → 1906.38] Okay.
[1907.16 → 1910.62] And do you have different commitments when it comes to internally, like, your internal
[1910.62 → 1914.18] team PRs versus people who are maybe contributing to your service?
[1914.56 → 1918.04] I.e., like, in our system, we have a lot of external teams that will contribute to our
[1918.04 → 1919.92] service and ask for PR reviews.
[1919.92 → 1925.98] Like, what is a reasonable timeline to commit to review those external PRs?
[1926.40 → 1928.16] I think there are two categories, right?
[1928.20 → 1931.26] If it's just a normal flow, they go in the same flow.
[1931.82 → 1937.16] But if it's something that someone external is doing because our team doesn't have capacity
[1937.16 → 1939.38] and then it is really important, right?
[1939.58 → 1941.74] Probably, I would try to prioritize this review.
[1942.52 → 1948.60] But also, if someone that's not from the team or doesn't know the rapid conventions, it's
[1948.60 → 1950.94] probably going to be a more thorough review.
[1950.94 → 1955.40] I strongly believe that your code should be consistent, right?
[1955.44 → 1959.32] I'd rather have something that they don't like, but it's consistent, and it's always
[1959.32 → 1963.54] there, than half of the code they like, half of the code they don't like, and another third
[1963.54 → 1964.64] they don't even have an opinion.
[1965.90 → 1971.64] So, in external reviews, I think there's the extra consistent thing in code conventions
[1971.64 → 1974.14] from the repo that you have to put through.
[1974.86 → 1977.04] And then it should be, I mean, it's better to be quicker.
[1977.58 → 1978.16] For sure.
[1978.60 → 1980.30] I really like that column policy.
[1980.42 → 1981.78] I might have to implement that on my team.
[1982.10 → 1982.72] Yeah, right.
[1982.90 → 1985.08] You can't put a PR on if they're already two.
[1985.16 → 1986.12] You have to review them.
[1986.70 → 1987.90] Yeah, it makes things...
[1987.90 → 1988.50] I love that.
[1988.56 → 1989.12] ...to move.
[1989.30 → 1990.26] I think it's nice.
[1990.82 → 1991.32] I agree.
[1991.60 → 1992.34] It's a weight group.
[1992.78 → 1995.00] We pretty much describe this concept now.
[1995.30 → 1996.70] It's a channel with a buffer.
[1996.70 → 1997.14] Yeah.
[1998.34 → 2001.86] And then I'm going to have to be the bad girl who comes into Slack and someone's like,
[2001.90 → 2004.10] oh, I'm ready to put my PR on this big new feature.
[2004.32 → 2006.08] And I'm like, you're not allowed to.
[2006.72 → 2007.12] Counterfoil.
[2007.44 → 2008.80] Go review Bob's PR.
[2009.20 → 2009.80] Throwing air.
[2011.24 → 2011.52] Yeah.
[2012.02 → 2014.36] There's the poking PR review.
[2014.60 → 2017.54] You only get your PR reviewed when you poke someone, right?
[2017.64 → 2018.36] You don't want to add.
[2019.76 → 2020.12] Exception.
[2022.64 → 2026.58] It can be a fun way of teaching all sorts of Go concepts now that...
[2026.70 → 2028.22] This gave me some ideas.
[2028.32 → 2028.68] Thank you.
[2028.86 → 2029.98] We're doing a PR review?
[2030.54 → 2031.46] By poking people?
[2031.92 → 2032.24] Yeah.
[2032.66 → 2033.58] With limiting this.
[2033.70 → 2035.82] This is a fun way to discuss this.
[2035.96 → 2039.96] And on the way, you discuss errors, throwing incorrect errors and also exceptions and so on.
[2040.16 → 2040.56] Okay.
[2041.08 → 2043.68] Go routines if you suddenly have to split into that.
[2043.84 → 2043.92] Yeah.
[2044.48 → 2046.70] Talking about teaching Go in unusual ways.
[2046.70 → 2057.72] I was thinking today, someone should write a Go program that simulates how the queue for the food works here and then make a proper Go concurrent good program for that.
[2057.98 → 2060.02] Because the queue is unnecessary here.
[2060.44 → 2061.84] We have a lot of contingents.
[2062.20 → 2065.10] I was like, you know, you can make better concurrency here.
[2065.10 → 2067.80] Because you have lots of food stations that people miss.
[2068.10 → 2068.64] That's the point.
[2068.70 → 2069.74] You have a lot of food stations.
[2069.86 → 2072.56] You can have a lot of concurrent access to that.
[2072.90 → 2073.94] But no, you get sequential.
[2074.12 → 2077.00] You get a huge queue and everyone goes through everything that they don't want.
[2077.72 → 2079.72] I think because we're just out of the...
[2079.72 → 2080.70] They didn't read the docs.
[2080.94 → 2081.94] They don't know what's the food.
[2082.04 → 2082.86] They didn't read the docs.
[2082.96 → 2083.30] Exactly.
[2084.10 → 2085.66] Everything can be explained with pick.
[2085.96 → 2086.78] Lesson learned.
[2086.98 → 2088.80] Always read the docs first.
[2089.04 → 2091.10] And if they're bad docs, then...
[2091.84 → 2092.44] Improve them.
[2093.08 → 2093.64] Improve them.
[2093.64 → 2095.00] Open a pull request for the docs.
[2095.16 → 2095.54] Yes.
[2097.10 → 2098.40] That's something that I love.
[2098.66 → 2107.36] If I'm reading documentation that it's easy to open a pull request and to see a failure or inconsistency or something, I open the pull request.
[2107.50 → 2112.30] I think it's such a valuable contribution and so easy most of the time.
[2112.86 → 2118.48] I love these docs that they have the button edit, and then you go direct to GitHub to create a pull request.
[2118.54 → 2119.08] That's fantastic.
[2119.54 → 2119.74] Yeah.
[2119.74 → 2122.14] I feel like I get into a bit of a rabbit hole.
[2122.14 → 2134.42] I had to stop myself editing documentation because it went from actually making it correct to actually just implying my personal stylistic choices when writing documentation and phrasing.
[2134.94 → 2138.00] I like this adjective slightly better, actually.
[2138.00 → 2143.38] So I had to pull back to be like, okay, review for correctness, not for like, I want a comma here.
[2144.40 → 2145.78] I think that's so hard.
[2146.26 → 2152.02] And for me, as a known native speaker, sometimes I was like, I don't think this sentence is correct.
[2152.16 → 2153.04] I think it's missing a comma.
[2153.14 → 2154.06] I think it's missing an article.
[2154.42 → 2156.66] And I was like, honestly, you don't know English so much.
[2157.28 → 2160.72] I don't even know if you could do that in proper Portuguese, like a proper grammar.
[2160.72 → 2162.16] But I think it's important.
[2162.54 → 2170.02] My take is if I believe it's compromising their understanding, I'm going to probably suggest something.
[2170.52 → 2170.64] Right.
[2171.06 → 2178.20] And also sometimes when the comment is there for a long time, I just, I make the change and suggest someone is going to review that.
[2178.28 → 2178.44] Is it?
[2178.84 → 2184.90] I sometimes put into some AI if I don't understand something and I read two, three times and I keep staring at it.
[2184.90 → 2187.16] I'm like, just explain that to me in other words.
[2187.36 → 2188.00] And that helps.
[2188.74 → 2189.26] Good AI.
[2190.22 → 2191.86] It's like pinging somebody, but yeah.
[2192.54 → 2198.92] But also make the changes just like you, because I think if I'm as a non-native don't understand this, there must be another non-native that gets lost there.
[2199.30 → 2199.60] Yeah.
[2199.84 → 2200.96] And clarity is important.
[2201.90 → 2208.70] And let's say you're interviewing, whether you are the candidate or you are the interviewing person.
[2209.34 → 2214.18] And part of the interview is reviewing a pull request from somebody from your team.
[2214.90 → 2217.98] What tips do you have for somebody to do this well?
[2218.66 → 2223.36] Actually, never been really on these shoes, neither side.
[2224.04 → 2229.72] I've been asking, oh yeah, in one of your code bases, any of your code base, what you would change or something.
[2230.32 → 2237.14] I think at the end of the day, a lot of the time we, to interview for culture fit, right?
[2237.22 → 2239.62] And a person that's nice, it's good to work with.
[2240.34 → 2241.26] This is super important.
[2241.26 → 2247.98] So I think it's, if you're on an interview, just be sure to be nice, right?
[2248.04 → 2251.28] In your comments and everything, don't go like, oh yeah, this is crap.
[2251.38 → 2252.10] This is bad.
[2252.36 → 2253.48] Just be nice.
[2253.58 → 2254.18] Be polite.
[2254.92 → 2255.98] Link the commendations.
[2256.28 → 2260.10] And I advise you to bring arguments, right?
[2260.10 → 2264.60] Don't say, okay, do that or change that or this need change without a reason, right?
[2264.60 → 2268.48] If an interview, usually an interview don't have so much time, right?
[2268.56 → 2273.14] So I would go for, oh yeah, you know, this name is not ideal.
[2273.62 → 2279.38] You know, the goal, effective goal, there is a section on name convention that explain why it should be like that.
[2279.52 → 2282.38] So as it's in goal, it's better to be like that.
[2282.68 → 2286.94] So always try to, to bring something to support your views.
[2286.94 → 2293.08] And when it's opinion, and that's something that I really do on pre-request, when it's like, it's my opinion, I say like, look, this is my opinion.
[2293.20 → 2298.74] I believe that's better because this, this, and this is up to you because I don't see a flaw here.
[2299.00 → 2301.70] I just think it can be better about any opinion.
[2302.56 → 2311.52] If you were interviewing someone and their task was to review a PR, what would be things that they did that would maybe be like, oh no, I don't know about that?
[2311.52 → 2315.00] I think it would be to be aggressive, right?
[2315.10 → 2320.88] And impolite to just diminishing the code and say like the code is bad or something.
[2321.60 → 2326.48] In interviews, they really, they show that they know, don't know what they're doing.
[2326.90 → 2333.24] I think if you interview people, you know, some people, they don't know what they're doing or just trying to fool you.
[2333.62 → 2333.98] Right?
[2334.04 → 2336.02] If it's hard to see that it's like, oh, no, no.
[2336.42 → 2337.74] It's better to say you don't know.
[2337.92 → 2338.74] It's not like that.
[2338.78 → 2339.30] It's like, great.
[2339.30 → 2339.86] Just go.
[2339.96 → 2341.44] And you know, I just, okay.
[2341.52 → 2341.76] Yeah.
[2342.04 → 2342.38] Mm-hmm.
[2342.52 → 2343.76] It's just an incentivized.
[2343.84 → 2344.20] Yeah, go.
[2344.44 → 2344.92] Go, please.
[2345.62 → 2347.18] And then, oh yeah, thank you very much.
[2347.20 → 2348.04] You're going to be in contact.
[2349.36 → 2349.72] Yeah.
[2349.86 → 2352.88] And definitely staying honest is a lot better than making things up.
[2353.30 → 2353.50] Yeah.
[2353.54 → 2354.42] Please say, I don't know.
[2354.46 → 2357.34] I think if someone to me in an interview say, look, I don't know.
[2357.38 → 2358.00] I don't remember.
[2358.50 → 2359.52] Oh, I don't know.
[2359.58 → 2361.72] And I think in that place I can get information.
[2362.14 → 2365.30] Dude, folk, you're like scoring a hundred points with me.
[2365.54 → 2368.58] If you're trying to just BS me through.
[2369.06 → 2369.18] Nah.
[2369.60 → 2370.04] That's fair.
[2370.04 → 2371.94] Anderson will not be having that.
[2371.94 → 2401.92] this episode is brought to you by our friends at chromosphere scaling cloud native is complicated
[2401.92 → 2407.20] and chromosphere helps teams take back control of observability team rampant data growth reduce
[2407.20 → 2412.08] cloud native complexity and increase confidence of the business and I'm here with martin MAL co-founder
[2412.08 → 2416.96] and CEO of chromosphere martin when it comes to cloud native observability what are the pain points
[2416.96 → 2422.06] of Kubernetes and making sure it's reliable you know I think the shift to Kubernetes has really
[2422.06 → 2428.60] changed the way we design applications it's changed the way we's changed our infrastructure as well
[2428.60 → 2432.56] so it's introduced a lot of change I would say and that's probably why it's causing a lot of
[2432.56 → 2438.76] issues in the observability space I think one thing we're finding is that a lot of companies out there
[2438.76 → 2445.12] are focused on producing a lot more data and there's a lot of focus on more metrics more traces more logs
[2445.12 → 2450.00] because these environments we're trying to monitor are far more complex these days I think that's
[2450.00 → 2454.68] maybe one of the mistakes the industry is running into, and it's interesting because obviously for
[2454.68 → 2459.20] all the solutions out there the vendors out there the more data that gets produced the better it is
[2459.20 → 2464.94] for all the vendors out there but what's interesting is that along with that increased volume of data
[2464.94 → 2470.38] people aren't actually getting better outcomes out of it people's number of incidents that people are
[2470.38 → 2476.40] running to still rising people's MTTR minds meantime to detection and resolutions actually getting
[2476.40 → 2481.34] higher as opposed to lower so I think this is the common state that a lot of companies find themselves
[2481.34 → 2486.46] in and of course with the increased volume of data folks bills increase and the problem actually
[2486.46 → 2490.70] gets harder so I think that's a common state we find a lot of companies into and this is probably
[2490.70 → 2494.94] why it's top of mind for a lot of companies out there very cool thank you martin all right the next
[2494.94 → 2501.06] step is to head to chronosphere.io to explore the platform and get a demo again chronosphere.io
[2501.06 → 2530.98] okay so we kind of touched on this a little earlier in the episode
[2530.98 → 2537.48] but I want to dig a little bit deeper in fact I will ask you a question first are you engaged in
[2537.48 → 2541.54] any kind of open source projects I know you said that you know contribute to go a little
[2541.54 → 2550.02] is that a world in which you feel like you have engaged and put PRS in so I can cheat my answer
[2550.02 → 2555.58] right okay yeah as I'm evolving open source because I work at the last the majority of our
[2555.58 → 2562.46] repels are open source right but as a 100 open source contribution that I'm not working for the
[2562.46 → 2568.50] company or not no I read you it's something that I always wanted I just said like I managed to get
[2568.50 → 2577.10] a committed to in go but I haven't fully got to participate in a project I still try oh no today I think i
[2577.10 → 2582.32] got one on Kubernetes too you see like it's one of my goals you know these plans that things you want
[2582.32 → 2587.00] to do also have to try a bit you know it goes back and forth I may go for a coin again perhaps
[2587.00 → 2592.56] you know the flame just like lighting up again reignite that passion that's going to happen but
[2592.56 → 2597.96] yeah no I'm not really engaged on let's say an external open source project that's not part of
[2597.96 → 2603.90] my daily job and when you have done it is part of the reason why you think it's difficult to engage
[2603.90 → 2609.22] fully is anything to do with that to do with like the difficult or the different process to put in a
[2609.22 → 2615.62] when it is an open source project as opposed to internal like within work PR reviews and submission
[2615.62 → 2620.30] I think to me what's always difficult like to find something meaningful to work
[2620.30 → 2627.50] right sometimes you don't know what you can do there is a tag first good issue and so but
[2627.50 → 2632.16] I think you're a lot I think yeah that's the point we're lost, and you don't have someone to go
[2632.16 → 2639.06] please help me yeah right or I try that or shall I do that right because my project and my team are
[2639.06 → 2644.36] comfortable to go and do a refactor yeah it's like complete external project that I don't know
[2644.36 → 2650.88] anyone there or anything I'm going to be afraid you know, and sometimes you're not even able to run
[2650.88 → 2656.58] the project so that I think that's a lot of the barrier I think if you would have something
[2656.58 → 2662.66] not necessarily a mentor, but you know perhaps like a channel ask questions right like oh I want
[2662.66 → 2667.62] to get even that like say oh I want to take this issue because sometimes they're good first issues
[2667.62 → 2672.92] they open like one year ago I was like dude I don't know if it's worth to fix that or not and then
[2672.92 → 2677.68] you open the pull request you fix everything no one reviews, and then you think no one reviews
[2677.68 → 2683.42] nothing got stale you get demotivated yeah fair enough and do you think there's a higher bar
[2683.42 → 2688.08] as to what you're willing to put in as a PR for an open source project I speak about this from my
[2688.08 → 2692.76] own personal like experience when I was trying to get into like okay I want to contribute to open
[2692.76 → 2697.68] source oh you should just go in and do like a little change but I was like yeah but I feel like
[2697.68 → 2703.86] I'm contributing to an open source library where everyone can see, and they're like oh angelica made
[2703.86 → 2710.16] like a one line change or like change that one function name I think and if I talk for myself
[2710.16 → 2715.02] I always had the feeling to contribute to open source pros the bar is super high yeah
[2715.02 → 2722.24] are you having to be like an expert developer and everything and the reality is no right and
[2722.24 → 2730.06] the issue is there the problem exists I think this is the best advice I can do to any junior developer
[2730.06 → 2736.70] just go for it, they know you already have right, so your change is not there the bug is not fixed
[2736.70 → 2743.64] the documentation not proved the feature is not there right, so this is not gonna change if your
[2743.64 → 2748.86] change didn't get there you learn something you play with a new technology I was trying to submit
[2748.86 → 2755.48] pull requests for the Kubernetes code just fixing leading issues I understand a bit how the that piece
[2755.48 → 2760.56] of code worked and I was like oh how they instructed that and like look at the packages because I had to
[2760.56 → 2766.20] read through the packages to fix leading issues I think one PR got merged the other ones got stale
[2766.20 → 2773.56] this life it happens and I learned something yeah so try to go for it let the other one say no it's not
[2773.56 → 2781.48] your job to say no for you right it's their job that is a popular opinion I bet applies to many fields
[2781.48 → 2792.10] in life that's true just do it yes try yeah well done all right the fun part unpopular opinions
[2792.10 → 2797.28] before we started the recording Anderson you mentioned you have several unpopular opinions
[2797.28 → 2802.20] and you were wondering whether you should go for the most yeah how did you phrase that I forget you
[2802.20 → 2809.20] used a good word the most controversial yeah exactly or the least controversial yeah now I'm taking
[2809.20 → 2816.24] I'm picking a controversial one yeah right but I can explain as I said in the PR you can explain
[2816.24 → 2823.96] you should not write more than 100 columns right you write your code should not really
[2823.96 → 2832.88] pass 100 columns from which yeah first things there's no magic numbers like 100 cut I would say 110
[2832.88 → 2839.32] it's okay when it's terrible to cut right 120 is almost a hard limit don't really go over that
[2839.32 → 2848.52] why first things first do you read books on landscape no right come on I think everyone had
[2848.52 → 2854.12] that right you got like this email right you're like in your four key or ever monitor and that thing
[2854.12 → 2859.92] goes from side to side, and you're reading for the listeners I'm moving my head as you know reading
[2859.92 → 2863.94] from one side to the other like you're watching tennis you feel like you know a typewriter that goes
[2863.94 → 2873.90] so it's hard to read right because we don't read in landscape we read in portrait the second
[2873.90 → 2880.92] thing is not everyone has got ice cream as big as yours there are people coding 14 13 inches right
[2880.92 → 2887.50] they want to have two tabs open perhaps so if you go much more than 100 it's going to be bad for
[2887.50 → 2894.00] some people and I believe for everyone too long it's hard to read so that's my unpopular opinion
[2894.00 → 2900.34] I want to disappoint you that I think I agree with you and I even take this into writing emails that
[2900.34 → 2906.38] I try to keep that I don't know how many characters that is but I sometimes break lines like one sentence
[2906.38 → 2912.02] into three four lines just so it stays so you don't have to scroll in case yeah images logos I don't know
[2912.02 → 2916.14] whatever happens in somebody's signature that it suddenly gets stretched I feel like you're
[2916.14 → 2922.66] unfortunately preaching to the choir with me and Natalie we're both like yes please I don't like
[2922.66 → 2929.50] my neck will hurt perhaps in go a chrome plugin that just truncates things for you yeah perhaps
[2929.50 → 2934.62] in go but I think if you go to java you know the things are long there yeah 100 characters is just
[2934.62 → 2942.34] the function name oh my gosh yes I feel like that one was a good one but like if we have time Natalie I want
[2942.34 → 2948.30] to hear another one yeah I want us to get like an unpopular one from you oh my god what was the
[2948.30 → 2952.24] other one that you were thinking about saying that you cheekily in your mind were like no I'm not gonna
[2952.24 → 2957.44] say that no I think this one's like the unpopular kind of popular okay I mean I see a lot happening so
[2957.44 → 2964.08] perhaps in unpopular return new is wrong period right you have to wrap the errors and add more context
[2964.08 → 2971.30] always I cannot count how many times I had to go to the code and dig deep and deep and deep to discover
[2971.30 → 2978.04] where this error came from because i you know it's like when you get like a try to write to the
[2978.04 → 2982.76] disk and get an error you get something like I got one too many colours in the address it's like
[2982.76 → 2988.58] this is finally the address how there are too many columns right, and then you have to understand where
[2988.58 → 2993.56] this address was going to be used which method it was and then oh yeah on this context there are too many
[2993.56 → 2998.68] columns, but they didn't have this information so return new is wrong you have to wrap your errors
[2998.68 → 3003.54] now you don't have an excuse you have ever wrapping when they send the library so I think wrapping errors
[3003.54 → 3009.52] will be an unpopular opinion yeah I feel like this second one is gonna probably be more unpopular
[3009.52 → 3016.04] yeah because a lot of people just return yeah, yeah interesting that's one of the things that I'm looking
[3016.04 → 3021.70] for requests and was like dude could you wrap that, and then it goes back on that if it's my repo
[3021.70 → 3028.44] my code I might say like no now when I say my please like my teams right I don't have this
[3028.44 → 3036.06] possessive I think code must be owned by a group, and it must be a consensus group but yeah this is the
[3036.06 → 3041.96] thing that I'm gonna point and usually if it's an external adding code even more important like okay
[3041.96 → 3049.28] like your wrapper your rules our wrapper our rules right so okay here we wrap do that if I'm owning your
[3049.28 → 3055.02] wrapper I play by your rules I like that one I'm also having so many more ideas this always happens
[3055.02 → 3059.82] when me and you have episode Nathan I'm like so many more episode ideas write them all down does
[3059.82 → 3065.68] your code belong to you or to the world I mean on an open source that's definitely a question right
[3065.68 → 3072.48] yeah also with AI tools that are writing code that's a question yeah oh god that's yeah who is the true
[3072.48 → 3078.64] either code yeah that's a good one yeah licensing is interesting for sure with a copilot and friends
[3078.64 → 3085.58] when the AI put the bug in production who do you blame who run the AI who wrote the AI
[3085.58 → 3092.22] or who reviewed the PR that's a good one right can AI review a PR for sure
[3092.22 → 3100.00] would you trust that I might have used that in the past yes oh that's nice okay I'm a big fan of AI
[3100.00 → 3106.08] and coding I think it's a fun combination I'm very happy to automate myself out of job that's good
[3106.08 → 3113.62] but I confess I know almost zero about AI and coding but I'm super interested looks fascinating to
[3113.62 → 3119.44] see where is it going yeah yeah definitely um both from the side of writing and from the side that's
[3119.44 → 3125.42] relevant to this episode which is the reviewing and like explaining and so on I think in general
[3125.42 → 3132.06] AI is they can see the context, and it carries so much information see part of the things that we just
[3132.06 → 3140.04] can't right and sometimes someone read experience can, but they cannot teach it so there is definitely a
[3140.04 → 3145.88] lot of value yeah yeah exactly about the context in particular I sent a twitter poll Natalie would you
[3145.88 → 3151.56] let an AI review your code maybe this can be my unpopular opinion for this episode
[3151.56 → 3159.00] I would like not have it just review and say good bad but I would use it as something like here is the
[3159.00 → 3164.90] code what does it do or list the problems, and then you know read the output and give it a secondary
[3164.90 → 3172.58] review I think this might end up being a popular opinion true now you've explained it and want us over
[3172.58 → 3179.76] to your side I feel like it will be popular yeah okay my next chrome plugin each episode is like 15 other ideas yeah
[3179.76 → 3187.96] summarize this PR for me yeah well this has been fun and this has been inspiring
[3187.96 → 3192.76] Anderson thanks a lot for joining us and uh sparing some of your time at gopher.com UK
[3192.76 → 3198.62] thank you very much for having me it was perfect I'm really happy thank you so much we're going to have to
[3198.62 → 3205.10] get you back on for who owns our code episode yeah I would love if it's a plan and everybody I hope
[3205.10 → 3210.54] you will also join us, and thanks for joining us this time bye thank you very much bye bye
[3210.54 → 3221.32] all right that is gone time for this week thanks for listening now is the best time to subscribe if you
[3221.32 → 3227.82] haven't yet head to go time.fm for all the ways and if you are a regular go time listener check out
[3227.82 → 3233.64] our membership program directly support our work save yourself some time by ditching the ads and get
[3233.64 → 3241.20] bonuses like exclusive content and free stickers check it out at changelog.com slash plus thanks
[3241.20 → 3248.16] again to our partners at fast for cunning for us to fly.io for serving up our app to the mysterious
[3248.16 → 3252.88] break master cylinder for these dope beats and to you for being part of the go time community
[3252.88 → 3258.62] we appreciate you that is all for this week we'll talk to you next time on go time
[3258.62 → 3268.62] you
