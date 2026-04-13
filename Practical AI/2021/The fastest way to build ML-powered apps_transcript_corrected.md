[0.00 → 8.74] The thing that I'm seeing more and more is that the thing that is most valued is people who are able to take some data, write some SQL, create this simple data set to train a model.
[8.74 → 18.60] And then if you can get it behind a Flask API working decently performantly, not amazingly performantly, honestly, you're in the top 1% of data scientists, I think.
[19.00 → 22.18] For me, the trend that I'm seeing is that people are valuing those people more.
[22.48 → 27.18] I think like five years ago, people were looking to hire data scientists and more and more it's like, hey, we want machine learning engineers.
[27.50 → 28.32] There's a difference there.
[28.32 → 38.90] And your data scientist is, in my mind, kind of flawed title in the sense that it just represents anything from someone doing BI as an analyst to people building models to ML engineers.
[39.02 → 41.18] And we're kind of separating those things out, which I think is great.
[41.46 → 45.12] But I think the trend that I'm seeing is that more people value those machine learning engineers.
[45.62 → 49.02] Unfortunately, it's very, very difficult to find those folks.
[49.16 → 52.26] I think it'll take a bit for everyone to catch up to that.
[55.00 → 57.58] Big thanks to our partners, Linde, Vastly, and Launch Darkly.
[57.58 → 58.50] We love Linde.
[58.58 → 60.02] They keep it fast and simple.
[60.14 → 62.50] Check them out at linode.com slash changelog.
[62.74 → 64.78] Our bandwidth is provided by Vastly.
[65.14 → 66.48] Learn more at Fastly.com.
[66.74 → 68.70] And get your feature flags powered by Launch Darkly.
[68.96 → 70.70] Get a demo at LaunchDarkly.com.
[73.58 → 76.16] This episode is brought to you by our friends at O'Reilly.
[76.52 → 82.66] Many of you know O'Reilly for their animal tech books and their conferences, but you may not know they have an online learning platform as well.
[82.66 → 87.48] The platform has all their books, all their videos, and all their conference talks.
[87.82 → 98.60] Plus, you can learn by doing with live online training courses and virtual conferences, certification practice exams, and interactive sandboxes and scenarios to practice coding alongside what you're learning.
[98.60 → 112.54] They cover a ton of technology topics, machine learning, AI, programming languages, DevOps, data science, cloud, containers, security, and even soft skills like business management and presentation skills.
[112.66 → 114.44] You name it, it is all in there.
[114.76 → 119.92] If you need to keep your team or yourself up to speed on their tech skills, then check out O'Reilly's online learning platform.
[120.46 → 124.02] Learn more and keep your team skills sharp at O'Reilly.com slash changelog.
[124.02 → 126.42] Again, O'Reilly.com slash changelog.
[135.22 → 142.30] Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive, and accessible to everyone.
[142.66 → 146.72] This is where conversations around AI, machine learning, and data science happen.
[147.08 → 151.76] Join the community and Slack with us around various topics of the show at changelog.com slash community.
[151.76 → 154.84] And follow us on Twitter. We're at Practical AI FM.
[161.08 → 164.14] Welcome to another episode of Practical AI.
[164.54 → 166.08] This is Daniel Whiten ack.
[166.20 → 177.50] I am a data scientist with SIL International, and I'm joined as always by my co-host, Chris Benson, who is a principal emerging technology strategist at Lockheed Martin.
[177.82 → 178.50] How are you doing, Chris?
[178.90 → 180.40] I'm doing great. How's it going today, Daniel?
[180.40 → 186.30] It's going wonderful. You got any cicada broods down by your parts?
[186.86 → 190.86] So for any listeners that have listened to us for a while, they know that I do these weird wildlife things.
[191.06 → 193.76] And so, yeah, I'm getting tons of calls.
[194.00 → 196.24] It is like totally outside the AI thing.
[196.44 → 201.30] Our nonprofit that does the animal stuff, we're getting all sorts of calls about copperheads and all that.
[201.38 → 202.24] And people are afraid.
[202.36 → 205.40] And really, it's probably too late by the time people listen.
[205.40 → 207.14] Listen, but it's not an issue.
[207.38 → 208.82] There are no more copperheads than there ever are.
[209.14 → 211.46] So I know that has nothing to do with AI and ML.
[211.66 → 212.44] But, you know, there you go.
[212.50 → 215.60] There's my public service announcement for the cicada.
[215.60 → 227.76] Yeah, I mean, it is sort of a fascinating thing that I hear people talking like, you know, of course, like with climate changing and other things, how the broods are sort of a bit off.
[228.12 → 236.90] But some people, you know, it's hard to know a little bit because also more people are reporting data via all sorts of apps and channels and all sorts of things.
[236.90 → 239.62] And now, I mean, you're probably familiar with these apps that.
[239.76 → 240.96] Yep, there's several of them.
[241.10 → 246.20] I think it's iNaturalist and other things where people report different species and that sort of thing.
[246.24 → 248.86] And those are fed into models and all sorts of goodness.
[249.02 → 250.40] So, I mean, it is interesting.
[251.10 → 254.34] I love how you just tied the wildlife thing in with the whole AI and ML thing.
[254.40 → 255.10] That was perfect.
[255.22 → 255.64] That was good.
[255.88 → 259.02] You know, it's just one stream of consciousness for me.
[260.22 → 261.30] I'm really excited.
[261.58 → 264.46] Well, Chris, you know that we're very practical on this show.
[264.46 → 267.56] At least we try to be and relevant to our listeners.
[267.94 → 268.34] Indeed, we are.
[268.46 → 277.20] And I think that this is definitely going to be a very practical discussion because we're going to talk a little bit more about some new AI and ML developer tooling.
[277.68 → 278.16] Excellent.
[278.32 → 280.58] And deployment tools and all of that stuff.
[280.90 → 287.80] Today, we've got Tureen Srivastava with us, who is co-founder and CEO of Base 10.
[288.04 → 288.66] Welcome, Tureen.
[288.86 → 289.58] Hi, thank you.
[289.66 → 291.04] Thanks for having me, Chris and Daniel.
[291.70 → 293.06] Yeah, it was great to meet you.
[293.06 → 299.90] We had a chat last week, and I was learning a little bit about some of the things that you're doing and had to get you on the show right away.
[300.10 → 302.34] So, really excited to hear about that stuff.
[302.52 → 309.92] But before we dive into all that, could you just give us a little bit of info about your background, how you got into doing what you're doing now?
[310.22 → 312.14] So, my background is actually in electrical engineering.
[312.32 → 314.54] I studied electrical engineering in college.
[314.86 → 320.94] And after college, I decided that the right thing to do was to go work in finance in New York for a couple of years.
[321.06 → 321.90] It had nothing to do.
[321.90 → 328.46] That's the rumour in academia that I heard was like, you can sell your soul and go make a ton of money in finance.
[328.46 → 331.08] Not that you have to sell your soul to go into finance.
[331.08 → 335.60] Yeah, well, I got to work on the fun problem of privatizing toll roads.
[335.76 → 336.80] Ah, there you go.
[336.80 → 338.34] Which is fascinating in its own way.
[338.46 → 341.46] But after a couple of years of it, I decided that this wasn't for me.
[341.92 → 343.80] And I decided to go back to engineering.
[343.80 → 360.48] So, I actually moved to Boston from New York to work at a weird academic lab at Beth Israel Medical Centre, which is part of Harvard Medical School, where there's a professor there who had won a prize for coming up with a non-invasive way of tracking the progression of ALS.
[360.48 → 365.38] And he was spinning off a startup as part of that that was very, very data driven.
[365.46 → 366.46] This is like 2011.
[366.46 → 369.68] And, you know, I didn't know anything about machine learning or stats.
[369.82 → 373.98] Well, you know, I'd done a bunch of electrical engineering and information signal processing in college.
[373.98 → 377.30] I was like, you know, I could probably convince him, just take me on.
[377.52 → 382.10] And, you know, Boston startups are a weird breed in that, you know, they're kind of very research focused.
[382.22 → 383.08] They get a lot of grants.
[383.24 → 385.02] And, you know, frankly, they're quite cheap.
[385.28 → 387.92] And so, I was like, you know, I'll go and tell them to pay me hourly.
[388.44 → 389.22] I'll go work there.
[389.26 → 397.88] So, I went there, and I got to work with, you know, this guy and these three MIT PhDs, basically figuring out if they can predict the prognosis of neuromuscular disease.
[398.22 → 398.32] Yeah.
[398.72 → 399.52] Do you remember their names?
[399.56 → 401.74] I'm just curious because I've read up on ALS lately.
[401.74 → 402.18] Yeah.
[402.32 → 404.08] So, the guy's name is Stuart Remove.
[404.42 → 408.80] And the technology that he created was called HIM, which is Electrical Impedance Biography.
[409.44 → 411.64] And this is fascinating, and it makes me excited.
[411.72 → 412.88] So, I'll tell you really quickly what it is.
[413.04 → 420.58] We use EMG today to track how muscle health is progressing when folks have neuromuscular disease.
[420.88 → 424.80] It's a pretty horrible thing to go into every three months and have a bunch of needles poked into you.
[424.80 → 438.54] So, his idea was rather than poke needles in and track the electrophysiological properties to shoot a small current, a microcurrent that no one can feel across the outside of the muscle, measure the impedance drop and see if that correlates with muscle health.
[438.92 → 439.82] And, you know, it does.
[439.94 → 441.20] He's been working on it for 20 years.
[441.36 → 444.94] I happened to catch him at a time when he was commercializing technology.
[445.22 → 446.86] You know, it was a really fun time.
[446.98 → 448.84] You know, I got to work on all sorts of things.
[448.90 → 450.22] I learned statistics again.
[450.22 → 456.68] I really go into machine learning and so really, you know, the first thing we did was at the time we were applying support vector machines.
[456.84 → 460.40] This is like 2011, 2012 when support vector machines were all the rage.
[460.82 → 466.16] Support vector machines to see if we could separate out healthy muscle from diseased muscle.
[466.64 → 467.28] And that was really fun.
[467.60 → 471.10] Published a couple of papers and kind of really got, I was like, okay, this is pretty cool.
[471.54 → 473.64] You know, it seems like there's not that many people doing this.
[473.82 → 475.26] I could focus on this for a few years.
[475.26 → 481.30] And so I did that for a couple of years and my wife was, my now wife, then girlfriend, I guess, was a PhD student at Berkeley.
[481.44 → 482.86] I was like, I need to move out to California.
[483.34 → 487.64] So moved to San Francisco and started working at this company called Gum road.
[488.02 → 489.84] You know, Gum road is a lot bigger now than it was then.
[489.92 → 491.26] And I was one of the first few employees.
[491.68 → 494.02] It was an open-ended e-commerce platform.
[494.12 → 496.54] So anyone can sign up and start charging people.
[496.62 → 497.58] Anyone can get paid out.
[497.94 → 499.10] Great idea for creators.
[499.52 → 502.98] You know, really, really horrible from like a payment security and fraud perspective.
[502.98 → 508.14] You know, especially in the early days, you know, we used to get hammered with fraud.
[508.60 → 510.68] And so we just started first applying heuristics.
[510.92 → 520.98] And then we built out an entire kind of like ML pipeline there to not only cash fraud, but also the tooling to be able to deal with it once something had been flagged.
[520.98 → 522.02] So I did that until 2015.
[522.02 → 536.68] And then one kind of had the entrepreneurship bug and founded our first company, which went through a bunch of twists and turns, end up being an operational analytics company where we would capture data from a bunch of different operational tools, create a BI layer on top of it.
[536.90 → 538.66] Not really ML related, more data related.
[539.08 → 540.26] Sold that company in 2018.
[540.26 → 547.76] And then, you know, after working at the Acquirer for a year, decided that, hey, I really wanted to go back and work on ML tooling.
[547.96 → 549.30] I'd built a bunch of this stuff.
[549.38 → 553.52] I think a lot of ML engineers and data scientists end up building their own tooling even today.
[553.90 → 559.60] And, you know, it seems like the beginning of something a lot bigger and, you know, don't know where it's going to take us.
[559.60 → 566.70] But I really wanted to work on this idea of how do we get more people doing more machine learning and the tooling that will enable that.
[566.70 → 578.72] So I'm curious, as you were sort of in that progression, you know, you were sort of thrown into the fire working with statistical tools and machine learning at various stages in different companies.
[578.72 → 587.02] Throughout that history, was it mostly sort of you as a like data scientist or ML type person working with a bunch of developers?
[587.02 → 594.70] Or was it sort of bunch of developers trying to kind of pull in machine learning tooling where they needed it for like the fraud detection and stuff?
[594.80 → 597.84] What sort of patterns did you see as you were working at those various places?
[598.84 → 599.76] Yeah, that's a perfect question.
[599.90 → 601.88] I didn't actually start as an engineer.
[602.20 → 604.20] I started as a data scientist, machine learning engineer.
[604.44 → 608.00] And when I was in Boston working at the healthcare company, it was okay because it was very academic.
[608.72 → 610.44] I mean, a lot of it was like in MATLAB.
[610.66 → 615.34] And we could get a lot of the stuff done in MATLAB and throw it over the fence to someone who would happily take it out of that.
[615.44 → 618.06] When I joined Gum road, it wasn't like that.
[618.46 → 619.56] I was a data scientist and engineer.
[619.68 → 620.68] It was an early stage company.
[621.12 → 625.24] You know, end up hiring another data scientist and engineer who was a perfect dear friend of mine from Australia.
[625.70 → 629.76] You know, we didn't have the resources to help us productize the stuff we were building or production.
[629.80 → 631.08] So we just had to learn it ourselves.
[631.56 → 634.84] So it was very much coming at it from a data scientist perspective.
[634.84 → 643.84] But I don't think I was ever lucky enough to have, you know, a team of devs readies to go being like, hey, we'll happily productize this or productionize it.
[643.98 → 650.94] It was very much I was expected as a data scientist or machine learning engineer to do that myself or be resourceful about that.
[650.94 → 656.18] So do you feel like in that process, where was your time spent in that process?
[656.46 → 662.86] Like, as opposed to like before when you were at the company where most of your time was developing this sort of prototypes of MATLAB.
[663.60 → 668.40] Like, and now you were having to bring in this engineering side of things.
[668.58 → 671.26] Like, how did that sort of split up your time?
[671.98 → 672.94] Yeah, that's interesting.
[673.08 → 675.62] I think initially it was obviously in the model development part of it.
[675.62 → 684.50] What I realized really quickly was, like a lot of other data scientists, you end up being perceived as somewhat of a research function as opposed to a product function.
[684.92 → 686.52] You know, I found that really demoralizing.
[687.10 → 698.12] And so what I found was that it was in my best interest and the company's best interest if I, you know, worked on getting my stuff out of the Jupyter notebook and in front of other folks, as opposed to keep optimizing my model.
[698.58 → 699.78] Because you can do that forever, right?
[699.84 → 701.36] The model is never going to be 100%.
[701.36 → 710.00] What I realized pretty quickly was that for me and Phil, who was the other data scientist I was working for, that, hey, we'd already got the highest order bits out of the model.
[710.38 → 721.74] What was the most important right now was to make this practical for the company and have it plugging in back into the business process and really have other folks, whether that be, you know, the CEO, whether that be other engineers, you know, customer support.
[721.94 → 726.44] Like really seeing the fruit of what this model can enable for the company, for them.
[726.44 → 741.94] It's a bit of a timeless problem that you're describing there and that I know in the organizations that I've been part of over the years, I've seen that same set of problems recur over and over again, as well as those same biases and perceptions that people have.
[741.98 → 748.22] You talked about people assuming that the data scientist just has a research function, whereas the three of us are talking here today.
[748.22 → 753.92] You know, we understand the value of applying data science into the daily operations of business.
[754.04 → 756.14] And yet so many people have failed to do that.
[756.46 → 769.48] It's a fairly wide chasm to get all the things together to be able to not only do the data science, but to be able to communicate that out to the audience effectively and in a way that is accessible and usable to them.
[769.48 → 772.24] How did you approach that problem?
[772.24 → 777.96] Because, I mean, that's a massive problem that many people have tried to tackle, and I don't envy you that.
[778.12 → 779.98] So how did you set about going that?
[780.48 → 785.14] Yeah, I think I was lucky in that I've talked to a lot of customers over the last like year and a half.
[785.26 → 794.38] And one thing we realized is that a lot of engineering functions, and this is just a kind of nature of the beast of where a lot of data science and machine learning engineers are coming from.
[794.38 → 797.08] A lot of engineers don't want them writing code.
[797.32 → 799.94] They're like, hey, like, you know, it'd be best if you didn't do that.
[800.10 → 804.10] And I was lucky enough to be in a place where it was encouraged to write code.
[804.18 → 807.84] And so honestly, like for three to six months, like I just became a Rails developer.
[808.04 → 810.68] I was like the company's monorepo was in Rails.
[810.74 → 812.78] I was like, I'm going to figure out how to do this.
[812.84 → 815.84] Like I'd already done a little bit of Django programming on the side.
[815.90 → 816.78] I was like, I'll learn Rails.
[816.92 → 818.62] I'll understand kind of their language.
[818.88 → 820.54] And then I'll be able to bridge that gap.
[820.92 → 822.02] I think that was perfect.
[822.02 → 830.76] Like it's been really great for me because, you know, as I've gone through and, you know, built products over the last five or six years, being able to be an engineer has been great.
[831.04 → 833.40] But at the same time, I don't know if that's attainable.
[833.50 → 841.72] I don't think, you know, a lot of greats, really intelligent data scientists who have a great intuition when it comes to models want to be engineers.
[841.82 → 843.66] I don't think they want to learn about unit testing.
[844.02 → 846.76] I mean, I don't know if the best years of their time, but that's how I went about it.
[846.76 → 854.88] I think I've heard this story enough that there's a lot of leverage to be gained if you can somehow give data scientists engineering skills.
[855.20 → 858.62] And, you know, and there's not enough folks who have both of those skill sets.
[858.76 → 860.40] And has that been your experience as well?
[860.80 → 861.46] It has.
[861.58 → 868.08] I mean, I know that like Daniel and I both came into the AI world with lots of programming experience and different backgrounds.
[868.20 → 871.02] We actually did not meet each other in the AI ML world.
[871.02 → 875.40] We met each other in the Go programming language world and kind of transitioned over.
[875.64 → 891.52] And so I think my own perspective on that is that no one can master everything, but it makes sense to have some areas of strength and then extend your tentacles in other directions so that you can collaborate with other people who also have multiple areas.
[891.52 → 894.24] But maybe their strengths are in a slightly different area.
[894.48 → 898.42] And so that's how I've kind of tackled it as I've worked with different groups over time.
[898.42 → 903.56] I'm always super excited to hear about how people are addressing it.
[903.94 → 914.94] And really, the thing that you're doing that I'm really impressed with is being able to scale that out to many people, whereas I'm struggling to do it on my own and to work with different teams and to make those skills overlap.
[915.54 → 921.88] And so I'm pretty excited to see, you know, kind of what you came up with in your solution here to enable that for other people such as myself.
[921.88 → 929.04] Yeah, I think that I do see this changing and maybe this is what you're referring to, Wien, with sort of things changing in the landscape.
[929.52 → 938.86] Before, when I saw many tutorials for people getting into AI and other things, really just focused on data prep, training and evaluation.
[939.50 → 948.82] And I think that like there's just this sort of common perception that like, OK, I'm evaluated, like end of story, like I've done my job.
[948.82 → 958.14] And some people I talk to just even this concept that like you can save a model, like you can serialize it to a file and then use it later.
[958.34 → 961.60] Like that's something they're sort of not quite used to yet.
[961.60 → 974.56] I find that very like, yeah, I mean, even if someone's not going to be like, you know, a very engineering focused person, like having some level of understanding of the integration points.
[974.70 → 974.86] Yeah.
[974.98 → 981.32] And how like our work feeds into other things, that integration point is very important.
[981.44 → 986.54] Was that what you were referring to when you're sort of talking about like trends you were seeing or other things?
[986.54 → 987.54] Yeah, totally.
[987.72 → 998.66] I think the thing that like I'm seeing more and more is that the thing that is most valued is people who are able to, you know, take some data, write some SQL, create this simple data set to train a model, start to train their model.
[998.92 → 1008.88] And then, you know, if you can get it behind a Flask API working decently performantly, not amazingly performantly, honestly, you're in the top 1% of data scientists.
[1008.88 → 1012.90] I think for me, the trend that I'm seeing is that people are valuing those people more.
[1013.00 → 1017.88] I think like five years ago, people were looking to hire data scientists and more and more it's like, Hey, we want machine learning engineers.
[1018.04 → 1019.02] There's a difference there.
[1019.02 → 1019.66] I think.
[1019.76 → 1030.82] And your data scientist is in my mind, kind of flawed title in the sense that it just represents anything from, you know, someone doing BI as an analyst to people building models to ML engineers.
[1030.82 → 1033.08] And we're kind of separating those things out, which I think is great.
[1033.18 → 1037.04] But I think the trend that I'm seeing is that more people value those machine learning engineers.
[1037.04 → 1040.94] Unfortunately, it's very, very difficult to find those folks.
[1041.08 → 1044.10] I think it would take a bit for everyone to catch up to that.
[1044.22 → 1046.42] And so, you know, that's kind of like the trend we're seeing.
[1046.50 → 1049.02] And that's one of the trends that we kind of latched onto as well.
[1049.78 → 1050.68] So I'm very curious.
[1050.82 → 1064.08] We've led up to it without talking, without diving into it yet, but I would love to hear the backstory about how the idea for Base 10 came about, how you moved into it, how you arrived at the start of that process.
[1064.54 → 1064.90] Absolutely.
[1064.90 → 1070.72] So, you know, I think we've kind of gone through the context here, which is, hey, you know, it's pretty hard to get a model working.
[1071.14 → 1082.06] The hardest part of that or maybe the most important part of getting a model working, from my perspective and, you know, quite frankly, from the name of this podcast perspective, is making that model practical.
[1082.06 → 1088.26] Is making it plugged into some process or in front of real users who can give feedback on that.
[1088.62 → 1091.50] Again, like, as I mentioned, we noticed this, we learned that skill set.
[1091.84 → 1094.56] So our two co-founders, one is Phil, who I've worked with a bunch.
[1094.62 → 1101.14] And our third co-founder was kind of the head of engineering at Gum road, who went to work at a healthcare setup, which was very, very data driven.
[1101.14 → 1107.20] And from his experience as well, was that there's so much tooling that needs to go in once you have that model.
[1107.20 → 1119.42] So, you know, whether that be the deployment, monitoring, tooling, but more importantly, like the stuff that happened afterwards, which is, you know, how do you build, how do you integrate that into an existing system or, you know, build an application out of that model?
[1119.42 → 1124.84] And, you know, what happens today that we noticed over and over again was people were kind of building these shitty flask apps.
[1124.98 → 1125.12] Sorry.
[1125.34 → 1127.06] I don't know if that's okay.
[1127.96 → 1128.54] It's okay.
[1128.62 → 1128.92] He's going.
[1129.92 → 1131.28] There's a lot of them out there.
[1131.46 → 1132.82] I've seen them with my own eyes.
[1133.00 → 1133.16] Yeah.
[1133.32 → 1137.04] So, you know, like flask apps that they're definitely not going to scale.
[1137.22 → 1138.70] It's pretty hard to get them deployed.
[1139.26 → 1145.86] You know, everyone starts by pickling their models, but really quickly, as soon as their model gets any significant size, you can't fit in memory anymore.
[1145.98 → 1148.06] So you can't keep pickling and unpicking things.
[1148.06 → 1149.48] You know, we used to do this stuff ourselves.
[1149.48 → 1150.94] Like I'm not hating on it at all.
[1151.00 → 1157.22] It's just like, you know, we built these terrible systems where we took a model and especially a summer, we then deployed it.
[1157.24 → 1158.26] So we built a flask API.
[1158.42 → 1160.02] We were pickling and unpicking it on the fly.
[1160.26 → 1160.96] Not great.
[1161.24 → 1164.26] But then we were building all the application logic that sat on top of that model.
[1164.64 → 1166.50] So, hey, model gets run.
[1166.68 → 1169.14] So we compute the features, model gets run.
[1169.20 → 1173.16] And then the decisioning part of it, if the model exceeds the threshold, do X, Y, and Z.
[1173.54 → 1177.94] Otherwise, you know, put it in front of a human to go and review that transaction.
[1178.42 → 1180.24] What we did was we went and built all those things.
[1180.24 → 1181.54] So we deployed the model.
[1181.90 → 1184.32] We built the backend service to support that model.
[1184.52 → 1191.16] And then we also learned from an engineering to go and build that kind of queue-like interface for folks to do that.
[1191.40 → 1199.30] And, you know, my co-founder had a very, very similar experience at a healthcare company where they were trying to predict diagnoses from a medical record.
[1199.30 → 1203.50] And, you know, they wanted to put that in front of the doctors, so the doctors could get feedback on it.
[1203.98 → 1206.66] The way they did this was they ran the predictions in Bash.
[1206.74 → 1210.60] They piped into some data warehouse, pulled it out, put it into Excel.
[1210.98 → 1211.44] And I'm not joking.
[1211.54 → 1217.40] They sent the Excel file with, like, the patient ID and the predicted diagnosis to the doctor and asked for feedback.
[1217.76 → 1220.32] Obviously, the doctor's not going to, like, act on that, right?
[1220.36 → 1221.66] They're going to be like, this is too much work.
[1221.66 → 1233.80] And so I've kind of led up to this where I'm saying that, you know, if you are that top 1% of data scientists or machine learning engineer who can kind of do all those things that, you know, we had to learn how to do, this is great.
[1233.90 → 1234.46] You can do that.
[1234.52 → 1238.30] But for the rest of them, can we give them the leverage to become that data scientist?
[1238.36 → 1239.42] And what does that leverage mean?
[1239.50 → 1245.74] And so what we went and built was a way to lower the barrier to usable productized machine learning.
[1245.88 → 1250.62] And so today with Base 10, you can deploy machine learning models with a couple of lines of code.
[1250.62 → 1259.04] And so what that means is that you go import Base 10 in your Python library, you Base 10.deploy with your model binary, and we take care of everything.
[1259.12 → 1265.46] So we Docker write, we create a Docker container, you know, we load it all up, you get an API that's ready to go that's nice and scalable.
[1265.74 → 1268.22] And really, like, don't worry about Flask.
[1268.46 → 1272.30] Don't worry about the infrastructure, the servers you need behind this to make it work.
[1272.40 → 1273.30] Do you need GPUs?
[1273.30 → 1278.98] It's literally, you know, an argument or a check of a box in our UI to put it behind power with a GPU.
[1278.98 → 1280.66] And don't worry about versioning.
[1280.72 → 1284.22] So you can keep deploying over this, and we can do, like, version rollout and you can switch back.
[1284.66 → 1287.68] What's most important, though, is that, like, that to us is the integration cost.
[1288.26 → 1291.52] Like, this is really exciting that you can do that with a couple lines of code.
[1291.64 → 1293.40] But that's not really where we see our value.
[1293.48 → 1295.06] Our value is the stuff that comes after it.
[1295.10 → 1300.72] Like, can we make it so as a data scientist and machine learning engineer, you can also write all the business logic on top of that model.
[1300.72 → 1305.76] So we kind of give you a serverless framework to be able to write logic on top of that model.
[1306.30 → 1307.66] And so, like, you can build APIs.
[1307.82 → 1308.82] You can run things from Iron.
[1309.16 → 1310.88] You can even, you know, have forks.
[1310.94 → 1313.84] So you can have decision points within that business logic.
[1314.24 → 1319.48] But a data scientist or machine learning engineer can do all these things without learning any infrastructure.
[1319.72 → 1321.88] All they really have to worry about is their Python code.
[1322.30 → 1325.44] And, you know, that complexity of the infrastructure doesn't vanish.
[1325.50 → 1326.10] It just shifts.
[1326.10 → 1327.94] And we think we can take care of that.
[1328.10 → 1331.68] And all you need to worry about is your code, your Python, and your model.
[1332.28 → 1337.26] Lastly, something that we loved, you know, at times we're kind of told that we're trying to boil the ocean here.
[1337.48 → 1338.90] But that's fun to us.
[1339.20 → 1345.06] The last thing we do that we love is, you know, we always wanted to put a face on our model, an interface on that model,
[1345.06 → 1349.14] so that folks could either give feedback on it or operate on the output of the model.
[1349.32 → 1356.00] So if you're building a recommendations model, can you really quickly assemble a UI, so someone can input something,
[1356.36 → 1361.16] run that model that you deployed, see the recommendations, and give feedback on each of those recommendations
[1361.16 → 1364.90] so the data scientist can take that and really get that iteration cycles going.
[1365.22 → 1370.18] So you can build that in a drag-and-drop way without learning any JavaScript, HTML, or CSS.
[1370.52 → 1373.20] And that's really where we arrived for now.
[1373.20 → 1379.12] What we, again, hope to be able to do is just give more machine learning engineers and data scientists that leverage
[1379.12 → 1381.04] so they can kind of ship full-stack applications.
[1381.04 → 1386.10] And hopefully as a result of that, what you'll see is that people will see results of machine learning faster.
[1386.56 → 1390.18] And as a result, they will invest in machine learning more because they'll see what it can do for them.
[1390.48 → 1391.94] Sorry, I just spoke for a long time.
[1392.08 → 1392.48] That was good.
[1392.58 → 1393.36] No, that's great.
[1393.48 → 1395.66] Yeah, perfect to get that whole context.
[1395.66 → 1403.58] One of the things that I find interesting is, like, I see sort of a trend on my end in terms of ML, AI.
[1404.04 → 1411.36] In that world, there's sort of this trend to kind of no-code solutions and that sort of thing where things plug together.
[1411.52 → 1415.80] What I find interesting about sort of what you just talked through is it's not no-code.
[1416.00 → 1419.90] So the data scientist is still sort of working in their, like, Python world.
[1419.90 → 1422.50] But then it lowers the barrier to these other things.
[1422.68 → 1435.64] So there's, like, you know, a data scientist, I think, if we assume they're working in Python, it's not that far, like you say, to maybe have them think about, like, a Flask app or something like that.
[1435.64 → 1441.96] But then as soon as they try to start getting that out into the world, they're like, oh, how do we scale this up and other things?
[1442.02 → 1448.26] And then they find out, oh, there's these, like, various layers of abstraction that I need to think about, like, you know, containers.
[1448.54 → 1449.92] And then how does that scale up?
[1449.98 → 1453.54] Well, now I need multiple instances of my service behind a load balancer.
[1453.66 → 1455.28] And where are all those containers going to run?
[1455.38 → 1458.80] Well, they're going to run in Kubernetes or some container orchestrator.
[1458.98 → 1465.10] It's like it starts to develop in their mind this sort of, like, inception dream within a dream within a dream.
[1465.10 → 1472.12] Like, they just sort of keep going down that thing and things start becoming just less clear and really strange.
[1472.32 → 1476.12] So I think, like, it's cool that you could still let them operate.
[1476.54 → 1483.44] From my experience, data scientists, you know, and people working in this area, they love opening their Python editor.
[1483.74 → 1484.30] 100%.
[1484.30 → 1485.92] Writing out their code.
[1485.92 → 1495.50] Really having kind of fine-grained control over the preprocessing and fine-grained control over how they build their model architecture and all those things.
[1495.62 → 1496.92] That's sort of where they want to live.
[1497.08 → 1503.38] So not, like, saying, sort of taking that away from them and saying, no, don't do that in code anymore.
[1503.60 → 1506.82] But, you know, sort of letting them still enjoy that part of their code.
[1506.82 → 1512.30] But then adding on these other things, I think, is a fascinating way of thinking about it.
[1512.84 → 1514.38] This guy has become a friend of sorts.
[1514.52 → 1515.60] His name is Slater Stitch.
[1516.00 → 1520.92] He had this great tweet over the weekend, which was, you know, what I want even more than no code is yes code.
[1521.04 → 1523.74] But literally, you never have to think about infra at all.
[1524.14 → 1529.82] And I think that is, from our perspective, like the data science, like the great articulation of the data scientists issue.
[1529.92 → 1531.80] Like, Python is a really, really valuable tool.
[1531.80 → 1535.10] You know, you take pandas away from me, I'm a third of the person I was.
[1536.32 → 1537.52] I want to write Python.
[1537.70 → 1541.46] I want to, you know, be able to use SQL as well, you know.
[1541.74 → 1544.44] But I don't want to think about Docker Kubernetes.
[1544.58 → 1548.82] I don't want to think about, you know, if I deploy a model, how do I switch versions?
[1549.14 → 1550.22] How do I A-B test things?
[1550.28 → 1551.74] How do I monitor things?
[1551.80 → 1552.80] How do I deal with downtime?
[1553.04 → 1554.24] You know, code is great.
[1554.70 → 1555.36] Infra is hard.
[1555.90 → 1556.00] Yeah.
[1556.14 → 1560.94] Before I ask the next thing, I got to say, you have some perfect one-liners in there that I'm going to steal for later on.
[1560.94 → 1561.58] Please do.
[1561.80 → 1565.98] The boil the ocean, well, that's what I like to do, is an excellent one because I hear that all the time.
[1567.82 → 1568.94] Every day of my life.
[1569.08 → 1569.22] Yeah.
[1569.54 → 1569.90] Yeah.
[1569.98 → 1572.38] You've had several there, so I'm stealing your stuff, dude.
[1572.44 → 1573.30] I appreciate it.
[1573.38 → 1583.82] I wanted to ask, so one of the things that it sounds like you've done a perfect job on is by taking those levels of abstraction, as Daniel referred to it, the dream within the dream.
[1583.98 → 1584.14] Yeah.
[1584.36 → 1586.44] You can only handle so many layers of abstraction.
[1586.62 → 1587.36] You can't do it all.
[1587.36 → 1595.92] And it sounds like by taking control of some of that, that somebody can use Base 10 to integrate in with an existing environment by using the APIs.
[1595.92 → 1598.60] And so they get a big payout.
[1598.60 → 1605.64] And they don't have to worry about all the things, you know, whether, you know, from containers, you name it, all the things that Daniel just talked about.
[1605.64 → 1613.02] And yet can get the benefit that way, which is quite beautiful because I know that it's kind of where people have been trying to drive to.
[1613.08 → 1617.60] And it sounds like you've gotten a very nice, elegant solution for achieving that.
[1617.72 → 1618.48] Is that fair?
[1618.62 → 1620.36] Is that kind of how you would think of using it?
[1620.58 → 1620.70] Yeah.
[1620.86 → 1626.02] I think, you know, we're very early on and, you know, early users will tell you that there's a lot more elegance to be added.
[1626.28 → 1627.12] But there always is.
[1627.12 → 1630.02] That is, you know, from like an abstraction perspective, absolutely.
[1630.28 → 1638.20] You know, like I think one of the things that we did early on was like we kind of defined kind of the principles of the architecture that we wanted to build.
[1638.46 → 1642.40] And I think like two of them that really stand out here are like the principle of least astonishment.
[1642.94 → 1645.36] You know, the like take it away, but don't make it magic.
[1645.64 → 1649.78] I think that's like, you know, it's like hide it from me, but still give me details of what you're doing.
[1650.00 → 1655.78] You have a blog post that includes that information, I noticed, which you could talk a little bit about here because I was going to bring that up as well.
[1655.78 → 1664.34] Yeah. So the principle of least astonishment is really important to us just because, again, like data scientists and machine learning engineers, we're kind of like these pseudo engineers, right?
[1664.36 → 1665.04] We're somewhere in between.
[1665.16 → 1666.24] We know what's going on.
[1666.54 → 1668.86] Maybe we don't know kind of all the intricacies.
[1669.08 → 1677.00] So all the attractions we've tried to keep quite similar to, you know, how firstly, like what data science and machine learning engineers understand.
[1677.12 → 1682.16] And two, you know, even like building an application for an end user, like there's a back end, there's a front end.
[1682.16 → 1687.90] And then you'll see these concepts in base 10, and we separate them out, and we allow the interplay of them, but we're not hiding them all together.
[1688.00 → 1694.28] I think, you know, the second thing, which I think you've kind of talked about is like, this is something that we saw from one of our early engineers.
[1694.28 → 1696.88] It was like, you know, easy things are easy and hard things are possible.
[1697.18 → 1699.26] And like, to me, that's such a great line.
[1699.36 → 1699.70] It is.
[1699.74 → 1703.90] Which is like, you know, we want to 80 or 90% of the things to be simple.
[1703.90 → 1706.12] And, you know, you don't have to think about it and they just happen.
[1706.12 → 1709.74] But that shouldn't come at the expense of control and visibility.
[1709.90 → 1715.88] And I think that's one place where a lot of kind of like lower code or no code abstractions get dinged.
[1715.94 → 1718.56] It's that they hide things away, and you're kind of like, well, how did that happen?
[1718.84 → 1719.86] That kind of scares me.
[1720.26 → 1721.46] We are exposing these things.
[1721.56 → 1728.48] And so you can go deeper if you want with each of our concepts, because, you know, like we are built on Docker, K-native, Postgres.
[1728.92 → 1730.54] You know, you can write Postgres queries.
[1730.70 → 1733.88] You can kind of inspect those technologies to go deeper if necessary.
[1736.12 → 1742.28] This episode is brought to you by Snowplow Analytics.
[1742.82 → 1746.60] Snowplow is the behavioural data management platform for data teams.
[1747.00 → 1757.66] Maximize the value of your behavioural data using Snowplow Insights, a managed data platform that's built on leading open source tech leveraged by tens of thousands of users.
[1758.08 → 1765.26] Capture and process high quality behavioural data from all your platforms and your products and deliver that data to your cloud destination of choice.
[1765.26 → 1772.96] When marketing needs to make data informed decisions, when product needs next level understanding, and when analytics needs rich and accurate data.
[1773.28 → 1780.58] Snowplow is a solution for data teams who want to manage the collection, processing, and warehousing of data across all their platforms and products.
[1780.90 → 1785.00] Get started and experience Snowplow data for yourself at SnowplowAnalytics.com.
[1785.00 → 1787.92] Again, SnowplowAnalytics.com.
[1787.92 → 1805.26] So with your solution, we've talked about several different things.
[1805.26 → 1812.36] So you talked about the sort of, you know, importing a few lines of code, deploying your model, and also this sort of UI builder.
[1812.36 → 1832.18] Could you kind of describe like for someone maybe that's listening to this that doesn't have a web page up, could you sort of, you know, just describe a bit like the developer workflow in terms of what they would need to do with base 10 versus in their code to take their model from local model to an API?
[1832.18 → 1836.26] And then also maybe to build in one of these UI apps around it.
[1836.32 → 1839.20] What does that workflow practically look like at this point?
[1839.54 → 1840.20] It's a perfect question.
[1840.32 → 1842.78] So you start the workflow from where you do your work.
[1842.78 → 1848.48] So from a Jupyter notebook, I mentioned earlier, you can import base 10 and base 10.deploy your model.
[1848.76 → 1849.14] That's it.
[1849.38 → 1849.64] And so.
[1850.04 → 1852.60] And that would be the REST API sort of framework?
[1852.98 → 1853.62] Yeah, exactly.
[1853.62 → 1858.80] So like basically, you know, we work with PyTorch, scikit-learn, and TensorFlow models right now.
[1858.98 → 1860.76] You can also write a custom model.
[1860.88 → 1869.06] So if you just create a class with a load and a predict method, basically every time the model gets run, that predict method will get called.
[1869.38 → 1871.00] The load is kind of the deployment step.
[1871.32 → 1874.44] Just again, easy things easy, hard things possible.
[1874.60 → 1877.12] Like if you want to do more, you can do those things.
[1877.12 → 1883.44] But once you deploy it with that single line of code or a couple lines of code, what you end up with is like a REST API.
[1883.72 → 1885.28] You'll go to base 10.co.
[1885.56 → 1889.02] You'll be able to see the status of your model, all the times it's been called.
[1889.30 → 1892.10] But then you get instructions on how to call it from your own services.
[1892.64 → 1898.54] Straight away, once you're there, you can easily move from the realm of the model to the realm of the application.
[1899.02 → 1900.48] And that's what we're really excited about.
[1900.48 → 1908.76] And so, you know, for that model, you can then write all the pre-processing code and post-processing code within base 10 in the surrounding browser.
[1908.80 → 1913.76] So think of it kind of like, you know, we're still iterating on this and figuring out the exact right experience.
[1913.76 → 1917.46] But right now, it kind of represents DAG that you're used to in Airflow.
[1917.62 → 1919.34] So you can write the code within base 10.
[1919.40 → 1920.80] It's represented in a graph-like structure.
[1921.46 → 1926.50] Again, there is a shared state and context between each of those nodes in that DAG.
[1926.50 → 1930.88] So, you know, you can reference things from the pre-processing node and the post-processing node.
[1931.20 → 1932.30] But you can do other things as well.
[1932.40 → 1935.54] You know if you want to call the Twitter API, it's a Python-like environment.
[1935.54 → 1937.38] So you can bring in whatever libraries you want.
[1937.76 → 1942.00] Once you've done that, now that entire thing, we already gave you the REST API for that model.
[1942.42 → 1944.22] That entire thing is called by an API.
[1944.56 → 1946.24] You can also trigger it from a cron job.
[1946.34 → 1949.64] So we've got built-in support for iron all in line.
[1950.26 → 1952.58] Or you can call it from a streaming data source.
[1952.58 → 1955.76] So if you have a Kafka queue, we've built those integrations as well.
[1955.76 → 1963.18] So, you know, you've really gone from just a model in your notebook to something that was deployed with an API really quickly.
[1963.38 → 1972.00] And then in, you know, just a little bit more, you can start to write the kind of pre-processing and post-processing code and logic within base 10, put that behind an API.
[1972.26 → 1981.86] And so really what we're seeing is stuff that would take, you know, three to five days of kind of wrangling and getting it set up without really even thinking about how to get it on AWS with an API.
[1981.86 → 1989.32] I don't like exaggerating, but it really is like within, you know, 30 to 40 minutes, we've had live services running with machine learning models.
[1989.62 → 1996.80] I think the last thing now, as I mentioned earlier, is that now you have kind of like, so you have this model, now you have these API endpoints.
[1996.80 → 2003.38] Then you can start to build UI within base 10 and link actions within that UI to those API endpoints.
[2004.32 → 2019.24] So with this deploy method, one of the things I'm thinking about just from your perspective in terms of developing this infrastructure is all the crazy stuff that like varied frameworks and architectures and everything that people are using.
[2019.24 → 2021.30] So they have all sorts of crazy dependencies.
[2021.76 → 2024.06] Some people are using, like you're saying, TensorFlow.
[2024.42 → 2025.76] Some people are using PyTorch.
[2026.20 → 2030.24] Right now, how do you approach that sort of dependency stuff?
[2030.34 → 2034.52] So you mentioned supporting like TensorFlow, PyTorch models, scikit-learn models.
[2035.06 → 2037.24] What about this sort of other dependency stuff?
[2037.90 → 2043.92] Is it a matter of pulling that from a person's like virtual environment, or how do you go about handling that side of things?
[2043.92 → 2044.24] Yeah.
[2044.38 → 2048.68] Again, as I said, like with the PyTorch and TensorFlow and scikit-learn stuff, like you don't have to really worry about that.
[2048.68 → 2051.64] With the custom model stuff, we do need that.
[2051.86 → 2053.66] We do need to know like what requirements you need.
[2053.78 → 2059.06] So really when you deploy that custom model, you also pass us a requirements.txt.
[2059.38 → 2063.10] And then we basically set up the environment with that ready to go.
[2063.28 → 2063.40] Cool.
[2063.78 → 2064.22] Yeah.
[2064.80 → 2065.06] Yeah.
[2065.26 → 2071.94] And I'm trying to, so at the beginning of this conversation, I think this conversation has clarified a lot for me.
[2071.94 → 2089.38] And sort of where I'm distilling things down is that it seems like if you look at this sort of landscape of developer tooling for AI people, there's sort of some things kind of over in one area around ML ops and like experiment management, like logging experiments and all the thing.
[2089.38 → 2096.42] You can run your Jupyter notebook and log your experiments and put your job in queues for GPUs or whatever.
[2097.00 → 2103.84] And then you sort of got maybe on the other side of things like widget and prototype type builders.
[2103.84 → 2107.18] You got sort of like Streamlet or Radio or something.
[2107.18 → 2112.44] In the middle, maybe you have like maybe some serving frameworks that people use.
[2112.60 → 2116.26] Maybe it's like TensorFlow serving or, you know, something like that.
[2116.26 → 2134.16] But there's sort of like path from like left, you know, from one side of that to the other, just like involves so many different like jumps between different sort of systems and spinning up all sorts of different kind of infrastructure and all of that.
[2134.16 → 2154.46] And I think all of those tools have obviously some fascinating features, but it almost seems like you're sort of not all of it, but you're gluing many parts of that together in sort of consistent workflow for people that really could, you know, sort of accelerate them through that process from experimentation to deployment.
[2154.78 → 2156.04] Am I characterizing that right?
[2156.08 → 2162.70] I'm trying to think of like how people might sort of view this with reference to like other things in the landscape they might be familiar with.
[2162.70 → 2165.88] Yeah, I think that's a perfect characterization of it.
[2165.96 → 2169.44] I think, you know, we talked a bit about this last week on Outcome.
[2169.56 → 2175.60] It's like, you know, this pretty wild, like how like the ML Oops tooling has evolved over the last couple of years.
[2175.66 → 2177.96] You know, there's so many great point solutions out there.
[2178.14 → 2182.38] And, you know, that's kind of like the ML Oops side on like the Streamlet Hex side.
[2182.48 → 2186.52] You know, there's some really great kind of notebook based application builders that are out there.
[2186.52 → 2189.98] You know, putting all these things together is quite difficult.
[2190.36 → 2197.82] And, you know, also like having to jump between three or four different tools to kind of have that end to end thing working is pretty hard.
[2198.02 → 2198.96] And, you know, it's complex.
[2199.60 → 2205.16] It takes time, patience, budget, you know, and most of these tools, including us, you know, we're in beta still.
[2205.24 → 2206.92] Like you can't just sign up, and you're ready to go.
[2206.92 → 2209.04] You know, so it is difficult to do.
[2209.12 → 2218.42] What we do want to be able to do is, again, when you're Aruba and you have, you know, literally millions of requests per second going through, you know, base 10 is not the right tool for you.
[2218.66 → 2220.02] You know, you need something specialized.
[2220.38 → 2229.66] When you're working on something that, you know, in its infancy or, you know, it's critical, but, you know, it doesn't need that type of latency or doesn't need that sort of specialization.
[2230.08 → 2233.62] What we hope is that base 10 can kind of fit the bill of that end-to-end solution.
[2233.62 → 2247.00] So you have your model and rather than waiting for DevOps to come and deploy your model, waiting for a front engineer, product engineer to come and build the things that make that model relevant for like 80 or 90% of the use cases, we think base 10 can be that end-to-end solution.
[2247.50 → 2254.78] To one, get your prototypes and toys out the door and two, in the end, build those full stack mission-critical applications as well.
[2254.90 → 2259.12] As you're looking now, you know, you're in beta, you're approaching release.
[2259.44 → 2261.04] What do you have in mind?
[2261.14 → 2263.50] What needs to be there that may not be there yet?
[2263.62 → 2265.36] That you're envisioning for release.
[2265.44 → 2268.94] Are there any new features or is it solidifying the things that you already have?
[2268.98 → 2269.18] Yeah.
[2269.40 → 2272.78] And based in, how are you seeing that 1.0 release in the short term?
[2273.40 → 2273.90] Yeah, totally.
[2274.06 → 2274.74] It's a perfect question.
[2274.96 → 2277.24] So we did like a launch last week, which is well received.
[2277.34 → 2279.80] And, you know, we got a ton of inbound from that, which has been great.
[2280.08 → 2283.30] But really what we're trying to figure out in this next phase is usability.
[2284.08 → 2290.72] You know, again, there's like the user and the use cases, the intricate and the complex and, you know, figuring out, hey, how can I get you to value?
[2290.72 → 2294.18] How quickly can you have your aha moment and be using this in something real?
[2294.50 → 2295.38] We want to solve that.
[2295.46 → 2300.68] And we want to solve that well before we, you know, open this up to kind of the world and say, go wild.
[2300.68 → 2309.96] Because we know that, you know, a lot of those decisions are easy to iterate on and change, you know, once you are working with a small core group of users where you know the value is to be added.
[2310.92 → 2316.96] As you're having all of these discussions with users, obviously right now you're talking to a lot of people, you're getting feedback.
[2316.96 → 2321.90] So you're sort of seeing a cross-section of the industry to some degree.
[2322.06 → 2340.10] As you're having that perspective and maybe looking at the industry more generally, as we close up here, is there anything in terms of the AI ML industry or maybe the developer tooling industry that just sort of generally excites you in terms of where the industry is headed or maybe capabilities that are being developed or other things?
[2340.10 → 2340.98] What's on your mind?
[2341.14 → 2341.28] Yeah.
[2341.42 → 2348.88] I mean, you're obviously focused a lot on base 10 right now, but sort of what are those things that you're thinking about towards the future?
[2349.28 → 2349.42] Yeah.
[2349.50 → 2353.94] So there are two things that I keep thinking about, which make me really, really excited.
[2353.94 → 2357.74] So the first one is one of our investors has a perfect campus recruiting program.
[2357.86 → 2360.12] And so we're able to spend a lot of time with new grads.
[2360.48 → 2370.46] What's really exciting to me is that, you know, nine out of 10 software engineers, not data scientists coming out of, you know, the best schools in the country or honestly any computer science degree have exposure to AI and ML.
[2370.46 → 2371.82] They're taking a couple of courses.
[2372.02 → 2379.50] At the very least, they can phrase, they can frame a problem in terms of how machine learning can solve it.
[2379.50 → 2390.16] And that to me is amazing because that means that the amount of evangelization that needs to be done within a company is lower because people already appreciate what can happen with that.
[2390.54 → 2399.12] I think the second thing, which should be considered in line with this or like together with this is the prevalence of pre-trained models is going up.
[2399.22 → 2402.62] You know, Hugging Face has done so, so freaking well over the last couple of years.
[2402.62 → 2409.42] And, you know, every company, almost every company that we talk to who's starting to some NLP initiative is starting with Hugging Face.
[2409.50 → 2411.00] Maybe with some fine-tuning step.
[2411.54 → 2414.68] But to me, that's really exciting because you have two things going on, right?
[2414.72 → 2418.10] So you have one thing going on, which is more and more people know what ML can do.
[2418.30 → 2423.06] And two is that there's all these ways to have that model ready to go.
[2423.36 → 2427.52] Like you don't need that, you know, two or three month effort to get that first model up and running.
[2428.00 → 2428.92] Put those things together.
[2429.02 → 2430.58] And I think you've got something really special, right?
[2430.58 → 2436.90] So you have, you know, people understand what the tool can do and more powerful tools in the form of, you know, pre-trained models.
[2436.90 → 2447.94] And I think, you know, that's one thing that we're kind of leaning into as well, even with our user base, that we're not only considering data science and machine learning engineers as our user base, but are you an engineer who knows what ML can do for you?
[2448.24 → 2452.16] Because if you are, we hook up all those pre-trained models and give you a model zoo.
[2452.54 → 2456.84] So if you want to have a zero shot classifier, like, you know, you don't really have to think about anything.
[2456.92 → 2462.22] You can have it embedded in a workflow in an application with base 10, as long as you know how to frame the problem.
[2462.22 → 2468.50] And so, you know, like I've tied it back to ourselves, but, you know, from like a high level, they're the two things I'm really, really excited about.
[2468.94 → 2469.68] That's awesome.
[2469.84 → 2471.16] Yeah, those are really exciting.
[2471.42 → 2483.22] It is really cool to see like most conversations now that I'm having with teams and companies, like you don't have to sort of get over the hurdle of like we expect AIMS to give us some value.
[2483.22 → 2491.56] It's more like entering into the follow-up discussion to that, which is where is their value, where should we focus and that sort of thing.
[2491.78 → 2495.18] And so technical teams are really thinking about this a lot, which is cool.
[2495.70 → 2497.96] So thank you so much to Main for joining us.
[2498.02 → 2498.92] This is really exciting.
[2499.16 → 2500.62] Congratulations on your launch.
[2500.76 → 2501.34] It's awesome.
[2501.72 → 2505.40] And we really hope that our listeners please check out what base 10 is doing.
[2505.58 → 2507.46] We'll have links in our show notes.
[2507.64 → 2508.86] So check them out.
[2509.20 → 2512.38] Talk to us about some of your opinions about this in our Slack channel.
[2512.38 → 2518.30] You can always find us in one of our communities on LinkedIn or go to changelog.com slash community.
[2518.52 → 2523.00] Join our Slack channel and happy to chat with you about base 10 and other things.
[2523.18 → 2526.60] So, yeah, thank you so much to Main, and we'll let you get back to work.
[2526.72 → 2527.70] Thank you guys so much.
[2527.80 → 2530.12] You guys are really nice, and it was really nice to be on the show.
[2533.52 → 2535.54] Thank you for listening to Practical AI.
[2535.88 → 2537.88] We appreciate your time and your attention.
[2537.88 → 2541.94] If you enjoyed this episode, help us out by spreading the word.
[2542.50 → 2543.28] Think of a friend.
[2543.48 → 2544.16] Think of a colleague.
[2544.44 → 2547.26] Somebody who would benefit from listening to it and send them a link.
[2547.60 → 2548.62] We'd really appreciate it.
[2548.90 → 2552.32] Practical AI is hosted by Chris Benson and Daniel Whiten ack.
[2552.54 → 2556.08] It's produced by Jared Santo with music by Break master Cylinder.
[2556.48 → 2559.66] Thanks again to our sponsors, Vastly, Linde and Launch Darkly.
[2559.82 → 2560.62] That's our show.
[2561.08 → 2563.76] We hope you enjoyed it, and we'll talk to you again next week.
[2563.76 → 2593.74] We'll see you again next week.
