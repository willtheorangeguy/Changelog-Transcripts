[0.00 --> 8.64]  Welcome to Practical AI.
[9.20 --> 15.96]  If you work in artificial intelligence, aspire to, or are curious how AI-related technologies
[15.96 --> 18.78]  are changing the world, this is the show for you.
[19.20 --> 24.36]  Thank you to our partners at Fastly for shipping all of our pods super fast to wherever you
[24.36 --> 24.66]  listen.
[24.92 --> 26.76]  Check them out at Fastly.com.
[26.76 --> 32.02]  And to our friends at Fly, deploy your app servers and database close to your users.
[32.44 --> 33.70]  No ops required.
[34.02 --> 36.08]  Learn more at fly.io.
[43.06 --> 46.28]  Welcome to another episode of Practical AI.
[46.68 --> 48.36]  This is Daniel Whitenack.
[48.44 --> 50.36]  I'm the founder of Prediction Guard.
[50.36 --> 55.78]  And I'm joined as always by my co-host, Chris Benson, who is a tech strategist at Lockheed
[55.78 --> 56.08]  Martin.
[56.08 --> 57.40]  How are you doing, Chris?
[57.76 --> 59.00]  Doing well today, Daniel.
[59.96 --> 66.62]  There's so much going on these days in this industry in terms of AI that just constantly
[66.62 --> 69.20]  learning new stuff and finding out who's doing what.
[69.54 --> 75.42]  Yeah, it's almost like you need to optimize some things about your life to keep up.
[75.52 --> 76.58]  Would you say that's accurate?
[76.86 --> 77.24]  Yeah.
[77.40 --> 80.38]  Speaking of optimization, I think that's a thread to pull right there.
[80.78 --> 81.74]  Yeah, yeah.
[81.74 --> 91.20]  So speaking of today, we have with us Mike Basios, who is the CTO and co-founder at TurinTech
[91.20 --> 91.60]  AI.
[92.04 --> 92.60]  Welcome, Mike.
[92.98 --> 93.54]  Hello, guys.
[93.70 --> 94.36]  Nice to meet you.
[94.70 --> 94.90]  Yeah.
[95.00 --> 96.86]  Well, we alluded to optimization.
[96.86 --> 104.82]  And I know one of the things that TurinTech is working on is code optimization with AI.
[105.40 --> 110.88]  And maybe some people, actually, probably a lot of people listening to this podcast are
[110.88 --> 118.52]  familiar with certain developer tools that are AI flavored, maybe GitHub Copilot or something
[118.52 --> 120.26]  like that for generation.
[120.78 --> 127.74]  I'm wondering if you could take a moment before we dive into AI driven code optimization.
[127.74 --> 130.78]  If you could just help set the stage for those that aren't aware.
[131.30 --> 133.40]  What do you mean when you say code optimization?
[133.76 --> 134.62]  Why is it useful?
[134.80 --> 141.88]  How has code optimization, quote unquote, been part of the developer lifecycle for some time?
[141.88 --> 151.64]  We are in an area nowadays that we see more and more applications consuming a lot of cloud
[151.64 --> 153.54]  resources and a lot of resources.
[153.90 --> 159.12]  And everybody is trying to optimize the performance of their code.
[159.26 --> 164.58]  Now, when we're talking about code optimization and in particular performance, typically people
[164.58 --> 170.78]  would like to optimize things like application being faster, maybe memory consumption.
[170.78 --> 176.22]  We know everybody complaining about Chrome using too much memory, for example, in the past.
[176.72 --> 183.76]  Or CPU usage, which is connected very much with the energy that the different software is using.
[183.92 --> 189.66]  If we talk about mobile phones, application there, we would all like to be more efficient and
[189.66 --> 190.74]  consume less energy.
[191.48 --> 197.04]  And practically, that's the area that we have been focusing in my research and our group in
[197.04 --> 198.56]  our research and in the company.
[198.56 --> 203.42]  Maybe you could talk a little bit about some of the history of that research.
[203.56 --> 209.80]  I'm sure that that has, just like everything else, been impacted by this kind of latest wave
[209.80 --> 212.76]  of AI technologies and generative AI.
[213.26 --> 220.56]  But I know that the company and yourself have been involved in research prior to and all during
[220.56 --> 221.96]  the development of these things.
[221.96 --> 228.34]  So could you give us a little bit of background on how you first started thinking about these
[228.34 --> 231.38]  problems and how it kind of developed over time?
[231.82 --> 231.96]  Yeah.
[232.14 --> 233.98]  Code optimization is not a new thing.
[234.08 --> 239.82]  If you read the research papers 20, 30 years ago, everybody would like to optimize and make
[239.82 --> 240.64]  the code efficient.
[241.10 --> 245.02]  Like there are a lot of tools like profilers.
[245.20 --> 249.06]  There are, you know, that help developers find hotspots.
[249.06 --> 255.20]  The biggest problem in this area is, okay, we profile our code, but how we can automatically
[255.20 --> 257.40]  improve it so we make it faster.
[257.92 --> 260.38]  Typically, this is a very, very manual process.
[260.76 --> 266.18]  And majority of the people that work on this area are super specialized.
[266.18 --> 273.40]  And it's more and more difficult nowadays to find people that know how to optimize the performance
[273.40 --> 279.12]  of their code because the programming languages are becoming higher and higher level.
[279.48 --> 283.98]  Like now people write more in language like Python, JavaScript, TypeScript.
[284.54 --> 291.44]  So nowadays, the real companies that deal with code optimization are companies in the lower
[291.44 --> 298.06]  of the hardware space, like big Intel, NVIDIA, and those, they write specialized software
[298.06 --> 303.34]  that take advantage of their hardware, whether they show the hardware it outperforms, or technology
[303.34 --> 305.18]  companies that need the scalability.
[305.46 --> 313.78]  But majority of developers will not necessarily bother about the performance of the code as an
[313.78 --> 316.64]  immediate first thing that they need to optimize.
[316.64 --> 324.50]  And we have tried and we have a platform that we helped practical engineers to automate this
[324.50 --> 330.80]  kind of process to make it easier for developers to identify places in their code that are slow,
[331.04 --> 337.50]  and then to optimize it without necessarily having the knowledge that they need, but also do
[337.50 --> 338.20]  it automatically.
[338.84 --> 343.54]  Now, the history of code optimization, as I said, it was a very, very manual process at the
[343.54 --> 344.10]  very beginning.
[344.10 --> 348.36]  Very few people know how to optimize code for specific hardware.
[348.74 --> 353.06]  You know, they had in the past, I guess, they had to read books and compiler options.
[353.66 --> 356.46]  Eventually, then you had better and better compilers.
[356.74 --> 363.70]  So you can use compilation option to optimize your code and tune the options of the compilers,
[363.86 --> 364.14]  et cetera.
[364.28 --> 369.20]  And then you have a lot of profiling tools that help developers also optimize.
[369.20 --> 376.78]  But still, all these processes most of the time has been manual or semi-manual, right?
[377.22 --> 382.82]  And that's where we see the advances of AI helping this process.
[383.28 --> 389.48]  And to give you a bit of context how we started our startup, this started after we published
[389.48 --> 394.84]  a paper in 2018, I think, that was in the Foundation of Software Engineering Conference,
[394.84 --> 400.70]  where we showed that we could automatically help developers choose better data structures
[400.70 --> 406.70]  by taking a code, looking at data structures, and optimize it by giving variations.
[406.86 --> 411.72]  For example, sometimes in languages like Java, for example, you don't need to use an array
[411.72 --> 412.10]  list.
[412.28 --> 416.48]  If you potentially can use a link list in a scenario that may be better.
[416.48 --> 423.04]  So we try to do these small changes and show that we have good performance impact.
[423.68 --> 430.34]  But majority of people at that point were manually translating code, like rule-based transformation,
[431.18 --> 432.36]  like regular expressions.
[432.44 --> 434.78]  If I see this pattern, convert it to this pattern.
[435.24 --> 441.80]  So that is how people have been doing those things with code refactoring tools until the LLM
[441.80 --> 443.26]  came into the discussion.
[443.26 --> 448.98]  Speaking of that, kind of getting into this latest wave of maybe what I'll just refer to
[448.98 --> 452.52]  as developer tools that are AI related.
[452.80 --> 460.54]  Again, you know, people might be familiar with code generation type of tools or explainers or
[460.54 --> 461.46]  something like that.
[461.88 --> 468.78]  There've also been, I've seen kind of agentic type of tools that will like write up PR for
[468.78 --> 473.06]  you to do, like you say, hey, I want to do this thing.
[473.20 --> 474.82]  And there's a PR generated.
[475.50 --> 481.94]  Here, given the focus on code optimization, could you draw out some of, just for people
[481.94 --> 486.66]  that are maybe kind of getting into this, could you draw out some of when they would
[486.66 --> 494.38]  want to use this kind of tool versus some of these other maybe generative application or
[494.38 --> 497.12]  applications of generative AI to code, I guess.
[497.12 --> 497.46]  Yeah.
[497.52 --> 498.84]  How does it fit into that ecosystem?
[499.32 --> 505.02]  So the way we present the code optimization tool currently is part of your CI, CD process.
[505.48 --> 509.78]  So you make a pull request, then you will run some unit tests.
[509.98 --> 511.50]  You will have your integration testing.
[511.78 --> 517.04]  Potentially, you'll have a scanning, security scanning tool like SNCC or check marks, et cetera.
[517.04 --> 522.12]  And then the next step is, depending on where your application is deployed, we analyze your
[522.12 --> 528.46]  code and we tell you, make those changes because you can have this 20% improvement in CPU and
[528.46 --> 529.80]  execution time, et cetera.
[530.30 --> 537.58]  That is the way we present it currently as a CI, CD tool in the tool chain of the developer
[537.58 --> 537.98]  tools.
[537.98 --> 545.30]  However, if you think about the technology underneath and all dev tools, the way I see it, are going
[545.30 --> 550.24]  to be using AI and they will take advantage of LLM-based solutions.
[550.24 --> 557.10]  From the moment you are using LLM, if you generate code or you translate code, it's a kind of the
[557.10 --> 560.28]  same kind of approach.
[560.54 --> 564.40]  It depends on the data that you will apply the LLM.
[564.94 --> 571.22]  So code generation tools, practically, they see when you say for the PR example, the way
[571.22 --> 576.48]  those LLMs have been trained is that they see that there is some comments below the code.
[576.48 --> 580.28]  So you say, if I give you those comments, can you predict the code?
[580.86 --> 586.46]  So in the code translation, where you don't know about the speed of the code, you say, I
[586.46 --> 589.82]  have seen this C++ code and the equivalent of Python code.
[589.92 --> 590.92]  And LLMs do it.
[591.08 --> 595.76]  Like, for example, Copilot or ChatGPT, they can translate code.
[596.10 --> 598.92]  Like, if it's perfect, probably not yet.
[599.26 --> 601.18]  But that is a fundamental technology.
[601.18 --> 607.58]  So code optimization is on the same set of tools, but it says, this is a slow code that
[607.58 --> 608.16]  I have seen.
[608.74 --> 610.96]  Now I have seen a variation of faster code.
[611.38 --> 614.42]  So I can recommend you this faster code.
[614.86 --> 617.12]  But eventually, you can expose the LLM.
[617.48 --> 626.38]  Like any other tool that is built on VS Code or LLM-based, you can expose it in an editor.
[626.38 --> 632.90]  And then the developers from our LLM will get suggestion for faster code.
[633.02 --> 638.84]  That doesn't mean that will be beautiful code necessarily, but it will be faster for the
[638.84 --> 640.70]  hardware that you need to run it.
[640.84 --> 646.22]  I'm kind of curious, as we're talking about speed, are there any other dimensions that are
[646.22 --> 650.98]  relevant in there that you guys are interested in that are either adjacent to speed or contribute
[650.98 --> 656.68]  to speed or any other characteristics that may not be directly speed specific, but are
[656.68 --> 659.04]  things that you're starting to target or expect to target?
[659.60 --> 662.04]  We apply multi-objective optimization.
[662.40 --> 667.16]  So when you do the translation, you can have different objectives that you try to optimize.
[667.32 --> 668.54]  Like speed is one factor.
[669.24 --> 670.46]  Memory usage is another.
[671.32 --> 672.22]  CPU usage.
[672.58 --> 676.88]  Typically, there is a trade-off between speed and memory usage.
[677.10 --> 680.40]  If you have more memory, you would like to use it, it increases speed.
[680.40 --> 685.02]  So our tool allows you and gives you different suggestions for what you need.
[685.60 --> 692.52]  But we see users, for example, we see this paradigm to be used in other use cases.
[692.76 --> 699.28]  Like users have told us, I can improve the readability of my code as far as I know that I don't
[699.28 --> 701.08]  impact performance, for example.
[701.42 --> 707.82]  Because there are managers in teams that they have five projects and they would like, let's
[707.82 --> 710.22]  say, five projects with five teams with developers.
[710.40 --> 714.76]  And they would like to guarantee that the quality across is good.
[715.40 --> 721.94]  So this AI approach, these tools, Artemis, our tool or other tools in the LLM space will
[721.94 --> 725.02]  be able to help with those.
[725.18 --> 732.54]  But the biggest problem of any LLM-based tool currently, like Chris, you mentioned you are
[732.54 --> 734.08]  working for Lockheed Marketing, etc.
[734.08 --> 737.70]  Is that the code generated by any LLM.
[738.24 --> 742.08]  It's not guaranteed that will work 100%.
[742.08 --> 747.86]  Also, you need existing tools to check if this code is secure.
[748.56 --> 751.52]  And also, you do not know if you will break your code.
[751.52 --> 755.96]  So still in the early stages of incorporating those LLMs.
[756.06 --> 759.54]  That's why it's also easy for a developer to give it as a suggestion right now.
[760.16 --> 768.86]  But I'm pretty sure like companies like that working bug fixing, code security checks, they
[768.86 --> 775.30]  are using and they will be using more and more LLMs because they can train on the data that
[775.30 --> 776.00]  they have access.
[776.00 --> 777.78]  So they can have competitive advantage.
[778.54 --> 783.34]  Would it be a good parallel just to kind of draw up to people's mind, like maybe something
[783.34 --> 785.10]  they've seen before in other domains?
[785.30 --> 791.84]  It almost sounds like a parallel to kind of a rephrasing type of prompt in an LLM where
[791.84 --> 798.88]  you might say, like, I do this a lot with, you know, emails or other things like, here's
[798.88 --> 804.22]  my really bad email, you know, make it flow better and sound better.
[804.22 --> 810.66]  Or here's my goofy email, make it business professional or something like that.
[811.24 --> 816.54]  You drew the comparison to like maybe machine translation or something like that.
[816.58 --> 819.54]  Is rephrasing kind of a good way to think about this?
[820.24 --> 823.16]  Let me give you a very simple example.
[823.28 --> 828.64]  Let's say you have an essay that you need to write and you have 10 paragraphs in that essay.
[828.64 --> 834.78]  And you would like to have a version of that essay that is much better and you can get a
[834.78 --> 836.50]  better grade, right?
[836.84 --> 843.12]  Now, what we do is we will look all the paragraphs and we will provide you better variations.
[843.96 --> 848.68]  So we will get you version one with three changes that are applied by different LLMs.
[849.46 --> 852.78]  Then you would need somebody to grade that essay.
[852.78 --> 855.94]  So in this case, we measure how fast the code is.
[856.28 --> 859.08]  So somebody says, okay, you have a 70%.
[859.08 --> 864.20]  Then we take that output and then we provide and give it back to the LLM and give you another
[864.20 --> 864.60]  version.
[865.10 --> 869.30]  So practically, you start from version zero of your essay.
[869.50 --> 871.32]  You apply the different LLMs.
[871.54 --> 872.28]  You get feedback.
[872.54 --> 876.32]  So it's like reinforcement learning, live learning and get different variations.
[876.32 --> 878.48]  And that score will be increasing eventually.
[878.48 --> 884.88]  And at the end, you have like a translated version of your original version that the LLMs and all
[884.88 --> 888.72]  those refactoring did, which is better on the metric that you have.
[889.34 --> 896.00]  But we in the platform test that the code passes, we compile it, and also we run the performance.
[896.42 --> 898.92]  In this scenario, we'd have a teacher that would grade.
[899.48 --> 906.10]  And if you think how OpenAI and everybody has been doing their training, they usually get LLMs
[906.10 --> 910.74]  and then they use reinforcement learning and HLF and all those techniques.
[911.26 --> 913.98]  So we have done that in the code optimization setting.
[914.22 --> 920.70]  That's why we have had some impressive results in taking an open source library and we just
[920.70 --> 925.88]  put in a tool and then suddenly optimize by 30% execution time without us doing anything.
[926.08 --> 927.30]  The models learn themselves.
[933.38 --> 935.38]  This is a Changelog Newsbreak.
[935.38 --> 942.54]  You can add Meta's CodeLlama to the ever-expanding list of code-generating LLMs.
[943.02 --> 950.36]  Based on LLMA 2, CodeLlama comes in three sizes, 7 billion parameters, 13 billion, and 34 billion.
[950.68 --> 952.90]  And it comes in three different varieties.
[953.50 --> 959.62]  A general model, one tuned for NLP instructions, and one fine-tuned for Python.
[960.10 --> 961.10]  How does it stack up?
[961.10 --> 968.92]  Well, Meta claims it outperforms other publicly available LLMs and it shares the same open-ish license as LLMA itself,
[969.32 --> 973.10]  which is free for research and commercial use unless you compete with Meta.
[973.10 --> 978.44]  You just heard one of our five top stories from Monday's Changelog News.
[978.82 --> 985.54]  Subscribe to the podcast to get all of the week's top stories and pop your email address in at changelog.com slash news
[985.54 --> 991.22]  to also receive our free companion email with even more developer news worth your attention.
[991.64 --> 995.12]  Once again, that's changelog.com slash news.
[995.12 --> 1008.06]  So, Mike, you got into something that I'm super interested in in terms of how you're going about this problem,
[1008.06 --> 1015.54]  which you alluded to the fact that you're using this sort of reinforcement learning loop or feedback loop
[1015.54 --> 1019.50]  to improve the performance of your tools.
[1019.72 --> 1028.74]  Given that you and your team have worked with sort of code generation or code-specific models for some time now,
[1029.18 --> 1033.36]  before we get into kind of some of the cool stuff that you've done specifically,
[1033.78 --> 1039.90]  could you just comment on kind of the state of code generation models that are out there
[1039.90 --> 1042.66]  on maybe the open source side specifically,
[1042.84 --> 1046.28]  but if you want to highlight any, you know, closed source ones, that's perfectly fine too.
[1046.28 --> 1054.26]  But from your perspective, how is that, the ecosystem of code generation models changing and advancing
[1054.26 --> 1057.36]  and what is the state of it sort of these days, I guess?
[1058.08 --> 1067.72]  So, I was one of the very first believers of LLM assistive code generation tools.
[1067.72 --> 1074.66]  Like, I tried to get bad access to GitHub Copilot, even tried to use GPT-3 to see all this kind of technology.
[1074.78 --> 1085.60]  I'm a very big believer because I have seen members of our team using LLM to build things much, much faster to code.
[1085.66 --> 1087.78]  For example, we had the backend engineer.
[1087.94 --> 1089.62]  We needed a prototype for a frontend.
[1089.94 --> 1094.06]  He just used one of the closed source LLMs.
[1094.06 --> 1098.44]  And he could, in one day, he did a new UI that he didn't even know the language.
[1098.56 --> 1099.36]  He didn't know TypeScript.
[1099.88 --> 1103.64]  So, I see that they are very, very promising.
[1104.14 --> 1111.02]  I see more usage right now for good developers that already know, you know, the basic of computer science.
[1111.12 --> 1113.16]  I'm not a believer of, hey, you don't need to code.
[1113.24 --> 1115.06]  You will use this LLM for you, right?
[1115.12 --> 1118.98]  That are, you know, some videos, potential, they are over-promoting that.
[1118.98 --> 1134.74]  But if you are a good enough developer, you know what you need and you use, they can practically help you dramatically to build easy applications, you know, to generate tests, to generate comments about your code.
[1135.24 --> 1143.08]  And, of course, the performance of, from our experience, I believe GitHub Copilot and ChatGPT are still outperforming the other models.
[1143.08 --> 1152.72]  But we see more and more open source models starting to become very, very good into the different languages.
[1152.72 --> 1155.50]  Like, we have been trying LLAMA 2.
[1155.72 --> 1157.08]  We have been trying CodeGen.
[1157.28 --> 1158.70]  We have been trying all of this.
[1158.76 --> 1162.70]  And we even expose them to our platform so people can compare the results of those.
[1162.70 --> 1171.90]  Those tools will need to become a bit easier for developers and VS Code tools to use.
[1172.16 --> 1181.12]  Because by default, people, this API exposure that some of the closed source models are giving is solving a lot of headaches for a lot of developers.
[1181.32 --> 1185.28]  That's why a lot of developers still have preference for this.
[1185.40 --> 1188.90]  But definitely open source models, they are very good.
[1188.90 --> 1196.06]  And I see them becoming even better if they are fine-tuned on specific language or specific context.
[1196.30 --> 1197.26]  I'll give you an example.
[1197.44 --> 1205.42]  If you want, if we want to do translation from SQL to an SQL, let's say we want to optimize SQL queries that people are doing in their databases,
[1205.42 --> 1209.38]  you can take one of the open source models and fine-tune it on SQL.
[1209.78 --> 1215.66]  And you probably will outperform GPT 3.5 or 4 on the context that you have.
[1215.66 --> 1218.28]  But I'm truly a very big believer.
[1219.24 --> 1223.40]  It's a bit of psychology between developers that, hey.
[1223.90 --> 1230.34]  But I am a believer that people that will use, they have advantage over people that don't use those tools currently.
[1231.12 --> 1233.38]  So that raises an interesting point.
[1233.52 --> 1236.04]  It's a little bit of a tangent, but you've kind of inferred it.
[1236.04 --> 1239.74]  This is kind of changing the way we humans are coding.
[1240.26 --> 1247.74]  I know you also talked about whether LLMs would just write the code for us and the overhype, you know, certainly today about that.
[1248.00 --> 1261.48]  But it's kind of changing the way that we code as humans and it's extending our capabilities dramatically in terms of being able to reach beyond what we might have been able to do two years ago, for instance.
[1261.48 --> 1283.80]  Do you see that accelerating when you're looking at the fact that if you looked at a traditional coding team a few years ago as you're producing your product for folks and you're starting to recognize that individual coders are starting to elbow their way out of their traditional swim lanes with these new tooling capabilities that you're providing, how does that change things?
[1283.88 --> 1287.04]  Like how does the market change that you're looking at going forward?
[1287.04 --> 1292.14]  I believe dramatically and that we have tested this with our internal developers.
[1292.58 --> 1302.06]  I have seen dramatic improvement in productivity of developers without access to LLMs and developers that have like there are two things.
[1302.18 --> 1306.62]  One is you can make more efficient developers that everybody would like to hear.
[1306.96 --> 1314.32]  But from a more senior level manager level, you do not need, unfortunately, as many developers as you would need before.
[1314.32 --> 1316.84]  You cannot avoid this.
[1317.36 --> 1328.32]  And developers should think for me like, okay, I am competing with some other developer in my team to produce, let's say, an API or produce a UI.
[1328.64 --> 1342.50]  If the guy has access to co-pilot or chat GPT, the other person doesn't have, I guarantee you like with very, very big chances, the guy that has access to chat GPT and those will outperform and have faster results.
[1342.50 --> 1348.72]  So it is like you have a very, very good assistant next to you that you should use.
[1348.86 --> 1349.90]  Otherwise, you are losing.
[1350.20 --> 1351.02]  That's how I see it.
[1351.22 --> 1351.34]  Yeah.
[1351.44 --> 1362.50]  As a two-second follow-up to that point you just made, when we start pervasively, because I think I've seen some stuff recently over the last month or two that like the majority of active developers out there are now using LLMs.
[1362.50 --> 1367.64]  So there's been really rapid adoption here within the developer community.
[1368.16 --> 1375.96]  So we've kind of moved very quickly from those who had versus those who didn't have into a world where everybody has.
[1376.04 --> 1380.68]  They may not all be using exactly the same models as things progress, but everyone has it.
[1380.94 --> 1383.02]  Any thoughts about kind of what that means?
[1383.02 --> 1389.02]  It's like you're democratizing LLMs across the population of developers, and now they're competing.
[1389.16 --> 1393.54]  So it's kind of like me and my LLMs are competing against you and your LLMs as a developer.
[1394.14 --> 1398.00]  Just any thoughts waxing poetic a little bit about what the implications there are?
[1398.36 --> 1398.56]  Yeah.
[1398.66 --> 1402.36]  I mean, it's a weird world that I don't know anymore.
[1402.36 --> 1407.34]  Like I code less and less, but I now can code again.
[1407.68 --> 1414.72]  Like because, for example, we have a data scientist in the team and he says, I don't feel like I'm a coder anymore.
[1414.86 --> 1421.06]  I'm just a manager of, you know, a user of this LLM that I validate the output.
[1421.28 --> 1422.22]  And yeah, it's OK.
[1422.32 --> 1427.00]  And it's a bit ridiculous, he says, because even simple things like copy-paste, I will not bother.
[1427.10 --> 1429.38]  I'll just say, OK, can you refactor this?
[1429.38 --> 1431.56]  It definitely has changed.
[1432.26 --> 1435.58]  And OK, there may be implications about creativity of people.
[1436.08 --> 1449.38]  And if you go into the AI, LLM space, like, for example, for images, when those models generate images, somebody, a painter may say to you, hey, you may lose creativity because you generate always the same thing.
[1450.04 --> 1451.66]  I don't have answers for those things.
[1451.72 --> 1453.74]  And I don't think a lot of people have answers.
[1453.90 --> 1455.18]  We'll just see, right?
[1455.24 --> 1456.76]  Like how things go sincerely.
[1456.76 --> 1460.46]  But yeah, it's interesting, right?
[1461.48 --> 1467.64]  Yeah, this idea of being a manager of your assistants, I think, is really helpful.
[1467.80 --> 1481.12]  I forget who it was we had on the show, Chris, but they were saying, hey, if you think about this thing just like a high school intern or something, you know, like is a high school intern going to solve all of your problems?
[1481.12 --> 1481.60]  No.
[1481.60 --> 1481.68]  No.
[1482.14 --> 1491.54]  But if they work all day on your problem or, you know, let's say you have infinite number of those high school interns that just can do work all the time.
[1491.66 --> 1492.60]  Is that useful?
[1492.78 --> 1493.16]  Certainly.
[1493.40 --> 1495.90]  There's a management aspect to that, right?
[1495.90 --> 1501.22]  Probably more so with high school interns than with LLMs.
[1501.32 --> 1501.82]  I'm not sure.
[1502.42 --> 1504.96]  But yeah, I love that metaphor.
[1505.18 --> 1506.00]  That's really good.
[1506.00 --> 1508.62]  I'm also wondering.
[1509.00 --> 1516.14]  So this particular application of AI within someone's code base, right?
[1516.14 --> 1527.64]  I think similar to what we've seen in other cases with Copilot and some of the things that have happened there, it's a very sensitive area, particularly for like enterprise business users.
[1527.64 --> 1539.32]  I think if you're like an indie hacker and like you say, you are wanting to create a TypeScript UI and you don't know TypeScript, like boom, you can get, you know, some really cool results really quickly.
[1539.52 --> 1543.82]  Of course, enterprise code is part of the IP of a company.
[1543.82 --> 1556.64]  There's, you know, two aspects of that, one of which is the fact that companies have been hesitant or even sued others over usage of their code or data in ways that they didn't expect.
[1556.64 --> 1572.72]  I think, though, the other aspect of this that you alluded to is it really is powerful when you start to bring your own data to the table, especially with these open models, both because they have kind of privacy conserving deployments.
[1572.72 --> 1578.72]  And there's also like code preference things and other things that your company might have.
[1578.72 --> 1586.90]  So I'm wondering if you could speak to that a little bit and how you envision you're helping build a product that's doing code optimizations for people.
[1587.04 --> 1600.48]  So how do you think about, you know, people creating customized models for their code bases and the sort of proliferation of these customer specific models and the hosting of those?
[1600.66 --> 1603.30]  What goes through your mind when you're thinking about those things?
[1603.30 --> 1606.48]  That's a very, very important topic.
[1606.74 --> 1608.66]  And we have quite a lot of experience with this.
[1608.94 --> 1616.32]  And I will mention an example where we wanted to, we went to a client, very big technology firm, super big, one of the best.
[1616.36 --> 1618.42]  And we said, hey, you know, this is our platform.
[1618.54 --> 1619.46]  We have these LLMs.
[1619.54 --> 1626.96]  You can use any LLM of your choice, like GPT-4 or open source LLMs like LAMA 2, et cetera.
[1626.96 --> 1633.34]  In the beginning, they said we don't have any approval for OpenAI because, first, they don't know the IP issue.
[1633.82 --> 1637.26]  Second, they don't want the code to go outside.
[1637.52 --> 1641.10]  We're talking about proprietary code at a lot of such companies.
[1641.78 --> 1648.46]  So the solution there was, okay, you can use the custom open source LLM on your data.
[1648.56 --> 1649.54]  We do not see anything.
[1649.54 --> 1651.72]  So it's a custom solution on premise.
[1652.34 --> 1659.60]  And while they're using a product, then practically our platform allows them to generate their own training data set.
[1659.76 --> 1661.68]  So, for example, they use Artemis.
[1661.82 --> 1663.36]  They optimize code.
[1663.46 --> 1665.18]  They see sometimes the code is optimized.
[1665.42 --> 1666.00]  It's not optimized.
[1666.60 --> 1668.28]  But they generate the data.
[1668.58 --> 1670.10]  And those data we cannot see.
[1670.40 --> 1675.50]  And the client should have those data for fine-tuning their own model.
[1675.50 --> 1679.46]  Then, through the platform, they can further fine-tune their own model.
[1679.84 --> 1687.98]  That is how the industry will go, especially in financial sectors and technology sector or defense companies.
[1688.14 --> 1691.68]  They will never give their code outside on an open source level.
[1692.24 --> 1694.44]  But LLMs are super powerful on that.
[1694.56 --> 1698.94]  Like with one client that they said, I'm not sure if I can get a recommendation.
[1699.60 --> 1706.14]  If you give me a recommendation from an LLM, who is liable if that code doesn't work?
[1706.32 --> 1707.38]  What is the IP issue?
[1707.76 --> 1709.24]  I said, how do you solve it now?
[1709.24 --> 1711.14]  They have the IP checkers, et cetera.
[1711.24 --> 1714.32]  I said, you can just use the IP checker for this moment.
[1715.12 --> 1717.82]  The same code, the same process that you would do.
[1718.68 --> 1724.88]  But also, LLMs, and we have added this functionality, can do very good similarity search.
[1724.88 --> 1736.68]  So, if you have other code bases and similar functions in your code base, you can fine-tune nicely, or you can look like the same way people are building chatbots on your documents.
[1736.68 --> 1739.58]  You can build your own chatbot on your code.
[1739.58 --> 1741.70]  So, it's practically similarity search.
[1741.70 --> 1747.98]  And then we could recommend that we even identify that three teams have implemented the same functionality a bit different.
[1748.20 --> 1750.36]  So, you even save time.
[1750.36 --> 1759.48]  So, still, this technology, the underneath technology, if you know how to use it properly, you can take advantage of it.
[1759.48 --> 1789.48] 
[1789.48 --> 1791.62]  Next question is, I guess, sort of selfish.
[1791.62 --> 1801.28]  And I like to ask this of people that have, you know, really built impressive things with this kind of new reasoning layer of LLMs.
[1801.28 --> 1815.02]  I'm wondering, as you look back on building this product for code optimization with LLMs, are there any challenges that were unexpected that you had to overcome?
[1815.88 --> 1826.14]  And are there any sort of takeaways that you would give to practitioners that are maybe working on their own products or integrations with LLMs?
[1826.14 --> 1834.88]  Like, what has been important for you to stress, especially as a CTO and bringing new people into the team, as you're working with these types of models?
[1835.18 --> 1839.88]  What's important in your mind and, you know, any of those challenges that had come up?
[1840.04 --> 1841.30]  Anything you'd like to highlight?
[1841.74 --> 1847.14]  If you're building applications and your application depends on an LLM output, right?
[1847.14 --> 1863.14]  Then you need to make sure that as a first stage, I would recommend you use something like a closed source API usage because it will solve you the headache of deploying your own LLM, having good GPUs.
[1863.76 --> 1866.04]  That is a problem that you cannot scale, right?
[1866.14 --> 1869.50]  At this moment, most teams don't know how to do it.
[1869.50 --> 1877.82]  And, of course, there are a lot of startups, a lot of companies that are working on this, on how to build your own LLM in a scalable way.
[1877.92 --> 1880.66]  But that can be a nightmare to build.
[1880.82 --> 1889.24]  So if your business is not how to deploy an LLM and the value somewhere else, if somebody provides it as a service, it makes sense to use it.
[1889.24 --> 1897.72]  So in our site, we say you can import with an API key and a secret key your NLLM that you have access.
[1897.88 --> 1900.32]  Then your application becomes much easier.
[1900.82 --> 1909.12]  But then you have the problem that you need to solve of is the client okay if those data are used on OpenAI or because there is the data that goes there.
[1909.30 --> 1914.32]  This in financial sector or currently cannot be accepted.
[1914.32 --> 1919.86]  Then our product will have to deploy LLM2, have to deploy it.
[1919.90 --> 1923.02]  So then you have to build it yourself for use of service.
[1923.14 --> 1926.56]  So we had to build it because we were one of the early adopters.
[1927.14 --> 1927.92]  But there are tools.
[1928.06 --> 1930.98]  Like Hugging Face provides a very nice API for you to deploy.
[1931.16 --> 1932.40]  Now they changed the license, I think.
[1932.48 --> 1934.58]  But, you know, I think majority of people can use it.
[1935.18 --> 1939.76]  So the speed of LLMs is a big problem for scaling application, definitely.
[1939.76 --> 1947.82]  Then other issues about LLMs, which were a bit in the beginning, now they're trying to be fixed, is token size.
[1948.34 --> 1951.84]  Every time you ask and the result may be incomplete.
[1953.18 --> 1960.00]  If there is, then how do you deal with the previous context and all this kind of, you need to spend time on this to do it properly.
[1960.00 --> 1968.42]  I am expecting more and more tools and open source are solving, like LankChain or those tools also open source are doing some of the things.
[1968.96 --> 1973.70]  And, of course, the biggest problem that a lot of people talk is about hallucination of the models.
[1973.82 --> 1975.78]  You cannot trust necessarily the models.
[1976.02 --> 1982.02]  And you cannot just say generate code and execute that code in your backend because somebody may do SQL injection.
[1982.28 --> 1988.94]  Like similar to where people were doing SQL injection in the past, especially for coding, you can have LLM kind of injection.
[1988.94 --> 1996.98]  So you need to be very careful on exposing the problem to the end user because somebody can really damage.
[1997.58 --> 1998.90]  So, yeah, those are them.
[1999.50 --> 2005.94]  When you're thinking about, you know, hallucinations from LLMs and you're, but you're working on a problem like optimization and stuff.
[2005.94 --> 2009.38]  And you acknowledged earlier, you know, some of the problems you face is one of them.
[2009.48 --> 2014.14]  You may not get, you know, the right code or compilable code because it's the output of an LLM.
[2014.14 --> 2016.32]  How do you approach that specific problem?
[2016.48 --> 2020.38]  I was actually wondering that earlier and the conversation continued on without it.
[2020.46 --> 2021.96]  But we kind of circle back around.
[2022.06 --> 2029.82]  Like, how do you think about dealing with hallucination when you're dealing with optimization and correctness, you know, and improving in that way?
[2030.00 --> 2031.08]  How balancing the two?
[2031.58 --> 2032.12]  Very good question.
[2032.26 --> 2036.22]  So it depends on the programming language and the existing tools that you can also use.
[2036.22 --> 2045.92]  So if you go for programming language like Haskell and functional programming, in theory, you can have a bit more proofs about code before and code after.
[2046.62 --> 2047.18]  Works the same.
[2047.30 --> 2049.42]  NASA, for example, would want this proof.
[2049.58 --> 2050.88]  You cannot have code.
[2051.28 --> 2056.80]  Second, the mechanism is ideally would like applications to have unit tests and test all the scenarios.
[2056.92 --> 2058.72]  So when you do change, ideally.
[2058.86 --> 2060.80]  But not all code bases have, right?
[2060.80 --> 2064.40]  You mean not all code bases are fully covered with tests?
[2064.40 --> 2064.82]  I hope.
[2067.40 --> 2067.92]  Yeah.
[2069.22 --> 2073.38]  Unfortunately, like, there are open source projects that the unit tests don't even pass.
[2073.96 --> 2079.54]  And they are, like, we take a code base, we save by test or whatever, they don't pass by default.
[2079.70 --> 2081.86]  So it's still, this needs to improve.
[2081.96 --> 2083.34]  Hopefully, LLMs can improve that.
[2083.34 --> 2090.68]  The third mechanism is we aim for minimum code changes with the biggest optimization.
[2091.64 --> 2092.80]  And we go gradually.
[2093.02 --> 2100.40]  Like, for example, we try to say first target data structure optimization that is one, two lines that you can check.
[2100.78 --> 2103.82]  Then go on one single for loops, double for loops.
[2104.24 --> 2105.82]  You go a bit gradually on that.
[2105.82 --> 2110.30]  And we currently make a pull request with the recommended changes.
[2110.48 --> 2114.20]  So we still want the developer to validate those changes.
[2115.02 --> 2117.56]  Because, you know, you cannot take that risk.
[2117.82 --> 2127.60]  And also, from a psychology perspective, if you have a tool there that you consider this is my performance expert and tells you at the end, hey, make those three changes that you can verify.
[2127.60 --> 2127.64]  Right.
[2128.12 --> 2137.24]  It's not different from if we change the name of the tool and put the developer name and make a pull request, that person will not know where this pull request came from.
[2137.30 --> 2137.48]  Right.
[2137.48 --> 2140.10]  So you follow the same process.
[2140.42 --> 2141.28]  That's how we see it.
[2141.28 --> 2166.22]  Something that I'm kind of getting in what you're saying as well, which I know is often a misconception that I run into when I'm either doing workshops or working hands on with people with generative models, is there's typically this misconception that you need to package everything into a single prompt and then output your final result.
[2166.30 --> 2167.88]  It's a sort of one step thing.
[2167.88 --> 2182.12]  I'm getting the sense that, you know, your workflow, for one, it probably involves, you know, multiple calls throughout the code base because of the context size, I would assume is partly because of that.
[2182.48 --> 2191.56]  But then also you mentioned this kind of iterative element where, hey, there's kind of big rocks that you can move that are the sort of worst offending areas.
[2191.56 --> 2194.46]  So there's hierarchy in that respect.
[2194.62 --> 2214.84]  But also it seems like let's just assume I know it's not a good assumption, but if we assume that a person's code base is fully tested, integration tests, unit tests, it seems like this is something you could just loop over and over and over and over again to to get increasing optimizations, probably with diminishing return.
[2214.84 --> 2222.54]  Could you speak a little bit to how you as a team think about that chaining element, I guess would be the way to say it?
[2222.76 --> 2225.36]  And then also maybe iterative element.
[2225.36 --> 2231.56]  First of all, the way we have presented this, like, let's say you take the original version of a code.
[2232.04 --> 2233.18]  There are two approaches there.
[2233.32 --> 2240.08]  It's one, I apply one LLM and take the first three, four suggestions of this LLM, right?
[2240.60 --> 2242.56]  And then apply which one works.
[2242.56 --> 2255.78]  Like, even on the papers on how good they are on the code base, they will say the first top five recommendations from the LLM, three out of five outperformed, something like this.
[2255.82 --> 2259.14]  So it's not a one chance applied LLM, et cetera.
[2259.68 --> 2266.46]  Now, the best approach from what we have seen is you get the first version, you apply the first version.
[2266.46 --> 2273.50]  And if you have the ability to get feedback from what you applied, that is where those LLMs are very, very good.
[2273.58 --> 2275.76]  So, for example, you say optimize this code.
[2276.06 --> 2282.62]  You try to pass the unit tests or you try to compile your code and you get the compilation error message.
[2282.98 --> 2290.16]  Then you go back automatically to the LLM and say the recommendation you gave me didn't pass because of this error.
[2290.32 --> 2292.52]  And then they can give you better.
[2292.52 --> 2298.74]  It's like the Wolverine technique or I think somebody did a demo where they were showing how you can compile and learn.
[2299.50 --> 2306.94]  And because this is also if you think how you are using those LLMs, let's say write my email, they recommend, they say, sorry, this is too official.
[2307.10 --> 2308.26]  I want it a bit more friendly.
[2308.76 --> 2312.52]  This is, I believe, currently the best approach.
[2313.44 --> 2315.52]  So it's like iterative approach.
[2316.52 --> 2320.64]  If you have a way to measure and give the feedback back, you can have the best result.
[2320.64 --> 2323.82]  Like if we take the logs and give it to the LLM, we'll have even better.
[2324.06 --> 2326.14]  But even if you say, hey, sorry, this is not good.
[2326.20 --> 2327.00]  Give me something better.
[2327.18 --> 2330.38]  It will, again, try to improve in the context.
[2331.22 --> 2341.52]  You can even do things like, again, I think, you know, I was in a presentation that Langchain and a similar one, where you can combine two, three versions of different LLMs.
[2341.70 --> 2345.16]  And then the three base, you can have three and then combine them.
[2345.20 --> 2346.54]  Say, take context from here.
[2346.62 --> 2347.50]  This work didn't work.
[2347.54 --> 2349.00]  So there are different approaches.
[2349.00 --> 2351.38]  You just stole my question right out of my mouth.
[2351.48 --> 2354.84]  I was going to ask when you extended that to multiple LLMs and integrated.
[2354.92 --> 2362.50]  I was kind of wondering how you were thinking about that because you were addressing like when one LLM gave you multiple points back in terms of optimization.
[2362.50 --> 2369.76]  And you're trying those out and kind of how you might extend that to multiple LLMs because we're getting in this world with an increasing number.
[2369.88 --> 2372.42]  We're going to just be awash in LLMs before long.
[2372.76 --> 2378.52]  And as you have so many APIs or so many deployments available to you, how does that change?
[2378.52 --> 2381.40]  You know, it sounds like your workflow would work for that regardless.
[2381.70 --> 2387.66]  But, you know, does that add value or do you think there's diminishing returns as you keep adding LLMs into it?
[2388.16 --> 2389.48]  No, I think there is a value.
[2389.48 --> 2394.72]  And also it gives a flexibility to the user to always not be locked to a single LLM.
[2394.72 --> 2397.64]  Like if you, for example, it may be different user.
[2397.74 --> 2398.94]  It may be pricing issue.
[2399.10 --> 2404.06]  It may be a new model this week can have bigger token size.
[2404.20 --> 2405.78]  It may be the performance of this.
[2405.86 --> 2409.30]  So you cannot rely on one single LLM.
[2409.42 --> 2417.68]  Nowadays, because it's so easy to build LLMs if you have the data, our business doesn't depend on, hey, we have the best LLM.
[2417.68 --> 2426.06]  And somebody else suddenly in a week can give you a better LLM and then you are out of business because you need to spend 100 million to train on CPUs.
[2426.06 --> 2435.74]  So in our case, combining LLMs, using LLMs and having that workflow, LLM agnostic, it's a way that you can utilize.
[2436.02 --> 2440.36]  Now, if people pay for better LLMs and access, then the result is better.
[2440.54 --> 2444.72]  Here, though, we have to mention one issue, which a lot of people may not know.
[2444.72 --> 2449.94]  Now, it is a bit tricky when you use output from one LLM or the other LLM.
[2450.08 --> 2452.30]  So there are IP issues, et cetera.
[2452.40 --> 2454.78]  So you cannot, we are also investigating exactly.
[2454.78 --> 2454.96]  That's a good point.
[2455.22 --> 2462.24]  Yeah, but you cannot use, in theory, chat GPT output to fine-tune LAMA in a commercial setting.
[2462.46 --> 2471.26]  Maybe, you know, the alpaca paper, I think the first one showed that you can say to chat GPT, give me examples, then fine-tune another model and then have it.
[2471.34 --> 2474.18]  But you are not allowed on a commercial side.
[2474.18 --> 2479.02]  But I'm sure there may be two open source LLMs eventually that you will use.
[2479.34 --> 2484.26]  As far as you have the framework, then we allow those things to happen.
[2484.26 --> 2499.28]  As we kind of near the end of our conversation here, I'm wondering if you can paint a bit of a picture for us from your perspective as someone working day-to-day in developer tools that are AI-driven.
[2499.28 --> 2507.82]  What are some of the most exciting things that keep you up at night as you look forward to sort of the next year?
[2508.44 --> 2514.08]  It could be things you're working on, but it might just be generally how this field is developing.
[2514.36 --> 2520.64]  What's really exciting for you as a person building these sorts of tools as you look to the next year or so?
[2520.64 --> 2527.36]  I personally believe that this is the start of the power of this technology.
[2527.60 --> 2531.18]  We already see how much it has changed the way people are coding.
[2531.18 --> 2542.74]  What I want to see, and I see more and more things make it like people nowadays want to use like talk speech to text and then code, these kind of things.
[2542.74 --> 2547.62]  Like they're trying to make developers even lazier, you know, these kind of things.
[2548.16 --> 2562.14]  So from my perspective, from what we are trying to do, I want us to, we are in the process of looking open source project, going through our platform, and they really get great optimization that we can give to the community.
[2562.14 --> 2576.46]  So for example, if I can get a very slow machine learning library, 30%, 40% all automatically, make a pull request, show to the people how easily we can optimize the speed and everybody can benefit from that.
[2576.98 --> 2590.64]  And it excites me to know that we still haven't found out what are the limitations of the current technology and how much inefficient code is outside there.
[2590.64 --> 2594.94]  And I'm excited to find out how much we can improve in an automatic way.
[2595.90 --> 2604.40]  Like, I don't know, Redis, these kind of things that everybody's using in their own day because they can make our, you know, laptop faster.
[2604.62 --> 2609.28]  Like already my fun is going crazy.
[2609.54 --> 2617.70]  And yeah, that's what this combination of LLMs and coding is something very, very exciting because we don't know the limitations of this.
[2617.78 --> 2620.02]  That's what I want to find out.
[2620.02 --> 2620.84]  That's awesome.
[2621.04 --> 2629.26]  Well, we will certainly be on the edge of our seat as you're exploring those limitations and those possibilities.
[2629.66 --> 2631.44]  Really appreciate you joining us, Mike.
[2631.48 --> 2632.90]  It's been a great conversation.
[2633.52 --> 2640.50]  And I'm very much looking forward to my code running faster despite my ignorance of how to make it do that.
[2640.84 --> 2642.14]  So thank you so much.
[2642.22 --> 2643.60]  And we'll talk to you soon.
[2643.70 --> 2644.14]  Thanks a lot.
[2644.36 --> 2644.66]  Thank you.
[2644.72 --> 2645.22]  Thank you, guys.
[2645.22 --> 2645.28]  Thank you.
[2645.28 --> 2645.34]  Thank you, guys.
[2645.34 --> 2645.44]  Thank you.
[2645.44 --> 2645.78]  Thank you.
[2645.78 --> 2647.28]  Thank you, guys.
[2647.28 --> 2647.34]  Thank you.
[2647.34 --> 2647.84]  Thank you.
[2647.84 --> 2649.22]  Thank you, guys.
[2649.22 --> 2649.34]  Thank you.
[2649.34 --> 2649.72]  Thank you.
[2649.72 --> 2656.16]  Thank you for listening to Practical AI.
[2656.70 --> 2660.50]  Your next step is to subscribe now if you haven't already.
[2660.94 --> 2666.96]  And if you're a longtime listener of the show, help us reach more people by sharing Practical AI with your friends and colleagues.
[2666.96 --> 2672.34]  Thanks once again to Fastly and Fly for partnering with us to bring you all Change Talk podcasts.
[2672.92 --> 2676.74]  Check out what they're up to at Fastly.com and Fly.io.
[2677.12 --> 2682.44]  And to our Beat Freakin' Residence Breakmaster Cylinder for continuously cranking out the best beats in the biz.
[2682.72 --> 2683.62]  That's all for now.
[2683.74 --> 2685.24]  We'll talk to you again next time.
[2685.92 --> 2686.60]  We'll talk to you again next time.
[2686.60 --> 2691.24]  We'll talk to you again next time.
[2691.24 --> 2692.28]  We'll talk to you again next time.
[2692.28 --> 2696.30]  We'll talk to you again next time.
[2696.30 --> 2697.38]  Okay.
[2697.38 --> 2697.68]  Bye.
[2697.68 --> 2698.18]  Bye.
[2698.20 --> 2698.28]  Bye.
[2698.28 --> 2698.90]  Bye.
[2698.90 --> 2699.92]  Bye.
[2700.00 --> 2700.54]  Bye.
[2700.54 --> 2701.34]  Bye.
[2701.34 --> 2703.36]  Bye.
[2707.40 --> 2711.70]  Bye.
[2711.70 --> 2712.62]  Bye.
[2712.62 --> 2713.38]  Bye.
