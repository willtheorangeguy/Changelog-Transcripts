[0.00 --> 4.82]  After about a year, maybe two years of that, a few of the people that we had been working
[4.82 --> 9.12]  with internally at NVIDIA, our subject matter experts who are constantly going out and engaging
[9.12 --> 12.72]  with customers and helping them solve their challenging problems, came to us and said,
[12.78 --> 14.82]  hey, there's this thing called deep learning.
[15.00 --> 15.92]  It's kind of interesting.
[16.16 --> 19.66]  And we built these little like Jupyter notebooks that kind of show people how to do it.
[19.66 --> 24.44]  Could we just maybe host that on your training platform and see if people want to learn how
[24.44 --> 25.24]  to do this thing?
[26.22 --> 26.90]  Within a very...
[26.90 --> 28.56]  How far we've come, right?
[29.32 --> 29.80]  Yeah.
[29.80 --> 35.40]  Within a very short amount of time, the number of people who signed up for an account and
[35.40 --> 40.50]  logged in and experienced this deep learning training completely eclipsed anything else
[40.50 --> 41.20]  we had done before.
[41.30 --> 44.28]  And we realized that we had a tiger by the tail on that.
[44.42 --> 45.60]  We'd been experimenting.
[45.80 --> 46.84]  We'd been trying things.
[47.06 --> 47.82]  Something worked.
[47.82 --> 49.74]  That's when we decided to double down.
[52.08 --> 54.50]  Bandwidth for ChangeLog is provided by Fastly.
[54.86 --> 56.78]  Learn more at Fastly.com.
[56.78 --> 60.08]  We move fast and fix things here at ChangeLog because of Rollbar.
[60.22 --> 61.88]  Check them out at Rollbar.com.
[62.10 --> 64.32]  And we're hosted on Linode cloud servers.
[64.66 --> 66.66]  Head to linode.com slash ChangeLog.
[66.66 --> 69.56]  This episode is brought to you by DigitalOcean.
[70.26 --> 70.58]  Droplets.
[70.92 --> 71.68]  Managed Kubernetes.
[72.04 --> 72.90]  Managed databases.
[73.54 --> 74.02]  Spaces.
[74.26 --> 75.14]  Object storage.
[75.42 --> 76.68]  Volume block storage.
[76.94 --> 80.40]  Advanced networking like virtual private clouds and cloud firewalls.
[80.62 --> 85.98]  Developer tooling like the robust API and CLI to make sure you can interact with your infrastructure
[85.98 --> 86.86]  the way you want to.
[87.26 --> 90.78]  DigitalOcean is designed for developers and built for businesses.
[90.78 --> 97.86]  Join over 150,000 businesses that develop, manage, and scale their applications with DigitalOcean.
[98.20 --> 101.62]  Head to do.co slash ChangeLog to get started with a $100 credit.
[101.96 --> 104.10]  Again, do.co slash ChangeLog.
[104.10 --> 128.42]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive,
[128.84 --> 129.76]  and accessible to everyone.
[129.76 --> 134.18]  This is where conversations around AI, machine learning, and data science happen.
[134.60 --> 138.64]  Join the community and Slack with us around various topics of the show at ChangeLog.com
[138.64 --> 140.52]  slash community and follow us on Twitter.
[140.66 --> 142.24]  We're at Practical AI FM.
[148.90 --> 151.94]  Welcome to another episode of the Practical AI podcast.
[152.36 --> 157.74]  We are the show that tries to make AI practical, productive, and accessible to everyone.
[158.06 --> 159.32]  My name is Chris Benson.
[159.32 --> 162.82]  I'm a principal emerging tech strategist at Lockheed Martin.
[163.14 --> 168.20]  And with me, as always, is Daniel Whitenack, who is a data scientist with SIL International.
[168.32 --> 169.18]  How's it going today, Daniel?
[169.50 --> 170.80]  It's going really well, Chris.
[171.22 --> 174.74]  It's been a busy week so far, but fairly productive.
[174.96 --> 175.60]  How about yourself?
[175.90 --> 177.18]  It's been a fun week for me.
[177.26 --> 179.10]  I just hit my 50th birthday.
[180.30 --> 181.92]  Ah, happy birthday.
[182.20 --> 182.72]  Thank you.
[182.76 --> 183.46]  It was a big one.
[183.52 --> 184.62]  I was pretty happy with it.
[184.70 --> 184.94]  Yeah.
[185.00 --> 189.10]  I don't get into the whole crying over your birthday thing, so I'm having fun.
[190.08 --> 190.72]  That's good.
[190.86 --> 193.74]  I'm trying to extend it for the entire month in every possible way.
[193.90 --> 194.96]  So good times.
[195.10 --> 195.42]  Right.
[195.60 --> 196.34]  Yeah, that's good.
[196.38 --> 200.34]  Do you have a party or any fun over the weekend?
[200.80 --> 202.78]  We are scheduling all sorts of fun stuff.
[202.92 --> 204.82]  We're just trying to do some good family stuff.
[205.04 --> 207.42]  Stay safe with COVID the way it is.
[207.60 --> 208.48]  And good times.
[208.72 --> 209.34]  Yeah, awesome.
[209.34 --> 213.20]  And it's been a pretty eventful week as well on the AI front.
[213.34 --> 218.64]  I'm sure you saw, as I did, a pretty large acquisition that's looking like it's going
[218.64 --> 220.34]  to happen between NVIDIA and ARM.
[220.50 --> 221.56]  So that's pretty cool stuff.
[221.90 --> 221.98]  Yeah.
[222.04 --> 227.84]  If it gets through, $40 billion acquisition, which is obviously big news.
[227.96 --> 232.64]  But I mean, really, anything NVIDIA does is big news, as we have proven time and time
[232.64 --> 232.92]  again.
[233.00 --> 234.12]  We're always talking about NVIDIA.
[234.12 --> 240.14]  And speaking of NVIDIA, we have a guest that I know both of us have really wanted on the
[240.14 --> 241.24]  show for a while now.
[241.36 --> 246.28]  With us today is Will Ramey, who is the Global Head of Developer Programs at NVIDIA.
[246.76 --> 247.62]  Welcome to the show, Will.
[248.14 --> 249.16]  Thank you for having me.
[249.52 --> 256.10]  So wondering, I know you and I have met previously at GTC and had conversations, and you have an
[256.10 --> 260.20]  interesting background in terms of how I know you run the Deep Learning Institute.
[260.20 --> 264.84]  I was wondering if, before we dive into all the cool stuff, if you could just tell us
[264.84 --> 269.34]  kind of how you got to where you are now in NVIDIA and in the particular position.
[269.64 --> 271.14]  And you guys do some amazing work.
[271.26 --> 272.92]  So I'm really looking forward to hearing this.
[273.32 --> 273.48]  Wow.
[273.58 --> 273.74]  Yeah.
[273.88 --> 277.14]  Let me see if I can summarize the short version of it.
[277.46 --> 282.80]  I got an undergraduate degree in computer science and worked as a software engineer in Silicon
[282.80 --> 288.64]  Valley for many years for starting with Silicon Graphics and then a number of startups,
[288.64 --> 290.72]  including a game studio.
[291.62 --> 297.70]  And during that time, I transitioned from working as a software engineer to a product manager
[297.70 --> 301.10]  and a producer and a general manager in the games industry.
[301.46 --> 307.74]  And then some friends of mine invited me down to join this scrappy little company called NVIDIA
[307.74 --> 315.04]  that was just, you know, really ferociously competing in the video game industry back then.
[315.04 --> 317.74]  And I accepted their offer.
[318.02 --> 319.86]  And that was 17 years ago.
[320.24 --> 320.70]  Holy cow.
[321.10 --> 324.82]  A little bit of change happening during that time at NVIDIA, I would imagine.
[325.26 --> 330.60]  It's been a wild ride, both, you know, for me personally and for the company over the
[330.60 --> 337.40]  last coming up on two decades here, where when I joined the company, we were viewed as a chip
[337.40 --> 338.34]  company, right?
[338.34 --> 339.46]  We designed chips.
[339.54 --> 340.76]  That's kind of our business.
[341.48 --> 347.18]  And I had the opportunity to work as the product manager for some of our developer tools and
[347.18 --> 352.64]  then do some program management of large software projects we were working on with Microsoft
[352.64 --> 356.26]  and others and work a little bit in our embedded business.
[356.26 --> 365.36]  And slowly but surely, the company started to climb up the value chain from chips to boards
[365.36 --> 368.70]  and embedded systems, kind of system level products.
[369.00 --> 374.60]  And then in 2009, we introduced this new technology called CUDA.
[375.54 --> 381.80]  And CUDA, as, you know, many people know and love it today, is a parallel computing platform
[381.80 --> 389.08]  that gives developers access to the parallel computing power, the accelerated parallelism
[389.08 --> 391.32]  of NVIDIA's GPU processors.
[392.28 --> 394.08]  And that was exciting, right?
[394.22 --> 399.38]  And scientists, researchers were starting to figure out new and innovative ways to take
[399.38 --> 401.74]  advantage of this computing capability.
[402.12 --> 405.78]  And I moved into a role as the product manager for CUDA.
[406.30 --> 410.86]  So, you know, introducing this new technology, talking with people who were trying to make sense
[410.86 --> 413.38]  of it and apply it to some of their most challenging problems.
[414.34 --> 418.76]  And that gave us the opportunity to go and really start working with people who we had
[418.76 --> 424.96]  never worked with before, you know, working with Fortran programmers, working on like climate
[424.96 --> 429.64]  and weather simulations, working with people in the energy industry, trying to figure out
[429.64 --> 432.22]  what is the subsurface of the earth look like.
[432.44 --> 437.00]  People who are working at the very smallest scales of physics, trying to figure out molecular
[437.00 --> 440.72]  dynamics and how things work at the quantum levels.
[440.88 --> 443.22]  Really big, sophisticated simulations.
[443.84 --> 443.96]  Yeah.
[444.02 --> 449.52]  In the beginning days of CUDA there, it sounds like the focus was a lot on like scientific
[449.52 --> 454.50]  computing, like materials modeling, more on the like scientific computing side.
[454.74 --> 457.76]  Was AI even in the mix at that point?
[458.30 --> 459.08]  Not at all.
[459.22 --> 465.46]  In fact, one of the most common questions we got was, wait, why should I use gaming technology
[465.46 --> 466.80]  to do real science?
[467.30 --> 467.46]  Yeah.
[467.52 --> 471.42]  And it seems kind of like just a strange question these days where some of the most important
[471.42 --> 478.16]  scientific challenges of our time are being addressed using not only this gaming technology,
[478.16 --> 482.32]  but what has grown into a more general purpose parallel computing platform.
[482.76 --> 490.40]  The application of this parallel computing technology to AI happened several years later.
[490.40 --> 496.52]  And it really came again from the research sector where there were a small number of researchers
[496.52 --> 504.84]  who had somehow managed to maintain funding and were exploring this area of deep neural networks
[504.84 --> 507.32]  and what we have come to call deep learning.
[508.12 --> 515.36]  And they were building what at the time seemed to be really large, complicated neural networks
[515.36 --> 519.62]  that had very simple amounts of processing in each node.
[519.62 --> 524.34]  And this was a very different approach from what had been done previously in other machine
[524.34 --> 531.34]  learning techniques and using really, really large amounts of data to train and fine tune
[531.34 --> 537.42]  these neural network models to perform various tasks initially in computer vision.
[537.52 --> 541.86]  So things like image classification and object detection and segmentation and things like that.
[541.86 --> 553.66]  And what they discovered was somewhat surprising in that these GPU parallel processors were almost ideally suited
[553.66 --> 564.66]  for accelerating the work of training these neural network models to perform a wide variety of tasks.
[564.66 --> 572.52]  And that was really the genesis of the deep learning AI revolution that we're all witnessing today.
[573.30 --> 578.84]  And I'm kind of curious, you know, because it sounds like, you know,
[578.96 --> 585.28]  this realization came from the research community initially when they started thinking more about
[585.28 --> 590.48]  accelerating these AI workflows on the GPUs or the graphics cards.
[590.48 --> 598.40]  So at what point did you sort of begin to see a shift into like sort of real world industry applications
[598.40 --> 605.96]  where industry people started, you know, really expressing this desire for GPU accelerated machines
[605.96 --> 611.54]  and that sort of thing, you know, out of research and into the industry world?
[612.16 --> 613.10]  Yeah, that's a great question.
[613.22 --> 614.66]  It happened in a couple of phases.
[614.66 --> 623.86]  And in some ways, we're all very fortunate that those initial researchers decided to publish
[623.86 --> 630.32]  not only their results in research papers, but they published the software that they used
[630.32 --> 635.32]  to train the deep neural network models, the things that we call deep learning frameworks today.
[635.88 --> 642.24]  You know, one of the early ones, there was CAFE and Torch, now PyTorch, TensorFlow, MXNet.
[642.24 --> 644.84]  You know, there are some called Paddle Paddle.
[645.50 --> 651.72]  And these frameworks being available in the open source community, but really just being available at all,
[652.22 --> 656.50]  allowed all of us to start to experiment with them.
[657.12 --> 660.70]  And what we observed happening was that very early on in the process,
[660.88 --> 667.38]  the cloud service providers who had adopted GPUs into their offerings
[667.38 --> 675.70]  very quickly recognized that this deep learning technology was going to be not only valuable to their own businesses,
[676.12 --> 683.28]  but a valuable new type of workload that allowed them to offer more compute services to their customers
[683.28 --> 685.22]  and grow their cloud computing business.
[685.22 --> 694.44]  And so you saw new types of instances, new types of servers being offered by the cloud service providers
[694.44 --> 701.06]  and pre-packaged virtual machine images, basically the operating system and all the software that you run
[701.06 --> 706.58]  on the servers on the cloud service provider platforms, pre-packaged and ready to go.
[706.58 --> 712.80]  All you had to do was, you know, click a few buttons and you had a server with GPUs and all the software you needed
[712.80 --> 716.44]  ready to start running and training your models on your data.
[717.10 --> 725.00]  So that lit a fire, really, especially in the startup community, where up until then,
[725.56 --> 730.20]  the cost of, you know, buying your own data center and getting everything set up
[730.20 --> 733.34]  was pretty prohibitive to small startups.
[733.76 --> 738.06]  Now they could just very quickly rent all of the compute capability they needed
[738.06 --> 743.72]  and most of the software was already set up for them to start exploring all the innovative ideas
[743.72 --> 747.86]  that startups come up with every time a new technology is released.
[748.60 --> 757.22]  And we also, in that timeframe, saw a number of, let's say, forward-thinking enterprise organizations
[757.22 --> 763.28]  and government agencies began to take advantage of these capabilities,
[763.28 --> 770.98]  where they saw there was a good business opportunity either to improve their own internal business operations
[770.98 --> 777.94]  and practices or to build new and enhanced products that allowed them to provide better experiences,
[778.16 --> 779.86]  better services to their customers.
[781.14 --> 786.78]  And now what we're seeing is really beyond, it's sort of crossed the chasm, if you will,
[787.22 --> 791.90]  to the point where the leading, the early adopters have already proven out the technology
[791.90 --> 798.62]  and everyone is just racing to figure out how to apply it practically to improving their products,
[798.72 --> 804.48]  their services, their business operations, and just other aspects of their challenging problems
[804.48 --> 805.94]  that this technology can address.
[806.86 --> 812.72]  So before we dive fully kind of into the AI, you know, powerhouse that NVIDIA is today,
[812.72 --> 817.28]  I'm kind of curious, you know, referring back to those early days when you started,
[817.28 --> 823.32]  and, you know, we really thought of NVIDIA as is that graphics company, graphics cards,
[823.52 --> 828.30]  and, you know, anytime in gaming and anytime we were thinking along those lines, that was the name.
[828.52 --> 832.94]  And you made this remarkable transition as an organization into being, you know,
[833.02 --> 837.86]  one of the dominant AI companies and on the hardware side, the dominant AI company.
[837.86 --> 839.98]  And that's a huge cultural shift.
[840.12 --> 844.50]  And I'm just curious, as someone who lived through that, that very successful shift that you made,
[844.76 --> 848.08]  how did the company do that when so many other organizations that do something similar
[848.08 --> 849.92]  tend to fall down on their face?
[850.46 --> 858.18]  Well, you know, I have to give our leadership a lot of credit here for having a very strong vision
[858.18 --> 865.98]  and a conviction that we were headed in a direction to be more valuable to the world.
[866.72 --> 871.02]  But at the same time, taking measured steps, right?
[871.14 --> 877.58]  Small measured steps each year, each quarter that allowed us to experiment and to learn quickly
[877.58 --> 883.98]  and to test what worked and what the various markets, what our customers were ready for.
[883.98 --> 892.90]  And through that process of continuous experimentation and innovation and proving out our hypotheses as we went,
[893.38 --> 899.96]  we were able to find our way into providing not just the technology,
[900.74 --> 909.38]  but the business models, the training, the support and resources that developers, researchers, data scientists,
[909.38 --> 919.38]  this emerging class of DevOps engineers who are proving to be so crucial in connecting the work that happens
[919.38 --> 924.58]  in the engineering and development teams with the IT deployment and operational teams.
[925.16 --> 932.16]  Just learning as we go and really investing in this ecosystem of developers
[932.16 --> 937.58]  and people who can use the technologies that we're creating to solve their problems
[937.58 --> 941.50]  is what my experience was kind of along the way.
[942.06 --> 942.18]  Yeah.
[942.32 --> 946.80]  And maybe to just kind of set the stage for where we're at now.
[946.92 --> 953.56]  So you mentioned a lot of different, you know, stakeholders there and involve parties from developers to DevOps and all of that.
[953.56 --> 964.70]  And I know, of course, people might think of NVIDIA as like the actual GPU cards and servers and these other things.
[965.12 --> 970.52]  But could you just kind of give us a very, you know, I know it's hard to not leave anything out,
[970.60 --> 977.12]  but just kind of a brief sketch of the different, you know, types of things that NVIDIA is offering the AI community.
[977.30 --> 980.16]  So there's the hardware side of things, but then there's other things as well.
[980.16 --> 990.00]  Like one of the things I use fairly frequently is the NGC containers that are fairly, like really easy to use, like optimized.
[990.20 --> 996.80]  So maybe you could just give a sketch of some of these other things that people might not be as aware of
[996.80 --> 999.04]  that NVIDIA is kind of offering the community.
[999.52 --> 1000.02]  Sure, sure.
[1000.14 --> 1003.62]  So it's a really long list, but maybe I can just pick a couple of the highlights.
[1003.82 --> 1004.38]  Yeah, yeah.
[1004.52 --> 1005.76]  I just highlight a few.
[1005.94 --> 1007.36]  There's a bunch, but.
[1007.36 --> 1020.14]  So in addition to, you know, the GPU hardware itself and now the networking hardware with the acquisition of Mellanox and Cumulus
[1020.14 --> 1022.36]  are bringing them into the NVIDIA family.
[1022.88 --> 1031.02]  And then the systems, the HGX system designs that we've designed and worked with lots of our OEM partners
[1031.02 --> 1033.10]  to build and put into the market.
[1033.66 --> 1038.88]  And of course, the DGX product line, the workstations and the servers and the pods,
[1039.60 --> 1043.34]  the kind of data center scale computing solutions that we offer.
[1043.34 --> 1054.26]  There's a really, really rich collection of software, some of which we contribute to as open source projects.
[1054.26 --> 1058.86]  So whether it's PyTorch or TensorFlow or any of the other leading deep learning frameworks,
[1058.86 --> 1069.02]  we have teams of engineers who are working on contributing to those projects to help them take best advantage of GPU acceleration directly,
[1069.26 --> 1073.50]  and then also take advantage of things like our TensorRT.
[1073.78 --> 1077.98]  This is the deep learning model compiler and runtime environment.
[1077.98 --> 1084.06]  So that once your deep learning model is trained, you know, in the same way that we as humans,
[1084.14 --> 1087.84]  we kind of put a lot of energy into training, you know, training ourselves and learning a new thing.
[1087.90 --> 1090.42]  But once we've learned it, we kind of have like the mental shortcut.
[1091.02 --> 1092.44]  You know, let's say you were learning to juggle.
[1092.70 --> 1098.80]  It takes a lot more effort to learn how to juggle than it does to actually juggle after you've learned how to do it.
[1099.06 --> 1103.10]  And it's the same thing for playing tennis or playing piano or anything like that.
[1103.42 --> 1104.48]  Same thing for deep learning.
[1104.48 --> 1113.14]  Once you've trained the neural network model, it turns out that it can be optimized and run at much faster performance
[1113.14 --> 1118.96]  in an inference deployment environment or at lower energy profile, depending on what your needs are.
[1119.38 --> 1121.66]  And this TensorRT runtime is able to help with that.
[1122.12 --> 1127.00]  But there are also higher level tools and resources like NGC.
[1127.00 --> 1139.20]  The NGC catalog provides both containers with all kinds of accelerated computing and deep learning and data science software environments
[1139.20 --> 1145.12]  that are pre-tested, pre-configured, ready to go, can be deployed in your own servers
[1145.12 --> 1151.74]  and your embedded Jetson-based platforms or on cloud service provider platforms.
[1151.74 --> 1155.94]  And also includes things like model recipes.
[1156.54 --> 1158.32]  So maybe you don't want the entire environment.
[1158.48 --> 1165.90]  You just want some deep learning models that are known to be good and a recipe for how to use that to train it with data and things like that.
[1166.06 --> 1168.46]  So NGC provides a number of those things as well.
[1168.46 --> 1182.98]  And then there are even higher level services on top of that that work with our EGX solutions that are kind of combined cloud or on-premises with Internet of Things.
[1182.98 --> 1193.88]  So say you're a city and you want to build a smart city type environment to be able to keep track of how many of which types of vehicles are running on your road
[1193.88 --> 1201.50]  so you can do predictive maintenance before potholes show up or figure out where the safe and less safe traffic patterns are
[1201.50 --> 1205.62]  so you can put in better crosswalks or change the timing of your stoplights and things like that.
[1205.62 --> 1213.38]  You might have hundreds or thousands of cameras and you need to be able to do analytics on those video feeds that are coming into the system.
[1213.70 --> 1219.20]  This is the kind of thing that these EGX scalable systems are able to handle.
[1235.62 --> 1242.40]  Changelog++ is the best way for you to directly support practical AI.
[1242.94 --> 1247.18]  Join today and unlock access to a private feed that makes the ads disappear,
[1247.62 --> 1253.32]  gets you closer to the metal, and helps sustain our production of practical AI into the future.
[1254.00 --> 1262.40]  Simply follow the Changelog++ link in your show notes or point your favorite web browser to changelog.com slash plus plus.
[1262.40 --> 1266.64]  Once again, that's changelog.com slash plus plus.
[1268.02 --> 1270.34]  Changelog++ is better.
[1281.60 --> 1288.48]  So given that we are just about to head into GTC, the GPU Technology Conference,
[1288.48 --> 1293.10]  I know there's all sorts of announcements and stuff and you guys are going to release new stuff coming up.
[1293.44 --> 1296.22]  Obviously, the thing on everyone's mind is ARM.
[1296.58 --> 1303.46]  I was wondering if you could tell us a little bit about what GTC is for those who may not have had the opportunity to attend already.
[1303.76 --> 1310.40]  And also, I imagine it's a little bit early, but if there is anything that you can address with the ARM acquisition, we'd love to hear it.
[1310.96 --> 1311.48]  Sure. Okay.
[1311.48 --> 1315.74]  Let's take those one at a time and we can start with GTC.
[1315.98 --> 1321.10]  You know, the GPU Technology Conference or GTC is something that's really near and dear to my heart.
[1321.28 --> 1324.88]  We organized the first one a little over 10 years ago,
[1324.88 --> 1331.16]  and it has grown and evolved with our ecosystem of developers and researchers and data scientists
[1331.16 --> 1336.02]  and everyone else who's learning and exploring how to apply the new technology.
[1336.02 --> 1346.42]  This year, with the COVID-19 virus, we transformed GTC into an online experience.
[1347.30 --> 1352.60]  And over 60,000 people joined us earlier this year for the very first one.
[1353.46 --> 1361.90]  In just a couple weeks, we're going to be doing what we call GTC Fall, the next installment of GTC.
[1361.90 --> 1369.16]  And it'll have all of the usual elements that people have become familiar with in the GTC conference.
[1369.30 --> 1373.94]  We'll have a keynote by Jensen Wong, our president and co-founder.
[1374.38 --> 1379.62]  He'll be kicking things off on Monday, Monday morning, October 5th.
[1379.62 --> 1389.08]  But we'll also have just hundreds and hundreds, I think it's something like over 600 live and pre-recorded sessions
[1389.08 --> 1396.60]  available this year, talking about all of the amazing work that is happening out in the ecosystem.
[1396.80 --> 1402.48]  Some of the talks are by NVIDIA engineers and experts and product managers to help people learn how to use these technologies.
[1402.94 --> 1406.86]  But a lot of them are by people who are using it to solve their own problems
[1406.86 --> 1414.44]  and then sharing back with the community the types of solutions that they're building in graphics and ray tracing,
[1414.84 --> 1416.88]  in artificial intelligence with deep learning.
[1417.34 --> 1419.68]  They'll be talking about hybrid cloud computing.
[1420.24 --> 1426.44]  They'll be talking about the work that they're doing in healthcare, in public sector and government applications.
[1427.20 --> 1432.20]  You know, just a really, really amazingly broad range of topics.
[1432.20 --> 1439.94]  And one of the most, I think, valuable things about GTC is it's one of the very few places
[1439.94 --> 1443.44]  where there's an opportunity for people from different disciplines,
[1443.68 --> 1446.16]  people working on completely different application domains,
[1446.44 --> 1454.48]  to kind of cross-pollinate their best ideas and inspire innovation in a large number of fields.
[1454.66 --> 1460.10]  Unlike most other events where, you know, people who are working on the same kind of thing get together
[1460.10 --> 1462.56]  and there can be, you know, a little bit of an echo chamber sometimes.
[1462.74 --> 1469.72]  So some of the things that we're doing to help facilitate that kind of, you know, innovative cross-pollination,
[1470.34 --> 1475.18]  even in a virtual environment, is hosting networking events for the attendees.
[1475.42 --> 1478.34]  We have this thing that we call Dinner with Strangers.
[1478.66 --> 1485.22]  There's basically, you know, a topic that could be an industry-related topic or a technology-related topic.
[1485.22 --> 1490.36]  And people who are interested in that technology and want to talk about it with people maybe they haven't met before
[1490.36 --> 1493.78]  are invited to get together in kind of small groups.
[1493.78 --> 1498.50]  We'll have someone from NVIDIA with some knowledge on the topic kind of host the gathering.
[1498.74 --> 1499.76]  But it's not a presentation.
[1499.76 --> 1502.82]  It's just a way for people with common interests to get together,
[1503.32 --> 1508.76]  maybe bring some dinner to their desk and eat and have some social interaction,
[1509.34 --> 1511.20]  talking with other people who have common interests.
[1511.20 --> 1512.94]  Yeah, this is so great.
[1513.04 --> 1518.42]  And before we go too much further, I just want to mention as well that, you know, this is coming up.
[1518.56 --> 1520.22]  It's October 5th through the 9th.
[1520.22 --> 1523.44]  As you can already tell, we haven't even gotten into everything.
[1523.66 --> 1525.92]  It's so much interesting stuff here.
[1526.12 --> 1532.78]  And NVIDIA has provided us with a 20% off discount for our listeners for GTC this year.
[1533.18 --> 1537.34]  And additionally, there's an early bird price that lasts until September 25th.
[1537.34 --> 1541.30]  So I know I'm registering the code we're going to list in our show notes.
[1541.62 --> 1545.56]  The code is CMINFDW20.
[1545.80 --> 1546.80]  It might be hard to remember.
[1546.92 --> 1548.44]  I'll definitely put it in our show notes.
[1548.58 --> 1550.10]  But this is a great deal.
[1550.16 --> 1551.06]  It's not very expensive.
[1551.36 --> 1554.78]  Lots of great material, it sounds like, to come.
[1555.22 --> 1561.30]  I'm curious, as you sort of tried this out earlier in the year, and now it's this fall edition,
[1561.30 --> 1567.34]  what were some of the, maybe the surprising elements that you noticed from having it online
[1567.34 --> 1570.60]  for the first time, completely online for the first time?
[1570.70 --> 1574.14]  Of course, there's like, sounds like a huge attendance for one.
[1574.52 --> 1578.56]  But what were some of the maybe surprising things that came out of the fact that
[1578.56 --> 1582.42]  you were able to have it online that maybe were unexpected to you?
[1582.42 --> 1588.98]  Well, I mentioned earlier how the kind of the evolution of NVIDIA over time has been supported
[1588.98 --> 1590.60]  by lots of small experiments.
[1591.60 --> 1599.50]  And one of the experiments that we did at GTC in the spring of this year was to offer our
[1599.50 --> 1604.38]  hands-on Deep Learning Institute training in a virtual environment.
[1604.64 --> 1606.06]  We had never done that before.
[1606.06 --> 1611.48]  And we'd certainly never done it at the scale of trying to train thousands of people at the
[1611.48 --> 1615.46]  same time as part of a GTC in these virtual classrooms.
[1615.74 --> 1621.52]  I'm just incredibly proud of the work that our Deep Learning Institute team did to pull
[1621.52 --> 1626.36]  that together, to work out all the kinks, to cross-train all of the instructors and teaching
[1626.36 --> 1634.30]  assistants so that thousands of people who attended those trainings in March could have a great
[1634.30 --> 1636.12]  hands-on learning experience.
[1636.98 --> 1647.24]  And I'm really excited that this upcoming GTC is a place where we're going to offer 16 of
[1647.24 --> 1652.62]  these workshops timed so that several of them are available in the North American time zone,
[1653.12 --> 1657.16]  several are available in the European time zone, and several are going to be available in
[1657.16 --> 1658.18]  the Asian time zones.
[1658.70 --> 1664.02]  And we'll be offering our brand new Fundamentals of Deep Learning course for everybody who just
[1664.02 --> 1667.76]  kind of wants to get started and understand what the basics are, get their hands dirty,
[1667.88 --> 1669.44]  training their first neural networks.
[1669.98 --> 1676.70]  We have a completely all-new updated natural language processing course that's based on the
[1676.70 --> 1681.22]  state-of-the-art tensors-based approaches to natural language processing.
[1681.86 --> 1688.14]  And we also have a brand new Recommender Systems course that will help people learn how to build
[1688.14 --> 1691.18]  recommendation systems and integrate them into their applications.
[1691.18 --> 1697.54]  And as always, you know, the other courses, including the multi-GPU course have been updated.
[1697.78 --> 1698.96]  There's a new course on CUDA.
[1699.72 --> 1708.00]  It's Deep Learning Institute program has helped us to train over 250,000 people worldwide in the
[1708.00 --> 1708.88]  last several years.
[1709.60 --> 1717.44]  And the demand for access to this kind of, you know, hands-on learning-by-doing style of training
[1717.44 --> 1719.16]  is just continuing to increase.
[1719.28 --> 1725.72]  And we're really excited about being able to offer that in an even larger way at GTC this October.
[1726.28 --> 1727.58]  Yeah, those are great classes.
[1727.70 --> 1733.10]  Having taken several of them myself, I love taking them and definitely recommend them.
[1733.10 --> 1737.40]  Um, and so I guess I wanted to just follow up for a second.
[1737.62 --> 1744.10]  I imagine that your CEO, Jensen Wong, is probably going to address the acquisition of Arm.
[1744.22 --> 1748.60]  Is there anything you can tell us or do you really have to wait until after he's talked at the keynote?
[1749.10 --> 1753.74]  You know, that news is hot off the presses just maybe a day and a half ago.
[1753.74 --> 1760.60]  We're still counting it in hours and, um, Jensen is really going to be our, our spokesperson on that.
[1760.74 --> 1764.04]  But, but what I can say is we're all just really excited about it.
[1764.14 --> 1771.82]  I mean, there's so, so many opportunities for, uh, ways that we can serve the ecosystem of developers
[1771.82 --> 1776.64]  and data scientists and researchers that the companies and organizations that are, they're
[1776.64 --> 1778.52]  trying to solve really, really hard problems.
[1778.52 --> 1784.58]  And we're just delighted that we have the opportunity to help them with the platforms
[1784.58 --> 1789.64]  and the technologies and the training that they need to make progress on those things.
[1790.08 --> 1791.86]  Yeah, that's, I totally understand that.
[1791.92 --> 1794.74]  And I knew it was so new, but I felt like I had to ask.
[1795.10 --> 1795.68]  It's exciting.
[1795.80 --> 1799.46]  And, you know, good, good timing for this episode for sure.
[1799.46 --> 1803.74]  And, uh, you know, tune in here in a couple of weeks to, to find out more for sure.
[1803.82 --> 1805.44]  It's going to be going to be exciting.
[1805.44 --> 1810.54]  Will, you mentioned one thing kind of, as you were talking about GTC and, you know,
[1810.64 --> 1815.28]  Chris mentioned that you'd taken some of these classes and, uh, you talked a little bit about
[1815.28 --> 1818.74]  the deep learning Institute, some of its activities at GTC.
[1818.80 --> 1824.24]  I was wondering if you could just give us kind of step back a bit and tell us a bit about sort
[1824.24 --> 1829.22]  of the origins of the deep learning Institute and kind of its, its current state and what
[1829.22 --> 1829.80]  it is now.
[1830.44 --> 1830.88]  Oh, sure.
[1830.96 --> 1832.50]  Yeah, actually, that's a pretty fun story.
[1832.50 --> 1838.20]  I think I mentioned at the beginning that for a period of time, I was the product manager
[1838.20 --> 1838.78]  for CUDA.
[1839.60 --> 1845.56]  And, um, when we were first starting to, to bridge from working in the, the academic
[1845.56 --> 1852.16]  research segment into commercial enterprises, there were a lot of customers who said, yeah,
[1852.20 --> 1853.12]  yeah, that looks promising.
[1853.12 --> 1855.94]  And we love the demos, but can you come show us how to do it?
[1855.94 --> 1856.20]  Right.
[1856.22 --> 1859.30]  We have smart people here where they can learn, but we need someone to come show us how.
[1859.30 --> 1866.10]  And so, you know, I dusted off my, uh, my frequent flyer mileage card and, uh, started
[1866.10 --> 1869.68]  traveling the world with literally a pallet of laptops.
[1869.82 --> 1872.64]  We, we got some gamer laptops that had GPUs in them.
[1872.94 --> 1879.78]  And a colleague and I started just like flying all over the world, shipping pallets of laptops.
[1879.78 --> 1884.88]  And we had this challenge that, you know, stuff breaks, it gets stuck in customs.
[1884.88 --> 1889.52]  You have to like reimage the darn things after every training to make sure they're going to
[1889.52 --> 1890.58]  work for the next people.
[1890.98 --> 1892.30]  And it was a big hassle.
[1892.66 --> 1899.98]  And after doing that for a couple of years, Amazon AWS announced that they were going to
[1899.98 --> 1903.46]  have thousands of GPUs available in their cloud.
[1903.46 --> 1907.90]  Uh, and we immediately said that, that is what we need.
[1908.24 --> 1913.22]  Uh, and so we updated our training materials and figured out how to get all of that hosted
[1913.22 --> 1913.86]  in the cloud.
[1913.98 --> 1923.42]  And now all we had to do was show up and all of the people who wanted to learn how to, uh,
[1923.42 --> 1928.62]  at the time develop applications using CUDA could just connect to these cloud servers
[1928.62 --> 1932.52]  pre-configured with all the software they would need from their own laptops.
[1932.52 --> 1936.60]  In fact, we had a few people just like do it from their iPads and it was fantastic.
[1937.22 --> 1938.72]  And then we realized, you know what?
[1938.76 --> 1945.12]  We could probably develop some self-paced content so that anybody in the world could just log
[1945.12 --> 1949.42]  in and learn how without having to wait for me to show up on their doorstep.
[1949.88 --> 1951.52]  And so that started taking off too.
[1951.72 --> 1957.64]  And after about a year, maybe two years of that, a few of the people that we had been
[1957.64 --> 1962.16]  working with internally at NVIDIA are subject matter experts who are constantly going out
[1962.16 --> 1966.68]  and engaging with customers and helping them solve their challenging problems came to us
[1966.68 --> 1969.02]  and said, Hey, there's this thing called deep learning.
[1969.02 --> 1970.12]  It's kind of interesting.
[1970.12 --> 1974.10]  And we built, we built these little like Jupiter notebooks that kind of show people how to do
[1974.10 --> 1974.26]  it.
[1974.26 --> 1979.56]  Could we just maybe host that on your training platform and, and see if people want to learn
[1979.56 --> 1980.48]  how to do this thing?
[1983.04 --> 1993.40]  And, uh, uh, within a very short amount of time, the number of people who, you know, signed
[1993.40 --> 1999.00]  up for an account and logged in and experienced this deep learning training completely eclipsed
[1999.00 --> 2000.50]  anything else we had done before.
[2000.50 --> 2004.10]  And we realized that we had a tiger by the tail on that.
[2004.28 --> 2006.26]  So that's, you know, we'd been experimenting.
[2006.42 --> 2007.48]  We'd been trying things.
[2007.96 --> 2008.82]  Something worked.
[2008.96 --> 2010.70]  That's when we decided to double down.
[2011.30 --> 2014.08]  And we gave this initiative a name.
[2014.26 --> 2016.08]  We decided to call it the Deep Learning Institute.
[2016.92 --> 2022.60]  We hired a team and began building out a rich catalog of both self-paced and instructor-led
[2022.60 --> 2023.06]  content.
[2023.32 --> 2026.38]  We started an instructor certification program.
[2026.38 --> 2031.14]  So now there are over 600 instructors all over the world who are certified to deliver
[2031.14 --> 2033.44]  our training to their audiences.
[2034.16 --> 2039.12]  Many of them are, you know, well-qualified professors and academic researchers working
[2039.12 --> 2040.06]  in higher ed.
[2040.44 --> 2046.18]  Many of them are independent, like training service providers who've now been able to make
[2046.18 --> 2047.84]  this part of their business practices.
[2048.54 --> 2054.12]  Some of them are even companies who have decided that they need so many of their own employees
[2054.12 --> 2060.20]  to be trained, that they're getting their internal employee instructors certified to deliver
[2060.20 --> 2065.78]  this training and scaling it up within their organizations as part of workforce transformation
[2065.78 --> 2068.58]  projects to become AI companies.
[2069.14 --> 2070.74]  We're happy to work with all of them.
[2071.00 --> 2073.30]  That's kind of how we've come to where we are today.
[2073.80 --> 2079.68]  And as I mentioned earlier, the latest new thing in the evolution of the Deep Learning Institute
[2079.68 --> 2087.68]  is this introduction of our online virtual classroom format that allows us to deliver training
[2087.68 --> 2094.66]  anywhere in the world and even to aggregate demand across many different customers or many
[2094.66 --> 2097.34]  different sites within the same customer.
[2097.96 --> 2101.80]  Because, you know, it doesn't really make sense to send an instructor to train two or three people.
[2102.10 --> 2104.12]  That's a lot of effort and expense for everyone.
[2104.12 --> 2110.50]  But if you can get 15, 20, 25 people together from multiple different sites, whether they're
[2110.50 --> 2116.52]  from the same company or from several different companies or organizations, then you can put
[2116.52 --> 2122.02]  together a really good learning experience for them to quickly learn how to use these new
[2122.02 --> 2127.56]  technologies through hands-on exercises and assessments and end up with a certification at
[2127.56 --> 2132.90]  the end of the day proving that they have actually developed competence in applying these technologies
[2132.90 --> 2134.36]  to solve worthwhile problems.
[2134.36 --> 2164.34]  So, Will, got a question about, you know, you guys have all these problems.
[2164.34 --> 2164.96]  Great classes.
[2165.38 --> 2168.02]  And they're very well run and they're very well integrated.
[2168.34 --> 2172.38]  But we're in this really fast-moving world of deep learning and AI in general.
[2172.66 --> 2176.70]  And how do you choose what should be part of your curriculum?
[2177.24 --> 2177.84]  What classes?
[2177.94 --> 2180.72]  There's so many topics out there and they're evolving so fast.
[2180.88 --> 2185.20]  That has to be a bit of a challenge to figure out what to provide for the people that you're
[2185.20 --> 2185.84]  serving out there.
[2186.30 --> 2187.22]  You know, it really is.
[2187.30 --> 2190.14]  But it's one of those problems that it's a good problem to have.
[2190.20 --> 2191.88]  It's like having an embarrassment of riches.
[2192.22 --> 2193.64]  There are so many opportunities.
[2193.64 --> 2200.78]  There are so many opportunities to develop training curriculum around these new and emerging and
[2200.78 --> 2206.74]  quickly evolving technologies that we do have to be a little bit careful which ones we choose
[2206.74 --> 2213.00]  to invest in and get a small army of instructors trained and certified to deliver.
[2213.00 --> 2224.32]  And so what we've tried to do is keep up with what is the state of the art and keep tabs on all the new research that's coming out.
[2225.10 --> 2236.58]  And as that research kind of evolves and new practices begin to start getting adopted, that's really the sweet spot for developing training.
[2236.58 --> 2245.96]  You know, you think training is really a way to teach people how to use and apply things that have already been proven.
[2245.96 --> 2257.08]  And so if you were to ask me, like at this time last year, I would have said, you know, there's a lot of work in recommender systems.
[2257.08 --> 2270.46]  But the state of the art is still evolving so rapidly that if we were to go take a couple months to distill that down into best practices and build a training course around it, by the time we actually got that out into the world,
[2270.46 --> 2277.36]  the state of the art would have moved on so quickly that people would be maybe a little frustrated or disappointed in the training.
[2277.98 --> 2290.66]  And so at this point, the best thing we should be doing is connecting them with the research papers and the open source projects and things like that so that people who are more comfortable living on the bleeding edge can adopt that technology while it is still in its infancy.
[2290.66 --> 2303.72]  But this year, things have evolved to the point where many of the recommender system development and design approaches, those best practices are established.
[2304.08 --> 2305.48]  In fact, they're really well established.
[2306.60 --> 2315.00]  And so we built a training course around that and are starting to offer it to everyone who needs to build these kinds of recommender systems.
[2315.54 --> 2318.14]  And it can kind of happen in waves.
[2318.14 --> 2321.44]  So this happened a few years ago for natural language processing.
[2321.58 --> 2324.40]  We built a course around it that was really incredibly popular.
[2324.48 --> 2327.62]  It was one of our more difficult courses, but it was really popular.
[2328.44 --> 2339.60]  And then last year or over the last year, a completely new approach to natural language processing has emerged that is based on transformers and models like BERT and GPT and so forth.
[2339.60 --> 2355.88]  And so it was time, very clearly time, for us to go back and completely update and replace that older course with something that is teaching people how to use the latest state-of-the-art techniques now that they've been boiled down to practice.
[2355.88 --> 2361.40]  On the DLI content team, we talk about this as it's kind of like painting the Golden Gate Bridge.
[2361.50 --> 2364.78]  By the time you get to the end, you paint it from south to north.
[2364.92 --> 2368.96]  By the time you get to the north side, it's time to go back and start painting it all over again.
[2368.96 --> 2374.72]  Yeah. And so you mentioned the interactions with open source and the research community.
[2374.96 --> 2386.18]  Of course, it was really interesting when you were talking about the kind of story of the Deep Learning Institute and how kind of Jupiter entered the mix and like these different projects.
[2386.18 --> 2402.98]  From your perspective, like, you know, it seemed like part of the reason why Chris and I started this podcast was that very much focus on the practical side of AI when it seemed like to us that there were a lot of, you know, it was kind of like the Wild West.
[2403.12 --> 2407.12]  There were a lot of things out there that just weren't extremely practical.
[2407.62 --> 2412.56]  But, you know, of course, that that has definitely changed and evolved over time.
[2412.56 --> 2419.20]  What is maybe in the Deep Learning Institute or maybe in your work more broadly and NVIDIA?
[2419.72 --> 2426.32]  How do you think about engaging with different open source projects and and contributing to those?
[2426.44 --> 2429.32]  I know NVIDIA is involved with with a lot of those.
[2429.40 --> 2434.78]  But like you mentioned, for example, NLP and Transformers, of course, we've had hugging face on the show.
[2434.78 --> 2445.72]  And I know I've seen pictures on their Twitter of like them getting boxes of Titan RTX GPUs in the mail for training their models.
[2445.90 --> 2453.88]  So how do you keep your pulse on not only the new techniques, but how the tooling and the open source side of things is evolving?
[2453.88 --> 2460.00]  And is there a lot of freedom within NVIDIA to contribute to open source or an encouragement around that?
[2460.06 --> 2465.22]  And how do you choose where to put your effort and all of that sort of thing on the open source side?
[2465.80 --> 2467.46]  Wow, that's a really good question.
[2467.74 --> 2476.24]  If I could even distill it down to a simple list or a recipe, there's a lot of people within the company who would really appreciate that.
[2476.24 --> 2485.84]  I think the best way to really explain it is that we look at each opportunity, at each situation based on its own merits.
[2486.10 --> 2502.60]  And we recognize that there are so very many different types of open source projects, some of which, many of which, hundreds of which, in fact, NVIDIA engineers have created and continue to maintain out in the world and invite others to participate in.
[2502.60 --> 2516.78]  Others, of which we actually have adopted and integrated into some of our products and continue to support and make contributions and so forth, too.
[2517.22 --> 2520.42]  There isn't really like a single one-size-fits-all recipe.
[2520.54 --> 2527.74]  I think it really depends on what do our customers need, what do our developers need, and what's the best ways that we can find to support them.
[2527.74 --> 2542.06]  And then at the same time, what are the best implementations, what are the best projects out there that we might be able to use and contribute to, to, you know, just be positive contributing members to the open source ecosystem?
[2542.44 --> 2545.28]  I'm not sure if that's a great, succinct answer to your question.
[2545.62 --> 2546.40]  It's a big question.
[2546.56 --> 2551.76]  Yeah, it'd be hard to distill that down, but I think it's, yeah, definitely good thoughts on that subject.
[2551.76 --> 2574.06]  So I guess, you know, as we're starting to get toward the end, I'm curious, being in the center of AI education and doing and accomplished, having accomplished all that you've done on this, kind of where do you see the future of AI education going with the Deep Learning Institute and even in a broader sense at large within the larger AI community?
[2574.06 --> 2584.12]  Obviously, we've had changes lately where we've moved from a lot of in-person training to more and more remote training because of COVID and its impact on the world.
[2584.24 --> 2590.26]  But what do you see over the horizons that maybe the rest of us haven't thought about and, you know, where you think things might go?
[2590.82 --> 2591.98]  Wow, that's a great question.
[2592.24 --> 2596.22]  Off the top of my head, I think there's really kind of three really important areas.
[2596.22 --> 2626.20]  One is in the training of AI practitioners, people who are going to be building and evaluating AI-based functionality to be integrated into these applications and helping them to understand just critical importance of analyzing the data that is used to train the neural networks and testing the outputs of those neural networks to ensure that they're really functioning as expected in all of the different scenarios.
[2626.22 --> 2639.96]  These are things like just making sure you have enough examples of all the different types of data that you need in order to have your neural network be effective in a real world environment.
[2640.20 --> 2654.80]  You know, for example, if you train a neural network to be able to distinguish between all the different types of flowers or dogs or cats in the world, and then later you show it a picture of a raccoon or a giraffe, it's not going to know what to do, right?
[2654.80 --> 2662.12]  So you need to train it to be able to handle all the variations, the variety of the real world that it's actually going to be exposed to.
[2662.72 --> 2663.44]  So that's one thing.
[2663.86 --> 2673.18]  The second thing is that for people who are not AI practitioners or who are, let's say, not yet AI practitioners, let's say they're earlier in their career or schooling,
[2673.18 --> 2687.10]  so much of our world and interaction with it are going to be influenced by these powerful AI tools that I think it's really important that, you know,
[2687.10 --> 2693.86]  even school-age kids have a basic understanding of what AI is and how it works.
[2693.86 --> 2701.90]  And, you know, when I go to a website and someone is recommending that I buy this pair of sneakers or this shirt or this, you know, whatever product,
[2702.24 --> 2705.80]  then I have a sense for, well, what might that be based on?
[2705.98 --> 2707.66]  Why are they recommending it to me?
[2708.04 --> 2713.66]  Is it because other people like me have also purchased this product and enjoyed it?
[2714.20 --> 2717.02]  And if so, how do they know who else is like me?
[2717.02 --> 2724.32]  You know, just being really thoughtful about how does that world work and taking a peek under the covers,
[2724.52 --> 2734.84]  I think is going to be a really important thing for really everyone to be comfortable with the capabilities and the limitations of this powerful technology.
[2735.10 --> 2735.74]  It's a great point.
[2735.94 --> 2740.08]  I was reminded of, I bought my nieces and nephews.
[2740.08 --> 2747.30]  There's like this series of books called, I think it's like calculus and other things for babies or kids or something like that.
[2747.52 --> 2747.88]  Oh.
[2748.02 --> 2756.06]  I was like, oh, we need some like AI for babies books to, you know, like you can put in along with the other children's books.
[2756.50 --> 2759.06]  Anyway, that my mind was going there while you were talking.
[2759.40 --> 2760.48]  What was your third point there?
[2760.48 --> 2771.04]  Oh, the third area, you know, these are just off the top of my head here, is the impact that AI is going to have on education itself.
[2771.90 --> 2789.22]  You know, as we transition to more online learning and you have things like Khan Academy and other services that have really packaged up some very high quality lectures on and learning materials on all of the core subjects.
[2789.22 --> 2803.50]  The ability of computers using AI and other data science techniques to observe how students are learning and to understand what is the learning style, right?
[2803.52 --> 2809.94]  Because we all have different types and different extents of different flavors of learning styles.
[2810.06 --> 2811.60]  Some people like to learn more visually.
[2811.86 --> 2813.60]  Some people to learn more by listening.
[2814.20 --> 2817.68]  I happen to be someone who learns, maybe you can tell by talking.
[2817.68 --> 2825.22]  And kind of repeating back what I have understood in order to get confirmation that I've understood it correctly.
[2825.68 --> 2828.48]  These different learning styles are things that can be observed.
[2828.76 --> 2838.56]  And then the students can be offered different forms or different formats of the material that helps them learn more effectively.
[2838.56 --> 2846.84]  And so that can take the shape of, you know, think of it as a, almost like a choose your own adventure type of storybook.
[2846.84 --> 2858.68]  If you, if you remember those, where you're offered different kinds of learning experiences to learn the same materials based on how you have learned best in the past.
[2858.68 --> 2860.68]  And there's always going to be some experimentation.
[2860.68 --> 2867.04]  And, you know, we're going to have to make some smart decisions around, you know, maybe some students are better auditory learners.
[2867.04 --> 2867.90]  They learn by listening.
[2867.90 --> 2874.36]  But it's really important that they develop their visual, analytical, and comprehensive skills as well.
[2874.58 --> 2882.16]  And so we'll need to balance that out in the types and formats of learning materials that are offered to them.
[2882.26 --> 2886.20]  This is an area that our Deep Learning Institute team is really interested in, right?
[2886.22 --> 2891.12]  They want to get all meta and apply deep learning to deep learning education.
[2891.12 --> 2893.08]  Yeah, that's so cool.
[2893.08 --> 2898.32]  And I just get the sense from, you know, how you describe that and your passion around it.
[2898.38 --> 2908.94]  You seem fairly optimistic in terms of AI's benefit to certain areas, like in terms of AI for good in education and other areas.
[2909.02 --> 2912.52]  It's something definitely Chris and I are very passionate about.
[2912.52 --> 2915.10]  As you look to the future, is that true?
[2915.18 --> 2926.84]  Are you sort of generally optimistic about, you know, AI's ability to impact our world for the better in different areas like education or health and that sort of thing?
[2927.26 --> 2941.12]  Maybe what's one other area that you're particularly, as we kind of close out, what's another area where you're particularly excited about the potential, you know, impacts for AI over the next couple of years?
[2941.12 --> 2945.10]  You know, in general, yes, I'm an optimist.
[2945.26 --> 2953.86]  I'm optimistic that we as humans will learn how to use AI technologies because it's just a tool, right?
[2953.88 --> 2955.72]  It doesn't actually think for itself.
[2956.34 --> 2960.08]  It's still a computer that does what we design it to do.
[2960.50 --> 2967.88]  Now, we may be designing it at a little further level of abstraction than we have with previous technologies,
[2967.88 --> 2972.56]  but it doesn't have its own agency to decide what to do.
[2973.50 --> 2980.50]  And so I am optimistic that we as humans will continue to learn and apply AI in really positive ways
[2980.50 --> 2989.34]  and also learn how to mitigate some of the potentially less positive ways in which this tool, this technology could be applied.
[2989.92 --> 2993.88]  One of the areas that I'm most excited about really is in healthcare, right?
[2993.88 --> 3007.68]  If you look at the work that is being done, even just around COVID-19 research and the speed at which the computational simulations are allowing scientists and researchers
[3007.68 --> 3025.40]  to very rapidly explore the problem space to test out their hypotheses in effectively zero-risk scenarios before they go start testing these drug molecules and treatments in a lab environment.
[3025.40 --> 3055.38]  It's just really, really incredible.
[3055.38 --> 3056.80]  And a number of other fields.
[3057.70 --> 3058.22]  Fantastic.
[3058.44 --> 3059.24]  Very inspiring.
[3059.82 --> 3067.72]  As we finish up, I actually want to note to listeners that we have had several episodes devoted entirely to NVIDIA.
[3068.06 --> 3072.86]  And obviously, NVIDIA comes up in many episodes as part of our casual conversation.
[3073.42 --> 3078.78]  Episode 15 was artificial intelligence at NVIDIA with Bill Daly, NVIDIA's chief scientist.
[3078.78 --> 3084.74]  Episode 36, we had Anima Anankumar, who is the director of ML Research at NVIDIA.
[3085.22 --> 3096.00]  And then more recently on episode 90, Daniel and I were just alone, but we talked all about exploring NVIDIA's Ampere architecture and the A100 GPU.
[3096.52 --> 3098.78]  Just wanted to let listeners know that.
[3098.88 --> 3105.32]  If you're interested in this conversation and haven't heard one of those, you probably want to go back and listen to get a lot more about NVIDIA.
[3105.32 --> 3108.36]  I wanted to remind listeners that we have a code.
[3108.46 --> 3117.26]  If you go to our show notes, which you can get to on whatever device you happen to be listening to, there is a discount code for the GPU Technology Conference.
[3117.98 --> 3120.70]  And with that, Will, thank you so much for coming on the show.
[3120.78 --> 3121.90]  This was a great conversation.
[3122.06 --> 3122.98]  We really enjoyed it.
[3123.40 --> 3124.60]  Well, thank you both for having me.
[3124.66 --> 3125.76]  This has been a lot of fun.
[3125.76 --> 3132.68]  And I look forward to seeing you again in person someday or, you know, at least virtually like this sometime soon.
[3133.30 --> 3133.72]  Absolutely.
[3133.94 --> 3134.28]  Will do.
[3134.44 --> 3134.86]  Thank you.
[3138.62 --> 3144.14]  Comment on this and every episode of Practical AI on changelog.com.
[3144.58 --> 3148.08]  There's a discussion link in your show notes for easy clickings.
[3148.24 --> 3149.42]  We would love to hear from you.
[3149.42 --> 3154.40]  We also have a free Slack community where these discussions take place.
[3154.40 --> 3157.24]  Join today at changelog.com slash community.
[3157.88 --> 3159.56]  And don't forget to follow the show on Twitter.
[3159.70 --> 3162.04]  We are at PracticalAI FM.
[3162.82 --> 3166.44]  Practical AI is hosted by Daniel Whitenack and Chris Benson.
[3166.82 --> 3168.30]  It's produced by me, Jared.
[3168.48 --> 3171.90]  And our music is provided by the Beat Freak, Breakmaster Cylinder.
[3173.14 --> 3175.22]  Shout out to all of our longtime sponsors.
[3175.46 --> 3179.36]  Thanks again to Fastly, Linode, and Rollbar for their continued support.
[3180.44 --> 3181.56]  That's all for now.
[3181.98 --> 3183.20]  We'll talk to you again next week.
[3184.40 --> 3214.38]  We'll be right back.
