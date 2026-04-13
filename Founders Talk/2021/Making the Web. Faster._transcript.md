[0.00 --> 6.90]  What's up? This is Founders Talk. I'm Adam Stachowiak, and here on Founders Talk, I share
[6.90 --> 12.78]  one-on-one conversations I have with founders, CEOs, and makers about their journey, their
[12.78 --> 17.46]  lessons learned, and what it takes to build and run their business. Today, I'm joined
[17.46 --> 22.18]  by Guillermo Rauch, founder and CEO of Vercel. We talk about building the Vercel platform
[22.18 --> 26.40]  and what it's taking to make the web faster and what's enabling Fernandez to do their
[26.40 --> 31.38]  best work, his framework for leading as a CEO, and how everything for Vercel is built
[31.38 --> 36.60]  on develop, preview, ship. Big thanks to our partners, Linode, Fastly, and LaunchDarkly.
[36.84 --> 42.24]  We love Linode. They keep it fast and simple. Get 100,000 credit at linode.com slash changelog.
[42.54 --> 47.72]  Our bandwidth is provided by Fastly. Learn more at fastly.com and get your feature flags
[47.72 --> 50.76]  powered by LaunchDarkly. Get a demo at launchdarkly.com.
[56.40 --> 62.80]  This episode is brought to you by Render. Render is a unified platform to build and run all your
[62.80 --> 69.26]  apps and websites with free SSL, a global CDN, private networks, and auto-deployers from Git.
[69.54 --> 74.34]  They handle everything from simple static sites to complex apps with dozens of microservices.
[75.06 --> 78.64]  There are a ton of use cases for Render, but the sweet spot I want to focus on right now
[78.64 --> 82.84]  is how they're able to offer a better, more streamlined approach to hosting modern apps
[82.84 --> 87.12]  at a better price point. For example, Heroku is known to be quite expensive at scale,
[87.46 --> 92.58]  and alternatives like AWS and Kubernetes require significant time and management overhead for
[92.58 --> 97.60]  early-stage startups. Render is built for modern applications and offers everything you need
[97.60 --> 104.36]  out of the box. One-click scaling, zero downtime deploys, built-in SSL, private networking,
[104.88 --> 109.40]  managed databases, secrets and configuration management, persistent block storage,
[109.40 --> 114.56]  and infrastructure as code. Render is powerful and it's easy to use. Automate your cloud hosting
[114.56 --> 119.34]  with Render at render.com slash changelog. The best part, our listeners get $100 in credit,
[119.66 --> 125.68]  and all that begins at render.com slash changelog. Again, render.com slash changelog.
[139.40 --> 145.26]  Guillermo, I've been so excited to get you on this show in particular. I know we've talked many times
[145.26 --> 151.62]  over your software career. I think five years ago, you actually came on the changelog with me,
[151.72 --> 156.68]  just solo, on 2.13, episode 2.13. This is early days of Zite, early days of,
[157.20 --> 161.32]  and it was brand new days of HyperTerm, for example, and then now, and we talked a lot about
[161.32 --> 167.00]  Zite and where you were at then, but it's been a while. We've been, you know, paying attention to what
[167.00 --> 170.86]  you're doing, and obviously, you know, I'm a big fan of your work and what you've been doing,
[171.24 --> 179.06]  spent time with you at Zite Days a couple years back, just really a big fan of your work. And so,
[179.16 --> 181.62]  I'm so glad to have you here on Finder's Talk. So, welcome.
[182.08 --> 186.02]  Thank you. I'm really happy to be here. You've been there since the very beginning, which is awesome.
[186.56 --> 192.04]  Yeah. I mean, some would say that the, you know, that the business, the changelog is
[192.04 --> 196.12]  an institution, and I feel like that's kind of true because we've been around for,
[196.74 --> 202.50]  as a business for 12 years, since 2009. I think we've just had timing, good luck, etc.,
[202.50 --> 207.14]  and the good fortune just to be there for so many awesome stories. And I think,
[207.46 --> 211.72]  you know, you have an interesting story because obviously, you know, your story better than I do,
[211.72 --> 216.58]  but you started to develop as a software developer very young. You started your entrepreneurship
[216.58 --> 220.50]  fairly young as well, from what I understand. And just like, I've been paying attention to what
[220.50 --> 225.76]  you've been doing for years. And it just seems like where you're at now as Vercel, as the company,
[225.84 --> 230.92]  and as an individual, is just layered on of like all these layers of what you've done and learned
[230.92 --> 235.74]  over the years. And you, you know, some people will like sort of like deplete their career capital,
[235.90 --> 240.50]  bank account, so to speak, you know, like start over somewhere else. It seems like you've just sort
[240.50 --> 246.88]  of like laser focused on like iteration over the years. How would you, how do you frame that? Is that
[246.88 --> 251.64]  true? And how do you frame that if it's true? Yeah, I think so. I think a lot of progress happens
[251.64 --> 258.56]  by building in layers or stages. So for me, going back to even the Mootools days, it felt like we're
[258.56 --> 264.14]  working on the foundations of, okay, JavaScript is going to be a very important part of our future.
[264.82 --> 270.68]  Let's build a layer on top of what came with JavaScript in the browser. Okay, now we have a
[270.68 --> 276.68]  library. Okay, let's build a layer on top. Obviously, we ended up settling on React as our
[276.68 --> 281.80]  engine, but okay, let's build a layer on top next. Okay, develop is part of a lifecycle.
[282.66 --> 288.74]  Vercel's motto is develop, preview, ship. Okay, so what's the next layer on top of that
[288.74 --> 294.08]  Next.js developer experience? Okay, it's previewing and collaborating with your team. Okay,
[294.08 --> 298.10]  what's the next layer on top? It's shipping to your customer. Okay, what's the next layer on top?
[298.10 --> 303.84]  Well, it's measuring that whatever you've shipped is performing for your customer. So we
[303.84 --> 310.76]  launched Next.js and Vercel Analytics. So it does feel like we're building in layers and it feels like
[310.76 --> 319.06]  a meaningful set of progressions. You know, the one thing I think about is just that path to being a
[319.06 --> 325.56]  founder. So many people will see somebody's success today, and they just don't know how they got there.
[325.56 --> 329.08]  You know, I'm talking about like everyone else who's paying attention to Vercel and to
[329.08 --> 333.74]  the hockey stick of Next.js, for example. And it's like all these fun things. They just think like,
[334.08 --> 339.58]  wow, they just, you know, they just arrived. And it's difficult to see all those iterations. Like
[339.58 --> 343.86]  you mentioned, mood tools and what's the next layer, develop, preview, ship, all those things that
[343.86 --> 350.04]  become the building blocks for Vercel as it is today. The easy question is, how did you begin,
[350.04 --> 356.46]  essentially? But like, when did you get that possibility of creating software and iterating
[356.46 --> 360.08]  software, but then building a business around it? When did that begin for you?
[360.64 --> 367.02]  I've always been intrigued by the concept of startups. My first startup was at a young age,
[367.26 --> 373.16]  even just going to school and trying to think about little businesses that I could do,
[373.16 --> 380.22]  even before I had any technical knowledge. I've always been intrigued with the idea of scalability,
[380.40 --> 386.20]  especially as I first arrived in the San Francisco Bay Area. Okay, not only can you build something,
[386.66 --> 392.98]  but that something can almost become an engine, a self-fulfilling prophecy in many ways. Because as you
[392.98 --> 397.96]  mentioned, once you hit a certain level of scale, there is that feeling of inevitability,
[397.96 --> 404.50]  or some people call it overnight success that comes with it. But the other thing is that it's
[404.50 --> 412.62]  always been for me about addressing pains that I felt myself in the past and scratching itches and
[412.62 --> 418.58]  trying to sort of unleash a lot of the potential that better tools and a better developer experience
[418.58 --> 425.10]  would create on the world. So starting a business, starting my own company was a very natural next
[425.10 --> 431.04]  step from there. I felt like I could empathize very strongly with the customer. I also believed
[431.04 --> 437.88]  in the customer. So I think there's an interesting story here. And so far, we're very focused on
[437.88 --> 446.26]  front-end developers. As Vercell evolves, the workloads that it's supporting are not just front-end.
[446.52 --> 451.48]  If your server rendering is at front-end or is that back-end? If you have an API page in X.JS,
[451.48 --> 457.54]  is that front-end or is the back-end? But the front-end developer defined as the person that
[457.54 --> 462.80]  is working on the UI layer, the person that's working right next to the layer that serves the
[462.80 --> 469.40]  customer, the person that's writing JavaScript or TypeScript, in many ways, it feels like we bet on
[469.40 --> 476.32]  them. We believed in them. Because going back many years, I would be confronted with the idea,
[476.46 --> 480.58]  well, does JavaScript make any sense? That's a toy. Brendan and I go and says,
[480.58 --> 487.20]  first, they said it couldn't work. Then we fixed it. Then they said it couldn't be fast.
[487.66 --> 493.26]  Then we fixed that too with V8, SpiderMonkey, and many other things. Then they said, I don't know,
[493.32 --> 500.64]  you cannot do things like native. Then we layered on WebAssembly. So we made a bet in that customer.
[500.64 --> 507.74]  We made a bet in that this set of tools would matter. And I think that bet worked out. And I think
[507.74 --> 512.06]  we're still in the early innings of that. Yeah. It's interesting to be in the early innings and be
[512.06 --> 520.10]  how many years? I want to say ZEIT was founded in 2015. So ZEIT is the previous name of your company,
[520.44 --> 526.68]  which is now called Vercel as of April, 2020. Well, that's six years, right? I mean, how can you be in
[526.68 --> 532.32]  the early innings six years deep? Well, that's the thing, right? I was just reading this incredible
[532.32 --> 539.82]  tweet about how old companies were when their most significant innovations came to market.
[540.42 --> 545.20]  You know, you look at the iPhone and these companies are like teenagers or young adults.
[545.68 --> 547.02]  They're decades old. I see.
[547.22 --> 553.70]  That really resonated, I think. Of course, we created NextChase a year in, right? So I think it was
[553.70 --> 562.62]  October 2016 that we published it. It still very much feels like it's a young project to us and how
[562.62 --> 568.16]  much we still have to accomplish in terms of making the web faster and making a better developer
[568.16 --> 573.86]  experience, et cetera, et cetera, et cetera. And at the same time, when we look at deploying
[573.86 --> 580.40]  edge computing and just making things more dynamic and instantaneous all over the world,
[580.40 --> 587.22]  very much in the early days as well. So these things are in many ways, infrastructure.
[587.60 --> 592.40]  I remember one time I used the word frontend infrastructure, which I borrowed from Facebook
[592.40 --> 596.50]  because the team that works on RIG is a frontend infrastructure team. And someone was like,
[596.58 --> 602.38]  wait, frontend requires infrastructure? So going back to that asymmetrical nature of the bet that we
[602.38 --> 607.02]  made, which is that, hey, these technologies are going to matter tremendously in the future.
[607.02 --> 613.18]  And, you know, along the way, there's been some developers or some CTOs or whatever that have
[613.18 --> 617.58]  been skeptical in the value of these technologies. But now it's become really clear that with Google,
[617.68 --> 623.36]  for example, ranking you by your core web vitals and performance and a lot of other innovations
[623.36 --> 629.32]  like TypeScript, like this is taking the world by storm. And that at the end of the day,
[629.32 --> 631.08]  we are still in the very early days.
[631.08 --> 637.70]  What's interesting about this focus of yours is this in the frontend, really, in that developer type,
[638.28 --> 644.32]  despite server side rendering or APIs skewing the line of frontend or not.
[644.44 --> 644.74]  Totally.
[644.96 --> 649.58]  Is this idea of a feedback loop, right? It's right there in your tagline, develop preview ship,
[649.74 --> 650.36]  right? For sure.
[650.42 --> 656.78]  That is a feedback loop. You develop an idea, right? You preview that. Does it meet what I think it
[656.78 --> 659.44]  should meet? Does it solve the customer's problems I think it should solve?
[659.44 --> 659.74]  Yep.
[659.74 --> 666.18]  Let's ship it and find out. And then rinse and repeat. That seems so easy. I mean,
[666.22 --> 671.58]  like it just seems so easy to think like that, but not everybody gets that idea. And I think you've
[671.58 --> 674.60]  been so focused on that for so long. It's astounding.
[675.12 --> 679.40]  Yeah. I think what's happening too. And the reason that frontend matters so much is that
[679.40 --> 688.04]  the complexity is significant, but the tools are getting so good, not just code tools, but low code
[688.04 --> 693.70]  and no code tools, which we support on the Vercel platform because we have a number of platforms
[693.70 --> 700.62]  that expose a GUI to this technologies underneath. So as I mentioned, it's turtles all the way down.
[701.06 --> 706.46]  We're seeing the rise of all these tools that compile down the Next.js and Vercel pages behind
[706.46 --> 713.90]  the scenes, but the end user is facing a GUI type interface or they're writing a notion document.
[714.62 --> 719.80]  And then all of a sudden they have a website that has been optimized for the best possible
[719.80 --> 724.32]  performance that hiring hundreds or thousands of developers would have gotten you.
[724.32 --> 731.00]  So really what we're seeing, and this is why frontend matters so much is this is where the value is.
[731.06 --> 739.86]  This is the cover letter. This is a presentation to your business, whether it's found through a Google
[739.86 --> 746.50]  search, whether it's found through an Instagram ad because you just launched your e-commerce business,
[746.98 --> 750.64]  whether it's invisible because of the power of APIs.
[750.64 --> 757.48]  We see so much traffic that is robot generated right today on the internet, but this is literally
[757.48 --> 765.38]  the entryway into everything. And I continue to think that the web will continue to become the
[765.38 --> 771.12]  entryway to everything. And that's the right bet to make, I think. And it's been super rewarding so far.
[771.76 --> 778.58]  This idea of no code, low code, you say you support it. What are your big idea thoughts on,
[778.58 --> 785.84]  I suppose, no code, low code today, 2021 to a few years from now? How is this going to change?
[785.88 --> 787.76]  Give me some sort of prediction. What are your thoughts?
[788.22 --> 796.96]  I think that we'll continue to coexist and thrive and ideally built in the same layer. So no code and
[796.96 --> 802.72]  low code have existed for years and years and years as years as throwaway strategies, right? Because
[802.72 --> 809.18]  you would start, you know, the changelow.com and it's just an idea. You want to put up a quick
[809.18 --> 815.72]  banner. GoDaddy would let you do this, like buy your domain and we'll host a very simple page for you
[815.72 --> 821.18]  that says that something awesome is coming. And you might use that because you just thought of the
[821.18 --> 822.86]  name. The changelow is an epic name.
[822.92 --> 823.48]  Keeps it easy.
[823.48 --> 828.82]  And you're like, wait, why am I going to sit down and develop? This thing is offering me to just
[828.82 --> 834.84]  write down a tagline. Boom. But later on, you're building a real business. You're concerned with
[834.84 --> 841.00]  appealing to your customer segment who is sensitive to, you know, design details and performance and
[841.00 --> 846.28]  they want an intuitive UI and you're adding dynamism that is coming from the data source of
[846.28 --> 850.40]  where you're publishing your audio files and descriptions and viewers and comments.
[850.40 --> 855.46]  So you throw away the no code load good thing. I think that's going to change quite dramatically
[855.46 --> 862.32]  in the next 10 years. I think you're not going to throw it away because the no code, low code and
[862.32 --> 867.86]  full code solution are going to build in the same front end infrastructure. We're starting to see this
[867.86 --> 875.92]  with platforms that understand react components and they build even on top of the rendering engine of
[875.92 --> 882.50]  the browser. So like, Hey, you're modifying and designing a component visually, or you're modifying
[882.50 --> 889.48]  and designing a section for an e-commerce store for a promotion. And you're part of the business team
[889.48 --> 896.50]  for a certain region of this e-commerce business. And you don't know the code, but you're reutilizing,
[896.76 --> 901.70]  remixing and working on top of the components that the front end developer team prepared
[901.70 --> 907.58]  in collaboration with the design team and accessibility experts to ensure that this
[907.58 --> 913.96]  component system represents the brand and performs well, and it looks good. So as these teams continue
[913.96 --> 919.58]  to collaborate more and more closely, which is basically a big theme for us is, you know, enabling
[919.58 --> 926.74]  everyone to collaborate on top of the web, not just, you know, the experts. So we're going to see that
[926.74 --> 932.74]  what you created visually, it's not going to be a temporary thing. It's going to eat more and more
[932.74 --> 939.14]  into different sections or pages, or even entire subdomains or entire domains of your business.
[939.28 --> 942.92]  It's not going to be the only thing, but it's definitely going to continue to grow.
[943.54 --> 948.86]  And if they share that infrastructure is going to be a non-regrettable decision for most companies.
[949.50 --> 953.36]  When you look at it from that lens, it's easier to see the bigger picture because I think people see
[953.36 --> 958.56]  it as a replacement and you sort of said they're different facets of the same thing and it's not
[958.56 --> 965.32]  going to replace it. And I think of like no code and low code options to say, you know, something
[965.32 --> 971.58]  super close to you with Next.js, for example, Next.js Live, that's an on-ramp. So when we talk about,
[971.58 --> 976.28]  you know, lowering the barrier of entry, which is one of your core principles, at least noted by your
[976.28 --> 981.56]  most recent round of funding, congratulations, by the way, here, just a few months back, $102 million
[981.56 --> 987.26]  Series C, big congrats on that. You put out three principles. You said that these are the promises
[987.26 --> 991.22]  we made with this investment we're going to do. You said build the SDK for the web, which is Next.js,
[991.86 --> 996.60]  lower the barrier of entry, which is essentially Next.js Live, and focus on the end user, which
[996.60 --> 1002.64]  essentially you've been doing your whole career. But when you put that kind of tool, Next.js Live
[1002.64 --> 1007.88]  out there and you put it out there in that way in a, in quotes, no code, low code scenario,
[1007.88 --> 1015.44]  what you're doing is you're, you're diversifying who can play in the game. Totally. Right. Because
[1015.44 --> 1021.94]  to be a software developer, it's so skewed. Almost everyone comes with this badge of imposter syndrome.
[1022.18 --> 1027.56]  I'm sure, you know, despite you being CEO of Resell and all your accomplishments, I'm sure
[1027.56 --> 1032.92]  that in the last week you've had imposter syndrome to some degree, maybe not massively,
[1033.06 --> 1037.50]  but maybe a little bit, maybe a lot, who knows? Point is, is that like, who is a developer?
[1037.96 --> 1041.64]  Yeah. I don't want to say you're not a developer, you are a developer, because why draw that line?
[1042.08 --> 1047.12]  Right. This discipline, essentially, this opportunity of no code, low code, and having that kind of
[1047.12 --> 1052.30]  foresight like you just played out is an on-ramp for so many who don't have a CS background or don't
[1052.30 --> 1057.34]  have, you know, in quotes, a real developer title or whatever it might be. It's an entry point.
[1057.56 --> 1058.28]  What do you think about that?
[1058.50 --> 1062.98]  Yeah. At the end of the day, I think a developer is anyone who develops anything.
[1063.64 --> 1071.12]  It's our responsibility as those who work on tools and infrastructure and guidelines even
[1071.12 --> 1076.10]  to ensure that anyone can develop. It's like anybody can cook and write a toolie.
[1076.10 --> 1086.56]  So Next.js Live for us is the first approach in terms of how quickly can you begin editing a site,
[1086.56 --> 1094.20]  right? How quickly can I make even a small contribution to a Next.js project? When you
[1094.20 --> 1101.34]  look at what it takes to just get started developing something that already exists, right? Like things
[1101.34 --> 1107.04]  that people have been already working on for years, just getting started on, okay, I want
[1107.04 --> 1111.00]  to make a quick change. I want to learn how it works. I want to understand what components
[1111.00 --> 1117.78]  are available in the system. It's a daunting task. In my blog post, I quoted Kelsey Hightower
[1117.78 --> 1123.38]  talking about like that weekend or that day that we're looking at helping someone learn
[1123.38 --> 1129.50]  programming. And the amount of time it took just to get the environment up and running was
[1129.50 --> 1139.68]  daunting. And it was eating into whatever cycles of creativity and willpower you had for the actual
[1139.68 --> 1145.24]  task of developing. So it's almost like in this industry, we have the work and then we have the
[1145.24 --> 1153.26]  meta work. Any second or minute or hour that goes into preparing your development environment is meta work.
[1153.82 --> 1161.26]  Every second you spend on improving the experience for your customers, adding new features, optimizing
[1161.26 --> 1167.44]  performance, reorganizing content, creating new content. That's the real work.
[1167.44 --> 1177.06]  Next.js Live will spin up a Next.js project, whether from a template or an existing one, in seconds.
[1177.66 --> 1183.60]  And it'll run all the tooling directly inside the web browser in a native fashion. It doesn't even
[1183.60 --> 1190.48]  require emulation. And on top of that, it layers on collaboration. So you can comment or point out
[1190.48 --> 1197.00]  things to folks in real time. You can even peer program with it because you can navigate a certain page
[1197.00 --> 1202.54]  and see, okay, like, what's the deal here with this problem or that problem. So I think this trend will
[1202.54 --> 1210.86]  continue in terms of blurring the lines between consumption and creation because the very web browser is able to do
[1210.86 --> 1216.98]  this, right? Like, this is an incredible thing about the web, right? The thing that you're using to consume is the
[1216.98 --> 1220.76]  same thing that you can use to create. That's unique. Yeah.
[1220.76 --> 1228.44]  That's what gets people going with the web. The browser has this hidden IDE if you do the right
[1228.44 --> 1231.98]  keyboard incantation, right? Yeah.
[1232.12 --> 1236.40]  Whereas you look at other platforms and it's just all about consumption.
[1237.12 --> 1242.08]  Or you look at the terminal and yeah, like all of that is about creation, but like, let's try to figure
[1242.08 --> 1247.02]  out, you know, how long it takes someone to get up and running with that. Downloading VSCO, downloading
[1247.02 --> 1254.20]  no, downloading this, downloading that. So we're very excited about where Next.js is headed, but also the web is
[1254.20 --> 1258.68]  headed and all these tools that are literally allowing everybody to develop.
[1259.34 --> 1265.94]  And we're seeing this movement happen. I mean, it's been a slow movement towards it. We see automation
[1265.94 --> 1274.66]  everywhere, essentially. We see it in infrastructure, build pipelines, all sorts of places. And recently, Codespaces
[1274.66 --> 1279.66]  was announced by GitHub. Gitpod's been out there for two years. They're open source. Would you say that
[1279.66 --> 1281.66]  Next.js Live is similar or
[1281.66 --> 1287.78]  in competition with them? You know, where do you place Next.js Live in comparison to say GitHub Codespaces
[1287.78 --> 1290.30]  or Gitpod or other
[1290.30 --> 1292.50]  essentially web IDE
[1292.50 --> 1294.22]  enabled things?
[1294.22 --> 1300.00]  Yeah. So the main distinction that I see that is a key component of Next.js's future
[1300.00 --> 1311.04]  is that we're using the browser as a platform, right? So Next.js Live doesn't require any VM running. It doesn't require a Linux
[1311.04 --> 1320.44]  operating system hidden somewhere in the cloud, which gives it major scalability. So the next billion developers could use
[1320.44 --> 1328.32]  Next.js Live and it will not need any additional resources other than their local computer, even offline. So that's a part of it.
[1328.32 --> 1333.64]  But the other thing is that Next.js is headed in this direction also towards edge execution.
[1334.28 --> 1338.84]  So when you want to server-side render your pages today,
[1339.36 --> 1342.64]  we're relying today on Linux as well to be sort of the
[1342.64 --> 1346.30]  under-the-hood operating system and hypervisor and so on.
[1346.82 --> 1350.80]  But we're kind of getting to the limits of what that technology can do in terms of performance,
[1350.92 --> 1354.72]  especially cold start performance in the serverless world where
[1354.72 --> 1357.04]  you know, you might go to a page that has not
[1357.04 --> 1359.72]  been booted very frequently or
[1360.28 --> 1364.42]  it's a new page that has just been created and we have the
[1364.42 --> 1367.28]  demand to render it dynamically
[1367.28 --> 1368.66]  instantaneously.
[1369.04 --> 1372.54]  So we're seeing is this symmetry also at the edge where
[1372.54 --> 1374.30]  browser APIs
[1374.30 --> 1380.64]  and V8 isolate style technology will be the one that will render your future pages as well.
[1380.64 --> 1383.20]  So in some ways is we're
[1383.20 --> 1386.70]  we're reconfiguring the cloud and just be web browsers everywhere.
[1387.30 --> 1389.10]  The development lifecycle
[1389.10 --> 1392.22]  happens in the browser or mostly in the browser.
[1392.40 --> 1395.18]  And then the edge execution
[1395.18 --> 1398.74]  is basically a cloud headless browser.
[1399.02 --> 1400.24]  You can imagine it that way
[1400.24 --> 1402.54]  that it's pre-rendering your page
[1402.54 --> 1405.64]  instead of putting that workload on the client device.
[1405.86 --> 1406.68]  That's profound.
[1406.68 --> 1410.62]  So Codespaces, I believe, uses VMs.
[1410.86 --> 1412.48]  Gitpod, I believe, uses containers.
[1413.10 --> 1417.98]  And Next.js is simply a headless browser to APIs, essentially.
[1418.48 --> 1419.96]  Yeah, it's just your web browser.
[1420.28 --> 1423.88]  So very much like how every page is already editable
[1423.88 --> 1426.04]  if you open the dev tools, right?
[1426.50 --> 1431.52]  There is no need with how awesome the web platform has gotten
[1431.52 --> 1435.96]  to actually require more technology than that.
[1435.96 --> 1438.70]  And it has this incredible advantage that
[1438.70 --> 1440.86]  we've arrived at the same realization
[1440.86 --> 1445.02]  when it comes to serverless and edge computing.
[1445.42 --> 1446.76]  We just need JavaScript
[1446.76 --> 1449.40]  plus some of the browser APIs
[1449.40 --> 1450.96]  to render your pages.
[1451.12 --> 1453.58]  And we gain massive efficiencies from that.
[1453.90 --> 1455.68]  So I think we're going to see this massive efficiencies
[1455.68 --> 1457.80]  happening for the cloud
[1457.80 --> 1459.94]  and for your own local development.
[1459.94 --> 1464.56]  You said that you started Next.js a year after founding Zite.
[1465.10 --> 1465.98]  So that's 2016.
[1466.96 --> 1468.88]  I think from my perspective,
[1468.88 --> 1471.04]  it seems like in the last several years,
[1471.04 --> 1474.06]  I've heard Next way more often than the years prior to that.
[1474.08 --> 1477.16]  And that's just maybe naturally how entropy works in the world
[1477.16 --> 1479.06]  or how scaling works with a product.
[1479.06 --> 1483.32]  But it seems like Next is used by just everyone.
[1483.32 --> 1487.46]  And it seems like it's Vercel's secret sauce
[1487.46 --> 1489.80]  to the scale you've reached.
[1490.32 --> 1491.98]  Not the only piece to the sauce,
[1492.08 --> 1493.56]  but a critical component
[1493.56 --> 1495.28]  to reaching the scale you've gotten to.
[1495.68 --> 1497.04]  Yeah, I would say that
[1497.04 --> 1500.12]  the cloud had developed itself
[1500.12 --> 1502.58]  in a very agnostic
[1502.58 --> 1506.56]  and unbundled way before, right?
[1506.78 --> 1509.52]  So you would hire AWS.
[1509.52 --> 1512.26]  I think this is even true for GitHub, right?
[1512.30 --> 1514.22]  And this is why Codespaces requires this
[1514.22 --> 1517.88]  very agnostic VM as well as its engine,
[1518.24 --> 1519.38]  because they tell you,
[1519.54 --> 1521.20]  you can do everything you want.
[1521.92 --> 1525.82]  So that increases the addressable space
[1525.82 --> 1528.34]  to lots of potential inputs
[1528.34 --> 1530.36]  and lots of potential outputs.
[1530.88 --> 1532.32]  I think what's interesting about Vercel
[1532.32 --> 1533.98]  is it's narrowing it down
[1533.98 --> 1537.28]  to the domain of literally publishing pages
[1537.28 --> 1538.84]  on the internet, right?
[1538.84 --> 1541.92]  And I think that DNA was right there in Next.js
[1541.92 --> 1543.04]  when we looked at React
[1543.04 --> 1544.28]  and we're like,
[1544.36 --> 1546.12]  okay, this is missing the pages folder.
[1546.38 --> 1548.48]  And it's missing the pages abstraction.
[1548.94 --> 1550.18]  Like, where's the page?
[1550.36 --> 1551.64]  We're building web pages here.
[1552.18 --> 1555.32]  And kind of the weird twist of fate
[1555.32 --> 1557.08]  of single page applications
[1557.08 --> 1558.98]  that eventually didn't pan out.
[1559.46 --> 1560.94]  But there was this perception
[1560.94 --> 1562.98]  that we're almost going to leave pages behind.
[1563.66 --> 1565.06]  The thing what's interesting about Vercel
[1565.06 --> 1567.90]  is that it's constrained the inputs further.
[1567.90 --> 1569.28]  It's saying, okay, you're building,
[1569.46 --> 1570.60]  you're developing pages
[1570.60 --> 1572.44]  and you're publishing pages.
[1572.44 --> 1574.30]  It turns out that, you know,
[1574.36 --> 1579.92]  that is akin to the addressable internet at large
[1579.92 --> 1581.68]  because there's just so many things
[1581.68 --> 1584.10]  that can be expressed with that abstraction.
[1584.46 --> 1587.42]  For example, when we introduced API routes,
[1588.12 --> 1590.08]  that is just simply create an API folder.
[1590.08 --> 1592.60]  And now every file in that folder
[1592.60 --> 1594.46]  becomes a service function
[1594.46 --> 1596.62]  that we run at the edge for you.
[1596.62 --> 1599.86]  So when we constrain those inputs,
[1600.14 --> 1600.70]  we're like, okay,
[1601.12 --> 1603.10]  the frameworks have to be frameworks
[1603.10 --> 1604.08]  that produce pages.
[1604.30 --> 1607.70]  So it's no longer arbitrary programming language
[1607.70 --> 1609.54]  that opens up a server
[1609.54 --> 1612.36]  and can do, you know, everything in there.
[1612.70 --> 1615.90]  It's Next.js or frameworks like it.
[1615.96 --> 1617.84]  So we're seeing a lot of success also with Nuxt
[1617.84 --> 1622.10]  and SvelteKit and newcomers into the space.
[1622.10 --> 1624.22]  So what happens next is that
[1624.22 --> 1625.68]  when you look at the preview phase,
[1626.14 --> 1628.18]  we built a build pipeline
[1628.18 --> 1630.50]  that also optimizes for this.
[1631.12 --> 1633.34]  So it's not that our build pipeline can't,
[1633.38 --> 1636.02]  for example, technically run tests
[1636.02 --> 1638.40]  or do other things that you would do,
[1638.48 --> 1641.78]  like build, you can't build Chromium in it.
[1641.92 --> 1643.70]  So we made a lot of automations
[1643.70 --> 1645.76]  and optimizations in the build pipeline
[1645.76 --> 1647.44]  for also that purpose.
[1647.44 --> 1651.36]  And our platform is well integrated
[1651.36 --> 1652.36]  into the frameworks.
[1652.98 --> 1654.46]  And then when it comes to shipping,
[1654.74 --> 1655.82]  we did the same thing again.
[1656.40 --> 1656.94]  So for example,
[1657.04 --> 1658.50]  something that happens
[1658.50 --> 1660.08]  when you ship to Vercel
[1660.08 --> 1663.20]  is that we can roll and revert
[1663.20 --> 1665.20]  without downtime instantly.
[1665.96 --> 1667.78]  I remember when I first saw containers,
[1667.96 --> 1669.04]  I also got excited,
[1669.50 --> 1672.52]  but then I looked at what reverting a server
[1672.52 --> 1676.04]  in the cutting edge Kubernetes experience was like.
[1676.04 --> 1677.24]  And it was like,
[1677.32 --> 1678.92]  I looked at companies,
[1679.02 --> 1680.24]  I looked at all the options
[1680.24 --> 1683.06]  and it was daunting and it was slow.
[1683.54 --> 1684.08]  I was like, whoa,
[1684.24 --> 1686.70]  but that's just reverting a set of pages
[1686.70 --> 1687.14]  on the internet.
[1687.22 --> 1688.32]  It cannot be that hard.
[1688.92 --> 1691.10]  It turns out that when we narrowed
[1691.10 --> 1693.62]  our addressable space in our domain,
[1694.02 --> 1695.72]  we found all this incredible,
[1696.50 --> 1697.96]  not just optimizations,
[1698.22 --> 1699.82]  but newfound powers
[1699.82 --> 1702.78]  and newfound efficiencies
[1702.78 --> 1704.08]  for our customers
[1704.08 --> 1706.24]  that now they take for granted,
[1706.36 --> 1706.84]  which is awesome.
[1717.28 --> 1718.74]  This episode of Founders Talk
[1718.74 --> 1720.18]  is brought to you by Auth0.
[1720.66 --> 1722.48]  Auth0 is a for developers,
[1722.64 --> 1724.12]  by developers identity platform
[1724.12 --> 1725.58]  built for the cloud era.
[1725.94 --> 1728.06]  They secure billions of logins every year.
[1728.42 --> 1729.74]  Identity is the front door
[1729.74 --> 1731.22]  of every user interaction
[1731.22 --> 1732.38]  and the login experience
[1732.38 --> 1733.46]  can make or break
[1733.46 --> 1734.74]  a user's first impression.
[1735.16 --> 1735.96]  Identity and authentication
[1735.96 --> 1738.02]  is never a set it and forget it thing.
[1738.38 --> 1739.40]  That means when teams decide
[1739.40 --> 1740.06]  to roll their own,
[1740.30 --> 1741.62]  they are taking on the full burden
[1741.62 --> 1742.80]  of constantly evolving
[1742.80 --> 1743.64]  industry standards,
[1743.92 --> 1744.72]  customer expectations,
[1745.02 --> 1746.00]  and data breach tactics.
[1746.26 --> 1747.56]  And they often don't have the time,
[1747.88 --> 1748.28]  expertise,
[1748.66 --> 1749.40]  or resources
[1749.40 --> 1750.56]  to meet those needs.
[1750.78 --> 1751.42]  This takes away
[1751.42 --> 1752.24]  from critical time needed
[1752.24 --> 1752.78]  to innovate
[1752.78 --> 1753.60]  and to improve
[1753.60 --> 1754.50]  their core product.
[1754.86 --> 1756.34]  Auth0 has solved this problem
[1756.34 --> 1757.18]  for every developer
[1757.18 --> 1758.90]  to give teams their time back
[1758.90 --> 1760.14]  and to make applications
[1760.14 --> 1761.02]  more secure.
[1761.42 --> 1762.58]  With Auth0 security,
[1762.80 --> 1763.26]  compliance,
[1763.74 --> 1764.66]  and industry standards,
[1764.80 --> 1766.16]  they're always up to date.
[1766.50 --> 1767.46]  Developers are free
[1767.46 --> 1768.08]  to provide
[1768.08 --> 1769.06]  the login options
[1769.06 --> 1769.92]  their users want
[1769.92 --> 1771.30]  with the security
[1771.30 --> 1772.78]  their application demands.
[1773.22 --> 1773.84]  Make login
[1773.84 --> 1774.70]  Auth0's problem,
[1774.80 --> 1775.26]  not yours.
[1775.82 --> 1777.50]  Learn more at Auth0.com.
[1777.76 --> 1779.54]  Again, Auth0.com.
[1780.06 --> 1781.06]  Auth0.com.
[1781.06 --> 1782.06]  Auth0.com.
[1782.06 --> 1783.06]  Auth0.com.
[1783.06 --> 1784.06]  Auth0.com.
[1784.06 --> 1785.06]  Auth0.com.
[1785.06 --> 1786.06]  Auth0.com.
[1786.06 --> 1787.06]  Auth0.com.
[1787.06 --> 1788.06]  Auth0.com.
[1788.90 --> 1789.90]  Auth0.com.
[1789.90 --> 1790.90]  Auth0.com.
[1790.90 --> 1791.90]  Auth0.com.
[1791.90 --> 1792.90]  Auth0.com.
[1792.90 --> 1793.90]  Auth0.com.
[1793.90 --> 1794.90]  Auth0.com.
[1794.90 --> 1795.90]  Auth0.com.
[1795.90 --> 1796.90]  Auth0.com.
[1796.90 --> 1797.40]  Auth0.com.
[1797.40 --> 1798.08]  One thing I see
[1798.08 --> 1799.34]  that is a trend line
[1799.34 --> 1799.78]  for you
[1799.78 --> 1801.36]  is your focus
[1801.36 --> 1803.12]  on the customer experience.
[1803.52 --> 1804.88]  I forget where I saw it,
[1804.90 --> 1805.62]  but I'm going to paraphrase
[1805.62 --> 1806.08]  what you said.
[1806.14 --> 1806.92]  You said that
[1806.92 --> 1807.70]  there's essentially
[1807.70 --> 1808.32]  two customers
[1808.32 --> 1809.14]  when it comes to
[1809.14 --> 1810.72]  the web or Versailles.
[1810.72 --> 1811.28]  I can't recall
[1811.28 --> 1812.36]  the exact context,
[1812.44 --> 1812.80]  but it was like
[1812.80 --> 1813.56]  the developer
[1813.56 --> 1814.92]  and then the thing
[1814.92 --> 1815.32]  the developer
[1815.32 --> 1816.68]  is making for the customer.
[1816.90 --> 1817.16]  Totally.
[1817.28 --> 1818.40]  And that your focus
[1818.40 --> 1819.20]  is not just simply
[1819.20 --> 1820.82]  on the dev experience
[1820.82 --> 1821.68]  and we hear this a lot
[1821.68 --> 1823.42]  like dev experience
[1823.42 --> 1824.16]  must be amazing,
[1824.30 --> 1824.66]  et cetera, et cetera.
[1824.74 --> 1825.72]  That's true for sure
[1825.72 --> 1826.68]  because you need to
[1826.68 --> 1827.94]  create a technology
[1827.94 --> 1829.32]  or a framework
[1829.32 --> 1830.20]  or a paradigm
[1830.20 --> 1831.60]  that can be adopted
[1831.60 --> 1832.66]  by software developers
[1832.66 --> 1834.04]  that can be understood,
[1834.22 --> 1834.82]  that can be taught,
[1834.90 --> 1835.48]  that can be,
[1836.04 --> 1836.30]  et cetera.
[1837.08 --> 1837.56]  But then
[1837.56 --> 1838.72]  the thing you make
[1838.72 --> 1839.92]  also has to be
[1839.92 --> 1840.94]  at the forefront,
[1841.08 --> 1841.90]  which is where I love
[1841.90 --> 1842.72]  your perspective.
[1842.72 --> 1844.44]  And this is kind of
[1844.44 --> 1844.94]  where I want to
[1844.94 --> 1846.02]  understand more so
[1846.02 --> 1847.00]  where you're at now
[1847.00 --> 1848.54]  CEO-wise
[1848.54 --> 1850.06]  to the originator
[1850.06 --> 1851.02]  of where a lot
[1851.02 --> 1852.26]  of where Versailles
[1852.26 --> 1852.80]  is at now
[1852.80 --> 1854.42]  because you started,
[1854.82 --> 1855.68]  I want to know more
[1855.68 --> 1856.74]  about how the company began,
[1856.82 --> 1857.58]  but where I'm trying
[1857.58 --> 1857.94]  to get to
[1857.94 --> 1858.74]  is your focus,
[1859.38 --> 1860.42]  your obsessive focus
[1860.42 --> 1861.56]  on not just
[1861.56 --> 1862.36]  the developer experience,
[1862.42 --> 1863.36]  but the customer experience
[1863.36 --> 1864.66]  that is the result
[1864.66 --> 1865.70]  of what the developers make.
[1866.38 --> 1866.80]  And so I kind of
[1866.80 --> 1867.42]  want to understand,
[1867.94 --> 1868.40]  one,
[1868.52 --> 1869.46]  help me dig
[1869.46 --> 1870.78]  and unpack that more so,
[1870.78 --> 1872.02]  but then from the lens
[1872.02 --> 1872.32]  of like,
[1872.38 --> 1872.72]  okay,
[1873.32 --> 1874.24]  back to the early days
[1874.24 --> 1874.58]  of Zite
[1874.58 --> 1875.14]  when it was called
[1875.14 --> 1876.30]  Zite and not Vercel,
[1877.02 --> 1878.18]  how you played a role
[1878.18 --> 1879.20]  in leading that
[1879.20 --> 1879.72]  and sort of
[1879.72 --> 1880.52]  where you're at now
[1880.52 --> 1881.08]  as a CEO,
[1881.26 --> 1881.98]  like how does your,
[1882.36 --> 1883.14]  how is your involvement
[1883.14 --> 1883.76]  in part today
[1883.76 --> 1884.62]  in comparison to say
[1884.62 --> 1885.60]  six years ago
[1885.60 --> 1886.14]  when you began,
[1886.22 --> 1886.64]  for example?
[1886.80 --> 1887.00]  For sure.
[1887.08 --> 1887.74]  Help me understand
[1887.74 --> 1888.82]  that obsessive focus
[1888.82 --> 1890.78]  and how you play
[1890.78 --> 1891.84]  the role day to day
[1891.84 --> 1893.10]  and maybe how you began.
[1893.58 --> 1893.96]  For sure.
[1894.44 --> 1895.42]  How we think about
[1895.42 --> 1896.06]  the company
[1896.06 --> 1897.06]  and its evolution
[1897.06 --> 1897.98]  actually relates
[1897.98 --> 1899.08]  very much to
[1899.08 --> 1900.24]  how we thought
[1900.24 --> 1900.66]  about
[1900.66 --> 1901.94]  designing Next.js
[1901.94 --> 1902.64]  in some ways
[1902.64 --> 1904.08]  because I remember
[1904.08 --> 1905.00]  when we introduced
[1905.00 --> 1906.18]  that concept of pages,
[1906.96 --> 1907.66]  one of the things
[1907.66 --> 1908.52]  that I remember
[1908.52 --> 1909.38]  telling folks
[1909.38 --> 1910.94]  is Next.js
[1910.94 --> 1913.76]  provides team scalability,
[1914.00 --> 1914.56]  I called it.
[1915.34 --> 1916.46]  We didn't stop at DX.
[1916.80 --> 1917.38]  In fact,
[1917.74 --> 1918.30]  the DX of
[1918.30 --> 1919.76]  single page applications
[1919.76 --> 1920.26]  in React
[1920.26 --> 1921.96]  was pretty darn great
[1921.96 --> 1922.76]  at the time.
[1923.20 --> 1924.52]  But I focused
[1924.52 --> 1925.88]  on other aspects
[1925.88 --> 1927.76]  that a lot of folks
[1927.76 --> 1928.44]  I think
[1928.44 --> 1929.84]  can miss.
[1929.84 --> 1931.72]  one was team scalability.
[1931.72 --> 1932.34]  I mentioned
[1932.34 --> 1933.40]  we have
[1933.40 --> 1934.80]  per page
[1934.80 --> 1935.80]  code splitting,
[1936.24 --> 1936.76]  which we
[1936.76 --> 1937.56]  ended up
[1937.56 --> 1938.92]  improving dramatically
[1938.92 --> 1939.70]  and changing a lot
[1939.70 --> 1940.36]  of it over time.
[1940.42 --> 1940.80]  But the idea
[1940.80 --> 1941.56]  still holds
[1941.56 --> 1941.96]  that
[1941.96 --> 1943.06]  if you're working
[1943.06 --> 1943.96]  on page A
[1943.96 --> 1945.56]  and you are a team
[1945.56 --> 1946.84]  and another team
[1946.84 --> 1947.22]  is working
[1947.22 --> 1948.18]  on page C,
[1948.76 --> 1949.48]  they should be able
[1949.48 --> 1950.68]  to fearlessly
[1950.68 --> 1952.00]  iterate
[1952.00 --> 1952.54]  on their
[1952.54 --> 1953.92]  respective areas
[1953.92 --> 1954.82]  of the system
[1954.82 --> 1955.86]  without
[1955.86 --> 1957.32]  hurting
[1957.32 --> 1958.38]  or encumbering
[1958.38 --> 1959.38]  the other team.
[1959.38 --> 1959.78]  So
[1959.78 --> 1960.76]  it was about
[1960.76 --> 1962.12]  creating a framework
[1962.12 --> 1964.00]  for not just
[1964.00 --> 1965.68]  end user performance,
[1965.80 --> 1965.98]  DX,
[1966.62 --> 1967.52]  but also
[1967.52 --> 1969.06]  the scalability
[1969.06 --> 1969.88]  of the organization
[1969.88 --> 1971.24]  that made the decision
[1971.24 --> 1971.80]  to use it.
[1972.22 --> 1973.02]  I remember
[1973.02 --> 1973.96]  interviewing,
[1974.22 --> 1974.94]  and I'll get into
[1974.94 --> 1976.54]  how my process
[1976.54 --> 1977.52]  works with customers,
[1977.70 --> 1977.84]  like,
[1977.92 --> 1978.72]  I remember interviewing
[1978.72 --> 1980.24]  an engineering manager
[1980.24 --> 1982.00]  from a very famous
[1982.00 --> 1982.96]  shoe company
[1982.96 --> 1984.16]  that associates
[1984.16 --> 1985.08]  themselves with
[1985.08 --> 1985.66]  high-performance
[1985.66 --> 1986.30]  athletes,
[1987.12 --> 1989.06]  and I remember
[1989.06 --> 1989.70]  asking them,
[1989.86 --> 1990.48]  what do you love
[1990.48 --> 1991.10]  the most about
[1991.10 --> 1991.84]  NXJS?
[1992.36 --> 1993.46]  Their answer was,
[1994.12 --> 1994.86]  any developer
[1994.86 --> 1996.28]  gets onboarded
[1996.28 --> 1997.02]  into this thing,
[1997.44 --> 1998.52]  they open the folder,
[1999.18 --> 2000.26]  and they basically
[2000.26 --> 2000.80]  understand how
[2000.80 --> 2001.50]  the whole thing works
[2001.50 --> 2002.34]  by just staring
[2002.34 --> 2003.16]  at the file system
[2003.16 --> 2003.54]  structure.
[2004.04 --> 2004.86]  They can see that
[2004.86 --> 2005.82]  we have a page
[2005.82 --> 2006.68]  for the product
[2006.68 --> 2007.64]  description,
[2007.94 --> 2008.50]  we have a page
[2008.50 --> 2009.22]  for the categories,
[2009.32 --> 2009.68]  we have a page
[2009.68 --> 2010.32]  for the search,
[2011.00 --> 2012.16]  and this is how
[2012.16 --> 2012.62]  we organize
[2012.62 --> 2013.44]  our storefront,
[2014.10 --> 2014.70]  which is
[2014.70 --> 2015.74]  responsible for
[2015.74 --> 2016.30]  lots and lots
[2016.30 --> 2016.92]  and lots of
[2016.92 --> 2017.92]  sales every year.
[2018.94 --> 2019.16]  So,
[2019.56 --> 2020.60]  the way that I think
[2020.60 --> 2021.84]  about our company,
[2022.46 --> 2023.54]  I think a lot about,
[2023.70 --> 2024.28]  first of all,
[2025.08 --> 2026.08]  picking the right
[2026.08 --> 2027.22]  fitness function.
[2027.82 --> 2029.10]  If this company
[2029.10 --> 2030.80]  gets inherited
[2030.80 --> 2032.90]  in decades
[2032.90 --> 2034.32]  by a completely
[2034.32 --> 2034.90]  different set
[2034.90 --> 2035.32]  of people,
[2036.14 --> 2037.18]  would they be able
[2037.18 --> 2038.06]  to take it
[2038.06 --> 2038.64]  to its right
[2038.64 --> 2039.26]  conclusion,
[2039.90 --> 2040.68]  regardless of
[2040.68 --> 2041.38]  who came before?
[2041.38 --> 2042.00]  Well,
[2042.02 --> 2042.52]  I think
[2042.52 --> 2043.44]  that has
[2043.44 --> 2043.84]  happened
[2043.84 --> 2044.36]  for a lot
[2044.36 --> 2045.56]  of amazing
[2045.56 --> 2046.20]  corporations.
[2046.40 --> 2046.84]  I think
[2046.84 --> 2048.02]  they have to
[2048.02 --> 2048.46]  have the right
[2048.46 --> 2048.80]  focus,
[2048.86 --> 2049.14]  they have to
[2049.14 --> 2049.60]  have the right
[2049.60 --> 2050.28]  fitness function.
[2050.44 --> 2050.58]  So,
[2050.86 --> 2051.36]  if our
[2051.36 --> 2052.06]  fitness function
[2052.06 --> 2053.10]  continues to be
[2053.10 --> 2054.70]  the end user
[2054.70 --> 2055.32]  performance
[2055.32 --> 2056.40]  and the success
[2056.40 --> 2057.14]  of the business
[2057.14 --> 2057.60]  at large
[2057.60 --> 2058.68]  in Pixar technology,
[2059.42 --> 2060.52]  I think we'll do
[2060.52 --> 2060.78]  well,
[2061.26 --> 2061.94]  because we'll be
[2061.94 --> 2062.44]  able to work
[2062.44 --> 2063.14]  backwards to the
[2063.14 --> 2063.62]  technology,
[2063.76 --> 2064.20]  to the right
[2064.20 --> 2064.64]  framework,
[2064.86 --> 2065.40]  to the right
[2065.40 --> 2066.28]  technique,
[2066.42 --> 2066.96]  to the right
[2066.96 --> 2067.50]  set of best
[2067.50 --> 2067.90]  practices,
[2068.02 --> 2068.42]  to the right
[2068.42 --> 2069.00]  analytics,
[2069.00 --> 2069.80]  etc.,
[2069.80 --> 2070.06]  etc.,
[2070.06 --> 2070.30]  etc.
[2070.30 --> 2070.56]  So,
[2070.78 --> 2072.16]  I think a lot
[2072.16 --> 2072.62]  in terms of
[2072.62 --> 2073.80]  evolutionary systems,
[2074.34 --> 2074.96]  and that's where
[2074.96 --> 2076.02]  the phrase
[2076.02 --> 2076.68]  fitness function
[2076.68 --> 2077.48]  really comes from,
[2077.64 --> 2078.98]  is a simple
[2078.98 --> 2080.40]  pathway to
[2080.40 --> 2080.88]  determining,
[2081.14 --> 2081.46]  are we doing
[2081.46 --> 2082.04]  the right thing
[2082.04 --> 2082.78]  or are we not?
[2083.30 --> 2083.96]  And also,
[2084.04 --> 2084.52]  by how we
[2084.52 --> 2085.02]  experiment,
[2085.20 --> 2085.34]  right?
[2085.40 --> 2085.62]  Like,
[2085.88 --> 2086.62]  we can launch
[2086.62 --> 2087.22]  lots of
[2087.22 --> 2087.86]  experiments,
[2088.36 --> 2088.96]  and we can ask
[2088.96 --> 2089.84]  ourselves if it,
[2090.02 --> 2090.28]  you know,
[2090.32 --> 2091.16]  contributed to that.
[2091.76 --> 2092.02]  So,
[2092.16 --> 2093.06]  on the other
[2093.06 --> 2093.48]  hand,
[2093.56 --> 2094.12]  I think,
[2094.72 --> 2095.10]  we,
[2095.34 --> 2096.26]  over the years,
[2096.26 --> 2097.34]  had the
[2097.34 --> 2097.94]  opportunity to
[2097.94 --> 2099.68]  learn in what
[2099.68 --> 2100.26]  ways is our
[2100.26 --> 2101.50]  technology 10
[2101.50 --> 2102.96]  times better than
[2102.96 --> 2103.62]  what currently
[2103.62 --> 2104.62]  existed.
[2105.18 --> 2105.94]  And that was
[2105.94 --> 2106.44]  really interesting
[2106.44 --> 2107.88]  and a really
[2107.88 --> 2108.62]  huge learning
[2108.62 --> 2109.40]  lesson for me.
[2109.64 --> 2110.30]  Because I
[2110.30 --> 2110.88]  started Next.js
[2110.88 --> 2111.26]  saying,
[2111.36 --> 2111.52]  okay,
[2111.96 --> 2112.48]  we're going to
[2112.48 --> 2113.98]  pre-render and
[2113.98 --> 2114.98]  dynamically server
[2114.98 --> 2116.14]  render because
[2116.14 --> 2116.72]  it's great for
[2116.72 --> 2117.52]  SEO and it's
[2117.52 --> 2117.78]  great for
[2117.78 --> 2118.30]  performance.
[2119.24 --> 2120.04]  And the
[2120.04 --> 2120.64]  technology was
[2120.64 --> 2121.26]  positioned as,
[2121.38 --> 2121.58]  well,
[2121.66 --> 2122.18]  it works for
[2122.18 --> 2122.58]  absolutely
[2122.58 --> 2123.10]  everything in
[2123.10 --> 2123.52]  the world.
[2124.00 --> 2124.28]  Awesome.
[2124.38 --> 2125.36]  It's a universal
[2125.36 --> 2126.08]  Turing machine.
[2126.26 --> 2126.66]  It can do
[2126.66 --> 2127.02]  anything.
[2127.60 --> 2128.32]  Over time,
[2128.38 --> 2128.92]  it turned out
[2128.92 --> 2130.24]  that those
[2130.24 --> 2131.10]  qualities of the
[2131.10 --> 2131.62]  framework and the
[2131.62 --> 2132.08]  platform,
[2132.28 --> 2132.68]  for example,
[2132.76 --> 2133.52]  ended up being
[2133.52 --> 2134.58]  great for
[2134.58 --> 2134.98]  everybody,
[2135.44 --> 2136.74]  but 10 times
[2136.74 --> 2137.36]  better or even
[2137.36 --> 2137.76]  more,
[2137.94 --> 2138.36]  for example,
[2138.52 --> 2139.12]  customers in the
[2139.12 --> 2140.00]  e-commerce space.
[2140.62 --> 2141.08]  And it's really
[2141.08 --> 2141.90]  interesting to reflect
[2141.90 --> 2142.24]  on this,
[2142.30 --> 2142.44]  right?
[2142.48 --> 2144.46]  Because their
[2144.46 --> 2146.06]  needs fit
[2146.06 --> 2147.62]  what we offer
[2147.62 --> 2149.10]  extremely well.
[2149.76 --> 2150.68]  One example I
[2150.68 --> 2151.44]  was reading today,
[2151.94 --> 2152.76]  folks are spending
[2152.76 --> 2154.40]  more hours on
[2154.40 --> 2155.44]  Amazon.com.
[2155.44 --> 2156.90]  than Walmart.
[2157.50 --> 2158.46]  If you count all
[2158.46 --> 2158.98]  their physical
[2158.98 --> 2159.66]  locations,
[2159.84 --> 2160.30]  all their web
[2160.30 --> 2160.82]  properties,
[2161.00 --> 2161.28]  et cetera.
[2161.80 --> 2162.58]  The e-commerce
[2162.58 --> 2163.52]  players of the
[2163.52 --> 2164.64]  world today,
[2164.98 --> 2165.82]  not all of them
[2165.82 --> 2167.24]  were born in
[2167.24 --> 2167.64]  the web.
[2167.76 --> 2168.30]  Not all of them
[2168.30 --> 2169.50]  were born online.
[2169.82 --> 2170.72]  Not all of them
[2170.72 --> 2172.26]  invented the cloud
[2172.26 --> 2173.50]  and data centers
[2173.50 --> 2175.08]  and EC2
[2175.08 --> 2175.74]  and S3.
[2176.40 --> 2177.18]  So on one side,
[2177.34 --> 2178.02]  they're playing
[2178.02 --> 2178.54]  catch up.
[2178.94 --> 2179.66]  They have no time
[2179.66 --> 2180.24]  to create front
[2180.24 --> 2181.12]  infrastructure teams.
[2181.62 --> 2182.34]  It's not a
[2182.34 --> 2183.22]  differentiator for them
[2183.22 --> 2183.76]  at this point.
[2183.76 --> 2184.30]  Well,
[2184.32 --> 2184.80]  that's meta work
[2184.80 --> 2185.08]  for them,
[2185.12 --> 2185.34]  right?
[2185.54 --> 2185.74]  Yeah,
[2185.76 --> 2186.16]  exactly.
[2186.68 --> 2187.06]  Wouldn't that be
[2187.06 --> 2187.58]  meta work for
[2187.58 --> 2188.44]  Walmart to build
[2188.44 --> 2190.70]  EC2 or AWS?
[2191.08 --> 2191.74]  Less meta work.
[2192.12 --> 2193.02]  And then on the
[2193.02 --> 2193.58]  other hand,
[2194.20 --> 2195.14]  it turns out that
[2195.14 --> 2196.10]  all these primitives
[2196.10 --> 2196.66]  that we're thinking
[2196.66 --> 2197.48]  about with Next.js,
[2197.78 --> 2199.48]  like great SEO,
[2199.84 --> 2200.60]  great performance,
[2200.74 --> 2201.10]  great this,
[2201.18 --> 2201.62]  great that.
[2202.26 --> 2202.48]  Yeah,
[2202.50 --> 2202.74]  sure.
[2202.80 --> 2203.30]  Like they're,
[2203.36 --> 2203.90]  they're great for
[2203.90 --> 2204.38]  my blog.
[2204.46 --> 2204.94]  They're great for
[2204.94 --> 2205.80]  Routjg.com.
[2205.86 --> 2206.40]  I'm really proud
[2206.40 --> 2207.00]  that it has a
[2207.00 --> 2208.10]  lighthouse almost a
[2208.10 --> 2208.76]  hundred or whatever.
[2209.38 --> 2210.44]  But for Walmart,
[2210.74 --> 2211.54]  who actually chose
[2211.54 --> 2211.88]  Next.js,
[2211.88 --> 2213.24]  it's a good metaphor.
[2213.90 --> 2215.14]  That is kind of
[2215.14 --> 2216.44]  the difference
[2216.44 --> 2217.94]  between being
[2217.94 --> 2218.84]  extremely competitive,
[2219.50 --> 2220.16]  even potentially
[2220.16 --> 2220.90]  overtaking,
[2221.40 --> 2222.76]  or spending all
[2222.76 --> 2223.36]  their time in
[2223.36 --> 2223.90]  meta work.
[2224.68 --> 2225.98]  So we learn a lot
[2225.98 --> 2227.48]  about what are
[2227.48 --> 2228.12]  the customers that
[2228.12 --> 2228.60]  we're going to make
[2228.60 --> 2229.26]  those tremendous
[2229.26 --> 2230.16]  differences for.
[2230.56 --> 2231.46]  We learn a lot
[2231.46 --> 2233.18]  about how.
[2233.62 --> 2234.38]  We learn a lot
[2234.38 --> 2235.44]  about communicating
[2235.44 --> 2237.38]  to them in ways
[2237.38 --> 2237.80]  that they can
[2237.80 --> 2239.54]  understand across
[2239.54 --> 2240.88]  all the layers of
[2240.88 --> 2241.42]  the stack,
[2241.54 --> 2242.86]  whether you're
[2242.86 --> 2243.52]  a junior engineer,
[2243.64 --> 2244.04]  you're a senior
[2244.04 --> 2244.44]  engineer,
[2244.70 --> 2244.94]  you're an
[2244.94 --> 2245.62]  engineering manager,
[2245.76 --> 2246.32]  you're a CTO,
[2246.42 --> 2246.96]  you're a VP of
[2246.96 --> 2247.42]  engineering.
[2247.96 --> 2248.64]  But also,
[2248.76 --> 2249.88]  as we spent
[2249.88 --> 2250.48]  time talking
[2250.48 --> 2251.20]  about no-code
[2251.20 --> 2251.80]  and low-code,
[2252.38 --> 2253.16]  there are so
[2253.16 --> 2253.64]  many people that
[2253.64 --> 2254.28]  want to contribute
[2254.28 --> 2255.12]  to these websites.
[2255.86 --> 2255.96]  Right?
[2256.08 --> 2256.32]  Like,
[2256.60 --> 2257.08]  you want to be
[2257.08 --> 2257.80]  able to go in
[2257.80 --> 2258.62]  and feature a
[2258.62 --> 2258.98]  product.
[2259.38 --> 2259.86]  You want to
[2259.86 --> 2260.50]  add a promotion.
[2261.04 --> 2261.50]  You want to
[2261.50 --> 2262.28]  theme it for
[2262.28 --> 2263.80]  Christmas coming
[2263.80 --> 2264.60]  in November and
[2264.60 --> 2264.94]  December.
[2265.16 --> 2265.22]  Right?
[2265.28 --> 2265.44]  Like,
[2265.64 --> 2266.12]  there's all
[2266.12 --> 2266.72]  those awesome
[2266.72 --> 2267.24]  things that you
[2267.24 --> 2268.44]  can do that,
[2268.60 --> 2269.02]  as I mentioned
[2269.02 --> 2269.24]  earlier,
[2269.38 --> 2269.74]  they will be
[2269.74 --> 2270.78]  developer-mediated.
[2270.88 --> 2271.68]  The developer
[2271.68 --> 2272.26]  will create
[2272.26 --> 2272.78]  the right
[2272.78 --> 2274.16]  schematisms
[2274.16 --> 2275.04]  or components
[2275.04 --> 2276.34]  or places
[2276.34 --> 2276.88]  in which you
[2276.88 --> 2278.02]  can add
[2278.02 --> 2278.62]  value,
[2279.24 --> 2279.70]  but then
[2279.70 --> 2280.78]  they're going
[2280.78 --> 2281.24]  to open
[2281.24 --> 2282.28]  those frameworks
[2282.28 --> 2283.54]  up for other
[2283.54 --> 2283.96]  folks to
[2283.96 --> 2284.34]  contribute.
[2284.54 --> 2284.66]  So,
[2284.86 --> 2285.62]  we learn about
[2285.62 --> 2286.32]  that as well.
[2286.50 --> 2286.54]  Right?
[2286.58 --> 2287.70]  We learn what is
[2287.70 --> 2288.34]  the right way
[2288.34 --> 2288.98]  that you can
[2288.98 --> 2289.64]  empower and
[2289.64 --> 2290.92]  enable the
[2290.92 --> 2291.68]  entire company
[2291.68 --> 2292.56]  on top of
[2292.56 --> 2293.18]  this Next.js
[2293.18 --> 2293.54]  and Versace
[2293.54 --> 2294.08]  transformation.
[2294.94 --> 2295.12]  So,
[2295.44 --> 2296.00]  these are all
[2296.00 --> 2296.42]  things that,
[2296.50 --> 2296.72]  you know,
[2297.00 --> 2297.84]  I sometimes joke
[2297.84 --> 2298.60]  to people that,
[2298.60 --> 2298.92]  like,
[2299.40 --> 2300.26]  I use words that
[2300.26 --> 2300.54]  I would have
[2300.54 --> 2301.00]  never used
[2301.00 --> 2301.68]  in the past
[2301.68 --> 2302.24]  just because,
[2302.40 --> 2302.56]  like,
[2302.88 --> 2303.52]  the lingo,
[2304.16 --> 2305.02]  I expanded it,
[2305.06 --> 2305.28]  really,
[2305.36 --> 2306.06]  because I continue
[2306.06 --> 2306.66]  to use our
[2306.66 --> 2307.22]  products.
[2307.84 --> 2308.42]  My framework
[2308.42 --> 2309.12]  for my time
[2309.12 --> 2309.48]  is,
[2310.18 --> 2310.58]  at least
[2310.58 --> 2311.48]  ideologically,
[2311.84 --> 2312.48]  is spend
[2312.48 --> 2313.06]  one-third of
[2313.06 --> 2313.64]  my time
[2313.64 --> 2314.80]  with customers
[2314.80 --> 2316.40]  and understanding
[2316.40 --> 2316.74]  what their
[2316.74 --> 2317.58]  requirements are
[2317.58 --> 2318.74]  and pitfalls
[2318.74 --> 2319.24]  and whatnot.
[2319.70 --> 2320.04]  And obviously,
[2320.14 --> 2320.78]  a lot of my team
[2320.78 --> 2321.22]  does that,
[2321.26 --> 2321.78]  but it's always
[2321.78 --> 2322.98]  great to deal
[2322.98 --> 2324.18]  with the
[2324.18 --> 2325.36]  escalations
[2325.36 --> 2326.08]  or the
[2326.08 --> 2327.02]  requirements
[2327.02 --> 2327.68]  that sort
[2327.68 --> 2328.42]  of are
[2328.42 --> 2328.92]  pressing
[2328.92 --> 2329.36]  about the
[2329.36 --> 2329.70]  future
[2329.70 --> 2330.28]  and so on.
[2330.92 --> 2331.68]  One-third
[2331.68 --> 2333.34]  with my
[2333.34 --> 2334.08]  own team
[2334.08 --> 2334.96]  and I
[2334.96 --> 2335.34]  always try
[2335.34 --> 2335.88]  to make
[2335.88 --> 2336.18]  that,
[2336.30 --> 2336.56]  if I'm
[2336.56 --> 2336.70]  going to
[2336.70 --> 2337.00]  err in
[2337.00 --> 2337.46]  one direction,
[2337.58 --> 2338.56]  spending a
[2338.56 --> 2338.84]  lot of
[2338.84 --> 2339.50]  time with
[2339.50 --> 2340.04]  my team
[2340.04 --> 2340.60]  and with
[2340.60 --> 2340.76]  our
[2340.76 --> 2341.22]  customers,
[2341.50 --> 2341.92]  ideally
[2341.92 --> 2342.42]  together,
[2343.02 --> 2343.44]  where,
[2343.56 --> 2343.80]  you know,
[2343.90 --> 2344.56]  we think
[2344.56 --> 2345.90]  about how
[2345.90 --> 2346.38]  we can do
[2346.38 --> 2346.76]  better.
[2347.20 --> 2347.52]  As I
[2347.52 --> 2347.76]  mentioned,
[2347.84 --> 2348.12]  if the
[2348.12 --> 2348.60]  company is
[2348.60 --> 2348.92]  almost like
[2348.92 --> 2349.48]  a framework,
[2349.94 --> 2350.30]  how can
[2350.30 --> 2350.86]  we improve
[2350.86 --> 2351.40]  that framework,
[2351.58 --> 2351.90]  how can
[2351.90 --> 2353.00]  we have
[2353.00 --> 2353.46]  a better
[2353.46 --> 2354.82]  experience
[2354.82 --> 2355.48]  for working
[2355.48 --> 2355.98]  at Vercel,
[2356.30 --> 2356.86]  for accessing
[2356.86 --> 2357.44]  information,
[2357.58 --> 2357.98]  for accessing
[2357.98 --> 2358.46]  data,
[2358.80 --> 2359.42]  for learning
[2359.42 --> 2360.10]  new things,
[2360.26 --> 2360.60]  et cetera,
[2361.12 --> 2361.90]  and for
[2361.90 --> 2362.50]  understanding
[2362.50 --> 2363.90]  also the
[2363.90 --> 2364.38]  priorities
[2364.38 --> 2366.08]  and the
[2366.08 --> 2367.62]  philosophies
[2367.62 --> 2368.58]  that drive
[2368.58 --> 2369.08]  our business
[2369.08 --> 2369.36]  forward,
[2369.40 --> 2369.90]  which actually
[2369.90 --> 2370.52]  relates into
[2370.52 --> 2371.52]  the last
[2371.52 --> 2371.90]  third,
[2372.60 --> 2373.08]  which for me
[2373.08 --> 2373.54]  is the ability
[2373.54 --> 2374.02]  to drive
[2374.02 --> 2374.54]  change.
[2375.24 --> 2375.80]  So we're
[2375.80 --> 2376.18]  going through
[2376.18 --> 2376.58]  this right
[2376.58 --> 2376.84]  now,
[2376.96 --> 2377.12]  right?
[2377.20 --> 2377.60]  As I
[2377.60 --> 2377.88]  mentioned,
[2377.98 --> 2379.10]  we're going
[2379.10 --> 2379.56]  through the
[2379.56 --> 2380.08]  transformation,
[2380.08 --> 2380.96]  in my
[2380.96 --> 2381.30]  opinion,
[2381.30 --> 2381.64]  of the
[2381.64 --> 2382.00]  entire
[2382.00 --> 2383.64]  cloud in
[2383.64 --> 2384.38]  terms of
[2384.38 --> 2385.12]  its ability
[2385.12 --> 2385.94]  to render
[2385.94 --> 2387.04]  pages very
[2387.04 --> 2387.64]  efficiently
[2387.64 --> 2390.22]  with browser-like
[2390.22 --> 2390.94]  technology.
[2391.44 --> 2392.04]  The future
[2392.04 --> 2392.36]  is going to
[2392.36 --> 2393.00]  look similar
[2393.00 --> 2393.42]  in many
[2393.42 --> 2394.86]  ways because
[2394.86 --> 2395.86]  we're,
[2396.04 --> 2396.24]  at the end
[2396.24 --> 2396.62]  of the day,
[2396.72 --> 2397.60]  still distributing
[2397.60 --> 2398.44]  pages throughout
[2398.44 --> 2398.94]  the world
[2398.94 --> 2399.88]  and distributing
[2399.88 --> 2400.52]  content.
[2401.08 --> 2401.56]  But it's also
[2401.56 --> 2402.64]  going to be
[2402.64 --> 2403.28]  very different
[2403.28 --> 2403.58]  from the
[2403.58 --> 2403.94]  past.
[2404.48 --> 2404.84]  It's going
[2404.84 --> 2405.62]  to be much
[2405.62 --> 2406.28]  more dynamic,
[2406.54 --> 2406.86]  much more
[2406.86 --> 2407.44]  instantaneous,
[2408.14 --> 2409.04]  even less
[2409.04 --> 2409.92]  of a
[2409.92 --> 2411.00]  operations
[2411.00 --> 2411.60]  burden for
[2411.60 --> 2412.10]  folks to
[2412.10 --> 2412.58]  scale.
[2413.46 --> 2414.26]  And driving
[2414.26 --> 2415.10]  this change
[2415.10 --> 2415.56]  when you've
[2415.56 --> 2416.50]  already succeeded
[2416.50 --> 2417.52]  in many ways
[2417.52 --> 2418.88]  sometimes can be
[2418.88 --> 2419.22]  challenging.
[2419.34 --> 2419.62]  That's why you
[2419.62 --> 2420.10]  have to spend
[2420.10 --> 2421.38]  time because
[2421.38 --> 2422.58]  you go through
[2422.58 --> 2423.18]  your own
[2423.18 --> 2424.70]  internal layers
[2424.70 --> 2425.34]  of innovation
[2425.34 --> 2425.92]  as well.
[2426.50 --> 2427.02]  This happened
[2427.02 --> 2427.50]  to us with
[2427.50 --> 2428.08]  Next.js many
[2428.08 --> 2428.66]  times already
[2428.66 --> 2429.86]  where Next.js
[2429.86 --> 2430.70]  started fully
[2430.70 --> 2431.44]  server-rendered.
[2432.20 --> 2432.52]  And then we
[2432.52 --> 2432.88]  realized,
[2433.00 --> 2433.48]  well, folks
[2433.48 --> 2434.54]  also need this
[2434.54 --> 2435.62]  beauty of
[2435.62 --> 2437.00]  edge caching
[2437.00 --> 2438.20]  that comes
[2438.20 --> 2439.52]  from static
[2439.52 --> 2440.18]  generation
[2440.18 --> 2441.12]  and later
[2441.12 --> 2442.18]  incremental
[2442.18 --> 2442.64]  static
[2442.64 --> 2443.14]  generation.
[2443.36 --> 2444.06]  So we
[2444.06 --> 2444.48]  kind of
[2444.48 --> 2445.64]  invented
[2445.64 --> 2445.98]  new
[2445.98 --> 2446.50]  technologies
[2446.50 --> 2447.78]  that in
[2447.78 --> 2448.08]  some ways
[2448.08 --> 2448.82]  almost seemingly
[2448.82 --> 2449.74]  went against
[2449.74 --> 2450.76]  previous wave
[2450.76 --> 2452.04]  at each
[2452.04 --> 2452.50]  layer.
[2453.34 --> 2453.78]  So driving
[2453.78 --> 2454.24]  that change
[2454.24 --> 2454.56]  is very
[2454.56 --> 2455.50]  important because
[2455.50 --> 2456.76]  first of all,
[2456.80 --> 2457.14]  it's driven
[2457.14 --> 2457.64]  by customer
[2457.64 --> 2458.06]  demand.
[2458.30 --> 2458.66]  Our customers
[2458.66 --> 2459.02]  are always
[2459.02 --> 2459.26]  saying,
[2459.40 --> 2459.78]  how can I
[2459.78 --> 2460.24]  be faster?
[2460.34 --> 2460.58]  How can I
[2460.58 --> 2460.86]  be more
[2460.86 --> 2461.22]  dynamic?
[2461.64 --> 2462.20]  How can I
[2462.20 --> 2463.12]  either sell
[2463.12 --> 2463.48]  more?
[2463.82 --> 2464.64]  Or how
[2464.64 --> 2464.88]  can you
[2464.88 --> 2465.32]  help me
[2465.32 --> 2466.54]  evolve faster
[2466.54 --> 2466.98]  and iterate
[2466.98 --> 2467.46]  faster?
[2468.22 --> 2469.50]  So I
[2469.50 --> 2469.94]  spend a lot
[2469.94 --> 2470.34]  of time
[2470.34 --> 2471.42]  driving that
[2471.42 --> 2471.90]  change and
[2471.90 --> 2472.56]  helping others
[2472.56 --> 2473.22]  drive it and
[2473.22 --> 2474.18]  internalize it
[2474.18 --> 2475.80]  and think of
[2475.80 --> 2476.08]  it and
[2476.08 --> 2476.82]  challenge it
[2476.82 --> 2477.64]  and discuss
[2477.64 --> 2478.12]  it and
[2478.12 --> 2479.00]  collaborate on
[2479.00 --> 2479.14]  it.
[2479.54 --> 2479.86]  I love that.
[2479.92 --> 2480.22]  You're spending
[2480.22 --> 2480.80]  time with the
[2480.80 --> 2481.24]  people that
[2481.24 --> 2481.72]  matter really
[2481.72 --> 2482.56]  most, which
[2482.56 --> 2483.88]  is first,
[2484.10 --> 2484.52]  I'm not sure
[2484.52 --> 2484.86]  if this is
[2484.86 --> 2485.76]  prioritized,
[2486.32 --> 2487.00]  customers and
[2487.00 --> 2487.50]  then team.
[2487.88 --> 2488.18]  I don't think
[2488.18 --> 2488.78]  it really matters
[2488.78 --> 2489.40]  honestly, so I'm
[2489.40 --> 2489.74]  not asking you
[2489.74 --> 2490.24]  to choose.
[2490.42 --> 2491.78]  But those are
[2491.78 --> 2492.78]  the two that
[2492.78 --> 2493.36]  matter most
[2493.36 --> 2493.80]  because you
[2493.80 --> 2494.32]  need a strong
[2494.32 --> 2495.56]  team and
[2495.56 --> 2496.16]  you need to
[2496.16 --> 2496.82]  satisfy the
[2496.82 --> 2497.22]  customer's
[2497.22 --> 2497.62]  needs.
[2498.44 --> 2499.58]  And when it
[2499.58 --> 2500.52]  comes down to
[2500.52 --> 2501.16]  it, you need
[2501.16 --> 2501.52]  to be the
[2501.52 --> 2502.18]  person leading
[2502.18 --> 2502.68]  the company
[2502.68 --> 2503.46]  to drive that
[2503.46 --> 2503.80]  change.
[2503.96 --> 2505.16]  If your team
[2505.16 --> 2505.34]  is doing
[2505.34 --> 2506.00]  something wrong
[2506.00 --> 2506.74]  or there's
[2506.74 --> 2507.18]  a process
[2507.18 --> 2507.60]  that's not
[2507.60 --> 2508.72]  right, you
[2508.72 --> 2508.92]  need to
[2508.92 --> 2509.40]  understand that
[2509.40 --> 2509.76]  deeply and
[2509.76 --> 2510.10]  you can't
[2510.10 --> 2510.40]  get that
[2510.40 --> 2510.86]  understanding
[2510.86 --> 2511.34]  unless you're
[2511.34 --> 2511.90]  spending time
[2511.90 --> 2512.24]  with them.
[2512.42 --> 2512.62]  For sure.
[2512.96 --> 2513.72]  And still
[2513.72 --> 2514.98]  that ability
[2514.98 --> 2515.60]  to drive that
[2515.60 --> 2515.94]  change.
[2516.02 --> 2516.32]  Can you give
[2516.32 --> 2517.46]  me any
[2517.46 --> 2518.60]  examples where
[2518.60 --> 2519.76]  you've spent
[2519.76 --> 2520.36]  this time
[2520.36 --> 2520.94]  with the
[2520.94 --> 2521.56]  customer or
[2521.56 --> 2522.26]  with the
[2522.26 --> 2522.58]  team?
[2522.78 --> 2523.20]  Aside from
[2523.20 --> 2524.08]  the mention
[2524.08 --> 2524.32]  you just
[2524.32 --> 2524.58]  mentioned
[2524.58 --> 2524.82]  around
[2524.82 --> 2525.06]  Next.
[2525.10 --> 2525.24]  Yes,
[2525.30 --> 2526.20]  but maybe
[2526.20 --> 2527.40]  the shoe
[2527.40 --> 2527.86]  company you
[2527.86 --> 2528.10]  mentioned,
[2528.36 --> 2529.14]  anything, I
[2529.14 --> 2529.44]  don't know,
[2529.52 --> 2529.76]  I'm just
[2529.76 --> 2530.66]  teasing out
[2530.66 --> 2530.92]  something.
[2531.32 --> 2531.68]  I'll give
[2531.68 --> 2532.22]  you a very
[2532.22 --> 2532.50]  interesting
[2532.50 --> 2533.04]  example.
[2533.88 --> 2534.94]  So a lot
[2534.94 --> 2535.18]  of my
[2535.18 --> 2535.98]  customer stories
[2535.98 --> 2537.14]  relate to
[2537.14 --> 2538.52]  understanding
[2538.52 --> 2539.90]  why they're
[2539.90 --> 2541.12]  succeeding or
[2541.12 --> 2542.02]  what else
[2542.02 --> 2542.36]  could be
[2542.36 --> 2543.00]  doing for
[2543.00 --> 2543.36]  them to
[2543.36 --> 2543.84]  succeed and
[2543.84 --> 2544.14]  in what
[2544.14 --> 2544.62]  ways they're
[2544.62 --> 2545.20]  not succeeding.
[2545.20 --> 2545.52]  Right?
[2546.24 --> 2547.02]  One thing
[2547.02 --> 2547.50]  that I
[2547.50 --> 2548.52]  noticed recently
[2548.52 --> 2549.26]  is Next.
[2549.26 --> 2549.58]  JS and
[2549.58 --> 2550.00]  Verstall are
[2550.00 --> 2550.60]  incredibly
[2550.60 --> 2551.06]  organic.
[2551.06 --> 2551.88]  You actually
[2551.88 --> 2552.68]  alluded to
[2552.68 --> 2553.12]  this where
[2553.12 --> 2553.70]  you just
[2553.70 --> 2554.18]  hear of
[2554.18 --> 2554.98]  it and
[2554.98 --> 2555.36]  you see
[2555.36 --> 2556.02]  it pretty
[2556.02 --> 2556.82]  much everywhere,
[2557.04 --> 2557.24]  et cetera,
[2557.32 --> 2557.56]  et cetera.
[2558.08 --> 2558.64]  So that
[2558.64 --> 2559.16]  actually has
[2559.16 --> 2560.44]  a disadvantage
[2560.44 --> 2561.14]  in some way
[2561.14 --> 2562.34]  in that you're
[2562.34 --> 2563.70]  not there to
[2563.70 --> 2565.32]  witness the
[2565.32 --> 2566.60]  internal process
[2566.60 --> 2567.48]  or processes
[2567.48 --> 2569.60]  that led to
[2569.60 --> 2570.80]  its decision
[2570.80 --> 2571.80]  of being there.
[2572.24 --> 2573.10]  That can even
[2573.10 --> 2573.76]  create an
[2573.76 --> 2574.58]  interesting pressure
[2574.58 --> 2575.66]  like easy
[2575.66 --> 2576.42]  come, easy
[2576.42 --> 2576.80]  go.
[2577.10 --> 2577.20]  Right?
[2577.20 --> 2577.54]  If it's
[2577.54 --> 2577.94]  so easy
[2577.94 --> 2578.44]  to choose
[2578.44 --> 2579.48]  it, would
[2579.48 --> 2579.88]  it be easy
[2579.88 --> 2580.30]  to choose
[2580.30 --> 2580.66]  the next
[2580.66 --> 2581.12]  thing?
[2581.48 --> 2581.60]  Right?
[2582.10 --> 2582.52]  So I
[2582.52 --> 2582.88]  spent a lot
[2582.88 --> 2583.20]  of time
[2583.20 --> 2584.00]  actually reverse
[2584.00 --> 2584.62]  engineering.
[2585.40 --> 2585.92]  Okay, why
[2585.92 --> 2586.22]  is this
[2586.22 --> 2586.84]  customer, why
[2586.84 --> 2587.12]  did they
[2587.12 --> 2587.56]  choose it?
[2588.12 --> 2588.46]  What are
[2588.46 --> 2588.94]  the things
[2588.94 --> 2590.06]  that stood
[2590.06 --> 2590.44]  out to
[2590.44 --> 2590.72]  them?
[2590.82 --> 2591.38]  Which in
[2591.38 --> 2591.80]  many ways
[2591.80 --> 2592.10]  is almost
[2592.10 --> 2592.44]  like a
[2592.44 --> 2593.04]  synchronization
[2593.04 --> 2593.64]  or calibration
[2593.64 --> 2594.28]  process,
[2594.44 --> 2594.62]  right?
[2594.64 --> 2595.52]  Because maybe
[2595.52 --> 2595.84]  you think,
[2596.04 --> 2596.98]  well, this
[2596.98 --> 2597.50]  one feature
[2597.50 --> 2598.22]  really is
[2598.22 --> 2598.62]  awesome.
[2599.14 --> 2599.48]  But then
[2599.48 --> 2599.86]  you talk to
[2599.86 --> 2600.08]  the customer
[2600.08 --> 2600.22]  and it's
[2600.22 --> 2600.50]  like, well,
[2600.52 --> 2600.76]  I couldn't
[2600.76 --> 2601.26]  care less
[2601.26 --> 2601.60]  about that
[2601.60 --> 2601.96]  feature.
[2602.38 --> 2603.40]  Actually, I'm
[2603.40 --> 2603.88]  really interested
[2603.88 --> 2604.44]  in that other
[2604.44 --> 2604.78]  feature,
[2604.78 --> 2605.10]  right?
[2605.26 --> 2605.64]  So it's
[2605.64 --> 2606.26]  that calibration
[2606.26 --> 2607.24]  process.
[2607.94 --> 2608.14]  And then
[2608.14 --> 2608.44]  also
[2608.44 --> 2609.02]  understanding,
[2609.66 --> 2611.38]  okay, as
[2611.38 --> 2612.04]  we just
[2612.04 --> 2612.68]  talked about,
[2612.80 --> 2613.36]  if my
[2613.36 --> 2614.28]  real goal
[2614.28 --> 2614.66]  is to
[2614.66 --> 2615.58]  help their
[2615.58 --> 2616.10]  customer,
[2616.48 --> 2617.22]  I most
[2617.22 --> 2617.82]  definitely
[2617.82 --> 2618.32]  need to
[2618.32 --> 2618.76]  talk to
[2618.76 --> 2620.20]  them to
[2620.20 --> 2620.82]  understand
[2620.82 --> 2622.04]  what problem
[2622.04 --> 2622.34]  they're trying
[2622.34 --> 2622.60]  to solve
[2622.60 --> 2623.06]  for their
[2623.06 --> 2623.48]  end user
[2623.48 --> 2624.06]  and how
[2624.06 --> 2624.32]  we can
[2624.32 --> 2624.74]  help them.
[2625.12 --> 2625.34]  So a good
[2625.34 --> 2625.82]  example from
[2625.82 --> 2626.36]  recently, I
[2626.36 --> 2627.74]  tweeted a
[2627.74 --> 2628.62]  DTC,
[2629.02 --> 2629.80]  direct-to-consumer
[2629.80 --> 2630.24]  e-commerce
[2630.24 --> 2630.76]  company,
[2631.34 --> 2631.90]  broke down
[2631.90 --> 2632.44]  their monolith.
[2633.24 --> 2633.58]  So they
[2633.58 --> 2634.46]  had this
[2634.46 --> 2635.08]  sort of
[2635.08 --> 2635.74]  monolithic
[2635.74 --> 2636.34]  build of
[2636.34 --> 2636.50]  their
[2636.50 --> 2637.16]  storefront
[2637.16 --> 2638.38]  coupled to
[2638.38 --> 2639.28]  a particular
[2639.28 --> 2639.68]  backend,
[2640.08 --> 2641.30]  and they
[2641.30 --> 2641.92]  decided to
[2641.92 --> 2642.66]  replatform on
[2642.66 --> 2642.88]  top of
[2642.88 --> 2643.24]  Next.js
[2643.24 --> 2643.76]  and Versel
[2643.76 --> 2645.24]  without making
[2645.24 --> 2645.94]  very drastic
[2645.94 --> 2646.34]  changes.
[2646.58 --> 2647.12]  So this
[2647.12 --> 2647.58]  was not
[2647.58 --> 2648.76]  like, we're
[2648.76 --> 2648.98]  going to
[2648.98 --> 2649.64]  reinvent the
[2649.64 --> 2650.30]  company type
[2650.30 --> 2650.66]  of thing.
[2650.78 --> 2651.22]  It was more
[2651.22 --> 2651.64]  like, okay,
[2651.64 --> 2652.34]  let's replatform
[2652.34 --> 2652.74]  and see how
[2652.74 --> 2653.12]  it goes.
[2653.74 --> 2654.38]  And they
[2654.38 --> 2654.96]  knew that
[2654.96 --> 2655.66]  if this
[2655.66 --> 2655.92]  project
[2655.92 --> 2656.44]  succeeded,
[2656.74 --> 2657.14]  it was
[2657.14 --> 2657.48]  going to
[2657.48 --> 2658.12]  yield better
[2658.12 --> 2658.48]  developer
[2658.48 --> 2658.90]  experience.
[2659.04 --> 2659.30]  So obviously
[2659.30 --> 2659.84]  developers were
[2659.84 --> 2660.42]  motivated to
[2660.42 --> 2660.74]  do this.
[2661.28 --> 2661.94]  But everyone,
[2662.14 --> 2662.50]  especially in
[2662.50 --> 2662.80]  e-commerce,
[2662.94 --> 2663.32]  this is why I
[2663.32 --> 2663.86]  love that
[2663.86 --> 2664.74]  cohort of
[2664.74 --> 2665.14]  our business
[2665.14 --> 2666.40]  is that you
[2666.40 --> 2667.64]  do have a
[2667.64 --> 2668.54]  pulse that's
[2668.54 --> 2669.24]  very clear on
[2669.24 --> 2670.24]  your ultimate
[2670.24 --> 2670.98]  performance of
[2670.98 --> 2672.04]  like, are we
[2672.04 --> 2672.64]  selling a lot of
[2672.64 --> 2673.22]  shoes or are we
[2673.22 --> 2673.72]  selling a lot of
[2673.72 --> 2674.04]  chairs?
[2674.48 --> 2674.52]  Right.
[2674.68 --> 2675.36]  Feedback loop is
[2675.36 --> 2675.60]  tighter.
[2675.60 --> 2676.40]  very tight.
[2677.00 --> 2678.08]  So it was
[2678.08 --> 2678.58]  amazing to hear
[2678.58 --> 2679.10]  from them that
[2679.10 --> 2679.90]  ever since the
[2679.90 --> 2680.82]  first day that
[2680.82 --> 2681.30]  they started
[2681.30 --> 2682.10]  A-B testing it
[2682.10 --> 2682.68]  in production,
[2683.34 --> 2683.84]  they couldn't
[2683.84 --> 2684.74]  believe their
[2684.74 --> 2685.40]  eyes when they
[2685.40 --> 2685.80]  were looking at
[2685.80 --> 2686.56]  the dashboards,
[2686.88 --> 2687.96]  which reflected
[2687.96 --> 2688.70]  what ultimately
[2688.70 --> 2690.06]  became a 16%
[2690.06 --> 2692.56]  lift in sales
[2692.56 --> 2693.54]  just from
[2693.54 --> 2694.56]  replatforming.
[2695.44 --> 2696.64]  And this is the
[2696.64 --> 2697.44]  kind of confirmation
[2697.44 --> 2698.88]  in customer story
[2698.88 --> 2700.38]  that, believe it
[2700.38 --> 2700.82]  or not, like
[2700.82 --> 2701.40]  sometimes people
[2701.40 --> 2702.38]  just knock on
[2702.38 --> 2702.76]  your door to
[2702.76 --> 2703.92]  tell you, you
[2703.92 --> 2704.40]  have to actually
[2704.40 --> 2704.88]  ask and make,
[2704.88 --> 2706.04]  hey, how are
[2706.04 --> 2706.46]  you succeeding?
[2706.62 --> 2707.42]  And also, folks
[2707.42 --> 2708.28]  sometimes just don't
[2708.28 --> 2708.74]  tell you they're
[2708.74 --> 2709.28]  not succeeding,
[2709.40 --> 2709.54]  right?
[2709.60 --> 2710.90]  Like, hey, we're
[2710.90 --> 2712.06]  thinking about
[2712.06 --> 2713.46]  ditching the web
[2713.46 --> 2714.68]  and moving to
[2714.68 --> 2715.46]  AMP.
[2715.68 --> 2716.46]  Bad news,
[2716.66 --> 2716.84]  Next.
[2716.94 --> 2717.70]  Yes is not for
[2717.70 --> 2718.10]  us.
[2718.34 --> 2718.52]  Yeah.
[2718.74 --> 2719.06]  We're going
[2719.06 --> 2719.38]  native.
[2719.56 --> 2719.92]  We're going
[2719.92 --> 2720.78]  native or we're
[2720.78 --> 2721.36]  going to AMP
[2721.36 --> 2721.98]  or whatever,
[2722.36 --> 2722.58]  right?
[2722.76 --> 2724.00]  So I also want
[2724.00 --> 2724.38]  to understand
[2724.38 --> 2724.78]  those.
[2725.14 --> 2726.58]  So it's such a
[2726.58 --> 2727.74]  large space that
[2727.74 --> 2729.22]  obviously you have
[2729.22 --> 2730.10]  to kind of pick
[2730.10 --> 2730.60]  your battles,
[2730.78 --> 2731.72]  especially now with
[2731.72 --> 2732.82]  my time being
[2732.82 --> 2733.52]  less available,
[2733.52 --> 2734.16]  but I try to
[2734.16 --> 2734.58]  also,
[2734.88 --> 2735.82]  understand folks
[2735.82 --> 2736.44]  at the different
[2736.44 --> 2736.96]  levels.
[2737.16 --> 2738.24]  Like, I still
[2738.24 --> 2739.46]  talk to the
[2739.46 --> 2740.04]  developer that
[2740.04 --> 2740.52]  will pick the
[2740.52 --> 2740.84]  tool.
[2741.46 --> 2742.38]  Recently, we
[2742.38 --> 2743.18]  organized a little
[2743.18 --> 2743.96]  meetup with the
[2743.96 --> 2744.92]  hackers of the
[2744.92 --> 2745.82]  future from
[2745.82 --> 2747.04]  Hack Club who
[2747.04 --> 2747.54]  came to our
[2747.54 --> 2748.26]  office and told
[2748.26 --> 2749.14]  us about the
[2749.14 --> 2749.76]  ways that they're
[2749.76 --> 2751.12]  learning about the
[2751.12 --> 2751.76]  web and what their
[2751.76 --> 2752.64]  perceptions of the
[2752.64 --> 2753.38]  technology and the
[2753.38 --> 2754.24]  web are.
[2754.60 --> 2755.48]  I also obviously
[2755.48 --> 2755.98]  talked to our
[2755.98 --> 2756.80]  enterprise customers
[2756.80 --> 2757.88]  and I talked to
[2757.88 --> 2758.32]  prospects.
[2758.32 --> 2759.62]  So it's nice to
[2759.62 --> 2760.46]  kind of have a
[2760.46 --> 2761.48]  view that's as
[2761.48 --> 2762.50]  broad as possible
[2762.50 --> 2764.02]  of who's out
[2764.02 --> 2764.68]  there because
[2764.68 --> 2765.46]  obviously we're all
[2765.46 --> 2766.00]  impacted by
[2766.00 --> 2766.40]  technology.
[2766.74 --> 2767.72]  I also sometimes,
[2767.86 --> 2768.00]  you know,
[2768.04 --> 2769.00]  like I'm curious
[2769.00 --> 2769.68]  when my mom
[2769.68 --> 2770.26]  thinks about the
[2770.26 --> 2770.78]  web, like,
[2771.10 --> 2771.78]  are you annoyed
[2771.78 --> 2773.46]  at GDPR banners?
[2773.94 --> 2774.54]  Like, do things
[2774.54 --> 2776.00]  load very slowly
[2776.00 --> 2777.10]  in Argentina?
[2777.46 --> 2777.74]  You know,
[2777.80 --> 2779.08]  like the world is
[2779.08 --> 2780.00]  so global just
[2780.00 --> 2781.12]  like the web and
[2781.12 --> 2781.96]  we're all in it
[2781.96 --> 2782.94]  and we're all in
[2782.94 --> 2783.38]  it together.
[2783.38 --> 2784.86]  So it's awesome
[2784.86 --> 2786.06]  to just kind of
[2786.06 --> 2786.68]  get the sense
[2786.68 --> 2787.42]  from everybody.
[2787.86 --> 2788.26]  I'm glad you
[2788.26 --> 2788.64]  explained this
[2788.64 --> 2789.38]  framework because
[2789.38 --> 2790.98]  again, a
[2790.98 --> 2791.44]  principle of yours
[2791.44 --> 2792.18]  that seems so
[2792.18 --> 2793.52]  simple to
[2793.52 --> 2794.20]  develop, to
[2794.20 --> 2794.78]  preview, to
[2794.78 --> 2795.60]  ship, to
[2795.60 --> 2796.60]  spend time with
[2796.60 --> 2797.48]  customers, to
[2797.48 --> 2797.94]  spend time with
[2797.94 --> 2798.54]  your team and
[2798.54 --> 2800.30]  to remain to
[2800.30 --> 2800.78]  have the ability
[2800.78 --> 2801.58]  to drive change.
[2801.72 --> 2802.06]  I think that
[2802.06 --> 2803.62]  those are like
[2803.62 --> 2804.60]  core tenets to
[2804.60 --> 2805.90]  someone's character
[2805.90 --> 2806.88]  like yours that
[2806.88 --> 2808.92]  really they're
[2808.92 --> 2810.16]  complex but
[2810.16 --> 2810.70]  they're just so
[2810.70 --> 2811.06]  simple.
[2811.50 --> 2811.94]  Yeah, I think
[2811.94 --> 2813.12]  simplicity continues
[2813.12 --> 2814.52]  to be very
[2814.52 --> 2815.22]  hard to attain
[2815.22 --> 2815.72]  for sure.
[2815.94 --> 2816.78]  I guess I
[2816.78 --> 2817.28]  remember actually
[2817.28 --> 2817.94]  the day that we
[2817.94 --> 2818.50]  came up with the
[2818.50 --> 2820.02]  motto, like I
[2820.02 --> 2820.60]  know that there's
[2820.60 --> 2822.06]  been a pattern of
[2822.06 --> 2822.74]  startups saying
[2822.74 --> 2823.48]  like, oh, we do
[2823.48 --> 2824.48]  A, B, and C and
[2824.48 --> 2824.74]  whatnot.
[2824.96 --> 2825.86]  Like it's, it
[2825.86 --> 2826.52]  doesn't seem
[2826.52 --> 2827.12]  novel, it doesn't
[2827.12 --> 2827.88]  seem interesting.
[2828.34 --> 2828.74]  But I remember
[2828.74 --> 2829.88]  when we're talking
[2829.88 --> 2831.34]  a lot in a room
[2831.34 --> 2832.66]  about, okay, like
[2832.66 --> 2833.98]  how do we explain
[2833.98 --> 2834.72]  the thing?
[2834.94 --> 2835.88]  Like, what do we
[2835.88 --> 2836.18]  say?
[2836.56 --> 2838.04]  Do we say it's
[2838.04 --> 2838.56]  a front and
[2838.56 --> 2839.10]  framework next to
[2839.10 --> 2840.22]  JS and a
[2840.22 --> 2841.44]  edge compute
[2841.44 --> 2842.20]  platform that's
[2842.20 --> 2842.68]  serverless?
[2842.68 --> 2843.38]  Like it's just
[2843.38 --> 2844.60]  lingo and like
[2844.60 --> 2845.30]  how we make it
[2845.30 --> 2846.24]  approachable and
[2846.24 --> 2847.64]  yeah, how can you
[2847.64 --> 2848.10]  make it a
[2848.10 --> 2848.48]  framework?
[2848.74 --> 2849.34]  For example, the
[2849.34 --> 2850.54]  other day, and so
[2850.54 --> 2851.24]  I love frameworks,
[2851.84 --> 2852.30]  the other day I
[2852.30 --> 2853.86]  was talking to a
[2853.86 --> 2855.26]  customer prospect
[2855.26 --> 2856.64]  that was very,
[2856.72 --> 2858.08]  very driven by
[2858.08 --> 2859.32]  security requirements.
[2859.84 --> 2859.96]  Right?
[2860.04 --> 2861.28]  Like for this
[2861.28 --> 2862.68]  person, you could
[2862.68 --> 2863.34]  have that developer
[2863.34 --> 2864.04]  experience that
[2864.04 --> 2865.66]  where every page
[2865.66 --> 2866.56]  change takes you
[2866.56 --> 2867.38]  three hours to
[2867.38 --> 2868.58]  reflect and the
[2868.58 --> 2869.30]  end user experience
[2869.30 --> 2870.12]  could be you can
[2870.12 --> 2871.28]  load one page a
[2871.28 --> 2872.28]  day, but their
[2872.28 --> 2872.80]  priority was
[2872.80 --> 2873.76]  security, right?
[2874.14 --> 2875.04]  So they would be
[2875.04 --> 2875.50]  okay with that.
[2875.88 --> 2876.72]  And this is what's
[2876.72 --> 2877.36]  fun too about
[2877.36 --> 2878.08]  understanding where
[2878.08 --> 2879.20]  everyone's priorities
[2879.20 --> 2880.48]  are, what everyone's
[2880.48 --> 2882.22]  own goals and
[2882.22 --> 2883.48]  fitness functions are
[2883.48 --> 2884.36]  for technology,
[2884.48 --> 2884.66]  right?
[2884.66 --> 2887.08]  And I was able to
[2887.08 --> 2888.48]  illustrate how we
[2888.48 --> 2889.22]  think about security
[2889.22 --> 2890.32]  through that life
[2890.32 --> 2890.68]  cycle.
[2890.68 --> 2891.72]  I said, well, on the
[2891.72 --> 2893.70]  develop phase, Next.js
[2893.70 --> 2894.72]  is introducing
[2894.72 --> 2895.82]  conformance for
[2895.82 --> 2897.26]  security to stop
[2897.26 --> 2898.32]  you early on in,
[2898.76 --> 2899.42]  even before you
[2899.42 --> 2900.04]  push, you're not
[2900.04 --> 2900.56]  going to push
[2900.56 --> 2901.34]  something that's bad
[2901.34 --> 2901.90]  for security.
[2902.60 --> 2903.60]  React has great
[2903.60 --> 2904.52]  support for XSS
[2904.52 --> 2906.38]  and it has, it
[2906.38 --> 2907.60]  blocks you from
[2907.60 --> 2909.40]  SQL injections or
[2909.40 --> 2910.34]  easy, or sorry,
[2910.44 --> 2911.48]  HTML and JS
[2911.48 --> 2912.54]  injections being easy
[2912.54 --> 2913.00]  and whatnot.
[2913.00 --> 2914.36]  And we're adding
[2914.36 --> 2915.24]  trusted types of
[2915.24 --> 2916.02]  support for even
[2916.02 --> 2916.76]  better XSS
[2916.76 --> 2917.32]  protection.
[2917.78 --> 2918.26]  Then on the
[2918.26 --> 2920.08]  preview side, we've
[2920.08 --> 2921.42]  invested tremendous
[2921.42 --> 2922.92]  amounts in making
[2922.92 --> 2924.16]  our builds completely
[2924.16 --> 2925.22]  isolated, zero
[2925.22 --> 2926.08]  trust environments.
[2926.60 --> 2927.70]  They get disposed
[2927.70 --> 2928.62]  after every build
[2928.62 --> 2929.06]  complete.
[2929.20 --> 2929.74]  So we're able to
[2929.74 --> 2930.32]  like, okay, like
[2930.32 --> 2931.56]  give you kind of a
[2931.56 --> 2932.36]  sense of even what
[2932.36 --> 2933.60]  the product does while
[2933.60 --> 2934.50]  it talks to you about
[2934.50 --> 2935.02]  security.
[2935.16 --> 2936.06]  And then when we
[2936.06 --> 2937.68]  ship the same at
[2937.68 --> 2938.74]  runtime, we have this
[2938.74 --> 2939.72]  incredible isolation
[2939.72 --> 2941.18]  primitives for
[2941.18 --> 2942.02]  executing arbitrary
[2942.02 --> 2942.98]  compute in a
[2942.98 --> 2943.98]  complete sandbox.
[2945.20 --> 2946.50]  So through that
[2946.50 --> 2947.42]  framework that I can
[2947.42 --> 2948.32]  use to explain the
[2948.32 --> 2949.08]  product, I was able
[2949.08 --> 2950.02]  to also explain
[2950.02 --> 2950.66]  security.
[2951.64 --> 2952.36]  And I can also,
[2952.54 --> 2953.14]  you know, maybe if
[2953.14 --> 2953.58]  I'm talking to an
[2953.58 --> 2954.24]  investor, I might use
[2954.24 --> 2955.22]  it to explain the
[2955.22 --> 2956.34]  total addressable
[2956.34 --> 2957.02]  market, right?
[2957.04 --> 2957.68]  Because I say, well,
[2957.94 --> 2958.78]  developers, we have
[2958.78 --> 2960.12]  13.7 million
[2960.12 --> 2961.46]  JavaScript developers,
[2961.46 --> 2962.32]  and that's growing.
[2962.84 --> 2964.44]  There is 550 million
[2964.44 --> 2965.78]  Excel users.
[2966.32 --> 2967.48]  So we can say, okay,
[2967.56 --> 2968.76]  developers could grow a
[2968.76 --> 2969.86]  lot and will, right?
[2970.50 --> 2971.62]  Previewing opens up
[2971.62 --> 2972.80]  collaboration, right?
[2972.84 --> 2973.52]  So we have customers
[2973.52 --> 2975.36]  like Washington Post
[2975.36 --> 2977.22]  that use a preview
[2977.22 --> 2978.66]  URLs primarily to
[2978.66 --> 2980.06]  collaborate with
[2980.06 --> 2981.40]  editors, non-technical
[2981.40 --> 2983.40]  folks, user testing,
[2984.02 --> 2984.84]  all kinds of
[2984.84 --> 2985.54]  reviews.
[2986.50 --> 2987.56]  So now Preview has
[2987.56 --> 2988.48]  opened up the
[2988.48 --> 2989.86]  addressable marketer,
[2989.90 --> 2990.70]  like everyone who
[2990.70 --> 2991.64]  wants to collaborate on
[2991.64 --> 2992.70]  a website, which is
[2992.70 --> 2993.74]  obviously a lot of
[2993.74 --> 2994.06]  people.
[2994.06 --> 2995.54]  And then shipping,
[2996.30 --> 2996.86]  you know, as I
[2996.86 --> 2997.52]  mentioned earlier,
[2998.20 --> 2998.90]  our goal would
[2998.90 --> 2999.70]  probably be, you
[2999.70 --> 3001.16]  know, we think the
[3001.16 --> 3002.34]  top 10,000 Alexa
[3002.34 --> 3004.30]  websites will always
[3004.30 --> 3005.94]  have top-notch
[3005.94 --> 3006.96]  engineering teams that
[3006.96 --> 3007.66]  work with developer
[3007.66 --> 3009.06]  tools, but then the
[3009.06 --> 3010.18]  entire rest of the
[3010.18 --> 3011.04]  world will access
[3011.04 --> 3011.88]  websites that have
[3011.88 --> 3012.48]  been created through
[3012.48 --> 3013.48]  no-code or low-code.
[3013.72 --> 3014.62]  So you can argue,
[3014.74 --> 3015.82]  you know, there's a
[3015.82 --> 3016.86]  very addressable
[3016.86 --> 3018.96]  segment there, which
[3018.96 --> 3019.92]  is the entire
[3019.92 --> 3020.30]  internet.
[3020.50 --> 3021.36]  But realistically
[3021.36 --> 3022.22]  speaking, you know,
[3022.24 --> 3023.38]  like you look at the
[3023.38 --> 3025.04]  Alexa and you find a
[3025.04 --> 3025.90]  ton of websites that
[3025.90 --> 3026.70]  need our help.
[3027.52 --> 3029.00]  So it's a good
[3029.00 --> 3029.50]  framework.
[3029.76 --> 3030.88]  And as I mentioned,
[3031.00 --> 3032.76]  to summarize how I
[3032.76 --> 3034.00]  spend my time, I
[3034.00 --> 3034.58]  spend my time thinking
[3034.58 --> 3035.44]  about frameworks, not
[3035.44 --> 3037.08]  just for the code, but
[3037.08 --> 3039.10]  frameworks for how the
[3039.10 --> 3040.10]  company can operate
[3040.10 --> 3042.38]  and how we can scale
[3042.38 --> 3043.92]  our approachability to
[3043.92 --> 3045.16]  customers and users
[3045.16 --> 3045.52]  alike.
[3053.38 --> 3063.28]  this episode is brought
[3063.28 --> 3064.26]  to you by Gitpod.
[3064.38 --> 3065.22]  Gitpod lets you spin up
[3065.22 --> 3066.24]  fresh, ephemeral,
[3066.40 --> 3066.92]  automated dev
[3066.92 --> 3067.90]  environments in the
[3067.90 --> 3068.56]  cloud in seconds.
[3069.10 --> 3069.56]  And I'm here with
[3069.56 --> 3070.32]  Johannes Landgraf,
[3070.44 --> 3071.50]  co-founder of Gitpod.
[3071.88 --> 3072.82]  Johannes, GitHub made a
[3072.82 --> 3073.32]  big announcement
[3073.32 --> 3074.40]  recently with Codespaces,
[3074.84 --> 3075.88]  validating that it is now
[3075.88 --> 3076.96]  time for dev teams to
[3076.96 --> 3077.72]  consider what automated
[3077.72 --> 3079.00]  dev environments can do
[3079.00 --> 3079.48]  for them.
[3079.60 --> 3080.08]  What do you have to say
[3080.08 --> 3080.40]  to that?
[3080.40 --> 3081.94]  I'd say welcome to
[3081.94 --> 3082.90]  the party, GitHub and
[3082.90 --> 3083.36]  Microsoft.
[3084.26 --> 3085.64]  No, honestly, we were
[3085.64 --> 3086.88]  very excited because it
[3086.88 --> 3087.62]  validated to the
[3087.62 --> 3088.68]  developer community what
[3088.68 --> 3089.62]  we have been pioneering
[3089.62 --> 3090.72]  over the last years,
[3090.94 --> 3091.50]  that developer
[3091.50 --> 3092.68]  environments need to be
[3092.68 --> 3094.06]  automated and ephemeral.
[3094.28 --> 3094.92]  We are now at the
[3094.92 --> 3096.08]  right place and the
[3096.08 --> 3097.06]  right time to move
[3097.06 --> 3098.08]  software development to
[3098.08 --> 3099.14]  the cloud for everybody,
[3099.38 --> 3100.36]  not just for developers
[3100.36 --> 3101.08]  working for the
[3101.08 --> 3102.20]  Googles, Facebooks or
[3102.20 --> 3103.36]  Shopify's who left
[3103.36 --> 3104.38]  local development already
[3104.38 --> 3105.42]  for several years.
[3105.82 --> 3106.80]  Gitpod is open source
[3106.80 --> 3107.72]  and provisions for
[3107.72 --> 3108.76]  every development team
[3108.76 --> 3110.16]  on GitHub, GitLab and
[3110.16 --> 3111.46]  that bucket cloud-powered
[3111.46 --> 3112.08]  dev environments.
[3112.42 --> 3113.16]  You can access your
[3113.16 --> 3114.00]  developer environments
[3114.00 --> 3115.40]  via upstream VS Code
[3115.40 --> 3116.46]  running on your desktop
[3116.46 --> 3117.92]  or in the browser and
[3117.92 --> 3119.26]  soon also all JetBrains
[3119.26 --> 3119.56]  IDs.
[3120.08 --> 3120.56]  Very cool.
[3120.62 --> 3120.96]  If this gets you
[3120.96 --> 3121.72]  excited, learn more and
[3121.72 --> 3122.84]  get started for free at
[3122.84 --> 3123.94]  gitpod.io.
[3124.26 --> 3125.36]  Gitpod is free for
[3125.36 --> 3126.54]  individual developers for
[3126.54 --> 3127.98]  50 hours a month, can be
[3127.98 --> 3129.16]  self-hosted and is
[3129.16 --> 3130.12]  available for every
[3130.12 --> 3131.02]  developer today.
[3131.50 --> 3132.66]  Again, gitpod.io.
[3132.66 --> 3149.26]  You know, I could, I can
[3149.26 --> 3150.10]  keep going down the
[3150.10 --> 3152.52]  layers of, of next, but I
[3152.52 --> 3153.44]  do want to take a turn
[3153.44 --> 3154.92]  because, you know what,
[3154.92 --> 3155.82]  I'll mention it just
[3155.82 --> 3156.48]  because I have to.
[3156.76 --> 3158.50]  So I don't develop
[3158.50 --> 3160.42]  websites for customers
[3160.42 --> 3161.68]  anymore, right?
[3162.10 --> 3163.08]  But years and years
[3163.08 --> 3163.96]  ago, I can remember
[3163.96 --> 3165.16]  when I was deploying
[3165.16 --> 3166.58]  websites with WordPress
[3166.58 --> 3168.40]  10 years ago even, or
[3168.40 --> 3169.78]  whatever, or some sort
[3169.78 --> 3171.20]  of CMS that, you know,
[3171.20 --> 3172.02]  that was a line item.
[3172.10 --> 3172.94]  That was what we sold.
[3173.76 --> 3175.88]  And they wanted a new
[3175.88 --> 3176.22]  website.
[3176.22 --> 3177.60]  They wanted to have
[3177.60 --> 3178.52]  this ability to sort
[3178.52 --> 3180.42]  of capture, you know,
[3180.44 --> 3181.18]  their market and
[3181.18 --> 3182.08]  showcase their value.
[3182.14 --> 3182.96]  And that's what we came
[3182.96 --> 3183.30]  in and did.
[3183.36 --> 3184.42]  We understood their
[3184.42 --> 3184.72]  brand.
[3184.80 --> 3185.62]  In some cases, it was a
[3185.62 --> 3187.32]  rebrand or it was a
[3187.32 --> 3188.34]  refinement of their brand.
[3188.34 --> 3189.50]  It was establishing their
[3189.50 --> 3190.68]  very first web presence.
[3190.82 --> 3191.72]  So this is years ago.
[3192.12 --> 3192.22]  Yeah.
[3192.28 --> 3193.16]  But I can recall saying
[3193.16 --> 3194.98]  they always had this
[3194.98 --> 3196.32]  need of, I need to be
[3196.32 --> 3198.26]  able to have, I want to
[3198.26 --> 3199.58]  be able to change my
[3199.58 --> 3199.90]  webpage.
[3200.86 --> 3201.82]  And, you know, I can
[3201.82 --> 3202.62]  recall back in those
[3202.62 --> 3204.00]  days, we, we would give
[3204.00 --> 3205.28]  that to them, but it was
[3205.28 --> 3207.60]  terrible because it just
[3207.60 --> 3209.64]  wasn't what I think you're
[3209.64 --> 3210.82]  delivering with next
[3210.82 --> 3211.22]  live.
[3211.22 --> 3212.62]  I think, or next.js live.
[3212.74 --> 3214.64]  I think that we wanted to
[3214.64 --> 3215.86]  as web developers at that
[3215.86 --> 3216.62]  time, and maybe we could
[3216.62 --> 3217.84]  have, but we wanted to
[3217.84 --> 3219.24]  promise that and sell
[3219.24 --> 3220.46]  them that because that's
[3220.46 --> 3221.90]  what they needed, but the
[3221.90 --> 3222.82]  tools weren't evolved
[3222.82 --> 3224.12]  enough to do that.
[3224.22 --> 3226.08]  And now we're at a place
[3226.08 --> 3227.28]  where that's possible,
[3227.54 --> 3227.66]  right?
[3227.70 --> 3229.62]  Like going back in the
[3229.62 --> 3230.32]  last couple of years, we
[3230.32 --> 3231.94]  have seen things happen.
[3232.08 --> 3232.96]  You know, for example,
[3233.46 --> 3234.60]  Gitpod, for example, is a
[3234.60 --> 3236.60]  very close example of at
[3236.60 --> 3237.18]  least the developer
[3237.18 --> 3238.78]  environment being in the
[3238.78 --> 3239.12]  cloud.
[3239.48 --> 3241.20]  But that is one step
[3241.20 --> 3242.24]  removed from what you've
[3242.24 --> 3243.32]  done with next.js live,
[3243.42 --> 3245.10]  which is put that same
[3245.10 --> 3247.26]  power into someone who
[3247.26 --> 3248.34]  is in quotes, not a
[3248.34 --> 3249.80]  developer or less
[3249.80 --> 3250.86]  developer friendly or
[3250.86 --> 3252.14]  whatever terminology you
[3252.14 --> 3252.78]  want to use for that
[3252.78 --> 3253.18]  person.
[3253.64 --> 3254.52]  You know, we wanted to
[3254.52 --> 3256.36]  give the office manager
[3256.36 --> 3257.56]  or the executive
[3257.56 --> 3259.26]  assistant or, you know,
[3259.28 --> 3260.16]  the person next to the
[3260.16 --> 3260.96]  person who runs the
[3260.96 --> 3262.04]  company the power to
[3262.04 --> 3263.60]  change their web
[3263.60 --> 3265.08]  pages, but failed
[3265.08 --> 3265.72]  consistently.
[3265.72 --> 3267.86]  And today I can say
[3267.86 --> 3268.32]  that you're helping
[3268.32 --> 3269.76]  people succeed with that
[3269.76 --> 3271.28]  because you are.
[3271.28 --> 3272.96]  You realize the promise
[3272.96 --> 3273.58]  essentially.
[3274.36 --> 3275.54]  Yeah, I think for the
[3275.54 --> 3276.96]  most part, we have a
[3276.96 --> 3279.38]  lot to thank to this
[3279.38 --> 3280.66]  idea of the component,
[3280.92 --> 3281.18]  right?
[3281.54 --> 3282.42]  The reason that
[3282.42 --> 3284.40]  WordPress couldn't get
[3284.40 --> 3285.64]  there, I think, is
[3285.64 --> 3287.56]  there wasn't a clear
[3287.56 --> 3289.34]  abstraction or
[3289.34 --> 3290.32]  definition between
[3290.32 --> 3291.46]  like, what is it that
[3291.46 --> 3292.12]  you're going to be able
[3292.12 --> 3293.46]  to go and edit,
[3294.08 --> 3294.42]  right?
[3294.82 --> 3296.12]  Is everything just like
[3296.12 --> 3298.12]  a continuum of code
[3298.12 --> 3299.82]  or have you been able to
[3299.82 --> 3301.16]  break it down into the
[3301.16 --> 3302.74]  right building blocks,
[3302.82 --> 3304.50]  the right Lego pieces
[3304.50 --> 3306.42]  that allow anybody in
[3306.42 --> 3307.94]  the world to understand
[3307.94 --> 3308.62]  the construction
[3308.62 --> 3309.22]  process.
[3309.62 --> 3310.54]  This is what I think
[3310.54 --> 3311.62]  our technology is
[3311.62 --> 3312.58]  ultimately allowing,
[3312.74 --> 3312.98]  right?
[3313.06 --> 3314.46]  There's a universality
[3314.46 --> 3316.40]  to this concept that
[3316.40 --> 3317.76]  is fascinating to
[3317.76 --> 3318.50]  ponder, I think,
[3318.56 --> 3320.52]  because anybody can
[3320.52 --> 3321.02]  develop.
[3321.24 --> 3321.34]  Yeah.
[3321.64 --> 3322.44]  Just like anybody
[3322.44 --> 3324.22]  could sit down and
[3324.22 --> 3325.96]  build amazing things
[3325.96 --> 3327.36]  out of Legos, right?
[3327.78 --> 3329.38]  Now, it's fine that
[3329.38 --> 3330.28]  there's going to be the
[3330.28 --> 3331.02]  folks that can,
[3331.16 --> 3332.36]  create the new types
[3332.36 --> 3334.26]  of pieces and can
[3334.26 --> 3335.68]  understand the,
[3336.02 --> 3336.84]  how you even get
[3336.84 --> 3339.08]  to the primitives
[3339.08 --> 3340.16]  that you're handing
[3340.16 --> 3341.72]  off to the person
[3341.72 --> 3342.12]  that's building
[3342.12 --> 3342.66]  something.
[3342.86 --> 3343.58]  For sure.
[3343.82 --> 3344.28]  You know, there's
[3344.28 --> 3345.14]  going to be engineers
[3345.14 --> 3346.86]  that work on all the
[3346.86 --> 3349.30]  layers down and
[3349.30 --> 3350.40]  they will continue to
[3350.40 --> 3350.96]  thrive.
[3351.30 --> 3352.40]  But I do think that
[3352.40 --> 3353.92]  the world is overdue
[3353.92 --> 3355.36]  for a transformation
[3355.36 --> 3357.34]  of making building
[3357.34 --> 3358.28]  really more accessible,
[3358.38 --> 3359.12]  more approachable.
[3359.12 --> 3360.56]  and we're very,
[3360.70 --> 3361.70]  very happy that we
[3361.70 --> 3362.32]  have an opportunity
[3362.32 --> 3363.24]  to contribute to that.
[3363.70 --> 3364.50]  And something that
[3364.50 --> 3365.52]  you had said when we
[3365.52 --> 3366.28]  talked about your
[3366.28 --> 3367.10]  goals for your future.
[3367.28 --> 3369.50]  So prior to doing
[3369.50 --> 3370.26]  these episodes,
[3370.58 --> 3372.00]  I ask a few questions
[3372.00 --> 3373.02]  to sort of prime the
[3373.02 --> 3373.52]  conversation.
[3373.68 --> 3374.26]  Not all the material
[3374.26 --> 3375.28]  makes it into the show,
[3375.34 --> 3376.62]  but a lot of it helps
[3376.62 --> 3378.60]  me understand your
[3378.60 --> 3379.24]  mindset, your
[3379.24 --> 3380.02]  framework reference
[3380.02 --> 3380.52]  and whatnot.
[3380.66 --> 3381.56]  One of the ones I ask
[3381.56 --> 3381.94]  you is what are your
[3381.94 --> 3382.66]  goals for the future?
[3383.22 --> 3383.86]  And you said there's a
[3383.86 --> 3384.64]  very unique opportunity
[3384.64 --> 3385.54]  to turn a lot more
[3385.54 --> 3386.80]  people into authors
[3386.80 --> 3387.62]  of the web.
[3388.00 --> 3388.20]  Yes.
[3388.34 --> 3389.32]  So what I mean by this
[3389.32 --> 3390.20]  is that the web has
[3390.20 --> 3391.38]  succeeded in making
[3391.38 --> 3392.28]  everyone be able to
[3392.28 --> 3393.14]  consume it really
[3393.14 --> 3393.60]  easily.
[3394.32 --> 3395.20]  I would assume you'd
[3395.20 --> 3396.08]  go on and say more
[3396.08 --> 3396.90]  about making the web,
[3397.00 --> 3397.42]  but, you know,
[3397.42 --> 3398.44]  kind of focusing on
[3398.44 --> 3399.74]  this opportunity to
[3399.74 --> 3400.50]  turn a lot of people
[3400.50 --> 3401.84]  into authors of the
[3401.84 --> 3402.00]  web.
[3402.08 --> 3403.54]  And that to me is
[3403.54 --> 3404.22]  super cool because
[3404.22 --> 3405.06]  you think of a
[3405.06 --> 3405.40]  creator.
[3405.66 --> 3406.26]  You might think,
[3406.50 --> 3406.76]  okay, well,
[3406.78 --> 3407.42]  that's a YouTuber
[3407.42 --> 3409.04]  or that's a TikToker
[3409.04 --> 3409.70]  or, you know,
[3409.70 --> 3410.18]  someone who does
[3410.18 --> 3411.00]  TikTok or whatever.
[3411.12 --> 3411.74]  How have you framed
[3411.74 --> 3412.06]  those?
[3412.46 --> 3413.28]  And the web is sort
[3413.28 --> 3413.96]  of this place where
[3413.96 --> 3414.46]  we haven't really
[3414.46 --> 3415.88]  thought about enabling
[3415.88 --> 3416.74]  more authors.
[3416.86 --> 3417.32]  We think of them
[3417.32 --> 3418.12]  just simply as
[3418.12 --> 3418.58]  developers.
[3419.34 --> 3420.24]  Not that developers
[3420.24 --> 3421.04]  aren't cool because
[3421.04 --> 3421.72]  they, of course,
[3421.82 --> 3423.34]  are, but this idea
[3423.34 --> 3424.54]  of enabling a lot
[3424.54 --> 3425.18]  more people to
[3425.18 --> 3425.80]  author the web,
[3425.86 --> 3426.16]  I think,
[3426.24 --> 3426.82]  is a pretty
[3426.82 --> 3427.78]  astounding thing.
[3428.78 --> 3429.16]  One thing I want
[3429.16 --> 3429.54]  to talk to you
[3429.54 --> 3430.36]  about is you
[3430.36 --> 3431.68]  mentioned how you
[3431.68 --> 3432.84]  think about
[3432.84 --> 3433.48]  frameworks.
[3434.34 --> 3434.96]  And what I often
[3434.96 --> 3436.06]  want to know is
[3436.06 --> 3436.66]  how do you know
[3436.66 --> 3437.18]  how to think,
[3437.38 --> 3437.60]  Guillermo,
[3437.86 --> 3438.22]  essentially?
[3438.74 --> 3439.32]  Do you have a
[3439.32 --> 3440.12]  CEO coach?
[3440.54 --> 3441.26]  Are you just very
[3441.26 --> 3441.72]  smart?
[3442.22 --> 3442.78]  Do you read lots
[3442.78 --> 3443.26]  of books?
[3443.66 --> 3443.84]  You know,
[3443.92 --> 3444.46]  what is your
[3444.46 --> 3445.22]  ingestion of
[3445.22 --> 3445.50]  knowledge?
[3445.62 --> 3445.98]  Where do you
[3445.98 --> 3446.90]  get wisdom
[3446.90 --> 3447.82]  poured into you?
[3448.28 --> 3448.80]  How do you
[3448.80 --> 3450.48]  get to thinking
[3450.48 --> 3450.98]  the way you
[3450.98 --> 3451.24]  think,
[3451.32 --> 3451.64]  essentially?
[3452.34 --> 3452.94]  I would say
[3452.94 --> 3454.02]  I've developed
[3454.02 --> 3454.78]  the privilege
[3454.78 --> 3457.32]  of being able
[3457.32 --> 3458.32]  to ask lots
[3458.32 --> 3458.96]  of questions.
[3459.60 --> 3460.34]  And I mentioned
[3460.34 --> 3461.10]  that that's a
[3461.10 --> 3462.80]  privilege because
[3462.80 --> 3464.10]  of many reasons.
[3464.72 --> 3465.16]  Obviously,
[3465.28 --> 3465.98]  I've had the
[3465.98 --> 3467.22]  support of
[3467.22 --> 3468.08]  our entire
[3468.08 --> 3468.96]  community and
[3468.96 --> 3469.96]  investors and
[3469.96 --> 3471.40]  creating really
[3471.40 --> 3472.24]  awesome networks
[3472.24 --> 3472.94]  of people that
[3472.94 --> 3473.36]  you can ask
[3473.36 --> 3474.10]  questions to.
[3474.10 --> 3475.04]  But the
[3475.04 --> 3475.48]  other way
[3475.48 --> 3476.28]  that's a
[3476.28 --> 3476.64]  privilege,
[3476.78 --> 3477.12]  I think,
[3477.24 --> 3477.94]  is it relates
[3477.94 --> 3478.32]  to actually
[3478.32 --> 3478.64]  what you
[3478.64 --> 3479.46]  mentioned about
[3479.46 --> 3480.98]  imposter syndrome
[3480.98 --> 3483.52]  because I've
[3483.52 --> 3484.00]  gotten to the
[3484.00 --> 3484.34]  point where
[3484.34 --> 3485.28]  asking questions
[3485.28 --> 3487.32]  becomes easier
[3487.32 --> 3488.02]  in so many
[3488.02 --> 3488.36]  ways.
[3488.50 --> 3489.72]  I think asking
[3489.72 --> 3490.64]  a question can
[3490.64 --> 3491.78]  have the opposite
[3491.78 --> 3492.46]  effect for a lot
[3492.46 --> 3492.90]  of you because
[3492.90 --> 3494.44]  you're trying to
[3494.44 --> 3495.56]  unblock yourself,
[3495.78 --> 3496.20]  unlock,
[3496.38 --> 3496.64]  learn,
[3497.24 --> 3498.40]  but sometimes
[3498.40 --> 3498.92]  it can be like,
[3499.00 --> 3499.56]  well, if I ask
[3499.56 --> 3500.14]  that question,
[3500.90 --> 3501.64]  it creates more
[3501.64 --> 3502.02]  doubt.
[3502.02 --> 3502.32]  It creates
[3502.32 --> 3503.20]  internal questions
[3503.20 --> 3504.40]  about how you're
[3504.40 --> 3504.68]  going to be
[3504.68 --> 3505.50]  perceived, for
[3505.50 --> 3505.84]  example.
[3506.46 --> 3508.56]  So I evolved
[3508.56 --> 3509.16]  through asking
[3509.16 --> 3509.56]  lots of
[3509.56 --> 3510.02]  questions.
[3510.28 --> 3510.84]  Coaches,
[3511.40 --> 3511.86]  advisors,
[3512.32 --> 3512.76]  investors,
[3513.16 --> 3513.64]  customers,
[3514.40 --> 3515.46]  ask a way
[3515.46 --> 3516.46]  to really
[3516.46 --> 3516.88]  learn.
[3518.26 --> 3519.00]  And I mean,
[3519.00 --> 3519.20]  there is
[3519.20 --> 3519.80]  something quite
[3519.80 --> 3521.18]  primordial there,
[3521.22 --> 3521.74]  I would say.
[3522.28 --> 3523.48]  It's ask and
[3523.48 --> 3524.16]  you shall receive.
[3524.38 --> 3524.92]  I think I
[3524.92 --> 3526.36]  found that it's
[3526.36 --> 3526.92]  been true for
[3526.92 --> 3527.38]  us.
[3527.38 --> 3528.72]  obviously it's
[3528.72 --> 3529.42]  not always
[3529.42 --> 3530.30]  easy and
[3530.30 --> 3531.14]  you have to
[3531.14 --> 3531.82]  also find the
[3531.82 --> 3532.90]  right people to
[3532.90 --> 3533.52]  ask the questions
[3533.52 --> 3534.62]  to, but the
[3534.62 --> 3535.30]  information is
[3535.30 --> 3535.96]  there and it's
[3535.96 --> 3536.64]  a very open
[3536.64 --> 3537.50]  world and
[3537.50 --> 3538.40]  you'd be surprised
[3538.40 --> 3539.44]  about how
[3539.44 --> 3540.88]  much possibility
[3540.88 --> 3542.40]  is just one
[3542.40 --> 3543.18]  question away
[3543.18 --> 3544.30]  to the right
[3544.30 --> 3544.80]  person.
[3544.98 --> 3545.72]  I actually even
[3545.72 --> 3546.46]  spend time
[3546.46 --> 3548.18]  still answering
[3548.18 --> 3549.16]  cold emails here
[3549.16 --> 3549.44]  and there.
[3549.56 --> 3549.78]  Obviously,
[3549.94 --> 3550.56]  they are getting
[3550.56 --> 3550.90]  to the point
[3550.90 --> 3551.72]  where there are
[3551.72 --> 3552.42]  way too many,
[3552.58 --> 3553.90]  but I appreciate
[3553.90 --> 3554.66]  people's willingness
[3554.66 --> 3555.86]  to ask either
[3555.86 --> 3556.58]  for help or
[3556.58 --> 3557.26]  for information,
[3557.38 --> 3558.16]  or really
[3558.16 --> 3558.64]  whatever they
[3558.64 --> 3558.94]  need.
[3560.26 --> 3561.54]  And yeah,
[3561.60 --> 3562.48]  that's a primary
[3562.48 --> 3563.24]  framework there.
[3563.46 --> 3564.00]  It sounds
[3564.00 --> 3565.80]  deceptively simple,
[3565.92 --> 3566.28]  but as you
[3566.28 --> 3566.64]  pointed out
[3566.64 --> 3567.08]  before,
[3567.70 --> 3568.14]  it can be
[3568.14 --> 3568.78]  quite hard.
[3568.94 --> 3569.54]  And also,
[3570.38 --> 3570.92]  a simple
[3570.92 --> 3571.48]  framework I
[3571.48 --> 3572.20]  have here too
[3572.20 --> 3573.32]  is that there
[3573.32 --> 3573.88]  can only be
[3573.88 --> 3574.82]  one priority,
[3575.28 --> 3575.60]  right?
[3575.78 --> 3576.40]  If you have
[3576.40 --> 3577.26]  multiple priorities,
[3577.38 --> 3578.14]  then you've
[3578.14 --> 3579.32]  broken the rule
[3579.32 --> 3580.20]  or you've
[3580.20 --> 3581.26]  broken the word
[3581.26 --> 3582.26]  or the semantics
[3582.26 --> 3582.76]  of the word,
[3582.84 --> 3583.00]  right?
[3583.00 --> 3583.52]  So there can
[3583.52 --> 3584.14]  only be one
[3584.14 --> 3585.84]  thing and
[3585.84 --> 3586.76]  as the
[3586.76 --> 3587.86]  machine becomes
[3587.86 --> 3588.78]  more complex,
[3588.78 --> 3591.10]  as more and
[3591.10 --> 3591.70]  more people
[3591.70 --> 3592.64]  join the
[3592.64 --> 3593.44]  ecosystem or
[3593.44 --> 3593.94]  the company,
[3594.10 --> 3594.48]  et cetera,
[3595.20 --> 3595.54]  you have to
[3595.54 --> 3596.54]  be very clear
[3596.54 --> 3598.38]  in what you
[3598.38 --> 3599.64]  say or
[3599.64 --> 3600.72]  where you ask
[3600.72 --> 3601.72]  and what you
[3601.72 --> 3602.28]  prioritize.
[3602.86 --> 3603.62]  So there can
[3603.62 --> 3604.22]  only be one
[3604.22 --> 3605.24]  thing and
[3605.24 --> 3605.86]  that means
[3605.86 --> 3606.46]  that your
[3606.46 --> 3608.12]  question is
[3608.12 --> 3608.94]  very valuable
[3608.94 --> 3609.66]  as well
[3609.66 --> 3611.26]  and that you
[3611.26 --> 3611.88]  might want to
[3611.88 --> 3612.82]  spend the most
[3612.82 --> 3613.34]  amount of time
[3613.34 --> 3614.80]  energy possibly
[3614.80 --> 3615.34]  in preparing
[3615.34 --> 3616.20]  correctly as
[3616.20 --> 3616.42]  well.
[3616.86 --> 3617.22]  Are there any
[3617.22 --> 3617.82]  habits that you
[3617.82 --> 3618.62]  think you have
[3618.62 --> 3619.26]  or you know
[3619.26 --> 3620.06]  you have that
[3620.06 --> 3621.42]  are sort of
[3621.42 --> 3621.74]  like,
[3622.08 --> 3623.26]  these are my
[3623.26 --> 3624.38]  secret sauce?
[3625.08 --> 3625.40]  Think about
[3625.40 --> 3626.10]  habits for me
[3626.10 --> 3626.80]  and I'm like,
[3626.86 --> 3627.16]  you know,
[3627.76 --> 3628.26]  just spending
[3628.26 --> 3628.72]  time with my
[3628.72 --> 3629.84]  family is oddly
[3629.84 --> 3630.34]  a weird
[3630.34 --> 3630.96]  productive habit
[3630.96 --> 3631.90]  for me because
[3631.90 --> 3633.42]  you wouldn't
[3633.42 --> 3633.88]  think that would
[3633.88 --> 3634.30]  be a habit.
[3634.44 --> 3634.54]  Like,
[3634.64 --> 3635.12]  I love my
[3635.12 --> 3635.76]  family a lot
[3635.76 --> 3636.52]  and I need
[3636.52 --> 3636.86]  them,
[3637.06 --> 3637.28]  right?
[3637.92 --> 3638.52]  And so I
[3638.52 --> 3639.58]  prioritize spending
[3639.58 --> 3640.16]  my time with
[3640.16 --> 3640.44]  them.
[3640.96 --> 3641.76]  And for me,
[3641.86 --> 3642.00]  like,
[3642.08 --> 3642.52]  that's what
[3642.52 --> 3643.04]  gives me the
[3643.04 --> 3643.54]  energy to be
[3643.54 --> 3643.96]  able to step
[3643.96 --> 3645.36]  away when
[3645.36 --> 3645.94]  necessary,
[3646.24 --> 3646.68]  which is
[3646.68 --> 3648.00]  obviously it's
[3648.00 --> 3648.64]  a job and I
[3648.64 --> 3649.26]  do what I do,
[3649.42 --> 3649.64]  but,
[3650.04 --> 3650.36]  you know,
[3650.48 --> 3651.38]  I have to
[3651.38 --> 3652.30]  prioritize my
[3652.30 --> 3652.70]  time with
[3652.70 --> 3653.00]  them.
[3653.62 --> 3654.02]  So that's one
[3654.02 --> 3654.76]  of my sort
[3654.76 --> 3655.08]  of like,
[3655.58 --> 3656.04]  wouldn't really
[3656.04 --> 3656.44]  call it a
[3656.44 --> 3657.18]  habit necessarily,
[3657.18 --> 3658.06]  but I think of
[3658.06 --> 3658.62]  it as a habit
[3658.62 --> 3659.86]  because I need
[3659.86 --> 3660.64]  to spend that
[3660.64 --> 3661.26]  time with them.
[3661.76 --> 3662.24]  I'm curious if
[3662.24 --> 3662.56]  you've thought
[3662.56 --> 3662.96]  through any
[3662.96 --> 3663.82]  specific habits
[3663.82 --> 3664.22]  for yourself
[3664.22 --> 3665.38]  that help you
[3665.38 --> 3666.60]  be as strong
[3666.60 --> 3667.14]  as you are
[3667.14 --> 3667.56]  in the day
[3667.56 --> 3667.88]  to day.
[3668.52 --> 3668.98]  It's cliche,
[3669.20 --> 3669.72]  but I have
[3669.72 --> 3670.50]  to say
[3670.50 --> 3672.66]  exercise and
[3672.66 --> 3673.22]  meditation,
[3673.60 --> 3674.50]  which I consider
[3674.50 --> 3674.96]  to be a
[3674.96 --> 3676.34]  continuum because
[3676.34 --> 3676.98]  for me,
[3677.58 --> 3678.26]  running for
[3678.26 --> 3678.76]  long periods
[3678.76 --> 3679.42]  of time,
[3679.92 --> 3680.86]  I enter a
[3680.86 --> 3681.72]  meditative state
[3681.72 --> 3682.44]  and I'm able
[3682.44 --> 3683.58]  to think
[3683.58 --> 3684.36]  through and
[3684.36 --> 3685.44]  solve problems.
[3686.20 --> 3687.44]  I'm by nature,
[3687.70 --> 3688.54]  I should say,
[3689.08 --> 3690.14]  a quite competitive
[3690.14 --> 3690.66]  person.
[3691.26 --> 3692.22]  I really enjoy
[3692.22 --> 3693.06]  competition through
[3693.06 --> 3694.04]  exercise and
[3694.04 --> 3695.58]  like just running
[3695.58 --> 3697.12]  and try to be
[3697.12 --> 3698.26]  faster or,
[3698.86 --> 3699.10]  I don't know,
[3699.10 --> 3700.40]  doing some new
[3700.40 --> 3700.84]  thing that I
[3700.84 --> 3701.14]  couldn't do
[3701.14 --> 3701.58]  before.
[3702.16 --> 3703.00]  So I'm very
[3703.00 --> 3704.88]  much competitive
[3704.88 --> 3705.80]  by nature.
[3705.94 --> 3706.80]  I think sports
[3706.80 --> 3707.82]  and exercise
[3707.82 --> 3708.92]  could awesome
[3708.92 --> 3709.58]  frameworks for
[3709.58 --> 3710.16]  a competition
[3710.16 --> 3711.94]  that I just
[3711.94 --> 3712.46]  enjoy.
[3712.98 --> 3713.94]  Going back to
[3713.94 --> 3714.94]  preparing the
[3714.94 --> 3715.76]  right question
[3715.76 --> 3716.70]  or deciding
[3716.70 --> 3717.16]  the next
[3717.16 --> 3717.68]  priority,
[3718.24 --> 3719.06]  I think that's
[3719.06 --> 3720.00]  nearly impossible
[3720.00 --> 3721.22]  to do without
[3721.22 --> 3722.46]  prolonged
[3722.46 --> 3723.08]  meditation.
[3723.58 --> 3724.02]  And I'm not
[3724.02 --> 3724.60]  talking just about
[3724.60 --> 3725.80]  meditation of the
[3725.80 --> 3726.72]  kind of,
[3726.72 --> 3727.58]  I'm sitting
[3727.58 --> 3728.42]  under a tree
[3728.42 --> 3729.36]  in the
[3729.36 --> 3730.06]  Himalayas.
[3730.30 --> 3730.70]  I'm talking
[3730.70 --> 3731.44]  about even
[3731.44 --> 3732.26]  just sitting
[3732.26 --> 3733.56]  down and
[3733.56 --> 3733.84]  thinking.
[3734.62 --> 3735.36]  I'm a big
[3735.36 --> 3736.06]  believer in
[3736.06 --> 3736.72]  background
[3736.72 --> 3738.04]  asynchronous work,
[3738.38 --> 3739.04]  not because I
[3739.04 --> 3740.74]  worked my entire
[3740.74 --> 3741.18]  career with
[3741.18 --> 3741.54]  JavaScript,
[3742.10 --> 3743.18]  but I'm a big
[3743.18 --> 3744.04]  believer that
[3744.04 --> 3745.62]  when you
[3745.62 --> 3746.30]  configure the
[3746.30 --> 3747.44]  right question
[3747.44 --> 3748.42]  for yourself,
[3748.76 --> 3749.26]  an internal
[3749.26 --> 3750.10]  question like,
[3750.74 --> 3751.32]  what should I
[3751.32 --> 3752.04]  learn next?
[3752.04 --> 3753.78]  the answer
[3753.78 --> 3754.18]  can be
[3754.18 --> 3754.62]  produced
[3754.62 --> 3755.60]  asynchronously
[3755.60 --> 3757.54]  through doing
[3757.54 --> 3758.24]  other activities
[3758.24 --> 3759.08]  like spending
[3759.08 --> 3759.76]  time with your
[3759.76 --> 3761.24]  family or
[3761.24 --> 3763.14]  exercising or
[3763.14 --> 3764.00]  walking around
[3764.00 --> 3765.20]  or reading a
[3765.20 --> 3765.38]  book.
[3765.82 --> 3766.50]  In fact, I
[3766.50 --> 3766.98]  always notice
[3766.98 --> 3767.46]  that I'm
[3767.46 --> 3767.82]  reading a
[3767.82 --> 3768.84]  book and I
[3768.84 --> 3769.32]  always catch
[3769.32 --> 3769.94]  myself not
[3769.94 --> 3770.38]  reading the
[3770.38 --> 3770.60]  book.
[3771.46 --> 3772.12]  That's why I
[3772.12 --> 3772.54]  actually don't
[3772.54 --> 3773.02]  read books
[3773.02 --> 3774.92]  because it's a
[3774.92 --> 3775.60]  performative
[3775.60 --> 3777.72]  action of I
[3777.72 --> 3778.32]  sit down and
[3778.32 --> 3778.74]  look at the
[3778.74 --> 3779.14]  page.
[3780.08 --> 3780.52]  And sometimes
[3780.52 --> 3781.04]  the book is
[3781.04 --> 3781.46]  really good.
[3781.46 --> 3781.86]  I do get
[3781.86 --> 3782.14]  into the
[3782.14 --> 3782.30]  book.
[3782.44 --> 3782.98]  But for
[3782.98 --> 3783.26]  the most
[3783.26 --> 3784.34]  part, my
[3784.34 --> 3784.86]  mind goes
[3784.86 --> 3785.22]  into that
[3785.22 --> 3785.54]  background
[3785.54 --> 3786.42]  processing of
[3786.42 --> 3786.92]  other things
[3786.92 --> 3787.28]  to do.
[3788.20 --> 3788.98]  And I
[3788.98 --> 3789.42]  find that
[3789.42 --> 3789.80]  awesome.
[3789.92 --> 3790.26]  It happens
[3790.26 --> 3790.88]  with dreams
[3790.88 --> 3792.24]  as well for
[3792.24 --> 3793.54]  me where a
[3793.54 --> 3794.26]  lot of my
[3794.26 --> 3795.30]  thinking also
[3795.30 --> 3796.80]  happens at
[3796.80 --> 3797.62]  night while
[3797.62 --> 3798.08]  I sleep.
[3798.86 --> 3799.86]  So, yeah,
[3800.10 --> 3801.00]  staying healthy
[3801.00 --> 3802.30]  and connected
[3802.30 --> 3803.10]  is, I think,
[3803.56 --> 3804.12]  the number one
[3804.12 --> 3804.66]  priority from
[3804.66 --> 3805.32]  which everything
[3805.32 --> 3806.78]  is downstream
[3806.78 --> 3807.62]  from that, I
[3807.62 --> 3808.42]  think, ultimately.
[3809.22 --> 3809.74]  Everything's
[3809.74 --> 3810.14]  downstream from
[3810.14 --> 3810.38]  health.
[3810.38 --> 3811.06]  There's this
[3811.06 --> 3812.48]  awesome, a
[3812.48 --> 3812.78]  lot of people
[3812.78 --> 3813.24]  think it's
[3813.24 --> 3814.50]  corny and
[3814.50 --> 3815.60]  weird, and I
[3815.60 --> 3816.26]  think I would
[3816.26 --> 3816.92]  agree to some
[3816.92 --> 3817.58]  extent as well,
[3817.64 --> 3817.92]  but the
[3817.92 --> 3819.66]  soft bank deck
[3819.66 --> 3820.26]  of their
[3820.26 --> 3821.16]  vision fund,
[3821.66 --> 3822.16]  what I think
[3822.16 --> 3822.64]  is awesome
[3822.64 --> 3823.28]  about it is
[3823.28 --> 3824.16]  that it
[3824.16 --> 3824.60]  explains in
[3824.60 --> 3825.16]  very simple
[3825.16 --> 3825.76]  terms what
[3825.76 --> 3826.84]  their ideal of
[3826.84 --> 3827.86]  the future is
[3827.86 --> 3828.70]  and how they're
[3828.70 --> 3829.48]  going to invest
[3829.48 --> 3830.04]  to make that
[3830.04 --> 3830.84]  future happen.
[3831.54 --> 3831.84]  And it has
[3831.84 --> 3832.88]  this slide that
[3832.88 --> 3834.42]  says, for us,
[3834.48 --> 3835.38]  it's all about
[3835.38 --> 3836.84]  making people
[3836.84 --> 3837.70]  happy and
[3837.70 --> 3838.54]  removing suffering
[3838.54 --> 3838.94]  from the
[3838.94 --> 3839.26]  world.
[3839.92 --> 3840.46]  I think it
[3840.46 --> 3841.38]  is as simple
[3841.38 --> 3841.80]  as that.
[3841.88 --> 3842.66]  It's about
[3842.66 --> 3844.00]  prioritizing
[3844.00 --> 3846.48]  happiness, which
[3846.48 --> 3847.58]  is not
[3847.58 --> 3848.44]  necessarily defined
[3848.44 --> 3849.26]  by joy.
[3849.50 --> 3850.02]  It can also be
[3850.02 --> 3850.44]  defined by
[3850.44 --> 3851.24]  challenge and
[3851.24 --> 3852.88]  competition and
[3852.88 --> 3854.00]  some amount of
[3854.00 --> 3855.14]  stress in terms
[3855.14 --> 3856.28]  of becoming
[3856.28 --> 3857.02]  better and
[3857.02 --> 3857.58]  achieving an
[3857.58 --> 3858.38]  award at the
[3858.38 --> 3858.66]  end.
[3859.16 --> 3860.00]  I like to
[3860.00 --> 3861.36]  stick to those
[3861.36 --> 3862.02]  simple things.
[3862.02 --> 3862.66]  Yeah.
[3863.30 --> 3863.88]  You mentioned
[3863.88 --> 3866.14]  meditation and
[3866.14 --> 3866.66]  I think an
[3866.66 --> 3867.54]  alternate word
[3867.54 --> 3868.86]  I might consider
[3868.86 --> 3869.88]  based upon your
[3869.88 --> 3871.30]  definition would
[3871.30 --> 3872.26]  be contemplation.
[3872.52 --> 3873.06]  Yeah, that's
[3873.06 --> 3873.30]  great.
[3873.42 --> 3874.22]  Back in
[3874.22 --> 3875.56]  Cornelius
[3875.56 --> 3876.28]  Vanderbilt's
[3876.28 --> 3876.86]  day, you
[3876.86 --> 3877.08]  know, the
[3877.08 --> 3877.76]  early pioneers
[3877.76 --> 3878.18]  of our
[3878.18 --> 3879.68]  country here
[3879.68 --> 3879.92]  in the United
[3879.92 --> 3880.82]  States, there's
[3880.82 --> 3882.52]  a few well-known
[3882.52 --> 3883.76]  entrepreneurs that
[3883.76 --> 3884.72]  really pioneered
[3884.72 --> 3886.26]  what entrepreneurship
[3886.26 --> 3887.28]  is, early
[3887.28 --> 3887.64]  entrepreneurs
[3887.64 --> 3888.06]  essentially.
[3888.06 --> 3889.64]  And this is a
[3889.64 --> 3890.16]  day when they
[3890.16 --> 3890.82]  didn't have
[3890.82 --> 3892.68]  Next.js Live or
[3892.68 --> 3893.72]  the internet or
[3893.72 --> 3894.68]  an iPhone in
[3894.68 --> 3895.10]  their pocket,
[3895.20 --> 3895.32]  right?
[3895.34 --> 3895.74]  They didn't have
[3895.74 --> 3897.22]  all these, one,
[3897.46 --> 3898.24]  possibilities and
[3898.24 --> 3899.58]  opportunities, but
[3899.58 --> 3900.34]  at the same time,
[3900.50 --> 3901.20]  to some degree,
[3901.84 --> 3902.62]  quite a distraction
[3902.62 --> 3904.28]  to send a
[3904.28 --> 3905.94]  message to their
[3905.94 --> 3907.14]  manager on a
[3907.14 --> 3907.58]  thing they were
[3907.58 --> 3907.90]  building.
[3908.06 --> 3908.34]  They would
[3908.34 --> 3908.96]  literally have to
[3908.96 --> 3910.50]  send a person
[3910.50 --> 3911.56]  with a message
[3911.56 --> 3912.92]  days on end to
[3912.92 --> 3913.72]  deliver that message
[3913.72 --> 3914.04]  and they would
[3914.04 --> 3914.58]  wait for it to
[3914.58 --> 3915.10]  come back.
[3915.62 --> 3916.06]  And so in
[3916.06 --> 3917.06]  between that
[3917.06 --> 3917.54]  latency,
[3918.06 --> 3918.82]  they would
[3918.82 --> 3920.20]  have room,
[3920.62 --> 3921.32]  room for
[3921.32 --> 3922.24]  thinking, room
[3922.24 --> 3923.14]  for contemplation.
[3923.60 --> 3923.94]  And I remember
[3923.94 --> 3924.52]  reading, because I
[3924.52 --> 3925.40]  read this biography,
[3926.08 --> 3926.52]  that he would
[3926.52 --> 3927.30]  just take naps,
[3927.74 --> 3928.46]  like during what
[3928.46 --> 3928.88]  we call the
[3928.88 --> 3929.72]  work day, right?
[3929.82 --> 3930.54]  Like just take a
[3930.54 --> 3930.84]  nap.
[3930.92 --> 3931.12]  Yeah.
[3931.48 --> 3932.38]  Because he could,
[3932.88 --> 3933.24]  you know, not
[3933.24 --> 3933.72]  because he could
[3933.72 --> 3934.12]  because he was so
[3934.12 --> 3934.86]  powerful, but like
[3934.86 --> 3936.14]  that's just the
[3936.14 --> 3936.76]  nature, that was
[3936.76 --> 3937.50]  doing business, that
[3937.50 --> 3938.26]  was working, taking
[3938.26 --> 3938.74]  a nap and
[3938.74 --> 3939.24]  contemplating.
[3939.52 --> 3939.94]  Yeah, I cannot
[3939.94 --> 3941.02]  possibly agree more
[3941.02 --> 3942.30]  with that sentiment
[3942.30 --> 3943.80]  because I think the
[3943.80 --> 3944.56]  internet has made
[3944.56 --> 3945.58]  us all hyper
[3945.58 --> 3947.28]  connected, but the
[3947.28 --> 3949.90]  benefits are not
[3949.90 --> 3951.46]  in the places I
[3951.46 --> 3952.54]  think in which,
[3953.28 --> 3954.28]  like I think it
[3954.28 --> 3954.64]  could have been
[3954.64 --> 3955.32]  easy to say, well,
[3955.32 --> 3955.86]  we're going to be
[3955.86 --> 3956.74]  a hundred times
[3956.74 --> 3957.28]  smarter.
[3957.56 --> 3958.34]  Like when you know
[3958.34 --> 3959.42]  when like science
[3959.42 --> 3960.48]  fiction folks like
[3960.48 --> 3961.28]  make predictions on
[3961.28 --> 3961.98]  the future, we're all
[3961.98 --> 3962.60]  going to be super
[3962.60 --> 3963.90]  connected and we're
[3963.90 --> 3964.38]  going to be a hundred
[3964.38 --> 3965.02]  times smarter.
[3965.02 --> 3966.98]  I think we're a hundred
[3966.98 --> 3967.92]  times smarter
[3967.92 --> 3969.32]  collectively through
[3969.32 --> 3970.42]  some efficiencies that
[3970.42 --> 3971.12]  we've generated with
[3971.12 --> 3972.44]  the internet, but I
[3972.44 --> 3973.40]  think individually the
[3973.40 --> 3974.34]  person that was in
[3974.34 --> 3975.52]  that position of deep
[3975.52 --> 3977.34]  contemplation, deep
[3977.34 --> 3979.36]  thought in a combined
[3979.36 --> 3980.76]  state of relaxation
[3980.76 --> 3982.84]  with work and good
[3982.84 --> 3983.60]  balance there and
[3983.60 --> 3985.44]  whatnot, that person
[3985.44 --> 3986.24]  competing with you
[3986.24 --> 3987.64]  today, I don't know
[3987.64 --> 3988.54]  if you're better with
[3988.54 --> 3989.62]  your, all your
[3989.62 --> 3990.58]  technology and whatnot
[3990.58 --> 3992.98]  in raw intellectual
[3992.98 --> 3993.92]  power, for example.
[3993.92 --> 3995.12]  I think I would even
[3995.12 --> 3996.14]  say certainly not.
[3997.10 --> 3997.72]  And I think in some
[3997.72 --> 3999.74]  ways our need is now
[3999.74 --> 4001.40]  to recover and claim
[4001.40 --> 4003.10]  back some of those
[4003.10 --> 4004.96]  techniques while we
[4004.96 --> 4006.22]  continue to merge
[4006.22 --> 4007.50]  with the machine into
[4007.50 --> 4009.08]  cyberspace, right?
[4009.40 --> 4010.18]  And this is why I
[4010.18 --> 4010.86]  always emphasize
[4010.86 --> 4012.24]  exercise because it's
[4012.24 --> 4014.80]  very primitive and
[4014.80 --> 4015.38]  primordial.
[4015.94 --> 4017.58]  It's you confronted
[4017.58 --> 4020.36]  with the terrain and
[4020.36 --> 4021.92]  the elements of
[4021.92 --> 4022.24]  weather.
[4022.24 --> 4024.64]  It's like down to
[4024.64 --> 4025.60]  the metal, basically,
[4026.00 --> 4027.04]  of the compute of
[4027.04 --> 4027.50]  your body.
[4027.66 --> 4028.92]  So it's an experience
[4028.92 --> 4030.10]  that is ultimately
[4030.10 --> 4031.90]  even more necessary
[4031.90 --> 4032.92]  today, even though it's
[4032.92 --> 4033.52]  just so basic.
[4034.06 --> 4034.14]  Yeah.
[4034.80 --> 4035.68]  Well, it's been fun
[4035.68 --> 4036.90]  talking to you through
[4036.90 --> 4038.56]  product and journey,
[4039.30 --> 4039.96]  frameworks,
[4040.62 --> 4041.38]  prioritization,
[4042.44 --> 4043.20]  obsession on the
[4043.20 --> 4044.30]  customer and their
[4044.30 --> 4044.94]  success.
[4044.94 --> 4046.44]  I mentioned earlier,
[4047.16 --> 4048.70]  congratulations for
[4048.70 --> 4050.16]  your recent Series C.
[4050.98 --> 4052.76]  Amazing next steps for
[4052.76 --> 4052.88]  you.
[4052.94 --> 4054.54]  But I'm curious where
[4054.54 --> 4055.34]  you're going from here.
[4055.90 --> 4056.82]  When you think about
[4056.82 --> 4059.18]  the horizon for
[4059.18 --> 4060.04]  either yourself
[4060.04 --> 4062.58]  personally or the
[4062.58 --> 4064.14]  horizon for Vercel,
[4064.28 --> 4065.20]  what's on the horizon?
[4065.36 --> 4066.30]  What's just over the
[4066.30 --> 4066.62]  horizon?
[4066.74 --> 4067.62]  What can you share about
[4067.62 --> 4068.16]  where you're going?
[4068.16 --> 4069.64]  I talked a lot about
[4069.64 --> 4071.18]  how I think that
[4071.18 --> 4072.80]  we're still in the
[4072.80 --> 4073.90]  early innings of
[4073.90 --> 4074.70]  the technology,
[4074.70 --> 4076.30]  which makes me
[4076.30 --> 4076.98]  really excited
[4076.98 --> 4078.08]  because
[4078.08 --> 4080.86]  with the post-COVID
[4080.86 --> 4081.68]  world, something
[4081.68 --> 4082.76]  nice that has come
[4082.76 --> 4084.22]  is that
[4084.22 --> 4085.70]  there is a
[4085.70 --> 4087.12]  global workforce.
[4087.80 --> 4089.06]  We're all better
[4089.06 --> 4089.54]  connected.
[4089.90 --> 4091.22]  We can all create
[4091.22 --> 4091.90]  from everywhere.
[4092.32 --> 4093.70]  We talked about how
[4093.70 --> 4095.14]  a lot has been done
[4095.14 --> 4095.78]  with the web for
[4095.78 --> 4096.42]  consumption,
[4096.42 --> 4098.70]  but not as much
[4098.70 --> 4099.46]  has been done for
[4099.46 --> 4100.50]  authoring for the
[4100.50 --> 4100.72]  web.
[4101.66 --> 4102.88]  And the web
[4102.88 --> 4103.60]  browser as a
[4103.60 --> 4104.60]  technology is in this
[4104.60 --> 4106.08]  incredible position of
[4106.08 --> 4107.48]  being both a
[4107.48 --> 4108.58]  consumption and a
[4108.58 --> 4109.28]  creation tool.
[4109.76 --> 4111.40]  I want to see that
[4111.40 --> 4113.30]  promise through,
[4113.82 --> 4115.28]  which will take us
[4115.28 --> 4116.12]  quite a bit of time,
[4116.32 --> 4117.12]  honestly, right?
[4117.26 --> 4118.86]  So it's not going to
[4118.86 --> 4119.62]  happen overnight.
[4119.98 --> 4120.82]  It's going to feel
[4120.82 --> 4121.50]  overnight once we
[4121.50 --> 4122.20]  accomplish it, of
[4122.20 --> 4122.50]  course.
[4123.22 --> 4124.36]  Of course, yes.
[4124.54 --> 4125.74]  But I think it's
[4125.74 --> 4126.46]  still going to take
[4126.46 --> 4126.92]  quite a bit of
[4126.92 --> 4127.22]  time.
[4127.86 --> 4128.66]  I think there's a
[4128.66 --> 4130.46]  lot of technology
[4130.46 --> 4132.10]  that we've built
[4132.10 --> 4134.00]  over decades that
[4134.00 --> 4135.56]  will continue to
[4135.56 --> 4136.98]  exist, just like the
[4136.98 --> 4138.08]  radio exists today.
[4138.84 --> 4140.32]  And even develop
[4140.32 --> 4140.66]  itself.
[4140.86 --> 4142.16]  I'm sure radio
[4142.16 --> 4142.84]  today is even
[4142.84 --> 4143.06]  better.
[4143.30 --> 4144.44]  I love Sirius XM,
[4144.58 --> 4145.00]  actually.
[4145.30 --> 4146.12]  So radio is
[4146.12 --> 4146.42]  awesome.
[4146.88 --> 4147.74]  And radio has not
[4147.74 --> 4148.98]  ceased to exist.
[4149.64 --> 4151.32]  But new, more
[4151.32 --> 4153.26]  innovative media have
[4153.26 --> 4155.34]  come that have
[4155.34 --> 4157.24]  grown and really
[4157.24 --> 4158.38]  cast a shadow on
[4158.38 --> 4159.38]  those technologies.
[4159.82 --> 4160.38]  My podcasts.
[4161.54 --> 4162.06]  Yes.
[4162.94 --> 4164.94]  I think that
[4164.94 --> 4165.98]  that's going to
[4165.98 --> 4167.34]  happen with the
[4167.34 --> 4168.84]  cloud and that's
[4168.84 --> 4169.50]  going to happen
[4169.50 --> 4170.08]  with the web.
[4170.44 --> 4170.86]  Any particular
[4170.86 --> 4171.66]  examples that you
[4171.66 --> 4172.32]  can think of for
[4172.32 --> 4173.20]  the creation process?
[4173.36 --> 4174.00]  I'm curious, like,
[4174.66 --> 4175.40]  where you might
[4175.40 --> 4176.94]  hone in initially.
[4177.44 --> 4178.22]  So one example
[4178.22 --> 4179.44]  that I think is
[4179.44 --> 4180.60]  super interesting is
[4180.60 --> 4182.24]  that technology
[4182.24 --> 4182.94]  that has been
[4182.94 --> 4184.94]  approachable for
[4184.94 --> 4185.64]  authoring for the
[4185.64 --> 4186.86]  web has also been
[4186.86 --> 4187.86]  quickly discarded,
[4188.00 --> 4188.54]  as I mentioned.
[4188.72 --> 4188.78]  Right?
[4188.88 --> 4189.80]  Like, oh, there's
[4189.80 --> 4190.44]  this, like, I
[4190.44 --> 4191.30]  actually used to use
[4191.30 --> 4192.74]  Dreamweaver many,
[4192.82 --> 4193.50]  many, many years
[4193.50 --> 4193.98]  ago.
[4194.30 --> 4194.52]  Yeah.
[4195.22 --> 4196.24]  And I remember,
[4196.38 --> 4196.98]  again, like, you
[4196.98 --> 4198.10]  kind of outgrow it.
[4198.38 --> 4199.06]  I think we're going
[4199.06 --> 4200.00]  to create technologies
[4200.00 --> 4201.56]  very durable in that
[4201.56 --> 4201.84]  sense.
[4201.92 --> 4202.40]  I always actually
[4202.40 --> 4203.84]  point out that I
[4203.84 --> 4204.62]  would have investors
[4204.62 --> 4206.22]  years ago tell us,
[4206.62 --> 4207.64]  well, front-end is
[4207.64 --> 4208.92]  not interesting because
[4208.92 --> 4210.04]  front-end frameworks
[4210.04 --> 4210.96]  get changed every
[4210.96 --> 4211.74]  other day and
[4211.74 --> 4212.02]  whatnot.
[4213.04 --> 4214.10]  And now we
[4214.10 --> 4214.66]  actually look at
[4214.66 --> 4215.54]  reality and we
[4215.54 --> 4217.16]  see that actually,
[4217.30 --> 4218.66]  like, the choice of
[4218.66 --> 4219.58]  React, for example,
[4219.68 --> 4220.72]  for major
[4220.72 --> 4221.48]  organizations,
[4222.18 --> 4222.66]  corporations,
[4222.84 --> 4223.68]  storefronts, et
[4223.68 --> 4224.46]  cetera, in the U.S.
[4224.46 --> 4225.44]  has been super
[4225.44 --> 4227.12]  stable, super
[4227.12 --> 4227.42]  durable.
[4227.56 --> 4228.42]  Durable like Git
[4228.42 --> 4229.32]  has been durable,
[4229.46 --> 4229.78]  right?
[4230.44 --> 4231.06]  And I think that's
[4231.06 --> 4231.92]  going to happen in
[4231.92 --> 4232.60]  lots of different
[4232.60 --> 4232.88]  ways.
[4232.88 --> 4234.12]  I think you see it
[4234.12 --> 4235.66]  with Shopify now
[4235.66 --> 4237.26]  taking headless a lot
[4237.26 --> 4238.46]  more seriously and
[4238.46 --> 4239.22]  welcoming
[4239.22 --> 4240.70]  React developers
[4240.70 --> 4242.40]  worldwide to build
[4242.40 --> 4243.32]  on top of that.
[4243.78 --> 4244.58]  But I think the
[4244.58 --> 4245.02]  same is going to
[4245.02 --> 4245.82]  happen with folks
[4245.82 --> 4246.48]  that are on the
[4246.48 --> 4247.30]  authoring side, on
[4247.30 --> 4248.26]  the editing side,
[4248.78 --> 4249.30]  the folks that
[4249.30 --> 4250.70]  contribute through
[4250.70 --> 4251.32]  no-code and
[4251.32 --> 4251.94]  low-code.
[4252.42 --> 4253.02]  It's not that
[4253.02 --> 4253.34]  they're going to
[4253.34 --> 4255.50]  be any less of a
[4255.50 --> 4256.62]  contribution or
[4256.62 --> 4257.90]  that their work is
[4257.90 --> 4259.00]  not going to be as
[4259.00 --> 4260.10]  important or that
[4260.10 --> 4260.52]  it's going to get
[4260.52 --> 4261.28]  rewritten by a
[4261.28 --> 4262.44]  developer a year
[4262.44 --> 4263.04]  later.
[4263.78 --> 4264.60]  Perhaps even the
[4264.60 --> 4265.62]  opposite, right?
[4266.24 --> 4266.84]  Developers will
[4266.84 --> 4267.26]  start saying,
[4267.38 --> 4267.96]  well, for this
[4267.96 --> 4268.94]  simple page that I
[4268.94 --> 4269.56]  need to build, I'm
[4269.56 --> 4269.98]  going to build it
[4269.98 --> 4270.78]  entirely visually.
[4271.42 --> 4271.98]  Or I'm going to
[4271.98 --> 4272.60]  build it entirely in
[4272.60 --> 4273.10]  the web browser.
[4273.20 --> 4274.22]  I'm not going to
[4274.22 --> 4275.94]  use the power tool
[4275.94 --> 4277.24]  for this anymore.
[4277.72 --> 4278.76]  And yet, that's
[4278.76 --> 4279.18]  going to be the
[4279.18 --> 4279.94]  right decision
[4279.94 --> 4281.52]  that's likely to
[4281.52 --> 4282.84]  stay for years and
[4282.84 --> 4283.46]  years and years to
[4283.46 --> 4283.70]  come.
[4284.26 --> 4284.98]  At the same time,
[4285.02 --> 4286.92]  I think AI will
[4286.92 --> 4287.70]  play a very
[4287.70 --> 4288.72]  important role here.
[4289.50 --> 4290.64]  I'm a big fan of
[4290.64 --> 4291.74]  the work that GitHub
[4291.74 --> 4292.44]  put out with
[4292.44 --> 4293.60]  better autocompletion.
[4294.16 --> 4295.20]  I've always been a
[4295.20 --> 4295.76]  fan of this.
[4295.76 --> 4297.14]  I created a demo
[4297.14 --> 4297.90]  called Thought
[4297.90 --> 4299.30]  Complete back in
[4299.30 --> 4301.10]  the day where you
[4301.10 --> 4301.98]  would type and you
[4301.98 --> 4302.56]  would autocomplete
[4302.56 --> 4303.32]  from tweets that
[4303.32 --> 4304.40]  other people wrote
[4304.40 --> 4305.86]  to just like augment
[4305.86 --> 4306.54]  your cognition.
[4306.74 --> 4307.22]  I think there's going
[4307.22 --> 4307.90]  to be a lot of that
[4307.90 --> 4309.98]  going on where we
[4309.98 --> 4311.02]  augment the
[4311.02 --> 4311.96]  developer cognition,
[4312.18 --> 4313.00]  we augment the
[4313.00 --> 4313.96]  non-developer
[4313.96 --> 4315.72]  cognition, we
[4315.72 --> 4316.48]  augment the
[4316.48 --> 4317.70]  marketer cognition
[4317.70 --> 4319.00]  in that marketers
[4319.00 --> 4320.62]  can try more
[4320.62 --> 4321.30]  things, more
[4321.30 --> 4323.46]  permutations of
[4323.46 --> 4324.34]  copy and
[4324.34 --> 4326.14]  ideas assisted
[4326.14 --> 4327.02]  by AI.
[4327.68 --> 4328.36]  You can almost
[4328.36 --> 4329.06]  think of this as
[4329.06 --> 4329.94]  a website building
[4329.94 --> 4330.90]  itself, right?
[4331.52 --> 4332.46]  And we're not
[4332.46 --> 4333.24]  really far away
[4333.24 --> 4333.64]  from that.
[4333.82 --> 4334.46]  We're talking,
[4334.62 --> 4336.22]  you know, maybe
[4336.22 --> 4338.46]  months, if not
[4338.46 --> 4339.54]  single digit years.
[4339.76 --> 4340.24]  Obviously, I'm too
[4340.24 --> 4341.10]  optimistic sometimes,
[4341.10 --> 4343.00]  but the websites
[4343.00 --> 4343.68]  that build themselves
[4343.68 --> 4344.46]  are certainly
[4344.46 --> 4344.84]  coming.
[4345.50 --> 4346.22]  Oh, yes.
[4346.36 --> 4347.10]  GitHub Copilot
[4347.10 --> 4347.82]  and the opportunities
[4347.82 --> 4348.16]  there.
[4348.28 --> 4349.06]  It's a new world.
[4349.36 --> 4350.38]  It's somewhat
[4350.38 --> 4352.58]  scary, but also
[4352.58 --> 4354.44]  welcoming to some
[4354.44 --> 4354.78]  degree.
[4355.02 --> 4355.44]  Liberating.
[4355.78 --> 4355.92]  Yeah.
[4356.30 --> 4357.02]  Everything that's
[4357.02 --> 4358.04]  scary in a lot of
[4358.04 --> 4358.74]  cases ends up being
[4358.74 --> 4359.32]  liberating.
[4359.92 --> 4360.54]  I actually was
[4360.54 --> 4361.74]  listening to this
[4361.74 --> 4362.80]  great podcast of
[4362.80 --> 4364.64]  Gary Kasparov and
[4364.64 --> 4366.34]  Lex Friedman, and
[4366.34 --> 4368.54]  he lived a very
[4368.54 --> 4369.18]  interesting
[4369.18 --> 4370.98]  first-hand
[4370.98 --> 4371.76]  experience of what
[4371.76 --> 4372.84]  it's like for AI
[4372.84 --> 4375.32]  to defeat what
[4375.32 --> 4376.66]  seemingly you had
[4376.66 --> 4377.44]  that was, first of
[4377.44 --> 4378.16]  all, unique in the
[4378.16 --> 4378.80]  entire world.
[4378.80 --> 4380.24]  because if you're
[4380.24 --> 4381.74]  raiding as a chess
[4381.74 --> 4383.44]  player, but also
[4383.44 --> 4384.74]  you had what was
[4384.74 --> 4385.82]  seemingly considered
[4385.82 --> 4386.96]  for a computer to
[4386.96 --> 4388.16]  not ever be able to
[4388.16 --> 4388.36]  do.
[4388.92 --> 4389.96]  What he said in the
[4389.96 --> 4390.44]  podcast that I
[4390.44 --> 4390.96]  thought was really
[4390.96 --> 4391.82]  interesting is that,
[4392.18 --> 4393.34]  well, that's awesome
[4393.34 --> 4394.30]  that they beat us.
[4394.98 --> 4396.12]  Okay, the computer is
[4396.12 --> 4397.24]  getting another nine
[4397.24 --> 4399.38]  in their SLA of
[4399.38 --> 4400.02]  things that they can
[4400.02 --> 4401.52]  do that are better
[4401.52 --> 4402.02]  than humans,
[4402.10 --> 4402.22]  right?
[4402.28 --> 4403.36]  So now, let's say
[4403.36 --> 4404.86]  they're at 99.9.
[4404.86 --> 4405.14]  Yeah.
[4405.46 --> 4406.82]  And 10 years pass and
[4406.82 --> 4408.78]  they get to 99.9.
[4408.80 --> 4410.76]  Here's the deal.
[4411.20 --> 4413.90]  The remaining 0.001,
[4413.96 --> 4415.46]  which is human
[4415.46 --> 4416.92]  capability, now it
[4416.92 --> 4417.66]  just matters more.
[4418.20 --> 4419.60]  It's not that because
[4419.60 --> 4420.96]  there's fewer things in
[4420.96 --> 4422.32]  which you truly excel
[4422.32 --> 4423.76]  that your impact is
[4423.76 --> 4424.14]  diminished.
[4424.26 --> 4425.72]  If anything, it's the
[4425.72 --> 4426.04]  opposite.
[4426.30 --> 4426.52]  Right.
[4426.62 --> 4427.58]  Because now you're
[4427.58 --> 4428.94]  truly able to focus on
[4428.94 --> 4429.46]  your creativity.
[4429.62 --> 4430.28]  I think ultimately
[4430.28 --> 4430.72]  that's what we're
[4430.72 --> 4432.20]  seeing with front-end,
[4432.30 --> 4432.42]  right?
[4432.48 --> 4433.72]  Like, okay, now you
[4433.72 --> 4434.24]  don't have to worry
[4434.24 --> 4435.54]  about the cloud at
[4435.54 --> 4435.76]  all.
[4435.76 --> 4436.80]  You might not even
[4436.80 --> 4438.22]  ever know what a
[4438.22 --> 4439.60]  server used to be or
[4439.60 --> 4440.12]  look like.
[4440.80 --> 4441.64]  You might not even
[4441.64 --> 4443.00]  understand what the
[4443.00 --> 4444.70]  infrastructure is made
[4444.70 --> 4445.20]  up of.
[4445.34 --> 4446.02]  Like, the other day, I
[4446.02 --> 4446.86]  don't even know this
[4446.86 --> 4447.88]  anymore, like, nor
[4447.88 --> 4449.14]  maybe ever, but, like,
[4449.16 --> 4449.98]  I'll give you a really
[4449.98 --> 4450.72]  good example, right?
[4450.78 --> 4453.66]  Like, S3, the CTO of
[4453.66 --> 4455.60]  Amazon said, is composed
[4455.60 --> 4457.66]  of 250 microservices.
[4458.52 --> 4459.66]  And it's like, that's
[4459.66 --> 4460.14]  insane.
[4460.14 --> 4463.58]  There's 250 independent
[4463.58 --> 4465.94]  services that are making
[4465.94 --> 4467.72]  up this greater service
[4467.72 --> 4469.64]  that I interface through
[4469.64 --> 4472.06]  two API calls, get and
[4472.06 --> 4473.74]  post, patch maybe
[4473.74 --> 4474.26]  sometimes.
[4474.88 --> 4476.44]  And it's just astounding.
[4476.86 --> 4478.52]  And I think that's just
[4478.52 --> 4479.54]  ultimately going to happen
[4479.54 --> 4480.98]  with, you know, again,
[4481.06 --> 4482.38]  like, we're continuing
[4482.38 --> 4483.56]  to, like, okay, now
[4483.56 --> 4484.74]  Vercel is helping at the
[4484.74 --> 4485.28]  other nine.
[4485.70 --> 4486.78]  Not only will you not
[4486.78 --> 4488.74]  know what file storage,
[4488.74 --> 4490.38]  how it actually works.
[4490.50 --> 4491.80]  Now you're not going to
[4491.80 --> 4493.44]  know how a page is built
[4493.44 --> 4495.60]  and rendered in the
[4495.60 --> 4495.92]  cloud.
[4496.32 --> 4497.40]  But that's awesome,
[4497.40 --> 4498.16]  because now you're
[4498.16 --> 4501.52]  remaining 0.001% is how
[4501.52 --> 4502.54]  you express your brand
[4502.54 --> 4504.20]  online, how you engage
[4504.20 --> 4505.60]  with your customers, how
[4505.60 --> 4506.50]  you choose to communicate
[4506.50 --> 4507.90]  with them, what your
[4507.90 --> 4510.22]  values are as a person
[4510.22 --> 4512.26]  doing business, how you
[4512.26 --> 4514.84]  express your identity,
[4514.84 --> 4516.40]  and all these amazing
[4516.40 --> 4516.72]  things.
[4516.72 --> 4517.40]  And, like, ultimately
[4517.40 --> 4518.36]  your own product that
[4518.36 --> 4518.78]  you're building.
[4518.98 --> 4519.60]  Whether it's hardware,
[4519.74 --> 4520.34]  whether it's software,
[4521.10 --> 4521.82]  how you give that
[4521.82 --> 4523.40]  service, in what
[4523.40 --> 4524.28]  languages, in what
[4524.28 --> 4525.74]  markets, etc.
[4526.52 --> 4528.00]  So, I think it's
[4528.00 --> 4528.28]  awesome.
[4528.44 --> 4529.50]  And I think we're just
[4529.50 --> 4530.60]  going to continue in
[4530.60 --> 4532.04]  that trajectory of
[4532.04 --> 4533.30]  more and more
[4533.30 --> 4535.04]  undifferentiated work
[4535.04 --> 4536.86]  being automated, and
[4536.86 --> 4537.58]  more power to you.
[4538.04 --> 4538.14]  Yeah.
[4538.50 --> 4540.22]  It sounds like a
[4540.22 --> 4540.80]  throwback to what you
[4540.80 --> 4542.02]  said earlier with
[4542.02 --> 4542.74]  meta, meta
[4542.74 --> 4543.18]  programming.
[4543.48 --> 4544.68]  It's like automating
[4544.68 --> 4545.12]  the meta.
[4546.04 --> 4547.06]  You know, like, to be a
[4547.06 --> 4547.82]  developer today to
[4547.82 --> 4549.70]  deliver an application
[4549.70 --> 4551.18]  to the web, I don't
[4551.18 --> 4552.52]  necessarily need to know
[4552.52 --> 4553.18]  about servers.
[4553.80 --> 4553.88]  Right?
[4553.88 --> 4554.48]  That's kind of meta.
[4555.12 --> 4555.98]  In some scenarios, it
[4555.98 --> 4557.60]  might make more sense for
[4557.60 --> 4558.68]  you to have greater
[4558.68 --> 4559.60]  granular control.
[4560.10 --> 4561.64]  But to deliver an e-commerce
[4561.64 --> 4563.24]  store, I don't really
[4563.24 --> 4564.04]  need to have that.
[4564.10 --> 4565.44]  I want to pull that into
[4565.44 --> 4566.70]  Shopify and use
[4566.70 --> 4567.44]  headless or something
[4567.44 --> 4567.94]  like that.
[4568.18 --> 4569.18]  Or just go straight up
[4569.18 --> 4569.62]  Shopify.
[4570.34 --> 4571.50]  It seems like automating
[4571.50 --> 4573.12]  the meta.
[4573.12 --> 4573.92]  For sure.
[4574.28 --> 4575.54]  Is there anything that
[4575.54 --> 4576.54]  I haven't asked you,
[4576.66 --> 4576.80]  Guillermo?
[4576.88 --> 4578.44]  I know we've always
[4578.44 --> 4579.24]  appreciated you coming
[4579.24 --> 4580.40]  on the ChangeLog and
[4580.40 --> 4581.26]  then recently JS
[4581.26 --> 4581.58]  Party.
[4581.72 --> 4582.38]  As a matter of fact,
[4582.70 --> 4583.66]  another thanks to you,
[4584.06 --> 4585.00]  we opened up this
[4585.00 --> 4587.44]  year's episode list on
[4587.44 --> 4588.24]  the ChangeLog with
[4588.24 --> 4588.50]  you.
[4589.08 --> 4590.76]  And that was a fun
[4590.76 --> 4591.68]  show, talking about
[4591.68 --> 4592.50]  the future of the web
[4592.50 --> 4593.90]  and essentially where
[4593.90 --> 4594.58]  we're going with the
[4594.58 --> 4594.84]  web.
[4595.00 --> 4595.74]  That was a lot of fun.
[4595.88 --> 4597.44]  So I appreciate you
[4597.44 --> 4598.52]  being a staple around
[4598.52 --> 4598.70]  here.
[4598.84 --> 4600.06]  But is there anything
[4600.06 --> 4601.58]  left unsaid in this
[4601.58 --> 4602.30]  show with me today?
[4602.30 --> 4603.40]  I think we've
[4603.40 --> 4604.00]  covered plenty.
[4604.22 --> 4605.60]  It was a great new
[4605.60 --> 4605.98]  take.
[4606.28 --> 4606.98]  There's a whole new
[4606.98 --> 4608.24]  side that we talked
[4608.24 --> 4608.76]  about today.
[4609.16 --> 4609.94]  The only piece we
[4609.94 --> 4611.12]  didn't cover, and I'm
[4611.12 --> 4611.84]  not asking to go into
[4611.84 --> 4613.06]  this, but it's still
[4613.06 --> 4614.56]  unclear to me if Zite is
[4614.56 --> 4615.50]  a bootstrap company or
[4615.50 --> 4616.40]  not, or what the early
[4616.40 --> 4617.34]  stages were, because it
[4617.34 --> 4619.00]  took you several years
[4619.00 --> 4619.54]  to raise.
[4619.68 --> 4620.56]  And when you raised,
[4620.60 --> 4621.24]  you changed your name.
[4621.80 --> 4622.28]  I think you may have
[4622.28 --> 4623.00]  had some seed funding,
[4623.12 --> 4624.54]  but your first Series A,
[4625.06 --> 4625.80]  five years in,
[4625.90 --> 4626.18]  essentially.
[4626.72 --> 4628.06]  Yeah, we spent a lot
[4628.06 --> 4628.62]  of time.
[4629.20 --> 4630.32]  We did raise some seed
[4630.32 --> 4632.04]  money, but we spent a
[4632.04 --> 4634.76]  lot of time on R&D,
[4634.84 --> 4635.70]  basically, right?
[4635.82 --> 4637.90]  So I guess, looking
[4637.90 --> 4639.12]  back, I think we had a
[4639.12 --> 4640.92]  very high bar for we're
[4640.92 --> 4642.46]  going to go out and
[4642.46 --> 4643.66]  raise a Series A and
[4643.66 --> 4644.68]  truly build this out.
[4645.14 --> 4646.64]  But we had a really high
[4646.64 --> 4648.72]  bar for ourselves for,
[4649.34 --> 4650.82]  again, like this is a
[4650.82 --> 4651.94]  lifetime commitment,
[4652.20 --> 4652.46]  right?
[4652.46 --> 4655.04]  it's a very long journey.
[4655.04 --> 4658.48]  And I needed the confidence
[4658.48 --> 4660.74]  that there was something
[4660.74 --> 4663.64]  that was ambitious, but it
[4663.64 --> 4664.90]  was also working and
[4664.90 --> 4666.14]  resonating with customers.
[4667.18 --> 4670.04]  So we took our time, and I'm
[4670.04 --> 4671.02]  really happy that we did.
[4671.48 --> 4673.36]  And we learned a tremendous
[4673.36 --> 4674.96]  amount through experimentation
[4674.96 --> 4678.86]  and prototyping and lots of
[4678.86 --> 4679.56]  different ideas.
[4679.56 --> 4681.78]  And then by the time we
[4681.78 --> 4684.24]  announced our new name and
[4684.24 --> 4686.46]  Vercel and a lot of the
[4686.46 --> 4688.06]  traction that we had built
[4688.06 --> 4690.68]  up as well, it felt like the
[4690.68 --> 4691.12]  right time.
[4692.44 --> 4693.16]  I agree.
[4693.36 --> 4694.02]  I've been enjoying your
[4694.02 --> 4694.58]  watching journey.
[4695.02 --> 4695.76]  It's been fun.
[4696.56 --> 4697.48]  The work you and the rest of
[4697.48 --> 4698.82]  your team have done make me
[4698.82 --> 4700.06]  more excited about the web.
[4700.60 --> 4702.62]  And I appreciate the work
[4702.62 --> 4703.04]  you've done.
[4703.12 --> 4704.34]  And thank you for sharing your
[4704.34 --> 4705.20]  time here today and your
[4705.20 --> 4706.86]  story today and your
[4706.86 --> 4707.42]  frameworks.
[4708.02 --> 4708.64]  Appreciate you.
[4708.64 --> 4709.18]  Thank you.
[4709.46 --> 4709.80]  Thank you.
[4712.60 --> 4713.80]  That's it for this episode of
[4713.80 --> 4714.26]  Founders Talk.
[4714.34 --> 4715.26]  Thanks for tuning in.
[4715.66 --> 4718.28]  Up next is Zach Smith, founder
[4718.28 --> 4719.52]  of Packet, which was
[4719.52 --> 4721.46]  acquired by Equinix and now
[4721.46 --> 4723.86]  operates as Equinix Metal to
[4723.86 --> 4725.50]  offer global interconnected
[4725.50 --> 4726.78]  bare metal at scale.
[4727.26 --> 4728.50]  Zach shared so much advice in
[4728.50 --> 4728.94]  this show.
[4729.24 --> 4729.86]  You're not going to want to
[4729.86 --> 4730.28]  miss it.
[4730.50 --> 4732.00]  On that note, if you haven't
[4732.00 --> 4733.06]  subscribed yet, what are you
[4733.06 --> 4733.72]  waiting for?
[4734.12 --> 4736.24]  Head to FoundersTalk.fm, where
[4736.24 --> 4737.78]  the galaxy brand move is to
[4737.78 --> 4739.66]  get all our shows in one
[4739.66 --> 4741.40]  single feed at
[4741.40 --> 4742.80]  changelog.com slash master.
[4743.12 --> 4744.78]  You can also get closer to
[4744.78 --> 4745.94]  the metal and make the ads
[4745.94 --> 4747.88]  disappear on all our shows
[4747.88 --> 4750.28]  at changelog.com slash plus
[4750.28 --> 4750.68]  plus.
[4751.12 --> 4752.28]  Thank you to our partners,
[4752.40 --> 4753.56]  Linode, Fastly and Launched
[4753.56 --> 4753.98]  Darkly.
[4754.16 --> 4755.28]  Also, thanks to Breakmaster
[4755.28 --> 4755.70]  Cylinder.
[4756.12 --> 4757.26]  And thank you to you for
[4757.26 --> 4758.02]  listening to the show.
[4758.40 --> 4759.26]  If you enjoyed it, do me a
[4759.26 --> 4759.54]  favor.
[4760.00 --> 4760.84]  Share it with a friend.
[4761.28 --> 4762.50]  Word of mouth is by far the
[4762.50 --> 4764.08]  best way to help us grow our
[4764.08 --> 4764.62]  shows.
[4764.62 --> 4766.10]  That's it for this show.
[4766.24 --> 4766.84]  We'll see you in the next
[4766.84 --> 4767.04]  one.
[4767.04 --> 4768.04]  Bye.
[4768.04 --> 4768.54]  Bye.
[4768.54 --> 4769.04]  Bye.
[4769.04 --> 4769.10]  Bye.
[4769.10 --> 4769.12]  Bye.
[4769.12 --> 4769.54]  Bye.
[4769.54 --> 4769.60]  Bye.
[4769.60 --> 4769.64]  Bye.
[4769.64 --> 4769.98]  Bye.
[4769.98 --> 4770.04]  Bye.
[4770.04 --> 4770.10]  Bye.
[4770.10 --> 4770.12]  Bye.
[4770.12 --> 4770.62]  Bye.
[4770.62 --> 4770.64]  Bye.
[4770.64 --> 4771.04]  Bye.
[4771.04 --> 4771.06]  Bye.
[4794.62 --> 4796.52]  Bye.
[4796.54 --> 4798.18]  Bye.
[4800.66 --> 4801.30]  Bye.
[4801.32 --> 4801.58]  Bye.
[4801.60 --> 4802.18]  러Ilele
[4802.18 --> 4802.34]  Bye.
[4802.36 --> 4802.52]  Bye.
[4802.56 --> 4802.70]  Bye.
[4802.72 --> 4802.94]  Bye.
[4803.10 --> 4803.52]  Bye.
[4803.58 --> 4803.62]  Bye.
[4803.64 --> 4803.76]  Bye.
[4804.00 --> 4804.06]  Bye.
[4804.10 --> 4804.54]  Bye.
[4804.56 --> 4805.30]  Bye.
[4805.46 --> 4805.84]  Bye.
[4805.92 --> 4806.02]  Bye.
[4806.02 --> 4806.32]  Bye.
[4806.78 --> 4807.32]  Bye.
[4807.32 --> 4807.82]  Bye.
[4807.82 --> 4807.98]  Bye.
[4809.96 --> 4810.92]  Bye.
[4811.12 --> 4811.98]  Bye.
[4812.00 --> 4812.12]  Bye.
[4812.12 --> 4812.30]  Bye.
[4812.40 --> 4812.42]  Bye.
[4813.08 --> 4813.76]  Bye.
[4813.76 --> 4814.30]  Bye.
[4814.34 --> 4814.70]  Bye.
[4814.70 --> 4815.98]  Bye.
[4818.76 --> 4819.60]  Bye.
[4819.80 --> 4820.26]  Bye.
[4820.26 --> 4820.36]  Bye.
[4820.38 --> 4820.84]  Bye.
[4821.02 --> 4821.86]  Bye.
[4821.86 --> 4822.68]  Bye.
[4822.72 --> 4823.04]  Bye.
[4823.30 --> 4824.46]  Bye.
