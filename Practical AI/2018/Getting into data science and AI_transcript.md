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
[89.18 --> 94.84]  Welcome to Practical AI. How are you doing, Chris? I'm doing very well. How's it going today, Daniel?
[95.12 --> 99.50]  It's going really great. As you know, in my background, I started out in academia,
[99.50 --> 104.84]  and then I moved into industry to become a data scientist. And I'm really excited to have
[104.84 --> 109.30]  Himani Agrawal here with us, who has also made a similar transition. And we're going to kind of
[109.30 --> 115.38]  talk about some of that today and also what she's working on currently with AT&T. So welcome, Himani.
[115.38 --> 119.64]  Hi, Chris and Daniel. Thank you very much for having me. I'm excited to be here.
[119.88 --> 124.16]  Awesome. Yeah. Well, could you just give us a brief sketch of your background and what you're
[124.16 --> 129.66]  doing now? Sure. So my name is Himani Agrawal. I'm a machine learning engineer at AT&T,
[129.78 --> 136.84]  where I work on predicting the network outages and avoiding customer dispatch. My background is very
[136.84 --> 142.44]  interdisciplinary. I pursued a bachelor's in the area of civil engineering, where I was
[142.44 --> 149.42]  using the optimizational algorithm to find optimal slope of a dam. During my PhD, I was working on
[149.42 --> 156.08]  solving interdisciplinary problems in the area of HIV infection, applied mathematics, and computing.
[156.58 --> 161.98]  Awesome. Yeah, that's a really great background. And I'd love to dive into the individual pieces of
[161.98 --> 167.78]  that. So you mentioned kind of starting out more on the engineering side, specifically in civil
[167.78 --> 174.00]  engineering. Was kind of data analysis and machine learning and data science always something that
[174.00 --> 177.96]  you were interested in pursuing? Or how did that develop during your schooling?
[178.30 --> 184.14]  Yeah. So I believe I was meant to be a machine learning engineer. And I see machine learning is
[184.14 --> 191.56]  an optimization problem. My tryst with optimization began in my undergrad school, which is located in the
[191.56 --> 197.68]  flat regions in the foothills of the Himalayas. A lot of dams have been built in the upstream of the city.
[197.78 --> 204.60]  And determining the optimal slope of these dams is a very, very important optimization problem that
[204.60 --> 210.74]  the engineers have to solve. I got really interested in that problem as a civil engineer. And I started
[210.74 --> 215.20]  working on developing a model to determine the optimal slope based on features like the type of
[215.20 --> 221.30]  soil, the water retention of the soil, precipitation conditions, vegetations, and so on. And to solve
[221.30 --> 229.04]  these problems, I use genetic algorithms, which is based on Darwin's theory of evolution of human
[229.04 --> 237.40]  beings. And what interesting thing happened while I was solving that problem, that not just computations
[237.40 --> 244.34]  and applied maths and optimization, I also fell in love with computational biology. So I decided to pursue
[244.34 --> 252.34]  a PhD to solve biological problems in the area of computational biology. And during my PhD, I was
[252.34 --> 258.50]  working in a very interdisciplinary area in compassing fields like mechanics, biophysics, applied mathematics.
[258.50 --> 265.10]  I collaborated with applied mathematics lab at Rutgers University and materials science lab at Rice
[265.10 --> 274.16]  University to solve a very interesting problem of how can soft, how can rigid HIV proteins can make a
[274.16 --> 275.16]  cell membrane softer.
[275.16 --> 280.16]  So that sounds pretty amazing. It sounds like you've really known you wanted to be in this field
[280.16 --> 285.44]  for a long time. And so I guess, you know, I was, I was going to ask you if you were kind of
[285.44 --> 289.60]  thought about getting into data science as you were doing your PhD, but it sounds like from your
[289.60 --> 294.16]  undergrad, you already knew you wanted to do that. How young were you when you decided that this was
[294.16 --> 297.44]  the right path for you and that this is the way you wanted to go?
[297.44 --> 304.64]  So I've been really into mathematics and computing since I was a teenager. I decided to pursue engineering
[304.64 --> 308.72]  because I thought that involved a lot of mathematics and computing.
[308.72 --> 314.48]  Yeah. As you were kind of like having those passions for mathematics, when did you start first
[314.48 --> 316.44]  hearing about data science and AI?
[316.44 --> 323.56]  So during my undergrad, I got a chance to attend the Grace Hopper Celebration of Women in Computing
[323.56 --> 329.88]  in India. And I presented a poster at the conference. I was also a Grace Hopper scholar
[329.88 --> 336.84]  for the Indian version of the conference. And that's where I got in touch with the technology industry.
[336.84 --> 342.20]  So when I attended the conference, I came to know how my engineering and computing background can be
[342.20 --> 348.52]  directly applied to solve a variety of problems in the technology industry. And one thing I was always
[348.52 --> 353.72]  interested in is that I have a very varied interest, a lot of diverse interests, and I wanted to solve
[353.72 --> 360.20]  a variety of problems. I never wanted to solve or get stuck in solving just one problem. So when I saw
[360.20 --> 367.56]  in the area of technology, people work on multiple use cases and acquire the domain knowledge as they
[367.56 --> 374.20]  go forward with the project, I was really excited about the nature of solving problems in the technology
[374.20 --> 374.76]  industry.
[374.76 --> 380.52]  Awesome. Yeah. So for those that aren't familiar, what is the Grace Hopper Celebration?
[380.52 --> 386.92]  Grace Hopper Celebration of Women in Computing is the world's largest gathering of women technologists.
[386.92 --> 394.44]  Last year, 22,000 women attended this conference in Houston. It sells out within minutes. It's an amazing
[394.44 --> 398.68]  conference. I've been attending the conference for the last five years. I have been Grace Hopper
[398.68 --> 406.52]  scholar twice, one in 2013 for the Indian conference and in 2014 when I attended the Phoenix conference.
[407.64 --> 412.12]  It has a wonderful community of women technologists, and I really love to attend it.
[412.12 --> 417.32]  So what does it mean to be a Grace Hopper scholar? Could you kind of share what you've done it twice now,
[417.32 --> 421.24]  but for those of us who are not familiar with the details of it, could you tell us a little bit about it?
[421.24 --> 428.76]  As a Grace Hopper scholar, the Anita Borg Institute sponsors you to attend the conference. Many of the
[428.76 --> 433.96]  scholars are also either speaking at the conference or presenting a poster at the conference. There are
[433.96 --> 440.76]  very exclusive Grace Hopper scholar networking events that happen at the conference where we get to meet
[440.76 --> 448.28]  with mentors and industry sponsors. We have roundtable discussions. So apart from the general
[448.28 --> 453.96]  conference, Grace Hopper scholars have access to have a unique networking event at the conference.
[453.96 --> 460.20]  Apart from that, we have a Grace Hopper scholar Facebook group where we keep in touch with all
[460.20 --> 465.88]  the Grace Hopper scholars. And yeah, it's a wonderful community. We help each other and it's a great
[465.88 --> 472.52]  networking platform. Awesome. Yeah. And I mean, it sounds like it had a really huge impact on your life in
[472.52 --> 479.08]  terms of, you know, you knowing about the engineering field and knowing that you really enjoyed mathematics,
[479.08 --> 485.56]  but then seeing how those skills could be applied in so many different areas. It sounds like it was
[485.56 --> 490.68]  really a great inspiration for you. So that's awesome. We'll definitely put a link in the in the show
[490.68 --> 496.92]  notes so people can find out more. I'd be interested to hear a little bit, you know, coming from a PhD myself,
[496.92 --> 505.72]  I know it was a really kind of, I guess I should say weird experience going from a PhD into industry.
[505.72 --> 511.00]  And I know I had to learn a bunch of different jargon and find my own way through that. I was
[511.00 --> 516.36]  wondering if you could speak to that yourself. Did you find that to be a similarly weird transition or
[517.00 --> 523.64]  how did you go about going from academia to industry? So my first experience with industry was
[523.64 --> 530.52]  when I got an internship with Microsoft Research. That's the first time in 2015 I interned with
[530.52 --> 535.56]  Microsoft Research. There was a group in Microsoft Research which works in the area of computational
[535.56 --> 542.60]  immunology and I joined them as a HIV domain expert. That was the problem I was solving during my PhD.
[542.60 --> 547.16]  I was working with a machine learning group at Microsoft Research, although my background was not
[547.16 --> 553.40]  in the area of machine learning and data science in the traditional sense. So it was great to contribute
[553.40 --> 560.84]  my domain knowledge to the projects at Microsoft Research. But I was also very inspired to see
[560.84 --> 566.12]  the kind of problems that the researchers there were solving, not just in the area of immunology,
[566.12 --> 571.96]  but in a variety of domains. And again, I said the very fact that technology, data science and machine
[571.96 --> 579.24]  learning helps me solve a variety of problems. That's what excites me. So apart from Grace Hopper Conference,
[579.24 --> 585.56]  that was a great platform where I got a first-hand experience seeing how machine learning can be
[585.56 --> 591.16]  applied to a variety of projects. Oh, that's pretty cool. So you also did an immersive data
[591.16 --> 595.72]  science program with Galvanize, right? You know, why did you do it and would you do that again? And,
[595.72 --> 600.60]  you know, could you just tell us a little bit about what that's like? Yeah, sure. Galvanize data science
[600.60 --> 605.96]  immersive program was a very transformational experience for me. When I finished my PhD,
[605.96 --> 611.88]  I knew that I wanted to join the technology industry. I had all the technical skills. I had
[611.88 --> 619.08]  great computational skills, but I just didn't know how to really be a data scientist in the technology
[619.08 --> 626.44]  industry. And Galvanize made that happen. Galvanize data science immersive is a 12 week 500 plus hour
[626.44 --> 631.80]  program that teaches industry standard data science tools and knowledge and statistical analysis,
[631.80 --> 638.68]  machine learning algorithms and data engineering. So it's during that program, it equipped me with
[638.68 --> 644.76]  the right skills, which made me transition into the tech industry. That sounds cool. Did it,
[644.76 --> 649.24]  so I'm kind of curious when you got to the end of that and, you know, thinking about the fact that you,
[649.24 --> 655.72]  you are now an AI engineer at AT&T, did that Galvanize training help you bridge that to the real world
[655.72 --> 661.72]  so that you could enter that job and be productive? Yes. So during the Galvanize program, we went through
[661.72 --> 669.80]  several projects, applied projects. And I also did an internship with machine learning for genomic
[669.80 --> 675.80]  medicine-based startup, Sympatica Medicine, where I worked on machine learning for early diagnosis of
[675.80 --> 682.68]  Parkinson's disease from RNA sequencing data. So the Galvanize program provided a great platform for me
[682.68 --> 689.88]  to not just learn the tech skills, but also apply it to a real world problem with a company. So that
[689.88 --> 697.00]  experience was very valuable. And then on the side, I also joined Jeremy Howard's fast.ai deep learning
[697.00 --> 702.60]  class at University of San Francisco, which was a great program. Jeremy Howard is a great teacher. I
[702.60 --> 709.56]  really enjoyed that class and I built my deep learning skills during that program. I was also working at
[709.56 --> 717.00]  Augment Solutions, which is a machine learning for customer experience based company. Does that sound
[717.00 --> 723.48]  right? Yeah. Where I was working on churn prediction from Frontier customer chats data. So this whole
[723.48 --> 730.20]  experience was possible only because of the Galvanize program. And then I transitioned into a full-time role
[730.20 --> 737.56]  at AT&T. Yeah. It's really great for me to hear that from you. Cause sometimes I think I myself, I feel pretty
[737.56 --> 744.68]  self-conscious in the industry because I also came from a non kind of a CS and machine learning
[744.68 --> 750.92]  focused background. I'm always learning new, new jargon that I wasn't exposed to before. I remember,
[750.92 --> 755.40]  you know, coming from academia, it's like when I realized that when people were talking about
[755.40 --> 760.36]  these regressions, it was really just like ordinarily squared. I remember like having these
[760.36 --> 766.52]  light bulb moments when I kind of understood, Hey, I did this back in science, but now it applies here.
[766.52 --> 772.52]  I was wondering if you've also kind of felt that way coming through this transition and what advice
[772.52 --> 779.08]  you have for students coming from engineering or science backgrounds and wanting to transition into
[779.08 --> 786.36]  data science and AI. I definitely felt that way. I realized that during my PhD, I was working on solving
[786.36 --> 792.84]  optimization problems, which are very similar to the problems in the data science industry,
[792.84 --> 800.04]  but I was not using the same jargons that are being used in the tech industry. So by being part of
[800.04 --> 808.04]  galvanized program, I got to learn data science in the tech way. So that really helped me a lot. And it
[808.04 --> 815.00]  helps me even today in my job at AT&T. Coming to your second question, how can people from different
[815.00 --> 820.44]  backgrounds can enter into data science? I believe that machine learning and data science is very
[820.44 --> 826.20]  ubiquitous right now. There is a huge scarcity of machine learning and data science expertise.
[826.76 --> 833.08]  So it's great if people from different backgrounds can enter into that field because that would really
[833.08 --> 839.40]  spark creativity. I think it's great that you're kind of exposing some of these things. I think some of
[839.40 --> 845.56]  people from engineering and science feel like, oh, you should just kind of know all this jargon and all of
[845.56 --> 850.68]  that stuff. But most people are trying to pick up either the computer science and programming pieces
[850.68 --> 855.96]  or the science pieces or the optimization pieces. I don't know if you know this, Chris, but I went
[855.96 --> 862.44]  through a similar transition and utilized the Thinkful course, which I think is now kind of like an online
[862.44 --> 869.96]  boot camp to get up on some of this jargon. So I had no idea. Yeah, I never knew that. I would similarly
[869.96 --> 876.76]  recommend. I think Amani hit the nail on the head that it's a great time to get into this field and
[876.76 --> 882.36]  don't let that kind of lack of jargon scare you away. But there's a lot of resources out there that
[882.36 --> 887.48]  you can use. So you two have made me want to go and get in a boot camp right now after hearing both
[887.48 --> 894.28]  of you talk about it. And what sort of events and opportunities are there with Women Who Code or
[894.28 --> 898.44]  Women in ML, these different organizations? What sort of things are available?
[898.44 --> 906.12]  So there are a lot of machine learning communities out there. For example, Women in Machine Learning
[906.12 --> 911.80]  and Data Science organizers, there are a lot of Women in Machine Learning and Data Science groups
[911.80 --> 919.24]  all over the world. And they organize technical talks at company where we get to meet with machine
[919.24 --> 925.32]  learning technologists from varied backgrounds. I remember I attended a talk at the Chan Zuckerberg
[925.32 --> 933.00]  initiative and that was great. Apart from that, I know WimelDS in San Francisco, they organize a
[933.00 --> 939.88]  code and coffee session every Friday. I think it's a great chance for aspiring data scientists to be
[939.88 --> 946.52]  involved in that community so that they can receive mentorship from experienced women. I've also been a
[946.52 --> 954.28]  part of Women in Machine Learning. It's a community that organizes a one-day workshop and luncheons at
[954.28 --> 961.48]  conferences like NIPS and ICML. I attended Women in Machine Learning workshop last year at NIPS. It was a
[961.48 --> 968.68]  great experience for me. Yeah, that's awesome. It's kind of one of my goals to go to NIPS sometime. I
[968.68 --> 975.16]  haven't been yet. It's another one of those that sells out like a Taylor Swift concert. But I know
[975.16 --> 981.72]  you were mentioning before the show as well, Hamanie. Aren't you involved with MLConf? Maybe you could
[981.72 --> 986.44]  share a little bit about that. I know you've shared a lot of great community things, but I think you're
[986.44 --> 993.32]  pretty active also in the greater machine learning community. So tell us a little bit about MLConf and
[993.32 --> 998.76]  what you're doing with that. I'm excited to tell you about the upcoming MLConf in San Francisco that's
[998.76 --> 1005.00]  happening on November 14. It's a single-day, single-track conference. It has amazing programming in the
[1005.00 --> 1011.32]  area of applied AI from top industry AI experts. If anyone wants to go, I have a 20% discount for them.
[1011.32 --> 1017.64]  They can use Hamanie20 and get 20% off the conference registration. Awesome. Yeah, and we'll put
[1017.64 --> 1022.84]  that in the show notes as well. It sounds like a great opportunity. I appreciate your efforts and
[1022.84 --> 1027.00]  helping to organize that. All right. As we come back out of our break,
[1027.00 --> 1033.16]  Hamanie, I'm going to turn us toward telecom since you are an AI engineer at AT&T. I wanted to start
[1033.16 --> 1037.80]  with kind of a general question and just ask, what are some of the main uses of machine learning
[1037.80 --> 1042.36]  and artificial intelligence in telecom? I would like to talk about telecom industry
[1042.36 --> 1048.76]  from AT&T perspective. AT&T, for me, is first and foremost a modern media company, which is
[1048.76 --> 1054.20]  empowered by telecommunication engineering, television engineering, and advertising analytics,
[1054.20 --> 1061.16]  along with our subsidiaries, HBO, CNN, Turner, Warner Brothers Entertainment, Xander,
[1061.16 --> 1068.04]  Alien Vault, and Magic Leap, truly sky is the limit with what machine learning problems can be solved
[1068.04 --> 1075.16]  at AT&T. Within AT&T, I work with an organization called Chief Data Office. It's a really wonderful
[1075.16 --> 1082.04]  organization and very young too, where I work with AT&T business units to develop automation solutions.
[1082.04 --> 1090.04]  We collaborate extensively with AT&T labs and use the research innovations that spin out of the labs in our
[1090.04 --> 1097.48]  applied AI projects in the Chief Data Office. As a machine learning engineer, I work on data analysis and
[1097.48 --> 1104.36]  pattern recognition of telecommunication devices and streaming alarms data to predict network outage and
[1104.36 --> 1112.44]  avoid customer dispatches. Furthermore, our devices have been impacted due to the recent hurricanes. So, I'm working
[1112.44 --> 1119.32]  on utilizing the weather, flood, and power data in conjunction with the streaming alarms data to predict the optimal
[1119.32 --> 1127.32]  dispatch time to restore the devices. Apart from that, AT&T has been a pioneer in the area of 5G,
[1127.32 --> 1134.04]  and I believe 5G, when combined with Magic Leap, in conjunction with machine learning,
[1134.04 --> 1140.04]  is truly game changing for personalized customer engagement for TV streaming.
[1140.04 --> 1149.56]  Well, I am just super impressed to hear all, I mean, coming from optimizing dams to working in
[1149.56 --> 1158.28]  computational biology to helping with, you know, disaster related recovery within telecom. All of this is
[1158.28 --> 1164.28]  definitely super inspiring to me. It sounds like your team, this Chief Data Office, it's kind of, like you said, it's
[1164.28 --> 1170.28]  positioned between research and the rest of the company. So, do I have it right that you're kind of more on the
[1170.28 --> 1176.36]  applied side that you take kind of some of the things that are coming out of research and kind of try to
[1176.36 --> 1179.96]  figure out how to apply them within the rest of the company? Is that right?
[1179.96 --> 1187.16]  Yeah, that's quite right. AT&T Chief Data Office is on the production side of things. We want to deploy machine
[1187.16 --> 1189.00]  learning solutions at scale.
[1189.00 --> 1196.52]  Awesome. Coming kind of from more the academic research side, have you been surprised at all by some
[1196.52 --> 1203.00]  of the challenges that are involved in kind of taking and applying those research things to a larger scale
[1203.00 --> 1204.44]  within a company context?
[1204.44 --> 1210.92]  I've seen a lot of commonalities between my research experience and my experience right now as a data
[1210.92 --> 1218.36]  scientist. For example, during my research, when we come up with a research problem, it's so hazy. We go
[1218.36 --> 1226.04]  out there, read all the research papers and try to figure out the problems that we have to solve. Similarly, at AT&T,
[1226.04 --> 1233.32]  when we work with the business units, we get tons of data and we have to figure out what kind of
[1233.32 --> 1239.48]  problems that can be solved. That's very similar to what we do as researchers. First, figure out the
[1239.48 --> 1242.28]  problems that we can solve and execute them.
[1242.28 --> 1247.72]  So, I have a follow-up question. You just mentioned when you work with business while you're doing that.
[1247.72 --> 1251.80]  I was wondering if you could actually share with us some of the things that you are working on.
[1251.80 --> 1253.96]  Kind of tell us what you're doing on a day-to-day basis.
[1253.96 --> 1261.80]  Yeah, sure. So, as I mentioned, I'm working on the data analysis on the streaming alarms data that
[1261.80 --> 1269.80]  come out of the telecommunications devices. And from that data, I try to figure out the root causes
[1269.80 --> 1276.36]  of the network outage. And by doing that, I'm preventing a dispatch to a customer's house.
[1276.36 --> 1281.96]  That is super cool. Yeah, it is really cool. And so, the data that you're processing is actually kind
[1281.96 --> 1288.68]  of streaming off of all of the AT&T-related devices, right? And then you're kind of detecting network
[1288.68 --> 1296.52]  outages. Is that right? Yeah. So, I have a topology with me. And from that,
[1297.08 --> 1302.44]  from all the alarms that are being generated from the network, I try to find out where exactly
[1302.44 --> 1307.16]  in the network the problem arrives. So, the dispatch can be sent to that particular location.
[1307.16 --> 1311.72]  That is cool. So, I didn't mention at the beginning of the show, but about 20 years ago,
[1311.72 --> 1317.16]  I worked for AT&T in network engineering. And honestly, we did not have any machine learning,
[1317.16 --> 1321.16]  at least that I was aware of at the time. So, I can tell you going back and thinking of the pain
[1321.16 --> 1325.96]  of putting together networks, I wish we had had someone like you there then to help us get through
[1325.96 --> 1330.20]  these kind of difficult things. So, I was just, I couldn't help but think about that as you were
[1330.20 --> 1333.56]  describing your daily duties. I didn't know you worked at AT&T.
[1333.56 --> 1338.52]  Yeah. And actually, I don't know that I've mentioned it on this show before, but my first job as a data
[1338.52 --> 1346.36]  scientist was with a VoIP startup, Voice over IP. And I know that we had in our mind kind of envisioned
[1346.36 --> 1351.48]  some of the things that you're talking about. So, it's just like really cool to see people actually
[1351.48 --> 1358.12]  kind of putting this into practice. I know it's not an easy problem to solve at all.
[1358.12 --> 1360.36]  So, is that when you got into AI?
[1360.36 --> 1367.32]  It was, yeah. I was in my PhD. I came out into industry. I was actually working at an IP firm.
[1367.72 --> 1372.98]  And that's when I was doing the Thinkful program. And then right after that, I started my very first
[1372.98 --> 1377.60]  data science job with this VoIP company called Telnix, which is still around actually. It's kind
[1377.60 --> 1383.56]  of a voice over IP and doing like number porting and all of that stuff via API.
[1384.12 --> 1384.34]  Yeah.
[1384.34 --> 1390.66]  So, I kind of wanted to dig into one more piece. You mentioned kind of magic leap and machine learning
[1390.66 --> 1397.06]  and other things. I was wondering, you know, as you look forward into the future of kind of the media
[1397.06 --> 1404.50]  and telecom industry, what are you excited about in the future that you could see maybe AI enabling?
[1404.98 --> 1410.10]  Yeah. So, I'm really passionate about music. I'm an opera singer.
[1410.48 --> 1412.08]  Oh, wow. That's awesome.
[1412.08 --> 1413.86]  That's cool. Are you going to sing for us now?
[1414.34 --> 1416.44]  No, not now.
[1417.20 --> 1419.90]  Oh, okay. I had to ask. Okay. I had to ask.
[1420.02 --> 1425.70]  Well, if you have any videos or links to you singing, we would love to include them in the
[1425.70 --> 1427.04]  show notes. It's awesome to hear.
[1427.06 --> 1432.14]  Yeah. I do have my performances. And actually, I also currently train with a University of
[1432.14 --> 1436.72]  North Texas voice professor in Italian singing as a mezzo-soprano.
[1437.06 --> 1442.18]  So, that is super cool. Actually, there's another connection we have. I'm not currently a singer,
[1442.18 --> 1446.78]  but when I was young, grew up in the Atlanta boy choir. And it's not something I was ever expecting
[1446.78 --> 1450.26]  to say on this podcast. But there's a little connection.
[1450.26 --> 1451.84]  Yeah. I'd love to hear more.
[1451.84 --> 1457.70]  I'm continually amazed with all of the things that you're able to do. You do the opera singing,
[1457.70 --> 1461.82]  and then you were kind of mentioning, you know, I think that was leading to something
[1461.82 --> 1466.72]  with the question of what kind of is inspiring to you in media and with AI.
[1466.72 --> 1471.78]  Yeah. So, the reason I'm so much interested in the media company is because I'm passionate
[1471.78 --> 1479.02]  about music. And I'm very interested in exploring research in the area of reinforcement learning
[1479.02 --> 1483.54]  and score following. So, that's my side research passion.
[1483.76 --> 1488.06]  That's awesome. Have you seen the stuff coming out of, I think it's Project Magenta?
[1488.42 --> 1493.98]  Yeah. That's a very cool project. I was particularly impressed with this project called AI Duet,
[1493.98 --> 1499.92]  in which the random notes laid by the user on their interface are turned into a beautiful melody.
[1500.40 --> 1503.04]  That was a very cool project that came out of Magenta.
[1503.38 --> 1506.92]  Oh, that's amazing. Yeah. So, do you ever see yourself in the future,
[1507.14 --> 1510.30]  kind of devoting more of your time to music and AI?
[1510.60 --> 1515.62]  I'm definitely very interested in it. I am very much interested to explore the realm of
[1515.62 --> 1519.56]  how reinforcement learning can be applied to music. I'm very excited about that area.
[1519.56 --> 1525.00]  So, when you delve into that, you'll have to come back on the show and share with us a reinforcement
[1525.00 --> 1530.28]  learning within music topic with us so that we can learn a little bit about that. That is one topic
[1530.28 --> 1534.28]  we're hitting reinforcement learning on the show, but we've never combined that with music.
[1534.36 --> 1537.12]  That would be great. I will keep you updated.
[1537.66 --> 1544.86]  Sounds great. I had another kind of question about your current work. And you mentioned that you're an AI
[1544.86 --> 1549.66]  engineer, and I know that there's a lot of different kind of labels that people are putting
[1549.66 --> 1554.46]  on those in industry doing AI and machine learning. Sometimes they're called data scientists or
[1554.46 --> 1559.56]  analysts or machine learning engineers or AI engineers. I was wondering, from your perspective,
[1559.56 --> 1564.66]  is there a difference in those things? Do you work with data scientists as well? Or how does
[1564.66 --> 1571.04]  engineering fit into AI? Yeah, that's a great question. So, my formal position is that of a data
[1571.04 --> 1578.96]  scientist, but I do apply machine learning. I do use deep learning, and I solve challenging problems
[1578.96 --> 1584.42]  in this area, which is the concept of AI. AI is a concept and a dream that the machines can see,
[1584.74 --> 1589.88]  machines can hear, and machines can be creative. So, I apply all of that in my role. So, that's how I
[1589.88 --> 1595.94]  see myself as an AI engineer. I believe that although there are a lot of titles that have come up recently,
[1595.94 --> 1603.90]  they are one and the same, in my opinion, because as my job in this whole realm, I have to use all the
[1603.90 --> 1610.60]  tools and technologies in multiple domains. So, even though different terms have come up,
[1610.80 --> 1615.96]  a data scientist or a machine learning engineer has to be well-equipped with multiple skills.
[1616.52 --> 1620.66]  That sounds really cool. I have a question, because as you're kind of talking about how those are going
[1620.66 --> 1626.92]  together, when you're working with co-workers that are not in data science and not in AI, I'm curious,
[1627.04 --> 1632.24]  what is their perception of you now bringing AI? Because, I mean, with this being, you know,
[1632.30 --> 1637.66]  relatively new to the industry and certainly in kind of a production role, as you talk to these
[1637.66 --> 1643.26]  co-workers, how do they perceive you and the job you're doing? So, my co-workers who are not data
[1643.26 --> 1647.02]  scientists, who are not machine learning engineers, believe that machine learning is magic,
[1647.02 --> 1652.14]  because all the work that was being done by human beings are now being done by machines.
[1652.50 --> 1657.30]  Machines are getting more intelligent and I feel it appears like magic to a lot of people,
[1657.54 --> 1662.20]  but I really believe at the very end, machine learning is mathematics deriving patterns from
[1662.20 --> 1668.84]  data and it's only as good as the data that we have. Yeah, that's a great point. I think that's a
[1668.84 --> 1676.26]  really great way to end up our conversation here, is really with that emphasis on the applied side and
[1676.26 --> 1683.18]  really emphasizing that AI is a set of methods that we apply in a predictable way. I was wondering
[1683.18 --> 1688.76]  if you want to share any about where people can find you online and maybe, you know, either on the
[1688.76 --> 1694.30]  AI side or the opera side or wherever and we'll kind of end up after that. Yeah, so I'm on LinkedIn,
[1694.68 --> 1699.62]  Twitter, I have two YouTube videos of my performance. I would be happy to share the links.
[1699.62 --> 1706.82]  Awesome. Great. Well, thank you so much for joining us, Amani. It's been fascinating to hear about your
[1706.82 --> 1713.00]  journey and what you're working on. I know me for one, I'm super impressed. And so thank you so much
[1713.00 --> 1716.22]  for being on the show. Thank you very much. Thank you so much for having me.
[1718.30 --> 1722.96]  All right. Thank you for tuning into this episode of Practical AI. If you enjoyed the show, do us a
[1722.96 --> 1727.96]  favor, go on iTunes, give us a rating, go in your podcast app and favorite it. If you are on Twitter or
[1727.96 --> 1731.26]  social networks, share a link with a friend, whatever you got to do, share the show with a
[1731.26 --> 1735.74]  friend if you enjoyed it. And bandwidth for changelog is provided by Fastly. Learn more at
[1735.74 --> 1740.00]  fastly.com. And we catch our errors before our users do here at changelog because of Rollbar.
[1740.26 --> 1745.42]  Check them out at rollbar.com slash changelog. And we're hosted on Linode cloud servers.
[1745.78 --> 1750.78]  Head to linode.com slash changelog. Check them out. Support this show. This episode is hosted by
[1750.78 --> 1756.64]  Daniel Whitenack and Chris Benson. Editing is done by Tim Smith. The music is by Breakmaster Cylinder.
[1756.64 --> 1761.86]  And you can find more shows just like this at changelog.com. When you go there, pop in your
[1761.86 --> 1766.74]  email address, get our weekly email, keeping you up to date with the news and podcasts for developers
[1766.74 --> 1771.02]  in your inbox every single week. Thanks for tuning in. We'll see you next week.
[1777.02 --> 1781.92]  I'm Tim Smith and my show away from keyboard explores the human side of creative work.
[1781.92 --> 1787.46]  You'll hear stories sometimes deeply personal about the triumphs and struggles of doing what
[1787.46 --> 1794.24]  you love. I need to give myself permission to not overdo it. If I know that the weather forecast is
[1794.24 --> 1797.88]  really good tomorrow and I don't have to do a podcast tomorrow and I could go to the beach,
[1798.06 --> 1802.90]  maybe I go to the beach. Maybe I do something that is not work. New episodes premiere every other
[1802.90 --> 1807.92]  Wednesday. Find the show at changelog.com slash AFK or wherever you listen to podcasts.
[1807.92 --> 1809.92]  You'll see you next week.
