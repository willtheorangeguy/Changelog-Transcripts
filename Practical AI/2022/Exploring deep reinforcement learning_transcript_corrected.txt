[0.00 → 5.18] For me, AI will change everything, but it's really important to consider that it will not solve everything.
[5.76 → 10.52] For instance, you know, we all talk about the question that AI will help a lot in healthcare, as I mentioned.
[10.52 → 16.82] But the problem is that if people can't afford, you know, to access these tools, the problem is not solved.
[17.24 → 21.66] So I think what's important to consider is that we need to improve AI,
[21.88 → 26.98] but AI must be, you know, really accessible to everyone to be a solution to human problems.
[30.00 → 32.86] Big thanks to our partners, Linde, Vastly, and Launch Darkly.
[33.04 → 35.28] We love Linde. They keep it fast and simple.
[35.40 → 37.76] Check them out at linode.com slash changelog.
[37.76 → 40.06] Our bandwidth is provided by Vastly.
[40.40 → 43.96] Learn more at Fastly.com and get your feature flags powered by Launch Darkly.
[44.22 → 45.94] Get a demo at LaunchDarkly.com.
[47.06 → 48.30] Hey, Jared here.
[48.88 → 53.12] One of the things we can count on in the software industry is change.
[53.80 → 56.40] The state-of-the-art changes so fast, in fact,
[56.40 → 60.34] that keeping up can feel like a whole other job on top of your actual job.
[61.24 → 63.22] That's why we created Change Log Weekly.
[63.82 → 68.10] It's our totally free newsletter that we drop in your inbox each and every Sunday.
[68.74 → 71.50] We link to the latest news, the best articles,
[71.80 → 74.38] and the most interesting projects that you should be aware of.
[75.04 → 78.76] We also add a little commentary from us saying why something's important,
[79.12 → 80.82] pointing you to other instances of a trend,
[80.94 → 83.12] or just making a dorky joke to keep it lively.
[83.12 → 86.74] So if you haven't yet, I recommend subscribing to Change Log Weekly
[86.74 → 89.30] and help us help you keep up with the latest.
[90.42 → 93.46] Head to changelog.com slash weekly and sign up today.
[93.74 → 96.22] Again, it's totally free and we never spam you.
[96.38 → 96.70] Yuck.
[97.58 → 101.08] One last time, that's changelog.com slash weekly.
[113.12 → 118.66] Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical,
[118.98 → 120.74] productive, and accessible to everyone.
[121.06 → 125.14] This is where conversations around AI, machine learning, and data science happen.
[125.50 → 128.66] Join the community and Slack with us around various topics of the show
[128.66 → 131.50] at changelog.com slash community and follow us on Twitter.
[131.64 → 133.18] We're at Practical AI FM.
[133.18 → 143.00] Welcome to another episode of the Practical AI podcast.
[143.44 → 147.94] We are the podcast that tries to make artificial intelligence practical,
[148.14 → 150.22] productive, and accessible to everyone.
[150.46 → 152.08] My name is Chris Benson.
[152.22 → 153.86] I am one of your co-hosts.
[154.04 → 156.52] And Daniel is actually out this week.
[156.60 → 159.34] He has told me I'm allowed to tell you he's down with COVID.
[159.34 → 162.80] And so we are hoping Daniel feels better much, very fast.
[163.32 → 166.74] But for those of you who joined us last week, I have a treat for you.
[167.14 → 170.32] I have an excellent co-host, a proven co-host.
[170.72 → 171.70] You already know her.
[171.90 → 174.50] Her name is Natalie Pistinovich.
[174.66 → 175.24] Sorry, Natalie.
[175.66 → 179.92] And thank you for agreeing to come back in while Daniel is struggling through COVID
[179.92 → 180.90] and co-hosting with me.
[181.02 → 181.52] Welcome back.
[181.86 → 182.16] Thanks, Chris.
[182.24 → 183.44] It's always fun to be here.
[183.66 → 184.10] Fantastic.
[184.48 → 187.46] And we are to dive right into the show here.
[187.46 → 194.40] We have a guest who is from one of the leading organizations in the AI world.
[194.62 → 196.72] It's one that we always love to talk about.
[196.92 → 198.48] One of our favourite organizations.
[198.90 → 202.20] And this particular guest has been doing some pretty cool stuff,
[202.28 → 204.30] I know, from the pre-show conversation.
[204.58 → 210.40] So I would like to introduce Thomas Simonies, if I got the last name correct, Thomas?
[210.52 → 210.96] That's correct.
[211.10 → 211.36] Welcome.
[211.80 → 214.96] You are a developer advocate at Hugging Face,
[214.96 → 217.36] which is the organization I was talking about.
[217.46 → 219.32] Working on deep reinforcement learning.
[219.48 → 223.68] And I know you're also the founder of a deep reinforcement learning course.
[224.32 → 228.98] But I guess if you, other than that little tiny tidbit that I've offered the audience already,
[229.02 → 231.02] if you would tell us a little bit about your background,
[231.62 → 235.34] how you arrived at where you're at doing deep reinforcement learning,
[235.34 → 236.46] and how you got there.
[236.48 → 239.48] And a lot of people, I know, ask us out of the episodes,
[239.64 → 241.00] kind of, how did you get there?
[241.02 → 242.18] Because they want to learn from you.
[242.18 → 243.56] So if you can kind of share people,
[244.16 → 245.84] share with people how you got to where you're at.
[245.84 → 248.54] Sure. So first thing first, thanks for inviting me.
[248.72 → 249.54] It's a vast question.
[249.80 → 253.38] Initially, I have a bachelor degree of law and political sciences.
[254.24 → 259.10] And what happened is that I was working in a startup incubator.
[259.10 → 266.24] And I was helping people who want to make startup to choose, you know, the technology behind their website,
[266.24 → 270.44] because I was a full stack web developer in addition to my studies.
[271.12 → 275.26] And what happened is that I met a lot of people who were working on machine learning.
[275.44 → 277.08] And I didn't know about that.
[277.08 → 278.70] And I discovered this domain.
[278.70 → 282.36] And after my bachelor degree, I quit my studies.
[282.72 → 285.92] And I started to self-study deep learning initially.
[286.68 → 289.18] And in 2018, I discovered deep reinforcement learning.
[289.18 → 291.54] And I fell in love with this domain.
[292.32 → 296.06] And at the same time, I started to write articles about deep reinforcement learning.
[296.48 → 297.64] And it became a course.
[297.86 → 299.20] It was not supposed.
[299.32 → 301.52] It was just one article, but it works really great.
[301.52 → 305.26] And it became, yeah, a free and open source course.
[306.12 → 311.24] And after that, so in 2019, I started to work at Data for one year and a half,
[311.36 → 318.88] where I work on implementing deep reinforcement learning agents for real-world application, dynamic pricing, for instance.
[319.56 → 323.52] Dynamic pricing is when you need to find a price.
[323.52 → 331.02] For instance, if you have an airline ticket, and the goal is that you find the best price to make the most benefits.
[331.52 → 334.80] And after that, I quit to work in the video game industry.
[335.62 → 343.18] And finally, I'm working at Hugging Face to work on implementing deep reinforcement learning in the ecosystem of Hugging Face.
[343.74 → 349.12] So I'm wondering, just because you mentioned it several times at the front, and I know I mentioned it at the beginning as well,
[349.50 → 354.78] there are a few people out there that may have heard of deep reinforcement learning, but they don't have the background.
[354.90 → 356.66] They haven't had a chance to dive into it themselves.
[356.66 → 362.08] Could you give us a quick kind of, you know, tell us a little bit about what it is and what's involved in it,
[362.28 → 365.68] you know, especially if you differentiate it from some of the other forms of deep learning?
[366.08 → 371.00] So to say it simply, deep reinforcement learning is to learn from action.
[371.34 → 376.04] So the idea is that you have an agent that will learn by interacting with his environment.
[376.72 → 381.56] If we take a simple example, you can make an agent that will learn to play Super Mario Bros,
[381.56 → 383.12] so to play video games.
[383.74 → 388.80] And how he does that, he just, you know, try some action in the environment, so going left or right.
[389.14 → 393.32] And based on the rewards he gets, so for instance, if he dies, it's negative,
[393.70 → 397.16] it will improve its behaviour to win the game.
[397.68 → 401.00] And Hugging Face, where you're the developer advocate now.
[401.10 → 404.20] So this is an AI community, right?
[404.58 → 406.30] And it's all open source.
[406.44 → 408.12] And so what is your mission?
[408.60 → 410.08] How do you do things?
[410.18 → 410.54] Why?
[410.54 → 417.52] So in Hugging Face, what we want to do is to democratize AI and what we call good AI
[417.52 → 422.06] through, as you mentioned, open source models and open source library.
[422.56 → 427.16] The idea, if you want, it's the GitHub for the AI models.
[427.46 → 432.18] It means it's a place where you can access a lot of trained models, very powerful,
[432.66 → 435.94] and you can use it for your own problems you have.
[435.94 → 441.38] And, you know, for instance, you can use a model to translate from English to French, etc.
[441.38 → 449.62] And our goal is really to democratize the access of AI by providing a place where you can share or upload models.
[449.96 → 452.32] But it's, you know, it's much more than that.
[452.32 → 457.40] You know, there is the transformer library that allows you, you know, to create transformers.
[457.40 → 461.40] So transformer is a model's natural language processing models.
[461.76 → 467.04] You have the asset library to create rapidly that asset or to share that asset and so much more.
[467.14 → 468.26] So I think, yeah.
[468.26 → 470.10] So I have a follow-up question to that.
[470.20 → 475.68] And that is in my day job, because believe it or not, running the podcast isn't the primary thing that I do.
[475.92 → 476.56] This is fun.
[476.64 → 477.22] This is passion.
[477.36 → 480.46] But in my day job, I was talking to my boss about an hour ago.
[480.56 → 484.94] And I told him I was interviewing you and, you know, that you're with Hugging Face as a developer advocate.
[485.42 → 489.78] And he, not for the first time either, said, I just love Hugging Face.
[489.86 → 493.82] He said, that's the library I want to use every time I'm doing NLP.
[493.82 → 498.52] And he went on for several minutes about you and so about the company and stuff.
[498.86 → 502.90] So, but it begs the question for those who aren't intimately familiar and haven't used it.
[503.18 → 507.58] What is it, in your opinion, as a developer advocate about Hugging Face that you're doing right?
[507.80 → 511.96] So many people really love using the libraries out of Hugging Face.
[512.16 → 514.38] And it's kind of a darling in the industry.
[514.90 → 522.12] What is it the Hugging Face is doing right that maybe others, I'm asking you to give away the secret sauce, I guess, that others would do well to emulate?
[522.12 → 527.64] Well, I think I will take my experience because I discovered Hugging Face, I think it was eight months ago.
[528.06 → 538.68] I think it's really a fact that you can rapidly, even though you're not a specialist in NLP, you can rapidly grab a model and use it for your own needs.
[538.92 → 541.54] You know, in two lines of code, we have something called pipeline.
[541.74 → 546.58] It's the first thing I discovered is in two lines, you can, for instance, translate.
[546.88 → 550.16] You can have a model that generates conversation, et cetera.
[550.16 → 559.96] For me, the secret sauce is really the place where you have so much trained model and so much, you know, powerful model that you can use in two lines of code.
[560.32 → 566.30] And I will also add that it's also community because we are very, a very, very strong community.
[566.78 → 570.16] It means that when you have questions, you know, people are really willing to reply.
[570.16 → 573.82] Even people outside of Hugging Face, you know, on the forum, on the Discord.
[574.52 → 584.32] And it really helped me when I started, you know, to train my first model to have people who are very involved and that do not work, you know, at Hugging Face to help us.
[584.64 → 589.04] And would you say that the community of users of Hugging Face, is it more developers?
[589.38 → 594.74] Is it more people who are just general enthusiastic about AI or more data scientists?
[594.74 → 597.08] Who do you see active there?
[597.36 → 602.44] I think it's both of them because we have a lot of researchers, but we have also a lot of enthusiasts.
[603.52 → 611.26] And for instance, there is a lot of people, you know, who worked on computer vision models, on natural language processing models.
[611.90 → 619.88] And there is a lot of people who just started, you know, in deep learning and or in deep reinforcement learning who directly, you know, try models.
[619.88 → 628.96] So it's very diverse, you know, but I think the majority of people who use Hugging Face are researchers and, you know, data scientists.
[629.22 → 635.18] But there is also a growing part of really, you know, beginners who just want to learn and to try some stuff.
[635.18 → 643.88] So one of the things that, you know, and I know that Hugging Face covers a lot of different kinds of approaches in the libraries.
[644.06 → 650.22] We're hearing over the last year or two, especially a lot about kind of the rise of deep reinforcement learning.
[650.34 → 654.00] It's been around for a while, obviously, but it's really come into its own.
[654.34 → 655.92] We're seeing it in more and more places.
[655.92 → 672.62] And what is it about that particular approach compared to some of the other approaches that it has replaced over time that is helping that become such a kind of one of the, you know, top tier first things you want to go to approaches these days?
[672.74 → 675.06] What's caused the rise of deep reinforcement learning?
[675.60 → 680.76] Well, I think it's because deep reinforcement learning is able to learn.
[680.76 → 682.94] We call that a policy, so a behaviour.
[683.26 → 686.34] It means choosing an action given a state.
[686.82 → 692.50] It's able to learn, you know, hidden behaviour that you couldn't, you know, train with classical models.
[692.84 → 694.94] So I think it's the first thing.
[695.18 → 701.26] And the second thing is also because deep reinforcement learning is becoming more and more efficient.
[701.70 → 705.14] You know, it was a big problem for a long time in deep reinforcement learning.
[705.14 → 709.74] It takes a lot and a lot of time to train compared to, you know, other models.
[709.74 → 718.10] And we're seeing that nowadays we have new models that are more and more powerful and require less and less data to train.
[718.58 → 724.98] So one of the things I was also wondering about is are there limitations to deep reinforcement learning that you're seeing?
[725.34 → 726.28] You know, what are the limits?
[726.38 → 733.18] We've seen some pretty amazing capabilities from all of these different deep learning capabilities over the last few years, these different algorithms.
[733.68 → 735.10] But what are the limitations?
[735.10 → 743.10] I know that I've heard people make some kind of crazy suggestions in various areas, and you're kind of like, we're not there yet, you know, or something.
[743.38 → 751.96] What are some of the limitations that you might caution people and say, maybe not, or maybe you're not looking at the right solution, or maybe we're just not there yet?
[752.16 → 753.00] Any thoughts around that?
[753.00 → 763.16] Yeah, there is, you know, for people who are doing deep reinforcement learning, they all know, you know, this article by Iran Alex called Deep Reinforcement Learning Does Not Work Yet.
[763.52 → 765.20] I think it was published in 2018.
[765.92 → 771.34] Nobody wants to talk about these articles, but it really presented every limitation of deep reinforcement learning.
[771.74 → 776.10] Limitations are, as I mentioned, something inefficient, but it's really changing.
[776.10 → 785.50] So something inefficient means that you need a lot and a lot and a lot of, you know, experience from your agent before, you know, is becoming good.
[786.12 → 789.94] And the second one is the most important is the problem of transfer learning.
[790.50 → 797.18] What we simply mean is that we are not able for now when you train an agent to transfer to another agent.
[797.56 → 801.22] So and the problem with that is also the problem of generalization.
[801.42 → 805.48] For instance, last week, I tried to train an agent to play Super Mario Bros.
[805.48 → 807.04] So it's a famous game.
[807.36 → 813.80] And when I tried to change the background, the background colour of the game, the agent become very bad.
[814.22 → 819.28] So the big problem is really the transfer learning and generalization error.
[819.48 → 828.04] What we simply mean is that for now, we can consider that a lot of deep reinforcement learning agents just overfit their environments.
[828.04 → 835.34] So they can't generalize, which is why I think it's a big problem in the deep reinforcement learning community.
[835.48 → 858.68] The change log is deep discussions in and around the world of software and has been going for over a decade.
[858.68 → 862.28] We interview hackers like Chris Anderson from 3D Robotics.
[862.56 → 867.26] At the time, drones were like predators and global hawks and military industrial.
[867.42 → 871.18] They were classified and super, you know, $10 billion things.
[871.18 → 877.36] We had just built a drone with Lego pieces around the dining room table programmed by a nine-year-old.
[877.60 → 879.88] And it's like, okay, that should not be possible.
[880.18 → 891.14] You know, when a nine-year-old can do something that is classified, that literally export control as ammunition with Lego, with toy pieces, it was something important in this world has changed.
[891.14 → 894.28] Leaders like Devin Fuel from GitHub.
[894.70 → 904.88] In the like 10 to 15-year range or 20-year range, what I would really like is for if you have like three 12-year-olds hanging out and one of them's like, I want to be a firefighter.
[904.96 → 906.52] Another one's like, I want to be a lawyer.
[906.66 → 909.00] I want one of them to say that I want to be an open source developer.
[909.60 → 911.28] And innovators like Amal Hussein.
[911.28 → 921.06] I've yet to kind of see applications at scale that don't use multiple languages, that don't have just arcane stories behind why this weirdo thing exists, you know?
[921.16 → 926.48] Like, all right, when you open this file, you're going to have to turn around three times and tap your nose once.
[929.00 → 932.20] Like it's just the most hilarious story, you know?
[932.28 → 934.46] But applications are living, breathing.
[934.78 → 935.96] They have craft.
[936.32 → 937.42] That's normal.
[937.42 → 943.90] So I want to normalize weirdness because that's just how applications evolve over time.
[944.60 → 946.08] Welcome to the changelog.
[946.38 → 950.44] Please listen to an episode from our catalogue that interests you and subscribe today.
[950.84 → 951.98] We'd love to have you with us.
[951.98 → 973.54] So the deep reinforcement learning course that you've been developing, how long have you been working on that?
[973.54 → 975.36] It started in 2018.
[975.76 → 979.68] And the last update was during the first lockdown.
[979.92 → 981.32] So it was in 2020.
[982.22 → 988.10] And initially it was just supposed to be two articles, and it becomes 10 articles and eight videos.
[988.28 → 994.82] I stopped updating it because I just updated the first articles because they were the oldest.
[994.82 → 1004.24] But now there is so much more, you know, educational resources that theory is still good, but the implementation, you know, are not relevant.
[1004.84 → 1005.84] You can still use it.
[1005.92 → 1006.98] You know, there are still people who use it.
[1007.08 → 1012.28] But I really advise people to look at the theory and use over implementation.
[1013.04 → 1019.14] There is, for instance, Costa Young who made very good implementation with what we call the Clean RL library.
[1019.14 → 1027.36] That you can use if you want to learn to implement from scratch, which is always a good idea to learn to implement from scratch, even though there is very good libraries.
[1028.04 → 1034.06] The best way to understand each architecture in deep reinforcement learning is really to implement by yourself.
[1034.46 → 1034.56] Gotcha.
[1034.72 → 1046.00] So would the target audience be someone, it sounds like someone who probably already is comfortable writing some code and probably has a little bit of familiarity with some of the other architectures out there?
[1046.00 → 1049.96] Or do you think it's a good one for someone who's just getting into it?
[1050.20 → 1053.04] How would you position somebody that you're recommending for your course?
[1053.22 → 1055.02] The course is really from beginner to expert.
[1055.36 → 1058.36] You just need to know to program in Python.
[1058.92 → 1064.60] But even though you don't know about PyTorch or TensorFlow, you can learn with the course.
[1065.16 → 1070.42] And I think that's why the course works great is that you don't need to be a mathematician to follow this course.
[1070.42 → 1090.52] Because in each chapter, what we do is that we really explain each part of the formulas, you know, because I think the big problem in deep reinforcement learning and in AI in general is that most of the people who start, you know, if they don't have a big, strong mathematical background, they can be very scared, you know, when they read a paper and there are big formulas.
[1090.52 → 1100.22] So the idea with this course is really to be very technical, but to go ahead step by step, not just to start, you know, with mathematics first.
[1100.92 → 1107.28] Do you think that deep reinforcement learning is a good first step into the deep learning world?
[1107.28 → 1114.96] It came along after, you know, like Natalie and I had our first exposures and stuff to the larger frame framework of deep learning.
[1115.14 → 1120.34] But if somebody was just coming in today, maybe they're in university, and they're studying.
[1120.62 → 1122.46] Is this a good place to start?
[1122.54 → 1129.56] Or would you say, no, no, go back to convolutional neural network or go back to other NLP things historically, start with transformers?
[1129.78 → 1135.20] How would you position deep reinforcement learning compared to that array of possible starting points?
[1135.20 → 1154.40] Well, I think it's better first to start with deep learning because we in deep reinforcement learning, we use, you know, neural network and also to work a little bit on convolutional neural network before starting deep reinforcement learning, because it's skills that you need to have before being able to start to learn deep reinforcement learning.
[1154.82 → 1160.46] And you mentioned in your about you that you're building the next generation AI in games.
[1160.60 → 1162.10] So tell us a little bit about that.
[1162.16 → 1162.98] That sounds fascinating.
[1162.98 → 1163.50] Yeah.
[1163.50 → 1163.56] Yeah.
[1163.82 → 1169.60] So before joining Aging Face, I really wanted to work, you know, in the video game industry.
[1170.26 → 1176.94] And what I started to do was initially to train reinforcement learning model for small games, casual games.
[1177.12 → 1183.82] But what I discovered is that in this part, you know, Game Studio use what we call behaviour tree, which is much easier.
[1183.98 → 1190.22] You know, its AI made by hand where the developer defines each action to take for an agent.
[1190.22 → 1199.26] And then after that, I started to see some demos about people who have conversation with AI, especially using OpenAI GPT-3.
[1200.08 → 1212.70] And I was fascinated, you know, with this part because I was like, you know, there is an equipment which works a lot on the video game industry that explained that in video games, you had a lot of improvement in terms of graphism.
[1212.70 → 1216.66] But in terms of interaction, we still, you know, at the dawn of age.
[1216.66 → 1227.22] So the idea was how we can use natural language processing models to create better interaction with what we call non-playable characters.
[1227.48 → 1232.40] So non-playable characters are, you know, games, you know, the AI with you have conversation with.
[1232.40 → 1235.78] And so I started to make some demo on that.
[1235.96 → 1246.52] We made a demo where you directly speak with NPC and their reply using OpenAI GPT-3 and an AI called Replica, which is an AI that generates voices.
[1247.42 → 1250.66] And at Hugging Face, we are currently working on a project.
[1251.12 → 1252.16] We don't have the title yet.
[1252.50 → 1260.28] It's called Murder on the Lighthouse, where you need to, there is a murder, and you have three characters, and you need to investigate who's the killer.
[1260.28 → 1264.46] But, you know, speak with them and find contradiction in their testimony.
[1265.02 → 1265.84] So that sounds good.
[1265.96 → 1272.30] So now that we're like into gaming, I got to ask, as you talk about it, I want you to expand just a little bit on it.
[1272.36 → 1275.58] Just I'm taking a slight detour here, but because I can.
[1275.58 → 1282.98] This is one of those moments, I will say as a parent, when I have a nine-year-old daughter interested in this, and she's going to want to hear this part.
[1283.20 → 1286.56] And so I'm kind of taking a detour to ask on behalf of my daughter.
[1286.56 → 1294.60] How should, as you're doing, you're using deep reinforcement learning in gaming, how do you kind of think about doing that?
[1294.70 → 1298.82] So there are a ton of kids I know because I'm listening to their calls.
[1298.96 → 1299.72] You know, we're in the pandemic.
[1299.92 → 1301.68] They're all doing online calls.
[1301.84 → 1307.26] So I will hear a bunch of young ladies that are deeply interested in gaming talking about it.
[1307.26 → 1313.66] But how can they think about what they need to be doing going forward to get into things like deep reinforcement learning?
[1313.78 → 1315.50] They want to do it in the context of gaming.
[1316.08 → 1325.58] Do you have some advice, since I have hijacked the conversation, so that those young ladies can start thinking about how they do this thing that that's what they really want to do?
[1325.66 → 1327.46] You're doing the thing that they're aspiring to.
[1327.46 → 1334.64] Well, if they want to use deep reinforcement learning in games, I think the first advice is to start to learn deep reinforcement learning.
[1335.06 → 1338.78] But there is also a lot of library that can use.
[1338.96 → 1340.88] And I think the best is to use Unity.
[1341.26 → 1348.36] They have something called ML Agents that allows you, you know, to create your game and then to train your agent on the game you created.
[1348.36 → 1355.10] For now, in video games industry, what can be done with deep reinforcement learning is mostly testing the game.
[1355.50 → 1359.46] So it means, you know, trying, having an agent that will try every part of the environment.
[1360.06 → 1367.20] But I'm pretty sure that in the future, we'll have AI in games that will be made with deep reinforcement learning.
[1367.80 → 1369.00] For now, it's not the case.
[1369.22 → 1371.64] We don't have published games who use it.
[1371.64 → 1377.02] But I really think that, you know, in the next year, it will be the case.
[1377.32 → 1381.14] But there is still some, you know, drawbacks to find solution.
[1382.02 → 1382.70] But, yeah.
[1382.84 → 1392.20] So as a bit of a tease for those who are curious to try more of the course, for example, I saw that on the website, there is, of course, Doom, right?
[1392.36 → 1393.42] Run Doom on everything.
[1393.66 → 1393.84] Yeah.
[1394.08 → 1398.16] So what are you doing in that course, for example, with Doom and with the games that we know?
[1398.16 → 1401.52] So during the course, we use, yeah, a different environment.
[1401.80 → 1402.36] We use Sonic.
[1402.64 → 1403.54] We use Mario.
[1403.78 → 1404.60] We use Doom.
[1404.92 → 1407.12] And in Doom, what you do, there are two levels.
[1407.48 → 1411.96] One, it's a simple level where you are in a poisoned place.
[1412.12 → 1414.98] So you lose health every time you walk.
[1415.40 → 1418.54] And so you need to grab, you know, the health pack to survive.
[1418.82 → 1420.68] So there is health pack spawn randomly.
[1420.68 → 1428.88] And the second one is you are in a corridor and there is some monster, and you need to shoot them before going at the end of the corridor.
[1429.12 → 1430.42] Otherwise, they will kill you.
[1430.74 → 1434.28] And after that, you have tons of other environment that you can use.
[1434.38 → 1438.84] Because always what we do in the chapter is that we always start with simple environment.
[1439.16 → 1442.54] And then we show you how you can iterate a more complex one.
[1442.54 → 1449.08] And in this Doom, there is, you know, death match, death match environment that you can use and you can train it.
[1449.12 → 1451.86] But it takes much more time than in this smaller environment.
[1452.60 → 1459.48] So I guess at this point, you know, with a little bit of the background on kind of how to get into the gaming and how to do that,
[1459.86 → 1465.96] where if someone goes through, and they've done your course, and they've started, and they've kind of they're learning their way into it,
[1465.96 → 1473.18] it's their first steps when they get to the end of the course, what kinds of things do you expect that they'll be able to do and be comfortable with?
[1473.52 → 1478.24] And then also, in addition to that, kind of where would you think they might want to go next?
[1478.54 → 1480.04] So they've kind of come through your course.
[1480.14 → 1481.24] It's the first one.
[1481.46 → 1487.80] They've now not only dipped their toes into this field, but have gotten some good hands-on experience.
[1487.96 → 1489.14] What comes next?
[1489.20 → 1490.74] What can they do, and where can they go from there?
[1490.74 → 1495.54] So after the course, they normally have the skill until the state of the art.
[1495.96 → 1503.08] So we go until proximal policy optimization, which is one of the state-of-the-art architecture and deep reinforcement learning.
[1503.62 → 1506.50] So they have the skills in terms of theory and in terms of practice.
[1506.98 → 1509.66] The next step will depend on what they want to do.
[1509.86 → 1516.18] If they want to work in video games, I would advise to learn to use Unity ML Agents.
[1516.50 → 1521.54] And in Unity ML Agents, they have free courses on how to use this library.
[1521.54 → 1530.24] And on the other hand, if they want to work in research, I would advise using Spinning Up Reinforcement Learning.
[1530.44 → 1534.08] So it's a course and a library made by OpenAI.
[1534.48 → 1542.76] Or to use Clean Reinforcement Learning, the one I talk about, to dive deeper on more complex implementation.
[1542.76 → 1552.98] So when are some surprising or unexpected uses that you see deep reinforcement learning was being used in the community?
[1553.50 → 1555.16] I think there was multiple.
[1555.34 → 1562.98] The first was the mine who use reinforcement learning for their cooler system in their server bay.
[1562.98 → 1569.10] The other thing, I think, when I was at the Techno, we worked on what we call dynamic pricing.
[1569.88 → 1574.12] And for video games, yeah, video games, there are a lot of funny things.
[1574.24 → 1577.94] For instance, you can train your agent on what we call Fujiko.
[1578.60 → 1581.00] And you can train, you know, like two feet.
[1581.48 → 1585.18] But you train to learn to walk with only two feet.
[1585.52 → 1590.70] You train making what we call the half cheetah to run, etc.
[1590.70 → 1593.22] So there are a lot of funny things around it.
[1593.68 → 1597.98] So you say that the thing that was in my head as you were describing that was,
[1598.08 → 1602.84] it seems like you really have to break things down to address things in a very precise way.
[1602.96 → 1608.22] So as we are moving forward, and this is in the deep reinforcement learning toolkit,
[1608.48 → 1614.22] for lack of a better word, is now part of creating games and all sorts of other things as well, obviously.
[1614.70 → 1618.82] Is that really what you kind of have to do is break down all of those things and think about
[1618.82 → 1621.28] how do I train just the feet, just the walking?
[1621.92 → 1628.98] Is it, might there be a time that you foresee where you can combine those, and it's able to do very complex things?
[1629.08 → 1631.44] Or are we still a long way from that point?
[1631.54 → 1637.10] Are you still going to have to do everything broken down in its individual constituents for a while?
[1637.10 → 1638.92] No, you can.
[1639.22 → 1645.04] There is, for instance, environments in ML agent where you train a complete humanoid to walk, etc.
[1645.70 → 1648.66] But there is a technique that we call curriculum learning.
[1649.26 → 1653.14] The idea is that you start to train your agents on very simple environments,
[1653.14 → 1656.42] and then you increase the complexity.
[1656.80 → 1660.08] So for instance, if you have an ensemble fight environment, you know,
[1660.36 → 1663.94] you start first to train your agent to learn to shoot snowball,
[1663.94 → 1666.90] and then you add, you know, the enemy.
[1667.36 → 1669.64] This way, you know, the agent will learn step by step.
[1669.76 → 1672.80] So it helps, you know, the training to have .
[1673.50 → 1677.66] You bring some interesting perspective into those different things that are,
[1677.84 → 1682.94] or the different usages for the deep reinforcement learning in your community and in general.
[1683.26 → 1689.26] Do you see that your original degree, which was not technical and was a bit of a different background,
[1689.26 → 1690.88] did it contribute to something?
[1691.04 → 1692.58] Did it help you in the way?
[1692.58 → 1698.42] Can you motivate people who have, who are positioned in a similar starting point as you were when you started?
[1698.58 → 1700.60] And how can this be a benefit?
[1700.90 → 1703.16] Yeah, I think it's very nice.
[1703.16 → 1707.26] Because I think the problem is that when I started, I thought, you know, that it was,
[1707.36 → 1710.18] it was something like a negative thing, you know,
[1710.20 → 1714.82] to not have a technical background and to come from, you know, a humanities background.
[1715.18 → 1720.82] But I think it's really important to consider that it's something positive when you start,
[1720.82 → 1730.08] because you have, you know, you have other way of thinking of other way of working than people who are more technical.
[1730.08 → 1732.84] So it's something to keep in mind.
[1732.84 → 1741.72] And I think that it's something that is feasible because nowadays, you have access to so much, you know, free educational resources online.
[1741.94 → 1745.70] For instance, if you want to learn mathematics, you have MIT OpenCourseWare.
[1745.92 → 1751.62] If you want to learn deep learning, you have Udacity and you have a lot of MOOC, you know, online.
[1751.62 → 1759.74] So my advice for people who come from, you know, humanities or less technical thing is just tried, start.
[1760.36 → 1764.14] And you'll see that, you know, it's hilarious to study.
[1764.72 → 1770.70] So, and the second thing is really don't feel like you don't belong here because, you know, you're not technical.
[1771.16 → 1776.36] You need to continue to work on and just don't think about the fact that you don't belong here because you belong here.
[1776.80 → 1780.22] If you do stuff, you know, you belong here, whatever your background.
[1780.22 → 1785.32] I'm so glad Natalie asked me that because your answer really got me thinking about something here.
[1785.44 → 1789.98] And that is, I'd like to expand that a little bit, extend the line of thought that you're on.
[1790.40 → 1798.22] We've been historically kind of in a place where there were quite a lot of barriers to entry for people moving into deep learning.
[1798.52 → 1803.00] And early on, you know, the university systems around the world are changing now to accommodate this.
[1803.56 → 1806.54] Most of us in the early days were coming from someplace else.
[1806.94 → 1809.40] It was hard for some people more so than others.
[1809.40 → 1813.22] I was just a software developer and I didn't have a lot of the mathematics on that.
[1813.36 → 1815.38] And so I had a steep learning curve myself.
[1816.06 → 1820.68] And with, but we've seen this trend over the years of more tooling.
[1820.80 → 1825.06] Hugging face has been a huge part of that, of the tooling becoming better and better.
[1825.06 → 1828.48] And it's kind of democratized the entire space.
[1828.80 → 1842.18] And it's allowed a lot more people to come into it without having to jump through quite as difficult of, you know, a set of hurdles as maybe the beginning days when there weren't, wasn't so much in the way of tooling and learning resources.
[1842.18 → 1869.52] So do you envision a day when you can be productive along these things where the things like doing deep reinforcement learning for gaming and stuff becomes a low enough bar to where somebody with some level of aptitude, some interest in that can kind of dive into it, even if it's not their primary thing to where they, you know, where it's, do you envision that it becomes that level of democratized?
[1869.52 → 1874.96] Or do you think there'll always be a certain level that you've got to really get to that's meaning.
[1875.10 → 1881.66] And when I say that meaning a bit of a challenge to get to as an entry point into it, how do you see that changing over time?
[1882.26 → 1891.84] Well, I think it's clearly possible because, you know, at Hugging Face, we already have something called auto NLP that allows you to train and to create models without coding.
[1891.84 → 1907.50] And I really believe that the next step in deep reinforcement learning is really that type of thing, you know, being able to just, you know, directly train the model without having, you know, to know everything about the model or how it works, etc.
[1907.50 → 1910.78] But I think, yeah, it's very still work before that.
[1911.18 → 1920.90] But in the future, it's clearly possible because, you know, AI will become something that we'll use as we use software, you know, so we will not need to know how it works.
[1920.98 → 1923.80] We will not need to know behind the hood, you know, it works.
[1923.88 → 1928.26] We just need, you know, to start the training and having some trend the most results.
[1928.26 → 1938.38] And in addition to the human part of this, what are the fields that you see in the future that will be revolutionized by deep learning?
[1939.02 → 1945.46] I think everything, you know, especially the industry, you know, with the robotics, we'll see more and more, you know, robotics.
[1945.94 → 1954.90] And I think on the one hand is a good thing because it will remove a lot of work that are very hard and that really, you know, underpaid.
[1954.90 → 1962.10] So it's a good thing. But also, I think in health, you know, we already see, you know, application in health with, you know, cancer detection.
[1962.34 → 1968.36] We see also, you know, with the mind who works, you know, on the question of protein detection.
[1969.26 → 1975.68] So for me, AI will change everything, but it's really important to consider that it will not solve everything.
[1976.06 → 1981.84] You know, for instance, you know, we all talk about the question that AI will help a lot in healthcare, as I mentioned.
[1981.84 → 1988.16] But the problem is that if people can't afford, you know, to access these tools, the problem is not solved.
[1988.74 → 1998.82] So I think what's important to consider is that we need to improve AI, but AI must be, you know, really accessible to everyone to be a solution to, you know, human problems.
[1999.48 → 2000.78] That's a great point you make there.
[2000.78 → 2011.26] And we find ourselves in different aspects talking about, you know, pieces of that all the time in terms of who has access to the technology.
[2011.96 → 2017.92] And, you know, some of us who are privileged to be in this field, maybe we get stuck in our bubble at times.
[2018.12 → 2023.20] And, you know, we're, you know, there are robots are starting to come around here, and it's right around the corner.
[2023.20 → 2031.94] And we're thinking about this, but there's kind of huge, huge segment of the world out there who hasn't really had access to this yet.
[2032.50 → 2046.90] So given that, you know, even with the best work from people like you and Hugging Face and others out there, we definitely have challenges of equity in terms of people having access to good solutions for their life.
[2046.90 → 2050.26] Do you have any thoughts on things that we can do?
[2050.66 → 2066.86] Because I know, I think it needs to be forefront of our mind, things that we can do that are in this field to try to steer these solutions toward those places and people that might need them worse than we do in a lot of ways that don't have all the benefits that some of us are enjoying right now.
[2066.98 → 2069.72] Any thoughts on how we find that path?
[2069.76 → 2070.84] It seems really hard to me.
[2070.84 → 2076.78] Well, I think there are a lot of positive things that's happening, especially because of open education.
[2077.42 → 2082.26] You know, the majority of people who look at MOOC are people from developing countries.
[2082.86 → 2088.52] So the new generation, especially in developing countries, are more and more educated.
[2089.16 → 2102.54] So I think if we want that AI will be accessible for everyone, we need to make sure that our models are open source, that, you know, everyone can participate in the documentation, participate in the project.
[2102.54 → 2120.60] And the second thing is more, I think, a politician thing, because we will need, you know, laws that make to force, you know, companies to make their AI accessible, to make their AI, you know, that we can analyze what's inside the AI to avoid bias and all that problems.
[2120.60 → 2123.46] So I think it's two parts for us.
[2123.46 → 2137.56] So for people who work in AI, we really need to work on the question of making educational content free or at least very cheap and working on open source projects and try to share as maximum as possible.
[2137.56 → 2150.74] And on the other side, we need to push our politicians to work on legislation to make sure that AI will be here for good and not for negative stuff.
[2150.74 → 2152.70] Yep, that makes a lot of sense.
[2152.70 → 2153.98] I absolutely agree.
[2154.58 → 2162.26] Oktoberfest is also time of the year when everybody who wants to start with open source, I always like recommending contributing to the docs.
[2162.48 → 2168.86] Like you say, this is a wonderful way to participate, and it has a less of a threatening entry threshold.
[2169.44 → 2171.18] Oh, I could absolutely not agree more.
[2171.88 → 2178.54] So the future scientist who is listening to this episode today, what is the first step that they should take in this field?
[2178.54 → 2189.86] I think the first step will be to just start with an introduction to deep learning and then, you know, to try different projects just to see what you prefer.
[2189.98 → 2198.86] If you want to dive more on NLP, so natural language processing, on deep reinforcement learning or, you know, on computer vision, audio, etc.
[2198.86 → 2209.80] I think the idea is not really to overthink, you know, this part because most of the people, you know, that I met who want to start always get stuck, you know, because there is a wide range of possibilities.
[2209.80 → 2217.26] And the only thing is just, you know, type on Google what you want to start on and start to learn deep learning.
[2217.62 → 2222.82] Take the first link, see how it goes, you know, and then iterate from that.
[2223.34 → 2228.86] But yeah, don't overthink, you know, because most of the people overthink and just say, oh, this is maybe not the best resources.
[2229.08 → 2231.20] This is not maybe what I want to do, etc.
[2231.20 → 2233.18] Just try and you'll see.
[2233.60 → 2237.36] So that future scientist has taken that first step.
[2237.62 → 2241.10] They are diving into this and doing exactly what you just said.
[2241.38 → 2245.56] Along the way, they're taking your course and they are learning these skills.
[2245.56 → 2261.50] And they are there in a world that is increasingly, you know, having this just amazing gamified experience that is now becoming available widely and not just, you know, in the context of video games, but across all life.
[2262.14 → 2269.78] And simultaneously, deep reinforcement learning is driving robotics, which are becoming ever more common as these new scientists are growing up.
[2270.18 → 2274.40] I'm thinking obviously of my daughter in this context, as I'm sure you figured out.
[2274.40 → 2279.82] So what are they grow up, and they are adults now, and they've come through this process.
[2280.30 → 2281.60] What do you think the world looks like?
[2281.78 → 2286.24] What do you think maybe some opportunities or challenges that they might face?
[2286.60 → 2291.42] And along the way, I would love your opinion about what you'd like to see as opposed to what you think will be there.
[2291.52 → 2297.82] You know if you have any preferences about what you're aspiring for right now as a data scientist doing this kind of work.
[2298.20 → 2303.80] Well, I think, yeah, in the future, clearly we will have much more robots than nowadays.
[2303.80 → 2310.88] They will do a lot of tasks, especially social tasks in terms of, you know, helping older people.
[2311.02 → 2316.50] We know with the question of autonomy, we will have, you know, autonomous cars, all of that question.
[2316.94 → 2325.06] What I really don't want to see especially is the question of using these technologies for, you know, military things, you know,
[2325.06 → 2329.68] because we see more and more, you know, the question of especially deep reinforcement learning.
[2330.02 → 2338.64] We see more and more people talking about using deep reinforcement learning for, you know, robots in during battles on that kind of stuff.
[2338.64 → 2341.34] And I think this is the worst thing to do.
[2341.46 → 2349.96] I think it's something that's unfortunately will go to happen because, you know, if someone does it, all the other country wants to do it, you know, to protect themselves.
[2350.50 → 2358.06] But it's really something bad because it's really something we don't want to do, and we shouldn't do.
[2358.06 → 2361.76] But unfortunately, I think we don't have a lot of power on that.
[2362.12 → 2371.86] The thing is, if I want to be positive, is when you work in this industry, we always need to think about the consequences of what we do.
[2372.22 → 2373.84] You know, sometimes it's very small consequences.
[2373.84 → 2381.08] But when we work on some models, we can, you know, induce bias that can, you know, be negative for a group of people.
[2381.60 → 2386.76] And it can be, you know, much, much worse than that if we speak about, you know, robots in army.
[2386.92 → 2397.28] But it's always important when we work on something to think on the consequences because sometimes, you know, we are too focused on the project, and we don't think about, you know, the outcomes of what we are doing.
[2397.94 → 2401.42] Well, Thomas, thank you very, very much for coming on to the show today.
[2401.42 → 2404.64] And Natalie, thank you very much for co-hosting with me.
[2404.78 → 2405.80] This has been a lot of fun.
[2405.90 → 2409.14] It's been a great conversation and really appreciate you.
[2409.16 → 2415.02] I hope you will come back sometime and tell us kind of what you've done next and deep reinforcement learning and other things.
[2415.32 → 2416.02] Sure. Thanks.
[2416.24 → 2416.74] Thanks, Thomas.
[2419.82 → 2420.74] All right.
[2421.02 → 2422.78] That's Practical AI for this week.
[2422.92 → 2423.72] Thanks for listening.
[2423.92 → 2428.64] If this is your first time with us, subscribe now at practicalai.fm
[2428.64 → 2432.92] or simply search for Practical AI in your favourite podcast app, we're in there.
[2433.24 → 2437.34] And if you're a longtime listener, do us a solid by recommending the show to a friend.
[2437.82 → 2441.72] Word of mouth is still the number one way people find new podcasts they love.
[2442.10 → 2446.62] Special thanks to our partners for supporting our work, Vastly, Launch Darkly, and Linde.
[2446.78 → 2447.58] We appreciate it.
[2447.58 → 2451.78] And to the mysterious Break master Cylinder for cranking out new beats for us all the time.
[2452.12 → 2452.90] That's all for now.
[2453.34 → 2454.50] We'll talk to you again next week.
[2458.64 → 2488.62] We'll talk to you again next week.
