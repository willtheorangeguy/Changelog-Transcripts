[0.00 --> 6.70]  Bandwidth for Changelog is provided by Fastly. Learn more at Fastly.com. We move fast and fix
[6.70 --> 11.42]  things here at Changelog because of Rollbar. Check them out at Rollbar.com and we're hosted
[11.42 --> 17.36]  on Linode servers. Head to linode.com slash Changelog. This episode is brought to you by
[17.36 --> 23.72]  DigitalOcean. They now have CPU optimized droplets with dedicated hyper threads from best in class
[23.72 --> 29.18]  Intel CPUs for all your machine learning and batch processing needs. You can easily spin up
[29.18 --> 34.74]  their one-click machine learning and AI application image. This gives you immediate access to Python 3,
[35.20 --> 42.68]  R, Jupyter Notebook, TensorFlow, Scikit, and PyTorch. Use our special link to get a $100 credit for
[42.68 --> 51.28]  DigitalOcean and try it today for free. Head to do.co slash Changelog. Once again, do.co slash Changelog.
[59.18 --> 68.60]  Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[69.02 --> 74.52]  productive, and accessible to everyone. This is where conversations around AI, machine learning,
[74.56 --> 78.66]  and data science happen. Join the community and snag with us around various topics of the show
[78.66 --> 84.48]  at changelog.com slash community. Follow us on Twitter. We're at Practical AI FM. And now onto the show.
[89.18 --> 94.96]  Hey, Chris. How's it going this week? Doing great. I am super excited about the next few weeks. Got
[94.96 --> 100.98]  some cool things coming up, which we'll talk about. Yeah, definitely. So I'm here joined by my co-host,
[101.14 --> 109.64]  my co-host Chris, and we're going to bring you some news and updates from the AI world today,
[109.64 --> 116.86]  and then also some learning resources to help you level up your AI skills in a practical sort of way.
[116.86 --> 123.26]  But yeah, there's a lot coming up, Chris. I know I'm traveling over the next three or four weeks
[123.26 --> 128.56]  quite a few times, and I know you've got some travel too. So there's a lot of exciting stuff
[128.56 --> 133.38]  coming up. There is. And there's so much happening in the news right now. I am going to just leap on
[133.38 --> 139.94]  into the first one, if you don't mind. Sounds good. Okay. So I came across something that I thought
[139.94 --> 145.68]  was really defined what I've been noticing in the industry. And that is, it was an article from
[145.68 --> 152.46]  VentureBeat called How AI is Decommoditizing the Chip Industry. And it was a cool read because
[152.46 --> 158.44]  it really was pointing out something. It seems like, you know, for years, as you had, you know,
[158.62 --> 164.96]  with before the era of AI and chips and the commoditization of different things coming out
[164.96 --> 169.92]  in computing in general. And now AI has kind of reversed that trend to some degree and that
[169.92 --> 175.88]  processing devices, CPUs and the like, GPUs, et cetera, are really becoming more and more specialized.
[176.44 --> 181.88]  And that is creating all sorts of entrepreneurial opportunities for different companies. And so we're
[181.88 --> 187.84]  seeing lots of chip startups instead of just software startups. And some of these companies
[187.84 --> 194.08]  are like Nirvana, whom some people may know from Intel at this point, Graphcore, Cerebrus,
[194.08 --> 200.64]  Vasith, there's a whole slew of them. And they're really challenging the big incumbents, which certainly
[200.64 --> 206.54]  in the AI era has been NVIDIA kind of leading the way. But, you know, Intel's come in hard,
[206.66 --> 214.44]  come back from the CPU world into the new AI-oriented chip world. Microsoft has theirs, AMD, Qualcomm,
[214.80 --> 221.56]  Google, TPUs, and IBM. All these big players are getting huge challenges. So NVIDIA really came in
[221.56 --> 226.78]  with early dominance with the GPU as they moved from consumer gaming into AI. And, you know,
[226.82 --> 232.82]  they had been kind of the poster child for the AI world. Even they at this point are having to watch
[232.82 --> 238.72]  some of the new risers coming in because of what's called ASICs, which is application-specific
[238.72 --> 244.72]  integrated circuits. And that is chips that are designed specifically for a particular application.
[244.92 --> 249.88]  They're completely optimized for that. And that's just fascinating when you think about it,
[249.88 --> 254.96]  because even though NVIDIA has their Volta architecture and Intel has Nirvana, Google's
[254.96 --> 260.26]  TPUs, at the end of the day, this article is suggesting that the future lies in ASICs rather
[260.26 --> 262.92]  than commodity hardware. What do you think about that? Do you think they're right?
[263.48 --> 272.48]  Well, I first of all think that you did an amazing job saying decommoditizing correctly on the first try,
[272.48 --> 277.84]  which I think is maybe one of the more impressive things that I've heard recently.
[278.56 --> 288.10]  But in all seriousness, I don't have as much exposure to, you know, the application-specific
[288.10 --> 295.10]  type circuit world. I think it'll be interesting to see that develop. What I do have exposure to is
[295.10 --> 301.20]  definitely the kind of resurgence of specialized hardware in the context of things like, you know,
[301.22 --> 306.88]  another company that Intel owns now, Movidius, has, you know, things like these neural compute sticks.
[306.94 --> 311.52]  And one of the things that I really like about them is they've kind of found a new niche that
[311.52 --> 319.14]  they're filling. But it's also, you know, enabling really interesting new types of applications.
[319.14 --> 325.96]  So they've got these little, you know, VPU visual processing unit, like USB sticks that you can plug
[325.96 --> 332.34]  into a Raspberry Pi or to a drone or other things and, you know, run your neural networks on this
[332.34 --> 340.40]  specialized architecture, you know, in a very kind of, you know, low power at the edge sort of scenario.
[340.40 --> 345.56]  And, you know, I'm at GopherCon this week, actually, and just had a conversation before I walked over
[345.56 --> 351.16]  to record this with someone and said, oh, it's so cool. Now I have, you know, I've been doing all
[351.16 --> 356.00]  this drone stuff and now I can just plug in these sticks into my drone and have them follow around,
[356.12 --> 362.06]  you know, specific people based on their, you know, facial recognition and all that, you know,
[362.06 --> 365.32]  stuff. So people are really excited about these things.
[365.50 --> 371.48]  You know, you have a great point there. And I've used a Movidius and I know so many software developers
[371.48 --> 376.68]  who are not data scientists. They're not coming from the traditional backgrounds leading into AI.
[377.04 --> 380.90]  They're software developers that have started in other areas. They might've been web developers and
[380.90 --> 385.74]  such. And, uh, and they've moved into this and having something like a Movidius stick or, or,
[385.74 --> 392.80]  or similar devices has really opened up the space for them. So, uh, since, uh, I was halfway thinking
[392.80 --> 398.14]  about suggesting you and I go create a startup where we, uh, we, we create an AI chip for, uh,
[398.14 --> 400.66]  that's designed around AI for good. I say tongue in cheek.
[400.66 --> 403.64]  Yeah. That, yeah, I, I would be, I would be happy to do that.
[403.86 --> 404.16]  There you go.
[404.66 --> 409.66]  You, you, you, you provide the funding. A couple of things that I found this week actually had to do
[409.66 --> 415.62]  with more on the research side, um, which was kind of, uh, I don't know, kind of different for me
[415.62 --> 420.08]  because I'm usually more on the, more on the non-research side, but I, I really found these
[420.08 --> 427.10]  interesting. The first is this new, uh, paper that came out on the archive from some, some people
[427.10 --> 432.68]  at Grenoble university in France. And there's also a PyTorch implementation of this network.
[432.68 --> 438.82]  And, um, what it is, is it's a kind of new type of sequence to sequence prediction. So if you're,
[438.92 --> 444.08]  if you're not familiar, that's where, you know, a very common type of neural network that's used in
[444.08 --> 450.54]  things like machine translation of texts and, you know, taking sequences of something to other,
[450.54 --> 455.70]  other sequences. And normally what happens in those is there's kind of an encoder and a decoder
[455.70 --> 462.00]  stage of those networks. And this paper showed that they could kind of combine those two things
[462.00 --> 468.24]  into a single two-dimensional convolutional layer, which I think is, is really, um, you know,
[468.24 --> 472.50]  it seems after you see it, it's like, oh, that's, that's a really great idea. But, you know,
[472.50 --> 478.74]  it took someone to, you know, kind of come up with that and a natural, natural step. So it's cool to see
[478.74 --> 484.58]  even in things that are utilized in production. So often there can, can be this sort of innovation
[484.58 --> 488.92]  and refining happening. You know, it's funny because when you think about sequences, you know,
[488.96 --> 495.44]  most people automatically turn to RNNs, but we, I know over the last year or so, I've seen so many
[495.44 --> 502.44]  CNN applications for, for sequential, um, applications. Uh, and, and it's, it's interesting
[502.44 --> 508.22]  to see how versatile different architectures in the, in the larger convolutional neural network space
[508.22 --> 513.56]  have been, uh, going beyond, you know, just the visual thing that we tend to associate with them
[513.56 --> 513.98]  normally.
[514.58 --> 518.86]  Yeah, definitely. And, and like I say, the, there's an implementation of this already on GitHub
[518.86 --> 524.74]  and in PyTorch, which I love working with PyTorch. And so I, I would love to try out some other examples
[524.74 --> 526.28]  and you guys can as well.
[526.68 --> 533.22]  Gotcha. Well, I am going to, uh, turn briefly toward the, the medical world where it intersects
[533.22 --> 539.34]  with AI. There is a couple of articles that I've run across. Uh, one is, uh, called John Hopkins
[539.34 --> 545.26]  researchers use deep learning to combat pancreatic cancer. And that one really struck a nerve with me,
[545.26 --> 549.94]  um, because, um, I, uh, incidentally I'm on my second marriage, but in my first marriage,
[549.94 --> 555.76]  I lost my mother-in-law to pancreatic cancer. And I, you know, we watched as, as she, as we,
[555.76 --> 562.64]  as she went downhill very, very rapidly. And, um, and in doing that, it made me very aware of how
[562.64 --> 568.82]  bad pancreatic cancer is in terms of, um, only 7% of patients that are diagnosed, make it another
[568.82 --> 574.76]  five years. It has the lowest survival rate of any form of cancer out there. Um, and so this was,
[574.84 --> 578.92]  this really caught my eye and that they are, they're basically saying that early detection,
[578.92 --> 584.88]  uh, could lead nearly a third of all diagnosis, uh, to be made four to 12 months earlier, which could
[584.88 --> 590.96]  save a lot of lives or extend a lot of lives out there. So in, in our, in our ongoing theme of AI
[590.96 --> 597.24]  for good, uh, I really, uh, I really am encouraged by that. They, they use deep learning, uh, in
[597.24 --> 602.66]  combination with a CAT scan to, to look for my new textural changes to the tissue. So that was pretty
[602.66 --> 610.38]  amazing. And then the other thing I saw, which was on the, uh, on the pharma side was, um, uh, a system
[610.38 --> 614.72]  that, uh, they call release, which stands for reinforcement learning for structural
[614.72 --> 619.56]  evolution, which uses these two neural networks, one that's kind of a, a teacher neural network
[619.56 --> 626.00]  and one, which is kind of a student. And they say that they can, the teacher knows 1.7 million
[626.00 --> 631.14]  active molecules in great detail. And the student's able to learn from that and then actually create
[631.14 --> 638.36]  new molecules and evaluate those new molecules with properties that researchers specify. And so
[638.36 --> 643.54]  this is where you're, you're seeing deep learning being applied to pharma to create designer drugs,
[643.54 --> 649.04]  uh, much more rapidly. And, and between the diagnosis of cancer and the life-saving aspects
[649.04 --> 654.14]  of that and being able to get to, to new life-saving drugs sooner, I'm just, uh, I'm just really
[654.14 --> 657.92]  impressed with how deep learning is revolutionizing medicine in general.
[658.36 --> 664.88]  Yeah, definitely. I think that, uh, especially coming from, uh, like a background where I was
[664.88 --> 670.30]  exposed to like computational chemistry and those sorts of methods, I think people don't, you know,
[670.30 --> 675.90]  when you say all of those molecules and those sorts of things, um, you know, maybe people don't fully
[675.90 --> 682.06]  realize that, you know, for even a single molecule, a small molecule like oxygen, you know, there's,
[682.42 --> 688.18]  if you ignore the, the protons and neutrons, you still have a bunch of electrons, uh, six, I believe,
[688.28 --> 693.10]  if I, if I haven't forgotten everything. And each of those are in a three-dimensional space and,
[693.10 --> 699.48]  you know, there's a time element and there's, um, potentially external fields. And there's just a lot
[699.48 --> 705.70]  of variables that happen in, in these sort of computational chemistry, uh, scenarios. And if
[705.70 --> 709.92]  there's anything we know about deep learning, uh, it's, it's pretty useful in, in high dimensional
[709.92 --> 715.40]  spaces sometimes. So, uh, I think that's, that's really interesting to see, um, more of those methods
[715.40 --> 720.54]  come out. Well, what else have you seen this past week? Well, I saw this super creepy video,
[720.54 --> 728.32]  which I shared with our, I shared with our users on, or not our users, our listeners on, uh,
[728.32 --> 735.82]  in our Slack channel, it's this, uh, new work, uh, from Berkeley and essentially the video that I saw,
[735.88 --> 741.62]  and maybe there's multiple out there, I'm not sure is like a guy dancing. Um, you know, it's like a
[741.62 --> 749.46]  Bruno Mars song. And what they did is they kind of taped two individuals moving around in some space
[749.46 --> 756.58]  to kind of train on their movements and then the, and their body structure. And then they generated
[756.58 --> 763.02]  video of these two individuals dancing in the same way as in, as in the, uh, Bruno Mars and then a
[763.02 --> 768.06]  ballet video. And it's, it's just amazing. And I think you mentioned when, when you first showed,
[768.10 --> 773.78]  you know, some people, they didn't even realize that it was generated in, you know, videos of people.
[773.78 --> 777.08]  They thought they were actually dancing, uh, synchronized in that way.
[777.08 --> 782.06]  Yeah. It was actually my six-year-old daughter, Athena. Um, we were looking after you posted in Slack,
[782.06 --> 786.94]  I saw it and she heard the music on it and she comes running up to my laptop and we were looking
[786.94 --> 791.76]  at it and, you know, I'm marveling cause they, they showed in the video, which people can see in the
[791.76 --> 797.16]  show notes. They, they showed the video of the, of the source dancer. In one case, it was kind of a,
[797.16 --> 802.14]  you know, a funk type dance. And then there was a ballet dancer. And then the, these two people that
[802.14 --> 807.20]  they were using to, to superimpose the motion on and, and they didn't always line up. And so
[807.20 --> 813.00]  you'd have these, uh, these brief moments, these subtle moments where the body was doing things,
[813.06 --> 816.58]  the body couldn't do. And it was enough for me to, you know, I kind of knew what I was looking at,
[816.60 --> 823.00]  but my six-year-old daughter never realized that it was generated. Is she, she's grown up in a world,
[823.00 --> 827.86]  you know, where, where this is normal, you know, AI doesn't even phase her at her age. Cause she's
[827.86 --> 832.04]  seen it from me. And, and just like mobile technologies and everything else, it's, it's normal. But
[832.04 --> 836.72]  later on, I said, do you realize those people weren't actually moving like that? The computer made
[836.72 --> 841.82]  them do that. And she goes, no, I had no idea. I mean, you know, it's, and I'm just thinking just
[841.82 --> 845.50]  two or three years down the road, where's this going to go? You'll be unable to distinguish
[845.50 --> 851.14]  generated motion from, from real life. Yeah. I think, um, you know, not to give away all of our
[851.14 --> 856.40]  startup ideas and I guess you can scoop us if you like, but, uh, another startup we should create is,
[856.52 --> 863.32]  you know, the, uh, computer generation of, uh, music videos where we kind of, uh, make obsolete all of
[863.32 --> 869.26]  the music video dancers and just get their training data. And then we can reuse the same dancers in any
[869.26 --> 875.46]  sort of video and any sort of background and make it seem realistic. That's my, my second startup
[875.46 --> 880.52]  proposition. I'm, I'm all over it, but, uh, just so long as it doesn't involve, you know, the two of
[880.52 --> 885.42]  us out there dancing, you know, so long as we're not the models used in any of this stuff. Yeah. Well,
[885.48 --> 889.80]  I, I'm sure you could do better than those, those dancers in real life. I don't know about that.
[889.80 --> 896.00]  My, my, my, my wife would tell you not so much. So the last thing that I wanted to share, uh,
[896.00 --> 903.00]  with everybody is that Chris and I are going to be at O'Reilly AI in San Francisco, the O'Reilly AI
[903.00 --> 910.64]  conference, uh, which is, I believe going on when this airs, it will be going on this week. So if you
[910.64 --> 918.24]  are at O'Reilly AI in San Francisco, come find us. We'll be walking around doing some interviews. We'll
[918.24 --> 923.74]  have stickers. We'll have some nice swag and, and all sorts of stuff. So come and meet us. We'd love
[923.74 --> 929.00]  to hear from you. We'd love to hear about your ideas and discuss whatever topics you'd like. So,
[929.38 --> 935.72]  so come find us there. I'm really excited to, uh, to attend. And I second that we're, we're just there
[935.72 --> 941.82]  to meet everybody and to have conversations, uh, to do a bit of recording. So, um, don't be shy.
[941.94 --> 944.88]  We're looking forward to meeting lots of people, uh, in San Francisco.
[944.88 --> 951.16]  Definitely. Uh, well, let's go ahead and move on to some learning resources. This is the part of
[951.16 --> 955.68]  these type of shows where we just kind of share a couple of things that we've run across that have
[955.68 --> 962.90]  been useful in terms of learning new things, uh, within the AI ecosystem or new frameworks or,
[962.90 --> 968.78]  or new techniques or whatever it is. The first one that I found this week, which I don't think is,
[968.78 --> 976.38]  uh, you know, totally new, but it was new to me is, uh, the site that kind of creates a data
[976.38 --> 982.56]  visualization of a map of all of these different data science and machine learning books. So it's
[982.56 --> 990.42]  called, you know, hands-on machine learning. And it's kind of like a little roadmap of all of these
[990.42 --> 996.62]  different books that have been released on different subjects, like deep learning and Python
[996.62 --> 1001.94]  in general and beginner books and expert books. And it kind of guides you to the different sections
[1001.94 --> 1007.00]  that, that you might be interested in. So, um, if you don't know, you know, where to start or what
[1007.00 --> 1011.66]  books to look at, that might be a good place to just kind of explore what's out there and maybe
[1011.66 --> 1018.98]  avoid an expert book. If you're looking to, to begin and, and start out in AI, or maybe you're looking
[1018.98 --> 1022.46]  for a book specifically about deep learning or something like that.
[1022.46 --> 1027.38]  I think this is great. I had not seen this before, so I'm looking at the link, uh, at this point.
[1027.58 --> 1031.66]  And after we're done recording, I'm going to go, uh, snoop through it and see what I need to go get.
[1032.04 --> 1034.26]  Sounds good. What do you got for us this week, Chris?
[1034.38 --> 1040.84]  So I have, uh, there is a Udemy course that I decided to put that's pretty good. Um, it is a
[1040.84 --> 1045.98]  paid course, uh, and the, and the price typically, this is one of those things where I've never seen it
[1045.98 --> 1050.90]  at full price. It's always at some kind of discount. Currently it's $10 to get it, but it's called
[1050.90 --> 1058.32]  complete guide to TensorFlow for deep learning with Python. And it is, uh, quite lengthy actually,
[1058.32 --> 1064.42]  and you can kind of pick and choose, but it has 14 hours of on-demand video. And so, uh, if video
[1064.42 --> 1070.06]  is your thing in terms of learning, uh, it kind of takes you through everything from the beginning
[1070.06 --> 1074.78]  is kind of what is machine learning to an introduction to neural networks, TensorFlow basics,
[1074.78 --> 1082.20]  CNNs, RNNs, various, uh, other topics, uh, that they, that are kind of, uh, ancillary auto
[1082.20 --> 1087.50]  encoders, reinforcement learning, uh, and even generative adversarial network scans. And so that,
[1087.58 --> 1093.24]  that was, it had such a breadth of topics that it was covering that, um, for 10 bucks, I thought it
[1093.24 --> 1097.96]  was a pretty good, uh, pretty good investment to get people into. And so if you like to use Udemy
[1097.96 --> 1104.72]  as a platform for learning, then I recommend this one. It has, uh, 4.5 stars, uh, out of, uh,
[1104.92 --> 1109.44]  six and a half thousand ratings as I, as I read this on their website right now. So that's what
[1109.44 --> 1113.74]  I found. I thought it was a good thing for a beginner to get into. Awesome. And yeah, I should
[1113.74 --> 1119.42]  mention too, that if anyone out there is looking for books on specific subjects or looking for
[1119.42 --> 1125.10]  specific types of courses, or maybe just a GitHub repo that has some relevant examples,
[1125.10 --> 1130.68]  go ahead and, and jump over into our Slack channel. You can join the practical AI and
[1130.68 --> 1136.80]  changelog Slack team by going to changelog.com slash community. And there's a practical AI
[1136.80 --> 1142.08]  channel in there and just send us your question and we'll do our best to point you to whatever
[1142.08 --> 1146.50]  resources we know about, and maybe some other resources that our other listeners know about.
[1146.68 --> 1153.48]  So make sure and, um, leverage that. And otherwise we'll, uh, we'll reconvene next week. We're
[1153.48 --> 1159.56]  talking with Susan Etlinger about AI ethics, which I'm really excited about. I know you are Chris,
[1159.58 --> 1164.50]  because our listeners have expressed to us a lot that they want to hear about this topic. And I
[1164.50 --> 1170.54]  know I want to hear about it as well. And Susan's, uh, an expert will also be talking at O'Reilly AI
[1170.54 --> 1174.76]  about the same subject. So make sure and, and join us again next week.
[1175.02 --> 1180.32]  Yep. She is super impressive. I can't wait for that conversation. And, uh, as this gets released,
[1180.32 --> 1186.06]  uh, I will be seeing you within a couple of days at, uh, O'Reilly AI and we'll meet a whole bunch
[1186.06 --> 1190.02]  of our listeners and do some recording as we go. So I'm looking forward to this coming week.
[1190.26 --> 1192.14]  All right. See you there. See you there. Talk to you later.
[1195.14 --> 1199.30]  All right. Thank you for tuning into this episode of Practical AI. If you enjoyed the show,
[1199.36 --> 1204.26]  do us a favor, go on iTunes, give us a rating, go in your podcast app and favorite it. If you are on
[1204.26 --> 1208.04]  Twitter or social network, share a link with a friend, whatever you got to do, share the show with a
[1208.04 --> 1212.54]  friend. If you enjoyed it and bandwidth for change log is provided by fastly learn more at
[1212.54 --> 1216.84]  fastly.com and we catch our errors before our users do here at change law because of roll bar,
[1216.84 --> 1222.72]  check them out at robot.com slash change log. And we're hosted on Linode cloud servers at a
[1222.72 --> 1227.98]  lino.com slash change log. Check them out. Support this show. This episode is hosted by Daniel
[1227.98 --> 1233.42]  Whitenack and Chris Benson. Editing is done by Tim Smith. The music is by break master cylinder,
[1233.42 --> 1238.66]  and you can find more shows just like this at change law.com. When you go there, pop in your
[1238.66 --> 1243.54]  email address, get our weekly email, keeping you up to date with the news and podcasts for developers
[1243.54 --> 1247.84]  in your inbox every single week. Thanks for tuning in. We'll see you next week.
