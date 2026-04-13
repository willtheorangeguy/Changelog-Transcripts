[0.14 --> 2.46]  Today's models are actually not models.
[2.62 --> 3.32]  Like we need a new name
[3.32 --> 4.84]  because there's something that doesn't exist.
[4.96 --> 7.36]  Like what do you call an encoder and a decoder
[7.36 --> 9.10]  working together to make an auto encoder
[9.10 --> 10.42]  or variational encoder, right?
[10.44 --> 11.02]  They're not models.
[11.16 --> 13.02]  It's collections of models interacting together.
[13.16 --> 14.18]  Same for transformers, right?
[14.36 --> 16.28]  So that's really what the lighting module is about.
[16.40 --> 17.84]  You pass in these models into it
[17.84 --> 19.62]  and then how they interact together
[19.62 --> 21.10]  is abstracted by that, right?
[21.34 --> 22.74]  And I think that's a missing abstraction
[22.74 --> 23.72]  that was not there.
[23.92 --> 25.44]  So it's important to decouple that
[25.44 --> 27.72]  because now I have this single file
[27.72 --> 29.30]  that's completely self-contained
[29.30 --> 31.34]  that I can now share with my team across
[31.34 --> 32.24]  in a different division.
[32.72 --> 34.76]  And their problem might be completely different
[34.76 --> 35.82]  with a different data set.
[35.92 --> 37.92]  And they don't have to ever change the code on that model.
[38.06 --> 40.22]  All they have to do is change what hardware they're using
[40.22 --> 41.30]  and then what the data set is.
[41.46 --> 44.20]  So it makes code extremely interoperable, right?
[44.24 --> 45.98]  So I think people come to Lightning
[45.98 --> 48.94]  because they want to train on multiple GPUs and so on,
[49.00 --> 50.66]  but that's only like a very small part of it.
[50.70 --> 51.78]  I think once you get into it,
[51.82 --> 53.22]  you see that the rest of it
[53.22 --> 55.04]  is the ability to collaborate with peers
[55.04 --> 57.82]  and be able to have reproducible and scalable code.
[59.30 --> 61.98]  Big thanks to our partners,
[62.08 --> 63.42]  Linode, Fastly, and LaunchDarkly.
[63.64 --> 64.36]  We love Linode.
[64.44 --> 65.86]  They keep it fast and simple.
[65.98 --> 68.34]  Check them out at linode.com slash changelog.
[68.46 --> 70.64]  Our bandwidth is provided by Fastly.
[70.98 --> 72.30]  Learn more at Fastly.com
[72.30 --> 74.54]  and get your feature flags powered by LaunchDarkly.
[74.80 --> 76.52]  Get a demo at LaunchDarkly.com.
[79.52 --> 80.94]  This episode is brought to you
[80.94 --> 81.98]  by our friends at O'Reilly.
[82.22 --> 83.14]  Many of you know O'Reilly
[83.14 --> 84.98]  for their animal tech books and their conferences,
[85.34 --> 86.44]  but you may not know
[86.44 --> 88.50]  they have an online learning platform as well.
[88.50 --> 90.50]  The platform has all their books,
[90.80 --> 91.50]  all their videos,
[91.78 --> 93.30]  and all their conference talks.
[93.64 --> 94.88]  Plus, you can learn by doing
[94.88 --> 96.68]  with live online training courses
[96.68 --> 97.86]  and virtual conferences,
[98.36 --> 99.76]  certification practice exams,
[100.10 --> 102.50]  and interactive sandboxes and scenarios
[102.50 --> 103.38]  to practice coding
[103.38 --> 104.44]  alongside what you're learning.
[104.68 --> 106.60]  They cover a ton of technology topics,
[106.72 --> 107.48]  machine learning,
[107.80 --> 108.18]  AI,
[108.68 --> 109.46]  programming languages,
[109.98 --> 110.28]  DevOps,
[110.78 --> 111.58]  data science,
[111.86 --> 112.26]  cloud,
[112.60 --> 113.08]  containers,
[113.68 --> 114.12]  security,
[114.60 --> 115.96]  and even soft skills
[115.96 --> 116.94]  like business management
[116.94 --> 118.38]  and presentation skills.
[118.50 --> 119.02]  You name it,
[119.16 --> 120.28]  it is all in there.
[120.62 --> 121.74]  If you need to keep your team
[121.74 --> 122.98]  or yourself up to speed
[122.98 --> 123.86]  on their tech skills,
[123.94 --> 124.74]  then check out O'Reilly's
[124.74 --> 125.76]  online learning platform.
[126.30 --> 127.96]  Learn more and keep your team skills sharp
[127.96 --> 128.90]  at O'Reilly.com
[128.90 --> 129.86]  slash changelog.
[130.00 --> 130.44]  Again,
[130.60 --> 131.40]  O'Reilly.com
[131.40 --> 132.26]  slash changelog.
[132.26 --> 142.64]  Welcome to Practical AI,
[143.00 --> 143.92]  a weekly podcast
[143.92 --> 145.50]  that makes artificial intelligence
[145.50 --> 146.08]  practical,
[146.40 --> 146.82]  productive,
[147.22 --> 148.14]  and accessible to everyone.
[148.48 --> 149.82]  This is where conversations
[149.82 --> 150.60]  around AI,
[150.84 --> 151.40]  machine learning,
[151.48 --> 152.56]  and data science happen.
[152.82 --> 153.68]  Join the community
[153.68 --> 154.60]  and Slack with us
[154.60 --> 155.58]  around various topics
[155.58 --> 156.10]  of the show
[156.10 --> 157.04]  at changelog.com
[157.04 --> 157.60]  slash community
[157.60 --> 158.92]  and follow us on Twitter.
[159.04 --> 160.64]  We're at Practical AI FM.
[160.64 --> 168.74]  Welcome to another episode
[168.74 --> 169.88]  of Practical AI.
[170.24 --> 171.92]  This is Daniel Whitenack.
[172.04 --> 173.26]  I am a data scientist
[173.26 --> 175.12]  with SIL International,
[175.46 --> 176.62]  and I'm joined as always
[176.62 --> 177.54]  by my co-host,
[177.70 --> 178.24]  Chris Benson,
[178.46 --> 180.20]  who is a tech strategist
[180.20 --> 181.34]  at Lockheed Martin.
[181.86 --> 182.56]  And this week,
[182.60 --> 184.86]  we have a really exciting show.
[185.02 --> 186.38]  I'm pumped to talk about this.
[186.50 --> 188.74]  We have William Falcon with us,
[188.74 --> 191.06]  who is creator of PyTorch Lightning
[191.06 --> 192.90]  and CEO of Grid AI.
[193.14 --> 193.66]  Welcome, William.
[194.12 --> 194.80]  Well, thank you guys
[194.80 --> 195.38]  for having me.
[195.44 --> 196.76]  Really excited to chat with you.
[197.22 --> 197.84]  Yeah, yeah,
[197.88 --> 198.68]  we are as well.
[198.82 --> 199.78]  And I think I might have
[199.78 --> 201.12]  even mentioned this to Chris
[201.12 --> 202.08]  on our Slack channel,
[202.22 --> 203.08]  but I saw you
[203.08 --> 204.52]  like on Twitter
[204.52 --> 206.10]  when Grid AI was launched,
[206.20 --> 207.72]  there was like a screencast
[207.72 --> 208.56]  of like,
[209.06 --> 210.16]  this is some things
[210.16 --> 210.88]  that you can do
[210.88 --> 211.62]  with Grid AI.
[211.82 --> 213.06]  And it was one of those moments,
[213.06 --> 213.50]  I don't know
[213.50 --> 214.26]  if you've ever seen
[214.26 --> 215.96]  like a Kelsey Hightower demo
[215.96 --> 217.64]  in like the Kubernetes world
[217.64 --> 218.52]  or something like that.
[218.86 --> 219.68]  But it was one of those moments
[219.68 --> 220.28]  where I was like,
[220.76 --> 222.16]  things just sort of snowballed
[222.16 --> 222.88]  and then all of a sudden
[222.88 --> 224.04]  you were running like,
[224.18 --> 225.02]  you were running models
[225.02 --> 226.28]  on all of these GPUs
[226.28 --> 226.82]  in the cloud
[226.82 --> 227.94]  with very little effort.
[227.94 --> 229.32]  And it was pretty cool.
[229.40 --> 230.42]  So I'm excited to dive
[230.42 --> 231.44]  into that at some point.
[231.64 --> 232.58]  Yeah, I'll start to share it.
[233.52 --> 234.34]  Yeah, cool.
[234.54 --> 236.34]  So maybe before we get to there,
[236.46 --> 237.32]  let's maybe start
[237.32 --> 238.48]  at PyTorch Lightning.
[239.04 --> 240.26]  People might have heard
[240.26 --> 241.12]  of PyTorch.
[241.24 --> 241.98]  They might have heard
[241.98 --> 242.56]  of Lightning.
[243.08 --> 244.96]  I know Lightning kind of shows up
[244.96 --> 245.88]  in my Twitter feed
[245.88 --> 246.52]  quite a bit.
[246.96 --> 248.02]  Could you just give us
[248.02 --> 249.16]  a little bit of context
[249.16 --> 251.34]  for what PyTorch Lightning is
[251.34 --> 253.52]  and how people can use it,
[253.58 --> 254.12]  where it might fit
[254.12 --> 255.02]  into people's workflow?
[256.04 --> 256.72]  Yeah, so I think,
[256.86 --> 257.02]  you know,
[257.06 --> 257.62]  I'll talk a little
[257.62 --> 258.46]  of my experience
[258.46 --> 259.66]  to understand the motivation
[259.66 --> 260.34]  behind it, right?
[260.38 --> 261.02]  Because I think
[261.02 --> 262.68]  my sense from speaking
[262.68 --> 263.46]  to people in the community
[263.46 --> 264.46]  is that we've all
[264.46 --> 265.84]  had very similar problems
[265.84 --> 266.70]  and thought about
[266.70 --> 268.22]  very similar approaches, right?
[268.68 --> 269.44]  The difference is,
[269.50 --> 269.64]  you know,
[269.64 --> 270.58]  we open source this
[270.58 --> 271.52]  and a lot of people
[271.52 --> 272.50]  started contributing to it.
[272.50 --> 274.48]  So I started out,
[274.62 --> 274.78]  you know,
[274.80 --> 275.60]  as a software engineer
[275.60 --> 276.80]  and I was working in finance
[276.80 --> 278.42]  and before that,
[278.46 --> 278.72]  I guess,
[278.78 --> 279.36]  I was an undergrad
[279.36 --> 280.26]  and I was starting,
[280.52 --> 280.72]  you know,
[280.72 --> 281.46]  to do research
[281.46 --> 283.44]  and I'd been working
[283.44 --> 284.52]  as a software engineer
[284.52 --> 286.22]  and when I got
[286.22 --> 287.12]  into AI research,
[287.12 --> 288.16]  it was in neuroscience,
[288.44 --> 288.54]  right?
[288.58 --> 289.50]  So computational neuroscience
[289.50 --> 290.52]  and we were trying
[290.52 --> 292.60]  to take a neural activity
[292.60 --> 293.40]  from the brain
[293.40 --> 295.00]  and trying to reconstruct
[295.00 --> 296.08]  what generated that,
[296.16 --> 296.32]  right?
[296.36 --> 297.48]  And that was in the context
[297.48 --> 298.32]  of, you know,
[298.60 --> 299.42]  eyesight basically.
[300.12 --> 301.76]  And so what happened there
[301.76 --> 302.64]  is none of us
[302.64 --> 303.48]  were like really,
[303.96 --> 304.78]  really big engineers
[304.78 --> 305.36]  in deep learning.
[305.46 --> 306.36]  Like we weren't experts,
[306.46 --> 306.66]  right?
[306.68 --> 307.92]  And so I started
[307.92 --> 308.52]  training models
[308.52 --> 309.12]  and, you know,
[309.16 --> 310.08]  back then I was using
[310.08 --> 311.00]  Teano, right?
[311.00 --> 312.00]  Which is like a very
[312.00 --> 312.84]  old framework
[312.84 --> 314.34]  and I remember
[314.34 --> 314.82]  the first time
[314.82 --> 315.24]  we got something
[315.24 --> 315.98]  running on a GPU
[315.98 --> 316.96]  and it was like magical
[316.96 --> 318.20]  because suddenly my time
[318.20 --> 319.04]  went from months
[319.04 --> 320.34]  to like a few days
[320.34 --> 320.76]  and I was like,
[320.84 --> 321.00]  great.
[321.78 --> 323.96]  And the research continued
[323.96 --> 325.40]  and what I found myself
[325.40 --> 326.26]  doing over and over
[326.26 --> 327.14]  back then was
[327.14 --> 328.74]  I'd have an idea
[328.74 --> 329.72]  about something
[329.72 --> 330.70]  that wasn't quite that,
[330.78 --> 330.90]  right?
[330.96 --> 331.90]  So in neural decoding
[331.90 --> 332.94]  it's basically like
[332.94 --> 334.76]  translating a sequence
[334.76 --> 336.02]  of signals
[336.02 --> 337.30]  into something,
[337.36 --> 337.90]  an image
[337.90 --> 339.12]  or another signal,
[339.20 --> 339.34]  right?
[339.36 --> 340.00]  So it's a translation
[340.00 --> 340.82]  problem in essence.
[341.46 --> 342.58]  And so you could do
[342.58 --> 343.66]  things like GANs,
[343.76 --> 344.56]  autoencoders,
[344.68 --> 345.18]  you could do things
[345.18 --> 345.70]  like regression,
[345.82 --> 346.44]  so many ideas.
[346.88 --> 347.86]  And I would want to try
[347.86 --> 348.74]  a few different approaches
[348.74 --> 349.62]  with my teammates
[349.62 --> 351.30]  and we would have to
[351.30 --> 351.82]  copy the code
[351.82 --> 352.48]  over and over again,
[352.56 --> 352.72]  right?
[352.78 --> 353.36]  You would either
[353.36 --> 354.20]  fork the project
[354.20 --> 355.40]  and then kind of like
[355.40 --> 356.44]  copy that code over
[356.44 --> 357.94]  and then if something
[357.94 --> 358.58]  new came out,
[358.66 --> 359.70]  like multi-GPU training,
[359.80 --> 360.52]  you have to then write
[360.52 --> 361.26]  it into all the code
[361.26 --> 361.72]  that you did.
[361.82 --> 362.40]  And so suddenly
[362.40 --> 362.96]  you're maintaining
[362.96 --> 364.06]  like 10 different files
[364.06 --> 364.60]  that are all doing
[364.60 --> 365.14]  the same thing.
[365.72 --> 366.88]  And I started abstracting
[366.88 --> 367.46]  that into like
[367.46 --> 368.34]  a kind of joint class
[368.34 --> 368.96]  and I think we all
[368.96 --> 369.30]  honestly,
[369.60 --> 370.28]  I think all of us
[370.28 --> 370.88]  kind of do this
[370.88 --> 371.40]  at some point.
[372.80 --> 373.88]  And I think at that
[373.88 --> 374.88]  point I had been using
[374.88 --> 375.90]  SQLearn for a while
[375.90 --> 376.76]  so I loved like their
[376.76 --> 377.92]  fit and all those
[377.92 --> 378.62]  methods and so I was
[378.62 --> 378.94]  like, okay,
[379.00 --> 379.34]  well, whatever,
[379.44 --> 379.92]  let's just call it
[379.92 --> 380.72]  fit and do that.
[381.18 --> 381.94]  And then I transitioned
[381.94 --> 382.52]  to TensorFlow
[382.52 --> 383.94]  because we needed to
[383.94 --> 385.14]  get into multiple GPUs
[385.14 --> 385.98]  and it was really
[385.98 --> 386.64]  hard to do in Theano.
[387.14 --> 388.16]  So that took our
[388.16 --> 388.70]  training time
[388.70 --> 389.52]  dramatically down.
[390.30 --> 390.70]  And then, you know,
[390.72 --> 391.28]  continue working
[391.28 --> 392.08]  on it for a while
[392.08 --> 393.74]  but the problem is like
[393.74 --> 394.80]  it just continued.
[394.98 --> 395.64]  Every time I wanted
[395.64 --> 396.32]  to do something new,
[396.36 --> 396.98]  you had to copy
[396.98 --> 397.58]  that code over
[397.58 --> 398.30]  and then new things
[398.30 --> 399.30]  came out all the time.
[399.42 --> 400.06]  Like there was just
[400.06 --> 400.64]  a different way
[400.64 --> 401.04]  of training
[401.04 --> 402.58]  and it was really
[402.58 --> 403.44]  hard to go back
[403.44 --> 404.72]  and copy and paste
[404.72 --> 405.26]  all that stuff.
[405.78 --> 406.34]  I kind of,
[406.44 --> 407.14]  I left that project
[407.14 --> 407.72]  for a bit
[407.72 --> 408.56]  and then kind of
[408.56 --> 409.20]  went into the startup
[409.20 --> 409.66]  world, right?
[409.70 --> 410.52]  And I spent a few years
[410.52 --> 411.86]  putting NLP models
[411.86 --> 412.52]  into production
[412.52 --> 414.24]  and there it was
[414.24 --> 414.98]  less about focus
[414.98 --> 415.42]  on training
[415.42 --> 415.84]  and more about
[415.84 --> 416.50]  deploying models
[416.50 --> 418.14]  and so I was just like
[418.14 --> 419.30]  cool, quick baseline
[419.30 --> 419.92]  and then just like
[419.92 --> 420.72]  put that thing in there
[420.72 --> 421.54]  and see what happens, right?
[421.90 --> 422.92]  I was less concerned
[422.92 --> 424.38]  about solving
[424.38 --> 425.54]  like a very unique problem
[425.54 --> 426.38]  and more about,
[426.60 --> 427.60]  hey, I have the data here.
[427.74 --> 428.30]  I just want,
[428.44 --> 429.44]  I don't care what the model is.
[429.48 --> 430.08]  I just want to see
[430.08 --> 430.94]  some results, right?
[431.46 --> 432.36]  So we got that working
[432.36 --> 433.16]  and ended up,
[433.18 --> 433.38]  you know,
[433.42 --> 434.70]  scaling that to a company
[434.70 --> 435.38]  that got acquired
[435.38 --> 437.18]  and that was basically
[437.18 --> 438.52]  using NLP to help,
[438.72 --> 438.96]  you know,
[438.98 --> 439.48]  low-income,
[439.66 --> 440.42]  first-generation students
[440.42 --> 440.92]  figure out how to pay
[440.92 --> 442.14]  for college over text message,
[442.62 --> 443.40]  which was really cool
[443.40 --> 444.92]  and from there
[444.92 --> 446.00]  I started my PhD
[446.00 --> 447.76]  and kind of like
[447.76 --> 449.92]  started that research flow again
[449.92 --> 450.54]  and then,
[451.08 --> 451.30]  you know,
[451.36 --> 452.30]  coming from the startup world
[452.30 --> 452.70]  I was like,
[452.76 --> 453.54]  how do I bring
[453.54 --> 455.10]  that speed and agility
[455.10 --> 456.42]  to research, right?
[456.50 --> 458.36]  Because we all know this
[458.36 --> 459.24]  and I think Garbathy
[459.24 --> 460.06]  talks about this.
[460.20 --> 460.46]  I mean,
[460.54 --> 461.32]  we all know this firsthand
[461.32 --> 462.74]  but like the outcome
[462.74 --> 464.36]  of doing anything
[464.36 --> 465.18]  with AI nowadays
[465.18 --> 466.26]  is honestly a function
[466.26 --> 467.22]  of how fast
[467.22 --> 468.42]  you iterate through ideas, right?
[468.44 --> 469.40]  Because like 90%
[469.40 --> 469.78]  of your ideas
[469.78 --> 470.36]  are going to fail
[470.36 --> 471.40]  and then one or two
[471.40 --> 471.86]  are going to work
[471.86 --> 472.52]  and then you're good to go.
[472.64 --> 473.58]  So literally
[473.58 --> 474.38]  just how fast
[474.38 --> 474.88]  can you power
[474.88 --> 475.58]  through those ideas
[475.58 --> 476.46]  is probably
[476.46 --> 477.82]  the single biggest predictor
[477.82 --> 478.48]  of if that thing's
[478.48 --> 479.26]  going to work or not.
[479.68 --> 480.56]  So I knew that
[480.56 --> 481.30]  and I wanted to bring
[481.30 --> 482.22]  that ability
[482.22 --> 483.16]  to my, you know,
[483.32 --> 484.08]  PhD research.
[484.08 --> 484.46]  I was like,
[484.50 --> 484.58]  hey,
[484.60 --> 485.50]  maybe I can finish this thing
[485.50 --> 486.36]  in like three years, right?
[486.40 --> 487.08]  As opposed to six
[487.08 --> 487.48]  or whatever.
[488.86 --> 489.22]  Ambitious.
[489.36 --> 489.62]  Yeah.
[490.42 --> 491.32]  Looking back now,
[491.34 --> 492.10]  it's not a good idea
[492.10 --> 492.56]  but yeah,
[492.62 --> 493.64]  that was the goal, right?
[494.00 --> 495.00]  And so...
[495.00 --> 495.80]  I know the feeling.
[495.92 --> 496.12]  Yeah.
[496.28 --> 497.50]  And so I took my code
[497.50 --> 498.56]  from my undergrad days
[498.56 --> 499.02]  and, you know,
[499.02 --> 499.96]  kind of brushed it off
[499.96 --> 500.80]  and then at that point
[500.80 --> 501.54]  I had already switched
[501.54 --> 502.18]  to PyTorch
[502.18 --> 502.60]  so I was like,
[502.68 --> 502.78]  okay,
[502.84 --> 502.94]  well,
[502.98 --> 503.58]  let me just rewrite
[503.58 --> 504.44]  this thing in PyTorch
[504.44 --> 505.16]  and see how it goes.
[505.72 --> 506.94]  So I started working with,
[506.98 --> 507.18]  again,
[507.24 --> 508.16]  NLP at that point
[508.16 --> 509.04]  and then we moved
[509.04 --> 510.22]  into like audio research,
[510.30 --> 510.46]  right?
[510.46 --> 511.62]  To do speech synthesis
[511.62 --> 512.22]  and so on.
[512.60 --> 513.54]  And all of that
[513.54 --> 514.68]  using the same code, right?
[514.78 --> 516.18]  So it was interesting
[516.18 --> 516.70]  because like
[516.70 --> 518.20]  the first code was for NLP
[518.20 --> 519.64]  and then I modified it
[519.64 --> 520.48]  to work for audio
[520.48 --> 521.18]  and then vision
[521.18 --> 521.74]  and so on.
[522.12 --> 522.78]  And then eventually,
[523.10 --> 523.82]  I don't think
[523.82 --> 524.62]  it was quite there
[524.62 --> 525.70]  at that abstraction level yet
[525.70 --> 526.54]  because I was still having
[526.54 --> 527.56]  to do a lot of bespoke code
[527.56 --> 528.78]  but then I don't know
[528.78 --> 529.14]  what happened.
[529.32 --> 529.40]  Like,
[529.58 --> 530.80]  I guess over the winter
[530.80 --> 531.70]  something clicked
[531.70 --> 532.18]  and then,
[532.52 --> 532.70]  you know,
[532.70 --> 533.92]  the trainer got factored out
[533.92 --> 535.46]  and then it just became obvious
[535.46 --> 536.14]  that at that point
[536.14 --> 537.20]  you need to separate the model
[537.20 --> 537.72]  from the hardware.
[538.30 --> 539.62]  And so that's what Lightning became.
[539.98 --> 540.78]  Then I open sourced
[540.78 --> 541.80]  and then I joined Facebook
[541.80 --> 543.04]  and I researched that summer
[543.04 --> 544.38]  as an intern at FAIR
[544.38 --> 545.48]  and, you know,
[545.50 --> 546.78]  continuing my PhD research
[546.78 --> 547.64]  and there you have
[547.64 --> 548.56]  a giant cluster, right?
[548.58 --> 549.12]  And I was like,
[549.16 --> 549.62]  okay, well,
[550.16 --> 550.36]  you know,
[550.40 --> 551.64]  if I have Facebook resources,
[552.10 --> 552.72]  what can I do?
[552.72 --> 554.98]  And, you know,
[555.02 --> 555.60]  very ambitious
[555.60 --> 556.56]  in terms of like
[556.56 --> 557.80]  trying to do research ideas.
[557.96 --> 559.00]  So we were trying
[559.00 --> 559.68]  to scale up
[559.68 --> 560.92]  like massive data sets
[560.92 --> 561.54]  on the cluster
[561.54 --> 562.58]  as much as we could, right?
[562.60 --> 564.36]  So I was consistently training,
[564.66 --> 564.96]  you know,
[565.04 --> 566.30]  500 GPU models,
[566.40 --> 566.90]  that kind of stuff
[566.90 --> 567.72]  all the time
[567.72 --> 568.52]  at FAIR
[568.52 --> 569.62]  with this framework
[569.62 --> 570.24]  and then,
[570.30 --> 570.44]  you know,
[570.48 --> 571.00]  people noticed
[571.00 --> 572.12]  because the cluster,
[572.64 --> 573.38]  there was like a handful
[573.38 --> 574.50]  of teams across Facebook
[574.50 --> 575.56]  that was using the cluster
[575.56 --> 576.36]  that efficiently
[576.36 --> 577.98]  but the rest of the teams
[577.98 --> 578.32]  weren't
[578.32 --> 578.92]  because like
[578.92 --> 579.60]  it takes a lot
[579.60 --> 580.30]  to do, you know,
[580.40 --> 581.16]  training at scale.
[581.74 --> 582.48]  And so, you know,
[582.48 --> 583.08]  I started working
[583.08 --> 583.60]  with those people
[583.60 --> 584.72]  because they're experts
[584.72 --> 585.28]  at this, right?
[585.32 --> 585.94]  And so we embedded
[585.94 --> 586.80]  a lot of those practices
[586.80 --> 587.36]  into Lightning
[587.36 --> 588.74]  and then ended up
[588.74 --> 589.62]  with a framework now
[589.62 --> 590.70]  that can do
[590.70 --> 591.68]  really scalable training.
[592.02 --> 592.96]  And then at that point,
[593.02 --> 593.24]  you know,
[593.28 --> 593.98]  there was some adoption
[593.98 --> 594.48]  internally,
[594.66 --> 595.76]  then adoption externally
[595.76 --> 596.72]  and then it just kind of
[596.72 --> 597.44]  took off after that.
[597.56 --> 598.20]  But, you know,
[598.22 --> 599.18]  I came at it from
[599.18 --> 600.36]  how do I move
[600.36 --> 601.76]  really fast through research
[601.76 --> 602.50]  knowing what I know
[602.50 --> 603.14]  about putting models
[603.14 --> 604.26]  into production as well
[604.26 --> 605.02]  and knowing what I know
[605.02 --> 605.80]  about doing research
[605.80 --> 606.48]  as well, right?
[606.84 --> 608.02]  So it was just kind of like
[608.02 --> 609.40]  having both requirements
[609.40 --> 610.58]  made it really interesting.
[610.90 --> 612.26]  And what's really cool now
[612.26 --> 613.14]  is that it's evolved
[613.14 --> 614.52]  into, you know,
[614.54 --> 615.72]  my vision really was
[615.72 --> 616.60]  you and I,
[616.82 --> 617.38]  all three of us
[617.38 --> 618.00]  are going to code
[618.00 --> 618.88]  the exact same thing
[618.88 --> 619.90]  in our own projects, right?
[619.92 --> 620.48]  We're going to code
[620.48 --> 621.14]  half precision.
[621.30 --> 621.88]  We're going to code
[621.88 --> 623.22]  stochastic weight averaging.
[623.40 --> 623.92]  We're going to code
[623.92 --> 624.98]  whatever new thing comes up.
[625.24 --> 626.42]  But why waste that effort?
[626.54 --> 627.58]  Like, that's not the job.
[627.66 --> 628.54]  The job is to like,
[628.92 --> 629.16]  you know,
[629.20 --> 630.04]  if you're Lockheed Martin,
[630.16 --> 630.46]  I don't know,
[630.56 --> 631.62]  predict metal,
[631.80 --> 632.30]  whatever, right?
[632.30 --> 633.64]  Like find, you know,
[633.72 --> 634.76]  deficiency in materials.
[634.86 --> 635.10]  I don't know
[635.10 --> 635.94]  what you guys do there, right?
[636.00 --> 637.32]  But that'll work.
[637.42 --> 637.82]  That'll work.
[637.82 --> 639.06]  I think that's exactly
[639.06 --> 639.84]  what Chris does.
[640.10 --> 640.60]  I assume.
[641.56 --> 642.84]  So that's the goal.
[642.96 --> 643.62]  The goal is not
[643.62 --> 644.62]  to figure out how to implement,
[644.70 --> 644.90]  you know,
[644.96 --> 645.88]  stochastic weight averaging,
[645.98 --> 646.18]  right?
[646.54 --> 648.00]  So what's cool now
[648.00 --> 648.40]  is that,
[648.58 --> 648.78]  I mean,
[648.78 --> 649.68]  I think we're approaching
[649.68 --> 650.48]  500 contributors,
[650.48 --> 651.44]  but these are all like
[651.44 --> 652.40]  top researchers
[652.40 --> 653.60]  and PhDs
[653.60 --> 654.36]  all over the world
[654.36 --> 655.56]  who implement these things
[655.56 --> 656.54]  and put them into papers.
[657.22 --> 657.72]  And then, you know,
[657.74 --> 658.38]  within a few hours,
[658.44 --> 659.16]  it's ready and available
[659.16 --> 659.64]  for everyone.
[659.82 --> 661.32]  So do you have to know
[661.32 --> 662.82]  how half precision works
[662.82 --> 663.88]  with, you know,
[663.96 --> 664.38]  I don't know,
[664.44 --> 665.16]  on GPUs?
[665.16 --> 665.84]  You don't, right?
[665.84 --> 666.40]  But you just know
[666.40 --> 667.42]  that it's going to save you memory.
[667.72 --> 669.30]  And so it's been basically
[669.30 --> 670.64]  turned into a community project.
[670.98 --> 672.48]  And my vision was really like,
[672.52 --> 673.22]  can we build like
[673.22 --> 674.58]  the world's research lab,
[674.64 --> 675.22]  basically, right?
[675.22 --> 676.44]  Can we have all access
[676.44 --> 677.66]  to top researchers
[677.66 --> 678.56]  and resources?
[679.10 --> 680.60]  And that's what's happened so far.
[681.42 --> 682.02]  So I noticed
[682.02 --> 682.94]  as you're kind of
[682.94 --> 684.18]  going through the story,
[684.32 --> 685.44]  it seems like
[685.44 --> 686.46]  as you progressed
[686.46 --> 687.36]  over those years
[687.36 --> 688.68]  through the different aspects
[688.68 --> 689.62]  of your own life,
[689.74 --> 690.92]  and you're kind of
[690.92 --> 692.28]  looking at the same problem
[692.28 --> 693.90]  through multiple lenses
[693.90 --> 695.08]  as you're going from
[695.08 --> 696.60]  software development,
[696.84 --> 697.84]  and then you're doing research,
[697.94 --> 698.68]  and then you're at Facebook
[698.68 --> 699.64]  doing research,
[699.68 --> 701.32]  and the scales are changing.
[701.48 --> 702.64]  It seems very much like
[702.64 --> 703.90]  you were scratching
[703.90 --> 704.74]  your own itch,
[704.82 --> 706.50]  but having the benefit
[706.50 --> 708.10]  of taking into account
[708.10 --> 709.76]  multiple perceptions
[709.76 --> 710.98]  of that problem
[710.98 --> 712.06]  so that you ended up
[712.06 --> 713.28]  having a very rich
[713.28 --> 714.32]  understanding
[714.32 --> 715.30]  of what was needed
[715.30 --> 716.54]  and how it could satisfy
[716.54 --> 718.02]  multiple user groups.
[718.12 --> 719.10]  Do you think that's
[719.10 --> 719.98]  a fair assessment,
[720.22 --> 721.60]  or am I missing the boat?
[721.70 --> 722.46]  It seems like it was
[722.46 --> 723.92]  a really smart way
[723.92 --> 725.50]  of building a robust project
[725.50 --> 727.30]  from different perspectives
[727.30 --> 728.36]  all rolled into one.
[728.96 --> 729.18]  Yeah, I mean,
[729.18 --> 729.78]  I think that's right.
[729.84 --> 730.56]  I think, like I said,
[730.70 --> 730.90]  you know,
[730.90 --> 731.68]  none of this was ever
[731.68 --> 732.40]  because I was trying
[732.40 --> 733.14]  to build anything
[733.14 --> 734.10]  for anyone else, right?
[734.10 --> 735.74]  I was trying to make myself
[735.74 --> 736.88]  move faster research.
[737.12 --> 737.24]  Right.
[737.24 --> 738.70]  I think, like,
[738.74 --> 739.38]  once other people
[739.38 --> 740.36]  started using it,
[740.82 --> 741.38]  they gave me
[741.38 --> 742.32]  the perspective there,
[742.42 --> 742.60]  right,
[742.60 --> 743.12]  and they put
[743.12 --> 743.92]  those constraints,
[743.92 --> 744.50]  and, I mean,
[744.70 --> 745.44]  Lightning is not
[745.44 --> 746.04]  where it is today
[746.04 --> 746.62]  because of me.
[746.72 --> 747.22]  It's there because
[747.22 --> 748.04]  of the community, right?
[748.08 --> 748.90]  Like, there's no way
[748.90 --> 749.66]  I could have ever
[749.66 --> 751.10]  created this by myself,
[751.18 --> 751.34]  right?
[751.36 --> 751.86]  I think, like,
[751.88 --> 752.86]  I could see the idea
[752.86 --> 754.02]  and see the templates,
[754.02 --> 755.48]  but a lot of my job
[755.48 --> 756.14]  has been to guide
[756.14 --> 756.66]  the community
[756.66 --> 757.76]  and maintain standards,
[757.92 --> 759.74]  maintain usability, right?
[759.76 --> 760.48]  So I care a lot
[760.48 --> 761.44]  about user experience,
[761.52 --> 762.68]  so, and I don't want
[762.68 --> 763.48]  to remember a lot of stuff,
[763.56 --> 764.58]  so there's just been
[764.58 --> 765.12]  a lot of guidance
[765.12 --> 765.70]  there as well.
[766.12 --> 766.80]  But at the end of the day,
[766.82 --> 767.28]  it's a community
[767.28 --> 768.30]  that's done a lot of this,
[768.42 --> 768.60]  right?
[768.94 --> 770.36]  But I think, like,
[770.58 --> 771.14]  holistically,
[772.10 --> 772.96]  having to focus
[772.96 --> 773.88]  on a lot of domains
[773.88 --> 775.44]  has made it super general,
[775.60 --> 775.80]  right?
[775.88 --> 777.38]  Because doing NLP
[777.38 --> 778.28]  is very different
[778.28 --> 779.52]  from vision,
[779.52 --> 780.40]  and it's very different
[780.40 --> 781.24]  from, you know,
[781.30 --> 782.04]  reinforcement learning
[782.04 --> 782.54]  and meta learning
[782.54 --> 783.06]  and so on,
[783.28 --> 784.22]  and it's not obvious
[784.22 --> 785.42]  to know where they overlap.
[785.54 --> 786.08]  So it's been
[786.08 --> 787.54]  kind of a research project,
[787.60 --> 788.40]  really, in the long run,
[788.48 --> 788.66]  right?
[788.76 --> 789.78]  How do you factor out
[789.78 --> 790.42]  deep learning code
[790.42 --> 791.58]  and make it interruptible?
[792.10 --> 793.04]  Yeah, so that's been
[793.04 --> 794.14]  an interesting journey so far.
[794.14 --> 795.60]  You mentioned
[795.60 --> 796.48]  when you were
[796.48 --> 797.08]  introducing
[797.08 --> 798.10]  the motivation
[798.10 --> 799.70]  behind Lightning,
[799.98 --> 801.14]  the idea of
[801.14 --> 802.10]  decoupling
[802.10 --> 803.12]  models
[803.12 --> 804.12]  from hardware,
[804.56 --> 805.18]  and I noticed,
[805.34 --> 805.50]  like,
[805.56 --> 806.34]  even just on,
[806.44 --> 807.46]  if I look at the
[807.46 --> 808.66]  repository for Lightning,
[808.76 --> 809.50]  you talk about,
[809.56 --> 809.80]  you know,
[810.52 --> 811.08]  PyTorch,
[811.40 --> 812.20]  Lightning is just
[812.20 --> 813.34]  organized PyTorch,
[813.38 --> 814.06]  and it's organized
[814.06 --> 815.04]  to sort of decouple
[815.04 --> 816.26]  science from engineering,
[816.46 --> 816.94]  and so you've got
[816.94 --> 817.78]  this model side
[817.78 --> 818.68]  and the hardware side.
[818.78 --> 819.56]  Could you dive into
[819.56 --> 820.48]  that a little bit more
[820.48 --> 821.40]  and talk about
[821.40 --> 822.24]  the specifics of
[822.24 --> 822.94]  what does it mean
[822.94 --> 824.18]  if I'm using Lightning?
[824.30 --> 824.92]  What does it mean
[824.92 --> 825.96]  that my model
[825.96 --> 827.42]  is disentangled
[827.42 --> 828.34]  or decoupled
[828.34 --> 829.30]  from the hardware,
[829.70 --> 830.38]  both practically
[830.38 --> 831.10]  in terms of
[831.10 --> 832.02]  how I write the code
[832.02 --> 832.56]  and, like,
[832.60 --> 833.28]  what happens,
[833.38 --> 833.68]  like,
[833.96 --> 835.02]  once I hit fit,
[835.10 --> 836.00]  like you're talking about?
[836.56 --> 837.64]  Yeah, so when we're working,
[837.78 --> 838.22]  I mean, look,
[838.28 --> 839.12]  I think if you're working
[839.12 --> 839.74]  at a company
[839.74 --> 841.10]  or any team,
[841.18 --> 841.32]  really,
[841.40 --> 841.94]  even research,
[842.04 --> 842.72]  if you're working
[842.72 --> 843.64]  with multiple people,
[844.06 --> 844.78]  you need the ability
[844.78 --> 845.46]  to share code,
[845.54 --> 846.40]  and if you're at a company
[846.40 --> 848.10]  or even university lab,
[848.10 --> 849.14]  you want to share code
[849.14 --> 850.34]  across teams, right?
[850.84 --> 852.26]  And that's really hard
[852.26 --> 852.72]  to do without
[852.72 --> 853.50]  something like Lightning
[853.50 --> 855.10]  because what happens
[855.10 --> 856.14]  is people tend
[856.14 --> 857.26]  to intermingle
[857.26 --> 857.98]  a lot of stuff
[857.98 --> 858.54]  like data,
[858.72 --> 859.02]  model,
[859.22 --> 860.52]  and hardware
[860.52 --> 862.00]  into the same files, right?
[862.34 --> 862.94]  Well, you know,
[862.98 --> 864.54]  one team may not have GPUs
[864.54 --> 865.14]  or may have different
[865.14 --> 865.94]  types of GPUs
[865.94 --> 867.24]  or may only be using CPUs
[867.24 --> 868.44]  or your production requirements
[868.44 --> 869.56]  mean that you can only use
[869.56 --> 870.74]  CPUs for inference, right?
[870.80 --> 871.76]  So there are a lot
[871.76 --> 872.50]  of constraints there.
[872.96 --> 874.40]  And I guess if you're not
[874.40 --> 875.22]  thinking about it
[875.22 --> 875.78]  how we are
[875.78 --> 876.88]  from the abstract level,
[876.88 --> 878.28]  you won't really realize
[878.28 --> 879.52]  that like a lot
[879.52 --> 879.94]  of the reasons
[879.94 --> 880.78]  why a lot of that code
[880.78 --> 882.14]  doesn't operate together
[882.14 --> 883.12]  is because you're mixing
[883.12 --> 883.54]  the hardware
[883.54 --> 884.76]  with the model code, right?
[885.16 --> 885.76]  And that's something
[885.76 --> 886.36]  that, you know,
[886.38 --> 887.48]  took us four years
[887.48 --> 888.28]  probably to get there
[888.28 --> 889.32]  to see this, right?
[889.34 --> 890.12]  To have these insights.
[890.74 --> 891.68]  And what that means
[891.68 --> 892.94]  is that we can factor out
[892.94 --> 893.56]  deep learning code
[893.56 --> 895.06]  into three major areas.
[895.16 --> 895.86]  Well, at least four,
[895.98 --> 896.48]  I guess, maybe,
[896.60 --> 897.42]  and we'll find more, right?
[897.48 --> 898.38]  I mean, it's ongoing research.
[898.62 --> 900.38]  So one is training code, right?
[900.40 --> 901.08]  So this is anything
[901.08 --> 902.00]  that has to do
[902.00 --> 903.08]  with linking your model
[903.08 --> 904.90]  to the machine specifically.
[904.90 --> 906.42]  So how do you do
[906.42 --> 907.88]  the backward pass?
[908.06 --> 908.80]  You know, backward pass
[908.80 --> 909.32]  and distributive
[909.32 --> 910.00]  is very different
[910.00 --> 911.30]  from just on CPUs, right?
[911.48 --> 912.52]  At least technically speaking.
[912.82 --> 913.68]  What happens if you have
[913.68 --> 914.38]  half precision there?
[914.46 --> 915.20]  What happens if you're
[915.20 --> 916.18]  stochastic with averaging?
[916.40 --> 917.20]  What happens if you have
[917.20 --> 918.36]  truncated back steps, right?
[918.42 --> 919.62]  So there are a lot of details
[919.62 --> 920.18]  that go into it.
[920.54 --> 921.06]  So all of that
[921.06 --> 921.84]  is handled by the trainer.
[922.30 --> 923.50]  And this is the stuff
[923.50 --> 924.38]  that you're going to do
[924.38 --> 925.34]  over and over again, right?
[925.40 --> 925.98]  It doesn't matter
[925.98 --> 927.44]  if you're doing audio
[927.44 --> 929.04]  or speech or vision,
[929.04 --> 929.68]  you're always going to have
[929.68 --> 930.26]  a backward pass.
[930.32 --> 930.78]  You're always going to have
[930.78 --> 931.74]  a training loop and so on.
[932.44 --> 933.36]  The model is the thing
[933.36 --> 933.82]  that changes.
[934.02 --> 935.66]  The model is not just,
[936.30 --> 936.50]  you know,
[936.62 --> 938.00]  I like to think about models.
[938.26 --> 939.28]  I guess Lightning,
[939.38 --> 939.94]  we have this concept
[939.94 --> 940.82]  of a Lightning module.
[941.08 --> 941.46]  And to me,
[941.48 --> 942.04]  a Lightning module
[942.04 --> 943.50]  is more of a system, right?
[943.56 --> 944.84]  So, you know,
[944.86 --> 945.64]  we can think about a model
[945.64 --> 946.18]  like, I don't know,
[946.22 --> 947.34]  like a convolutional network
[947.34 --> 948.70]  or a linear regression model, right?
[948.74 --> 950.54]  Just like a self-contained module.
[951.34 --> 952.08]  Today's models
[952.08 --> 953.96]  are actually not models.
[954.00 --> 954.82]  Like we need a new name
[954.82 --> 955.66]  because there's something
[955.66 --> 956.36]  that doesn't exist.
[956.42 --> 957.26]  And I think the Lightning module,
[957.26 --> 958.28]  which is a system, right?
[958.32 --> 959.64]  Because models now interact
[959.64 --> 960.12]  with each other.
[960.12 --> 961.12]  Like what do you call
[961.12 --> 962.74]  an encoder and a decoder
[962.74 --> 963.46]  working together
[963.46 --> 964.46]  to make an autoencoder
[964.46 --> 965.80]  or variational encoder, right?
[965.82 --> 966.40]  They're not models.
[966.52 --> 967.48]  It's collections of models
[967.48 --> 968.40]  interacting together.
[968.52 --> 969.58]  Same for transformers, right?
[970.18 --> 971.06]  So that's really
[971.06 --> 972.12]  what the Lightning module is about.
[972.24 --> 973.70]  You pass in these models into it
[973.70 --> 975.46]  and then how they interact together
[975.46 --> 976.96]  is abstracted by that, right?
[977.20 --> 977.82]  And I think that's
[977.82 --> 978.58]  a missing abstraction
[978.58 --> 979.60]  that was not there.
[979.80 --> 980.90]  And which is why people
[980.90 --> 981.40]  were jumping through
[981.40 --> 982.26]  so many hoops, right?
[982.26 --> 982.66]  To be like,
[982.66 --> 983.70]  oh, well, how do you do GANs?
[983.70 --> 984.60]  How do you do this other stuff?
[985.18 --> 985.76]  So it's important
[985.76 --> 986.48]  to decouple that
[986.48 --> 987.76]  because now I have
[987.76 --> 988.78]  this single file
[988.78 --> 990.36]  that's completely self-contained
[990.36 --> 991.42]  that I can now share
[991.42 --> 992.40]  with my team across
[992.40 --> 993.30]  in a different division.
[994.02 --> 994.70]  And their problem
[994.70 --> 995.82]  might be completely different
[995.82 --> 996.88]  with a different data set.
[997.00 --> 997.76]  And they don't have to ever
[997.76 --> 998.98]  change the code on that model.
[999.12 --> 999.68]  All they have to do
[999.68 --> 1000.74]  is change what hardware
[1000.74 --> 1001.26]  they're using
[1001.26 --> 1002.36]  and then what the data set is.
[1002.40 --> 1003.28]  As long as it conforms
[1003.28 --> 1004.48]  to the API
[1004.48 --> 1005.44]  that the model is expecting,
[1005.52 --> 1005.90]  it works.
[1006.00 --> 1007.00]  So it makes code
[1007.00 --> 1008.76]  extremely interoperable, right?
[1008.80 --> 1009.94]  So I think people
[1009.94 --> 1010.54]  come to Lightning
[1010.54 --> 1011.90]  because they want to,
[1011.92 --> 1012.18]  you know,
[1012.30 --> 1013.38]  train on multiple GPUs
[1013.38 --> 1013.94]  and so on.
[1014.00 --> 1015.02]  And under the hood,
[1015.04 --> 1015.74]  we have this API
[1015.74 --> 1016.70]  called Accelerators
[1016.70 --> 1017.56]  that lets you do that.
[1017.92 --> 1018.68]  But that's only like
[1018.68 --> 1019.66]  a very small part of it.
[1019.70 --> 1020.78]  I think once you get into it,
[1020.82 --> 1022.22]  you see that the rest of it
[1022.22 --> 1022.96]  is the ability
[1022.96 --> 1024.04]  to collaborate with peers
[1024.04 --> 1024.98]  and be able to
[1024.98 --> 1026.00]  have reproducible
[1026.00 --> 1026.82]  and scalable code.
[1043.38 --> 1045.02]  This episode is brought to you
[1045.02 --> 1046.52]  by Snowplow Analytics.
[1047.10 --> 1048.58]  Snowplow is the behavioral
[1048.58 --> 1049.78]  data management platform
[1049.78 --> 1050.84]  for data teams.
[1051.34 --> 1052.42]  Maximize the value
[1052.42 --> 1053.86]  of your behavioral data
[1053.86 --> 1055.32]  using Snowplow Insights,
[1055.58 --> 1057.00]  a managed data platform
[1057.00 --> 1057.84]  that's built on
[1057.84 --> 1058.94]  leading open source tech
[1058.94 --> 1060.50]  leveraged by tens
[1060.50 --> 1061.90]  of thousands of users.
[1062.30 --> 1063.52]  Capture and process
[1063.52 --> 1064.76]  high quality behavioral data
[1064.76 --> 1065.84]  from all your platforms
[1065.84 --> 1066.86]  and your products
[1066.86 --> 1067.96]  and deliver that data
[1067.96 --> 1068.90]  to your cloud destination
[1068.90 --> 1069.50]  of choice.
[1069.50 --> 1070.72]  When marketing needs
[1070.72 --> 1072.10]  to make data-informed decisions,
[1072.10 --> 1073.16]  when product needs
[1073.16 --> 1074.30]  next-level understanding,
[1074.72 --> 1075.40]  and when analytics
[1075.40 --> 1077.18]  needs rich and accurate data,
[1077.52 --> 1078.60]  Snowplow is the solution
[1078.60 --> 1079.26]  for data teams
[1079.26 --> 1079.94]  who want to manage
[1079.94 --> 1080.54]  the collection,
[1080.96 --> 1081.32]  processing,
[1081.76 --> 1082.90]  and warehousing of data
[1082.90 --> 1084.20]  across all their platforms
[1084.20 --> 1084.80]  and products.
[1085.14 --> 1086.22]  Get started and experience
[1086.22 --> 1087.28]  Snowplow data for yourself
[1087.28 --> 1089.22]  at SnowplowAnalytics.com.
[1089.54 --> 1092.14]  Again, SnowplowAnalytics.com.
[1102.10 --> 1106.84]  Thank you for the great introduction
[1106.84 --> 1109.02]  to what lightning is
[1109.02 --> 1111.06]  and how to think about
[1111.06 --> 1112.70]  some of the abstractions
[1112.70 --> 1113.76]  that you're working with.
[1113.86 --> 1115.12]  I'm wondering if you could
[1115.12 --> 1116.68]  maybe share a little bit.
[1116.76 --> 1117.74]  I've seen some different
[1117.74 --> 1118.66]  stories online,
[1118.66 --> 1119.64]  but I was wondering
[1119.64 --> 1120.82]  from your experience
[1120.82 --> 1122.12]  with the community
[1122.12 --> 1123.30]  that's working with this,
[1123.40 --> 1124.06]  could you provide
[1124.06 --> 1125.38]  any sort of stories
[1125.38 --> 1127.10]  around how people
[1127.10 --> 1127.84]  have been able
[1127.84 --> 1128.98]  to scale things up
[1128.98 --> 1129.72]  with lightning,
[1129.72 --> 1131.72]  maybe in your own work,
[1131.72 --> 1132.94]  or maybe, you know,
[1132.96 --> 1134.20]  stories that you like
[1134.20 --> 1134.72]  to highlight?
[1135.24 --> 1135.94]  I mean, there are a lot
[1135.94 --> 1137.28]  of companies and labs
[1137.28 --> 1138.48]  using lightning today, right?
[1138.50 --> 1140.42]  So you can get on GitHub
[1140.42 --> 1141.74]  and see that for yourself.
[1141.86 --> 1142.22]  I think,
[1142.68 --> 1143.96]  I don't know the exact numbers,
[1144.12 --> 1146.00]  but it's definitely like,
[1146.56 --> 1147.46]  you know, the thousands,
[1147.58 --> 1148.24]  like a few thousands
[1148.24 --> 1149.04]  of them, right?
[1149.46 --> 1152.14]  And they go from pharma
[1152.14 --> 1153.58]  to retail
[1153.58 --> 1156.04]  to anything you can think of, right?
[1156.04 --> 1157.68]  And I think today
[1157.68 --> 1159.14]  what's interesting is that
[1159.14 --> 1161.14]  when I run into these people
[1161.14 --> 1162.40]  because we're coming
[1162.40 --> 1163.26]  to work with them on Grid
[1163.26 --> 1164.00]  on some of them,
[1164.38 --> 1165.16]  it's interesting to hear
[1165.16 --> 1165.98]  the use cases, right?
[1166.04 --> 1166.92]  Like stuff that I would
[1166.92 --> 1168.26]  never imagine, right?
[1168.26 --> 1169.18]  Because I'm not at a company
[1169.18 --> 1169.96]  doing this kind of stuff.
[1170.02 --> 1171.32]  So that's why I made the joke
[1171.32 --> 1171.98]  about Lockheed Martin,
[1172.08 --> 1172.82]  but I'm sure you guys
[1172.82 --> 1173.82]  are doing much more
[1173.82 --> 1174.40]  advanced stuff.
[1174.58 --> 1175.38]  Unless I'm building,
[1175.46 --> 1176.34]  you know, planes,
[1176.48 --> 1177.70]  there's no way that I'd know
[1177.70 --> 1178.64]  to do that, right?
[1179.20 --> 1180.54]  So what's cool is just like,
[1180.82 --> 1181.90]  it's been super flexible.
[1182.06 --> 1183.20]  I think there are public cases
[1183.20 --> 1184.24]  that we can talk about.
[1184.38 --> 1185.58]  I mean, there are blog posts
[1185.58 --> 1187.08]  by big companies like NVIDIA,
[1187.38 --> 1188.36]  Facebook, and so on,
[1188.36 --> 1189.66]  about how they use Lightning,
[1189.76 --> 1189.92]  right?
[1189.92 --> 1190.56]  So you can read that.
[1190.62 --> 1191.52]  And I think something
[1191.52 --> 1192.98]  that we do specifically
[1192.98 --> 1194.00]  in the community is like,
[1194.06 --> 1195.40]  we really like to kind of
[1195.40 --> 1196.50]  protect our partners
[1196.50 --> 1197.24]  because like,
[1197.64 --> 1198.34]  this is a community
[1198.34 --> 1200.36]  and we want to keep people's work
[1200.36 --> 1201.56]  fairly private as well.
[1201.80 --> 1202.58]  So I won't get into
[1202.58 --> 1203.18]  too many details.
[1203.18 --> 1204.24]  So I'm just pointing you
[1204.24 --> 1204.94]  to open sources
[1204.94 --> 1205.80]  that you can look at
[1205.80 --> 1207.04]  and how they use it, right?
[1207.06 --> 1207.94]  But these are big projects
[1207.94 --> 1208.26]  as well.
[1208.34 --> 1209.44]  And there are probably
[1209.44 --> 1211.26]  about 3,000 projects
[1211.26 --> 1211.96]  now that use Lightning
[1211.96 --> 1212.60]  that you can literally
[1212.60 --> 1213.86]  just go to see them.
[1214.18 --> 1214.82]  So the companies
[1214.82 --> 1215.52]  that have open sourced
[1215.52 --> 1216.08]  their work,
[1216.22 --> 1217.04]  you can see what projects
[1217.04 --> 1217.48]  are working on.
[1217.78 --> 1218.52]  So it's everything
[1218.52 --> 1220.28]  from like video prediction
[1220.28 --> 1221.56]  to segmentation
[1221.56 --> 1223.22]  to NLP, right?
[1223.28 --> 1224.00]  To summarization
[1224.00 --> 1224.92]  to classification.
[1225.70 --> 1226.56]  We integrate really well
[1226.56 --> 1227.42]  with basically
[1227.42 --> 1228.46]  most frameworks out there.
[1228.58 --> 1229.92]  So if you use anything
[1229.92 --> 1231.16]  that's PyTorch-based,
[1231.26 --> 1232.40]  it's very likely going
[1232.40 --> 1233.06]  to work with Lightning
[1233.06 --> 1233.62]  off the bat.
[1234.26 --> 1235.52]  Now, in terms of scaling,
[1236.26 --> 1237.06]  I mean, I've personally,
[1237.20 --> 1238.50]  we've done it internally, right?
[1238.56 --> 1239.28]  But we've also heard
[1239.28 --> 1240.20]  from the corporate partners
[1240.20 --> 1241.92]  that they're training things
[1241.92 --> 1242.98]  on, yeah,
[1242.98 --> 1244.58]  I mean, I guess the number,
[1245.32 --> 1245.74]  I don't know,
[1245.84 --> 1247.22]  there's no real limit so far.
[1247.28 --> 1247.82]  I guess it's whatever
[1247.82 --> 1248.68]  PyTorch supports.
[1249.80 --> 1251.06]  However many GPUs
[1251.06 --> 1251.86]  you can get your hands on.
[1251.86 --> 1252.58]  Yeah, and like, you know,
[1252.62 --> 1253.58]  that's a big part
[1253.58 --> 1254.36]  of Grid now, right?
[1254.40 --> 1255.18]  It's like with Grid
[1255.18 --> 1255.54]  and Lightning,
[1255.70 --> 1256.72]  you can literally type in,
[1256.76 --> 1257.02]  I don't know,
[1257.06 --> 1258.00]  1,000 GPUs.
[1258.06 --> 1258.78]  And if you have
[1258.78 --> 1259.86]  the Amazon quota,
[1260.02 --> 1261.44]  like, great, you know?
[1262.32 --> 1263.40]  And we can give you
[1263.40 --> 1264.60]  as many as we can as well,
[1264.68 --> 1266.00]  but there's no limitation, right?
[1266.04 --> 1267.48]  So you just have to run it.
[1267.68 --> 1268.18]  And like, I know
[1268.18 --> 1268.80]  it sounds crazy,
[1268.80 --> 1269.54]  but you literally
[1269.54 --> 1270.36]  just have to run it
[1270.36 --> 1271.54]  and then it'll just work, right?
[1271.54 --> 1273.26]  So it's just a function
[1273.26 --> 1274.14]  of the compute there.
[1274.26 --> 1276.18]  I mean, a few weeks ago,
[1276.30 --> 1277.06]  no, it was like a month
[1277.06 --> 1278.00]  ago at this point,
[1278.08 --> 1278.78]  we did a collaboration
[1278.78 --> 1279.46]  with Microsoft.
[1279.66 --> 1280.86]  So Microsoft has this library
[1280.86 --> 1281.56]  called DeepSpeed,
[1281.60 --> 1282.22]  which is really cool.
[1282.76 --> 1283.66]  Facebook has one
[1283.66 --> 1285.18]  also with the Fairscale team.
[1285.36 --> 1285.76]  And basically,
[1285.94 --> 1286.96]  it lets you scale up models
[1286.96 --> 1288.88]  dramatically by helping
[1288.88 --> 1290.68]  you use CPU memory efficiently.
[1291.04 --> 1291.64]  And, you know,
[1291.66 --> 1292.92]  the way you shard gradients
[1292.92 --> 1294.08]  and the way you shard
[1294.08 --> 1295.54]  parameters across GPUs
[1296.06 --> 1296.54]  really helps.
[1297.10 --> 1297.80]  So we were able
[1297.80 --> 1300.80]  to train a GPT model,
[1300.80 --> 1302.00]  I think it was like,
[1302.60 --> 1303.40]  I remember it was like
[1303.40 --> 1304.74]  20 billion parameters
[1304.74 --> 1305.54]  or something like that.
[1305.86 --> 1306.74]  So we have a case study
[1306.74 --> 1307.10]  for that.
[1307.52 --> 1308.84]  So just for context,
[1309.02 --> 1310.22]  like the original GPT-3
[1310.22 --> 1311.64]  was, I don't remember,
[1311.76 --> 1312.18]  it was like,
[1312.48 --> 1313.28]  hold on, let me see here,
[1313.74 --> 1315.06]  160 billion parameters
[1315.06 --> 1315.76]  or something like that.
[1316.48 --> 1317.38]  So I don't want
[1317.38 --> 1318.58]  to misquote you numbers,
[1318.76 --> 1319.78]  but basically whatever
[1319.78 --> 1321.30]  the original GPT-3 was,
[1321.36 --> 1322.06]  I think it was like
[1322.06 --> 1323.02]  one third of that.
[1323.12 --> 1324.38]  Well, only eight GPUs.
[1325.04 --> 1326.68]  So that's crazy.
[1326.86 --> 1327.48]  Just, I don't think
[1327.48 --> 1328.54]  anyone in industry
[1328.54 --> 1329.38]  needs that much.
[1329.38 --> 1330.28]  I haven't seen people
[1330.28 --> 1330.82]  use that much.
[1330.96 --> 1332.12]  So I'm just saying like,
[1332.58 --> 1333.94]  that's a pretty good
[1333.94 --> 1335.26]  lower bound.
[1336.62 --> 1338.38]  175 billion.
[1338.74 --> 1339.52]  That's, or at least
[1339.52 --> 1340.08]  that's what Google
[1340.08 --> 1341.40]  is telling me on a search.
[1341.56 --> 1341.78]  Yeah.
[1341.98 --> 1343.12]  So you were very close
[1343.12 --> 1344.04]  and you said you were
[1344.04 --> 1344.80]  running that on what,
[1344.88 --> 1345.92]  eight GPUs?
[1346.12 --> 1347.10]  Yeah, on A100s.
[1347.22 --> 1347.76]  Only eight of them.
[1347.76 --> 1347.94]  Oh, wow.
[1348.08 --> 1349.48]  And I mean, it's A100s,
[1349.50 --> 1350.14]  so they're much bigger
[1350.14 --> 1350.86]  than V100s,
[1350.98 --> 1351.86]  but I mean,
[1351.90 --> 1353.10]  we'll be doing more tests.
[1353.44 --> 1353.96]  That was with these,
[1354.06 --> 1354.52]  just literally,
[1354.64 --> 1355.42]  and what's cool about it
[1355.42 --> 1355.92]  is if you're just
[1355.92 --> 1356.40]  using Lightning
[1356.40 --> 1357.66]  on your trainer,
[1357.66 --> 1358.42]  you just say,
[1358.52 --> 1359.12]  I think it's like
[1359.12 --> 1361.08]  plugin equals DeepSpeed,
[1361.14 --> 1362.48]  like a string called DeepSpeed.
[1362.54 --> 1363.40]  Just by doing that,
[1363.48 --> 1364.58]  you get that out of the box,
[1364.72 --> 1364.92]  right?
[1365.42 --> 1366.52]  So that's the kind of stuff
[1366.52 --> 1367.54]  that we embed into training.
[1367.72 --> 1368.40]  So, you know,
[1368.44 --> 1369.04]  do you have to know
[1369.04 --> 1369.66]  how to do that?
[1369.72 --> 1370.16]  You don't,
[1370.32 --> 1371.38]  but now you get that benefit.
[1371.38 --> 1373.70]  So I want to real quick
[1373.70 --> 1374.46]  pop in one thing
[1374.46 --> 1375.30]  before we kind of
[1375.30 --> 1376.58]  start moving on on this.
[1376.98 --> 1377.76]  There are some people
[1377.76 --> 1378.36]  that are listening
[1378.36 --> 1379.00]  that may not,
[1379.10 --> 1379.80]  they may even be
[1379.80 --> 1380.90]  not PyTorch users.
[1381.00 --> 1382.06]  They might be TensorFlow users,
[1382.06 --> 1382.66]  but they're thinking
[1382.66 --> 1383.24]  about switching.
[1383.58 --> 1383.74]  You know,
[1383.82 --> 1385.20]  we always get into conversations.
[1385.80 --> 1387.32]  How does a workflow look like
[1387.32 --> 1388.26]  when you're integrating
[1388.26 --> 1389.14]  PyTorch Lightning
[1389.14 --> 1390.28]  into your workflow?
[1390.82 --> 1391.84]  You're using the rest
[1391.84 --> 1392.64]  of the ecosystem.
[1392.88 --> 1393.96]  Could you at a high level
[1393.96 --> 1394.96]  just for those
[1394.96 --> 1395.90]  who haven't used it
[1395.90 --> 1397.40]  and maybe not have the
[1397.40 --> 1398.58]  something directly
[1398.58 --> 1399.04]  that they're going,
[1399.16 --> 1399.46]  oh yeah,
[1399.60 --> 1400.54]  I've done similar to that.
[1400.54 --> 1401.18]  I can just add lightning
[1401.18 --> 1401.52]  into that.
[1401.76 --> 1402.60]  What that looks like,
[1402.74 --> 1403.54]  what that savings,
[1403.68 --> 1404.56]  why is it called lightning
[1404.56 --> 1405.08]  for them?
[1405.14 --> 1405.62]  They're kind of going,
[1405.72 --> 1406.48]  oh, there's this thing
[1406.48 --> 1407.94]  that may really help me.
[1408.02 --> 1408.80]  Can you kind of just
[1408.80 --> 1410.28]  top off a little bit
[1410.28 --> 1410.80]  of a workflow
[1410.80 --> 1411.80]  on how I go
[1411.80 --> 1412.58]  from the beginning
[1412.58 --> 1413.78]  to getting something
[1413.78 --> 1414.82]  productively deployed
[1414.82 --> 1415.96]  and what that looks like
[1415.96 --> 1416.52]  for somebody
[1416.52 --> 1417.38]  who hasn't seen it before?
[1417.86 --> 1418.30]  Yeah, absolutely.
[1418.58 --> 1419.34]  Wait, so I found
[1419.34 --> 1419.88]  the blog post.
[1420.00 --> 1420.64]  So it was actually
[1420.64 --> 1421.94]  45 billion parameters
[1421.94 --> 1422.84]  that we scaled it up
[1422.84 --> 1424.22]  on eight A100s.
[1424.42 --> 1425.34]  And you can look it up
[1425.34 --> 1425.80]  but it's called
[1425.80 --> 1427.04]  accessible multi-billion
[1427.04 --> 1428.06]  parameter model training
[1428.06 --> 1429.16]  with PyTorch Lightning
[1429.16 --> 1429.96]  and DeepSpeed.
[1429.96 --> 1431.00]  And we'll link it
[1431.00 --> 1431.74]  in the show notes.
[1431.94 --> 1432.66]  Yeah, sounds good.
[1433.08 --> 1434.50]  Okay, so basically
[1434.50 --> 1435.24]  it's how do you adopt
[1435.24 --> 1436.12]  lightning into your workflow,
[1436.22 --> 1436.38]  right?
[1436.46 --> 1437.66]  So, I mean,
[1437.68 --> 1438.76]  obviously if you're coming
[1438.76 --> 1439.72]  from not PyTorch,
[1439.84 --> 1440.98]  then you would just,
[1441.10 --> 1441.64]  you know,
[1441.72 --> 1442.48]  start with lightning.
[1442.82 --> 1444.16]  There's a very simple
[1444.16 --> 1444.68]  readme there.
[1444.80 --> 1445.50]  Like I would say,
[1446.18 --> 1446.42]  you know,
[1446.50 --> 1447.50]  copy paste that readme.
[1447.60 --> 1448.64]  There's an MNIST example
[1448.64 --> 1448.98]  on there
[1448.98 --> 1450.16]  and you just run it.
[1450.30 --> 1451.30]  You'll notice those people
[1451.30 --> 1451.62]  will say,
[1451.70 --> 1452.26]  well, but where are
[1452.26 --> 1452.98]  the advanced examples?
[1453.10 --> 1453.86]  And my point is that
[1453.86 --> 1455.04]  that is the advanced example.
[1455.24 --> 1455.80]  Like all you have to do
[1455.80 --> 1456.52]  is change the data
[1456.52 --> 1457.28]  and it'll still work
[1457.28 --> 1458.18]  for ImageNet, right?
[1458.18 --> 1458.22]  Right?
[1459.44 --> 1459.76]  So,
[1459.96 --> 1461.22]  that's the beauty of it.
[1461.26 --> 1461.96]  There's no different
[1461.96 --> 1462.76]  example for that.
[1462.86 --> 1463.02]  I mean,
[1463.04 --> 1464.14]  we put it in if you want,
[1464.30 --> 1465.12]  but at the end of the day,
[1465.16 --> 1465.92]  just change your data
[1465.92 --> 1467.74]  and set GPUs to 64
[1467.74 --> 1468.62]  and you're good to go.
[1469.12 --> 1469.42]  So,
[1469.74 --> 1470.70]  that's the easy part, right?
[1470.70 --> 1470.82]  So,
[1470.82 --> 1471.18]  if you're coming
[1471.18 --> 1471.98]  outside of PyTorch,
[1472.06 --> 1472.74]  then you can do that.
[1473.08 --> 1473.54]  If you're coming
[1473.54 --> 1474.52]  from within PyTorch,
[1474.62 --> 1475.72]  then what two people
[1475.72 --> 1476.26]  tend to do is
[1476.26 --> 1476.70]  when they start
[1476.70 --> 1477.32]  a new project,
[1477.48 --> 1478.08]  they'll either start
[1478.08 --> 1478.96]  it on lightning directly
[1478.96 --> 1479.96]  or they'll convert
[1479.96 --> 1480.86]  their existing projects
[1480.86 --> 1481.72]  into lightning.
[1482.34 --> 1482.50]  So,
[1482.62 --> 1483.30]  it is really
[1483.30 --> 1484.34]  a refactor
[1484.34 --> 1485.54]  on your PyTorch project,
[1485.66 --> 1485.84]  right?
[1485.92 --> 1486.08]  So,
[1486.16 --> 1487.10]  you basically take
[1487.10 --> 1489.58]  your main loop code,
[1489.70 --> 1490.66]  which usually looks
[1490.66 --> 1491.36]  something like,
[1491.88 --> 1492.16]  you know,
[1492.22 --> 1493.16]  you initialize a model,
[1493.30 --> 1494.38]  you set a bunch of flags,
[1494.52 --> 1495.18]  you set some sort
[1495.18 --> 1496.10]  of arc parse arguments,
[1496.52 --> 1497.58]  and then you download
[1497.58 --> 1498.16]  some data
[1498.16 --> 1499.32]  or link it somehow.
[1499.94 --> 1500.30]  And then,
[1500.34 --> 1500.58]  you know,
[1500.62 --> 1501.46]  it's all boilerplate.
[1501.60 --> 1502.34]  And then there's like
[1502.34 --> 1502.76]  a loop,
[1503.04 --> 1503.78]  two loops in there,
[1503.84 --> 1504.54]  which is like,
[1504.64 --> 1504.94]  you know,
[1505.00 --> 1506.90]  four epochs and epochs.
[1506.90 --> 1507.76]  And then you have in there
[1507.76 --> 1509.94]  four batch in your data loader
[1509.94 --> 1510.76]  and then you start training.
[1511.26 --> 1511.42]  So,
[1511.68 --> 1512.06]  literally,
[1512.50 --> 1514.00]  everything up to that
[1514.00 --> 1515.48]  four batch in your data loader
[1515.48 --> 1516.32]  is deleted,
[1516.54 --> 1516.74]  right?
[1516.82 --> 1516.94]  So,
[1517.02 --> 1517.42]  it's gone.
[1518.10 --> 1518.18]  Yeah.
[1518.30 --> 1518.62]  So,
[1518.78 --> 1519.56]  then the only thing
[1519.56 --> 1520.40]  that you need to track
[1520.40 --> 1521.18]  is what's in there,
[1521.20 --> 1521.34]  right?
[1521.38 --> 1521.94]  Which is like,
[1522.06 --> 1523.46]  we call that the training step,
[1523.50 --> 1524.04]  which is the meat
[1524.04 --> 1524.52]  of what you want.
[1524.60 --> 1524.72]  I mean,
[1524.74 --> 1525.64]  think about when you're doing work,
[1525.72 --> 1526.44]  like that's where you spend
[1526.44 --> 1526.94]  your time on.
[1527.46 --> 1527.72]  So,
[1527.72 --> 1528.74]  that goes into this function
[1528.74 --> 1529.80]  called the training step.
[1530.42 --> 1531.30]  And then the training step
[1531.30 --> 1532.28]  goes all the way
[1532.28 --> 1533.24]  from taking your batch
[1533.24 --> 1534.36]  into generating a loss
[1534.36 --> 1535.04]  that you return
[1535.04 --> 1536.20]  with that gradient attached,
[1536.32 --> 1536.48]  right?
[1536.48 --> 1536.70]  So,
[1536.76 --> 1537.24]  some graph.
[1537.80 --> 1538.04]  So,
[1538.68 --> 1539.52]  you know,
[1539.54 --> 1540.38]  it could be a few lines.
[1540.62 --> 1540.94]  Usually,
[1541.04 --> 1541.92]  it's only a few lines
[1541.92 --> 1543.04]  because that's most
[1543.04 --> 1543.56]  of what you're doing.
[1544.60 --> 1544.94]  Now,
[1545.02 --> 1546.14]  the model that you left
[1546.14 --> 1546.74]  at the top,
[1547.04 --> 1547.36]  that one,
[1547.42 --> 1548.22]  you can keep it separate
[1548.22 --> 1548.96]  and just pass it
[1548.96 --> 1549.68]  into lightning module
[1549.68 --> 1550.36]  and just use it,
[1550.42 --> 1550.54]  you know,
[1550.62 --> 1551.76]  soft.model equals model.
[1552.00 --> 1553.02]  Or you can define
[1553.02 --> 1553.60]  that model
[1553.60 --> 1554.48]  within the lightning module,
[1554.58 --> 1554.76]  right?
[1554.82 --> 1554.98]  So,
[1555.06 --> 1555.60]  you can literally
[1555.60 --> 1556.72]  copy paste the layers
[1556.72 --> 1557.16]  and all that
[1557.16 --> 1557.98]  into the lightning module
[1557.98 --> 1558.40]  if you want
[1558.40 --> 1559.78]  because the lightning module
[1559.78 --> 1560.94]  is an nn.module
[1560.94 --> 1561.60]  at the end of the day.
[1562.04 --> 1562.20]  So,
[1562.54 --> 1563.32]  that gets you
[1563.32 --> 1564.58]  basically most of it.
[1564.72 --> 1565.32]  Then you need to find
[1565.32 --> 1566.06]  your optimizer
[1566.06 --> 1567.20]  and bring it
[1567.20 --> 1567.68]  into a function
[1567.68 --> 1568.98]  called configure optimizers
[1568.98 --> 1570.44]  and then you just
[1570.44 --> 1571.12]  return it there,
[1571.22 --> 1571.40]  right?
[1571.40 --> 1571.60]  So,
[1571.68 --> 1571.86]  then,
[1572.04 --> 1572.36]  you know,
[1572.38 --> 1572.90]  you're going to link up
[1572.90 --> 1573.48]  the parameters
[1573.48 --> 1574.36]  through that as well.
[1574.74 --> 1574.92]  So,
[1574.96 --> 1575.64]  that's three methods,
[1575.74 --> 1575.88]  right?
[1575.92 --> 1576.46]  That's your init,
[1576.58 --> 1577.44]  that's your training step
[1577.44 --> 1577.94]  and then that's your
[1577.94 --> 1578.80]  configure optimizer.
[1579.34 --> 1581.08]  And then the rest of that
[1581.08 --> 1582.00]  is optional
[1582.00 --> 1582.80]  after that,
[1582.88 --> 1583.06]  right?
[1583.12 --> 1583.30]  So,
[1583.46 --> 1583.84]  forward,
[1583.98 --> 1585.02]  we don't actually need it.
[1585.30 --> 1586.72]  We use the forward method
[1586.72 --> 1587.76]  for inference,
[1587.88 --> 1588.04]  right?
[1588.04 --> 1588.16]  So,
[1588.16 --> 1589.04]  if you train a model
[1589.04 --> 1590.34]  and you,
[1590.46 --> 1590.78]  for example,
[1590.86 --> 1591.46]  an autoencoder,
[1591.58 --> 1591.72]  right?
[1591.76 --> 1591.84]  So,
[1591.84 --> 1593.04]  an autoencoder has two sides,
[1593.12 --> 1594.16]  an encoder and a decoder.
[1594.16 --> 1595.88]  The encoder maps some input
[1595.88 --> 1596.78]  into some space
[1596.78 --> 1597.76]  and embedding
[1597.76 --> 1598.92]  and then the decoder maps
[1598.92 --> 1599.64]  that embedding back
[1599.64 --> 1600.74]  into some space.
[1601.18 --> 1601.26]  So,
[1601.32 --> 1602.28]  an autoencoder can be used
[1602.28 --> 1602.80]  in two ways.
[1602.94 --> 1603.68]  You can use it as,
[1604.02 --> 1604.80]  you know,
[1604.84 --> 1605.24]  an embedder,
[1605.36 --> 1605.68]  basically.
[1606.10 --> 1606.28]  So,
[1606.34 --> 1607.04]  you can take an image
[1607.04 --> 1608.02]  and get an embedding for it
[1608.02 --> 1608.30]  and then,
[1608.44 --> 1608.64]  you know,
[1608.68 --> 1609.60]  do similarity search
[1609.60 --> 1610.06]  and so on.
[1610.16 --> 1610.24]  So,
[1610.28 --> 1610.96]  if you're building like
[1610.96 --> 1611.62]  a visual engine
[1611.62 --> 1611.98]  or something,
[1612.06 --> 1612.54]  you would do that.
[1613.08 --> 1614.10]  Or you can use a decoder
[1614.10 --> 1614.60]  for sampling.
[1614.78 --> 1616.26]  You can give it a random vector
[1616.26 --> 1617.16]  and it'll give you an image,
[1617.22 --> 1617.58]  for example,
[1617.96 --> 1618.20]  or,
[1618.20 --> 1618.54]  you know,
[1618.60 --> 1619.42]  text or whatever you want.
[1619.90 --> 1620.12]  So,
[1620.50 --> 1622.08]  depending on what your use case is,
[1622.08 --> 1623.18]  that's how you're going to
[1623.18 --> 1624.00]  implement the forward
[1624.00 --> 1625.50]  because the forward
[1625.50 --> 1626.44]  is what's going to be called
[1626.44 --> 1627.12]  in production,
[1627.30 --> 1627.42]  right?
[1627.44 --> 1628.26]  You're going to call the model
[1628.26 --> 1629.22]  with the input to it.
[1629.64 --> 1629.90]  So,
[1630.06 --> 1631.20]  we actually allow
[1631.20 --> 1632.84]  the model to be Torch scripted
[1632.84 --> 1634.52]  and put into Onyx as well,
[1634.66 --> 1635.22]  O-N-X,
[1635.36 --> 1635.58]  I guess,
[1636.10 --> 1637.12]  for production use cases.
[1637.24 --> 1638.08]  It's literally a function
[1638.08 --> 1639.40]  called .toTorchScript
[1639.40 --> 1640.16]  .toOnyx
[1640.16 --> 1640.98]  and then you're good to go
[1640.98 --> 1642.40]  and it does all the things for you.
[1643.04 --> 1643.44]  And then,
[1643.50 --> 1643.66]  you know,
[1643.68 --> 1644.26]  you just have to
[1644.26 --> 1644.92]  get the inputs,
[1645.10 --> 1645.66]  transform it,
[1645.84 --> 1646.34]  pass it through
[1646.34 --> 1647.52]  and then do the return.
[1647.60 --> 1647.68]  So,
[1647.72 --> 1648.20]  it's very simple.
[1648.94 --> 1649.14]  Now,
[1649.28 --> 1650.92]  there's other stuff left.
[1651.26 --> 1651.34]  So,
[1651.34 --> 1652.02]  that's literally
[1652.02 --> 1652.26]  it.
[1652.34 --> 1652.44]  So,
[1652.54 --> 1653.70]  you just have to copy that stuff.
[1654.26 --> 1654.54]  And then,
[1654.62 --> 1655.52]  anything else that's left
[1655.52 --> 1657.02]  is usually around data
[1657.02 --> 1657.94]  or maybe validation
[1657.94 --> 1658.92]  or testing.
[1659.44 --> 1660.08]  The validation,
[1660.52 --> 1661.80]  we have a validation step
[1661.80 --> 1663.22]  and a test step as well
[1663.22 --> 1664.08]  where you can just copy,
[1664.24 --> 1665.00]  paste that code in there
[1665.00 --> 1666.10]  if you want a validation loop
[1666.10 --> 1666.70]  or test loop.
[1667.12 --> 1667.82]  For the data,
[1667.94 --> 1668.72]  you can leave it as this.
[1668.76 --> 1669.52]  You can just pass in
[1669.52 --> 1670.58]  the data loaders directly
[1670.58 --> 1671.40]  to Lightning
[1671.40 --> 1673.18]  or you can use something
[1673.18 --> 1674.04]  called the data module
[1674.04 --> 1674.84]  which is a completely
[1674.84 --> 1675.68]  optional abstraction
[1675.68 --> 1677.22]  but it basically
[1677.22 --> 1678.86]  captures your training,
[1679.22 --> 1679.58]  validation,
[1679.82 --> 1680.68]  and test data loader
[1680.68 --> 1681.40]  into one class
[1681.40 --> 1682.42]  and couples
[1682.42 --> 1683.36]  and transforms as well
[1683.36 --> 1685.26]  because what usually happens
[1685.26 --> 1686.10]  in big companies
[1686.10 --> 1686.66]  is that,
[1687.12 --> 1687.38]  you know,
[1687.44 --> 1688.36]  I'm working on,
[1688.56 --> 1688.90]  I don't know,
[1688.98 --> 1689.82]  let's say I'm doing,
[1690.22 --> 1690.62]  I guess,
[1690.92 --> 1693.08]  maybe selling something,
[1693.28 --> 1693.44]  right?
[1693.48 --> 1693.76]  And so,
[1694.16 --> 1695.58]  I'm selling clothing
[1695.58 --> 1696.16]  and so,
[1696.28 --> 1697.16]  I have the data set
[1697.16 --> 1697.88]  of our inventory
[1697.88 --> 1698.64]  with images
[1698.64 --> 1699.22]  and so on
[1699.22 --> 1700.80]  and then when I give it to you,
[1700.86 --> 1701.42]  you're going to be like,
[1701.50 --> 1701.64]  hey,
[1701.68 --> 1702.78]  how did you transform the images?
[1703.00 --> 1703.64]  Did you crop it?
[1703.68 --> 1704.40]  Did you random flip?
[1704.48 --> 1705.18]  What did you do, right?
[1705.54 --> 1705.72]  So,
[1705.78 --> 1706.74]  unless I give you that code,
[1707.10 --> 1707.68]  then it's going to be
[1707.68 --> 1708.30]  a little bit hard
[1708.30 --> 1709.52]  and we could mess it up.
[1709.60 --> 1709.66]  So,
[1709.72 --> 1710.32]  the data module
[1710.32 --> 1711.02]  embeds all of that.
[1711.06 --> 1711.14]  So,
[1711.16 --> 1711.82]  I just have to say,
[1712.22 --> 1713.12]  here's a data module
[1713.12 --> 1714.72]  for the clothing data set
[1714.72 --> 1715.62]  and you just run it
[1715.62 --> 1716.36]  and you know it's going to be
[1716.36 --> 1717.36]  consistent across the board
[1717.36 --> 1718.24]  no matter how you run it.
[1718.66 --> 1718.76]  So,
[1718.82 --> 1719.46]  that's an optional,
[1719.80 --> 1720.00]  I mean,
[1720.04 --> 1721.24]  highly encouraged abstraction
[1721.24 --> 1721.92]  but it's optional.
[1722.54 --> 1722.70]  Yeah,
[1722.76 --> 1723.60]  that's basically it.
[1723.70 --> 1723.82]  So,
[1723.92 --> 1724.76]  if you do it,
[1724.84 --> 1726.00]  I would just recommend like,
[1726.60 --> 1727.80]  don't delete your project,
[1728.02 --> 1729.36]  just do the refactor first,
[1729.48 --> 1730.22]  put it into Lightning,
[1730.74 --> 1731.56]  run it once,
[1731.72 --> 1731.94]  right?
[1732.10 --> 1733.12]  You can run it on CPU,
[1733.22 --> 1733.94]  when you do it with Lightning,
[1734.02 --> 1734.74]  you're going to be able to run it
[1734.74 --> 1735.56]  on your local machine
[1735.56 --> 1736.86]  with CPUs or GPUs.
[1737.34 --> 1738.54]  Take a batch of data
[1738.54 --> 1739.70]  from your data set
[1739.70 --> 1741.06]  or a single example
[1741.06 --> 1742.78]  and overfit both models,
[1742.92 --> 1744.12]  like your original code
[1744.12 --> 1744.72]  and this one
[1744.72 --> 1745.34]  with the same seed
[1745.34 --> 1745.76]  and everything
[1745.76 --> 1746.34]  and make sure you get
[1746.34 --> 1746.94]  the same results
[1746.94 --> 1747.86]  and then once you get that,
[1747.96 --> 1748.52]  then you're good to go.
[1748.60 --> 1749.46]  You know you didn't mess it up.
[1749.74 --> 1750.28]  At that point,
[1750.34 --> 1750.88]  you can go ahead
[1750.88 --> 1752.10]  and say GPUs equals,
[1752.30 --> 1752.56]  you know,
[1752.60 --> 1753.06]  128
[1753.06 --> 1754.24]  and then off you go.
[1754.96 --> 1755.36]  So,
[1755.44 --> 1756.64]  it sounds like that
[1756.64 --> 1758.50]  if I'm a PyTorch developer
[1758.50 --> 1760.60]  and I'm already using
[1760.60 --> 1761.42]  that API,
[1761.86 --> 1763.42]  I'm creating the layers
[1763.42 --> 1764.36]  of my model,
[1764.52 --> 1765.74]  I don't have to like
[1765.74 --> 1767.22]  throw out the way
[1767.22 --> 1767.88]  that I,
[1768.08 --> 1769.72]  the way that I created
[1769.72 --> 1770.40]  that model.
[1770.62 --> 1771.48]  In some ways,
[1771.48 --> 1773.34]  I get to sort of delete
[1773.34 --> 1774.30]  a bunch of my code
[1774.30 --> 1775.54]  having to do with like
[1775.54 --> 1776.00]  the,
[1776.40 --> 1776.74]  you know,
[1776.88 --> 1778.00]  hardware stuff
[1778.00 --> 1779.60]  and some of the other
[1779.60 --> 1780.98]  training related things
[1780.98 --> 1782.14]  and I can keep my model
[1782.14 --> 1783.30]  and sort of refactor it
[1783.30 --> 1785.48]  into this PyTorch module,
[1786.12 --> 1787.02]  the Lightning module
[1787.02 --> 1788.36]  and then call the trainer
[1788.36 --> 1789.80]  and essentially then
[1789.80 --> 1791.64]  I now have less code
[1791.64 --> 1793.42]  but my code is also
[1793.42 --> 1794.08]  more,
[1794.08 --> 1795.26]  more robust
[1795.26 --> 1796.38]  in that I can run
[1796.38 --> 1796.90]  that training
[1796.90 --> 1797.84]  on a whole variety
[1797.84 --> 1798.44]  of hardware
[1798.44 --> 1799.62]  and that sort of thing.
[1799.68 --> 1800.26]  Am I basically
[1800.26 --> 1801.58]  summarizing that correct
[1801.58 --> 1802.48]  or anything you would,
[1802.58 --> 1803.70]  you would change about that?
[1803.78 --> 1804.56]  And it's more readable,
[1804.56 --> 1804.90]  right?
[1804.96 --> 1805.94]  You can literally give it
[1805.94 --> 1806.56]  to your colleagues
[1806.56 --> 1807.40]  and then they know
[1807.40 --> 1808.20]  to go to training step
[1808.20 --> 1808.96]  to see what's happening.
[1809.22 --> 1809.50]  Otherwise,
[1809.74 --> 1810.44]  what do you do today?
[1810.50 --> 1810.84]  You're like,
[1810.96 --> 1811.12]  hey,
[1811.16 --> 1811.84]  here's this like
[1811.84 --> 1813.04]  seven lines on GitHub.
[1813.34 --> 1813.86]  That's crazy.
[1814.12 --> 1814.30]  You know,
[1814.34 --> 1814.92]  you can actually,
[1815.28 --> 1815.60]  they're like,
[1815.66 --> 1815.76]  wait,
[1815.84 --> 1816.02]  where,
[1816.14 --> 1817.08]  where is it what you're doing?
[1817.08 --> 1817.84]  Because most of it,
[1817.94 --> 1819.16]  it's like boilerplate
[1819.16 --> 1820.04]  training stuff,
[1820.08 --> 1820.24]  right?
[1820.84 --> 1821.66]  Now you can be like,
[1821.72 --> 1821.84]  hey,
[1821.88 --> 1822.82]  here's exactly what I'm doing.
[1822.86 --> 1823.14]  They're like,
[1823.22 --> 1823.38]  oh,
[1823.40 --> 1824.86]  you're sampling the latent space
[1824.86 --> 1825.80]  before doing this thing.
[1825.92 --> 1826.04]  Oh,
[1826.12 --> 1826.48]  interesting,
[1826.78 --> 1826.94]  right?
[1826.96 --> 1828.02]  It's not mingled
[1828.02 --> 1828.88]  with all this other stuff.
[1828.94 --> 1829.66]  So it's very easy
[1829.66 --> 1830.72]  to read as well.
[1831.16 --> 1831.40]  You know,
[1831.44 --> 1831.78]  I joke,
[1831.84 --> 1832.70]  but it is kind of like
[1832.70 --> 1833.20]  cleaning,
[1833.78 --> 1833.98]  yeah,
[1834.02 --> 1834.90]  like cleaning your house,
[1834.92 --> 1835.20]  I guess.
[1835.40 --> 1836.12]  Like imagine,
[1836.40 --> 1837.04]  I guess roses,
[1837.20 --> 1837.36]  right?
[1837.36 --> 1838.42]  So maybe this is a good example.
[1838.52 --> 1839.06]  So a rose,
[1839.48 --> 1840.52]  you have to cut it from a bush
[1840.52 --> 1841.36]  and trim all the stuff
[1841.36 --> 1841.72]  and then,
[1841.78 --> 1841.96]  you know,
[1842.00 --> 1843.08]  you get this like bulb
[1843.08 --> 1843.58]  at the end,
[1843.58 --> 1844.58]  which is what you care about.
[1844.92 --> 1845.76]  It feels like that.
[1845.82 --> 1846.18]  It's like,
[1846.30 --> 1847.92]  no one's adding these other leaves
[1847.92 --> 1848.62]  because they want to,
[1848.68 --> 1849.40]  it's because they have to,
[1849.46 --> 1849.62]  right?
[1849.68 --> 1851.50]  So when you refactor your code,
[1852.02 --> 1853.16]  it's the sense of like,
[1853.22 --> 1853.46]  okay,
[1853.50 --> 1854.72]  it's a lot cleaner now.
[1854.78 --> 1855.54]  Like I just removed
[1855.54 --> 1856.96]  a lot of unnecessary stuff
[1856.96 --> 1858.08]  and also stuff
[1858.08 --> 1859.14]  that you're likely to mess up,
[1859.18 --> 1859.30]  right?
[1859.30 --> 1860.48]  Like we test very,
[1860.62 --> 1861.10]  very thoroughly
[1861.10 --> 1862.08]  and we have thousands
[1862.08 --> 1863.24]  of people testing this stuff.
[1863.36 --> 1864.62]  So did we mess up
[1864.62 --> 1865.36]  the backward pass?
[1865.66 --> 1866.46]  Definitely not,
[1866.52 --> 1866.70]  right?
[1866.96 --> 1868.08]  Did you mess it up?
[1868.38 --> 1868.96]  Hopefully not.
[1873.58 --> 1886.14]  ChangeLog++
[1886.14 --> 1887.66]  is the best way
[1887.66 --> 1889.38]  for you to directly support
[1889.38 --> 1890.40]  practical AI.
[1890.94 --> 1891.68]  Join today
[1891.68 --> 1892.64]  and unlock access
[1892.64 --> 1893.84]  to a private feed
[1893.84 --> 1895.18]  that makes the ads disappear,
[1895.62 --> 1897.22]  gets you closer to the metal
[1897.22 --> 1898.46]  and help sustain
[1898.46 --> 1899.30]  our production
[1899.30 --> 1900.50]  of practical AI
[1900.50 --> 1901.34]  into the future.
[1902.14 --> 1903.12]  Simply follow
[1903.12 --> 1904.36]  the ChangeLog++
[1904.36 --> 1905.96]  link in your show notes
[1905.96 --> 1907.52]  or point your favorite
[1907.52 --> 1908.06]  web browser
[1908.06 --> 1909.36]  to ChangeLog.com
[1909.36 --> 1910.38]  slash plus plus.
[1910.70 --> 1911.54]  Once again,
[1911.72 --> 1913.20]  that's ChangeLog.com
[1913.20 --> 1914.58]  slash plus plus.
[1916.08 --> 1917.06]  ChangeLog++
[1917.06 --> 1918.34]  is better.
[1929.02 --> 1929.54]  Okay.
[1929.70 --> 1930.84]  I want to kind of circle
[1930.84 --> 1931.64]  all the way back
[1931.64 --> 1932.74]  to where our conversation
[1932.74 --> 1933.56]  started because
[1933.56 --> 1934.48]  I want to get back
[1934.48 --> 1935.48]  to that cool demo
[1935.48 --> 1937.04]  that I saw on Twitter
[1937.04 --> 1938.20]  about Grid AI.
[1938.82 --> 1939.70]  So maybe you could
[1939.70 --> 1940.26]  just give us
[1940.26 --> 1941.30]  a little bit of sense
[1941.30 --> 1943.60]  of what Grid AI is,
[1943.72 --> 1944.84]  kind of how it came about,
[1945.26 --> 1946.32]  how it's maybe connected
[1946.32 --> 1948.32]  to the Lightning community,
[1948.32 --> 1949.24]  if at all,
[1949.60 --> 1950.30]  and then we can get
[1950.30 --> 1951.30]  into some of the details
[1951.30 --> 1952.36]  about what it enables.
[1953.02 --> 1953.80]  So, I mean,
[1953.88 --> 1954.84]  as you saw from my story,
[1954.92 --> 1955.64]  like I care a lot
[1955.64 --> 1956.56]  about reproducibility
[1956.56 --> 1957.64]  and speed of iteration
[1957.64 --> 1959.58]  and something
[1959.58 --> 1961.20]  that I thought
[1961.20 --> 1961.78]  a lot about
[1961.78 --> 1962.86]  as we were doing research
[1962.86 --> 1963.42]  and, you know,
[1963.46 --> 1964.00]  building Lightning
[1964.00 --> 1965.86]  was in a corporate setting,
[1966.20 --> 1967.10]  you would want
[1967.10 --> 1968.22]  to scale this stuff up
[1968.22 --> 1969.94]  on a lot of compute
[1969.94 --> 1971.08]  and you have cloud resources
[1971.08 --> 1971.94]  and all these different things.
[1972.06 --> 1973.12]  So the requirements
[1973.12 --> 1974.36]  for training at scale
[1974.36 --> 1975.18]  in a company
[1975.18 --> 1975.92]  are very different,
[1976.04 --> 1976.28]  right,
[1976.34 --> 1976.88]  than just like
[1976.88 --> 1978.08]  on a Google Colab
[1978.08 --> 1978.62]  or a Kaggle.
[1978.76 --> 1979.18]  It's just like
[1979.18 --> 1980.04]  a very different world,
[1980.12 --> 1980.30]  right?
[1980.38 --> 1981.42]  So, you know,
[1981.50 --> 1982.28]  it's funny because,
[1982.48 --> 1982.82]  you know,
[1982.94 --> 1984.48]  deployment also goes into that.
[1984.56 --> 1984.96]  People are like,
[1984.96 --> 1985.62]  oh, here you go.
[1985.70 --> 1986.74]  He deployed on this thing.
[1986.80 --> 1987.06]  It's like,
[1987.10 --> 1987.66]  well, yeah,
[1987.72 --> 1988.62]  but like most APIs,
[1988.86 --> 1990.60]  most real machine learning systems
[1990.60 --> 1991.44]  are not just an API,
[1991.58 --> 1991.74]  right?
[1992.86 --> 1994.18]  So we know that,
[1994.26 --> 1994.46]  I mean,
[1994.46 --> 1995.68]  a lot of us build these models.
[1995.86 --> 1996.52]  We've all been at companies
[1996.52 --> 1997.70]  before as well at scale.
[1997.82 --> 1998.46]  So we know exactly
[1998.46 --> 1999.20]  the pain points there.
[1999.72 --> 2000.96]  So the thing
[2000.96 --> 2001.62]  that kept coming up
[2001.62 --> 2001.92]  is like,
[2001.98 --> 2002.10]  cool,
[2002.22 --> 2002.94]  Lightning is letting me
[2002.94 --> 2003.40]  do all this,
[2003.52 --> 2004.66]  but how do I,
[2004.98 --> 2005.14]  you know,
[2005.16 --> 2006.10]  I'm still having to
[2006.10 --> 2007.98]  do all of this cloud stuff.
[2008.10 --> 2008.50]  Like why,
[2008.74 --> 2009.02]  you know,
[2009.04 --> 2010.60]  if I asked for 32 GPUs
[2010.60 --> 2011.00]  on Lightning,
[2011.66 --> 2011.88]  yeah,
[2011.94 --> 2012.82]  Lightning will do the thing,
[2012.88 --> 2013.20]  but like,
[2013.26 --> 2013.92]  you need to give me
[2013.92 --> 2014.90]  the 32 GPUs.
[2014.96 --> 2015.58]  And giving you
[2015.58 --> 2016.54]  the 32 GPUs,
[2016.60 --> 2017.48]  that's a lot of work
[2017.48 --> 2018.62]  to do it consistently
[2018.62 --> 2019.42]  and at scale
[2019.42 --> 2020.22]  and cheaply
[2020.22 --> 2020.82]  so that you don't have
[2020.82 --> 2021.54]  to burn resources,
[2021.66 --> 2021.84]  right?
[2022.30 --> 2023.38]  So what people end up
[2023.38 --> 2024.16]  doing generally
[2024.16 --> 2024.86]  is they build these
[2024.86 --> 2025.68]  like ad hoc
[2025.68 --> 2026.90]  internal solutions.
[2027.08 --> 2027.66]  They're like,
[2027.76 --> 2028.00]  you know,
[2028.00 --> 2028.94]  kind of put together
[2028.94 --> 2029.78]  bash scripts
[2029.78 --> 2030.74]  or things that like
[2030.74 --> 2031.80]  they string together
[2031.80 --> 2032.80]  like assemblings
[2032.80 --> 2033.50]  of a platform
[2033.50 --> 2034.36]  and they're great.
[2034.46 --> 2034.68]  And like,
[2034.72 --> 2034.86]  yeah,
[2034.90 --> 2035.90]  you will get things running,
[2036.00 --> 2037.50]  but like you won't
[2037.50 --> 2038.48]  be able to just,
[2038.68 --> 2039.02]  you know,
[2039.10 --> 2040.40]  scale them down immediately.
[2040.40 --> 2041.02]  You won't be able
[2041.02 --> 2041.92]  to have really fast
[2041.92 --> 2042.36]  build times
[2042.36 --> 2043.44]  because they're highly optimized.
[2043.70 --> 2044.20]  You want to have
[2044.20 --> 2045.20]  real-time logs.
[2045.32 --> 2045.70]  You want to have
[2045.70 --> 2046.38]  real-time metrics.
[2046.52 --> 2046.92]  You want to have
[2046.92 --> 2047.72]  time integrations,
[2047.82 --> 2047.98]  right?
[2048.02 --> 2048.96]  So all of these
[2048.96 --> 2049.56]  bells and whistles,
[2049.82 --> 2050.42]  when these things
[2050.42 --> 2051.12]  happen internally,
[2051.60 --> 2052.74]  they usually get pushed away
[2052.74 --> 2053.46]  because they're not
[2053.46 --> 2054.12]  a company priority
[2054.12 --> 2054.86]  because they shouldn't be.
[2054.96 --> 2055.12]  Like,
[2055.24 --> 2055.54]  you know,
[2055.62 --> 2056.54]  you're building airplanes,
[2056.66 --> 2057.26]  you're not building
[2057.26 --> 2058.18]  machine learning platforms,
[2058.26 --> 2058.46]  right?
[2058.46 --> 2060.42]  So you're normally
[2060.42 --> 2061.48]  not going to put the effort
[2061.48 --> 2062.10]  into making
[2062.10 --> 2063.08]  all the things
[2063.08 --> 2064.00]  that we care about
[2064.00 --> 2064.50]  as,
[2064.58 --> 2065.08]  you know,
[2065.14 --> 2065.60]  researchers
[2065.60 --> 2066.66]  and data scientists
[2066.66 --> 2067.20]  and machine learning
[2067.20 --> 2068.40]  engineers in there.
[2068.46 --> 2068.96]  So it's just going to
[2068.96 --> 2069.58]  make your life
[2069.58 --> 2070.08]  a lot harder.
[2070.26 --> 2071.02]  So it's about
[2071.02 --> 2071.72]  how do we bring
[2071.72 --> 2072.46]  that whole experience
[2072.46 --> 2072.94]  and encompass
[2072.94 --> 2073.90]  that model development
[2073.90 --> 2074.66]  cycle
[2074.66 --> 2076.20]  in a scalable way
[2076.20 --> 2077.12]  for the needs
[2077.12 --> 2077.98]  of like companies
[2077.98 --> 2078.88]  and even big labs,
[2078.92 --> 2079.08]  right?
[2079.08 --> 2079.76]  Because like most
[2079.76 --> 2080.72]  serious AI labs,
[2080.84 --> 2081.58]  they're training things
[2081.58 --> 2082.20]  on very,
[2082.32 --> 2083.36]  very large scales as well.
[2083.74 --> 2084.44]  Because training
[2084.44 --> 2085.16]  is a big part
[2085.16 --> 2085.62]  of the picture.
[2085.76 --> 2086.62]  It's not just a deployment.
[2086.62 --> 2087.44]  I think the deployment
[2087.44 --> 2088.46]  is interesting,
[2088.62 --> 2089.60]  but it's a lot easier
[2089.60 --> 2090.18]  because we've been
[2090.18 --> 2091.04]  deploying websites
[2091.04 --> 2091.84]  and things forever,
[2091.96 --> 2092.14]  right?
[2092.16 --> 2093.26]  But we haven't been
[2093.26 --> 2094.66]  training for that long.
[2094.72 --> 2095.66]  It's kind of a newer thing.
[2096.00 --> 2096.56]  So that's really
[2096.56 --> 2097.40]  the focus of Greatest
[2097.40 --> 2098.34]  to just completely
[2098.34 --> 2100.00]  eliminate the pain point
[2100.00 --> 2100.70]  that was left
[2100.70 --> 2101.66]  from using Lightning
[2101.66 --> 2102.96]  by not even having
[2102.96 --> 2103.58]  to deal with it.
[2103.60 --> 2105.22]  You just type in 32 GPUs
[2105.22 --> 2105.88]  and it just happens,
[2105.98 --> 2106.16]  right?
[2107.04 --> 2108.64]  So I'm wondering,
[2108.98 --> 2110.06]  there's still a lot
[2110.06 --> 2110.58]  of people,
[2110.70 --> 2111.16]  I think,
[2111.38 --> 2112.36]  and maybe I have
[2112.36 --> 2113.70]  a misconception about this,
[2113.76 --> 2114.30]  that they think
[2114.30 --> 2114.88]  like maybe
[2114.88 --> 2116.04]  training
[2116.04 --> 2117.02]  models
[2117.02 --> 2117.98]  on GPUs
[2117.98 --> 2118.62]  in the cloud
[2118.62 --> 2119.52]  is always going
[2119.52 --> 2120.52]  to be more expensive
[2120.52 --> 2121.60]  than training
[2121.60 --> 2122.92]  on a sort of like,
[2123.18 --> 2123.84]  you're going to buy
[2123.84 --> 2125.54]  an on-prem server
[2125.54 --> 2127.38]  and do it in-house.
[2127.62 --> 2128.74]  Based on sort of
[2128.74 --> 2129.44]  your experience
[2129.44 --> 2129.96]  with that
[2129.96 --> 2131.02]  and like the current
[2131.02 --> 2131.90]  sort of state
[2131.90 --> 2132.94]  of cloud providers
[2132.94 --> 2133.64]  and all of that,
[2134.06 --> 2135.16]  is that perception
[2135.16 --> 2136.08]  mostly driven
[2136.08 --> 2137.42]  by the fact that,
[2137.96 --> 2138.22]  you know,
[2138.30 --> 2139.42]  and I feel very seen
[2139.42 --> 2140.12]  by the comment
[2140.12 --> 2140.82]  about like,
[2140.90 --> 2141.74]  you have all these
[2141.74 --> 2142.64]  bash scripts
[2142.64 --> 2143.62]  strung together,
[2143.76 --> 2144.86]  that's like my life,
[2144.86 --> 2145.44]  maybe.
[2146.28 --> 2147.48]  But is it because
[2147.48 --> 2148.64]  like that way
[2148.64 --> 2149.94]  of doing things
[2149.94 --> 2151.74]  is a bit
[2151.74 --> 2152.64]  inefficient
[2152.64 --> 2153.62]  and you waste
[2153.62 --> 2154.84]  a lot of resources
[2154.84 --> 2156.68]  and that sort of thing
[2156.68 --> 2157.74]  or where do you think
[2157.74 --> 2158.26]  that perception
[2158.26 --> 2158.88]  is coming from
[2158.88 --> 2159.38]  and do you think
[2159.38 --> 2159.88]  it's accurate,
[2159.96 --> 2160.22]  I guess,
[2160.30 --> 2161.12]  is my question.
[2161.40 --> 2161.64]  I think,
[2161.72 --> 2161.82]  yeah,
[2161.84 --> 2162.46]  I think you hit it
[2162.46 --> 2163.00]  right on the nail.
[2163.10 --> 2164.32]  Like if your system
[2164.32 --> 2164.84]  is inefficient,
[2164.84 --> 2166.22]  then it's more efficient
[2166.22 --> 2167.26]  to have your own machines,
[2167.40 --> 2167.56]  right?
[2167.60 --> 2169.44]  Because like running
[2169.44 --> 2170.14]  on grid means
[2170.14 --> 2171.34]  that we install
[2171.34 --> 2171.98]  your dependencies,
[2172.38 --> 2173.00]  everything you do,
[2173.06 --> 2173.74]  link up your data
[2173.74 --> 2174.66]  in a matter of minutes,
[2174.70 --> 2175.44]  if not seconds,
[2175.54 --> 2175.70]  right?
[2176.16 --> 2177.02]  People don't generally
[2177.02 --> 2178.16]  optimize their stuff
[2178.16 --> 2178.74]  in the backend
[2178.74 --> 2179.26]  to do that.
[2179.34 --> 2180.10]  So what they end up doing
[2180.10 --> 2180.80]  is they want to run
[2180.80 --> 2181.54]  on the local machines
[2181.54 --> 2182.28]  because they don't have
[2182.28 --> 2183.16]  to install their environments
[2183.16 --> 2183.70]  and have to do
[2183.70 --> 2184.50]  all this stuff again,
[2184.54 --> 2184.70]  right?
[2184.96 --> 2185.52]  It's just there
[2185.52 --> 2186.20]  and it's repeatable
[2186.20 --> 2187.06]  and things start immediately.
[2187.20 --> 2187.82]  So it's a lot cheaper.
[2188.22 --> 2189.00]  I'm not going to say
[2189.00 --> 2189.74]  that running
[2189.74 --> 2190.54]  on your local stuff
[2190.54 --> 2191.80]  is not generally cheaper
[2191.80 --> 2192.38]  if you're doing things
[2192.38 --> 2193.18]  24-7,
[2193.38 --> 2194.58]  but you're limited
[2194.58 --> 2196.24]  by bursting capabilities,
[2196.48 --> 2196.68]  right?
[2196.76 --> 2197.92]  So you're never going
[2197.92 --> 2198.48]  to have,
[2198.58 --> 2198.94]  you know,
[2199.14 --> 2199.82]  I don't know how many
[2199.82 --> 2200.96]  GPUs AWS has,
[2201.08 --> 2201.60]  but it's got to be
[2201.60 --> 2202.32]  hundreds of thousands,
[2202.32 --> 2202.62]  right?
[2203.08 --> 2203.94]  So if you have to
[2203.94 --> 2204.54]  hit a deadline
[2204.54 --> 2205.62]  or do something
[2205.62 --> 2206.20]  really quick
[2206.20 --> 2207.16]  and even go through
[2207.16 --> 2207.96]  ideas fast,
[2208.38 --> 2208.88]  if you're buying
[2208.88 --> 2209.84]  your own GPUs,
[2210.32 --> 2210.86]  you're going to be
[2210.86 --> 2211.64]  limited by how many
[2211.64 --> 2212.22]  you have there,
[2212.32 --> 2212.54]  right?
[2212.98 --> 2214.54]  So it's going to be
[2214.54 --> 2215.62]  more like sequential
[2215.62 --> 2216.80]  model building
[2216.80 --> 2217.56]  as opposed to
[2217.56 --> 2218.52]  asynchronous building.
[2218.68 --> 2219.24]  So with Grid,
[2219.64 --> 2220.54]  you can go spin up
[2220.54 --> 2221.46]  200 GPUs,
[2221.72 --> 2222.44]  run for five minutes
[2222.44 --> 2223.26]  and shut them down
[2223.26 --> 2223.94]  and you just got
[2223.94 --> 2224.62]  a lot done,
[2224.74 --> 2224.98]  right?
[2225.34 --> 2226.30]  Whereas on your own
[2226.30 --> 2226.76]  machines,
[2227.16 --> 2227.74]  even if you were
[2227.74 --> 2228.24]  to do it yourself
[2228.24 --> 2228.84]  on the cloud,
[2229.28 --> 2229.94]  you would probably
[2229.94 --> 2230.64]  not even get the
[2230.64 --> 2231.52]  models running for,
[2231.58 --> 2231.86]  you know,
[2231.86 --> 2232.88]  20 minutes and 30
[2232.88 --> 2233.56]  while you spin up
[2233.56 --> 2234.00]  the machine,
[2234.16 --> 2234.94]  set up all that
[2234.94 --> 2235.18]  stuff,
[2235.22 --> 2235.38]  right?
[2235.62 --> 2236.86]  So I can take
[2236.86 --> 2237.88]  $100 on Grid
[2237.88 --> 2239.32]  and get more GPU
[2239.32 --> 2240.50]  minutes out of it
[2240.50 --> 2241.68]  than you would
[2241.68 --> 2242.52]  normally with
[2242.52 --> 2243.24]  without optimal
[2243.24 --> 2243.70]  systems,
[2243.80 --> 2243.98]  right?
[2244.08 --> 2244.76]  So it's just
[2244.76 --> 2245.02]  very,
[2245.12 --> 2245.58]  very optimized.
[2246.20 --> 2246.38]  Now,
[2246.48 --> 2247.24]  I do think that
[2247.24 --> 2247.70]  people need to
[2247.70 --> 2248.48]  know about things.
[2248.62 --> 2248.78]  I mean,
[2248.78 --> 2249.32]  we do a lot
[2249.32 --> 2250.26]  to lower the cost,
[2250.34 --> 2250.50]  right?
[2250.50 --> 2250.96]  And I think one
[2250.96 --> 2251.36]  of those things
[2251.36 --> 2252.20]  is spot instances,
[2252.44 --> 2252.60]  right?
[2252.70 --> 2254.00]  So spot instances
[2254.00 --> 2255.16]  are machines
[2255.16 --> 2256.80]  that can be
[2256.80 --> 2257.78]  killed at any
[2257.78 --> 2258.92]  time by AWS,
[2259.20 --> 2259.38]  right?
[2259.38 --> 2260.08]  Or whatever cloud
[2260.08 --> 2260.74]  provider you're using.
[2261.46 --> 2262.26]  And then at that point,
[2262.32 --> 2262.88]  you're kind of done,
[2262.94 --> 2263.10]  right?
[2263.20 --> 2263.56]  And so,
[2263.96 --> 2264.84]  but the nice thing
[2264.84 --> 2265.90]  about spot is that
[2265.90 --> 2266.94]  it will be like,
[2267.46 --> 2267.84]  I don't know,
[2267.90 --> 2269.48]  50 to 80%
[2269.48 --> 2270.32]  the discount,
[2270.50 --> 2270.66]  right?
[2270.66 --> 2271.70]  So if a GPU costs
[2271.70 --> 2273.54]  $3 an hour,
[2273.68 --> 2274.44]  it could be like
[2274.44 --> 2275.34]  30 cents an hour
[2275.34 --> 2276.48]  to maybe a dollar
[2276.48 --> 2276.86]  an hour,
[2276.94 --> 2277.12]  right?
[2277.12 --> 2277.76]  So it really depends.
[2277.76 --> 2278.68]  And so I think
[2278.68 --> 2279.28]  what you're saying
[2279.28 --> 2279.74]  is true because
[2279.74 --> 2280.46]  I did the calculus
[2280.46 --> 2280.88]  myself.
[2281.06 --> 2281.32]  And I,
[2281.48 --> 2281.66]  in fact,
[2281.70 --> 2282.52]  I have like blog posts
[2282.52 --> 2282.96]  on how to build
[2282.96 --> 2283.56]  your own GPUs
[2283.56 --> 2284.04]  for this reason,
[2284.54 --> 2285.62]  but that was only
[2285.62 --> 2287.42]  for 10 to 80 TIs,
[2287.62 --> 2287.84]  right?
[2288.30 --> 2289.72]  And it cost me
[2289.72 --> 2290.66]  maybe six grand
[2290.66 --> 2291.38]  to build that machine,
[2291.48 --> 2291.94]  which is great.
[2292.50 --> 2292.86]  Now,
[2292.98 --> 2293.56]  $6,000,
[2294.00 --> 2294.56]  if I'm paying
[2294.56 --> 2295.84]  full GPU prices,
[2295.84 --> 2296.54]  I'll burn through
[2296.54 --> 2297.28]  that in like two weeks
[2297.28 --> 2297.66]  for sure,
[2297.82 --> 2298.00]  right?
[2298.28 --> 2298.90]  But if I'm paying
[2298.90 --> 2299.80]  spot prices,
[2300.42 --> 2301.20]  then that's gonna,
[2301.32 --> 2302.14]  that changes the game.
[2302.42 --> 2303.42]  And then not only that,
[2303.46 --> 2304.02]  but if I'm getting
[2304.02 --> 2305.18]  more training minutes
[2305.18 --> 2305.88]  out of that,
[2306.00 --> 2306.80]  that's a lot better.
[2306.80 --> 2307.50]  And then you factor
[2307.50 --> 2308.24]  in the appreciation
[2308.24 --> 2309.06]  and this other stuff
[2309.06 --> 2310.16]  plus maintenance,
[2310.16 --> 2311.18]  then it actually
[2311.18 --> 2311.96]  becomes a little bit
[2311.96 --> 2312.36]  competitive,
[2312.56 --> 2312.74]  right?
[2313.06 --> 2313.32]  It does.
[2313.78 --> 2314.32]  I'm curious,
[2314.52 --> 2314.70]  you know,
[2314.72 --> 2315.44]  and we're talking
[2315.44 --> 2316.26]  a lot about the training.
[2316.62 --> 2317.50]  Could you talk a little bit
[2317.50 --> 2318.46]  about Grid AI's
[2318.46 --> 2319.46]  deployment story
[2319.46 --> 2320.28]  and what that is?
[2320.42 --> 2321.70]  And in my mind,
[2321.76 --> 2322.22]  one of the things
[2322.22 --> 2323.40]  like speaking for myself,
[2323.64 --> 2324.80]  I'll be training centrally
[2324.80 --> 2325.76]  in the cloud and stuff,
[2325.82 --> 2326.54]  but at the end of the day,
[2326.54 --> 2328.06]  I gotta get my model
[2328.06 --> 2329.32]  or my system of models
[2329.32 --> 2331.10]  out there into something,
[2331.16 --> 2332.50]  often some sort of edge device,
[2332.88 --> 2334.08]  not cloud-based,
[2334.30 --> 2334.64]  you know,
[2334.70 --> 2336.12]  something that's a physical thing
[2336.12 --> 2336.88]  out in the real world.
[2337.28 --> 2338.12]  Can you talk about
[2338.12 --> 2339.74]  how you work with Grid AI
[2339.74 --> 2340.52]  to affect that?
[2341.16 --> 2341.26]  Yeah,
[2341.32 --> 2342.14]  so today Grid doesn't
[2342.14 --> 2342.96]  support deployments,
[2343.00 --> 2343.18]  right?
[2343.42 --> 2344.44]  So the thing that
[2344.44 --> 2345.66]  we like to focus on
[2345.66 --> 2346.30]  is making sure
[2346.30 --> 2347.60]  that we really nail
[2347.60 --> 2348.34]  certain experiences
[2348.34 --> 2349.10]  before moving on
[2349.10 --> 2349.62]  to other things,
[2349.66 --> 2349.82]  right?
[2349.82 --> 2350.54]  So we will support
[2350.54 --> 2351.70]  deployment at some point,
[2352.02 --> 2352.82]  probably very soon,
[2352.90 --> 2353.10]  right?
[2353.18 --> 2354.34]  But the thing is like,
[2354.34 --> 2355.24]  I don't think that we're
[2355.24 --> 2356.56]  fully, fully optimal
[2356.56 --> 2357.56]  on the training side yet.
[2357.72 --> 2358.42]  Like I think we want
[2358.42 --> 2359.06]  to provide a really
[2359.06 --> 2360.18]  world-class experience there.
[2360.62 --> 2361.88]  So for our users today,
[2362.00 --> 2362.24]  like,
[2362.72 --> 2363.00]  you know,
[2363.00 --> 2364.30]  you can access artifacts,
[2364.56 --> 2365.66]  you can get model checkpoints
[2365.66 --> 2366.24]  and all that stuff.
[2366.32 --> 2367.00]  So the deployment,
[2367.60 --> 2368.90]  most users have a deployment
[2368.90 --> 2369.84]  system and has already,
[2370.00 --> 2370.70]  so they can just
[2370.70 --> 2371.26]  take artifacts
[2371.26 --> 2372.00]  and do their thing,
[2372.06 --> 2372.20]  right?
[2372.20 --> 2372.90]  So we're not blocking
[2372.90 --> 2373.44]  any of that.
[2373.90 --> 2374.62]  And all of these things
[2374.62 --> 2375.60]  are like URL-based.
[2375.78 --> 2376.42]  And if it's lightning,
[2376.64 --> 2376.76]  like,
[2376.82 --> 2377.00]  I mean,
[2377.00 --> 2377.92]  that's very easy to do.
[2378.34 --> 2379.12]  Now we're going to make it
[2379.12 --> 2380.20]  a lot easier for sure,
[2380.34 --> 2380.50]  like,
[2380.64 --> 2380.88]  you know,
[2380.96 --> 2381.56]  kind of the way
[2381.56 --> 2382.32]  that we do things.
[2382.58 --> 2383.48]  But today we are
[2383.48 --> 2384.64]  laser focused on training.
[2384.84 --> 2385.62]  But I will say,
[2385.70 --> 2386.72]  I think like working
[2386.72 --> 2387.84]  with Grid at this stage
[2387.84 --> 2388.62]  is great
[2388.62 --> 2389.90]  because I think companies
[2389.90 --> 2391.36]  were able to help us
[2391.36 --> 2392.38]  influence that roadmap,
[2392.64 --> 2392.86]  right?
[2392.88 --> 2393.78]  And help us build something
[2393.78 --> 2394.78]  that they really care about
[2394.78 --> 2395.20]  as well.
[2395.56 --> 2396.50]  Because as soon as we start
[2396.50 --> 2397.22]  getting into deployment,
[2397.42 --> 2397.70]  like,
[2397.82 --> 2398.58]  we're going to do it
[2398.58 --> 2399.16]  our way,
[2399.22 --> 2399.40]  right?
[2399.42 --> 2400.34]  And we have a very special
[2400.34 --> 2401.02]  way of doing things.
[2401.12 --> 2402.36]  So we hope that we have
[2402.36 --> 2403.50]  the feedback from the community
[2403.50 --> 2404.88]  and users to make sure
[2404.88 --> 2405.54]  that we're doing it
[2405.54 --> 2406.84]  in like a really useful way.
[2407.40 --> 2407.76]  And how,
[2408.14 --> 2409.36]  as a user of Grid AI,
[2409.50 --> 2410.44]  because this is really
[2410.44 --> 2411.36]  fascinating to me
[2411.36 --> 2412.30]  because I've even
[2412.30 --> 2413.48]  been struggling to
[2413.48 --> 2415.16]  get some in-house GPUs
[2415.16 --> 2416.60]  just with supply chain issues
[2416.60 --> 2417.60]  and all of those things.
[2417.64 --> 2418.72]  So running things on the cloud
[2418.72 --> 2420.02]  is something that we're
[2420.02 --> 2420.96]  actively, you know,
[2421.04 --> 2422.06]  thinking a lot about
[2422.06 --> 2422.72]  and doing it
[2422.72 --> 2423.92]  in an optimized way.
[2424.56 --> 2424.96]  Now,
[2425.40 --> 2426.52]  we kind of talked before
[2426.52 --> 2427.32]  about going, say,
[2427.40 --> 2428.06]  from PyTorch
[2428.06 --> 2428.94]  to PyTorch Lightning.
[2429.28 --> 2430.24]  Let's say I've got
[2430.24 --> 2431.78]  my Python code.
[2432.04 --> 2433.04]  I'm using Lightning.
[2433.48 --> 2434.36]  It works great.
[2434.46 --> 2435.56]  And now I want to run it
[2435.56 --> 2436.56]  with Grid AI
[2436.56 --> 2437.96]  on, you know,
[2438.10 --> 2439.24]  100 GPUs
[2439.24 --> 2440.06]  in the cloud.
[2440.54 --> 2441.52]  What does that look like?
[2441.60 --> 2442.32]  Do I need to set up
[2442.32 --> 2443.20]  my cloud account,
[2443.50 --> 2444.80]  set up billing on that side,
[2444.84 --> 2445.58]  and then set up
[2445.58 --> 2446.64]  my Grid account
[2446.64 --> 2447.54]  and then use
[2447.54 --> 2448.70]  a grid tool
[2448.70 --> 2450.22]  to connect them both?
[2450.30 --> 2451.20]  How does that whole
[2451.20 --> 2452.14]  flow work
[2452.14 --> 2452.82]  from that point?
[2454.02 --> 2454.94]  So I think,
[2455.04 --> 2455.70]  yeah, that's a good question.
[2455.96 --> 2457.06]  Okay, so generally,
[2457.36 --> 2458.38]  I like to think about
[2458.38 --> 2459.14]  what we're trying to do,
[2459.28 --> 2460.44]  like, you know,
[2460.48 --> 2461.34]  the leap between,
[2461.72 --> 2462.10]  I don't know,
[2462.16 --> 2463.40]  like Windows machines
[2463.40 --> 2464.92]  to Mac machines, right?
[2464.96 --> 2466.02]  Like where things just work, right?
[2466.04 --> 2467.92]  So what is that Apple experience
[2467.92 --> 2468.96]  for machine learning, right?
[2469.02 --> 2469.58]  And I think
[2469.58 --> 2470.82]  to answer your question,
[2471.44 --> 2473.48]  it's very, very easy.
[2473.58 --> 2474.38]  It's not as easy
[2474.38 --> 2475.30]  as I want it to be today,
[2475.30 --> 2476.02]  but it will be.
[2476.36 --> 2477.00]  So basically,
[2477.56 --> 2478.44]  there are a few ways, right?
[2478.44 --> 2480.52]  So we have three tiers
[2480.52 --> 2481.98]  of usage on Grid, right?
[2482.00 --> 2482.96]  We have the community tier,
[2483.02 --> 2483.58]  which is free.
[2483.76 --> 2484.02]  Literally,
[2484.20 --> 2485.00]  you're just paying
[2485.00 --> 2486.30]  the AWS compute, right?
[2486.30 --> 2487.08]  There's nothing in there.
[2487.22 --> 2487.76]  Like we're just
[2487.76 --> 2489.04]  orchestrating stuff for you,
[2489.10 --> 2490.40]  but it doesn't really work
[2490.40 --> 2490.88]  for teams
[2490.88 --> 2492.22]  and like big companies, right?
[2492.22 --> 2492.86]  Because there's a lot
[2492.86 --> 2493.68]  of stuff that needs to happen.
[2494.18 --> 2495.26]  So there we have the teams
[2495.26 --> 2496.04]  and enterprise tiers
[2496.04 --> 2496.50]  that let you do
[2496.50 --> 2497.14]  those kind of things.
[2497.58 --> 2498.48]  On the community tier,
[2498.80 --> 2500.00]  you literally have to do nothing.
[2500.18 --> 2501.16]  You just copy paste
[2501.16 --> 2502.56]  the link to a GitHub file,
[2502.88 --> 2503.94]  you paste it into the UI
[2503.94 --> 2505.22]  or use the CLI,
[2505.76 --> 2506.28]  and you select
[2506.28 --> 2507.38]  how many GPUs you want,
[2507.38 --> 2508.22]  and you press enter
[2508.22 --> 2509.50]  and you're done, right?
[2509.54 --> 2510.74]  Like it's that easy.
[2511.36 --> 2512.44]  Dependencies are automatically
[2512.44 --> 2513.56]  pulled for you.
[2513.74 --> 2514.32]  They're, you know,
[2514.38 --> 2515.16]  inference from the code
[2515.16 --> 2515.74]  that you have,
[2515.80 --> 2516.32]  your requirements,
[2516.52 --> 2517.08]  all that stuff.
[2517.48 --> 2518.40]  So we try to do
[2518.40 --> 2519.18]  as much as possible.
[2519.64 --> 2520.56]  Yes, there will be times
[2520.56 --> 2521.24]  when that fails
[2521.24 --> 2522.22]  and we will, you know,
[2522.22 --> 2522.76]  work with you
[2522.76 --> 2523.84]  to figure out what happened
[2523.84 --> 2524.68]  and, you know,
[2524.68 --> 2525.58]  make sure that we get it done.
[2526.00 --> 2526.36]  But, you know,
[2526.40 --> 2527.18]  dependency management
[2527.18 --> 2529.16]  is a big deal for everyone
[2529.16 --> 2529.86]  and it's a really hard
[2529.86 --> 2530.42]  problem to solve.
[2530.52 --> 2531.64]  So it's going to take us
[2531.64 --> 2532.52]  a while to fully solve
[2532.52 --> 2532.94]  that problem.
[2533.54 --> 2534.34]  But if you are
[2534.34 --> 2535.12]  at a company
[2535.12 --> 2535.90]  or at a big lab,
[2535.98 --> 2537.40]  like usually that's,
[2537.54 --> 2537.72]  you know,
[2537.72 --> 2538.68]  we call that community tier.
[2538.80 --> 2539.64]  That's going to work great
[2539.64 --> 2540.60]  for like side projects
[2540.60 --> 2541.44]  and public data
[2541.44 --> 2542.28]  and stuff like that.
[2542.40 --> 2543.12]  Kaggle, you know,
[2543.40 --> 2544.18]  prototyping things.
[2544.30 --> 2545.00]  Sure, if your data
[2545.00 --> 2545.74]  is not secret,
[2545.86 --> 2546.46]  then it's fine.
[2546.90 --> 2547.78]  So great for academics
[2547.78 --> 2548.22]  as well.
[2548.56 --> 2549.68]  But if you have corporate data,
[2549.68 --> 2550.48]  then you're going to be
[2550.48 --> 2550.88]  on the teams
[2550.88 --> 2551.92]  or enterprise tier, right?
[2552.02 --> 2553.44]  There, what you end up doing
[2553.44 --> 2555.00]  is we basically link up
[2555.00 --> 2556.34]  your cloud accounts, right?
[2556.38 --> 2557.24]  So you just set it up
[2557.24 --> 2557.66]  through Grid,
[2557.84 --> 2558.72]  you're passing credentials
[2558.72 --> 2559.26]  through there.
[2559.66 --> 2560.72]  And then those keys
[2560.72 --> 2562.12]  let us control resources
[2562.12 --> 2562.78]  on your behalf
[2562.78 --> 2563.80]  only as much
[2563.80 --> 2564.88]  as you allow us to, right?
[2565.28 --> 2566.10]  To make sure that
[2566.10 --> 2566.98]  we orchestrate everything
[2566.98 --> 2567.50]  in your cloud.
[2567.68 --> 2569.22]  So it's kind of this hybrid
[2569.22 --> 2570.76]  on-prem versus not on-prem.
[2570.90 --> 2571.70]  We also offer on-prem
[2571.70 --> 2572.36]  if people want it.
[2572.76 --> 2573.62]  So once you do that,
[2573.70 --> 2574.80]  you basically put in
[2574.80 --> 2575.88]  your cloud credentials
[2575.88 --> 2576.28]  in there,
[2576.76 --> 2577.56]  then you're good to go.
[2577.66 --> 2578.72]  When you run stuff on Grid,
[2579.06 --> 2579.72]  instead of running
[2579.72 --> 2580.42]  on the Grid cloud,
[2580.50 --> 2581.50]  which is a community cloud,
[2581.84 --> 2582.84]  you just select your cloud,
[2583.00 --> 2583.78]  whatever you named it,
[2583.84 --> 2585.22]  and then you just run on it, right?
[2585.28 --> 2586.48]  And that means you can link up
[2586.48 --> 2587.08]  as many of these
[2587.08 --> 2587.84]  as you want as well.
[2587.84 --> 2589.56]  As we kind of wind up here,
[2589.60 --> 2590.02]  one of the things
[2590.02 --> 2590.82]  that's really struck me
[2590.82 --> 2591.64]  through the conversation
[2591.64 --> 2593.36]  is that you are a man
[2593.36 --> 2594.52]  of substantial vision.
[2595.16 --> 2596.60]  And as we kind of wind up,
[2596.66 --> 2597.52]  I'm really curious
[2597.52 --> 2598.62]  if you would kind of
[2598.62 --> 2600.50]  look out a little bit beyond
[2600.50 --> 2601.38]  just, you know,
[2601.38 --> 2602.48]  the next product cycle
[2602.48 --> 2603.34]  and that kind of thing
[2603.34 --> 2605.16]  into where you want to go,
[2605.24 --> 2606.12]  both with Grid AI
[2606.12 --> 2607.10]  and where you see
[2607.10 --> 2608.66]  the larger industry
[2608.66 --> 2609.62]  going in general
[2609.62 --> 2610.78]  in terms of trying to
[2610.78 --> 2611.92]  make this work
[2611.92 --> 2612.62]  a little bit better
[2612.62 --> 2613.26]  for people
[2613.26 --> 2614.14]  and take the struggle
[2614.14 --> 2614.70]  out of it
[2614.70 --> 2615.78]  that you clearly
[2615.78 --> 2616.52]  have been working on
[2616.52 --> 2617.16]  for a while
[2617.16 --> 2618.18]  in various capacities.
[2618.66 --> 2619.30]  Could you tell us
[2619.30 --> 2619.94]  a little bit about
[2619.94 --> 2621.46]  what future you think
[2621.46 --> 2622.20]  we're going toward
[2622.20 --> 2623.54]  and what you would like
[2623.54 --> 2624.30]  to shape it
[2624.30 --> 2625.28]  and how you would like
[2625.28 --> 2625.76]  to shape it?
[2626.16 --> 2626.40]  You know,
[2626.44 --> 2627.60]  when I started in research,
[2627.60 --> 2629.12]  I was really disappointed
[2629.12 --> 2630.02]  that I had to do
[2630.02 --> 2630.96]  so much work
[2630.96 --> 2631.76]  over and over again
[2631.76 --> 2632.42]  that other people
[2632.42 --> 2632.84]  were doing
[2632.84 --> 2634.84]  and that I had to learn
[2634.84 --> 2635.96]  so much
[2635.96 --> 2636.82]  just to,
[2636.82 --> 2637.18]  you know,
[2637.26 --> 2638.26]  decode a little bit
[2638.26 --> 2638.98]  of neural activity,
[2639.20 --> 2639.38]  right?
[2639.38 --> 2642.10]  and the world
[2642.10 --> 2642.60]  that I would love
[2642.60 --> 2644.18]  to kind of help
[2644.18 --> 2645.54]  bring to the table
[2645.54 --> 2646.84]  is a world
[2646.84 --> 2648.02]  where the person,
[2648.34 --> 2648.84]  the scientist,
[2649.12 --> 2649.60]  the researcher,
[2649.72 --> 2650.32]  the machine learning engineer,
[2650.40 --> 2651.18]  the person that has
[2651.18 --> 2651.64]  the knowledge
[2651.64 --> 2652.54]  of whatever they're building,
[2652.64 --> 2652.76]  right?
[2652.80 --> 2653.28]  The doctor,
[2653.96 --> 2654.66]  the biologist,
[2655.02 --> 2656.34]  the mechanical engineer,
[2656.52 --> 2656.70]  you know,
[2656.74 --> 2657.10]  you name it.
[2657.10 --> 2657.88]  The person who really
[2657.88 --> 2658.84]  knows their domain
[2658.84 --> 2660.58]  can basically focus
[2660.58 --> 2661.12]  on that
[2661.12 --> 2662.32]  and not like
[2662.32 --> 2663.20]  have machine learning
[2663.20 --> 2664.84]  and all of this cloud stuff
[2664.84 --> 2665.58]  just kind of fade
[2665.58 --> 2666.18]  into the background,
[2666.36 --> 2666.52]  right?
[2666.52 --> 2668.42]  And just be like Wi-Fi,
[2668.56 --> 2670.08]  just like your cell phone signal,
[2670.16 --> 2671.06]  like you don't think about it,
[2671.08 --> 2671.22]  right?
[2671.22 --> 2671.80]  You're just working
[2671.80 --> 2672.38]  on your problem.
[2672.86 --> 2674.10]  So how do we take that leap?
[2674.12 --> 2674.62]  And I think that's
[2674.62 --> 2675.36]  what we're trying to solve.
[2675.46 --> 2676.06]  Are we there yet?
[2676.14 --> 2676.42]  No,
[2676.82 --> 2678.76]  but we're definitely on track.
[2678.94 --> 2679.16]  And,
[2679.36 --> 2679.54]  you know,
[2679.54 --> 2680.38]  I think that working
[2680.38 --> 2682.46]  with a lot of amazing companies
[2682.46 --> 2683.60]  and getting to make sure
[2683.60 --> 2684.92]  that we support their use cases
[2684.92 --> 2686.56]  is what's going to help us get there.
[2686.96 --> 2688.92]  So the person who builds the models,
[2689.02 --> 2690.00]  who has the ideas,
[2690.14 --> 2690.64]  that doctor,
[2691.00 --> 2691.88]  they can be the ones
[2691.88 --> 2692.46]  to actually,
[2692.60 --> 2692.98]  you know,
[2693.04 --> 2694.34]  train and deploy this stuff
[2694.34 --> 2694.64]  because,
[2694.92 --> 2695.40]  you know,
[2695.44 --> 2696.08]  at the end of the day,
[2696.08 --> 2696.94]  I think that deployment
[2696.94 --> 2698.36]  is literally just another
[2698.36 --> 2699.34]  training cycle.
[2699.44 --> 2700.44]  It's if the data's live
[2700.44 --> 2701.46]  and you're not backpropagating
[2701.46 --> 2702.04]  into your model,
[2702.18 --> 2702.34]  right?
[2702.84 --> 2703.40]  That's awesome.
[2703.72 --> 2704.48]  Thank you so much
[2704.48 --> 2705.46]  for talking to us
[2705.46 --> 2707.00]  about Grid AI and Lightning.
[2707.20 --> 2708.44]  It's been really wonderful.
[2708.70 --> 2709.38]  And like I say,
[2709.42 --> 2710.30]  we'll put show notes
[2710.30 --> 2710.90]  and everything,
[2711.48 --> 2712.28]  the relevant links
[2712.28 --> 2713.48]  that we've talked about
[2713.48 --> 2714.38]  in terms of Lightning
[2714.38 --> 2715.20]  and Grid AI.
[2715.36 --> 2716.36]  Definitely check it out.
[2716.94 --> 2717.28]  And yeah,
[2717.36 --> 2717.98]  thank you so much
[2717.98 --> 2718.80]  for joining us, William.
[2718.88 --> 2719.46]  It's been a pleasure.
[2720.00 --> 2720.10]  Well,
[2720.14 --> 2720.62]  thank you guys.
[2720.70 --> 2721.86]  This is a really fun conversation.
[2722.00 --> 2722.24]  Thank you.
[2722.24 --> 2726.66]  Thank you for listening
[2726.66 --> 2727.60]  to Practical AI.
[2727.92 --> 2729.14]  We appreciate your time
[2729.14 --> 2729.92]  and your attention.
[2730.40 --> 2731.72]  If you enjoyed this episode,
[2731.88 --> 2732.80]  help us out
[2732.80 --> 2734.00]  by spreading the word.
[2734.54 --> 2735.32]  Think of a friend,
[2735.52 --> 2736.20]  think of a colleague,
[2736.50 --> 2737.38]  somebody who would benefit
[2737.38 --> 2738.30]  from listening to it
[2738.30 --> 2739.30]  and send them a link.
[2739.66 --> 2740.64]  We'd really appreciate it.
[2740.98 --> 2741.72]  Practical AI
[2741.72 --> 2743.14]  is hosted by Chris Benson
[2743.14 --> 2744.36]  and Daniel Whitenack.
[2744.58 --> 2745.96]  It's produced by Jared Santo
[2745.96 --> 2746.90]  with music
[2746.90 --> 2748.12]  by Breakmaster Cylinder.
[2748.52 --> 2749.60]  Thanks again to our sponsors,
[2749.82 --> 2750.24]  Fastly,
[2750.38 --> 2750.76]  Linode,
[2750.76 --> 2751.72]  and LaunchDarkly.
[2752.04 --> 2752.66]  That's our show.
[2753.12 --> 2754.08]  We hope you enjoyed it
[2754.08 --> 2755.20]  and we'll talk to you again
[2755.20 --> 2755.80]  next week.
[2755.80 --> 2756.80]  Bye.
[2756.80 --> 2757.42]  Bye.
[2757.42 --> 2757.46]  Bye.
[2757.46 --> 2757.60]  Bye.
[2757.60 --> 2757.66]  Bye.
[2757.66 --> 2757.70]  Bye.
[2757.70 --> 2757.78]  Bye.
[2757.78 --> 2757.88]  Bye.
[2757.88 --> 2757.94]  Bye.
[2757.94 --> 2758.02]  Bye.
[2758.02 --> 2758.08]  Bye.
[2758.08 --> 2758.14]  Bye.
[2758.14 --> 2758.32]  Bye.
[2758.32 --> 2758.58]  Bye.
[2758.58 --> 2758.60]  Bye.
[2758.60 --> 2758.90]  Bye.
[2758.90 --> 2758.92]  Bye.
[2758.92 --> 2759.04]  Bye.
[2781.46 --> 2807.46]  Bye.
[2809.54 --> 2810.06]  Bye.
[2810.08 --> 2810.16]  Bye.
[2810.18 --> 2810.54]  Bye.
