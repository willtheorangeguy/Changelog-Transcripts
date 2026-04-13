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
[89.18 --> 95.28]  Welcome to Practical AI. I'm Chris Benson, one of your co-hosts. And with me is my partner,
[95.54 --> 99.14]  Daniel Whitenack. How's it going today, Daniel? It's going great. How about with you, Chris?
[99.30 --> 104.70]  I'm doing well. It's been a long time since we have put out a new show. So this one is long overdue.
[104.80 --> 109.10]  What have you been up to lately? I've kind of been doing a little bit of traveling. Went out to
[109.10 --> 114.20]  O'Reilly AI. Recorded a couple episodes there, which have been released. That was a lot of fun.
[114.20 --> 120.76]  Went on a little bit of vacation and also learned a little bit of data visualization stuff with a
[120.76 --> 127.30]  package called Vega, which that was fun. But yeah, glad to be back on the show. I know you've had
[127.30 --> 133.54]  some health broken bone issues, so I'm glad to see you're back in action and great to be recording
[133.54 --> 137.52]  with you again. Yeah, it's good to be back after MIA for a little while. For our listeners,
[137.84 --> 143.64]  I was actually going to be at O'Reilly AI in San Francisco with Daniel to do recording for those
[143.64 --> 149.82]  last couple of episodes that we had of those. And I missed it because like two hours before
[149.82 --> 155.42]  I was supposed to be at the airport, I broke my foot. And so I ended up going to the emergency
[155.42 --> 160.96]  room and calling Daniel from the emergency room going, I'm not going to make it. So thank you so
[160.96 --> 165.20]  much for handling all that alone. I know you were even fighting a cold off with losing your voice.
[165.20 --> 170.88]  And so you had your hands full. Well, it was you were missed, but the next conference,
[170.88 --> 176.28]  we'll do that one together. And I should say too, for the for the listeners, if first off,
[176.32 --> 182.48]  we'd love to have you join our Slack community at changelog.com slash community. And we'd love to
[182.48 --> 191.64]  hear about what events you're going to be at, whether that's O'Reilly AI or ODSC or Strata or
[191.64 --> 197.16]  machine learning, applied machine learning days or MLConf, whatever, whatever ones you're going to be at,
[197.16 --> 202.40]  let us know and let us know if if you'd like us to be around at those at those conferences,
[202.54 --> 207.24]  recording some content and and interacting with the community. We'd love to meet some of you.
[207.60 --> 213.28]  So yeah, and we get great feedback from you guys on in the Slack community. And we also have a fairly
[213.28 --> 219.18]  new LinkedIn group called Practical AI. So if you're on LinkedIn, I invite you to join that because we
[219.18 --> 224.60]  have some conversation going there as well. And and yeah, I guess it's good to be back on the podcast.
[224.60 --> 230.78]  Now I've done a couple of of conference keynotes in recent days, and I've been hobbling around on my
[230.78 --> 237.94]  cast. So I'm sure I looked quite comical as I walked up to the podium. So anyway, on to the show today.
[238.08 --> 243.08]  Daniel, you want to start us off? Yeah, sure. So it has been a while since we've had this sort of
[243.08 --> 248.52]  conversation. We're going to do another kind of news and update show for you guys. There's been a ton of
[248.52 --> 254.72]  news in the AI community over the past few weeks. So we're going to dive into some of that and discuss
[254.72 --> 260.68]  it and and let you know about some of the things that were on our radar over the last three or four
[260.68 --> 265.80]  weeks. And also, we're going to share with you a couple of new learning resources if you're trying
[265.80 --> 270.98]  to level up your AI game or maybe you're just getting into the community and want to start
[270.98 --> 275.74]  experimenting. We're going to point you to a couple of those resources later in the show. So stick around
[275.74 --> 282.28]  for that. But to start us out, I'd love to just start by some big news in the community over the
[282.28 --> 289.76]  last few weeks, which has been around PyTorch version 1.0. So in my understanding, at least at
[289.76 --> 297.60]  the time of this recording, PyTorch 1.0 is in kind of its preview or release candidate stage. Maybe by the
[297.60 --> 302.88]  time it releases, it'll it'll actually have the have the full release cut. But first off, I mean,
[302.88 --> 307.24]  we just want to congratulate the PyTorch team. That's a it's a huge accomplishment getting to
[307.24 --> 313.56]  version 1.0. And we're really yeah, I'm really excited about it. I just want to pass on, you know,
[313.60 --> 319.76]  our congrats to that team. And also, I mean, this is just it seems like the community is really
[319.76 --> 326.32]  latching on to this. Even, you know, Google Cloud is implementing a lot of implement PyTorch
[326.32 --> 331.70]  implementations in their in their images and other things. And so, yeah, it's it's really great to see
[331.70 --> 337.08]  this. What do you think, Chris? I think PyTorch is really rocking right now. It has come on so strong
[337.08 --> 342.84]  in the last year. And, you know, it is really just talking to people. So there's no scientific basis
[342.84 --> 348.38]  to this when I say it. But just observing, I mean, that I really am hearing a lot about PyTorch. And
[348.38 --> 352.86]  then obviously TensorFlow, which is, you know, been big for a while and talk about that in a moment. But
[352.86 --> 358.62]  PyTorch team, you're really rocking. And so keep up the great work. It is a fantastic framework to work
[358.62 --> 365.16]  with. Yeah. And I think maybe this is a good opportunity to just kind of give some perspective,
[365.46 --> 370.78]  at least from our very biased perspective, as far as the PyTorch and the TensorFlow community,
[371.02 --> 375.40]  the state of them, if they're kind of I don't know, Chris, do you think that they're kind of
[375.40 --> 381.40]  reaching different segments of the of the community? And who do you see using one or the other?
[381.40 --> 388.50]  So it's kind of funny, I see historically PyTorch, among the people I'm running around with in data
[388.50 --> 393.82]  science and AI, on a day to day basis has really been in the academic and research arena. And then
[393.82 --> 400.48]  to contrast that TensorFlow was kind of dominating the kind of corporate production teams, but PyTorch
[400.48 --> 406.04]  on their on their front page right now, in big letters, it says from research to production. And I
[406.04 --> 411.14]  think that captures exactly the feeling of where they've been going is they've have moved to compete
[411.14 --> 417.20]  with TensorFlow squarely on that corporate roll things out to production front and compete with
[417.20 --> 423.32]  TensorFlow's existing tools that have been out there. PyTorch is now becoming just a powerhouse,
[423.48 --> 428.62]  not only in academia, but for corporate teams that once upon a time really would only have said,
[428.74 --> 432.84]  well, we got to do TensorFlow for what they have in terms of getting this stuff out in the world.
[432.84 --> 439.24]  So I'm just really happy to see PyTorch coming on the way they are. And from research to production
[439.24 --> 443.66]  is the perfect attitude for that team, from my perspective as an outsider.
[444.06 --> 448.70]  Yeah, I think you've hit the nail on the head with that. I really see in the blog posts that
[448.70 --> 455.36]  I've read about PyTorch version 1.0, it does seem like a lot of the emphasis is on production,
[455.62 --> 461.22]  quote unquote production or system integration, scaling out sort of things. Some of the things I'm
[461.22 --> 466.24]  really excited about is their really tight integration with the ONIX neural network exchange
[466.24 --> 472.08]  format, which standardizes kind of model format, you know, across PyTorch and scikit-learn and
[472.08 --> 477.84]  MXNet and all of these things. So you can train your PyTorch model and then export it in this way and
[477.84 --> 483.00]  then serve it with MXNet. Stuff like that is just really cool. Also, you know, integrations that
[483.00 --> 488.92]  they're working on with things like Kubeflow, which is a set of standards for deploying machine learning
[488.92 --> 496.64]  technology on top of Kubernetes, which of course really kind of zeros in on making PyTorch really
[496.64 --> 503.18]  useful at scale in a company's infrastructure. And then, of course, we see things even from Google
[503.18 --> 510.76]  Cloud that where they're working on integrations of PyTorch with TPUs, which is Google's accelerator
[510.76 --> 517.98]  technology, kind of similar to GPUs, but different as we learned last week from our guests from NVIDIA.
[517.98 --> 524.26]  But they're also integrating PyTorch to be able to be used with TPUs. And so there's a lot of
[524.26 --> 529.54]  emphasis on that front. And for one, I'm really happy to see that because I think from my experience,
[529.54 --> 534.72]  that's a lot of times where people get blocked in terms of implementing and applying these methods.
[535.22 --> 539.50]  Yeah. The things that they call out as kind of highlights on their feature page include
[539.50 --> 544.76]  hybrid front end, distributed training, Python first, tools and libraries, native ONIX support,
[544.76 --> 550.60]  C++ front end, and then cloud partners. And all of those, especially the cloud partners,
[550.78 --> 555.24]  you know, where TensorFlow has been so dominant lately that it's great seeing. I love having
[555.24 --> 561.56]  choice. I love having the option to go where I want. And so big congratulations to the PyTorch team.
[561.92 --> 568.10]  Yeah. And I think that it's really cool to see that interoperable stuff because I think the PyTorch
[568.10 --> 573.18]  and the TensorFlow community are just both very, very vibrant. I mean, there's TensorFlow Dev Summit,
[573.30 --> 578.84]  which is, is, has a lot of momentum. There's, there's the PyTorch dev conference, I forget what
[578.84 --> 583.42]  they call it. We're just seeing about that. And both just are really vibrant. And of course, the
[583.42 --> 588.80]  online community, the open source community. I think one of the things that, you know, I always
[588.80 --> 594.78]  appreciated, and I use PyTorch now probably a little bit more than TensorFlow. But one of the things I
[594.78 --> 601.82]  always appreciated about PyTorch was the kind of Pythonic way it allowed you to build up AI
[601.82 --> 608.98]  applications without having to worry about like the static graph computations that were, that were
[608.98 --> 614.02]  in TensorFlow. But I know that that's, that's actually changing as well. And you were telling
[614.02 --> 621.06]  me a little bit about that. So what's going on there? So TensorFlow 2 has been, been discussed
[621.06 --> 625.18]  with the TensorFlow team, they made an announcement a couple of months ago, and then they've updated
[625.18 --> 631.12]  the site. And ironically, I think that part of the motivations in TensorFlow 2 that we'll address
[631.12 --> 636.86]  here kind of come from that, that competition with the PyTorch team, because, you know, PyTorch is,
[636.96 --> 643.26]  has been considered to be because of that, that kind of putting Python first mentality, it's been so
[643.26 --> 649.04]  easy to use. And TensorFlow has been notoriously difficult because of the graph mode. And so one of the
[649.04 --> 653.20]  big highlights of TensorFlow 2 is that they're putting the eager execution, which has been out
[653.20 --> 658.54]  recently, is the primary mode now. So you'll start in eager execution. And then if for performance
[658.54 --> 662.64]  reasons, or a variety of other reasons, you want you're ready to move into graph mode, then you can
[662.64 --> 667.64]  do so. But I think a lot of people are going to welcome that ease. There was a video that I saw
[667.64 --> 673.78]  recently where they were comparing the two frameworks, and they were showing kind of TensorFlow 1 versus
[673.78 --> 679.96]  TensorFlow 2 syntax. And you could just see it, it was much more readable. And it was a lot, it was
[679.96 --> 684.42]  just, you know, putting Python first again. And so that was nice to see. And they're increasing support
[684.42 --> 689.86]  for for platforms on the TensorFlow side, and they're starting to remove deprecated APIs and things like
[689.86 --> 695.56]  that in 2.0. So I, for one, am really looking forward, not only to this PyTorch 1.0 release, but also
[695.56 --> 698.50]  to the TensorFlow 2.0 release when it arrives.
[698.94 --> 703.12]  Yeah, that's exciting. Is there a timeline for that release? Or I think they just announced that
[703.12 --> 704.52]  they're working on it. Is that right?
[704.80 --> 709.74]  I think so. I pulled up the TensorFlow site, and I don't see a date jumping out at me,
[709.84 --> 711.56]  but I couldn't guarantee it right now.
[711.84 --> 719.74]  Well, kind of along the same front as the practical production ready system integration
[719.74 --> 725.60]  and applied AI stuff that we've been talking about with PyTorch. One thing that another thing
[725.60 --> 731.26]  that I saw, you know, over the past few weeks is this kind of set of articles and resources from
[731.26 --> 738.42]  Google AI that's called Responsible AI Practices. So if you remember, I forget if which episode it
[738.42 --> 742.92]  was in, we can put it in the show links. But we talked about Google's previous release of their
[742.92 --> 747.86]  AI principles, which really had more to do with maybe on the ethics side of things, things that
[747.86 --> 753.62]  they would or wouldn't want to do with AI. Yep, I remember. Yep, how they viewed that. So we'll find
[753.62 --> 758.98]  that that show link and put it in. But these Responsible AI Practices, they really are more at the
[758.98 --> 765.64]  practical level of the AI developer, which I can definitely appreciate. I know we on the show can
[765.64 --> 773.10]  definitely appreciate. And they've had these broken down into a few different sections. So
[773.10 --> 779.22]  general recommended practices, fairness, interpretability, privacy, security. And I just
[779.22 --> 784.64]  find these, you know, really practical, really useful. Some of their general recommended practices,
[784.64 --> 789.12]  and they really break these down into bullet points that you can follow easily. But generally,
[789.12 --> 794.38]  they include things like human centered design, identifying multiple metrics to assess training
[794.38 --> 800.12]  and monitoring, examine your raw data when possible, understand the limitations of your data set in your
[800.12 --> 806.16]  model, test, test, test, which is, of course, hugely important. And then last, continue to monitor and
[806.16 --> 813.64]  update the system after deployment. And they even include some links to ways that they do that in the
[813.64 --> 817.72]  article. And I just think that, you know, what I was thinking about when I was reading through this
[817.72 --> 823.34]  is this would make a great like if I was leading an AI team, or a new project, I would almost take
[823.34 --> 828.76]  these and map them to a checklist of sorts where we could kind of just check off that we've at least
[828.76 --> 834.40]  considered each of these points. And we've either implemented some of their suggestions, or we have
[834.40 --> 839.18]  a good reason that we're not doing that. And I think that would be a really great way to kind of move
[839.18 --> 842.16]  forward responsibly on a on a project. What do you think?
[842.16 --> 848.56]  No, I think that's great. And my last employer, I had to go in and build out the team from scratch.
[848.90 --> 854.58]  And so having there weren't there was not there was a little bit out there. But it's been really in
[854.58 --> 861.16]  the last year that Google and other key players in the AI community have have released these kinds
[861.16 --> 867.56]  of guidelines. And I would very much have liked to have had them available to me in those early days,
[867.56 --> 871.70]  as I was trying to put together my own playbook and figure out how do you build a team? What are the
[871.70 --> 876.70]  different skill sets? How do you divide those up? What types of work can you do? There are just so
[876.70 --> 883.36]  many questions. And, and I guess that that kind of leads me into another one that we had this week,
[883.44 --> 889.52]  was Nvidia had an article, it's in Forbes.com, actually, from an Nvidia person, it's not as
[889.52 --> 895.22]  comprehensive, but it was it was five steps to build a business's deep learning workflow. And in
[895.22 --> 901.82]  that article, they kind of walk you through some highlights that is somewhat similar to to the Google
[901.82 --> 905.86]  guidelines that you just walked us through. And I want to note before we leave that behind that you
[905.86 --> 910.10]  only covered what was under the general category when you were kind of highlighting the sub bullets,
[910.10 --> 915.96]  there's another three or four pages of things that Google had released. And that was having those
[915.96 --> 922.36]  and combining like Nvidia's here, they talk about identify business problems, build a data strategy,
[922.36 --> 928.40]  build and train models, evaluate model accuracy and deploy train models. And each one of those has a
[928.40 --> 934.44]  number of bullets under it. And so I know, as practitioners being able to go and look at all
[934.44 --> 939.80]  of these different guidelines and and how to put it together, posts that these, you know, major
[939.80 --> 944.80]  organizations are releasing out there, and starting to get a sense of what your playbook should look like
[944.80 --> 950.14]  as you're building out an AI capability in your organization. It's a fantastic place to start. And I agree
[950.14 --> 954.72]  with you on that. Yeah. Is there anything like from your perspective, because I know, you know,
[954.72 --> 958.94]  one of the things that I've appreciated about talking to you is you have kind of gone through
[958.94 --> 964.12]  the process of building up a team around AI and that sort of thing. Were there things that,
[964.12 --> 968.92]  you know, were particularly important for you as you did that, that were maybe highlighted in these
[968.92 --> 973.56]  articles or things that maybe you didn't expect as you were going through that process?
[974.06 --> 978.06]  Yeah, there's a lot there, actually. So I'm just gonna touch on the tip. And at some point,
[978.06 --> 982.74]  I know, in the future, we're going to talk about how to put together organizations and hiring
[982.74 --> 987.68]  considerations. And I'll go into more depth, from my perspective, when we get to that. But kind of
[987.68 --> 992.92]  all the things that I just called out on NVIDIA, are kind of high level processes. And the bullets
[992.92 --> 997.24]  are not enough, this, this article alone won't help you get all the way there. But it kind of tells you
[997.24 --> 1002.70]  the categories you should be thinking about. And the Google document that we were just talking about
[1002.70 --> 1007.02]  kind of goes through a lot of the process stuff that you need to be thinking about. Now, in your
[1007.02 --> 1010.68]  organization, you're likely going to have to customize all these around your own size,
[1010.82 --> 1015.62]  your own operations, your own team capabilities. And so everyone's a little bit different in that
[1015.62 --> 1020.38]  way, because you're having to put together your own AI capability, and it's going to be a little
[1020.38 --> 1025.14]  bit unlike everybody else's. But these are good places to start. It just as a teaser for future,
[1025.34 --> 1030.48]  I actually have what I think will be some controversial opinions that I developed when I was doing the
[1030.48 --> 1034.60]  team build out. I'm busy writing a blog post I'm in the middle of right now. And I will,
[1034.60 --> 1041.56]  I will throw those out into the for everyone to, to have a go at in a future episode. So
[1041.56 --> 1044.64]  yeah, I'll just leave that. I'll just leave that hanging there.
[1044.82 --> 1049.66]  I'm definitely looking forward to that and giving, of course, my highly biased opinions as well.
[1050.12 --> 1053.88]  Yeah, I like what you say. I mean, I think what we're trying to do here, and I think what many
[1053.88 --> 1061.18]  people and organizations are trying to do is represent some type of scaffolding, or like I was
[1061.18 --> 1065.34]  kind of saying checklist, but really, it's kind of like a scaffolding where like, you need to be
[1065.34 --> 1070.16]  considering this point that might look different in your organization than other organizations,
[1070.16 --> 1074.54]  but you need to consider this point and not, you know, not ignore it, right?
[1074.72 --> 1079.84]  Yeah, totally agree with that. It's, it's a very creative process is all I can say at this point in
[1079.84 --> 1085.56]  time, you know, we're still in such early days in building out AI capabilities and the maturity of
[1085.56 --> 1090.02]  the community in general. For me, having been around the block more than a few times, it feels
[1090.02 --> 1096.20]  like when the internet was come into being in, you know, about 1993 on that. And if you think how far
[1096.20 --> 1100.30]  software development and software engineering has come in the years since, that is the road ahead
[1100.30 --> 1105.72]  for us in the AI community right now. So seeing these things and discussing how to put them together,
[1105.72 --> 1109.62]  it's the right time. We already know how to do this in other areas of technology, but we're still
[1109.62 --> 1112.98]  learning in data science in general, and specifically, certainly in AI.
[1112.98 --> 1119.26]  Yeah, for sure. All right, Chris, well, I'm going to transfer our discussion to a slightly
[1119.26 --> 1125.64]  different topic and that of transfer learning. I ran across this article, it was published September
[1125.64 --> 1133.00]  17. And it's called Deep Learning Made Easier with Transfer Learning. It came out from Fast Forward
[1133.00 --> 1140.04]  Labs, which is now part of Cloudera, and is associated, you know, with with some bigger names in the in the
[1140.04 --> 1144.52]  space. But I've really appreciated content that they put out in the past. Have you have you read
[1144.52 --> 1146.82]  any of their their blog posts or content in the past?
[1146.82 --> 1152.46]  I have. And, you know, Fast Forward is is has been a great Fast Forward Labs has been a great source of
[1152.46 --> 1157.38]  of information in the past. Obviously, they're now part of the larger organization there at Cloudera.
[1157.50 --> 1162.04]  But I love seeing their stuff. And I love this article, by the way, that you found. I'll have
[1162.04 --> 1165.66]  some comments. I'll let you share a little bit more about what it's about. And then I have some
[1165.66 --> 1166.24]  commentary on it.
[1166.50 --> 1172.02]  Yeah, definitely. And I would encourage people they've actually put out Fast Forward Labs, I mean, has put out
[1172.02 --> 1178.74]  a number of reports or kind of white paper ish sort of things on various topics. I remember reading
[1178.74 --> 1184.56]  their one on machine learning interpret interpretability, which really kind of gave me a
[1184.56 --> 1190.52]  sense of what people are doing on that topic and what considerations there are. And they have a bunch
[1190.52 --> 1195.30]  of other content that's that's really great for learning. So in a sense, these are kind of learning
[1195.30 --> 1200.80]  resources in and of themselves. We'll give you some more later. But this article, I really appreciated
[1200.80 --> 1206.98]  because I think, you know, transfer learning is is so important in terms of how people are
[1206.98 --> 1212.28]  implementing their AI strategy in their in their company. But the article kind of goes through and
[1212.28 --> 1218.44]  it tells you, you know, what what transfer learning is, the sense that you're taking, you're taking a
[1218.44 --> 1223.84]  model that was maybe trained on a certain task and kind of starting from that starting point and
[1223.84 --> 1229.28]  building or generalizing that model to another task, building an additional additional knowledge.
[1229.28 --> 1234.20]  And they kind of walk you through that concept with with a bunch of different compelling figures,
[1234.20 --> 1241.90]  and even some some code and some some PyTorch examples, and robot pictures and cat pictures.
[1241.90 --> 1246.30]  And I just thought the article was really good. So I would definitely highly recommend.
[1246.86 --> 1250.68]  And I will kind of foreshadow another teaser of that same thing I was talking about earlier. And that
[1250.68 --> 1255.96]  is that that this is transfer learning gives you the option of standing on the shoulders of giants. And
[1255.96 --> 1261.18]  so most companies out there that are creating capabilities are going to be on the implementation
[1261.18 --> 1265.82]  side, they're not going to be doing research the way Google brain is and the way the Facebook team
[1265.82 --> 1271.32]  is and stuff. So you know, they'll do enough to get what their use case is. And that's going to be
[1271.32 --> 1277.56]  the majority of production work in industry. And so if that's the case, and if you're able to,
[1277.66 --> 1282.76]  to use your framework of choice, and find some work that somebody has already done on a model,
[1282.76 --> 1289.12]  and you can do that, adjusting your way into your use case, transfer learning is really almost the
[1289.12 --> 1294.42]  default way that that a lot of data scientists and AI engineers are going to be, you know,
[1294.48 --> 1299.08]  accomplishing their own goals. And that's certainly on the teams that I've been on, that has been
[1299.08 --> 1304.42]  the approach that we've used. And, and I think that that is definitely the major use case. And so I
[1304.42 --> 1309.00]  think the more people understand how that process works, the more useful it's going to be. So I think
[1309.00 --> 1313.06]  this is a great article in explaining that. Yeah, there is a kind of a general misconception,
[1313.06 --> 1318.96]  I think that people when they think about AI, they really look to a lot of content that out that's out
[1318.96 --> 1324.98]  there on the web, which is really good content, but maybe it's from like, you know, deep mind or open
[1324.98 --> 1330.98]  AI or something like this. And really, the incentives of those companies around research and the projects
[1330.98 --> 1337.14]  that they work on and the way that they work on them is very different from the incentives in a
[1337.14 --> 1341.70]  typical company, where they're really focused on these deep research questions and new model
[1341.70 --> 1346.84]  architectures and all of that. For the most part, I think, you know, when you're in a company,
[1347.26 --> 1351.74]  you're going to be like you said, you know, standing on the shoulders of giants, you're going to be
[1351.74 --> 1358.02]  taking model definitions and architectures that were developed at somewhere maybe like open AI or
[1358.02 --> 1363.80]  somewhere, and actually applying them to your to your own data. I was actually teaching a workshop a few
[1363.80 --> 1368.88]  weeks ago now. And this question came up. And the question was really around like, what does it
[1368.88 --> 1374.94]  mean to have a custom machine learning model or AI model for your use case in your company? And the
[1374.94 --> 1379.14]  misconception amongst the crowd there was that, well, that always means that you're going to kind
[1379.14 --> 1385.30]  of make up your own sort of model definition and equations and expressions that are really kind of
[1385.30 --> 1391.30]  tailored to your particular use case and, and specifically designed to model your data.
[1391.30 --> 1397.36]  And I think that by and large is, is not how things are done. I think in pretty much every case
[1397.36 --> 1403.36]  of applying AI and machine learning, what you're doing is you're taking, you know, a model definition
[1403.36 --> 1408.84]  that has been developed somewhere like deep mind or open AI, maybe that's a recurrent neural network
[1408.84 --> 1414.22]  or a convolutional neural network or whatever it is, and you're applying it to your particular use
[1414.22 --> 1418.74]  case. But really, when we say you're customizing it for your use case, you're not changing up the
[1418.74 --> 1424.54]  layers of the network, even in many cases, what you're doing is you're just training that model
[1424.54 --> 1429.80]  on your own data to get your own set of, you know, weights and biases, your own set of parameters
[1429.80 --> 1435.26]  that parameterize that model definition that someone else has developed. And I think by and large,
[1435.34 --> 1440.80]  that's, that's what people do. And of course, transfer learning provides even a layer of additional
[1440.80 --> 1445.74]  help on top of that in that you're not even starting from scratch when you do that training,
[1445.74 --> 1450.74]  but you're taking knowledge that was already developed in another tasks and you're kind of
[1450.74 --> 1452.38]  starting from a good checkpoint.
[1453.04 --> 1458.10]  So I agree with everything that you said. And I think that I think between us, we've identified
[1458.10 --> 1462.34]  what I think most people who have been working in the space would agree is kind of the way real
[1462.34 --> 1465.08]  life works on that. So great article. Thanks.
[1465.08 --> 1467.22]  Do we live in real life if we're doing AI?
[1467.22 --> 1473.86]  Good, good question. Although I'm about to transition us into a little bit of a scary
[1473.86 --> 1479.38]  real life here leading in, you know, you and I are always talking about the theme of AI for good.
[1479.58 --> 1484.06]  It's a, it's something that you and I care about very much. And we talk about, you know,
[1484.12 --> 1489.62]  versus the horror stories about what could go wrong. We like to talk about AI being used for purposes
[1489.62 --> 1494.44]  that helps the planet, helps mankind, helps everything about us. And we've had some,
[1494.44 --> 1499.14]  some great episodes with people who were doing just that. But I want to turn to a darker story
[1499.14 --> 1503.78]  for a moment, at least from, from certainly from my perspective, I ran across one. It's on,
[1503.88 --> 1510.48]  it's ABC news, I believe in Australia, I think. And it's on, it's called leave no dark corner.
[1510.48 --> 1517.14]  And it's about the social credit system that is coming into being in China right now. And it is
[1517.14 --> 1523.80]  essentially a system where all 1.4 billion Chinese citizens are going to be monitored
[1523.80 --> 1531.52]  24, 7, 365 all the time through all sorts of different channels. And they are essentially
[1531.52 --> 1537.24]  expected to tow the party line, if you will. The communist party itself calls it the social
[1537.24 --> 1543.46]  credit system. It's supposed to be fully operational by 2020. And a quote from the party,
[1543.56 --> 1549.66]  from the communist party says that it will quote, allow the trustworthy to roam freely under heaven
[1549.66 --> 1555.22]  while making it hard for the discredited to take a single step. And I just, I read that in horror.
[1555.70 --> 1557.20]  It's like something out of a novel.
[1557.38 --> 1563.28]  It is. I mean, it's, it's, it's a 1984 theme again, but, but it's no longer, you know, in past
[1563.28 --> 1568.06]  shows, we've talked about some of the darker stories about, about, oh my God, we don't want to go down
[1568.06 --> 1572.48]  a path like that in the future, but this is happening now. They're talking about it being fully
[1572.48 --> 1579.52]  operational in 2020, but it's already in place partially now. And they interview several people. So if you're,
[1579.66 --> 1584.46]  if you are that Chinese citizen who is completely in sync with the communist party, then you are
[1584.46 --> 1589.76]  good to go because you're going to, you're living a prescribed lifestyle that is approved. And,
[1589.76 --> 1595.30]  but if you are, for instance, an investigative journalist and you discover that maybe high
[1595.30 --> 1598.90]  ranking officials in the communist party are corrupt and there, you know, there's been the
[1598.90 --> 1604.58]  big corruption crackdown recently in the communist party in China, and maybe you upset certain people,
[1604.58 --> 1610.26]  then they give an example of one man in particular who does exactly that. And his social credit is
[1610.26 --> 1614.16]  very low and he can't even travel within the country. He can't get plane tickets. He can't
[1614.16 --> 1619.54]  get train tickets within the country. And rail is very popular in China. And it's just a, when I look
[1619.54 --> 1624.06]  at that as a Westerner and as an American with the biases inherent in that, that is exactly the
[1624.06 --> 1628.78]  opposite of what I hope my life to be in my children's life to be going forward. So I just wanted to draw
[1628.78 --> 1633.16]  that out. And if you're not aware of the social credit system in China, now you are. And if that's not
[1633.16 --> 1637.12]  what you want as a listener, maybe be thinking about what you do want and how to get there.
[1637.12 --> 1643.54]  Yeah. I think this was actually like, literally, I think this was a black mirror episode on Netflix.
[1644.12 --> 1648.66]  I remember like people walking around and doing certain things and then they're like, you know,
[1648.70 --> 1652.94]  they would get a ding and their social credit, you know, went up or down or, or whatever. I forget
[1652.94 --> 1658.02]  what they called it. Maybe some of our listeners can, can remind us in our Slack channel, but yeah.
[1658.18 --> 1662.92]  And one of the things that I think beyond the fact of just the social credit system,
[1662.92 --> 1669.34]  itself, it's like, you know, we've already experienced AI and machine learning being used
[1669.34 --> 1675.74]  like in the social media context in terms of engineering people's political views and all
[1675.74 --> 1680.30]  of that. And really what we've seen is that those systems and especially the ones that are driving
[1680.30 --> 1686.62]  advertising are really pushing people to the extremes of their, of their views. Right. And it seems like
[1686.62 --> 1691.64]  this is, you know, the same thing, but on a, on a greater scale in the sense that the people that are,
[1691.64 --> 1695.74]  that are just, you know, discriminated against or their social credit is pushed down, they're only
[1695.74 --> 1701.26]  going to be more radicalized and the people that are want to get their social credit up,
[1701.32 --> 1706.42]  they're just going to turn more to kind of the norm of what's expected. So yeah, there's definitely,
[1706.42 --> 1713.04]  I think tons of interesting and scary implications. And I think that people should be aware and kind of
[1713.04 --> 1718.16]  watching what's going on, not just in the U S and even in Europe, but in China. And also,
[1718.16 --> 1724.60]  you know, like in India with the Adhar system, of course, there's, there's now like billions of
[1724.60 --> 1730.74]  data points of people's biometric data can be used and in various ways and, you know,
[1730.94 --> 1735.32]  hopefully some good ways, but there's also a lot of, you know, potential dangers of course,
[1735.32 --> 1740.10]  in that. And you're already seeing people bring up things and talk about that in this context.
[1740.10 --> 1745.32]  So we definitely need to be watching and kind of involved in, in the discussion around this,
[1745.32 --> 1749.72]  around the world. So sorry to give everyone nightmares here today, uh, talking on this
[1749.72 --> 1756.26]  topic, just as a, as a final note to balance it in the near future, we're going to have an AI for
[1756.26 --> 1761.44]  good episode. So, uh, that's coming up and hopefully that'll, that'll give you some, uh,
[1761.44 --> 1764.34]  some inspiration instead of, uh, instead of the terror here.
[1764.34 --> 1768.52]  Yeah. And, and there's definitely always going to be a balance. I think it's with any technology.
[1768.72 --> 1773.56]  And we've mentioned this before is technology in and of itself. And this has always been true of
[1773.56 --> 1778.68]  whether it was a, uh, smartphones or, or the internet or whatever, of course can be used in,
[1778.78 --> 1784.32]  in good and bad ways. And really what we want to be doing is promote the positive as much as we can
[1784.32 --> 1789.88]  and promote the responsible practices as much as we can to hopefully, you know, help people to
[1789.88 --> 1798.54]  be asking the right questions. Amen, brother. Yep. So from that, let me recenter my mind. Um, and, uh,
[1798.54 --> 1803.76]  I, I, I did want to bring up a couple of kind of interesting data visualization things that I ran
[1803.76 --> 1809.50]  across and I don't know if, if both are entirely new, but anyway, they were new to me. The first
[1809.50 --> 1817.82]  is this, uh, how to visualize decision trees. This is, uh, an article and a package, uh, for scikit
[1817.82 --> 1824.04]  learn that, that came out from, uh, Terrence Parr and Prince Grover. Sorry if I mispronounce any of
[1824.04 --> 1829.60]  those names at the university of San Francisco's, uh, masters in data science program, basically this
[1829.60 --> 1835.80]  package just kind of, it gives you a really, really nice way of visualizing and interpreting
[1835.80 --> 1842.62]  how your decision tree models were trained and kind of understanding the decisions that they're
[1842.62 --> 1848.20]  making at the various levels of the tree, which if our users aren't familiar, a decision tree model is
[1848.20 --> 1854.12]  it's kind of like a, a bunch of if then statements. So your features are split up into certain ranges
[1854.12 --> 1859.84]  and based on those ranges or their values, then you kind of navigate through these various, uh,
[1859.84 --> 1865.44]  layered if then statements and, and, uh, these visualizations, I just find them really compelling.
[1865.44 --> 1870.72]  And I think that as people are using neural networks and other more complicated models that are,
[1870.72 --> 1876.28]  you know, increasingly less interpretable, although there are many people working on that very, uh,
[1876.28 --> 1882.56]  topic, I think keeping in mind this sort of model and the, even the fact that you can utilize a
[1882.56 --> 1889.10]  package like this to really visually understand how your data is transformed from input to prediction.
[1889.20 --> 1894.56]  I just think that's really cool. I think things like this should be used as much as they can.
[1894.56 --> 1899.82]  And they give a bunch of examples, of course, on like the Iris data and diabetes data, digit data.
[1900.34 --> 1901.66]  Yeah. I just find it really compelling.
[1901.66 --> 1907.00]  You know, and it's funny because being able to use tools like decision trees and the visualizations
[1907.00 --> 1911.62]  around them are really important. We tend to think of them, you know, just within the data science
[1911.62 --> 1915.96]  world, but there's the rest of the world that we have to communicate with and that we have to, uh,
[1915.96 --> 1920.76]  explain things to that we've been asked to explain and show what the possibilities are going forward.
[1920.76 --> 1925.60]  So being able to do this and to visualize them well, and I'm just looking through all the,
[1925.60 --> 1928.42]  the, the great examples they have in this article is really,
[1928.42 --> 1932.38]  really important for people who aren't necessarily in the same field that you're in.
[1932.38 --> 1936.56]  Just wanted to call that out. It's a great set of communications tools that they have here.
[1936.56 --> 1941.46]  Yeah. So the other one that I was going to mention was this anatomy of an AI system,
[1941.46 --> 1947.10]  which I think is kind of attempting to be an infographic that represents all of the interconnected
[1947.10 --> 1955.86]  pieces that are at play in Amazon's Alexa system, or more generally kind of that type of smart speaker
[1955.86 --> 1960.28]  system, all the way from like the materials that are used to make the various devices
[1960.28 --> 1967.48]  to the neural networks that are, that are being used to the AWS infrastructure, to the kind of control
[1967.48 --> 1974.88]  flow and geography. Uh, so I, you know, it's probably not meant to be a fully technical spec of the whole
[1974.88 --> 1980.68]  system, but I think it is meant to be kind of, to give us an idea of the impact of the systems that
[1980.68 --> 1987.48]  we're building both, um, functionality wise and kind of otherwise in terms of people, in terms of,
[1987.48 --> 1991.80]  of places and materials and all of that stuff. Yeah, I totally agree.
[1992.02 --> 1995.88]  Yeah. It's interesting. So take a look at that. I think you can download it as a, as a PDF and,
[1995.88 --> 1997.24]  and take a look through it.
[1997.44 --> 2001.56]  Yeah. It's super detail. I'm just looking through the, uh, looking through it as you're talking and,
[2001.56 --> 2006.26]  uh, zooming in on different aspects. So, uh, definitely interesting to look, to look through.
[2006.26 --> 2010.84]  Uh, after the show, I'll probably, uh, keep doing this where I can just take 15 minutes and explore
[2010.84 --> 2016.66]  it. Yeah, for sure. So I want to turn us, uh, briefly over to spending. You know, we talked
[2016.66 --> 2021.30]  about the, the scary China thing a few minutes ago with social credit. And I want to point out that,
[2021.30 --> 2025.58]  you know, that China has already committed, the government has committed to actively building a
[2025.58 --> 2031.78]  $150 billion AI industry by 2030. Um, and you know, they're, they're really behind it, whether you like
[2031.78 --> 2035.98]  what they're doing or don't like what you're, they're doing. And other major players like Russia
[2035.98 --> 2040.86]  are as well. Vladimir Putin, uh, announced last year that, uh, he was in front of a bunch of
[2040.86 --> 2045.12]  university students and he, he said, artificial intelligence is the future, not only of Russia,
[2045.12 --> 2049.02]  but of all mankind and the industry leader will rule the world. And there's a little bit of a,
[2049.02 --> 2054.80]  an ominous tone to that in my view. No biggie there. Uh, September 1st, 2017 was when he,
[2054.80 --> 2060.70]  he made that speech. And, and I came across an article on CNN business actually, that talks about
[2060.70 --> 2066.14]  that the Pentagon is investing $2 billion into artificial intelligence. That was actually at
[2066.14 --> 2071.60]  the 60th anniversary conference of DARPA. Uh, and DARPA was talking about this $2 billion investment
[2071.60 --> 2076.66]  into them. And I'm sure the Pentagon is spending lots of dollars in other places and stuff, but I
[2076.66 --> 2080.74]  just kind of wanted to say that there are other governments I know outside of the U S and other
[2080.74 --> 2086.00]  Western countries that are, that are very focused on AI. I would like to see a level playing field
[2086.00 --> 2090.32]  throughout the world. I think everybody's going to be doing it. And I would like there to be no one
[2090.32 --> 2094.68]  that just masters it puts their point of view across to everybody. So to Western governments,
[2095.06 --> 2099.00]  you might be thinking about making a little bit more investment on this and make sure that you,
[2099.08 --> 2103.50]  you don't lose the status of being a leader in the field. That was, even though it was a $2 billion
[2103.50 --> 2107.70]  price tag after reading some of the other announcements from other places in the world, I was,
[2107.86 --> 2112.92]  I was kind of let down and I wanted to share that view. Yeah, I definitely agree. And to any of our
[2112.92 --> 2117.96]  listeners that bag some of that 2 billion, then call us up and we'd, we'd love to go to dinner.
[2118.70 --> 2122.78]  Absolutely. Daniel and I are available for your $2 billion budget.
[2123.88 --> 2130.18]  And speaking of, uh, speaking of the community around AI and also the development of AI, of course,
[2130.20 --> 2135.12]  a lot of that is open source. Now I just wanted to highlight that, you know, it's Hacktoberfest.
[2135.30 --> 2139.24]  If you don't know what that is, it's kind of a unofficial, I don't know if we'd call it a holiday,
[2139.24 --> 2145.60]  a season put on by a digital ocean. And so if you're making contributions to open source during
[2145.60 --> 2149.18]  the month of October and you sign up on their website, which we'll have in the show links,
[2149.18 --> 2153.56]  then you can get a, uh, you can get a free t-shirt if you do a certain number of pull requests.
[2153.56 --> 2158.56]  And so we encourage you get involved, find a project, whether that's PyTorch or Onyx or these
[2158.56 --> 2163.26]  visualization libraries or something else that's interesting to you and, and contribute to the
[2163.26 --> 2165.90]  larger community. And that'll be a great way to get involved.
[2165.90 --> 2169.30]  Sure. And are there some other, uh, you have some other conference announcements coming up?
[2169.76 --> 2175.36]  Uh, yeah, good reminders. So I've got, just wanted to remind people that we're kind of getting into,
[2175.36 --> 2180.82]  uh, spring conference season as far as submitting proposals. I wanted to highlight Applied Machine
[2180.82 --> 2185.42]  Learning Days. It's a really great conference in, in Europe if, if you're able to make it there and
[2185.42 --> 2191.72]  they have a call for talks and posters. Also there's O'Reilly AI New York that CFP is open.
[2191.72 --> 2198.54]  And then if you're more on the, uh, research side, especially on the image and video sort of side,
[2198.64 --> 2204.68]  uh, CPVR, their, their call is open. I think it goes into November. So get ready for those things and,
[2204.90 --> 2209.76]  and, uh, definitely get out in the community and, and get involved and meet some people and in real
[2209.76 --> 2214.36]  life. Sounds great. I encourage everyone to get involved. There are two other things I was wanting
[2214.36 --> 2219.84]  to mention. Uh, one, I'm actually going to get a note. I like to do, uh, as do, as do you, I know,
[2219.90 --> 2225.60]  like to do little personal projects and have fun. I have a six year old daughter, uh, Athena, that I'm,
[2225.80 --> 2230.70]  that I'm always kind of, uh, pushing fun technology things for kids in front of her. And I ran across
[2230.70 --> 2236.02]  something that even appealed to my wife who, uh, who stays, uh, out of the AI, AI space. It's not her
[2236.02 --> 2241.32]  interest. She's like, yep, you can have that. But it was a, uh, a little thing where it just showed how
[2241.32 --> 2245.86]  my wife has a bunch of hummingbird feeders on our back deck and we have hummingbirds flitting all
[2245.86 --> 2251.54]  over the place here. And, um, somebody had taken a camera and had put a mount on it, uh, through some
[2251.54 --> 2257.38]  3d printing and was using image classification through a deep learning framework. And I don't
[2257.38 --> 2260.92]  remember which one they used right off the top of my head to capture when the hummingbirds were at
[2260.92 --> 2266.12]  the feeders. And it's just a kind of a silly little weekend project, but it's a lot of fun. It allowed me
[2266.12 --> 2270.50]  to get my family involved. And I do that with my daughter often. I also have a little tello that I'm,
[2270.50 --> 2275.46]  I'm playing around with, with her. And so if you're not doing little personal fun things out
[2275.46 --> 2279.16]  there in the audience, and this isn't all serious stuff, sometimes we can have a little bit fun.
[2279.30 --> 2283.06]  I would encourage you to do that. And then the last thing I had was, I just wanted to mention that,
[2283.06 --> 2288.76]  uh, Google has their dataset search beta out. If you're not aware of it, you can go to, yeah,
[2288.82 --> 2295.76]  no kidding. You can go to toolbox.google.com slash dataset search. And, uh, and it gives you the,
[2295.76 --> 2300.26]  the usual little Google search page, but you can start finding publicly available
[2300.26 --> 2304.66]  datasets out there. And since this was released, I've been using it more and more to try to locate,
[2304.66 --> 2309.80]  uh, datasets to start putting together for my own projects. And I think this is, uh, I think this is
[2309.80 --> 2315.16]  a fantastic tool for us. It's, it's, you know, it's just a search bar, but, uh, it's one that I have
[2315.16 --> 2321.54]  open in a tab all the time these days. So that's it for me, uh, prior to us hopping into some learning
[2321.54 --> 2326.32]  stuff, some learning resources. And keep in mind, you know, when you're searching for data,
[2326.32 --> 2330.88]  it's, it's not always just what your company produces or what, you know, is available to you.
[2330.88 --> 2335.82]  There's a lot of, you know, public data and other data out there, you know, and you can find it with
[2335.82 --> 2341.42]  the tools like this, like Google dataset search. So this is great. So yeah, we'd like to turn now to,
[2341.60 --> 2347.60]  to learning resources again, you know, Chris and I were always trying to learn more and, uh, keep up
[2347.60 --> 2352.20]  with the latest things, but also just remind ourselves of some of the fundamentals of machine
[2352.20 --> 2356.90]  learning and AI. And, uh, so we wanted to share some of those resources with you. The one that I
[2356.90 --> 2362.68]  wanted to share is a set of machine learning cheat sheets. So you might've seen a bunch of different,
[2362.68 --> 2369.54]  uh, cheat sheets out there, but these are from, uh, they're made for Stanford CS 229 class, which is a
[2369.54 --> 2375.94]  machine learning course. And I just found these to be probably like higher quality and better produced
[2375.94 --> 2380.86]  than many of the cheat sheets that I see out there. And they're good, really good reference cards for,
[2380.86 --> 2385.22]  they have one for supervised and unsupervised learning, deep learning tips and tricks,
[2385.40 --> 2390.76]  probability and statistics and, and more. So I think these are a great thing to include and
[2390.76 --> 2396.60]  they're even available in a bunch of languages, um, you know, Spanish and French and Arabic and other
[2396.60 --> 2401.48]  things. So yeah, I think these are, these are really great to kind of bookmark on your browser
[2401.48 --> 2406.68]  and pull up when you need them. This is fantastic. I went from the, the GitHub link that you provided
[2406.68 --> 2411.54]  and they, they list off to another website. And I dived into the deep learning topic on that.
[2411.54 --> 2415.60]  And I'm just looking through this and it's amazing. I am going to be using this all the time.
[2415.60 --> 2421.48]  It covers so much material that you're the kind of things that you're always having to look up or
[2421.48 --> 2428.92]  recall or whatever. So fantastic. Fine, Daniel. Thanks. And my learning resource, I was just at one
[2428.92 --> 2434.06]  of our Atlanta deep learning meetups a few days ago, and we are always having people coming in there
[2434.06 --> 2438.92]  asking for starting off and, and, you know, what to do. And we're always throwing throughout the
[2438.92 --> 2443.78]  usual things. And some of those I've already put out, but my buddy reason, a couple of other guys
[2443.78 --> 2449.44]  were pointing out that one that, that we had not covered was Udacity's machine learning by Georgia
[2449.44 --> 2454.70]  tech, which they have online. It covers supervised, unsupervised and reinforcement learning. It's free.
[2454.84 --> 2459.30]  And they said that for them, I have not been through this course, but they said, uh, part of the
[2459.30 --> 2464.52]  nano degree program and that it had really provided them with a great base upon which to continue
[2464.52 --> 2470.28]  learning. So having had several people say this was definitely a worthy place to start out with,
[2470.30 --> 2472.66]  I wanted to, to, to share that with the audience at large.
[2473.30 --> 2477.64]  Awesome. Yeah. And like we've mentioned, if you have questions about AI, or maybe you have a good
[2477.64 --> 2483.58]  resource that we don't know about, get on our Slack channel, get on our LinkedIn page and let us know
[2483.58 --> 2487.34]  about it. We'd love to hear from you, hear what questions you're having, hear what resources you're
[2487.34 --> 2491.54]  using. And of course we'll try to keep bringing you some good ones, but in the coming weeks,
[2491.54 --> 2496.40]  we're going to have more, uh, guest interviews. We've got some really great stuff lining up as
[2496.40 --> 2501.86]  Chris mentioned about really technical topics and more, uh, use case stuff and ethics and,
[2501.86 --> 2506.56]  and all sorts of things. So keep tuned in and I'll see you again next week, Chris.
[2506.98 --> 2511.76]  I'll see you again, Daniel. It was a great show today and looking forward to next week. So talk to
[2511.76 --> 2512.26]  you later on.
[2512.60 --> 2513.04]  Bye.
[2513.24 --> 2513.48]  Bye.
[2513.48 --> 2520.30]  All right. Thank you for tuning into this episode of practical AI. If you enjoyed this
[2520.30 --> 2524.82]  show, do us a favor, go on iTunes, give us a rating, go in your podcast app and favorite it.
[2524.92 --> 2528.38]  If you are on Twitter or a social network, share a link with a friend, whatever you got to do,
[2528.60 --> 2532.46]  share the show with a friend. If you enjoyed it and bandwidth for change log is provided by
[2532.46 --> 2537.16]  fastly learn more at fastly.com and we catch our errors before our users do here at change log
[2537.16 --> 2542.72]  because of roll bar, check them out at robot.com slash change log. And we're hosted on Linode cloud
[2542.72 --> 2548.76]  servers at leno.com slash change log. Check them out. Support this show. This episode is hosted by
[2548.76 --> 2554.16]  Daniel Whitenack and Chris Benson. Editing is done by Tim Smith. The music is by Breakmaster
[2554.16 --> 2559.84]  cylinder and you can find more shows just like this at change log.com. When you go there, pop in your
[2559.84 --> 2564.72]  email address, get our weekly email, keeping you up to date with the news and podcasts for developers
[2564.72 --> 2569.02]  in your inbox every single week. Thanks for tuning in. We'll see you next week.
[2575.66 --> 2581.16]  I'm Nick Neesey. This is KBall. And I'm Rachel White. We're panelists on JS Party, a community
[2581.16 --> 2586.12]  celebration of JavaScript and the web. Every Thursday at noon central, a few of us get together and chat
[2586.12 --> 2590.86]  about JavaScript, Node, and topics ranging from practical accessibility to weird web APIs.
[2590.86 --> 2595.82]  I like your rhymes with mafia idea. Like that's a, that's a good way to get it across. I'm trying
[2595.82 --> 2604.40]  to think what I can do. KBall rhymes with ball. Join us live on Thursdays at noon central. Listen
[2604.40 --> 2608.88]  and Slack with us in real time or wait for the recording to hit. New episodes come out each Friday.
[2608.88 --> 2614.82]  Find the show at changelog.com slash JS Party or wherever you listen to podcasts.
[2620.86 --> 2625.82]  I'm Tim Smith and my show away from keyboard explores the human side of creative work.
[2626.06 --> 2631.36]  You'll hear stories sometimes deeply personal about the triumphs and struggles of doing what
[2631.36 --> 2636.72]  you love. I ended up in hospital with burnout. I just kept ignoring the way that it was making
[2636.72 --> 2641.62]  me feel and just kept powering through it. And then eventually my body started to give me physical
[2641.62 --> 2647.06]  symptoms to say like, Hey, you should stop and listen to me. New episodes premiere every other
[2647.06 --> 2652.12]  Wednesday. Find the show at changelog.com slash AFK or wherever you listen to podcasts.
