[0.00 --> 6.70]  Bandwidth for Changelog is provided by Fastly. Learn more at Fastly.com. We move fast and fix
[6.70 --> 11.42]  things here at Changelog because of Rollbar. Check them out at Rollbar.com and we're hosted
[11.42 --> 17.36]  on Linode servers. Head to linode.com slash changelog. This episode is brought to you by
[17.36 --> 23.72]  DigitalOcean. They now have CPU optimized droplets with dedicated hyper threads from best in class
[23.72 --> 29.18]  Intel CPUs for all your machine learning and batch processing needs. You can easily spin up
[29.18 --> 34.74]  their one-click machine learning and AI application image. This gives you immediate access to Python 3,
[35.20 --> 42.68]  R, Jupyter Notebook, TensorFlow, Scikit, and PyTorch. Use our special link to get a $100 credit for
[42.68 --> 51.30]  DigitalOcean and try it today for free. Head to do.co slash changelog. Once again, do.co slash changelog.
[59.18 --> 68.60]  Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[69.02 --> 74.52]  productive, and accessible to everyone. This is where conversations around AI, machine learning,
[74.56 --> 78.66]  and data science happen. Join the community and snag with us around various topics of the show
[78.66 --> 84.48]  at changelog.com slash community. Follow us on Twitter. We're at Practical AI FM. And now onto the show.
[89.18 --> 95.10]  Welcome to another Practical AI. Chris, I know that you've had a number of jobs throughout your
[95.10 --> 101.94]  career. Was the hiring process always super smooth for you? Anything but. I've been hired more than a
[101.94 --> 107.92]  few times and I've hired lots of people over the years. And no, for me at least, way, way more art
[107.92 --> 113.96]  than science. So I'm looking forward to maybe learning something here. Yeah, we've got Lindsay
[113.96 --> 118.32]  Zulaga with us. Welcome, Lindsay. Hi, nice to be here. Yeah, did I get the name right?
[118.32 --> 123.16]  Yeah, you did good. Okay, perfect. Well, I'm excited to have you on the show today. I know
[123.16 --> 128.72]  me as well, kind of with Chris. I've had some awkward experiences in the hiring process. I've
[128.72 --> 133.92]  done well at interviewing. I've crashed in the interviewing process. I've done well and bad
[133.92 --> 139.54]  at assessments and coding things. And we're just excited to have you because we're going to be
[139.54 --> 146.82]  talking today about your work with AI and hiring and also bias in AI. So super great to have you here.
[146.82 --> 151.64]  It'd be great if we could just hear a little bit about your background. I know you started out in
[151.64 --> 155.70]  academia and then eventually moved into industry. So give us a little bit of your story.
[156.10 --> 163.16]  Sure. I studied physics. So I did my undergrad here in Utah, the University of Utah. And then I
[163.16 --> 169.94]  did a master's and PhD at Rice University in Houston, Texas, and a postdoc in Germany as well. So
[169.94 --> 175.92]  during that time, I was in the field of nanophotonics. I was studying and doing experiments
[175.92 --> 183.40]  on how nanoparticles interact with light. So building laser setups and kind of a pretty different
[183.40 --> 189.78]  world than what I'm in now. When I went into graduate school, I really wanted to work with
[189.78 --> 194.82]  my hands. I thought I didn't want to sit at a computer all day. But to my surprise, what I actually
[194.82 --> 200.66]  enjoyed the most about my work was writing code to analyze data. So when I did transition into
[200.66 --> 206.00]  industry, data science ended up being a really good fit, kind of relies on a lot of those similar
[206.00 --> 211.88]  problem solving skills that I learned. Obviously, having a strong math background was useful and,
[211.94 --> 217.80]  you know, analyzing data, writing code to analyze data. So it was kind of a good fit,
[217.94 --> 222.98]  right place at the right time. My transition, and you guys talked about job interviewing,
[222.98 --> 228.28]  I'll say I've written a blog post about this, but my transition from academia to industry
[228.28 --> 234.76]  was a lot more difficult than I expected. I was doing well in academia. So I kind of thought
[234.76 --> 241.14]  it'd be easy for me to transition into industry and really kind of was naive about the importance
[241.14 --> 247.66]  of connections. You know, I had a CV, not a resume, but a CV with publications on it and
[247.66 --> 252.88]  things that people in industry don't really care about. So I came into the whole industry,
[252.98 --> 259.16]  job world, a little naive and ended up applying for a lot of jobs online and going through this
[259.16 --> 264.16]  process. And many people have probably been through it where you apply for a job through what's called
[264.16 --> 270.76]  an applicant tracking system and an ATS, and you enter all your information and you upload your
[270.76 --> 276.36]  resume and then you have to reenter all the information in. And then all your information
[276.36 --> 280.90]  kind of gets parsed into plain text. And you finally submit, you know, and you've,
[280.90 --> 286.24]  you've spent all this time kind of trying to personalize your cover letter and you submit
[286.24 --> 290.04]  and you just never hear anything again. So it's kind of this black hole.
[290.66 --> 295.26]  I hate those systems, whether I'm an applicant or a hiring manager, either way, they're terrible.
[295.76 --> 301.10]  Yeah. I hate how you format your resume perfectly and you get it all flashy looking. And then
[301.10 --> 305.74]  you go through the system and then you realize that you just have to like put it in as plain text
[305.74 --> 311.94]  or something. And all of that work is for not. Exactly. And there's a lot of gaming in the system,
[311.94 --> 315.58]  which I didn't know when, and maybe I would have benefited from knowing this at the time,
[315.58 --> 320.58]  but there's actually like, there's a website. I can't remember what it's called, but you can go
[320.58 --> 325.02]  and see you put in a job posting and then you put in your cover letter or your resume and it will
[325.02 --> 331.44]  tell you the likelihood of getting past these ATS filters. And it's really just a lot of times,
[331.44 --> 337.98]  it's just like a keyword match. And I always felt like that was a little weird to just like put the
[337.98 --> 344.20]  exact keywords that are in the job posting in my, in my application. But it turns out that does help
[344.20 --> 348.46]  you get past these filters. A lot of times these filters are pretty simple. They're looking for
[348.46 --> 354.26]  certain keywords or they're looking for certain school you went to or GPA, which is silly because
[354.26 --> 360.32]  we found a lot of times that doesn't really tie to job performance very strongly at all. But the
[360.32 --> 365.16]  bottom line is, you know, companies just have so many applicants. They need some way of filtering
[365.16 --> 370.90]  through people. And I went away from the experience feeling like something's wrong with this system
[370.90 --> 376.70]  when me and so many people that I know that had PhDs and once they got a job, they did really well.
[377.08 --> 382.26]  They were just passed up by so many companies. The companies are losing out as well. That story is
[382.26 --> 388.38]  kind of my motivation of, of why I care about hiring and kind of fixing this broken system.
[388.38 --> 391.78]  Now you're director of data science at HireVue. Is that correct?
[392.00 --> 392.26]  Yes.
[392.58 --> 397.58]  Yeah. And what does HireVue do? Is it one of these systems or what do you work on and what
[397.58 --> 398.38]  does the company do?
[398.64 --> 402.64]  No. Yeah. We're not an applicant tracking system, although we do a lot of times have to work
[402.64 --> 409.74]  with them, integrate into them. We are a video interviewing company. So our philosophy is that
[409.74 --> 416.14]  a resume and a cover letter are not a very good representation of a person. So, you know,
[416.14 --> 421.94]  we started years ago with a video interviewing platform and our most popular product is called
[421.94 --> 429.30]  an on-demand interview, which is asynchronous. Our customers are companies that create interviews.
[429.76 --> 435.64]  They can have any different types of questions. They can have professional football player ask
[435.64 --> 440.10]  the question. They can do all sorts of interesting things, but they can send the same interview out to
[440.10 --> 444.72]  many different people and the people record themselves answering questions on their own time.
[444.72 --> 449.54]  And then the companies can review those interviews on their own time. So that's a very popular
[449.54 --> 455.26]  product. And that was, you know, kind of our main product for a long time because it kind of replaces
[455.26 --> 462.56]  this resume phone screening, like initial stage of the funnel, because we've all experienced, you know,
[462.64 --> 466.94]  looking at resumes and they all look the same and it's really hard to differentiate people.
[467.12 --> 471.34]  But once you hear them talk about what they're interested in and how they communicate,
[471.34 --> 475.50]  you can get a better feel for who they are. So we had a lot of success with that product,
[475.62 --> 481.06]  but we still had this issue of volume. Like I said before, like companies are just getting so many
[481.06 --> 486.98]  applicants that it's impossible for them to actually look at all of them. And the way it ends up going
[486.98 --> 493.94]  today is that a lot of people are just randomly ignored. So we started building our AI product a few
[493.94 --> 500.62]  years back where we said, we have all this, this rich data from job interviews. And if our customers
[500.62 --> 506.74]  can tell us who ended up being good at a job and who was bad at a job and that what that is,
[506.74 --> 511.66]  depends totally on the job. So we have some performance metrics around, you know, this person
[511.66 --> 516.94]  was a really good salesperson. They sold a lot and this person wasn't. Can we train algorithms to
[516.94 --> 524.70]  notice patterns between, you know, people who are top performers in a job and others? So that is the
[524.70 --> 530.56]  assessments product that I work on. So would it be fair to say that you're kind of focusing on using
[530.56 --> 536.92]  machine learning to take the bias out of the process of hiring? And if so, how does that work?
[536.98 --> 539.94]  How does that manifest itself? How do you train to get rid of that?
[540.48 --> 545.16]  Yeah. So it is a common question that we get pretty immediately when people hear about what they do,
[545.16 --> 550.10]  what we do is a little bit of like, oh, this is creepy. And how, how do you know what the
[550.10 --> 555.14]  algorithm's doing? How do you know it's not bias? So, you know, algorithms are really good at
[555.14 --> 562.16]  stereotyping and that can be an issue anywhere where AI is used. If there's any bias in the training data
[562.16 --> 568.82]  or just even under representation in the training data of certain groups, the algorithm could mirror
[568.82 --> 570.14]  that bias.
[570.14 --> 576.04]  So do you mean kind of like if there's only a representation of certain type of candidates,
[576.22 --> 581.58]  let's say, then your algorithm might behave differently when it's trained on that data,
[581.72 --> 586.70]  according to when it sees those candidates versus, you know, candidates that weren't in the,
[586.78 --> 590.96]  in the pool and the training pool is, is that kind of a fair statement?
[591.38 --> 596.08]  Sure. And I think an even bigger issue is if there's a small number of like,
[596.08 --> 602.48]  say there's only one female software engineer and she wasn't very good. Then the algorithm takes that
[602.48 --> 609.32]  and says, oh, every time I've seen someone act like this or talk like this, they were bad. So if
[609.32 --> 615.06]  there's no one, the algorithm doesn't learn as strong of patterns, although it could, and it's
[615.06 --> 620.16]  something you want to look out for. But, um, a lot of times, uh, under representation or just
[620.16 --> 626.56]  explicit, you know, bias, like in the data, which, which we do sometimes see. And depending on how
[626.56 --> 632.34]  subjective that performance metric is, that can be strong. And depending on the country as well,
[632.34 --> 637.82]  we've seen it, um, vary and kind of like, like manager ratings and things that are subjective
[637.82 --> 642.92]  like that. So we definitely prefer objective metrics like sales numbers, call handle time,
[642.92 --> 646.06]  you know, kind of productivity measures, things like that.
[646.06 --> 652.40]  I'm curious, have you had more of a challenge on this front in certain industries? I'm not sure
[652.40 --> 656.10]  which industries, you know, higher view is, is working with. You mentioned sales a little bit,
[656.14 --> 661.04]  maybe software engineering. Do you have to kind of approach this as far as your models go
[661.04 --> 666.48]  differently in different industries, or is this something that's kind of a problem across the board?
[667.08 --> 672.84]  Yeah, I would say it's probably more on a company level, um, or a cultural level that we,
[672.84 --> 681.04]  we notice differences. So a lot of what is important in trying to level a playing field is,
[681.18 --> 686.86]  is, um, you know, these interviews ask people very consistent questions. And that's something
[686.86 --> 691.54]  that's, that's been done in hiring over the past several decades, because, you know, hiring is
[691.54 --> 697.72]  very much about gut feelings. So we've improved it by trying to treat all candidates in a consistent
[697.72 --> 703.36]  way, but it's pretty much impossible for humans to actually do that. Humans have this implicit bias
[703.36 --> 710.62]  that we don't even know we have. So there's also a big culture recently of like this concept of
[710.62 --> 717.12]  cultural fit, which is very popular. And companies say they want to hire someone who they like, and
[717.12 --> 721.82]  that can communicate well with them and work well with their teams. But this often results in like a
[721.82 --> 726.80]  similarity bias where I don't know why I just like that person. Well, you like them because they're a lot
[726.80 --> 732.44]  like you, or they are a lot like your team already. So you get this homogeneity in your team.
[733.20 --> 739.06]  So to some degree, would it be fair to say that when, when a company is looking for cultural fit,
[739.10 --> 743.66]  are they almost acknowledging their bias and saying, we're going to, we're going to accept that as part
[743.66 --> 745.66]  of the process or, or am I misreading that?
[746.18 --> 750.66]  Um, I mean, I think some people have made that argument. There's, you know, there's articles written
[750.66 --> 755.90]  about the issues with cultural fit, which is just, are you just opening the door for bias?
[755.90 --> 760.48]  I wouldn't go that far to necessarily say that that's exactly what's going on. I mean,
[760.48 --> 767.68]  I do understand the concept, but it is, it is very tricky and, and, you know, humans are probably
[767.68 --> 772.08]  going to be a part of the hiring process for a long time. So it's something that we need to try to deal
[772.08 --> 772.48]  with.
[773.40 --> 779.18]  So I'm kind of thinking in my mind, um, right now in terms of like, okay, we know that humans are biased
[779.18 --> 785.28]  in terms of these ways that we've mentioned. We know that we can kind of subtly introduce bias into
[785.28 --> 791.10]  our machine learning and AI models via, uh, representation in the dataset and other ways.
[791.44 --> 797.78]  Um, I'm just wondering as kind of human AI developers, you know, what chance do we have
[797.78 --> 803.20]  of, of kind of fighting this bias and how can we have hope to actually do something better?
[803.86 --> 810.18]  Yeah, I think a big part of it is just becoming aware. So as data scientists, I think we've,
[810.18 --> 815.20]  we spend a lot of time just trying to optimize the accuracy of our algorithms and kind of not
[815.20 --> 822.12]  thinking about bias or fairness at all. As I've studied algorithmic fairness more and more, I found
[822.12 --> 829.06]  that it's a, it's a more nuanced, tricky topic than you might assume. So if you look up, there's
[829.06 --> 834.60]  a recidivism model. This is kind of a, started a whole conversation. It's called compass. And it was
[834.60 --> 839.86]  this recidivism model in Florida where you tried to predict the chances that someone would
[839.86 --> 844.82]  re-offend after they were released from prison. When you looked at the data, actually blacks had
[844.82 --> 851.50]  a higher, uh, false positive rate. So they were marked as being at risk when they actually didn't
[851.50 --> 856.76]  re-offend in the training data at a higher rate than whites. That algorithm was trained to optimize
[856.76 --> 862.02]  accuracy, but because of different base rates in the data, this was a side effect. So this,
[862.02 --> 866.80]  this whole thing spurred a really interesting conversation around fairness and how to define it.
[866.80 --> 871.66]  And the upshot is that basically there's, there's many different notions of what makes
[871.66 --> 877.08]  an algorithm fair. And with most real world problems, it's impossible to satisfy all of them.
[877.80 --> 883.18]  So it makes things tricky for data scientists. And we actually need to consider what notions of
[883.18 --> 887.94]  fairness matter the most for our particular problem. Another example, and I think marketing
[887.94 --> 893.64]  is a really interesting space because it, it relies a lot on demographics. So an example of a situation
[893.64 --> 898.46]  to think about is if you're trying to predict who would click on a data science job posting,
[898.46 --> 904.66]  like an ad for a data science job, the algorithm could look at a bunch of browser data and say,
[904.80 --> 911.64]  users who look at female type things online are less likely to, to click on that ad and end up making
[911.64 --> 916.44]  an algorithm that doesn't show it to any females. It's a really strict notion of fairness to say,
[916.56 --> 921.74]  we need this to be shown to the same percentage of men and women. That's obviously pretty strict
[921.74 --> 926.40]  because there are more men that are interested in the ad and would click on the ad. So you,
[926.48 --> 931.80]  so you, the marketing company would lose money, but it's maybe realistic to aim for something else.
[931.80 --> 935.68]  Like we just want the same true positive rate. So out of the people that are interested,
[936.28 --> 941.84]  same percentage of men and percentage of women saw the ad, for example. So those are the kinds of
[941.84 --> 946.90]  things. And, and there's a lot more detail beneath that, but those are the kinds of different notions
[946.90 --> 951.56]  of fairness that I think you need to take into consideration when you're building an algorithm.
[952.36 --> 957.78]  So we've kind of dived right into, into doing it from the algorithm. And, and I guess I'd like to
[957.78 --> 962.98]  see if we can differentiate a little bit between what a, a traditional job assessment process looks
[962.98 --> 967.96]  like and how HireVue is approaching it algorithmically at this point. And, and what are the,
[968.06 --> 972.78]  what are the things that might be the same, uh, for companies, uh, going from one to the other?
[972.78 --> 976.08]  And what are some of the things that might change for them and how do they prepare for that?
[976.68 --> 981.16]  Sure. So yeah, a lot of people are familiar with this traditional job assessment, which is often
[981.16 --> 986.30]  like multiple choice tests and they've been around for a long time. They're, they are the result of
[986.30 --> 991.22]  trying to make the process more consistent. Some of the drawbacks are that they are, they're closed
[991.22 --> 998.72]  ended. So you have maybe multiple choice, but none of those choices describe you. And they also can be
[998.72 --> 1003.98]  kind of a bad candidate experience. So companies care a lot about that. Like they want people to
[1003.98 --> 1007.82]  come in and have a good experience, even if they didn't get the job, they don't want to damage their
[1007.82 --> 1015.38]  brand by having this awful experience. So those assessments can be long and make that, that experience
[1015.38 --> 1022.80]  negative. And they also give results like personality traits and the connection between personality traits
[1022.80 --> 1031.08]  and actual job performance is loose or it's maybe kind of made up by a person. So assuming, you know,
[1031.60 --> 1037.60]  we want a salesperson to have these exact personality traits is sometimes not validated. In our process,
[1037.60 --> 1042.32]  we actually, you know, like I said, we train straight to performance. Like I mentioned before,
[1042.32 --> 1047.28]  we try to get objective performance metrics and that could depend on the job, what that,
[1047.40 --> 1048.50]  what exactly that means.
[1048.50 --> 1053.06]  So like in the example of the salesman that you talked about, there's a stereotype that,
[1053.16 --> 1057.22]  you know, people have about what is a salesman, you know, what's that natural born salesperson,
[1057.40 --> 1061.16]  you know, look like personality wise. And that usually has a picture that, you know,
[1061.18 --> 1064.90]  is our, the stereotype in our head. Are you essentially trying to take those stereotypes
[1064.90 --> 1071.84]  out of the process by validating which of the metrics are applicable for that job versus what we
[1071.84 --> 1073.02]  can see from the data is not?
[1073.34 --> 1077.18]  Yeah, sure. And I think sometimes that does happen that humans have an assumption about
[1077.18 --> 1082.18]  what is going to make the perfect person for this job versus what is actually in the data.
[1082.58 --> 1088.02]  And so I think a lot of times those notions are overturned by looking at actual performance data.
[1088.74 --> 1092.58]  And one thing that, that I'm thinking about here is, you know, it might be like,
[1092.60 --> 1096.52]  you already mentioned the example where you only have the one example of a,
[1096.52 --> 1102.12]  of a female software engineer who, who went through and maybe performed one way or the,
[1102.12 --> 1108.18]  or, or another, is it, is it hard for you to, as you're thinking about, you know, being objective
[1108.18 --> 1114.18]  in, in these ways? Um, I imagine in some cases it might be hard for you to actually get the data
[1114.18 --> 1119.94]  that you need to, to be objective. Like maybe, you know, when you're first working with a company,
[1119.94 --> 1124.60]  you don't, you don't know the performance information of how the people that they've hired
[1124.60 --> 1129.66]  in the past have performed in this objective way. How do you go about kind of establishing that
[1129.66 --> 1134.82]  data that you need as the, as the foundation? Yeah. A lot of times that's a process. So a lot
[1134.82 --> 1143.10]  of companies don't have really strong performance metrics. And so we have a team of IO psychologists or
[1143.10 --> 1149.08]  industrial organization, industrial organizational psychologists who go in from the very beginning
[1149.08 --> 1153.80]  and help our customers kind of get set up. If they're existing customers, they might already have
[1153.80 --> 1158.98]  their, their own interview and, and their own questions. But ideally we kind of start with them
[1158.98 --> 1163.82]  from the beginning, what is important to this job? We do a whole job analysis, right? So
[1163.82 --> 1169.62]  what are, what do you want to measure? What are you looking at? And our IO psychologists have a lot
[1169.62 --> 1176.20]  of experience with knowing which questions to ask to actually tease out that information. So it's kind
[1176.20 --> 1181.12]  of interesting that there's questions like, tell me about yourself, which are good warmup questions
[1181.12 --> 1186.36]  that don't actually differentiate people very well at all. Whereas questions that are about a
[1186.36 --> 1191.00]  situation, like what would you do if this happened? You have this difficult customer and,
[1191.20 --> 1197.30]  you know, some detailed scenario, how would you act in that situation? Those, those questions tend to be
[1197.30 --> 1203.54]  better at differentiating top and bottom performers. So the hope is we go in from the beginning and kind
[1203.54 --> 1209.24]  of design the interview. We design the process of, you know, how we're going to collect performance data.
[1209.24 --> 1215.30]  As you guys know, machine learning algorithms do rely on our training data being kind of representative
[1215.30 --> 1221.48]  of who's coming in the funnel. So we want to see a distribution of people. Sometimes gathering enough
[1221.48 --> 1227.84]  data is a challenge though. So we have continuous monitoring of our algorithms. I can say a little
[1227.84 --> 1233.14]  bit more about that. After we release an algorithm, we're, we're always watching for how it scores
[1233.14 --> 1238.84]  different groups of people and making sure that it's not treating different groups of people in a
[1238.84 --> 1244.58]  statistically significantly different way. That makes sense. That, that was something, Chris, I know we,
[1244.58 --> 1249.48]  we talked about in our last news updates thing is, um, you know, Google recommending through their,
[1249.48 --> 1255.74]  their AI, uh, forget what they called it, AI guidelines, um, to always be continuously monitoring
[1255.74 --> 1261.04]  for those, uh, those biases and everything. Yep. Yeah. So for us, I mean, I mentioned before,
[1261.04 --> 1266.76]  you know, when I, when I've done research on fairness and AI and bias and AI, there's a lot of problems
[1266.76 --> 1271.70]  that are really difficult to solve because the features that you're looking at, the inputs to
[1271.70 --> 1277.14]  your model that actually do matter for the thing you're trying to predict have different base rates
[1277.14 --> 1283.28]  in the data. So an example would be like, if you want to predict who should be given a loan or not,
[1283.50 --> 1288.44]  you'd need to look at credit score and income, but credit score have different and income have
[1288.44 --> 1295.48]  different distributions among different age, race, gender groups. So it's really hard to get away
[1295.48 --> 1301.84]  from that coming into your model and a way we're really lucky because we are only looking at this
[1301.84 --> 1307.50]  job interview. We don't do any kind of facial recognition. We don't find out who this person
[1307.50 --> 1312.96]  is and try to like scrape the internet for more information about them. We're not throwing in a
[1312.96 --> 1318.88]  bunch of data that we don't understand. We know exactly what we're dealing with. And the way we take
[1318.88 --> 1325.90]  our video interview data and structure it is intentionally made to kind of obscure some of
[1325.90 --> 1329.24]  the things that we don't want to know. Like we don't want to know your age, race, gender,
[1329.44 --> 1335.82]  attractiveness. We want to know the content of what you said, how you said it, like tone of voice,
[1336.06 --> 1340.18]  pauses, things like that, and your facial expressions. So those are kind of the three
[1340.18 --> 1343.80]  types of features we pull out and structure.
[1343.80 --> 1350.14]  So we're already kind of blinding the algorithm to demographic traits. But one thing to be aware
[1350.14 --> 1355.18]  of is that, you know, if there's bias in the training data, sometimes those traits can leak
[1355.18 --> 1361.58]  through somehow. So for example, maybe you have an algorithm that was trained to be sexist and it
[1361.58 --> 1367.90]  will notice some little difference in how men and women speak in the data set. So if that's the case,
[1368.02 --> 1373.68]  this continuous monitoring is really important to see how the algorithm is behaving in the wild.
[1373.80 --> 1379.12]  And if it does have any issues, like it's scoring men and women differently, we can go back and say,
[1379.26 --> 1383.44]  what are the features that are even telling the algorithm who's a man and who's a woman,
[1383.44 --> 1388.58]  and then remove some of those features. So we'll do a mitigation process. We are in the situation
[1388.58 --> 1393.22]  where we have a lot of features, so we can afford to throw some out. If they're contributing to bias,
[1393.32 --> 1398.20]  we simply remove them. In doing that, we might lose a little bit of predictive power, but we
[1398.20 --> 1405.56]  mitigate that adverse impact. We're also lucky in the sense that our rules are very well defined by
[1405.56 --> 1412.82]  the EEOC or the Equal Employment Opportunity Commission. So there's federal laws about how
[1412.82 --> 1420.80]  assessments can need to behave. And so we follow those very closely. And basically, the rules say
[1420.80 --> 1426.20]  that whatever, if you have some kind of a cutoff, like people who score above this score continue on to
[1426.20 --> 1432.26]  the next steps, and if you score below, you're out of the running. At that cutoff, no group can be
[1432.26 --> 1440.12]  scoring less than 80% or four-fifths of the top scoring group. So we have to follow those rules.
[1440.56 --> 1444.94]  That's U.S. law, and making sure that our algorithms are not treating people differently.
[1445.24 --> 1448.52]  And if we ever see anything, we can go through this mitigation process.
[1448.52 --> 1455.36]  Okay. So coming back out of break, I have a question for you, Lindsay. What types of things
[1455.36 --> 1462.26]  cannot be covered well algorithmically? And, you know, starting with that, and then kind of where
[1462.26 --> 1467.72]  do humans fit into the equation? You noted at the beginning that you thought humans would be
[1467.72 --> 1473.18]  in the equation for a while to go, for a long time potentially. And I'd like to understand kind of
[1473.18 --> 1476.02]  where they fit in and how the human and the algorithm work together.
[1476.02 --> 1482.00]  Yeah. So definitely we're not taking humans out of the loop anytime soon. I always kind of laugh
[1482.00 --> 1488.06]  when I try to talk to Siri and she does a terrible job of understanding what I'm saying.
[1488.50 --> 1494.66]  And I think like, oh my God, we're worried about these robots taking over. There's still so many
[1494.66 --> 1500.84]  things that humans are a lot better at. I think the important things that AI will be taking over are the
[1500.84 --> 1507.42]  mundane, boring things that AI can do well, while humans still really need to be a part of making
[1507.42 --> 1513.40]  personal connections, making final decisions and taking in other information that might not be
[1513.40 --> 1520.08]  available to the AI. For hiring, that does, you know, on the other side of the coin mean that bias
[1520.08 --> 1526.26]  will still be a part of hiring. But we've found that even removing bias from a chunk of that hiring
[1526.26 --> 1532.40]  funnel can help people get through to later stages that they might not have originally. We've had,
[1532.46 --> 1538.66]  you know, we've had customers say they've increased their diversity by 16% or give us these great
[1538.66 --> 1544.60]  metrics around, you know, kind of if this initial stage of the funnel is open to more people, they
[1544.60 --> 1550.60]  tend to get further along in the funnel. So definitely for the slice that AI is taking over,
[1550.60 --> 1557.72]  we hope to remove that bias. And one of the things you mentioned is kind of monitoring around fairness.
[1557.72 --> 1562.62]  And I was wondering, you know, it seems like you have to kind of develop a certain culture as
[1562.62 --> 1570.64]  data scientists and as a data science or AI team to really make that like a core part of a goal on each
[1570.64 --> 1575.70]  one of your products to kind of monitor for fairness and all of that. I was wondering if you could kind of
[1575.70 --> 1581.60]  briefly talk about, you know, how you went about developing that culture on your team and, you
[1581.60 --> 1586.04]  know, maybe make some recommendations for those out there that are kind of thinking about, oh, well,
[1586.08 --> 1590.20]  this is something I'd really like to do on our team, but I maybe don't know where to get started or
[1590.20 --> 1596.40]  how to develop that culture. Yeah, definitely. I think for us, a lot of it came from our IO
[1596.40 --> 1600.70]  psychology team and being in the assessment space. So starting from there, we kind of had,
[1601.24 --> 1605.52]  you know, like I said, we have laws around what our assessment, how our assessment scores,
[1605.52 --> 1610.48]  people, our particular assessment happens to include AI. We were coming into this space that
[1610.48 --> 1616.50]  the job assessment space that had been around for decades. So we got a lot of those, those ideas
[1616.50 --> 1621.70]  started there. And then it's kind of blossomed more and more as we've studied. There's a lot of
[1621.70 --> 1627.54]  academic study going on around this. And we, and we collaborate pretty closely with some researchers
[1627.54 --> 1632.70]  here at the university of Utah who study algorithmic fairness. Like I said, it's, you know,
[1632.70 --> 1637.04]  what constitutes fair is not well-defined. So it's usually something that needs to be discussed
[1637.04 --> 1644.26]  and refined for every individual problem. I would suggest a great place to start. IBM just released,
[1644.46 --> 1650.00]  it's called AI fairness 360. You can go on their website and just play. I played with it a little
[1650.00 --> 1656.18]  bit with just some Kaggle data and they show, you know, a lot of, a lot of these metrics that I talked
[1656.18 --> 1661.20]  about, you know, these kinds of definitions of fairness, and you can kind of see how those things are
[1661.20 --> 1666.92]  related to each other and how you can possibly mitigate bias. Another recommendation I have
[1666.92 --> 1672.64]  just to kind of illustrate the concept is a Google did some research. I think if you just,
[1672.76 --> 1678.06]  if you look for attacking discrimination with smarter machine learning, there's an article with,
[1678.06 --> 1684.68]  with an interactive portion where you can play with this fake data where it's credit score and
[1684.68 --> 1688.54]  you're trying to predict who would repay a loan. And this is something I mentioned earlier,
[1688.54 --> 1695.60]  but it's a great thing to play with and kind of see how there's trade-offs. So there's in real world
[1695.60 --> 1701.00]  situations, there's really not one way to do things where you could satisfy all notions of fairness.
[1701.24 --> 1705.78]  So you're always dealing with these trade-offs. And I think that's something that's good to look at.
[1705.86 --> 1711.94]  And again, this really varies from problem to problem, depending on your inputs and how different
[1711.94 --> 1717.32]  your base rates are and how much you rely on inputs with different base rates to predict your outcome.
[1717.32 --> 1722.96]  So, you know, keeping things practical, because this is, is practical AI. I'm finding all of this
[1722.96 --> 1726.78]  really, really fascinating. And I was wondering if you could just kind of walk through. So
[1726.78 --> 1733.28]  do you establish like maybe based on looking at some of this Google work or, or IBM work kind of
[1733.28 --> 1739.60]  figure out some metrics that at least make sense to track first? And then how are you tracking them?
[1739.60 --> 1744.30]  So you're, you're making predictions with your, your model. And then are you, are you running those
[1744.30 --> 1751.28]  metrics on the, on the predictions? Are you running them kind of on the, the training data that you're,
[1751.28 --> 1756.80]  that you're feeding in? What exactly are you, you monitoring and what's kind of the process? Like
[1756.80 --> 1762.54]  you put the metrics in place and then you kind of send notifications to people to, to review them and
[1762.54 --> 1765.42]  who reviews them. I'm kind of interested in those sorts of details.
[1765.42 --> 1770.88]  Yeah. So like I said, the notions of fairness that we look at are tightly tied to law, like
[1770.88 --> 1775.66]  employment law, but we also do, we look at other things as well. And we're always kind of interested
[1775.66 --> 1781.08]  in being ahead of it. I think it's kind of common that people assume data scientists don't care about
[1781.08 --> 1785.90]  this. And we really given it a lot of thought and we're always looking for different ways of looking
[1785.90 --> 1792.58]  at it and seeing how we can improve certain notions. But again, we kind of always come back to
[1792.58 --> 1799.14]  the regulations in the employment space as being kind of our most important base to cover.
[1799.46 --> 1804.80]  So I mentioned the four fifths rule or the 80% rule for us, which is something we closely monitor.
[1805.36 --> 1812.08]  And you, and like you did ask before about training data versus kind of how the algorithm is behaving in
[1812.08 --> 1817.20]  the wild. So we're always watching that, like here's the customer's cutoff score. They are watching
[1817.20 --> 1822.22]  job interviews for everyone who has scored above this. And maybe first, or maybe they're not
[1822.22 --> 1829.42]  watching the lower score, the lower scorers at all. So what, what are those ratios that that cut off?
[1829.42 --> 1835.10]  You know, how are men scoring compared to women? How are the different races scoring? If we ever have
[1835.10 --> 1840.10]  an issue there, continuous monitoring is really important because we start off, you know, with a
[1840.10 --> 1846.64]  training set of maybe hundreds and hundreds of interviews, and there wasn't a lot of diversity.
[1846.64 --> 1852.06]  Possibly there's, there's groups that were small and it was kind of hard to see with all the noise,
[1852.06 --> 1857.12]  how the, how the algorithms treating those groups. So watching how the algorithm actually behaves in
[1857.12 --> 1863.10]  the wild is very important as well. So we're, we're always watching those numbers and being proactive
[1863.10 --> 1869.58]  about coming to our customers and saying, Hey, we need to mitigate your algorithm. Obviously we also
[1869.58 --> 1873.74]  mitigate at the beginning, but if we ever see that, that we need to mitigate after the algorithms
[1873.74 --> 1879.32]  been out in the wild for a while, we will do that. Have you seen kind of have, have certain things
[1879.32 --> 1885.08]  surprise you as you've done this sort of monitoring, like biases or things pop up where you, you thought
[1885.08 --> 1890.48]  you did a really good job preparing the algorithm, but it turns out like you didn't in some way or
[1890.48 --> 1897.30]  another. Yeah. Most of that probably just come if, if there's any bias that comes in later on,
[1897.30 --> 1904.72]  a lot of that is because your training group just wasn't very diverse. So that is something that,
[1904.78 --> 1910.40]  you know, we see when we have, maybe there were very few people of color in this data set,
[1910.68 --> 1914.92]  or maybe there are very few women. So like I said, it was really hard to tell with just the training
[1914.92 --> 1922.30]  data that there was some, some feature that was allowing the algorithm to mimic bias in the data,
[1922.30 --> 1927.98]  but it becomes apparent later on. And we have seen that usually, usually not too badly. I mean,
[1928.00 --> 1933.00]  usually we're pretty on top of our monitoring. We don't see anything too drastically different than
[1933.00 --> 1939.66]  we expected. Cool. Yeah. So do you see, I'm thinking, you know, maybe we can transition a little
[1939.66 --> 1946.74]  bit here to kind of the machine learning and AI community in general, maybe outside of hiring.
[1946.74 --> 1954.08]  Are there things in like trends in the community around how we're developing AI that, that concern
[1954.08 --> 1959.64]  you around like the, the topic of fairness? And then are there maybe other things that are encouraging
[1959.64 --> 1964.80]  maybe these, these, these projects from IBM and Google, for example?
[1965.38 --> 1973.42]  Yeah. I think the conversation like IBM's 360 toolkit is an awesome example of how this is kind of
[1973.42 --> 1978.80]  coming into the conversation and people are talking about it for the last few years. I've sometimes
[1978.80 --> 1986.16]  been frustrated by the alarmism that goes on in the media, kind of calling out situations where
[1986.16 --> 1992.26]  data scientists did behave really irresponsibly, or just absolutely didn't think about repercussions.
[1992.72 --> 1997.74]  And it's hard as a, as a data scientist who does care about this and works on it a lot to not get a
[1997.74 --> 2002.80]  little defensive when you're stereotyped. But I think there are some legitimate concerns. Um,
[2002.80 --> 2008.34]  and there are a lot of books and articles about algorithms gone wrong and kind of showcasing
[2008.34 --> 2013.58]  these kinds of examples. I think it's good that that conversation is out there in some ways that
[2013.58 --> 2019.72]  it scares people and they kind of make assumptions that all algorithms are bad, which can be frustrating
[2019.72 --> 2025.54]  from the hiring point of view. You know, I talked about how broken hiring is and, and I really feel
[2025.54 --> 2031.38]  like we've made huge improvements where with an algorithm, we can actually look inside the algorithm
[2031.38 --> 2037.20]  and say, okay, what features are causing this bias? You know, you really quantitatively see how the
[2037.20 --> 2041.48]  algorithm is treating different people where it's a lot harder to do that with human beings.
[2042.06 --> 2045.90]  Human beings don't even know why they made the decisions they made. You can't open up their brain
[2045.90 --> 2049.76]  and figure out, oh yeah, you're a little racist. And that's why you're doing that. Let's just tweak
[2049.76 --> 2055.36]  your brain and account for that. And so, so we have like these tools that are amazing,
[2055.36 --> 2061.22]  but you know, like any powerful tool, they could be good or bad. And so I think it's,
[2061.22 --> 2065.12]  we're reaching a point where people are having these really important conversations about
[2065.12 --> 2066.66]  using them responsibly.
[2067.46 --> 2072.14]  Talking about bias in these ways, we we've had various conversations across different episodes
[2072.14 --> 2076.84]  with, with people doing all sorts of different types of work. And, and it's, it really seems that
[2076.84 --> 2082.40]  you have a great process now on how you're approaching it from with the monitoring and with the
[2082.40 --> 2086.32]  feature selection and trying to make sure your data fairly represents where you want to go.
[2086.42 --> 2091.30]  In a broader sense, beyond just the topic of hiring, we have so many people that listen that
[2091.30 --> 2097.60]  are faced with similar challenges. Do you have any, any more generalized recommendations that you would
[2097.60 --> 2102.66]  make to a data science team that is trying to get the bias out of their own situation, out of their
[2102.66 --> 2108.74]  own circumstances or, or something where rules of thumb that utilize on that, that is kind of broad
[2108.74 --> 2112.90]  based and simple for them to follow. Yeah. I know I've seen like, for example,
[2112.94 --> 2117.12]  like checklists come out. I don't know if those are useful or anything around like, you know,
[2117.16 --> 2123.04]  your data and your process and all of that. Yeah. I think, like I said, it's, it's, it's hard to define
[2123.04 --> 2129.00]  what fair is. And, and I think you have to kind of sit down and have a conversation with a lot of input
[2129.00 --> 2134.84]  about, you know, what you care about in this problem and, and, and being transparent about it,
[2134.84 --> 2141.00]  you know, are, are we, if you're not just trying to get a higher prediction accuracy,
[2141.00 --> 2146.84]  be clear that we care about these notions of fairness and, and this is what we're doing.
[2147.26 --> 2151.16]  This is what we're measuring and this is what we're doing to mitigate. That's something that's
[2151.16 --> 2155.38]  just been really useful for us because we were doing this for a long time and not really talking
[2155.38 --> 2161.72]  that much about it. We were getting criticized and, you know, when people assumed that we were
[2161.72 --> 2166.48]  being careless. So I think now this conversation started and people are, people are really,
[2166.48 --> 2171.20]  really transparent to be really open about it and say, Hey, what, you know, what we're trying to do
[2171.20 --> 2175.84]  is difficult. These are the notions of fairness that we care about and that we're trying to optimize
[2175.84 --> 2181.22]  and we're open to have conversations about that. And we're open to, you know, changing that. I think
[2181.22 --> 2186.96]  everybody understands that, you know, machine learning can be very powerful. And if there isn't clear
[2186.96 --> 2191.68]  answers, we want to have a conversation about what we're trying to do with it.
[2191.68 --> 2196.36]  One of the things that, that we've noted before is, you know, we're still in the very early days
[2196.36 --> 2201.10]  in data science, you know, especially if you compare it to, to software engineering, who has
[2201.10 --> 2205.52]  been maturing for, for decades now. And I'm kind of talking about the AI space specifically,
[2205.52 --> 2211.34]  but do you think that this period right now where we're all grappling with bias is a kind of growing
[2211.34 --> 2216.08]  pains that we're going through? Or do you think this is going to be inherent from now on? Is it always
[2216.08 --> 2219.34]  something that we're going to contend with, or do you think we'll have better tools going forward
[2219.34 --> 2220.30]  to tackle it?
[2220.30 --> 2226.10]  I think kind of both. I mean, I do think it's a growing pain. I think in five to 10 years,
[2226.28 --> 2231.92]  way more data scientists will be well-versed in fairness and, and understand that it's a part of
[2231.92 --> 2236.54]  their job and it's, it's something they need to think about. But at the end of the day, it's like
[2236.54 --> 2242.28]  any complex topic, there's always going to be different opinions. So because there's not one clear
[2242.28 --> 2247.50]  answer, I think there will always be debate about what an algorithm should be doing. And this is
[2247.50 --> 2251.20]  a great example with the compass model, the recidivism model that I mentioned.
[2251.68 --> 2257.26]  At the end of the day, there's no agreed upon way it should behave because different notions of
[2257.26 --> 2263.28]  fairness to satisfy them, you sacrifice another. And there will always be people that have their
[2263.28 --> 2267.70]  opinions about what the most important notions are. So I think it will be something that's
[2267.70 --> 2269.52]  controversial going forward.
[2269.96 --> 2275.72]  I know that I have definitely appreciated your perspective on this, Lindsay. It's been super
[2275.72 --> 2282.76]  enlightening to me. So thank you so much for being on the show. Are there any places where you'd like
[2282.76 --> 2288.32]  to point to people to, to, to find you online or, or certain resources or blog posts that you'd like
[2288.32 --> 2288.74]  to highlight?
[2289.16 --> 2296.94]  Sure. I'm on mostly just on LinkedIn, Lindsay with an E-Y, Zulaga, Z-U-L-O-A-G-A. That's where I'm
[2296.94 --> 2298.20]  probably the most active.
[2298.72 --> 2304.52]  Awesome. Well, thank you so much for, uh, for, uh, being on the show. And I know I'm really
[2304.52 --> 2309.40]  looking forward to seeing more of the great content that you put out and, and, uh, the great
[2309.40 --> 2312.16]  work that you and your team are doing. So thank you so much.
[2312.48 --> 2313.26]  Thanks for having me.
[2313.48 --> 2314.04]  Thanks a lot.
[2316.34 --> 2320.56]  All right. Thank you for tuning into this episode of Practical AI. If you enjoyed this show,
[2320.62 --> 2325.54]  do us a favor, go on iTunes, give us a rating, go in your podcast app and favorite it. If you are on
[2325.54 --> 2329.10]  Twitter or a social network, share a link with a friend, whatever you got to do, share the show
[2329.10 --> 2333.64]  with a friend. If you enjoyed it and bandwidth for change log is provided by fastly learn more
[2333.64 --> 2338.08]  at fastly.com. And we catch our errors before our users do here at change all because of rollbar
[2338.08 --> 2343.48]  check them out at robot.com slash change log. And we're hosted on Linode cloud servers.
[2343.48 --> 2348.84]  Head to linode.com slash change log. Check them out. Support this show. This episode is hosted by
[2348.84 --> 2354.24]  Daniel Whitenack and Chris Benson. Editing is done by Tim Smith. The music is by Breakmaster
[2354.24 --> 2359.40]  Cylinder. And you can find more shows just like this at change law.com. When you go there,
[2359.46 --> 2364.26]  pop in your email address, get our weekly email, keeping you up to date with the news and podcasts
[2364.26 --> 2369.10]  for developers in your inbox every single week. Thanks for tuning in. We'll see you next week.
[2375.68 --> 2380.48]  I'm Nick Neesey. This is K-Ball. And I'm Rachel White. We're panelists on JS Party,
[2380.48 --> 2384.70]  a community celebration of JavaScript and the web. Every Thursday at noon central,
[2384.86 --> 2389.36]  a few of us get together and chat about JavaScript, node and topics ranging from practical accessibility
[2389.36 --> 2395.72]  to weird web APIs. You could just eval the text that you're given and then, and that's basically,
[2395.72 --> 2401.36]  that's basically what it's doing. What could go wrong? Yeah, exactly. This is not a legal advice
[2401.36 --> 2406.90]  to eval text as it comes in. Join us live on Thursdays at noon central. Listen and slack with
[2406.90 --> 2410.68]  us in real time or wait for the recording to hit. New episodes come out each Friday.
[2410.68 --> 2416.60]  Find the show at changelog.com slash JS Party or wherever you listen to podcasts.
[2424.78 --> 2429.82]  I'm Tim Smith and my show away from keyboard explores the human side of creative work.
[2429.94 --> 2435.78]  You'll hear stories sometimes deeply personal about the triumphs and struggles of doing what you love.
[2435.78 --> 2441.40]  I got really depressed last year. And the reason it was so hard is because basically everything
[2441.40 --> 2446.86]  culminated at once. All these things I'd been avoiding, all these things I'd swept under the rug,
[2447.00 --> 2451.50]  they all came out at once. New episodes premiere every other Wednesday.
[2451.50 --> 2456.18]  Find the show at changelog.com slash AFK or wherever you listen to podcasts.
