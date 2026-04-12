[0.00 --> 13.90]  What up nerds? I'm Jared and this is Changelog News for the week of Monday, November 24th,
[13.90 --> 22.12]  2025. Turns out Gen Z has a weaker top password choice than every older generation except the
[22.12 --> 28.78]  80 plus crowd. Don't get cocky, boomers, Gen Xers, and millennials. It's pretty rocky for us too.
[28.78 --> 37.54]  According to a new report, the most commonly leaked Gen Z password is 12345, while the most
[37.54 --> 46.48]  commonly leaked password for the other age groups is 123456. This proves that you can be a winner and
[46.48 --> 53.30]  a loser at the same time. Okay, let's get into this week's news. What is a tech bubble anyway?
[53.30 --> 55.10]  Cedric Chin says,
[55.10 --> 62.38]  Comparisons of our current AI maybe bubble to the dot-com bubble and the 2008 GFC are limiting.
[62.64 --> 62.94]  Quote,
[62.94 --> 69.74]  First, the 2008 crisis wasn't a technology bubble. Second, the dot-com bubble was idiosyncratic for a
[69.74 --> 75.14]  number of reasons. The biggest one being that going public has since become an order of magnitude more
[75.14 --> 81.20]  difficult. It shouldn't come as a surprise that the hottest AI companies today are all private companies.
[81.46 --> 87.22]  Unavailable to the retail investor, that's different enough from 1999 that it should, I think,
[87.22 --> 92.94]  give you pause. End quote. Cedric also believes that calling this a bubble or not doesn't really
[92.94 --> 99.60]  matter. What really matters is, what should I do? And that, of course, depends on who you are and what
[99.60 --> 105.10]  you are trying to accomplish. But leaving the subjective aside, I'm linking up Cedric's post
[105.10 --> 111.08]  because he provides five bullet points that lay out a pattern that we can use to see what might come
[111.08 --> 117.54]  next. Unfortunately, each bullet point is too long to read here and not long enough to summarize in a
[117.54 --> 123.10]  useful way. So I'm not going to save you a click on this one. Find that link in the newsletter.
[123.60 --> 130.66]  The Cloudflare outage unwrapped. File this one under stories you most likely already know all about,
[130.92 --> 137.28]  but I'm telling you about anyways. Cloudflare CEO Matthew Prince posted an excellently transparent
[137.28 --> 142.62]  post-mortem of their significant failures to deliver core network traffic last week,
[142.76 --> 148.26]  which brought much of the internet to its knees and took our AI agents with it. The details are
[148.26 --> 154.36]  fascinating. Murphy's Law was in full effect that day. Quote, throwing us off and making us believe
[154.36 --> 160.86]  this might have been an attack was another apparent symptom we observed. Cloudflare's status page went
[160.86 --> 166.54]  down. The status page is hosted completely off Cloudflare's infrastructure with no dependencies on
[166.54 --> 172.04]  Cloudflare. While it turned out to be a coincidence, it led some of the team diagnosing the issue to
[172.04 --> 177.92]  believe that an attacker might be targeting both of our systems as well as our status page. End quote.
[178.22 --> 183.80]  The smoking gun at the end of this murder mystery was a single line of rust code which executes a single
[183.80 --> 190.22]  method, unwrap. It just so happens that unwrap, which assumes an operation succeeded and extracts data
[190.22 --> 197.14]  from its inner value is considered by many rustations to be one of the language's few foot guns. Cloudflare
[197.14 --> 201.42]  engineering shot themselves with it and the internet felt the pain.
[201.84 --> 209.84]  A high-performance log viewer for humans. HL is a fast, powerful log viewer slash processor that converts
[209.84 --> 218.00]  JSON and log fumped logs into a clear, human-readable format before we do our own parsing and analysis.
[218.00 --> 224.36]  It has paging built in, can handle streaming logs, lets you filter by fields, log levels or timestamps,
[224.70 --> 230.38]  includes a follow mode, and more. This isn't the first log viewer for humans on the block,
[230.52 --> 235.52]  but it does stand out from the crowd in their provided benchmark. Comparing HL to alternatives
[235.52 --> 243.58]  on a 2.3 gigabyte log file, HL opened the 6 million line log in about 1.1 seconds compared to HLogF,
[243.58 --> 252.72]  which did it in 8.7 seconds. Hewn log, clocking in at about 79 seconds. And FBlog, which took 34 seconds.
[253.28 --> 259.38]  It's now time for sponsored news. Give your GitHub Actions a serious speed boost.
[259.78 --> 264.38]  Your current GitHub Actions setup is doing the job, but it's also taking way longer than it should.
[264.66 --> 269.94]  Every time you push code, you're watching the spinner on 10 plus minute builds. Not fun.
[269.94 --> 275.46]  Namespace flips the script by giving you infrastructure designed from the ground up for fast builds.
[275.94 --> 281.02]  All you have to do is point your existing workflows at Namespace runners instead of the default GitHub
[281.02 --> 286.30]  hosted runners, and instantly those 10 plus minute builds drop to minutes. Behind the scenes,
[286.46 --> 292.02]  Namespace is handling incremental caching, parallel execution of independent jobs, and optimized Docker
[292.02 --> 297.78]  layer caching. The cost difference is also dramatic. Namespace's model gives you predictable pricing,
[297.78 --> 302.40]  and they're built for teams that ship constantly. Instead of watching spinners, they're shipping
[302.40 --> 308.66]  features. Head to namespace.so. Stop watching spinners, get faster builds, and get more of your
[308.66 --> 317.62]  time back for real work. Once again, that's namespace.so. Continuum 93. This is kind of insane.
[317.96 --> 325.24]  Quote, Continuum 93 is an emulator of a classic retro computer that never existed before and is designed
[325.24 --> 332.34]  for retro games programming in native assembly code. End quote. Yes, I read that correctly. This is a
[332.34 --> 338.58]  fantasy computer emulator, which means it has emulated a computer that never was, but certainly
[338.58 --> 344.56]  could have been, and perhaps should have been, but again, it was not. But now it is? My head hurts.
[345.08 --> 351.36]  Continuum 93 was recently open sourced, runs on Windows, Mac, Linux, all 64-bit Raspberry Pis,
[351.36 --> 358.46]  and Steam Deck. It's also created by a guy whose online handle is Enthusiast Guy, which is so apropos,
[358.76 --> 365.38]  my headache went away. Things that aren't doing the thing. The only thing that is doing the thing
[365.38 --> 370.40]  is doing the thing. You already know that. I already know that. But sometimes we need a reminder,
[370.74 --> 376.80]  don't we? Well, here's your reminder. Quote, Making a to-do list for the thing isn't doing the thing.
[376.80 --> 383.04]  Telling people you're going to do the thing isn't doing the thing. And fantasizing about all the
[383.04 --> 388.54]  adoration you'll receive once you do the thing isn't doing the thing. End quote. You get the point,
[388.80 --> 392.64]  but if you want to drill it in your head by reading even more things that aren't the thing,
[392.94 --> 397.32]  click through or stop listening to Changelog News and just go do the thing.
[397.32 --> 403.66]  Changelog News Classifieds. This is our new segment, creating opportunity to share your startup,
[404.02 --> 411.60]  passion project, opinion, big idea, upcoming event, etc. With your fellow 25,000 plus readers and 30,000
[411.60 --> 418.00]  plus listeners, feedback is welcome. Here's this week's classifieds. Shareable Claude Code
[418.00 --> 430.28]  sessions at aviator.co. Styleframe. Type safe composable CSS at styleframe.dev. AI requirement
[430.28 --> 440.72]  software that just works. Battle proven at storywise. That's storywi.se. And Excalibur,
[440.72 --> 447.98]  your friendly TypeScript 2D game engine for the web at excaliburjs.com. All those
[447.98 --> 452.06]  links are in your newsletter, including an additional link that you can use to book your
[452.06 --> 458.56]  own classified ad. That's the news for now, but go and subscribe to the Changelog Newsletter for the
[458.56 --> 464.68]  full scoop of links worth clicking on, such as building a simple search engine that actually
[464.68 --> 473.24]  works, 300 plus NPM packages and 27,000 plus repos have been infected via a fake bun runtime,
[473.24 --> 481.56]  and Android can now airdrop to iPhones. Get in on the newsletter at changelog.news. Last week on the
[481.56 --> 486.76]  pod, Spencer Chang from the Alive Internet Theory and Internet Sculptures joined me for an interview,
[487.18 --> 492.56]  and Practical AI's Chris Benson was on Changelog and Friends explaining to us what is and what is not
[492.56 --> 497.36]  a swarm. Find those in your feed and stay tuned because we have some great episodes coming up this
[497.36 --> 503.84]  week. On Wednesday, we are joined by Bill Buechler, a real-life Wikipedia expert to figuratively gaze
[503.84 --> 510.14]  upon the eighth wonder of the world. And on Friday, our old friend, Lash Vickman, joins us from the west
[510.14 --> 515.70]  coast of Sweden. Have yourself a great week, like, subscribe, and leave us a five-star review
[515.70 --> 518.90]  if you dig the show, and I'll talk to you again real soon.
