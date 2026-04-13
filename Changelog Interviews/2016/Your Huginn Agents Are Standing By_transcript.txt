[0.00 --> 3.18]  I'm Andrew Cantino, and you're listening to The Change Log.
[12.16 --> 17.06]  Welcome back, everyone. This is The Change Log, and I'm your host, Adam Stachowiak. This
[17.06 --> 23.70]  is episode 199, long time in the making. I know you've been waiting for the next episode. I'm
[23.70 --> 30.82]  sorry. I was on paternity leave, got behind. We're back on schedule, so no worries. Jerry
[30.82 --> 36.28]  went solo on this show with Andrew Cantino about Huguen, and now Huguen is a system for
[36.28 --> 41.14]  building agents that perform automated tasks for you online. They can read the web, watch
[41.14 --> 46.60]  for events, and take actions on your behalf. Think of it as a hackable Yahoo Pipes Plus
[46.60 --> 52.66]  If on your own server. We have three sponsors for the show today, CodeShip, DigitalOcean,
[52.66 --> 58.62]  and TruSight Pulse. Our first sponsor today is our friends at CodeShip. They have a new
[58.62 --> 64.08]  platform called CodeShipJet, and they've got this webinar coming up to talk about managing
[64.08 --> 69.28]  test environments with Docker and this new platform called CodeShipJet. CodeShip's engineer,
[69.44 --> 74.24]  Brendan Fosbury, is going to show you how to use Docker to simplify managing your application
[74.24 --> 79.28]  across different environments by using Docker and CodeShip's continuous integration platform,
[79.28 --> 86.74]  Jet. This is a free webinar, April 28th, 2016, at noon Eastern Standard Time. I'm going to put a
[86.74 --> 93.06]  link into the show notes, but in the meantime, go to CodeShip.com slash changelog to learn more
[93.06 --> 95.72]  about CodeShipJet, and now on to the show.
[95.72 --> 110.12]  Welcome back, everyone. Jared here. I want to start this show out with a shout out to a brand new
[110.12 --> 116.22]  member of the changelog family. That's the baby Stachowiak. So congratulations to Adam and Heather
[116.22 --> 122.64]  and welcoming Eli to the world. Adam not here on the show today taking care of more important things,
[122.64 --> 127.90]  but we are excited nonetheless to be joined by Andrew Cantino to talk about his project,
[128.24 --> 134.12]  Hugin. Andrew, welcome to the show. Thank you. So, Andrew, as we like to get started,
[134.32 --> 139.26]  it helps out and it's fun to understand who the guest is, where you're coming from,
[139.36 --> 145.30]  how you got to the point where you built Hugin, which is a system for building agents that perform
[145.30 --> 150.24]  automated tasks for you online. We're going to dig deep into that, but first of all, I'd like to learn
[150.24 --> 157.00]  a little bit about you. So can you tell us a little bit about yourself? Sure. I've been doing
[157.00 --> 163.40]  programming for probably about 20 years. I started when I was, I think I was about 12,
[163.54 --> 169.76]  and I took a summer class on robotics. And I actually didn't particularly like the robots
[169.76 --> 174.80]  because they tended to break a lot, hardware, but I really enjoyed programming for them in BASIC.
[174.80 --> 180.92]  And so after that summer, I convinced my parents to buy me a Pascal compiler, which I don't think I
[180.92 --> 187.20]  ever actually used. I just kept using BASIC and I learned Microsoft Quick BASIC, and then I learned
[187.20 --> 194.46]  something called Real BASIC for Mac. And then I got into Perl. This was before college, and I did a
[194.46 --> 201.58]  bunch of Perl scripts, some of which I sold. And then in college, I majored in physics, but I kept doing
[201.58 --> 206.78]  computer science as well. I took a bunch of classes and ended up minoring in computational science,
[206.94 --> 213.44]  applying it to physics. And I think I learned Java and Python and kept using a lot of Perl for
[213.44 --> 221.20]  web-based projects in college. And then after college, I went to grad school and I switched from
[221.20 --> 227.26]  physics to pure computer science, and I studied machine learning in grad school for a couple years.
[227.26 --> 232.38]  And then I came out to Silicon Valley, and I've been at a bunch of startups and companies out here
[232.38 --> 233.00]  since then.
[233.60 --> 238.90]  Go back to your Perl scripts. You said you sold some of those. What kind of scripts were you selling
[238.90 --> 241.38]  that they were valuable enough people want to pay money for them?
[241.98 --> 249.70]  This was like before the dot-com boom, and people would buy these CGI scripts for very, what we would
[249.70 --> 255.38]  now consider very primitive websites. I had Perl scripts. I had a guest book that you could leave notes
[255.38 --> 261.46]  for each other on a website. I had a chat script, which actually got pretty popular. I ran a network
[261.46 --> 267.44]  of chat servers that were, you could run them with no JavaScript at all. It was better if you had
[267.44 --> 273.20]  JavaScript, but they were pure HTML and CSS if you wanted. So we had a lot of users on web TV,
[273.58 --> 280.46]  which was a thing, and like these really primitive clients that couldn't run JavaScript. And it got
[280.46 --> 284.74]  popular in these sort of strange niche communities for, I think I ran it for almost 10 years.
[285.08 --> 286.58]  Closed it down sort of right after college.
[287.80 --> 292.52]  Web TV, was that that thing where it's kind of like what smart TVs are now, but it was way before
[292.52 --> 296.32]  its time, and you could like get on the web from your television? Is that what that was?
[297.06 --> 303.56]  Yeah, I think you had a device that had a modem, I believe. And you plugged it into your TV,
[303.56 --> 306.94]  and it was a very poor quality screen because TVs were really low resolution.
[306.94 --> 312.34]  Right. And you could very slowly browse the web. And some of them, I don't think even ran JavaScript
[312.34 --> 321.58]  at all. Right, right. So on your website, you say that you're an experimentalist. What does that mean?
[322.56 --> 329.92]  I like building things and tinkering with things and experimenting with new ideas. I sort of like
[330.92 --> 336.76]  building systems from scratch to see how they work. I built a web browser in high school just for
[336.76 --> 340.26]  fun to sort of learn what the primitives were, although back then they were a lot simpler.
[342.12 --> 345.88]  And then so I've, you know, playing with algorithms, playing with toys.
[348.32 --> 353.76]  What's some other stuff you've experimental? I mean, I think perhaps when we get to Hugin,
[353.84 --> 358.62]  we'll find out that that's probably coming out of that tinker mindset. But do you have any other
[358.62 --> 362.48]  examples of things that you just kind of experimented with?
[362.48 --> 370.46]  I've had a couple fun projects. I had a project in college, it might have been before college,
[370.54 --> 379.06]  actually, where I was trying to evolve CSS styling for websites. So you could look at a website and
[379.06 --> 383.16]  it would take the style sheet and mutate it, and then make a couple potential offspring,
[383.36 --> 388.38]  kind of like Blind Watchmaker. And it would display them over a proxied version of the site,
[388.38 --> 393.60]  and you pick the one you like. Or if you wanted, you could pick multiple offspring and pick the
[393.60 --> 399.62]  ones that you like. And then it would combine them and basically treat lines of CSS as genes that
[399.62 --> 404.98]  it could flip back and forth. And so it would do both mutation and combination with the offspring.
[405.14 --> 407.60]  And then you could evolve a style sheet that you liked for that site.
[408.90 --> 409.62]  Very cool.
[410.62 --> 411.22]  Anything else?
[411.22 --> 419.12]  Well, Selector Gadget is a project that I did a while ago that still gets some use. It's a tool for
[419.12 --> 424.80]  building CSS selectors for websites. It's a Chrome extension or a bookmarklet. And you can
[424.80 --> 431.04]  click on a region of the page that you're interested in. And it highlights, it sort of does a best guess
[431.04 --> 435.32]  of what selector would make sense there. So it'll prefer an ID. And then if there's no ID, it'll fall
[435.32 --> 440.08]  back to a class. And it'll highlight everything on the page that matches that. And then usually,
[440.08 --> 443.92]  it's not right on the first try. So then you click on something that you don't want in your
[443.92 --> 450.44]  selection. And it turns red. And then it tries to figure out the sort of minimal selector that
[450.44 --> 452.84]  matches everything you do want and nothing that you don't.
[453.58 --> 457.46]  Yeah, let me just give you props on Selector Gadget. In fact, when I was on your website
[457.46 --> 462.24]  preparing for this call, I saw that you made Selector Gadget. And I was like, yes, that's awesome,
[462.24 --> 466.00]  because I used that back in the day. And it was kind of a revelation because
[466.00 --> 471.76]  I don't know exactly why, but it was so impressive to see it like just, you know,
[472.18 --> 476.80]  drill down on a specific section and grab the selector for you. Because back then,
[476.80 --> 480.56]  we were all kind of learning about CSS selection and how to do it best and how not to do it. And
[480.56 --> 485.40]  at least for me, it was like, it was helping me realize other ways of selecting things
[485.40 --> 490.60]  that I previously would have never known. So very cool. People, people are still using that today.
[490.60 --> 497.08]  Yeah, it still gets some use. I turned it into a Chrome extension maybe a year ago, and it's
[497.08 --> 502.30]  getting some use. It's never sort of taken off. It's hard to know, you know, it's because people
[502.30 --> 507.88]  just use it. I don't have any great metrics on how much it gets used. But sometimes it shows up on
[507.88 --> 508.58]  Twitter periodically.
[509.18 --> 513.88]  Right, right, right. That leads to me one question I've been asking people recently, because I'm kind
[513.88 --> 520.38]  of becoming transfixed on this idea of longevity with software projects, and really having a lot of
[520.38 --> 526.64]  respect for things that are, well, what people might consider legacy, but are just like older,
[526.76 --> 532.60]  but actually had value and still work today. And so looking back at myself and my own software
[532.60 --> 537.18]  development career, I look back at stuff that I wrote back in the, I mean, I can only go back about
[537.18 --> 542.52]  10 or 12 years, because that's how long I've been doing development. But I look at things that I wrote,
[542.62 --> 549.52]  you know, 10 years ago, and ask myself, what's still useful? And so thinking about it like that,
[549.52 --> 554.66]  and you have a longer history than I do. Does anything go past selector gadget going back?
[554.72 --> 558.76]  You said that you had these ProScripts that ran for quite a long time. What's the oldest piece
[558.76 --> 562.88]  of software that you wrote that's still being used in some capacity today?
[563.84 --> 569.84]  That's a good question. Well, older than selector gadget, I was on the Gmail team at Google
[569.84 --> 576.74]  for a summer internship. And I'm pretty sure that code I wrote to generate filters in Gmail is still
[576.74 --> 584.68]  in use, as well as possibly some of the code in the search bar that does autocomplete. I don't know
[584.68 --> 590.82]  how much it's evolved since I was there. But that's about eight years old. And then older still,
[590.82 --> 596.08]  there was a project called absurdly cool freebie finder, which was this search engine for finding
[596.08 --> 602.44]  free stuff. Nice. And that's still online. But unfortunately, I sold it, which was not
[602.44 --> 607.50]  unfortunate. I'm you know, that was great. Unfortunately, I mean, unfortunately, the new
[607.50 --> 611.50]  owner has just sort of let it die, which has actually been my experience in general of stuff
[611.50 --> 616.74]  that I've sold, I've sold it. And then the next person doesn't care as much as I did. Yeah. So it
[616.74 --> 621.94]  sort of goes away. The site's technically still up, but it's not aggregating anymore. Yeah. But I ran
[621.94 --> 630.48]  that since, uh, see, since about 2005. Older than that, I'm sure there's still some Perl scripts
[630.48 --> 634.98]  running somewhere. I mean, I had like 100,000 downloads of that guestbook. There's no way they're
[634.98 --> 640.74]  all gone. But it was, you know, super insecure, terribly written, untested Perl. So I kind of hope
[640.74 --> 646.58]  they're all gone. So you told us how you got into software. What about open source specific? Can you go
[646.58 --> 652.10]  back to you? Remember your open source roots and where the idea of open source kind of, uh,
[652.86 --> 658.94]  sprung up in you and you got excited about it? That's a good question. Um, well, so the,
[658.94 --> 663.30]  the Perl scripts that I mentioned, most of those were open. There was no real realistic way to make
[663.30 --> 668.26]  them closed source because they would, you just have to provide the script for someone to run. Um,
[668.44 --> 672.56]  so some of those I think got changed and you could, most of them were free. Many of them were free.
[672.56 --> 683.24]  So that was in high school, um, 20 years ago. Um, before that, a really sort of formative experience
[683.24 --> 688.90]  for me was this Macintosh application called hotline. And it was this network of, it was
[688.90 --> 694.18]  peer to peer and it had trackers and it had servers that would register to the trackers and each server
[694.18 --> 702.54]  could have a chat room and a forum and file exchange. Um, and I was probably 13 or something.
[702.56 --> 709.06]  When I found these and I stumbled on this community of other children, roughly my age, some were older,
[709.30 --> 713.94]  some were younger, but we're all sort of teenagers, um, who are learning real basic together.
[715.46 --> 720.48]  And that was the language that I was playing with at that time. Um, and that was really cool because
[720.48 --> 724.34]  people would just upload examples of something they made and someone else would download them and
[724.34 --> 730.42]  sort of riff on it and upload a new one. And that's, that was really sort of formative for me to get
[730.42 --> 734.76]  into real programming. And cause there were people there who were more experienced than me and I
[734.76 --> 739.96]  could learn from their tricks. Um, that's where I sort of, I mentioned that I wrote a simple web
[739.96 --> 744.36]  browser. It was there and shared it. People thought, you know, you get props, you know, people like,
[744.42 --> 749.42]  this is awesome. How did you do this? And it was really, it was like a fun game. Um, so that's sort
[749.42 --> 753.04]  of proto open source. Like, I don't think many things came out of that that became real products.
[753.04 --> 759.10]  I'm sure some did. Um, but it was really important for me to sort of work with a community of other
[759.10 --> 764.74]  programmers. Just thinking about that and the, even the open nature of the Perl scripts that you
[764.74 --> 770.28]  were selling makes me wonder cause it was so back so far back. Um, how did you go about, like,
[770.28 --> 774.56]  what was the transaction like when you sold a Perl script back then? Was it a mail me some cash?
[774.66 --> 780.58]  Was it, was it? Yeah, I think so. I think it was like mail me, mail me a check. Um,
[780.58 --> 783.22]  that's probably cash sometimes. Yeah. And we're not talking, you know,
[783.22 --> 786.18]  this was like a hundred bucks and I was in high school and that was, that was great.
[788.22 --> 790.18]  A hundred bucks is awesome when you're in high school.
[790.98 --> 794.00]  Yeah. I mean, I think I had a few that might've been a couple grand. Like it was,
[794.38 --> 797.08]  it was certainly a great, great spending money in high school.
[797.90 --> 803.08]  Very cool. Well, we are going to talk about Hugin. Let's take a quick break and we will dive
[803.08 --> 806.38]  into what that is and why it's awesome. We'll be right back.
[806.38 --> 813.24]  We're working with our friends at BMC to spread the word about true site pulse,
[813.34 --> 818.98]  the real time monitoring service for apps and infrastructure. I talked to Mike Moran,
[819.06 --> 825.66]  the senior architect about the idea of dev teams out there rolling their own monitoring system
[825.66 --> 831.10]  using something that's open source or building their own from scratch. And he had this to say,
[831.10 --> 836.98]  I think if you want to roll your own and spend the dev effort of having to build that internally,
[836.98 --> 841.18]  that's great. My only question to you is if you spend your time doing that,
[841.18 --> 846.46]  are you providing value to your customer and are you actually moving your product forward or are you
[846.46 --> 850.64]  holding your product back? And I think a lot of what something like true site pulse offers you is
[850.64 --> 855.18]  we take a lot of that on for you so you can provide that value to your customer on your product
[855.18 --> 859.40]  instead. So we have plugins for, I think there's 30 plugins for different parts of your
[859.40 --> 863.44]  infrastructure. We have an agent that's been running for three years written in C that takes
[863.44 --> 867.74]  a very small amount of your resources. As you add more servers, you're not going to have to worry
[867.74 --> 871.56]  about the scalability as much. And we've written the chef and the puppet scripts for you. So that's
[871.56 --> 876.50]  all taken care of. It's letting us worry about it so you can focus on your customers. That's kind of
[876.50 --> 881.14]  the value that true site pulse adds as opposed to you having to do it yourself. We've all been in
[881.14 --> 885.80]  organizations where we've joined and had to rewrite the entire monitoring stack. And that's just
[885.80 --> 890.38]  something we didn't want to have to do. We want to come in, we want that taken care of. And then
[890.38 --> 894.66]  that way we can focus on the things that are going to matter to our customers. That was Mike Baran,
[894.78 --> 900.58]  senior architect at true site pulse. To learn more about true site pulse and how it helps you deliver
[900.58 --> 907.94]  more value to your customers, head to bmc.com slash true site pulse, all one word and tell them Adam
[907.94 --> 917.48]  from the Chainslog sent you. All right, we are back with Andrew Cantino and we want to talk about
[917.48 --> 923.76]  this really cool project called Hugin that has caught traction probably more so than selector gadget. I
[923.76 --> 930.68]  think you got 13,000 stars, 1300 plus forks, 110 contributors, which is quite an accomplishment.
[930.68 --> 935.90]  Um, we're going to talk about what Hugin does, but let's first, let's get the name out of the way.
[936.62 --> 943.44]  Um, because it's one of these things where, as I was saying before the call, uh, as programmers,
[943.44 --> 947.84]  we tend to write things all the time and we read words and we all kind of live on our terminals,
[948.06 --> 952.40]  you know, reading text. And it's not until shows like these where we get together and
[952.40 --> 957.40]  actually have to talk about concepts and many things, we just pronounce them differently. And so I
[957.40 --> 962.28]  thought it was Hugin ever since I've heard about it, which was a couple of years ago now, until you
[962.28 --> 967.08]  sent me your audio clip and I found out you pronounce it Hugin. So can you first give us the
[967.08 --> 975.28]  inspiration for the name and then, uh, kind of describe the pronunciation? Sure. Um, so Hugin is named after
[975.28 --> 982.20]  one of the ravens of the Norse god Odin. Uh, they, in mythology, they flew around the world and reported
[982.20 --> 987.38]  back on what they saw. So the two ravens were Hugin and Munin, thought and memory.
[988.20 --> 993.64]  Um, and I've always pronounced a Hugin when I've looked online, um, for someone who might actually
[993.64 --> 999.56]  know what they're talking about. I've heard Hugin. Um, I've never actually heard Hugin, which is what a
[999.56 --> 1003.72]  lot of people say in the open source community. And I think it's kind of cute, so it doesn't bother me.
[1003.80 --> 1008.20]  Yeah. It's kind of funny because when you come across the name, like I did at just reading it and
[1008.20 --> 1012.36]  saying, Hmm, and you just kind of sound it out. And I don't know anything about that mythology. I think
[1012.36 --> 1017.24]  it's a cool name based on that makes lots of sense. You're like, Oh, it's trying to hug you.
[1017.24 --> 1023.24]  Like, it's gonna like, Hmm, I'm not really sure why I named it Hugin, but there it is. Hugin. Um,
[1023.88 --> 1027.40]  so it's just funny how we, we kind of construct these things in our minds to fill in the gaps.
[1028.12 --> 1032.52]  Um, but that's such a great name based on that mythology. Was it something where
[1033.24 --> 1037.32]  you already knew the story and you're said, well, this makes tons of sense because this is
[1037.32 --> 1041.64]  an agent getting information for you, just like in the mythology, or were you digging for a name
[1041.64 --> 1045.00]  and you like came across that and you thought, Oh, I can use this. How'd that come about?
[1045.00 --> 1049.24]  That's a really good question. And I honestly can't remember. Okay.
[1049.24 --> 1055.88]  I think that I was looking around for a name and sort of looking for inspiration in mythology,
[1055.88 --> 1058.76]  but that, that may not be right. I can't remember.
[1058.76 --> 1062.44]  Are you ever thought about starting a Munin project?
[1063.32 --> 1064.84]  I would, but there is one. Yes, there is.
[1064.84 --> 1066.76]  It's a, it's a monitoring tool. That's right.
[1068.76 --> 1073.08]  Well, uh, so you're, you're in San Francisco and you're said you, you worked at some startups,
[1073.08 --> 1078.20]  so you're very familiar with the elevator pitch, right? So if you had to describe Hugin to somebody
[1078.76 --> 1083.00]  in a paragraph or two and you had to do the elevator pitch, what would that sound like?
[1083.00 --> 1090.60]  So if you're aware of products like if, if, which is if this, then that, or Zapier,
[1090.60 --> 1094.84]  then Hugin is really easy to describe because it's basically an open source self-hosted
[1095.48 --> 1099.32]  clone of the if or Zapier or a little bit like Yahoo pipes.
[1101.00 --> 1108.36]  And then the more pure elevator pitch would be use Hugin to monitor the world for you to take data in
[1108.36 --> 1115.32]  from interesting sources on the internet and then react to it, filter it, aggregate it, and then take actions on your behalf.
[1115.80 --> 1120.76]  So, which is often as simple as sending you an email, but it could be more complicated to like posting something or
[1121.40 --> 1122.92]  taking some more interesting action.
[1123.32 --> 1129.32]  We might have to take a moment to a pause for pouring out a drink for Yahoo pipes. Isn't that dead now?
[1130.28 --> 1133.48]  It is. Um, I was sad to see it go. It was a great product.
[1133.48 --> 1136.52]  Yeah, it really was such an interesting idea and so many uses.
[1136.52 --> 1143.16]  Um, I was, I think a lot of the open sourcers were, were sad to see that one finally get closed down.
[1143.64 --> 1149.96]  There's been an influx of users after Yahoo pipes closed down to, I'd say sort of varying degree of
[1149.96 --> 1155.00]  success. Like some of them, Hugin really does meet their needs and some of them want to use Hugin for
[1155.56 --> 1162.60]  sort of very deep feed recombination and filtering, which it can do if you sort of squint, but it's not,
[1163.24 --> 1165.00]  not sort of perfect for that at the moment.
[1165.00 --> 1171.72]  So perhaps some more of your disgruntled users or, or your feature requesters are the people
[1171.72 --> 1178.76]  coming from the Yahoo pipe site. Um, first commit March 3rd, 2013. So it's, you know, three years
[1178.76 --> 1186.28]  old now. Um, was you said you describe it as if you understand if this, then that, and, or Zapier,
[1186.28 --> 1191.80]  then you can describe Hugin as a clone of those things or an open source version of those things.
[1192.44 --> 1198.12]  Was, uh, if this, then that, or Zapier, the actual inspiration for it, was it a clone or
[1198.12 --> 1202.76]  it just happened to be like mutual, uh, invention or how did it, how did it start?
[1202.76 --> 1209.00]  No, it wasn't a clone. Um, I started it a little earlier than that. I think it was
[1209.48 --> 1216.20]  December around Christmas of 2012. Um, I was at home visiting my family and needed a project to
[1216.20 --> 1223.48]  tinker on and had this idea for basically just a GUI for cron jobs and sort of reusable components
[1223.48 --> 1229.16]  that could be wired together. Cause I ended up writing so many little scripts in Pearl or Ruby to
[1229.16 --> 1234.12]  automate things. And they, you know, I tend to rewrite them all the time and I don't have a
[1234.12 --> 1238.76]  shared library. And so it was, it started as a shared library of stuff that I wanted to wire
[1238.76 --> 1244.52]  together inside of a rails app. Um, I think my first use case, which I still actually use, um,
[1244.52 --> 1249.40]  was it would be really cool if I got an email in the morning or push notification, if it was going to
[1249.40 --> 1256.92]  rain that day so that I actually remember to take my umbrella because I'm terrible at this. Um, so I have a
[1256.92 --> 1261.00]  network of Huguen agents that does that for me and it did that very early on. I think it was the first
[1261.00 --> 1268.60]  thing I implemented. Um, I also played with a bunch of location based stuff early on. Um, so yeah,
[1268.60 --> 1273.56]  it wasn't really, I don't think it was inspired by any existing product that I was aware of. It was
[1273.56 --> 1278.44]  just sort of the result of tinkering. So as you became aware of those products, did you ever think,
[1278.44 --> 1286.52]  uh, they, perhaps they ripped you off or that, uh, you could compete with them or like, what was your
[1286.92 --> 1291.56]  what was your reaction as you, I think Zapier is probably newer. I don't know. I actually don't
[1291.56 --> 1297.16]  know the history. I feel like it's newer than if in the marketplace. Um, and so maybe they cloned them,
[1297.16 --> 1301.16]  but what do you, what were your thoughts as you see, see these other things come out and they're like,
[1301.16 --> 1306.60]  you know, pretty successful, uh, small businesses or startups at this point, uh, that are basically
[1306.60 --> 1309.72]  providing very similar functionality to what you've been doing in the open source space.
[1310.60 --> 1316.04]  I think it's great. Um, they're good products and I have nothing against them. And if you don't want
[1316.04 --> 1320.68]  to host, you know, something on your own or you're not trying to extend it, they're really good
[1320.68 --> 1325.16]  solutions. Uh, they have a lot of connectors that are monitored by, you know, professional
[1325.16 --> 1329.72]  people who know how to run services. Right. And that's awesome because then I don't need to build
[1329.72 --> 1335.56]  a, you know, hosting platform. And, um, I, my interest was always in controlling my own data.
[1335.56 --> 1340.76]  I didn't really want to have my data be in someone else's hands. And I, it doesn't really bother me
[1340.76 --> 1346.28]  sort of in an abstract sense, but mostly in sort of the longevity that you mentioned, you know,
[1346.28 --> 1350.92]  startups come and go, and I want to have, I would love if I have, you know, 20, 30 years of history
[1350.92 --> 1354.92]  at some point of all this data that I can play with. And that seems unlikely if I'm giving it all
[1354.92 --> 1362.12]  to a startup. Um, so my motivation was sort of twofold, one to control the data, not so much out
[1362.12 --> 1367.64]  of paranoia, but just sort of to keep my hands on it. And the second was really that, you know,
[1367.64 --> 1376.04]  I'm a programmer. It's satisfying to write things. And Hugen is a library of reusable components.
[1376.04 --> 1380.12]  And often I find myself needing to add just one more to make something complicated work.
[1380.68 --> 1385.24]  So it's really satisfying as a developer, because you can go in there, use a simple API,
[1385.24 --> 1390.28]  write another agent and wire it all together. Um, and that's just not something you can easily do
[1390.28 --> 1393.96]  in these hosted solutions. You can't just go write arbitrary code and run it.
[1393.96 --> 1397.00]  Yeah. You have to fit it inside of whatever framework they provide, which
[1397.64 --> 1404.44]  is usually limiting. Um, and all things are, all interfaces are limiting. So what are some of
[1404.44 --> 1409.16]  the cool things that you can do with Hugen? You mentioned the first one, which seems like
[1409.16 --> 1413.96]  was your primary use case at first, which was, let me know when I need to remember my umbrella.
[1414.92 --> 1419.96]  That's right. Um, what are some other ones? Oh, there's a bunch. Um, and frankly,
[1419.96 --> 1425.80]  I think that I am one of the more boring users of Hugen. It has mostly met my needs for a while.
[1425.80 --> 1431.16]  Um, and some of the stuff that people are using it for now are much more complicated than any of my
[1431.16 --> 1437.08]  personal use cases. One of my favorite uses that I do use it for routinely is to monitor Twitter.
[1437.96 --> 1444.44]  Um, so Hugen can run a Twitter agent and follows the, the Twitter filtered feed. You can give it a
[1444.44 --> 1449.96]  bunch of terms that you'd like to hear about. Um, and then Hugen can either just, you know, emit an event,
[1449.96 --> 1456.92]  um, for every term. So for something rare, I do that. For example, the word Hugen, um,
[1456.92 --> 1461.64]  not particularly common. So I just see all of them or my last name is actually pretty rare. So I just see
[1461.64 --> 1467.32]  all of those. Um, but for anything frequent, I don't want to get an email for every time it's
[1467.32 --> 1472.92]  mentioned. I just want to know when it's changed in an interesting way. And so in, in that case,
[1472.92 --> 1477.96]  I use the Hugen mode. It has two modes, either events or counts. And if you do counts,
[1477.96 --> 1482.04]  and it's basically emitting a histogram bucketed by whatever check frequency you set.
[1482.52 --> 1487.24]  So you say to check every five minutes and roll up, um, the number of times that a certain term
[1487.24 --> 1493.88]  has occurred. And then I've send those to a peak detector agent, which, um, can filter,
[1493.88 --> 1499.48]  basically watches for a high standard deviation spike in that time series, and then triggers its
[1499.48 --> 1504.04]  own event if, if that occurs. And then that I either send to either, you know, a push notification or
[1504.04 --> 1511.64]  an email or something else. So I can give you two examples. Um, for the push notification case,
[1512.20 --> 1516.92]  that's something I want to know right now. So I have a couple agents that watch for like the terms
[1516.92 --> 1523.08]  San Francisco tsunami or bomb threat or something like that. And I want to know, like, tell me right
[1523.08 --> 1527.32]  away if this happens. And so I could find out in a couple, you know, in about a minute, if there's a
[1527.32 --> 1533.88]  sudden spike in conversation about those terms on Twitter. Um, that's really cool. And then luckily
[1533.88 --> 1540.12]  those haven't triggered very often. Um, and then the more useful day to day ones are the slightly
[1540.12 --> 1545.56]  less frequent, but interesting terms where I basically use Huguen to watch for interesting
[1545.56 --> 1549.16]  stuff to happen on Twitter that I think might happen eventually. And just tell me if it does.
[1549.16 --> 1555.72]  So I don't have to check myself. So for example, if I'm waiting for, you know, a call for a call
[1555.72 --> 1559.72]  for papers at a conference, I'll put, I'll put the conference name in Twitter and it'll spike when
[1559.72 --> 1565.48]  they announce something. Um, I'm waiting for Mass Effect 4 to be released. So I just have Mass Effect 4.
[1565.48 --> 1571.00]  And if there's some announcement, I get an email, uh, NASA announcement, Ruby vulnerability.
[1572.12 --> 1576.12]  Um, one, a recent one I started using is if there's a movie I'm waiting for on Netflix,
[1576.12 --> 1581.56]  I do just movie name Netflix and that will spike when it gets released and I'll get an email.
[1582.76 --> 1589.48]  It's basically like a sort of fuzzy natural language API to the world. Like Twitter, you know,
[1589.48 --> 1594.28]  people are going to say things in their own words when something happens. And it has such volume that
[1594.28 --> 1598.92]  if you just keep an eye on it, almost any term that you pick is going to increase proportionally
[1598.92 --> 1603.96]  to the amount of interest. And so if you just look for spikes in that, it works surprisingly well.
[1603.96 --> 1609.56]  I love that. It's kind of like, you know, the Google news search alert type of a thing only.
[1610.28 --> 1614.44]  And I'm not sure how much they put into it, but I love how it's proportionality or based on trends.
[1615.24 --> 1619.64]  Um, because you, you tend to get so many false positives or, you know, I used to have one out
[1619.64 --> 1625.48]  for my name and, uh, cause my name is pretty unique, at least when the first and last combined
[1625.48 --> 1629.48]  and unique enough that there weren't false positives. But all I would get alerts on is whenever I published
[1629.48 --> 1634.20]  my own a blog post and I'd be like, oh yeah, well, I already knew that one. Cause I just hit,
[1634.20 --> 1638.76]  you know, the publish button a couple hours ago. Um, but then if you get more specific on,
[1638.76 --> 1644.76]  then if you try to generalize more, you get overflow, you know, you get tons of results.
[1645.16 --> 1651.00]  Um, I used to have that problem. So one of the ways that I bootstrapped my consultancy back in,
[1651.00 --> 1658.20]  I don't know, it was seven, oh eight, whenever Twitter was first out there. Um, and I started
[1658.20 --> 1663.48]  realizing that a lot of people would, they, when they turned, when they needed the technical help,
[1664.04 --> 1670.36]  it was a lot of work to like post a job listing, right. Or to, um, you know, put an ad in the paper
[1670.36 --> 1676.44]  or whatever your traditional means were to post for help. And it was really easy to just like
[1677.00 --> 1680.84]  put something out on Twitter. I noticed a lot of people were starting to do that with specific
[1681.48 --> 1685.56]  you know, programming needs. And so I wrote a little monitor similar to the one that you just
[1685.56 --> 1690.92]  mentioned, looking for specific keywords and then paired those with phrases. And mine turned into
[1690.92 --> 1696.36]  an RSS feed cause I was just consuming RSS in the morning anyways. And I use that as ways of finding,
[1696.36 --> 1703.72]  you know, job leads, uh, using, you know, freelance type stuff. But there was, it was super useful and
[1703.72 --> 1709.64]  it ended up being a way that I, I did get a lot of business that way. Um, but it was full of false
[1709.64 --> 1713.88]  positives, especially cause like the word Ruby is also a girl's name and you know, you run into
[1713.88 --> 1721.00]  stuff like that. And, uh, it seems like your way of doing trends or waiting for a certain proportional
[1721.00 --> 1726.92]  change probably flakes out a lot of the false positives. So it's just higher signal, less noise.
[1726.92 --> 1727.64]  Is that what you found?
[1729.00 --> 1735.00]  Yeah, it does pretty well. It's not perfect, but, um, it's low enough noise that it's useful.
[1735.00 --> 1739.48]  And for those, I just have it send me a digest email once a day. So I skim through them and
[1739.48 --> 1743.48]  it formats them. So each one's a link to the search results on Twitter. So I can pretty quickly
[1743.48 --> 1748.28]  see like, Oh no, that's, you know, totally unrelated. I can see why it triggered it, but
[1748.28 --> 1752.12]  most of them are actually relevant. And so it's, I keep using it.
[1752.12 --> 1756.44]  I love how many ideas you have about ways of viewing that, using that one single feature.
[1756.44 --> 1761.16]  I feel like I wouldn't have, I've never even figured if I put Netflix plus a word
[1761.56 --> 1766.44]  that I'll know when the movie's available. Like I've, my brain doesn't connect those dots on its own.
[1767.24 --> 1771.16]  Um, I'm sure there's a place for at least Huguen agents where you guys have a list of like,
[1771.16 --> 1775.80]  here's different ways that you could use it. But what about your, your specific Twitter stuff?
[1775.80 --> 1779.32]  Is there anywhere where that lives online where somebody could go for inspiration
[1780.04 --> 1784.20]  of ways of, you know, being notified of an earthquake and Molly?
[1785.80 --> 1789.64]  I've, uh, I've written a couple of blog posts about it. Um, there's some tutorials,
[1789.64 --> 1794.12]  but, and I know other people are doing it too, but I don't know, you know, of the user base of
[1794.12 --> 1798.20]  Huguen, how many people are using Twitter. A number of people have said they are.
[1799.48 --> 1803.64]  But, and a bunch of people are using it in different ways than me. They use it for posting or for,
[1803.64 --> 1807.48]  you know, following a small group of people and rolling it up into an RSS feed.
[1809.16 --> 1815.24]  I also, um, I'm not sure that we've really sort of explained at a higher level, how Huguen is wired
[1815.24 --> 1818.20]  together. If you think that would be useful to talk about.
[1818.20 --> 1821.16]  Well, first, just give us a couple more use cases. I think we'll definitely do that.
[1821.16 --> 1821.72]  Sure.
[1821.72 --> 1824.28]  Um, and we would like to, when we, when we hear about that architecture,
[1824.28 --> 1829.08]  we'll probably talk about the specific bits because I think technically it's, it's interesting.
[1829.08 --> 1833.00]  There's lots of, you know, moving pieces and you've put together into a holistic system.
[1833.00 --> 1837.32]  We want to hear about that. Um, just to continue to wet our appetites. You have,
[1837.32 --> 1842.12]  let me know when it's raining. You have Twitter based aggregation notifications. What are some of
[1842.12 --> 1846.20]  these? Those are your, your main use cases. What are some of the crazier ones that other people have
[1846.20 --> 1851.72]  done that you're like, wow, that's really cool. Well, one of my favorites, mostly because it's just a
[1851.72 --> 1857.40]  big name is that the New York times used it to monitor some of their internal Olympics coverage a couple of years ago.
[1857.40 --> 1862.84]  So I believe they were using it for sort of fairly traditional monitoring where they were,
[1862.84 --> 1866.84]  it was watching their own, what would their own website and looking at their own output and then
[1866.84 --> 1872.52]  alerting if it didn't match expectations. Um, but that resulted also, you know, that was,
[1872.52 --> 1878.52]  that was neat. That's cool to see that use case and also, um, got some contributions from them in terms
[1878.52 --> 1885.32]  of additional code. That's nice when people stay involved and keep adding to it. Um, there's another use case
[1885.32 --> 1890.36]  I heard about where someone was using it to download, uh, civic data releases. Like if governments
[1890.36 --> 1895.56]  released interesting datasets, they would watch those fairly hard to follow feeds and let them
[1895.56 --> 1901.96]  know in a more useful way if it happened. Um, I've seen a lot, you know, there's home automation stuff,
[1901.96 --> 1908.84]  like turn on my porch light at my actual local sunset, stuff like that. You have listed on the readme,
[1908.84 --> 1913.96]  just different things you can do with it. One is create Amazon mechanical Turk workflows as the
[1913.96 --> 1919.96]  inputs or outputs of agents. For example, once a day, ask five people for a funny cat photo,
[1920.60 --> 1924.52]  send the results to five more people to be rated. Send the top rated five to people,
[1924.52 --> 1929.56]  five other people for a funny caption, send to five final people to rate for funniest caption. Finally,
[1929.56 --> 1934.28]  post the best caption photo on my blog. I don't know. No one's doing that. Right.
[1935.80 --> 1941.48]  I mean, I tried it once and it mostly worked and then I decided I didn't need to personally run a
[1941.48 --> 1949.24]  funny cat blog, but it did work. It's awesome. Is it as Amazon Turk, as if you know, anybody using that
[1949.24 --> 1953.40]  to great advantage in any way, that's not one of these fun kind of like that would be cool.
[1953.40 --> 1959.72]  I think it's being used a lot in the machine learning and AI community to build data sets. I
[1959.72 --> 1965.72]  think that's the sort of most valuable use case is building a data set of human labeled information,
[1965.72 --> 1974.68]  either labeling photos or annotating sentiment on tweets or, you know, noting down the text regions
[1974.68 --> 1979.80]  of documents of photos of documents, stuff like that, where you just need to build these really
[1979.80 --> 1982.60]  large data sets for deep learning. Yeah, that makes tons of sense.
[1983.56 --> 1987.72]  Well, I think this is a natural place to break. We do want to talk all about the
[1988.92 --> 1994.76]  the nitty gritty details of how Huguen works, the agents, the peak. What do you call that? A peak
[1994.76 --> 2001.24]  adapter, peak monitor. I don't know. You have a peak detector. You got a nice Asian event flow document.
[2001.24 --> 2007.16]  So some graph is fun coming up. Let's take a quick break and we will dive into that on the other side.
[2007.16 --> 2013.24]  If you're like me or most people out there, you want to attach highly available,
[2013.24 --> 2019.40]  expandable block storage to your droplets on digital ocean. And guess what? The feature is here.
[2019.40 --> 2025.48]  You've asked for it. They've delivered kind of right now. You can request early access.
[2025.48 --> 2031.40]  The feature is coming in the summer of 2016. So I heard that the earlier you get on the list,
[2031.40 --> 2037.48]  the earlier you get the feature. So head to digitalocean.com slash features slash storage.
[2037.48 --> 2039.96]  Get early access. Do it today.
[2039.96 --> 2047.32]  All right, we are back. And I don't know about everybody else, but I've been,
[2047.32 --> 2053.28]  my appetite has been sufficiently wetted. I'm very interested. Huguen sounds really cool. It can do
[2053.28 --> 2058.44]  lots of different things, things that I would never even imagine to even want to be done until I hear
[2058.44 --> 2062.92]  about them. And I think, oh yeah, that would be pretty cool. Which is kind of the beauty of these
[2062.92 --> 2069.40]  types of system is that they really are just a bunch of tools and ways that you can do things and you
[2069.40 --> 2075.56]  have to bring your ideas to them and make them do cool things. So Andrew, talk to us about specifics,
[2076.36 --> 2082.44]  how it was built, how it works. You have agents. It appears to be a Ruby on Rails application.
[2083.24 --> 2091.56]  Can you break it apart for us and tell us how it all is wired together? Sure. So it is a Rails
[2091.56 --> 2097.16]  application. It's actually a pretty traditional Rails application. We're not doing anything particularly
[2097.16 --> 2105.08]  unusual. It's my sort of my focus has always been on ease of use and ease of deployment and ease of
[2105.08 --> 2111.16]  development. And so it's not really intended for high throughput. You know, I wouldn't use Rails for
[2111.16 --> 2117.32]  really high throughput application for data processing. But it holds up totally fine for sort of personal
[2117.32 --> 2124.84]  business use. It's like small business use. The basic wiring is that we have these models called
[2124.84 --> 2129.72]  agents. They're the core object in the system. There's many types of agents. You know, there's
[2129.72 --> 2133.16]  some of the ones I've mentioned, like the one that can talk to Twitter and the peak detector,
[2133.72 --> 2138.28]  the mechanical Turk agent. There's a lot of other agents that sort of focus on outputting to systems,
[2138.28 --> 2145.40]  like push bullet or pushover, RSS, Slack. And then there's things like webhook agents that can
[2145.96 --> 2153.08]  both send and receive posts to remote systems. And then one of the more complicated ones is the
[2153.08 --> 2160.76]  website agent that can sort of scrape arbitrary websites in, I think at this point, RSS and HTML and
[2160.76 --> 2167.48]  JSON and XML. It's sort of, it's gotten a little bloated, but it's very powerful for, you can give it a set of
[2168.28 --> 2175.08]  CSS selectors or XPath selectors. And it can grab all the regions of a page that match and emit those
[2175.08 --> 2182.60]  as events. So that brings us to events. Agents are connected together in an event flow graph. So
[2182.60 --> 2191.32]  agents can receive and emit events. Events just flow to all the receivers and they propagate down until
[2191.32 --> 2196.28]  they stop propagating. So, you know, you should avoid making loops. In theory, you could get yourself
[2196.28 --> 2201.56]  into a situation where you had an infinite loop. Although in reality, it doesn't happen. I've never
[2201.56 --> 2209.48]  really had it happen. And then, so you have agents, you have events that they emit and receive,
[2209.48 --> 2215.40]  and they just propagate along. And then agents are modeled after sort of a simple reaction agent. So they
[2215.40 --> 2222.92]  have state, they have memory that they get to use however they want. You can have many instances of an
[2222.92 --> 2228.12]  agent and they each have their own memory, but then they just receive and emit events and events are immutable.
[2229.40 --> 2234.52]  So, you know, that's sufficient to build most types of systems where I need to store some state,
[2234.52 --> 2240.44]  I need to react to things. And then it means that there's a pretty simple API for developers to add new
[2240.44 --> 2245.88]  agents. Cause it's just basically a simple active record model that you extend, you wire in.
[2245.88 --> 2251.80]  If you want to receive events, then you define a receive method. If you want to check for events on
[2251.80 --> 2256.68]  a schedule, sorry, if you want to do something on a schedule, you define a check method and the user
[2256.68 --> 2261.96]  can pick what schedule should run. And then you can use your memory if you need it and you can emit
[2261.96 --> 2267.48]  events if you need to. Obviously there's some more complexities. We have types of agents that can run
[2267.48 --> 2273.40]  continuously in a background thread and some other stuff like that. But at a basic level, it's really pretty
[2273.40 --> 2279.72]  simple. Yeah. So your, your, your main user interface is the creation and the editing and
[2279.72 --> 2285.00]  the hooking up of the different agents to do what you want. And then it shows you kind of the status
[2285.00 --> 2290.92]  of those agents and what they've done recently. How does the, the scheduling system work? How does the
[2290.92 --> 2297.64]  backgrounding work? So we're running a background. We have two versions that can either run multi-process or
[2297.64 --> 2304.52]  multi-thread by default these days, it runs multi-thread. We use Rufus scheduler, which is a
[2304.52 --> 2312.04]  Ruby gem that does a good job of simulating both cron style scheduling, as well as pure sort of exact
[2312.04 --> 2319.24]  time scheduling is basically cron. And we use it to trigger any set of registered agents on a certain
[2319.24 --> 2325.08]  schedule. So when you make a new agent that has a check method defined, you can say, I want this to run
[2325.08 --> 2331.32]  at midnight every day or every five minutes, et cetera. And it will do whatever its check method
[2331.32 --> 2336.68]  does and, you know, do whatever this agent is designed to do. And then we just in the background
[2336.68 --> 2342.92]  use Rufus schedule to make sure those run. I imagine, like we said earlier, you have 110 contributors,
[2343.48 --> 2350.04]  you know, most projects will have a lot of kind of long tail contributors, but only a few, you know,
[2350.04 --> 2355.16]  core people that work on it. This seems to be pretty typical in that sense. But is the majority
[2355.16 --> 2360.60]  of your contributors besides typos and minor bug fixes, are they adding agents to the system? Is
[2360.60 --> 2366.68]  that the main way that people contribute to the project? Yeah, I'd say that's the primary way.
[2366.68 --> 2373.08]  We do get a lot of small bug fixes too for the core system. But there's probably the bulk of the
[2373.08 --> 2378.76]  contributors have come, have shown up, added one agent that they needed for their use case
[2378.76 --> 2383.24]  in a pull request, and then they've sort of disappeared. Some of them show up again a year
[2383.24 --> 2389.16]  later with another agent or a bug fix because they've started to push the system. So yeah, I think that's
[2389.16 --> 2393.80]  pretty much true. And one thing you mentioned is that you want to keep it as vanilla or as simple
[2393.80 --> 2401.08]  as possible for ease of deployment. And I would say that, you know, as an open source advocate and as a
[2401.08 --> 2407.32]  developer, as well as a person who's ran many websites and many services over the years,
[2408.60 --> 2415.32]  I'm almost allergic to some of these systems because of the maintenance. And I would almost
[2415.32 --> 2420.36]  always use a provided service, even though I'm completely well aware that most of these startups
[2420.36 --> 2426.04]  disappear. And I've definitely had them disappear right out from under me. And so everything's a trade
[2426.04 --> 2431.24]  off. But maintenance is a burden. One that I still run to this day for my business is Airbit,
[2431.56 --> 2439.72]  which is a self hosted version of like Airbrake for error reporting. And it's just on Heroku and
[2439.72 --> 2446.92]  it's they do their best. And it's a great project. And I love it. But I still have to like update it.
[2446.92 --> 2451.40]  And I'm always afraid it's on MongoDB, which I'm not as familiar with from a maintenance perspective.
[2451.40 --> 2456.28]  And I'm just always afraid that this next time when they do a release and I, you know,
[2456.28 --> 2461.96]  pull that tag down and push it out to Heroku, all hell's going to break loose and now my reporting
[2461.96 --> 2468.92]  system's broken. What measures have you taken to make deployment easy and just like that idea of
[2468.92 --> 2475.64]  not letting it die on the vine, like keeping up with the Huguen Joneses as a user? Have you guys
[2475.64 --> 2481.08]  struggled with that? And what have you done to make it so that people can deploy and not feel like,
[2481.08 --> 2486.20]  it's a huge burden? That's a great question. It's a hard problem because, you know,
[2486.84 --> 2494.60]  most people haven't deployed a Rails application before. And that's not trivial. Until fairly recently,
[2494.60 --> 2501.24]  we didn't have a great solution. We had tutorials on how to deploy a Rails app with Capistrano. And we had
[2501.24 --> 2506.52]  example Capistrano scripts and example, you know, Nginx proxy scripts, but you know,
[2506.52 --> 2510.20]  it was really for a pretty small set of people who were comfortable doing that.
[2510.20 --> 2517.24]  Recently, we've wrapped it in a Docker container and that's definitely helped. So now you can use
[2517.24 --> 2523.32]  Huguen with Docker. As long as you link it to an external data source, either Postgres or MySQL,
[2523.88 --> 2528.76]  in another Docker container, then it's trivial to just sort of re-download the new one and launch it,
[2528.76 --> 2535.08]  and it should be fine. We definitely make an effort to not break agents in a backwards incompatible way.
[2535.08 --> 2540.12]  So when you upgrade that, we really try to make sure that the options that your agent has will
[2540.12 --> 2547.24]  still work. And we write migrations if necessary to make sure that happens. I don't think we've ever
[2547.24 --> 2552.20]  broken people in a backwards incompatible way, except for, you know, I don't think we've ever like had
[2552.20 --> 2556.28]  data loss issues where we've really broken people with an upgrade. Obviously, there have been bugs that
[2556.28 --> 2562.20]  have been introduced. It is, you know, an open source project. It's all volunteer. It does break
[2562.20 --> 2569.48]  sometimes, but overall it's been pretty stable. And I've tried to make very conservative technical
[2569.48 --> 2576.52]  choices. You know, we haven't gone very far from traditional Rails. We, you know, I've resisted
[2576.52 --> 2581.96]  pulling in new dependencies like Redis or Mongo, even though, especially with Redis, I'm a fan, but I just
[2581.96 --> 2588.28]  don't want people to have to deploy another component. It works with Postgres or MySQL and we want to just
[2588.28 --> 2594.76]  keep it stable with whatever you have running. And, you know, the trade-off is that it's then a little
[2594.76 --> 2600.44]  hard to make it high throughput and like really performant if someone's trying to build a system around it.
[2601.96 --> 2607.08]  We have a few users who have really pushed it to its limits with tens of thousands of agents running
[2607.08 --> 2614.12]  really, really frequently and monitoring all very complicated flows. I've never had a need to push it that far.
[2614.44 --> 2617.00]  They start to run into issues where they're, you know,
[2617.48 --> 2623.64]  extending their database, which is too small or the system isn't high throughput enough. But for the most part,
[2623.64 --> 2627.24]  for the types of tasks that I've always wanted to use it for, which is personal automation
[2628.04 --> 2633.96]  or sort of small-scale business automation, it's it holds up pretty well and it's not too difficult to deploy.
[2633.96 --> 2636.36]  You can also push it to Heroku.
[2637.88 --> 2638.52]  Deploy button.
[2639.88 --> 2647.64]  I think, yeah. So that and that works last time I checked. And so a bunch of people run it there as well.
[2647.64 --> 2655.56]  Heroku's restructuring of their pricing strategy has limited the way people deploy hobby tooling to Heroku,
[2655.56 --> 2658.60]  right? Because it's that can only be on for 18 hours.
[2658.60 --> 2665.24]  That's right. And Huguen is intended to run all the time. So that did affect a lot of our users.
[2667.08 --> 2672.52]  But if you upgrade to their first plan, it's not too expensive and it does run. It runs fine at the base plan.
[2673.96 --> 2678.04]  Also runs fine on a, you know, a $5 digital ocean image or something like that.
[2678.04 --> 2683.48]  Exactly. So I mentioned keeping up with the Joneses and I was just checking out your gem file
[2684.68 --> 2690.60]  previous to the call and you appear to be on the most recent version of Rails 4.
[2692.04 --> 2696.12]  All projects that have lived multiple years, you know, go through different versions of Rails,
[2696.12 --> 2700.04]  all your dependencies. It is a complicated enough application that your gem files,
[2700.76 --> 2706.52]  you know, got 100 plus lines in it. I'm not sure exactly how many gems are loaded on a regular basis,
[2706.52 --> 2709.88]  but you do have a, even though you're trying to keep it simple, you still have a pretty
[2710.92 --> 2716.52]  rich dependency graph. Can you explain any trials and tribulations over the years of just
[2717.16 --> 2722.36]  maintaining it, keeping it up to date, security patches? Has that been a struggle for you or has
[2722.36 --> 2728.68]  it been pretty smooth? It's, I mean, it's not trivial, but because we're fairly traditional Rails,
[2728.68 --> 2734.76]  the Rails upgrades themselves have not been particularly hard. Sometimes the dependencies are a little more
[2734.76 --> 2740.52]  complicated and we've always toyed with the idea of pulling agents into gems so that you can pick and
[2740.52 --> 2746.92]  choose exactly which ones you want. About two years ago, we refactored the gem file so you can turn a
[2746.92 --> 2751.64]  bunch of gems off and the agents gracefully just sort of disable themselves. So if you're trying to run
[2751.64 --> 2758.04]  this on like a Raspberry Pi, which sort of barely works, you can turn a bunch of stuff off that you don't
[2758.04 --> 2764.36]  need just to reduce your overhead. And that works fairly well. It's always been this trade-off between
[2764.36 --> 2770.44]  I really have resisted pulling everything into gems, even though it has a sort of structural elegance,
[2771.00 --> 2777.40]  because right now it's sort of the polished monolith where if we make a change to the system,
[2777.40 --> 2782.92]  we could update all the agents simultaneously in one commit and it's going to work. If everything's in
[2782.92 --> 2788.12]  gems, then we end up in sort of version management hell where we need to either own all the gems and
[2788.12 --> 2793.32]  update them all ourselves, or if they're owned by third parties, we have to send them a pull request or
[2793.32 --> 2798.84]  ask nicely. And I think it's just, I've been resistant to having to manage that. It's a little
[2798.84 --> 2804.76]  bit like my experience in the DevOps world between Chef and Ansible, where Ansible shifts with this really
[2804.76 --> 2810.84]  rich standard library. My experience has been that when we moved to Ansible, we got to stop using all
[2810.84 --> 2815.32]  these community supported things that didn't work super well from Chef and just use the core library
[2815.32 --> 2821.40]  that was updated in lockstep with Ansible itself. And it was just much more stable. So that's sort of
[2821.40 --> 2826.84]  where I'm trying to keep it. It does limit people's ability if I don't accept a pull request, because
[2826.84 --> 2830.84]  the agent brings in a lot of new dependencies that I don't think people are going to, most of the
[2830.84 --> 2836.84]  population isn't going to want. It makes it hard for people to get that. They could obviously use a fork,
[2836.84 --> 2841.80]  but if it were in gems, it would be really easy for people to just add exactly which they want.
[2841.80 --> 2845.96]  So there's a real trade off. You might even call it a majestic monolith.
[2848.12 --> 2849.72]  I heard that term recently. I think we all heard it.
[2851.56 --> 2858.04]  Let me pose this question to you, because I'm looking at the MIT license. I'm seeing the years of
[2858.04 --> 2863.24]  work that's gone into this. And it obviously is working quite well. You have many people using it.
[2863.24 --> 2867.32]  And you mentioned that some people have come around and push it to certain limits,
[2867.32 --> 2871.40]  you know, with whether it's the number of agents they run or how often they check or the
[2871.40 --> 2876.76]  the types of things that they are doing. Have you ever considered the possibility of
[2877.48 --> 2884.28]  somebody coming by and saying, this is really nice as a basis for my new company. And I'm going to
[2884.28 --> 2889.88]  take Hugin. I'm going to wrap it with a new shiny new UI. And I'm going to start,
[2889.88 --> 2897.00]  you know, some new company, Inc. Is that something that you've thought about? Is that something that
[2897.00 --> 2898.44]  scares you? What are your thoughts on that?
[2900.04 --> 2906.04]  I would be totally fine with that. I kind of hope it happens. I think, yeah, I think that
[2906.92 --> 2913.08]  it would be great if there's a population of the user of my users who grudgingly run a Rails app,
[2913.08 --> 2918.76]  but don't really want to. But they love the power of Hugin because it is in a lot of ways more powerful
[2918.76 --> 2923.40]  than if this and that or Zapier, because both of those, you can't chain multiple agents together
[2923.40 --> 2927.96]  through a deep flow. As far as I know, I haven't used either in about six months. But
[2930.44 --> 2936.12]  so Hugin can do some very powerful sort of flows of agents that you can't necessarily do somewhere
[2936.12 --> 2940.60]  else. And you also can extend it. So there's a population of people who would love to use it,
[2940.60 --> 2944.60]  but don't really know how to run a Rails app and don't really want to use Docker and just want to
[2944.60 --> 2950.12]  use Hugin. And I've been hesitant to start a business around it because I don't think it's a
[2950.12 --> 2954.68]  huge business. And I don't particularly want to be in the hosting business myself.
[2956.52 --> 2962.44]  So although I am still slowly considering it, but if someone wants to take Hugin and build a product
[2962.44 --> 2967.48]  around it, and I'm aware of a couple of people who have been doing that, I'm totally fine with that.
[2967.48 --> 2972.60]  That's great. More users, more contributions. I mean, it would be awesome if they contribute back
[2972.60 --> 2978.12]  some of their work, which is likely if they want to get the goodwill of the community. So I think
[2978.12 --> 2984.12]  that would be great. Awesome. Let's talk about your community. There's lots of open source projects
[2984.12 --> 2989.80]  out there and there's only so much limelight. You have Selector Gadget, which had a little bit of
[2989.80 --> 2995.40]  limelight, but like you said, never gained major traction. Hugin seems like it's got the traction.
[2996.84 --> 3001.88]  It's a lot of people active, 110 contributors. Like I said, 13,000 stars. People are using it.
[3001.88 --> 3009.72]  New York Times is using it or has used it. Take us back to the launch and the initial reception,
[3009.72 --> 3017.44]  or if you had any delusions of grandeur, or if you had a marketing idea, like how did it get traction?
[3017.44 --> 3023.12]  So very similar to other projects that I've launched that eventually sort of got attention.
[3023.12 --> 3030.16]  Hugin didn't get any attention when I initially released it. I wrote it and I put it, I think I
[3030.16 --> 3037.20]  posted on Hacker News in March of 2013, or a little earlier actually. I think it was in like December of
[3037.20 --> 3043.36]  2013 maybe, or of 2012. And you know, got like two stars or something like that on Hacker News. It
[3043.36 --> 3048.56]  wasn't, no one cared. But that's the exact same pattern that I followed on other projects. My
[3048.56 --> 3053.28]  Freebie Finder site that I built in high school, I posted it at that point. I don't think Hacker
[3053.28 --> 3059.04]  News existed. It was Dig. Dig was what everyone cared about. Yeah. So I posted on Dig and it didn't go
[3059.04 --> 3066.08]  anywhere. And then I'm like, well, that sucks. And then a month or two later, I reposted on Dig,
[3066.08 --> 3072.88]  talked some friends into voting it up. And it got, you know, thousands of digs, I guess, and got really popular.
[3073.36 --> 3077.36]  So, you know, Hugin had a somewhat similar trajectory where I posted it, no one cared.
[3078.08 --> 3082.88]  I posted it again. I don't think I, you know, both schemed in this case. I think I just posted
[3082.88 --> 3088.56]  it again in March of 2013. That time, for whatever reason, you know, it got to the front page.
[3090.48 --> 3097.84]  Stayed there for a while, got some users at that point. And then I may have reposted it. I know it
[3097.84 --> 3102.56]  was on Hacker News again in 2014, and I don't remember whether I posted it or if someone else did.
[3102.56 --> 3107.28]  And then it actually was on Hacker News again to the front page last month. And I definitely
[3107.28 --> 3112.72]  didn't post it then. Someone else did. So, you know, it keeps, I feel like every couple of years,
[3112.72 --> 3117.04]  it gets rediscovered and another wave of users and contributors shows up.
[3118.96 --> 3123.36]  Again, also with Yahoo Pipes closing down, there was a, there was a blog post that talked about it.
[3123.36 --> 3129.92]  And, you know, I've always made a real effort to write good read me's and to sort of invite people
[3129.92 --> 3134.80]  in and say, hey, this is, everyone's welcome. And here's all the cool things you can do with this
[3134.80 --> 3140.80]  project. And we'd love to see what you do with it and to have an approachable read me. And that's
[3140.80 --> 3143.12]  always served me well, just like making it approachable.
[3143.12 --> 3150.24]  Yeah, I would just say, I think this last round of Hacker News coverage was probably what spawned
[3150.24 --> 3156.32]  this show because you can head cross my radar previously. And actually 2012 was probably peak
[3156.32 --> 3160.80]  Hacker News for me. So I may have been your one at one of your two upvotes there. I was living on the
[3160.80 --> 3170.96]  website back then. Don't check it quite so often nowadays, but, but people do. And I think it started
[3170.96 --> 3177.28]  getting tweeted about again and somebody mentioned it on our ping repo and another person emailed us.
[3177.84 --> 3181.60]  And so it was kind of like these things just kind of bubble up. And I guess if you, if you're
[3181.60 --> 3186.32]  interesting enough and you stick with it because you have been working on it, it seems like maybe
[3186.32 --> 3192.80]  not nonstop, but in a committed way for a few years is you just kind of get these different rounds of
[3192.80 --> 3197.92]  attention. Yeah, that's, that's exactly what I've observed. And that's been true on multiple
[3197.92 --> 3202.32]  projects is, you know, it's a little hard to predict when, when people are going to care.
[3202.32 --> 3206.32]  And that as soon as a few people care and start talking about it, suddenly everyone notices and
[3206.32 --> 3212.88]  right, you know, everyone suddenly cares. And it also needed a certain critical mass of agents and
[3213.68 --> 3217.44]  scale, I think before it met enough use cases that people found it interesting.
[3217.44 --> 3221.44]  What does success look like for Hugen? Like if you can look five years down the road and said,
[3221.44 --> 3226.64]  wow, that was a huge success. What would happen between now and then that would make that the case?
[3226.64 --> 3233.68]  That's a good question. Um, you know, I've thought about trying to start a business around it,
[3233.68 --> 3238.08]  but I'm not moving in that direction right now. Um, you don't want to be in the hosting business.
[3238.88 --> 3242.72]  I don't really want to be on the hosting business and maybe I sort of have a blind spot,
[3242.72 --> 3248.32]  but I'm having trouble seeing a large enough business around it. I, you know, it's conceivable
[3248.32 --> 3253.28]  that there could be a pro version of Hugen that's worked well for like other open source projects.
[3253.28 --> 3258.96]  Right. Um, so I'm thinking about that. So that might be one, one definition of success,
[3258.96 --> 3264.40]  but I certainly haven't committed to that yet. Um, I think a more general definition would be,
[3264.40 --> 3268.96]  it still exists and it's still getting used and it's works. Um, I really, you know,
[3268.96 --> 3274.00]  you mentioned longevity earlier and I really care about sort of survivable software. One of the things,
[3274.00 --> 3279.52]  I want to build systems that I can build and slowly extend for many years and into something that
[3279.52 --> 3286.80]  meets my needs. Um, so no, I would be content if Hugen is just continuing to get used and get,
[3286.80 --> 3292.96]  it's continuing to solve problems for people. Yeah. I like that survivable software. Ooh,
[3293.60 --> 3299.76]  you go, you can go into marketing, right? That, that term. Um, so I think, I mean,
[3299.76 --> 3304.72]  business wise, just looking at it, um, you know, Metabase rings a bell, uh, with a recent show
[3304.72 --> 3311.76]  that we had in the open source slash product, uh, business. Um, and similar in certain ways,
[3311.76 --> 3317.12]  they're doing business intelligence or, you know, exposing data to more people, uh, in enterprises
[3317.12 --> 3323.04]  and small businesses. And it seems like what Hugen provides is an opportunity. It's so much information
[3324.16 --> 3328.08]  that people just don't even know that they need it. But if you show that to them,
[3329.04 --> 3332.48]  they read, they immediately see the value. Even myself, I look at this and think,
[3332.48 --> 3336.40]  oh, there's probably 10 things that I'm doing manually every week or that I'm not even doing
[3336.40 --> 3341.28]  at all because it require too much of my time. Um, that a product like this could,
[3342.88 --> 3346.08]  could solve for me. And then you take that times all the small businesses
[3346.64 --> 3351.76]  and people who actually can't write things themselves because I tend to be the kind of
[3351.76 --> 3356.24]  guy that's like, oh, I'll just write this little one-off script each time, you know, to my, to my shame.
[3356.96 --> 3359.84]  Um, but many people don't even have that ability. And it seems like,
[3359.84 --> 3362.24]  unless you want to take over the world, it seems like there'd be enough
[3362.48 --> 3367.20]  room for a, at least a small business. And I think there's a huge education side of that,
[3367.20 --> 3372.56]  which is expensive. Um, but maybe your, your Zapiers and your ifts are doing some of the
[3372.56 --> 3377.52]  education for, for you. Um, and so, yeah, I think there's a possibility.
[3377.52 --> 3382.48]  I think that's right. Yeah. Um, and I'm definitely thinking about it. That would be,
[3382.48 --> 3386.40]  that would certainly be an exciting outcome. And I know some of my other, um,
[3386.40 --> 3389.60]  core committers are definitely interested in that. So we'll see.
[3389.60 --> 3392.96]  Yeah. Tell me real quick, we're going to take a break, but tell me about your other core
[3392.96 --> 3398.56]  committers. Uh, one thing that leads to survivable software or longevity or sustainability and project
[3398.56 --> 3402.64]  is not having to do all the work yourself. And it seems like you have some people who are,
[3403.52 --> 3408.40]  um, right up there. In fact, one fella has more commits than you nowadays or total,
[3408.40 --> 3413.04]  even though I think you have more lines of code committed, but, uh, how did you get these other
[3413.04 --> 3417.52]  contributors and how much have they meant to you? They've been incredibly important. I mean,
[3417.52 --> 3423.76]  it's been a team effort. Dominic and Akinori have been written a huge amount of code. Um,
[3423.76 --> 3428.56]  especially Dominic has recently has been, he did all of the Docker work and he's been contributing
[3428.56 --> 3435.20]  really important changes around how we handle files, which are upcoming. Um, in his case, I,
[3436.16 --> 3440.96]  I'm not entirely sure how Dominic first found Hugin. He definitely sent some early pull requests
[3441.60 --> 3447.84]  and clearly knew what he was doing. And, um, I invited him to be a, uh, committer if he would
[3447.84 --> 3454.72]  like to be. And, and he joined and then the same with Akinori. Um, he made some really important early
[3454.72 --> 3459.04]  changes. He's been a little less active recently. I think he's busy on his own projects, but, uh,
[3459.04 --> 3464.64]  he's certainly around. Um, and then we have a couple other less active committers who show up
[3464.64 --> 3469.20]  occasionally and do documentation or help with some Docker stuff. And we're always looking for more.
[3469.20 --> 3474.00]  I mean, really all I'm, I'm just sort of keeping an eye on pull requests. And if I start to see the
[3474.00 --> 3480.16]  same person submit a few well-tested, well-written pull requests, I make an offer. Um, because you
[3480.16 --> 3484.32]  know, the more the merrier. It's definitely, I completely agree with you that we need to spread out the
[3484.32 --> 3490.88]  load. Cool. Well, let's, uh, let's pause here for our final break and we will be right back.
[3492.32 --> 3496.56]  Here at the change law, we have two emails. We'd love for you to subscribe to the first
[3496.56 --> 3500.64]  is change law weekly. And we've been shipping this email for several years. Now we ship it
[3500.64 --> 3506.08]  every single Saturday morning. It's everything that hits our open source radar. It's our editorialized
[3506.08 --> 3512.16]  take on what happened this week in open source and software development, go to change law.com
[3512.16 --> 3517.52]  slash weekly to subscribe. And our second email is changed all nightly. Every single night we ship
[3517.52 --> 3525.28]  this email out covering all the top new and top star repos on GitHub at 10 PM central time. It's all
[3525.28 --> 3530.96]  the latest stuff on GitHub before it blows up. It's often our own radar. We're often creating shows and
[3530.96 --> 3535.52]  finding new people, finding new projects, putting things on our own radar based on what we find in
[3535.52 --> 3541.04]  there. So we'd love for you to subscribe to that head to change law.com slash nightly. And now back to the show.
[3542.16 --> 3550.80]  All right, we are back with Andrew Cantino talking about Hugin. Let's talk about the roadmap. What's
[3550.80 --> 3555.76]  in the immediate future? You mentioned you've had a lot of help with one of your contributors
[3555.76 --> 3560.72]  working on how you're going to deal with files, which I imagine is tricky and a large feature.
[3560.72 --> 3564.08]  Can you tell us about that and about other things that are coming down the pipeline?
[3564.08 --> 3571.52]  Sure. So the file stuff has been entirely Dominic. He's been figuring out sort of how he wants to
[3571.52 --> 3577.68]  handle it. The current plan is to use sort of the concept of a file pointer. So events are JSON
[3577.68 --> 3583.84]  objects that flow between agents, and they're basically schema-less. So he's introducing, you know,
[3583.84 --> 3589.28]  a little bit of schema where if you declare a file point, you annotate your agent as emitting file
[3589.28 --> 3594.88]  pointers, then we can look in the event for, I think that's just called file pointer, which will
[3594.88 --> 3602.08]  be a reference to either a remote S3 object or a local file object, or I think there's a third case.
[3602.08 --> 3606.64]  I think you could just put the raw, you know, binary or text data if it's small right in the event.
[3607.28 --> 3613.84]  And then agents that know how to receive that, like a CSV parsing agent or a file pending agent,
[3613.84 --> 3617.68]  can receive that and do things with it. So I'll be interested to see how...
[3617.68 --> 3621.68]  So reading files and writing files, kind of two separate things, but they interplay because...
[3622.80 --> 3626.00]  Would that play into an import and export type of an idea as well?
[3627.44 --> 3629.20]  Are you referring to between systems?
[3629.20 --> 3632.72]  Yeah, I was thinking between systems, but I guess you're thinking between agents?
[3634.24 --> 3639.20]  Yeah, well, or between systems, because a lot of people use Hugen to, you know, when I post on Facebook,
[3639.20 --> 3645.36]  post on Twitter, that kind of thing. And there's often a request for, and please move my photos.
[3645.36 --> 3647.68]  And that's not something we really can do very well right now.
[3649.20 --> 3652.80]  Also, often people are running Hugen in an environment where they can't write files locally,
[3652.80 --> 3660.88]  you know, Heroku or Docker. And so we need to make sure that you can do things like S3 or remote blob stores.
[3660.88 --> 3665.84]  So then you could even do like timed or event-based backups or something like that.
[3665.84 --> 3672.00]  Yeah, that would be interesting. You certainly could fetch a photo on a schedule and do something with it.
[3672.00 --> 3675.44]  You know, make a, I don't know, make a time lapse or something would be cool.
[3675.44 --> 3680.32]  Yeah. What else you got? So files, I think that sounds like it opens up a world of possibilities.
[3681.12 --> 3687.28]  Anything else that you guys definitely want to get done in the next, you know, six months, a year that you're thinking about?
[3687.28 --> 3695.52]  I think the two most important next steps for us are extending this concept to what's called a scenario.
[3695.52 --> 3700.16]  I haven't mentioned it yet, but you can take your agents and basically tag them with a label.
[3700.16 --> 3707.44]  We call it a scenario. And then you can export them and hand someone else a JSON file, which has a set of configured agents in it.
[3707.44 --> 3716.00]  And they can import it and use it. And then one of the cool things is you can actually peer to peer subscribe to their scenario from your Huguen instance.
[3716.48 --> 3726.64]  And if you click the update button, it'll go fetch the embedded URL for their scenario on their system, assuming it's public, and do a diff and merge it into yours.
[3726.64 --> 3733.20]  So you can actually sort of subscribe to other people's agents and scenarios, which are basically just collections of agents.
[3733.20 --> 3748.96]  The next step for that that would really make it much more powerful would be to variabilize it so that you can have a set of options that you fill out when you first subscribe to a scenario, such as your API key for something that you know, something that isn't embedded already in the options of those agents.
[3748.96 --> 3753.58]  Or your, you know, your personal location preference or something like that.
[3753.84 --> 3757.88]  Right now, you could do it by editing the options of the agents once they've come in.
[3757.98 --> 3768.40]  And that mostly works, but it would be really cool to make a library of these, which leads to the second thing that we really need, which is a community site to share these scenarios.
[3769.06 --> 3776.64]  Yeah, that was where I was just waiting for my turn to talk because I would have said, you know, where's your HQ or your place where people can just share their agents.
[3776.64 --> 3781.82]  And I love that you'd be able to just like merge your own fields into one you're subscribed to.
[3781.88 --> 3786.24]  It'd be super powerful and actually kind of necessary if you're going to have that kind of sharing going on.
[3786.98 --> 3790.58]  Here's a random question that may seem off topic, but here we go anyways.
[3791.36 --> 3799.02]  How do you guys deal with like expiring auth tokens when you're doing agent or like background based tasks?
[3799.02 --> 3807.14]  Lots of times like an OAuth token will expire and then usually like a user would have to get involved and refresh their browser or do the redirect flow again.
[3807.82 --> 3809.74]  What does it do in those situations?
[3810.92 --> 3812.24]  So it depends on the system.
[3812.40 --> 3819.82]  We use Omnioff embedded in Rails to manage the actual request for the OAuth2 token.
[3819.82 --> 3823.06]  And then it depends on the system.
[3823.18 --> 3825.82]  So for example, Twitter and Dropbox, I've never seen them expire.
[3826.32 --> 3828.28]  I think they have perpetual access tokens.
[3829.32 --> 3835.16]  Facebook definitely expires after it might be a month, it might be a couple months, and they don't offer refresh tokens.
[3835.34 --> 3836.58]  So you do need to get involved.
[3836.76 --> 3837.48]  It will just break.
[3838.34 --> 3840.38]  Agents have a concept of whether or not they're working.
[3840.38 --> 3845.28]  So they'll turn red if whatever that means for the agent.
[3845.58 --> 3850.46]  Often it means they've successfully received an event or successfully created an event in a certain time window.
[3851.50 --> 3853.34]  They'll turn red and then you can update them.
[3853.44 --> 3855.68]  They also have a log of their own errors.
[3856.50 --> 3858.14]  Are there agents that watch the agents?
[3859.46 --> 3861.78]  Yeah, there's agents that can control their agency.
[3861.96 --> 3864.40]  They're reconfiguring them or checking if they're working.
[3864.40 --> 3868.50]  Or notify you that you need to come back and fix this thing.
[3869.72 --> 3869.88]  Yeah.
[3870.74 --> 3871.14]  Cool.
[3871.28 --> 3872.36]  So that's Roadmap.
[3872.42 --> 3872.92]  You've got files.
[3873.02 --> 3873.84]  You've got the community stuff.
[3873.90 --> 3875.60]  Anything else you want to mention before we move on?
[3877.24 --> 3881.90]  I think the community site's the really big one where we certainly could use help if someone wanted to get involved.
[3882.86 --> 3884.28]  It's its own chunk of work.
[3884.36 --> 3895.80]  And it would be really exciting if it was tied back in some way to the core Hugen system so that you could either preview the networks of agents or, you know, have conversations about them and how they work.
[3895.80 --> 3909.06]  And it would be even more interesting if it was distributed so that, you know, if I run, much like Hotline, which I mentioned earlier, if I run a tracker and it knows about a bunch of scenarios, someone else could replicate it with a feed and run their own.
[3909.06 --> 3914.20]  And it would be a little bit, it would be decentralized at least a little bit so that we don't have to run a core one.
[3914.20 --> 3914.24]  Yeah.
[3914.24 --> 3915.98]  Or you could set up a commerce system.
[3916.12 --> 3919.78]  You could sell your agents and take you all the way back to the days of your Perl scripts.
[3920.40 --> 3922.84]  And you can go to put this around selling little scripts.
[3923.08 --> 3923.38]  It'd be awesome.
[3924.24 --> 3925.38]  But open source wins.
[3925.80 --> 3931.70]  So let's talk about roads to getting involved from two angles.
[3931.70 --> 3935.20]  First of all, what's the happiest path to becoming a Hugen user?
[3935.68 --> 3937.68]  So deploying my own instance and then setting it up.
[3938.26 --> 3943.86]  And then secondly, from the development side, if I want to get involved from that angle, where do I start and where do I go?
[3943.92 --> 3945.16]  So start with as a user.
[3946.54 --> 3952.78]  So if you're a user and you're not planning to develop on Hugen, I would recommend either Docker or Heroku.
[3953.58 --> 3954.76]  They both work quite well.
[3955.50 --> 3959.94]  If you are planning to develop on it, then you're going to want to make sure you have a local checkout and a fork.
[3959.94 --> 3962.10]  And it's not particularly hard to run locally.
[3962.94 --> 3970.70]  And then you're probably going to want to push your updates either with Capistrano or just pulling from your public or private fork of Hugen.
[3971.00 --> 3977.30]  And we have a pretty good tutorial that Dominic wrote about how to take any sort of base Linux system.
[3977.44 --> 3986.42]  I think Ubuntu and one or two others that he supports and just full instructions on how to get it set up to run Hugen as a Rails app,
[3986.42 --> 3989.90]  including monitoring and backups and stuff like that.
[3990.36 --> 3992.20]  But that's obviously fairly involved.
[3992.42 --> 3998.14]  And I wouldn't do that unless you're planning to also develop and want to make it really easy to push to your own instance.
[3999.22 --> 4000.46]  So what about once I get up and running?
[4000.74 --> 4004.50]  Now I'm going back to my thoughts on managing an install.
[4004.88 --> 4006.34]  And I'm on the Docker version.
[4007.14 --> 4010.16]  Do you guys have like specific releases that you do?
[4010.30 --> 4013.14]  Like when do I update my stuff?
[4013.56 --> 4015.00]  Like how does that work once I'm running?
[4015.10 --> 4016.80]  But I want to get your latest features.
[4018.12 --> 4021.06]  So we use the Docker Hub automatic builds.
[4021.22 --> 4024.04]  So whenever master gets updated, it updates the Docker build.
[4024.54 --> 4026.30]  And so you would just have to reprovision it.
[4028.36 --> 4031.20]  We don't really have a great versioning system.
[4031.60 --> 4036.34]  I've been meaning to figure out a good way to do versioning on top of a Rails application.
[4036.34 --> 4039.52]  But I don't feel like we have a good answer right now.
[4039.52 --> 4042.92]  We try really hard to keep master green and correct.
[4043.22 --> 4046.06]  And I think we 90% of the time, at least, that's true.
[4047.64 --> 4050.72]  You know, we have automated builds and automated Docker builds.
[4051.58 --> 4060.94]  But I think what most of our community does is just pull when they see a new interesting feature go across the changelog, so to speak, of, you know, our releases.
[4060.94 --> 4064.74]  And either they saw a pull request get merged or I update the changes file.
[4065.60 --> 4066.94]  And they want that change.
[4068.62 --> 4069.22]  Very good.
[4069.28 --> 4072.38]  Well, I guess that would probably lead us directly into our closing questions.
[4072.62 --> 4076.26]  And I'll just start with this one because it seems like you have a lot of needs.
[4076.46 --> 4079.68]  You're an open source project with a good group of contributors.
[4079.98 --> 4086.44]  But there's lots of fun things coming down the pipeline and lots of places where people can contribute in big ways.
[4086.44 --> 4099.68]  So with that in mind and with how you get going on development, if you were going to have a call to action for the open source community, if you're speaking directly to the community and they could help out in some way, what would you say to them?
[4101.76 --> 4102.98]  Well, I'd say welcome.
[4103.30 --> 4104.56]  We would love to have you.
[4106.02 --> 4111.02]  Huguen is really easy to get involved with because you can always add new agents, which are very modular.
[4111.02 --> 4116.38]  We just expect you to write, you know, one Ruby file for the agent and one Ruby file for the spec.
[4117.08 --> 4121.76]  And we're happy to help if you haven't done testing before to help you write your R spec.
[4123.40 --> 4128.46]  Beyond that, documentation and tutorials and updates to the wiki are very much appreciated.
[4128.64 --> 4130.02]  I think they're as important as code.
[4130.94 --> 4133.46]  And a bunch of issues have been tagged with help wanted.
[4133.88 --> 4139.84]  So if you're looking for an interesting project to work on, and we've had a number of people just show up, not convinced they'd ever used Huguen before,
[4139.84 --> 4142.02]  and just pick a help wanted issue and start working on it.
[4143.28 --> 4144.00]  That's great, too.
[4144.12 --> 4144.50]  I like that.
[4144.58 --> 4147.04]  So actually, you guys use GitHub issues, right?
[4147.76 --> 4152.42]  So in there, you actually have a label called help wanted, and you will tag specific issues with help wanted.
[4154.12 --> 4154.58]  That's right.
[4154.68 --> 4156.98]  And any issue people are welcome to get involved with.
[4157.10 --> 4158.08]  These are just ones that are...
[4158.08 --> 4159.30]  Like explicitly waiting for someone to pick them up.
[4159.34 --> 4160.64]  I think that's a good idea.
[4160.88 --> 4161.00]  Yeah.
[4162.32 --> 4163.50]  Ideally approachable, too.
[4163.56 --> 4167.50]  I try to tag ones that I feel like a fairly new user could sort of make progress on.
[4167.50 --> 4167.78]  Great.
[4167.84 --> 4173.04]  I think that's a great path to getting involved is go out there, check out the issues, and look for the help wanted label.
[4173.76 --> 4179.62]  Start picking them off, and then eventually you'll probably be ready to move past those into the more complex things.
[4181.80 --> 4182.32]  Very good.
[4182.36 --> 4186.50]  Well, let's move on to our second closing question, and this one is programming hero.
[4186.50 --> 4196.54]  So if you had to name somebody who has inspired you or mentored you or you look up to in the software community, who would that be and why?
[4197.60 --> 4200.42]  I think I would pick Jeremy Ashkenas.
[4201.20 --> 4205.00]  He created Backbone underscore CoffeeScript.
[4205.00 --> 4217.60]  He's just super prolific and has sort of built the backbone, perhaps, of modern JavaScript development.
[4217.76 --> 4225.24]  Backbone itself is great, and it's fun if you want to sort of have a small-scale component that's really stable and that you can rely on and build on.
[4225.24 --> 4232.32]  And then it's informed much of more modern, deeper applications like Ember.
[4233.76 --> 4238.52]  And then CoffeeScript as well had a huge influence on new JavaScript and was really formative.
[4239.06 --> 4241.80]  I'm very impressed with basically everything he's built.
[4242.50 --> 4244.00]  I'll get my aim in on that one.
[4244.20 --> 4245.44]  I'm a big fan of his as well.
[4245.44 --> 4255.64]  And he also seems to be traveling the world on a bike or something, which is inspiring as well and makes me quite envious.
[4256.72 --> 4262.80]  But very, as you said, prolific guy, very interesting stuff, and I'm actually interested in getting him on the show.
[4263.82 --> 4264.86]  Let's do the next one.
[4265.34 --> 4269.66]  So Hugin came across our open source radar again recently.
[4270.34 --> 4274.18]  We like to ask our guests what's on their open source radar.
[4274.18 --> 4280.56]  So what's something that either you haven't played with yet and you want to, or maybe you got a taste of it and you want some more?
[4280.66 --> 4288.30]  If you had a free weekend and you weren't working on Hugin, what was a project or a couple of them, if you have them, that are on your radar that you'd like to tell us about?
[4289.40 --> 4292.66]  Well, so I've started tinkering with Rust just starting.
[4293.08 --> 4296.92]  It's been interesting and very different than many languages I've used.
[4297.50 --> 4298.76]  So I've been enjoying that.
[4298.76 --> 4308.96]  And then it'll be a lot more than a weekend, but I'm starting to think about sort of conversational interfaces like Siri and Cortana and Google Now.
[4308.96 --> 4315.66]  And I really feel like there's the opportunity here for an open source project to be innovative there.
[4316.20 --> 4323.30]  Because I think Siri and Cortana and those tools are a lot like AOL before the internet.
[4323.52 --> 4329.88]  Like it's one company trying to catalog all the world's information, trying to catalog sort of all the things a user might want to do.
[4329.88 --> 4331.52]  And that's ridiculously long tail.
[4331.70 --> 4332.92]  And it just never seemed realistic.
[4334.32 --> 4341.84]  And I feel like, you know, AOL was replaced by HTTP and the open internet because it's the obvious answer to distribute the problem.
[4342.38 --> 4354.52]  And it seems like something like Siri would be better replaced by an open protocol route and where you route requests to appropriate agents on the open internet that can meet your needs and take actions for you.
[4355.24 --> 4357.38]  I don't think Hugin will evolve into that.
[4357.38 --> 4361.74]  I think it's a pretty different type of architecture, but it certainly got me thinking about it.
[4361.80 --> 4363.32]  I think there's something there.
[4363.44 --> 4367.38]  I feel like it's not going to be single company systems in 10 years.
[4367.50 --> 4368.46]  Yeah, I think that's interesting.
[4368.62 --> 4371.46]  I hadn't considered an open version of that.
[4371.58 --> 4384.66]  I feel like the barrier there is probably integration into the operating system and devices out there, which are, you know, things that you can work around, but would make it, you know, a challenge.
[4384.66 --> 4387.78]  The challenges are always good to get people using it.
[4389.90 --> 4390.60]  Yeah, I agree.
[4390.74 --> 4404.14]  I think somebody, I just, something was either in weekly, our weekly newsletter last week or we put it on Twitter, had an API into Alexa, which I think is Amazon's, you know, tool that drives the Echo and such products.
[4404.14 --> 4408.54]  And I think they at least are exposing that as an available API now.
[4408.96 --> 4410.80]  You can actually decide how it responds.
[4411.06 --> 4412.20]  So it's still a black box.
[4412.98 --> 4417.90]  But I imagine some interesting open source will be built around those kinds of things.
[4418.70 --> 4420.74]  Yeah, it's a really interesting problem space.
[4420.90 --> 4428.68]  I think that more and more interaction with computers is going to be conversational because for many types of things, you just want to talk to it the way you would talk to a person.
[4428.80 --> 4429.66]  Go solve this for me.
[4429.66 --> 4430.34]  Absolutely.
[4431.64 --> 4433.30]  Well, Andrew, thanks so much for joining us.
[4433.34 --> 4434.16]  This was a blast.
[4434.76 --> 4437.46]  You have got, you've piqued my interest.
[4438.04 --> 4445.32]  I might actually go and get this thing set up and put a few things in there and see how it goes despite my deployment fears.
[4447.08 --> 4447.70]  Good luck.
[4448.60 --> 4450.22]  I'm expecting some pull requests.
[4450.40 --> 4455.36]  I only do pull requests in anger, so you might have some of that going as well.
[4455.66 --> 4457.92]  But all feedback is good, I guess.
[4457.92 --> 4460.30]  But thanks so much for listening.
[4460.40 --> 4460.76]  Stay tuned.
[4460.84 --> 4462.76]  We have a bunch of great shows in the works.
[4463.02 --> 4465.82]  As we've been talking about, we are having Mats on soon.
[4466.44 --> 4467.96]  To talk 20 years of Ruby.
[4468.80 --> 4473.54]  Also, Raquel Velez and Sarah Chips of Jewelbots are all coming soon.
[4473.70 --> 4476.44]  So if you haven't subscribed yet, what's your problem?
[4476.56 --> 4478.88]  Hit that button and come back next week.
[4478.88 --> 4485.28]  We want to thank our sponsors this week, Codeship, Digital Ocean, Rollbar, and Truesight Pulse.
[4485.40 --> 4488.52]  And of course, we want to thank you, the listener, for sticking with us.
[4488.80 --> 4491.04]  We appreciate everybody who listens to our show.
[4491.76 --> 4493.40]  And until next time, we'll say goodbye.
[4493.40 --> 4494.82]  We'll be right back to you soon.
[4494.82 --> 4494.86]  Bye.
[4495.00 --> 4495.56]  We'll be right back.
[4495.70 --> 4495.82]  Bye.
[4495.92 --> 4496.02]  Bye.
[4496.64 --> 4496.72]  Bye.
[4496.72 --> 4497.20]  Bye.
[4497.38 --> 4501.62]  Bye.
[4505.80 --> 4505.86]  Bye.
[4505.98 --> 4513.72]  Bye.
[4513.88 --> 4514.18]  Bye.
[4516.06 --> 4516.26]  Bye.
[4516.32 --> 4517.26]  Bye.
[4519.42 --> 4523.26]  Bye.
[4523.26 --> 4553.24]  Thank you.
