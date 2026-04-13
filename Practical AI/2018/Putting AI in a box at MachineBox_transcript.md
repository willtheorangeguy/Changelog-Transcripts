[0.00 --> 6.70]  Bandwidth for Changelog is provided by Fastly. Learn more at Fastly.com. We move fast and fix
[6.70 --> 11.42]  things here at Changelog because of Rollbar. Check them out at Rollbar.com and we're hosted
[11.42 --> 17.66]  on Linode servers. Head to linode.com slash Changelog. This episode of Practical AI is
[17.66 --> 23.28]  brought to you by Hired. One thing people hate doing is searching for a new job. It's so painful
[23.28 --> 28.32]  to search through open positions on every job board under the sun. The process to find a new
[28.32 --> 33.94]  job is such a mess. If only there was an easier way. Well, I'm here to tell you there is. Our
[33.94 --> 38.64]  friends at Hired have made it so that companies send you offers with salary, benefits, and even
[38.64 --> 44.04]  equity up front. All you have to do is answer a few questions to showcase who you are and what type
[44.04 --> 48.90]  of job you're looking for. They work with more than 6,000 companies from startups to large publicly
[48.90 --> 53.88]  traded companies in 14 major tech hubs in North America and Europe. You get to see all of your
[53.88 --> 58.88]  interview requests. You can accept, reject, or make changes to their offer even before you talk
[58.88 --> 62.68]  with anyone. And it's totally free. This isn't going to cost you anything. It's not like you have
[62.68 --> 66.52]  to go there and spend money to get this opportunity. And if you get a job through Hired, they're even
[66.52 --> 70.50]  going to give you a bonus. Normally it's $300, but because you're a listener of Practical AI,
[70.82 --> 75.74]  it's $600 instead. Even if you're not looking for a job, you can refer a friend and Hired will send
[75.74 --> 81.48]  you a check for $1,337 when they accept the job. As you can see, Hired makes it too easy.
[81.48 --> 84.70]  Get started at Hired.com slash Practical AI.
[97.94 --> 103.34]  Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[103.78 --> 109.26]  productive, and accessible to everyone. This is where conversations around AI, machine learning,
[109.26 --> 113.38]  and data science happen. Join the community and snag with us around various topics of the show
[113.38 --> 119.22]  at changelog.com slash community. Follow us on Twitter. We're at Practical AI FM. And now onto the show.
[123.66 --> 129.66]  Welcome to Matt and David from Machine Box. It's great to have you here on Practical AI. I know that
[129.66 --> 136.40]  Chris and I, when we started thinking about guests for Practical AI, and I was thinking about our
[136.40 --> 142.06]  slogan or our mantra at Practical AI, which is making artificial intelligence practical,
[142.34 --> 147.32]  productive, and accessible to everyone. I know the first people that came to my mind
[147.32 --> 150.64]  were Matt and David from Machine Box. So welcome, guys.
[151.34 --> 153.16]  Thank you very much. It's great to be here.
[153.66 --> 154.18]  Yeah, thank you.
[154.30 --> 160.32]  Yeah. Let's start out maybe with just a kind of brief personal intro from both of you guys.
[160.32 --> 164.42]  So, David, why don't you start by giving us a little personal intro?
[164.88 --> 171.26]  Yeah, I'm David Hernandez. So my background is in computer science and engineering. So I was
[171.26 --> 178.16]  studying back more than 10 years ago in the uni, machine learning and artificial intelligence.
[179.46 --> 186.16]  Mostly, I never used it until recently, the last three years that the machine learning was bombing,
[186.16 --> 194.66]  and I started to get through, refresh my knowledge and started to implement things. And probably that's
[194.66 --> 203.04]  how we started Machine Box in some way. And professionally, I've been developing since I finished my degree. It's
[203.04 --> 212.14]  almost also 10 years doing distributed systems, website. My highlights probably, I've been, I work
[212.14 --> 221.02]  at the BBC at 2012 for the Olympics. So we were delivering the real-time system to all the stats
[221.02 --> 231.90]  and all the video player data for the Olympics, basically. It was a real nice project. So yeah, that's it.
[233.20 --> 238.48]  Sounds great. And Matt, why don't you give us a little bit of an idea of where you're coming from?
[238.48 --> 245.70]  Yeah, sure. So hi, my name is Matt Ryer. I've been doing computer science all my career in various
[245.70 --> 251.26]  forms. I spend a lot of time in the Go community at the moment. I kind of fell in love with Go as a
[251.26 --> 257.34]  language before it was released as version one. There was a little experimental tag in Google App
[257.34 --> 261.72]  Engine, and I wanted to build something on App Engine. And anything that's got a little experimental
[261.72 --> 268.26]  tag is going to grab my attention. It always has. So I jumped into the language kind of quite early.
[268.26 --> 274.56]  And I've just been kind of using Go since then, really, wherever I can. And it turns out you can
[274.56 --> 283.18]  use it everywhere. I speak at conferences about Go mainly. And also, I have a book, Go Programming
[283.18 --> 288.68]  Blueprints, which is nice because you build real projects in that book. So it's not a book where you
[288.68 --> 294.20]  learn the language or you just learn theory. You actually build real things. So it's very practical
[294.20 --> 299.96]  and very pragmatic. And that's why I quite like the way you guys are approaching this podcast,
[300.34 --> 305.48]  because, you know, complicated things can be extremely powerful, but they're very difficult
[305.48 --> 311.50]  for people to kind of marshal and get, you know, get into a shape that they can put into production.
[311.84 --> 317.76]  And that's really our philosophy at Machine Box is to give people a head start on that and get them
[317.76 --> 322.70]  into production much quicker. And hey, Matt, while we're at it, what's the name of your book before
[322.70 --> 329.14]  we go on? Oh, it's called, thank you. It's called Go Programming Blueprints, colon, second edition.
[330.26 --> 334.86]  Okay. Thank you very much. Yeah. You don't have to say it in that accent, but it helps.
[334.96 --> 336.62]  It sounds much better. I think it does help.
[336.62 --> 342.92]  So how did you guys originally meet and how did you start thinking about forming a company
[342.92 --> 348.46]  together that's focusing on AI? Well, that's interesting story. So
[348.46 --> 357.66]  back a few years ago, I was one of the organizers of Golang UK, the first one, now GoferCon UK,
[358.42 --> 365.48]  or just GoferCon, I don't know. GoferCon UK. GoferCon UK. So Matt was one of the speakers. So I met
[365.48 --> 374.30]  actually Matt in that conference. He was in another company before and I was looking kind of for a job.
[375.26 --> 382.82]  I was a contractor at the time. So I joined the same company that Matt was and we met there,
[382.96 --> 390.44]  basically. We worked there for a few years. Yeah. David has a really kind of unique ability to
[390.44 --> 400.24]  think very clearly about big problems that are otherwise very complicated. And that's a key skill
[400.24 --> 405.94]  for any team to have. If you can bring somebody in that can look at these kind of big, broad problems,
[406.04 --> 412.66]  like massive kind of scale, planet scale sort of problems. Like David mentioned earlier, he was part
[412.66 --> 418.26]  of the team that delivered the software that ran the Olympics. And you can't, there's no dry runs of
[418.26 --> 422.84]  that. You can't say to everyone, guys, can we just like a week before, can we just have another
[422.84 --> 431.32]  Olympics just so we can test out all the software? They'd probably say no. So having somebody like
[431.32 --> 440.58]  that on a team is invaluable. And it was very natural when it came to looking at machine learning
[440.58 --> 449.24]  and David's expertise in it. It was kind of his eureka moment where he said, you know, we could
[449.24 --> 455.14]  actually kind of containerize this and deliver it in a way that makes it very trivial for everybody
[455.14 --> 463.68]  to use machine learning capabilities rather than having to learn TensorFlow and work in these kind of
[463.68 --> 470.28]  abstract mathematical models. We could tell some stories differently. We could give people an API
[470.28 --> 477.76]  that just makes it very clear and sort of changes the way you think about the problem a little bit.
[477.82 --> 484.10]  It focuses really on the problem that you're trying to solve rather than technical sort of low level
[484.10 --> 491.00]  machine learning components that you might use to solve it. Yeah, that's great. And again, I think,
[491.42 --> 497.72]  you know, I've been a machine box user for quite a while. I think, you know, very soon after you guys
[497.72 --> 504.58]  launched, I was super excited about it just because of the practicality of the project. So in terms of
[504.58 --> 511.52]  like what machine box is actually, you know, as a developer, like if I was wanting to use machine box
[511.52 --> 516.92]  to do something, what might that something be? And what would be the interface to doing that?
[517.26 --> 526.54]  Yeah, sure. So machine box is basically we deliver machine learning models in Docker containers. So what
[526.54 --> 533.40]  you basically need is Docker install in your computer that is available in any
[533.40 --> 543.02]  major platform, Windows, Mac and Linux. You just Docker pull one of our images. You have a nice API
[543.02 --> 553.34]  in our images. So you only need to know about HTTP APIs to get started and do, for example, face recognition.
[553.34 --> 563.20]  That is one of our most famous boxes. So you can add face recognition to your stack in just minutes.
[564.00 --> 573.90]  So that's basic tools. Docker, a little knowledge to do HTTP APIs as a programmer that probably every
[573.90 --> 582.42]  programmer should learn that skill nowadays. And that's basically you don't need any other knowledge.
[582.42 --> 589.90]  So just to just to clarify, I mean, really, like if I was a, you know, a data scientist or a developer
[589.90 --> 596.52]  or whatever I am, you know, there's a lot of APIs out there, both, you know, from the cloud platforms,
[596.52 --> 601.62]  like with, you know, machine learning, but also other things, like if I want to send an email or
[601.62 --> 609.46]  something programmatically, there's there's like a REST API for for that, which uses HTTP and and and JSON.
[609.46 --> 616.36]  And so you're saying kind of one of your goals is to really make the interface to doing something
[616.36 --> 622.60]  complicated, maybe like facial recognition or something as easy as it is to, you know, send an
[622.60 --> 627.68]  email via via one of those APIs. Is that is that kind of a good? Yeah, that's that's exactly right.
[627.84 --> 634.84]  Yeah. So essentially, the machine learning that that's going on inside the boxes is very complicated.
[634.84 --> 642.46]  And sometimes we mix different kinds of technologies in different ways, where and if we tried to explain
[642.46 --> 649.04]  how to do that, it would be very complex. And I think the deployment would be difficult. And
[649.04 --> 654.74]  even just managing the dependencies would be a bit of a nightmare. So we take on all that pain
[654.74 --> 660.42]  and provide APIs that tell different stories. So for example, you mentioned facial recognition,
[660.42 --> 669.26]  face box is a Docker container, you download it, you run it, you then have HTTP access. And you the
[669.26 --> 674.38]  operations you can do are things like here's an image, tell me all the faces in that image and give
[674.38 --> 683.62]  me the coordinates of the faces. Not only that, if you recognize these people in who the face belongs to,
[683.86 --> 690.26]  tell me who that person is as well. And then there's another API call to teach. And we
[690.26 --> 696.16]  support one shot teaching, which is also pretty kind of rare still, which is but it just means that
[696.16 --> 704.08]  with one image, so Daniel, I could take an image of your face and teach face box with one example image.
[704.08 --> 709.84]  And then if we took a big, big photograph at a conference, and you were in it, face box would
[709.84 --> 716.00]  be able to find you and identify you. You know, so you get that facial recognition capability. And it's
[716.00 --> 721.44]  only a couple of API endpoints you have to learn. It's basically teach this face. And here's an image,
[721.62 --> 726.74]  who do you who do you see in there. And then yeah, it's all JSON, because we wanted to just feel
[726.74 --> 734.34]  really familiar and just fit into what people already had. And, you know, HTTP and JSON APIs still
[734.34 --> 739.48]  dominate the simplest to use, you can use them like they're nice, because you can just use them in the
[739.48 --> 745.52]  browser. And when you run one of our boxes, we actually host inside the box, a little private
[745.52 --> 751.64]  website, which you access through localhost 8080. And that website contains all the API documentation,
[751.64 --> 757.28]  but also lets you interact with the box without even writing any code. Because it's very important
[757.28 --> 765.16]  on our mission to make, first of all, communicate what's possible in a very simple way, and then make
[765.16 --> 770.90]  that easy to play with and get to use so that people can see the power of it. And then once
[770.90 --> 775.72]  they've sold on that, then it's just a question of making that making the integration easy and
[775.72 --> 782.14]  operations. And so we're, we're really focusing on that whole, that whole flow end to end. In particular,
[782.14 --> 789.00]  we care about people without any kind of machine learning experience being able to use these powerful
[789.00 --> 789.68]  technologies.
[789.68 --> 795.68]  So it sounds like machine boxes is, is, is been, you've taken the machine learning part
[795.68 --> 801.20]  and abstracted that and put it in a little black box for your end users. Who specifically are you
[801.20 --> 803.70]  targeting as your customer for this?
[804.66 --> 809.66]  Well, we've, we've, we have already paying customers. And so I say already, because although
[809.66 --> 815.86]  Daniel started playing with machine box way before we really launched anything. And one of the nice
[815.86 --> 822.94]  things about the fact that the way we approach our developer community is we give them the technology
[822.94 --> 829.44]  for free early and let them just play with it. And that process, what happens is, first of all,
[829.70 --> 834.76]  any bugs are immediately found and squashed. Luckily, it doesn't happen very often. We do a lot of
[834.76 --> 840.24]  testing and test driven development and other techniques, which help us when it comes to kind of
[840.24 --> 847.76]  code quality. But beyond that, we get to validate the way we've told a story. And also, you know,
[847.76 --> 853.30]  if the APIs really make sense for the particular way in which their system expects to use a technology
[853.30 --> 859.54]  like this. So we've had, we see customers are all kinds. We, we, we, we really only, uh, it's a
[859.54 --> 865.22]  developer tool. So this is for developers to integrate into their platform. So by and large,
[865.22 --> 872.06]  all of our audience are developers, but the people that really kind of have so far found it to be
[872.06 --> 879.86]  useful are people who they understand machine learning in broad terms, some of them, but they
[879.86 --> 887.10]  know that it's a lot of effort to go to, to build your own things yourself. And then, you know, if you
[887.10 --> 893.58]  care about the data, not leaving your own network, whether that's on-prem or your own cloud, uh, because
[893.58 --> 898.90]  we're just Docker containers, you can spin them up anywhere and scale them anywhere. It's, you know,
[899.00 --> 905.12]  you keep control of all that data. So it's people who they, they understand they have already a need,
[905.16 --> 910.26]  which is great. They've got a problem that they want to use machine learning to solve. And then
[910.26 --> 916.60]  they use our APIs to, uh, to solve that problem. So they're basically developers of all levels.
[916.60 --> 921.74]  Usually, uh, I mean, some, some of them are just JavaScript developers. Some of them are, uh, Ruby.
[921.74 --> 928.42]  We do have a Go SDK. So we have a lot of gophers. We have a lot of Go people that are using it. So
[928.42 --> 933.38]  it's really that that's, that's who we target is basically any, anyone's a potential target, but
[933.38 --> 939.98]  specifically we've seen traction in, in developers who don't want to have to do all the heavy lifting
[939.98 --> 942.80]  of machine learning. You just want to get something and get going.
[942.80 --> 951.48]  Yeah. My favorite, uh, users, uh, are it's, it's kind of a personal opinion and it doesn't necessarily
[951.48 --> 958.56]  mean that that, uh, is, is right. So my favorite users are, are DevOps or people doing DevOps basically,
[958.56 --> 965.50]  because they, they basically love it because they usually don't have time or willing to learn any kind
[965.50 --> 971.94]  of data science. They want to solve specific problems and, and they find much inbox and our,
[971.94 --> 978.38]  or API is really good and really productive for that. So we, we, we get a lot of love from, from,
[978.38 --> 984.42]  from DevOps. The best comments that we, we hear is if from people doing DevOps, like, oh, I have this
[984.42 --> 990.08]  problem. I want to solve it quickly. I want to deploy it quickly. And it, it, it is just the,
[990.08 --> 997.18]  the perfect tool for, for, for that kind of people. Uh, and, and yeah, pretty much.
[997.88 --> 1005.72]  Yeah, that's great. I, I know, um, personally, uh, I, I can attest to, uh, you know, just the,
[1005.72 --> 1011.58]  the quality, uh, of, of the models. Um, I know I actually kind of got into, uh, a little bit of
[1011.58 --> 1016.98]  trouble at a, at a conference cause I was showing face box and, uh, kind of one shot updating of the,
[1016.98 --> 1022.34]  of the model and, uh, and people didn't believe me that it actually worked, uh, worked that well.
[1022.60 --> 1028.96]  So, so that made for, yeah, that's happened to us as well. I think, uh, in a demo, we've had it
[1028.96 --> 1035.78]  where people just think we've spoofed it. Um, yeah, I know it's surprising because, um, you know,
[1035.82 --> 1040.22]  we, we're told again and again for machine learning to be any good, you need massive amounts of training
[1040.22 --> 1046.56]  data. So that's why, um, it's, it's, and, and really the solution, I mean, it's kind of a bit secret
[1046.56 --> 1053.22]  of what we do, but it's, um, we, it's just a clever, uh, use of technology inside the box,
[1053.22 --> 1058.58]  which allows us to provide that. But the thing is, we don't want people to have to worry about
[1058.58 --> 1064.72]  how it works. We just want them to know that it works and, um, and, and integrate it, you know,
[1064.72 --> 1068.98]  and, and get to MVP really quickly. That's really another one of our goals.
[1069.34 --> 1075.88]  You know, a few weeks ago, I was in San Jose at, uh, NVIDIA's annual, uh, GPU technology conference.
[1075.88 --> 1081.32]  Uh, and, and through my employer, I had, I was in a small group meeting with the NVIDIA CEO,
[1081.44 --> 1087.22]  Jensen Wong. And, uh, he noted something that I see you guys, uh, kind of going toward and he,
[1087.42 --> 1092.46]  that we're really at a junction where software developers are becoming the targets of machine
[1092.46 --> 1097.56]  learning rather than just data scientists. And it will continue to be both, but, uh, he noted that
[1097.56 --> 1102.62]  that was, that was a big strategic initiative on them was to target the software development
[1102.62 --> 1106.02]  community, uh, which is somewhat new to these technologies. And it seems that you guys have
[1106.02 --> 1107.98]  really centered your strategy around that approach.
[1109.58 --> 1115.06]  Yes. I mean, that's, that's right. I mean, really what happened in, if I'm being completely honest,
[1115.06 --> 1121.24]  is we just built something that we needed to use. We wanted to use some of these technologies
[1121.24 --> 1127.62]  and it's, it's hard and we had constraints and, you know, some of the, some of them at scale,
[1127.62 --> 1134.92]  some of the prices of the, the machine learning APIs at scale really, um, it's, it's really becomes
[1134.92 --> 1139.80]  prohibitive. I mean, it's, it's just, it's still quite expensive and it's still, it's, it's, it's quite
[1139.80 --> 1146.12]  valuable, I guess. So that's why, but we weren't, we weren't really kind of too strategic about it in the
[1146.12 --> 1151.50]  beginning. We just thought, let's just build, let's build it how we think it should be built and how
[1151.50 --> 1158.66]  we would want to use it. Um, and from there we've then started to see, uh, traction and, or, and,
[1158.66 --> 1161.90]  you know, some great feedback from our, on our developer experience.
[1162.56 --> 1169.12]  Yeah, definitely. Um, and I kind of want to, um, follow up a little bit on those, you know,
[1169.20 --> 1174.42]  that idea kind of that we mentioned around, around the conference talks is, you know, you kind of use
[1174.42 --> 1179.36]  this machine box to do something and it's doing something complicated under the hood and it's
[1179.36 --> 1185.32]  giving you great, you know, great results. But to some degree, you know, um, even though you might
[1185.32 --> 1191.10]  know generally what's happening in, in the box, it still is a black box. And, um, there's kind of a lot
[1191.10 --> 1196.78]  of back and forth in, in industry right now, at least in the circles that I kind of frequent around,
[1196.78 --> 1203.14]  you know, is treating machine learning and AI models as kind of a black box, a good thing or,
[1203.14 --> 1209.06]  or a bad thing. And, you know, AI, you know, like I can, I can download pre-trained models and that
[1209.06 --> 1214.82]  sort of thing that I don't really understand right from the TensorFlow repo and other things. Um, and
[1214.82 --> 1222.94]  often really there, you know, I don't get the kind of results that are, that are, you know, either
[1222.94 --> 1227.76]  published results or the kind of quality that's promised from these pre-trained models. Now the
[1227.76 --> 1232.86]  models that you're putting out are, are definitely, I get really good, um, quality, but I, I still
[1232.86 --> 1238.28]  don't really know, um, all of what's going on, on, on the inside. Um, so in this case, like we're
[1238.28 --> 1242.94]  treating machine learning and AI models kind of like a black box. Why do you think in, in, at least
[1242.94 --> 1249.46]  in certain cases, you know, treating models like this, like a black box can be, can be a really good
[1249.46 --> 1254.32]  thing or maybe what, what are, what are some downsides or, or cases in which maybe you wouldn't
[1254.32 --> 1260.06]  want to treat them like that? Yeah, sure. So, um, yeah, all the machine box models are kind of a
[1260.06 --> 1267.34]  black box. So in that case, we, we don't have any explainability for any of the models, but also most
[1267.34 --> 1274.06]  of the models are based in, in neural networks. So nobody has that answer yet in the research.
[1274.18 --> 1280.38]  There are some being researched about it, but nobody knows what, what is happening inside.
[1280.38 --> 1288.26]  Uh, so you just mean in terms of the complexity of the models? Uh, yeah. Uh, but also, uh, for use
[1288.26 --> 1297.94]  cases. So, I mean, uh, for example, if, if you're gonna deny or accept a credit or, or, or an insurance
[1297.94 --> 1304.96]  is, is quite important to understand what a model is predicting. I'm saying, oh, if, if my income is
[1304.96 --> 1310.94]  less than this quantity, uh, the, the model is going to say, oh, you, you're gonna, you, you're not
[1310.94 --> 1315.36]  going to get the insurance or you're not going to get the credit. But for, for example, facial
[1315.36 --> 1324.12]  recognition, you care less about, uh, why the model is predicting that this is matching a face, uh,
[1324.44 --> 1330.70]  rather than not matching the, this other identity. So you, you are more worried about, uh, the value that
[1330.70 --> 1336.76]  you can extract for that matching rather than the, the value that you can get explaining what, why the
[1336.76 --> 1343.96]  model is doing. So it's, it's quite a balance and it really depends the use cases. Uh, mostly our use
[1343.96 --> 1349.98]  cases doesn't really matter the explainability in most of the boxes. We have, for example,
[1349.98 --> 1357.22]  classification box that allows you to build any kind of classifier, uh, given text or images. So
[1357.22 --> 1365.96]  it may matter most for, for that kind of, uh, model. But in general sense, we, we more focused
[1365.96 --> 1373.52]  on getting value for the models rather to explain what the models do. Um, yeah, that's, that's a great
[1373.52 --> 1380.64]  point. And I mean, to, to your guys point, um, I think, you know, if, if you're not able to put your
[1380.64 --> 1386.96]  model into production and get any value out of it, uh, via a useful interface, then, you know,
[1386.96 --> 1393.42]  um, really what we're talking about is just, you know, AI research that isn't really applicable in
[1393.42 --> 1397.28]  a, in a business setting. So you have to be able to get things into production. And I think that's,
[1397.66 --> 1402.84]  that's where this sort of black black box treatment, in my opinion, um, is, is a really
[1402.84 --> 1409.08]  good thing in terms of, you know, providing a unified interface for developers and DevOps people
[1409.08 --> 1414.42]  and infrastructure people to, to interact with a model. But yeah, but anyway, it should be,
[1414.42 --> 1420.92]  I, I believe that the research is gonna come through. Um, um, um, someday we can explain
[1420.92 --> 1427.94]  how a neural network, uh, do the reasoning and why a prediction is, is that prediction. So,
[1427.94 --> 1433.96]  uh, we, we probably try to keep up with the research and if, if that comes through, we, we,
[1433.96 --> 1436.34]  it's a possibility to add it to the boxes.
[1437.12 --> 1442.12]  Yeah. But those kinds of, um, those sorts of things and, and a lot of the arguments against
[1442.12 --> 1450.08]  black boxing are for, it's really, I think people who are deep in machine learning, they know about
[1450.08 --> 1457.62]  it. Um, they want to, um, that, you know, they want to invest time and resources into kind of
[1457.62 --> 1462.44]  building expertise and things like that. Lots of people aren't in a position where they can do that.
[1462.44 --> 1468.94]  Um, so we, you know, we, we give them a capability. It's a solution. It's, it's, it's,
[1469.00 --> 1474.02]  they are models inside. Sometimes there are multiple ones inside each box, but there's also
[1474.02 --> 1480.18]  other things going on in there. So really it is a solution that, um, you know, we, the only reason
[1480.18 --> 1485.90]  really that machine box isn't just completely an open source project is that it's just so
[1485.90 --> 1492.94]  complicated that it wouldn't be, I don't think, you know, it's not like it's just kind of a trivial
[1492.94 --> 1497.24]  little, little package that would be sensible to open source and everyone can get use out of
[1497.24 --> 1504.30]  to use, to be able to contribute to the machine box code base, I think would be, uh, more difficult
[1504.30 --> 1509.46]  than other projects. And so that's one of the reservations I have against open sourcing is,
[1509.58 --> 1515.08]  is that, but yeah, so it's really an audience question. I think if people care deeply and know a lot
[1515.08 --> 1518.96]  about machine learning, then maybe they're going to want to pick up TensorFlow and tackle it
[1518.96 --> 1525.50]  themselves. If you're an app developer and you want to quickly, you know, make your, make your
[1525.50 --> 1530.92]  software smarter, slotting machine box in, um, is just the quickest way to do that.
[1531.42 --> 1536.12]  Yeah. And, and I think it's like not inconsistent with other trends we're seeing like TensorFlow
[1536.12 --> 1540.38]  estimators and that sort of thing, right? Which, which is intending to kind of give these
[1540.38 --> 1544.58]  modules to people that, that will let them practically integrate things.
[1544.58 --> 1549.64]  Yeah, exactly. Yeah. It's kind of, uh, overlapping. They are catching up with,
[1549.64 --> 1555.50]  uh, with machine box for, and that, that was a great transition. And when you were talking about,
[1555.50 --> 1560.66]  uh, about the tooling and under the hood, uh, I assume you're, you're talking about TensorFlow
[1560.66 --> 1567.00]  there. Uh, what other tooling are you using? Uh, where are you using go of any, uh, love to know
[1567.00 --> 1568.80]  what, how you guys are putting the pieces together.
[1568.80 --> 1577.08]  Yeah. So, uh, the, the basic stack is in, in go. So we basically probably more than 80%
[1577.08 --> 1584.10]  of the code is, is go because more than 80% of the code is just APIs and network calls and,
[1584.10 --> 1590.86]  and this kind of things. And the machine learning models, uh, the training is, is done in Python
[1590.86 --> 1600.82]  and our, uh, favorite, uh, um, frameworks are Keras and TensorFlow. That's mostly what we use for deep
[1600.82 --> 1607.74]  learning. We use other ones like more traditional machine learning things like, uh, ball pump,
[1607.74 --> 1617.16]  BABIT is, is a, a really old C library that I quite like. Um, but, but basically that's it. This is not,
[1617.16 --> 1625.08]  not so much, much in learning code. We, we serve all the models in go, um, and train all the models
[1625.08 --> 1627.80]  in, in Python on even, even scripts.
[1628.34 --> 1633.74]  And, and just out of curiosity and maybe for, for the audience, why go for 80% of the stack? What,
[1633.74 --> 1639.94]  what is it about go? Because so many people in the AI space are, are doing Python. They're doing C++.
[1640.36 --> 1644.46]  You don't hear go as often. So I'd love to know why that for your selection.
[1645.44 --> 1654.32]  Yeah. So go has a deliberately limited language feature set. Um, I will, I once was speaking to a
[1654.32 --> 1659.62]  group and I said, you can't do that many things with go. And it got a laugh because I realized how
[1659.62 --> 1664.78]  it sounds, but what I meant was the actual language itself doesn't have that many features,
[1664.78 --> 1669.72]  which forces the code to therefore be simpler. You know, in some of the more modern languages with
[1669.72 --> 1675.18]  OO, you have big type inheritance. You've got all these language features that, that allow you to
[1675.18 --> 1681.74]  build really quite complicated, very clever and complicated things. The go philosophy is around
[1681.74 --> 1686.42]  simplicity, which mirrors exactly what we're, what we're doing at machine box. So it fits brilliantly.
[1686.42 --> 1693.34]  Essentially all of our code is, uh, a go code all kind of looks the same. So it's all familiar and
[1693.34 --> 1700.20]  you get such kind of benefits at, at development time, but actually more as you maintain the project,
[1700.28 --> 1705.54]  you know? Um, so that's why go wins, I think from our point of view, plus we're, we're fanboys of go.
[1705.62 --> 1712.38]  There's no denying that we met at a go conference. Um, you know, so much, yeah. But also some people
[1712.38 --> 1717.84]  are really surprised when they, they ask him, they may hear about matching box in a blog post or,
[1717.84 --> 1725.58]  or at a conference. Um, they contact us and say, Oh yeah, I like your product. Just out of curiosity,
[1725.58 --> 1732.46]  how many people are you? Um, well, it's just Matt and me development. Uh, we have some business side
[1732.46 --> 1736.72]  with, with, with Aaron, but it's just pretty much three, three people company right now.
[1737.08 --> 1744.34]  And the people get quite surprised like, Oh, you, you did so much. Um, you have so many boxes,
[1744.34 --> 1749.02]  so many products in, in like two people developing and one business developing.
[1749.42 --> 1756.40]  Yeah. And the answer isn't that we're awesome. Although David is, the answer is, uh, that we,
[1756.40 --> 1762.68]  we, we, we are very selective about where we, what we do. So we, we deliberately don't do as much as
[1762.68 --> 1768.02]  you could do. There's, there's loads of possible things that we could push into face box, for example.
[1768.22 --> 1773.04]  And some of them tell you where the eyebrows are. I haven't yet seen a good use case for why you need
[1773.04 --> 1778.38]  to know in an image where the eyebrows are, but maybe there is one, but until that, you know,
[1778.38 --> 1782.60]  until then we're not going to, we're not going to invest all that time and effort. And also,
[1782.60 --> 1788.70]  you know, add, add that kind of complexity to the API. So yeah, it's because we pick,
[1788.80 --> 1795.72]  we're very selective about what we do. We pick the things that we think are just the gold from the,
[1795.84 --> 1801.36]  all this potential kind of complexity. And, and we just sort of focus around telling that story and
[1801.36 --> 1806.78]  solving that problem. So that's how we're able to do so much. It seems, I think. Um, go, it's the
[1806.78 --> 1812.44]  perfect tool for our, our, our philosophies. Yes. It feels really well into that.
[1812.60 --> 1817.70]  Uh, mantra into that mindset. So, so it's, it's the perfect tool for us.
[1818.64 --> 1822.22]  I, I think both of you guys are awesome just to set the record straight.
[1822.22 --> 1825.92]  Thank you. I was, I was fishing for that. That's why I said it. Yeah.
[1826.04 --> 1832.72]  I'm glad you picked up on it. I figured you were. Um, and, uh, not only that, but you've given me my
[1832.72 --> 1838.20]  next blog post idea, which is around eyebrow, eyebrow based, uh, analysis. Very important stuff.
[1838.20 --> 1843.70]  Yeah. You can, you can detect sarcasm with it. That's the only use I think.
[1843.86 --> 1850.26]  Yeah. Matt, with you or maybe anger, Matt, with you, if you had that sarcasm detector,
[1850.36 --> 1855.62]  wouldn't it be pegged most of the time? Yeah, it would, uh, you can basically just return true.
[1855.92 --> 1856.24]  Okay.
[1856.24 --> 1856.58]  That's a shock.
[1856.92 --> 1860.46]  Yeah. That would be 99.9 accuracy.
[1860.46 --> 1865.36]  There was one time where I said something serious and wasn't being sarcastic, but I forget what it
[1865.36 --> 1865.78]  was now.
[1869.46 --> 1875.02]  So you, you've talked a lot about kind of your, your technology stack, why, why you've chosen go
[1875.02 --> 1881.12]  one thing I'm curious about. I mean, so I think everybody should use machine box in one way or
[1881.12 --> 1885.76]  another, but there's a lot of people out there maybe that are working on data science teams or
[1885.76 --> 1892.38]  data engineering teams or whatever it is and are, you know, maybe using TensorFlow to develop and
[1892.38 --> 1898.06]  train models that are getting deployed internally into their own sorts of services and products.
[1898.22 --> 1904.34]  I'm curious kind of, you know, because you consistently produce such high value, uh, models
[1904.34 --> 1909.54]  that are integrated in, into your products. Do you have any advice around kind of that progression
[1909.54 --> 1915.54]  from training, training your model to kind of getting it deployed within some type of service?
[1915.76 --> 1920.18]  Um, whether that be kind of, you mentioned testing, you know, testing might look differently
[1920.18 --> 1924.88]  for machine learning models or AI models than, than in other cases, but do you have any kind
[1924.88 --> 1930.88]  of advice and, and insights around that process from, you know, training your model to actually
[1930.88 --> 1936.18]  integrating it into a service, um, whether that's integrating machine box into your service,
[1936.18 --> 1939.96]  or maybe that's integrating your own model into your own internal service.
[1939.96 --> 1947.34]  Yeah. So I don't really know. So most of the problems are just technology that usually technology,
[1947.34 --> 1953.72]  you just get it solved with one way or another. So there are a lot of tools coming up these
[1953.72 --> 1959.00]  days that solve that problem. Well, including machine box, but also in TensorFlow, the deployment
[1959.00 --> 1967.02]  is getting better. So, but I think most important is people. So how this machine learning thing
[1967.02 --> 1974.28]  is transforming the way that people see software, especially talking with customers. Now we have,
[1974.28 --> 1978.14]  well, you know, in machine learning, we have a lot of false positives, false negatives.
[1979.26 --> 1985.36]  Once you have something in production, they come up with, with questions. Sometimes the most,
[1985.80 --> 1992.70]  the question that most of the customers are, so we have this problem. Well, that's not actually a
[1992.70 --> 1998.90]  problem. It's just a false positive. And there are ways to deal with false positives and false negatives.
[1999.38 --> 2005.82]  And changing the mindset to accept that a thing is not a bug, it's a, it's a false positive in a
[2005.82 --> 2011.66]  machine learning model. It changed the way that you interact with people. It's like, oh, you're not
[2011.66 --> 2017.98]  going to have a machine learning that is 100% accurate. So you have to deal with these situations.
[2017.98 --> 2025.48]  And that situation is just you, the way that we are mostly struggling or just trying to get the
[2025.48 --> 2032.48]  right conversations with people. And I think that is going to come up in any software development in
[2032.48 --> 2038.76]  the next couple of years. Like, yeah, our job, one of our big challenges is communicating what's
[2038.76 --> 2044.32]  actually going on. Like, you know, we thought we're just going to deliver face recognition APIs,
[2044.32 --> 2051.10]  that's it, or image recognition, image classification or personalization APIs. And we found
[2051.10 --> 2055.66]  that quite quickly, we did, we did actually have to get into the conversation a bit more about,
[2056.14 --> 2064.54]  look, this, we don't expect this to get everything right 100% of the time, we, we expect it to do a
[2064.54 --> 2069.70]  much better job automatically than than you're doing. Hopefully, you can get it to the point where,
[2069.82 --> 2073.38]  you know, the exceptions that you have to deal with, if there are any in the workflow,
[2073.38 --> 2078.70]  get smaller and smaller. But yeah, that's definitely been something we've had to focus on is,
[2078.84 --> 2085.60]  is communicating that this is a kind of, unlike other software, where you do something and you
[2085.60 --> 2090.16]  get a result you don't like, that's a bug. And we've had some bugs opened where it says,
[2090.16 --> 2094.82]  I put this image in, and it didn't find the face, you know, and of course, the image,
[2095.02 --> 2099.62]  the face is like turned to the side, or it's got a weird shadow on it, or just something is weird
[2099.62 --> 2105.66]  about it. And then we kind of get into that conversation. It's well, it isn't really a bug.
[2105.66 --> 2110.12]  I mean, you know, it's kind of part of the expected workflow. The question is,
[2110.42 --> 2116.30]  how do we then tackle that going forward? From a data scientist's point of view, someone did actually
[2116.30 --> 2123.16]  ask if they could put their models into our boxes, because they knew the the building the models bit,
[2123.24 --> 2127.70]  they were good at that, but they had no idea about getting things into production and running them
[2127.70 --> 2134.64]  at scale. One of the things one of the very early kind of rules that we gave ourselves, and this
[2134.64 --> 2139.90]  comes, this is kind of common sense now, I think a little bit, but comes from David's experience
[2139.90 --> 2145.70]  building a massive scale for the Olympics in particular, was that we had, you know, we had
[2145.70 --> 2151.50]  to be able to horizontally scale the boxes just by adding more of them, you know, because scale is,
[2151.74 --> 2156.36]  you know, it's fine if you get this awesome technology, and it works nice and slow on one machine.
[2156.36 --> 2162.44]  But to really get the value from it, in most cases, you want to run this thing at scale,
[2162.44 --> 2169.04]  so that it can really, you know, get through work that it needs to get through. And so we did,
[2169.18 --> 2173.50]  we spent a lot of time also, which you don't really see apart from the fact that it just works. But
[2173.50 --> 2179.20]  we spent a lot of time in making sure that this, these boxes could horizontally scale in a kind of
[2179.20 --> 2184.56]  Kubernetes environment where it was just elastic up and down as you needed. And of course, you have to
[2184.56 --> 2189.66]  think about what's the state inside the box, how does that work? And various other sort of,
[2189.90 --> 2195.42]  you know, we'll just load balancing across the boxes be enough, you know, to get what you want?
[2195.92 --> 2199.64]  Or is there more that we need to do? And where does that happen? And all those kinds of things. So
[2199.64 --> 2204.40]  yeah, it's been a great, it's been a great sort of experience building it. And it's even,
[2204.56 --> 2209.12]  it's more fun when people start integrating it and paying for it. That's, that's when you really feel
[2209.12 --> 2214.24]  like you've created something valuable. Yeah, that's, that's great. And I can definitely
[2214.24 --> 2220.32]  resonate with, with some of the things you said around kind of exceptions in models and that sort
[2220.32 --> 2226.70]  of thing. I think people too often, in my personal opinion, you know, think about an end to end machine
[2226.70 --> 2231.82]  learning or AI model that does everything all the time correctly. And I think that's, you know,
[2231.84 --> 2237.34]  to some degree, the wrong thought in a lot of cases, because, you know, when machine learning models
[2237.34 --> 2241.92]  fail, it's the same, you know, we, we have an opportunity to refactor them, right, which is,
[2242.02 --> 2248.62]  is in the end, a good thing, right? So just to kind of, you know, getting getting close to the
[2248.62 --> 2253.26]  end here, I was wondering, you know, again, what what you guys are doing is kind of setting some
[2253.26 --> 2258.40]  some standards as far as interacting with machine learning models. And so I'd love to get more more
[2258.40 --> 2265.52]  advice from you guys, in terms of the, like the skills that data engineers, or just kind of
[2265.52 --> 2271.72]  developers who don't really consider themselves data scientists or AI researchers, what sort of
[2271.72 --> 2278.34]  skills would you kind of recommend them, you know, looking into or what kind of skills do they need
[2278.34 --> 2283.40]  to begin to start integrating machine learning into their, into their applications?
[2284.04 --> 2289.68]  I think that I don't think you need that many depends how deep you want to go into it.
[2289.80 --> 2294.36]  The trajectory that I would recommend to somebody who didn't have any kind of idea about it
[2294.36 --> 2301.06]  would be to start by consuming APIs. And, and because if, if those if, if that's good enough,
[2301.06 --> 2306.46]  if that works for your case, then you don't have to do anything more. And that's what we've found so
[2306.46 --> 2312.68]  far. A lot of our customers have said, you know, we're just gonna, we're just gonna kind of try this,
[2312.68 --> 2317.50]  because then we can build MVP quickly. And then later, we might change it. And then that later never
[2317.50 --> 2322.44]  happens, because the, you know, the boxes are doing just such a good job that they don't need to then
[2322.44 --> 2329.60]  change it. So definitely, like, any kind of API skill around consuming APIs, you know, most people
[2329.60 --> 2335.50]  already have those already. And then I think, beyond that, it's really just a question of, I think,
[2335.62 --> 2341.82]  understanding a little bit more about just the kind of high level concepts, I would say would be useful,
[2341.82 --> 2351.34]  like, you know, with with with classification box, with classification box, you can create your own
[2351.34 --> 2357.24]  classifier with with training, a training set. Now with classification box, you do need a good amount
[2357.24 --> 2364.38]  of examples for each class. So, you know, if you when some people start using it, they have just a couple
[2364.38 --> 2369.80]  of images, a couple of examples, and you can't really get a model that's, that's useful from from
[2369.80 --> 2376.62]  that. So learning things like the sort of softer skills around machine learning, I guess, which is, you
[2376.62 --> 2382.50]  know, the kinds of data, the kinds of problems that machine learning is good at, first of all, then what
[2382.50 --> 2387.46]  kind of training data are you going to have? Because machine learning is only as bad as its training data.
[2388.24 --> 2394.52]  So I think those sorts of things would be the useful for everyone to have. And then if if you're getting
[2394.52 --> 2400.46]  into more machine learning technical stuff, then, then I don't know. Yeah, so in my opinion, you should
[2400.46 --> 2406.22]  focus in one type of problem. So the machine learning is quite broad. So if you want to get a
[2406.22 --> 2412.50]  starter, there are many different sub fields. So probably just focus in a problem that you have,
[2412.50 --> 2418.90]  or you want to solve, like, I don't know, sentiment analysis, or classifying text, or something
[2418.90 --> 2427.68]  more or less straightforward, or in machine learning work, more or less easy, and learning by doing it
[2427.68 --> 2437.14]  instead of focusing in maths or, or things like that, you can get easily losing in that sense. So try
[2437.14 --> 2444.74]  to solve, try to learn by doing, solve a problem that you have, and, and see how it goes. Once you have
[2444.74 --> 2450.22]  that working, you, you have that boost of energy, just, oh, I have something that is more or less
[2450.22 --> 2455.00]  working. Maybe it's not, it's not the state of the art, it's not very accurate, but it's better than
[2455.00 --> 2460.14]  random. So it's, it's the much, the machine is actually learning. And, and that's, it's a good
[2460.14 --> 2466.94]  feeling. I'm probably just, just that is, is good to, to get started and get more curiosity and learn
[2466.94 --> 2472.68]  more, more, more things. That sounds great. So let me ask one last question for you as we wind up.
[2472.68 --> 2478.96]  So many of the listeners that we have are, are trying to figure out how to get into machine
[2478.96 --> 2484.18]  learning themselves. And they might be software developers. They might be business people who
[2484.18 --> 2490.98]  are intrigued by, by what's possible here. And so as, as two entrepreneurs who have gone down this
[2490.98 --> 2497.78]  road and you have created a business based on, on making AI technologies available and, and recognizing
[2497.78 --> 2502.50]  there's so many people that may want to, to either supplement their own business that they have,
[2502.50 --> 2506.98]  or, or create a new business. What, what advice do you have for other entrepreneurs that,
[2507.10 --> 2511.28]  that might be interested in, in taking the same adventure that you guys are, are now,
[2511.48 --> 2514.96]  you know, a couple of years down, what, what would you say to them?
[2515.68 --> 2521.80]  Yeah, I would always say, um, solve a specific problem. Make sure you're solving a real problem.
[2521.88 --> 2527.44]  This goes for any kind of software actually, but it's too, especially machine learning,
[2527.44 --> 2532.84]  because it's all cool and sexy and, and hard. Like machine learning is hard. So anyone that,
[2533.54 --> 2538.90]  like David said, if you make some ground, you really, you get really kind of big rewards for
[2538.90 --> 2545.50]  doing that. Like just emotional rewards you get. So yeah, it's kind of, uh, difficult to
[2545.50 --> 2551.48]  make sure that you're building something that has some true value. Um, you know, because if you're just
[2551.48 --> 2556.62]  building cool tech, then there's no guarantee that's ever going to be anything. And often,
[2557.08 --> 2562.20]  often you can build, you end up building something that technically is brilliant,
[2562.20 --> 2570.62]  but actually doesn't quite fit the problem. And then you have to basically move or change what
[2570.62 --> 2575.32]  you're doing so that it does solve a real problem. And that can be quite a painful transition.
[2575.72 --> 2580.56]  Usually involves adding loads of complexity because it didn't quite, you, you weren't really thinking
[2580.56 --> 2585.24]  about those things from the beginning. So of course you want to be able to evolve and learn and move,
[2585.36 --> 2592.50]  you know, a project along, but I would say start with a real problem that you understand. And the
[2592.50 --> 2596.86]  problem shouldn't be anything to do with machine learning, but machine learning might be part of
[2596.86 --> 2603.00]  the solution. Great. Yeah, that's a, that's wonderful advice. And we'll include links of course,
[2603.00 --> 2607.90]  to machine box and other things that we've talked about, you know, TensorFlow and Keras and, uh,
[2607.90 --> 2611.76]  Docker and Kubernetes. If you're not familiar with those technologies, we'll include some,
[2612.16 --> 2617.76]  some good links to getting started with those and learning more. And just want to want to thank
[2617.76 --> 2622.84]  David and Matt one more time for joining us. It's been, been great to have you here and really excited
[2622.84 --> 2627.44]  about what's going on with machine box. Thank you very much. Yeah. And good luck with the podcast.
[2627.44 --> 2633.42]  Um, I think it's awesome. I can't wait for future episodes. I'm sorry to everyone who had to listen
[2633.42 --> 2638.98]  to our voices for this episode, but future ones I'm sure will be even more interesting. Yeah.
[2639.36 --> 2643.30]  Thank you very much. Thank you. Thank you. Appreciate it very much.
[2645.18 --> 2649.84]  All right. Thank you for tuning into this episode of Practical AI. If you enjoyed this show, do us a
[2649.84 --> 2654.86]  favor, go on iTunes, give us a rating, go in your podcast app and favorite it. If you are on Twitter or
[2654.86 --> 2658.14]  social network, share a link with a friend, whatever you got to do, share the show with a
[2658.14 --> 2662.62]  friend. If you enjoyed it and bandwidth for change log is provided by fastly learn more at
[2662.62 --> 2666.94]  facet.com and we catch our errors before our users do here at change law because of roll bar,
[2666.94 --> 2672.82]  check them out at robot.com slash change log. And we're hosted on Linode cloud servers at a
[2672.82 --> 2678.06]  lino.com slash change log. Check them out, support this show. This episode is hosted by Daniel
[2678.06 --> 2683.50]  Whitenack and Chris Benson. Editing is done by Tim Smith. The music is by Breakmaster cylinder,
[2683.50 --> 2688.74]  and you can find more shows just like this at change law.com. When you go there, pop in your
[2688.74 --> 2693.24]  email address, get our weekly email, keeping you up to date with the news and podcasts for
[2693.24 --> 2697.94]  developers in your inbox every single week. Thanks for tuning in. We'll see you next week.
