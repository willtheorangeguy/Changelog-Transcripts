[0.08 --> 5.72]  Hey, how's it going? I'm your host, Gerhard Lzu, and you're listening to Ship It, a podcast
[5.72 --> 11.64]  about getting your best ideas into the world and seeing what happens. We talk about code,
[11.96 --> 18.00]  ops, infrastructure, and the people that make it happen. Yes, we focus on the people because
[18.00 --> 24.12]  everything else is an implementation detail. Getting a Kubernetes cluster is easy. It can
[24.12 --> 30.82]  take as little as 15 seconds with K3S. But the rest of the first steps are not as straightforward.
[31.30 --> 37.72]  And do you even need Kubernetes? The fact that everyone is talking about it, and even those
[37.72 --> 43.66]  that don't need it, use it, doesn't mean that you should. Coming from an Elixir background,
[44.00 --> 50.40]  with many years of helping companies build and run highly concurrent and fault-tolerant applications,
[50.40 --> 57.62]  Lars developed a most pragmatic approach to shipping software. Erlang has some great primitives
[57.62 --> 64.02]  built-in, including self-contained releases and hot code reloading. And sometimes a monolith running
[64.02 --> 69.92]  on a single host with continuous backups and a built-in self-restore capability is everything
[69.92 --> 76.54]  that a small team of developers needs. That's right, KISS. As in, keep it simple, Sprout.
[76.54 --> 82.88]  Check Lars's blog to understand what I really mean. But after two years of running changelog.com,
[83.06 --> 87.60]  a Phoenix monolith on Kubernetes, what do I think? Let's find out.
[88.02 --> 93.76]  Big thanks to our partners Fastly, LaunchDarkly, and Linode. Our bandwidth is provided by Fastly,
[94.10 --> 100.22]  learn more at fastly.com, feature flags powered by LaunchDarkly.com, and we love Linode.
[100.22 --> 105.20]  They keep it fast and simple. Check them out at linode.com forward slash changelog.
[106.54 --> 115.36]  This episode of Ship It is brought to you by Render, the zero DevOps cloud that empowers you
[115.36 --> 120.50]  to ship faster than your competitors. Here's Anurag Goel, CEO of Render, sharing why developers
[120.50 --> 123.70]  choose Render over Heroku and how they're innovating much faster.
[124.06 --> 129.24]  A lot of Render customers come to us from Heroku and they tell us Render is what Heroku
[129.24 --> 134.74]  could have been. I think it's because we offer a more streamlined approach to hosting modern cloud
[134.74 --> 141.36]  applications at a significantly better price point. Applications on Render heal themselves and
[141.36 --> 146.94]  scale automatically, giving developers the features and flexibility of something like Kubernetes,
[147.38 --> 153.02]  but without any of the complexity. We're always working to bring the latest industry advances
[153.02 --> 158.44]  to our platform so your applications can leverage the state of the art in the cloud without you having
[158.44 --> 164.08]  to do or learn anything. All right, learn more about how Render compares to Heroku at render.com
[164.08 --> 170.22]  slash compare or email changelog at render.com for a personal intro and to ask questions about
[170.22 --> 175.84]  the Render platform. Again, that's render.com slash compare or email changelog at render.com.
[175.84 --> 181.42]  We are going to send three, two, one.
[195.10 --> 200.48]  I'd like to start with a story. I know that you've been helping changelog.com, the code base,
[200.48 --> 206.86]  in different ways. The thing which I remember is that our response latency went down.
[207.80 --> 212.10]  You did some tweaks. Is that right? Or am I confusing you with Alex?
[212.62 --> 214.96]  I think Alex gets the credit on that.
[215.16 --> 219.30]  Alex gets the credit. I definitely know he improved the N plus one queries, that's for sure.
[219.72 --> 221.94]  Yeah, I even cost some of those.
[222.34 --> 225.28]  Oh, right. Okay. Okay. So you're the opposite of Alex. Okay.
[225.28 --> 232.26]  Yes, exactly. I'm here to create opportunities for performance improvements.
[232.74 --> 237.02]  I see. So that's the way it goes. Okay. So you're making it worse and he's making it better.
[237.36 --> 243.74]  And the difference is like it's zero, right? Okay. So we're not going anywhere.
[244.08 --> 248.26]  It's very important to have a stable code base and a very stable operation.
[248.26 --> 255.80]  It is. Right. So some of the work I've done with the changelog has been on a few things that haven't
[255.80 --> 263.28]  been released and a few things that basically housekeeping around how emails are sent out and
[263.28 --> 271.20]  to whom. I think and I hope that there will be some more stuff done with the meta costs feature I
[271.20 --> 277.70]  made. I had the opportunity to write a small DSL, which would be nice to expose to the public. I don't
[277.70 --> 282.08]  think Jared has put it into action. So that's a good time to shame him a little bit about it.
[282.44 --> 287.10]  Okay. So Jared, if you're not listening, it's okay. And if you are listening, what's up with the
[287.10 --> 292.62]  meta costs? I don't know anything about it, but yeah, what's up with it? That's what I'm wondering.
[292.62 --> 300.60]  Yeah. So, but it was, it was very fun to get a chance to work with Jared and the changelog code base
[300.60 --> 306.96]  in a slightly dedicated fashion. So it was a few months that would have been last summer that I,
[306.96 --> 311.68]  that I spent some time with this code base. Then I introduced Alex when I didn't have time
[311.68 --> 317.96]  anymore. And he seems to have torn things up. He really, really has pushed a few things forward.
[318.34 --> 323.44]  So he did. Yes, definitely. The, the, the Promex stuff, I think is the one that I got most excited
[323.44 --> 327.62]  about because it touches on the infrastructure side of things. It just integrates a couple of
[327.62 --> 331.72]  things together. So that is from my perspective, very visible and something which I'm very interested
[331.72 --> 338.28]  in to see how are things behaving. The N plus one optimizations improvements, N plus one query
[338.28 --> 342.44]  improvements. That was great to see as well. I didn't know that you're the, you were the cause
[342.44 --> 352.58]  for it. So I'm not sure how I feel about that. I think I only introduced one fairly chunky case of
[352.58 --> 357.66]  them. And it was mostly, mostly when you're doing development that it turned things a little bit
[357.66 --> 362.90]  slow to start because I was doing something, something optimistic and that didn't turn out.
[363.52 --> 369.22]  I mean, the, the key takeaway from this little conversation is that you are deep into Elixir,
[369.38 --> 375.88]  into Erlang, into, is it, is Erlang fair to say? I mean, you're on Beam Radio, a co-host of Beam Radio.
[376.14 --> 377.80]  So Beam is all Erlang.
[378.26 --> 383.72]  I'm very excited and enthusiastic about Erlang, but I don't write Erlang. I write Elixir.
[383.72 --> 390.84]  It runs on the same VM as Erlang. So all the Erlang technology benefits Elixir. A lot of the
[390.84 --> 397.14]  Elixir technology benefits Erlang, but it can't fully go in both directions, unfortunately.
[397.88 --> 403.20]  Mostly a technical reason for it. Yeah. But, but that's, I am very invested in,
[403.32 --> 407.28]  in the Beam ecosystem. So the Beam is the name of the virtual machine.
[407.60 --> 408.74]  Do you know what Beam stands for?
[408.74 --> 417.38]  So I think early on it was Bogdan's something, something machine. I don't remember exactly.
[417.58 --> 421.76]  Erlang, abstract machine. Bogdan's Erlang, abstract machine.
[421.82 --> 426.94]  Because initially it was Jam, which was Joe's abstract machine, I imagine.
[427.12 --> 432.12]  Yes. Joe, you're still in our minds. I know that you're not listening, but those that know,
[432.46 --> 437.98]  Joe Armstrong, the co-creator of Erlang, you're still in our minds. Thank you for everything you've done.
[437.98 --> 440.38]  And you shipped a great thing into the world.
[440.84 --> 447.20]  Yeah. The Beam and Erlang are absolutely wild. And it's, it's been interesting that through many
[447.20 --> 452.88]  years I've heard of Erlang and people have been like, oh, it's a weird, that's a weird one,
[453.44 --> 457.98]  but it has some really strong ideas and it has some really strong features. And it's like, okay,
[457.98 --> 463.58]  whatever. I don't really do FP though. It wasn't really in my wheelhouse. And I figured it was
[463.58 --> 473.06]  probably too complicated for me. Now I'm very, very keen to avoid working with non-Beam languages if I
[473.06 --> 481.46]  can, because there are, there's just so much you get with, with a Beam that you just don't have in
[481.46 --> 485.12]  other runtimes or that you have to work so very, very hard for in other runtimes.
[485.12 --> 487.96]  Which are your top three favorite Beam features?
[488.46 --> 495.38]  Concurrency and parallelism at the same time for essentially no extra effort. It makes you do
[495.38 --> 502.28]  concurrency and parallelism correctly and reasonably without tripping you into sort of mutable state
[502.28 --> 507.94]  and the dangers of concurrency and parallelism. So that's one. Then there's the whole resiliency
[507.94 --> 516.32]  thing, which is built on sort of the same idea or some of the same ideas where there will be things
[516.32 --> 523.02]  that happen to your application that are unexpected that you can't really catch with just catching an
[523.02 --> 527.22]  exception. Maybe the disc was full. Maybe the service you were talking to was down. There's always
[527.22 --> 532.22]  something to make it blow up. And it has been described as the let it crash philosophy, but it's
[532.22 --> 539.42]  not always the most, it's not the best marketing. It makes managers very, very nervous. But the idea
[539.42 --> 545.86]  that it's okay if certain components fail, the important thing is to have a recovery strategy.
[546.28 --> 553.12]  And this actually sort of feeds into, to the Kubernetes thing, which, which has a similar
[553.12 --> 559.90]  approach, but in a, on a different scale. And this, this sets me apart from a lot of functional
[559.90 --> 566.38]  programmers, some functional programming enthusiasts really, really like their types. I'm very,
[566.38 --> 574.04]  very glad that Erlang and Elixir are dynamic. Okay. Apparently there is a typed Erlang syntax,
[574.16 --> 579.58]  DSL coming from Facebook. I say Facebook, but it's really WhatsApp. I keep forgetting its name,
[580.24 --> 584.26]  but something Muscala. Do you know who I'm referring to?
[584.26 --> 590.82]  Yeah. Mikhail Muscala is the guy that, as far as I know, sort of started the effort or
[590.82 --> 596.20]  that's probably leading the effort. I spoke to him once in Prague. That was before he was at WhatsApp,
[596.44 --> 603.52]  but that's a super interesting effort. And I think that type system makes perfect sense for what they
[603.52 --> 611.72]  need. They're a very large organization, but I don't really find it compelling for building the kind of
[611.72 --> 619.10]  web apps and the systems that I do. I find type systems to be a little bit annoying. I've done
[619.10 --> 624.10]  some work recently with Elm, which has a lot of types. That was frustrating at first, but it was
[624.10 --> 631.36]  also compelling. It showed me some of what, what you really get with a, with a types first approach,
[631.36 --> 640.16]  I guess. So interesting, but I'm not sure I love it. So I'm very, very happy with, with having a
[640.16 --> 647.74]  dynamic language. I come from Python and PHP originally. So that's, yeah, the Ruby lineage
[647.74 --> 653.64]  of Elixir works fine with what I'm sort of used to. It was an easy, a fairly easy transition,
[654.04 --> 659.84]  all things considered. That is a really good top three. So we have a good idea of, well,
[660.14 --> 666.14]  why you like Erlang and which are the top three features of the Beam, specifically I say Erlang.
[666.14 --> 669.80]  When I'm saying Erlang, I'm referring to the ecosystem more, the virtual machine,
[670.22 --> 676.56]  less the programming language. So that makes a lot of sense. I'm wondering when you're done
[676.56 --> 681.64]  coding your Elixir app, how do you ship it? How'd you get it out there?
[681.96 --> 685.72]  So that very much depends on, on context. So I'm...
[685.72 --> 689.88]  Let's take the last one, last Elixir app that you had to, and whether it's a service,
[690.00 --> 694.06]  I mean, you can, you can tell me about it. How did you get it into, how did you ship it?
[694.06 --> 699.64]  So right now I've been spending part of my day setting up a Docker file.
[700.40 --> 706.32]  So that, that'll tell you something. So Elixir and Erlang has this idea of releases
[706.32 --> 711.46]  where you bundle everything, including the runtime into a nice little package
[711.46 --> 715.90]  that you can just shove into a server and start without needing any dependencies,
[716.14 --> 718.40]  essentially, or very few dependencies, at least.
[718.90 --> 720.42]  OpenSSL is always the trickiest.
[720.42 --> 725.74]  Yeah. OpenSSL and usually encurses, limit curses.
[725.94 --> 729.88]  If you, if you need that, but yes, I know OpenSSL, you will definitely need that because
[729.88 --> 733.14]  you will be doing some sort of encryption somehow, it doesn't matter how.
[734.68 --> 736.62]  But there's always encryption in there somewhere.
[736.98 --> 737.32]  Exactly.
[737.74 --> 742.36]  So I think releases are sort of my ideal for keeping it very lean and just shipping it to
[742.36 --> 746.02]  a server. But in this case, we're going to be doing on-prem deployments.
[746.02 --> 753.74]  So someone else is going to set it up on their own hardware. And my plan is for them to be given
[753.74 --> 761.24]  a Docker compose file, some credentials and just go Docker compose up. There I'm mostly using Docker
[761.24 --> 770.52]  because we want to set up a database and it's not an embedded database. So we need to start a
[770.52 --> 772.00]  database. Which one?
[772.80 --> 778.68]  In this case, it will be Postgres, probably. It was built with MySQL, but I'm sort of transitioning
[778.68 --> 784.82]  it to Postgres as a little bit of a preference of mine. In this case, Docker is mostly serving as sort
[784.82 --> 791.62]  of being so industry standard that it will be familiar to more operations people than actually
[791.62 --> 793.24]  just running a binary would be.
[793.24 --> 799.28]  Yeah. I mean, that's interesting because I think if you are shipping just the app itself,
[799.72 --> 805.48]  then a binary, that's okay, right? Executible, just run it and off it starts. It's no different
[805.48 --> 811.98]  than, for example, a Docker container. Now, if you do have dependencies like Postgres SQL,
[812.62 --> 817.36]  how do you get that started? And which version will you get? And will the package manager have
[817.36 --> 824.72]  the version that you get? And will it have SSL enabled? Maybe it will, maybe it won't. So all
[824.72 --> 830.52]  that configuration now is starting to get into the whole configuration aspect of it. So how do you
[830.52 --> 834.72]  configure it? How do you get them to talk? What about, I don't know, maybe you need to do some
[834.72 --> 839.80]  tunings in Postgres SQL. Will you be shipping them as well? Or will you just let the team that runs it
[839.80 --> 840.84]  figure that part out?
[840.84 --> 848.08]  Yeah. And in this case, we would want to take care of all of that and just provide the Docker
[848.08 --> 854.12]  Compose and like, go ham. And whenever there's an update, maybe we need to tell them to pull a new
[854.12 --> 861.64]  Docker Compose, or maybe they just need to update an image or, but yeah, when you have additional
[861.64 --> 866.38]  infrastructure and you need someone else to set it up, that's a different case for, from, for example,
[866.38 --> 873.26]  how I run my own stuff. Just small services I run. I run beambloggers.com, which is just
[873.26 --> 879.72]  scraping RSS feeds for the Beam community. So if you want to track sort of Erlang and Elixir,
[880.56 --> 891.28]  that's a good place to get an ever-growing RSS feed. But the way I do that is just a release that I
[891.28 --> 899.72]  actually build on a server and stand up there because the availability level I need to maintain
[899.72 --> 901.58]  on that one is whatever I feel like.
[902.50 --> 908.52]  That's a good one. I think that has merit, right? I mean, some use cases, that's perfectly fine.
[908.52 --> 913.32]  Nothing wrong with that. It's all contextual. I keep mentioning this. If that works for you,
[913.74 --> 918.72]  that's great. There's no problem, right? And maybe someone could benefit from that simplicity.
[918.72 --> 924.92]  And that system particularly actually stores all its data in memory. And whenever I restart it,
[924.94 --> 927.48]  it just blows it away and it refitches it from the web.
[927.84 --> 929.00]  That's interesting. Okay.
[929.26 --> 934.98]  It was a fun way of building it, mostly. It means I don't have to deal with any database setup for
[934.98 --> 940.60]  that particular service. I have a few different services where I just keep things around in memory
[940.60 --> 946.26]  because they are fairly ephemeral or like the history isn't particularly important.
[946.26 --> 951.86]  So what I'm hearing is that there are stateless systems, stateless services, which means that
[951.86 --> 958.48]  you could start them anywhere and they would gather data just in time after they boot or maybe part of
[958.48 --> 963.72]  the booting process. I'm not sure when exactly it happens, but there's no state that you have to
[963.72 --> 971.66]  move with a service. So for example, if you were to stand this bean bloggers elsewhere on boot,
[971.66 --> 976.30]  it would get all the data that it needs and would start serving it, it would need to run on a specific
[976.30 --> 976.80]  machine.
[977.30 --> 984.92]  Yeah. So it's very, at least very independent. It's stateful when it runs in that it keeps a lot
[984.92 --> 992.52]  of state around, but it absolutely does not rely on some source of state or needing to carefully
[992.52 --> 999.84]  manage state when it goes up and down. For some other services where I do want to keep history around,
[999.84 --> 1006.78]  I've started using SQLite much more than I used to because that's also operationally much simpler
[1006.78 --> 1014.12]  than Postgres. And I don't find Postgres particularly challenging. It's easy enough to manage and I like
[1014.12 --> 1021.78]  it. But SQLite is even easier and makes a lot of sense if you don't have a lot of heavy needs. And I've
[1021.78 --> 1031.00]  recently seen, so there's a project called Lightstream, which solves one of my bigger concerns with SQLite,
[1031.00 --> 1038.64]  which is replicating it or at least having a very recent backup because it's very easy to accidentally
[1038.64 --> 1046.42]  blast away a file on disk. So it hooks into the write-ahead log of SQLite and just ships it to
[1046.42 --> 1055.10]  NES3 compatible storage on any update. So it does an ongoing replication of SQLite and then you can
[1055.10 --> 1060.40]  just restore from that. I don't think it's necessarily feasible to do sort of high availability
[1060.40 --> 1068.20]  with SQLite. But I mean, if I was building a product right now, sort of a small scale SaaS or
[1068.20 --> 1074.56]  that kind of thing, this would definitely be something I consider. There was a Hacker News thread around the
[1074.56 --> 1083.60]  time that Lightstream got some attention. It's done a few rounds. Someone mentioned running a product
[1083.60 --> 1090.02]  on SQLite and I think they'd benchmarked it to 10,000 reads a second to 5,000 writes a second
[1090.02 --> 1098.70]  on an NVMe drive. That's a lot of read and write activity. A lot more than I would typically expect
[1098.70 --> 1106.60]  to need to serve for a small scale SaaS. And if you can scale with just using something like SQLite
[1106.60 --> 1112.10]  up to that level, then you're probably successful enough that you can switch it out for something
[1112.10 --> 1118.24]  else at that point and make all those decisions about complexity. That is a very good point,
[1118.44 --> 1124.68]  actually. Lightstream, it will be in the show notes, but it's lightstream.io. It's Ben Johnson,
[1124.68 --> 1131.28]  Ben B. Johnson. I think he was on Changelog at some point. I remember this coming up and you're right.
[1131.38 --> 1136.30]  I mean, he's Ben Johnson. He's the author of Bold DB. So, you know, he has some experience in this
[1136.30 --> 1142.08]  area. Let's put it that way. I do remember it sounding really interesting. So you can check it
[1142.08 --> 1149.68]  out if you want. But my takeaway is that you like keeping things simple. And if it gets the job done,
[1150.30 --> 1153.84]  that's it. That's all it needs to be. It doesn't need to be fancy. It doesn't need to be impressive.
[1153.84 --> 1159.38]  It doesn't need to be, you know, look at me, you know, I've done it in this way that no one else
[1159.38 --> 1165.26]  has done it before. It doesn't have to be that. It just has to work. Yeah. And if this works for you,
[1165.46 --> 1174.08]  that's great. Yeah. And since I do consulting for a number of different clients, it's,
[1174.60 --> 1180.04]  I always have to adapt to whatever's already there. So the client that I will be shipping
[1180.04 --> 1186.68]  on-prem for doesn't actually have a thing in place. So that's sort of me putting my opinions
[1186.68 --> 1193.04]  and stamp on that. I'm there to solve that problem. But in other cases, there's an existing ops
[1193.04 --> 1200.32]  person or ops team and I'm mostly shipping code and then I'll roll with whatever they have. And
[1200.32 --> 1204.92]  if I don't like it, I'll be swearing a little bit under my breath and maybe giving them some
[1204.92 --> 1211.96]  some opinions, but, but typically I'm happy to roll with whatever's, whatever's there.
[1212.38 --> 1217.24]  I don't really believe in making radical changes to software that's already working,
[1217.24 --> 1222.74]  even if it's not working in the way you think it maybe should. But there is this
[1222.74 --> 1230.52]  trend also in, particularly in the Beam ecosystem where there's a lot of things you can get done by
[1230.52 --> 1238.60]  using only the Beam. The Beam ship actually ships with an, a distributed database inside of it.
[1239.08 --> 1247.08]  So Amnesia, it has a lot of challenges. It has some sort of conflict resolution problems when you run
[1247.08 --> 1253.88]  it in a distributed fashion. So I haven't been keen on using it for anything else than sort of caching,
[1253.88 --> 1260.12]  but with SQLite in place, then you can actually use the sort of standard tooling in Elixir around
[1260.12 --> 1266.28]  Ecto and which is essentially the ORM, not so much objects, but relational mapper, I guess.
[1266.28 --> 1271.32]  Do you know which is the biggest Erlang project that uses Amnesia?
[1271.64 --> 1273.24]  It would probably be WhatsApp.
[1274.28 --> 1281.16]  They do, but they use it in a different way, very different way. So they, as far as I know,
[1281.16 --> 1287.00]  and this was like many years ago, they used it on just a few servers and they used it for,
[1287.00 --> 1295.24]  I think it was just metadata, but like very small metadata. So nothing that is heavy writes or heavy
[1295.24 --> 1301.88]  reads. And I think the eventual consistency was okay for it. So things did not like, like dirty reads,
[1301.88 --> 1307.16]  for example, were a big thing for them, but they used it like on a subset of nodes and I had like
[1307.16 --> 1312.68]  dedicated nodes for that. And I think they wanted to move away from it or there was talk about that.
[1312.68 --> 1315.00]  This was like at least five years ago.
[1315.00 --> 1315.48]  Yeah.
[1315.48 --> 1322.44]  The project which I have in mind and I had a first class C to it is RabbitMQ. And it's one of its
[1322.44 --> 1330.04]  Achilles heels. Amnesia, oh wow. Like if it's at any sort of scale, you start seeing some serious issues,
[1330.04 --> 1337.32]  like 10,000 writes per second. No way. No way. Because it's the synchronization part and you have
[1337.32 --> 1342.92]  to go over a network and you have multiple nodes and it's all synchronous. So you have transactions.
[1343.88 --> 1351.48]  Yeah. So you have to typically look at Amnesia in the context that was created, which was telecom.
[1351.48 --> 1357.80]  And as far as I understand, it was typically between machines that were very tightly coupled together.
[1358.52 --> 1363.00]  I've heard people talk about back planes and I have no idea what that is. So I'm not even going to try.
[1363.96 --> 1373.72]  But yeah, it was about managing. So phone calls and that kind of connecting, which is very different
[1374.44 --> 1380.92]  from your typical sort of web app or like we're keeping everything around forever type of
[1380.92 --> 1387.64]  infrastructure that we deal with now. I've definitely looked for something that would
[1388.68 --> 1394.68]  essentially scale arbitrarily as a database across nodes as you add more. Not that I have the need,
[1394.68 --> 1399.88]  just because I want to see if there's sort of the perfect solution out there. And I found CockroachDB
[1399.88 --> 1406.84]  to be very appealing in that sense, because it's Postgres compatible and it's made to be distributed by
[1406.84 --> 1415.88]  by default, which Postgres has a lot of upside and it's great, but it is not built to be distributed
[1415.88 --> 1423.00]  by default. And they've built a lot of sort of distributed features into it, but you know very well
[1423.00 --> 1431.08]  what can happen when you try to replicate Postgres. I thankfully haven't had a reason to spend too
[1431.08 --> 1439.32]  much time replicating Postgres. But yeah, looking at Cockroach though, you'll also see that sort of
[1439.32 --> 1448.52]  suggested specs and what they suggest for setting up Cockroach, there's a lot of concerns and a lot of
[1448.52 --> 1455.24]  things to think about and a lot of details suddenly that you don't typically think about when you're
[1455.24 --> 1461.80]  setting up a single Postgres instance. And I think this feeds sort of into the whole idea of Kubernetes
[1461.80 --> 1469.96]  as well. That's like, oh, but this is an abstraction layer that simplifies everything. It generalizes
[1469.96 --> 1477.00]  everything so you don't have to think about all the details. But in my book, you can never, ever stop
[1477.00 --> 1482.84]  thinking about the details. It's like, okay, we brought in Kubernetes, so now we don't have to know
[1482.84 --> 1491.40]  how Linux works? No, no, I don't think so. Or what's your experience there? Does bringing Kubernetes in
[1492.44 --> 1495.88]  make you stop having to care about your Linux installations?
[1505.80 --> 1511.64]  What's up shippers? This episode is brought to you by our friends at Teleport. With Teleport Access
[1511.64 --> 1517.16]  Plane, you can quickly access any computing resource anywhere. Engineers and security teams can unify
[1517.16 --> 1523.00]  access to SSH servers, Kubernetes clusters, web applications, and databases across all environments.
[1523.32 --> 1528.12]  Teleport is open core, which you can use for free, and it's supported by their cloud hosted version,
[1528.12 --> 1533.16]  which lets you forget about configuring, updating, or managing Teleport. The Teleport team does all
[1533.16 --> 1539.00]  that for you. Your team can focus on your projects and spend less time worrying about infrastructure access.
[1539.00 --> 1543.16]  Try Teleport today in the cloud, self hosted, or open source. Head to
[1543.16 --> 1547.80]  GoTeleport.com to learn more and get started. Again, GoTeleport.com
[1547.80 --> 1561.56]  You mentioned a couple of things which I would like to dig in a little bit more.
[1561.56 --> 1569.40]  First of all, you mentioned about using PostgreSQL in your most recent project that you're doing for
[1569.40 --> 1574.76]  a customer, the one that you're deploying using Docker Compose, or that you're using Docker Compose to run it.
[1575.64 --> 1581.32]  And I'm wondering in that context, why did you choose PostgreSQL over SQLite?
[1581.32 --> 1585.80]  Yeah, that's actually a very good question, and I've been wrestling with it myself a little bit.
[1585.80 --> 1596.28]  So one of the big reasons is that the current SQLite adapter for Elixir is fairly new.
[1597.08 --> 1605.64]  And SQLite is very reliable, but I don't feel like that particular adapter has necessarily been proven
[1605.64 --> 1615.16]  out yet. And shipping that to customers before I'm certain and I have a track record with it.
[1616.44 --> 1622.68]  That's more than a few experiments. I just don't feel entirely comfortable doing that. So I opted for
[1623.32 --> 1629.96]  even steering them away from MySQL, which is perfectly well supported into what is the absolute main
[1629.96 --> 1639.08]  line of Phoenix, which is PostgreSQL. It seems to have the community behind it. Partly, I want to leave
[1639.08 --> 1646.52]  the client with something that other developers will definitely recognize and be capable of working with.
[1647.48 --> 1653.88]  If it ends up that I'm not around in the long run or for whatever reason, I want to bring us closer to
[1653.88 --> 1660.28]  the main line. And there are a few very cool projects and very useful projects in the Elixir community that
[1660.28 --> 1667.08]  lean on PostgreSQL specific features. One of them is Oba in a job processor. So having the option of using
[1667.08 --> 1675.16]  that is also a good one. But this would be a good project for a SQLite and shipping that. There's also
[1675.16 --> 1681.32]  a little bit of a question mark around some backups. Like, okay, then we will want to use Lightstream.
[1681.32 --> 1687.56]  But do I have something S3 compatible to ship it to? Or do I need to stand that up myself and then
[1687.56 --> 1693.16]  pull the file out and throw it at... Yeah. Those are very good points. And I really like the way
[1693.16 --> 1697.64]  you're thinking about this because it's about confidence. Whatever you're giving, right? When
[1697.64 --> 1703.48]  you're, let's say, shipping it and here you go, customer, this is what was done for you. Someone has
[1703.48 --> 1709.80]  to maintain it. Someone has to deal with all the issues that arise because they will arise. Updates,
[1709.80 --> 1714.20]  hello. Everybody seems to forget about them except when they have to be done and then they don't do
[1714.20 --> 1721.24]  them because updates now. It's very important to keep up with those things. CVEs, right? How do you
[1721.24 --> 1726.68]  address CVEs if you don't have a good way of releasing these updates out there? And if you're
[1726.68 --> 1731.88]  not confident in what you have and, you know, like the point that you reach, it becomes a bit more
[1731.88 --> 1737.16]  difficult to take those small steps, those small improvement steps. So I think it makes perfect sense.
[1737.16 --> 1742.60]  Not to mention that, as you said, you may not be around. Someone else may take this over and you
[1742.60 --> 1748.60]  want them to take over the most supported, the most documented, the most known thing, right?
[1748.60 --> 1754.20]  Yeah. And I think Ruby on Rails was like that for a long, long time in that I can see a lot of parallels
[1754.20 --> 1760.12]  between Ruby on Rails and Phoenix. And there were some good sensible defaults in Ruby on Rails that if you
[1760.12 --> 1767.88]  went outside of those, there was a lot of pain there. So sure, you can use MongoDB, but why would
[1767.88 --> 1773.48]  you with your Ruby app? Just stick to my SQL, like that's what the majority does. And I do remember
[1773.48 --> 1777.72]  being in situations in the past when we did that and there was some pain there. The drivers were
[1777.72 --> 1783.24]  great. I still remember many discussions with Jordan. I forget his family name, but he was the
[1783.24 --> 1788.36]  the maintainer of Mongoid, I believe, if I remember it correctly. And that was a great library, but
[1788.36 --> 1792.68]  still there were issues that you wouldn't expect. So it just goes to show that even from my experience,
[1792.68 --> 1801.72]  I remember moments when I wished I had chosen the default and I didn't. And not just me, but others
[1801.72 --> 1806.84]  paid the price for that. And it was just not fair. So if I learned anything, if you can stick with the
[1806.84 --> 1812.28]  defaults or like with the most common path, especially in these cases, it may be best to. Now, if you have a
[1812.28 --> 1816.44]  personal project like you have, right, like you have a couple of like experimental projects,
[1816.44 --> 1822.12]  you can use anything you want because your SLO is whatever you want it to be. And it can change from
[1822.12 --> 1827.88]  day to day and it's fine. So it doesn't really matter. But for others, you know, that's reliability,
[1827.88 --> 1833.64]  upgradeability is important. You need to choose differently. Yeah. Sometimes it pays to make a
[1833.64 --> 1839.96]  dull choice here and there. Yes. I'm happy to go absolutely wild on my own projects,
[1839.96 --> 1846.60]  but it's also things like if I'm shipping a library to the community, that's also where I will be
[1846.60 --> 1853.32]  looking quite closely at like, okay, but what is a good library? What does it mean to be behave well as
[1853.32 --> 1860.52]  a library in this ecosystem? I can't just put all of my opinions in there if I want to be a sort of good
[1860.52 --> 1869.72]  citizen. Yeah. I think that sort of carefulness about what you choose, that's something I've picked
[1869.72 --> 1877.48]  up with, with the years. I've definitely had a few, a few years of chasing shiny new frameworks,
[1877.48 --> 1885.40]  shiny new ops technology, setting up servers in cool new ways, building a custom microservice
[1885.40 --> 1889.88]  architecture from the ground up. Just because you could, right? Now the reason I can do this,
[1889.88 --> 1894.52]  so why not? No, no. Oh, we absolutely needed to scale that product so hard. That's actually what
[1894.52 --> 1899.40]  we had sort of as an objective. Like this has to be scalable. The last iteration of this product was
[1899.40 --> 1904.52]  not scalable. Let's greenfield it. Let's build it right. It should be able to scale. And that
[1904.52 --> 1909.16]  architecture could absolutely have scaled, but that product did not need that scale at all.
[1910.04 --> 1915.48]  It could have been so much simpler. That's a good, like why, why does it need to scale? If you don't
[1915.48 --> 1924.36]  ask enough why's, like why with an S at the end, you will like, this is something which I have seen,
[1925.16 --> 1931.24]  teams and products that keep going in the wrong direction. And then it doesn't matter how fast
[1931.24 --> 1936.60]  you go in that direction because it's so wrong. You're going infinitely, infinitely fast in the wrong
[1936.60 --> 1941.24]  direction. So we're going infinitely slow, right? Because it's like, you're not even going in the
[1941.24 --> 1947.56]  right direction. So what's the point? Why are you rushing towards a direction that doesn't benefit
[1947.56 --> 1952.60]  anyone? And then years later, people will be asking, but why do we do that? And no one will recall
[1953.56 --> 1956.76]  because it doesn't make any sense, right? Like things that don't make sense, people tend
[1956.76 --> 1959.24]  people tend to forget. Like you're right. It doesn't make sense.
[1959.24 --> 1965.72]  Yeah. I wrote a retrospective on that particular architecture, the entire product through like
[1965.72 --> 1970.76]  three different iterations and put it on my blog. And I've had some interesting feedback on that because
[1971.80 --> 1976.28]  people don't always share. I wouldn't even call it a failure story because the product was a success
[1976.28 --> 1983.64]  and it did fine until it was shut down at some point. Yeah. Some of the technical choices I would not
[1983.64 --> 1989.64]  make again, but that's where I learned that I probably shouldn't have done that or shouldn't
[1989.64 --> 1994.20]  have done it that way. Some of the choices checked out. Some of them didn't.
[1994.20 --> 1999.48]  So in that retrospective of a post that you wrote, by the way, what's the title of the post?
[1999.48 --> 2004.60]  I think it's 10 years in the vertical. 10 years in the vertical. Okay. We will link it in the show
[2004.60 --> 2009.96]  notes for those that want to read it. It's a three part series, one version of the system.
[2009.96 --> 2015.32]  Awesome. So get your coffee ready, tea ready, whatever you're drinking, strap down. It's a
[2015.32 --> 2020.76]  long one, but a good one worth it. Right. I will read it myself by the way, because it sounds very
[2020.76 --> 2025.64]  interesting. Is it funny? I'm not sure if it's funny. I hope it's a little bit funny.
[2025.64 --> 2030.12]  That's the killer. I definitely had good feedback on it. So it should be bearable to read at the very
[2030.12 --> 2035.56]  least. Okay. All right. The coffee will make it worth it. No, no, no. I'm joking. Like the funny and
[2035.56 --> 2039.64]  interesting, it's like a killer combo. And if you can do both, it's great. Right. It's like,
[2040.12 --> 2043.64]  the jackpot I think of content. And on the shipping side of that,
[2043.64 --> 2049.72]  that was mostly Ansible, but it ended up being a lot of Ansible because we did split everything
[2049.72 --> 2055.24]  up into microservices. Oh yes. For a three person team. That's what you get, right? I mean,
[2055.24 --> 2060.20]  it's like one of the trade-offs that you get and you may need that, right? I know that some teams do,
[2060.20 --> 2065.48]  but not everyone does. And knowing the difference when to use a microservice versus a monolith is a very
[2065.48 --> 2071.56]  important thing. Like know the answer before you embark on the journey. And even if the answer
[2071.56 --> 2078.28]  comes slower, it's worth it. Take your time. Because getting out of that particular journey,
[2078.28 --> 2083.80]  it will be very difficult. It can be done, but it's unlikely to happen. So it's one thing that
[2083.80 --> 2088.28]  you want to choose wisely. You could choose maybe your cloud provider, you can migrate,
[2088.28 --> 2095.08]  and even that can be a bit difficult, but it's easier than going back from a microservice decision
[2095.08 --> 2099.08]  or a monolith one. By the way, sometimes that is the wrong decision. So we're not saying that one is
[2099.08 --> 2105.32]  better than the other. No. Okay. So we covered about, like we touched on a couple of interesting
[2105.32 --> 2111.00]  things, but I still think we haven't dug deep enough in the whole, before you mentioned about
[2111.00 --> 2115.80]  Kubernetes. So I don't think we dug deep enough into that. One of the reasons why we're even having
[2115.80 --> 2121.08]  this conversation, because I know that for you, Kubernetes doesn't make sense. And that fascinates
[2121.08 --> 2126.36]  me because I'm not saying that everybody should use that. I'm not saying that, but I can see a lot more
[2126.36 --> 2132.84]  reasons to use it than not to use it. And it's that API that, from my perspective, is the best thing
[2132.84 --> 2139.64]  that it has. So it's how it approaches operations and the building blocks that you have at your
[2139.64 --> 2147.08]  disposal. You can achieve the same thing in different ways, but I don't know, having tried most of them,
[2147.08 --> 2155.16]  I kind of like it and it makes a lot of sense. So why in your case, Kubernetes, you're not using it
[2155.16 --> 2159.88]  at all, right? Because I don't think you're using Kubernetes. You hear about it a lot, but you don't
[2159.88 --> 2166.92]  use it. Why is that? My experience with Kubernetes is essentially, I tried K3S at some point and started
[2166.92 --> 2173.88]  sort of learning how to set up manifest files and a lot of swearing ensued. And then I stopped,
[2174.52 --> 2183.24]  essentially. For one thing, I don't generally build systems at a large scale. I typically work with
[2183.24 --> 2188.60]  teams that are maybe five developers or so. That didn't stop us from using Kubernetes
[2188.60 --> 2192.76]  changelog, right? There were like, what, three developers? And like one full time,
[2192.76 --> 2197.00]  and even not that much full time, and we're still using Kubernetes. So that didn't stop anyone.
[2197.00 --> 2198.04]  Yeah. But please continue.
[2198.04 --> 2202.36]  Yeah. I could argue with you whether a changelog should be using Kubernetes.
[2202.36 --> 2204.36]  Yes, please. Let's.
[2204.36 --> 2211.16]  I for sure do not see the need for a system such as the changelog to have Kubernetes. Now,
[2211.96 --> 2219.00]  again, context, the guy that's responsible for operating changelog apparently likes Kubernetes,
[2219.64 --> 2227.80]  which means that he enjoys his job more if he gets to run it on Kubernetes. So it sort of checks out.
[2227.80 --> 2230.92]  But it's not that because I'm that guy. So just like for the listeners, that's me.
[2230.92 --> 2234.12]  Oh, yeah. Yeah. I'm absolutely talking about you there.
[2234.12 --> 2239.32]  I'm that guy. Okay. So let's unpack this. I tried to answer this question a couple of times,
[2239.32 --> 2245.56]  and either people, I must be answering it wrong. So let me try again. Okay. The reason why we chose
[2245.56 --> 2251.96]  Kubernetes is because it reached a certain level of maturity. That was one of the things. And Linode,
[2251.96 --> 2256.92]  our partner for all things infrastructure, they started offering a managed Kubernetes service.
[2256.92 --> 2261.80]  So that was important for us, right? We don't want to deal with managing it. So that is a provider
[2261.80 --> 2269.16]  concern. We had to solve a couple of things, like for example, DNS. DNS updates, like whenever the IP
[2269.16 --> 2275.08]  changes or the load balance that changes, the IP has to be updated in the DNS. The certificate,
[2275.08 --> 2280.36]  we used to pay for those. And then Let's Encrypt came along. So how do we get free certificates
[2280.36 --> 2284.84]  via Let's Encrypt and support that mindset?
[2284.84 --> 2286.20]  A cron job.
[2286.20 --> 2292.52]  A cron job. Excellent. Okay, great. Great. A cron job. So yeah, that is a valid answer.
[2292.52 --> 2301.24]  And then how do you push updates? Like, do you have your CI that deploys? In some cases you do,
[2301.80 --> 2307.16]  right? In some cases, the CI is the thing that has the keys to the kingdom. And that's what we had.
[2307.16 --> 2312.52]  And it can do anything. Is that a good thing? I don't think it is. But whatever, you know,
[2312.52 --> 2318.84]  it's just like an opinion. But there's more. How do you keep your certificate in sync between your CDN,
[2319.96 --> 2326.28]  your load balancer, and any other place that may use it? In our case, it was just these two,
[2326.28 --> 2330.60]  the load balancer and the CDN. So you have to keep, not only have to renew it, but then you have to
[2330.60 --> 2335.32]  upload it and make sure it's the same one everywhere. Excellent. How do you run backups?
[2335.32 --> 2341.64]  Another cron job, right? So before you know it, you have like all these things that you need to
[2341.64 --> 2346.84]  have. Like what gets, for example, Docker Compose or whatever you're using in place? What installs
[2346.84 --> 2352.44]  Erlang? What determines which version of Erlang you have? What about the monitoring? Where do you run
[2352.44 --> 2357.64]  that? How do you configure the monitoring? How do you configure, for example, the monitoring, not just
[2357.64 --> 2363.00]  like the metrics and the logging, but I'm also talking about the synthetic monitoring, your pings,
[2363.00 --> 2367.40]  your pingdoms, or your Grafana clouds, or whatever you may be using. And before you know it, you have
[2367.40 --> 2375.56]  all these concerns that typically are either in a wiki or in someone's head or different people
[2375.56 --> 2379.80]  approach it in different ways. In this case, it's just me. So, you know, it's not really a problem,
[2379.80 --> 2383.64]  but you have all these things, secrets. Oh, that's like another one. Where do you store
[2383.64 --> 2396.04]  the secrets and how do you rotate secrets when there's a leak?
[2401.24 --> 2407.16]  This episode is brought to you by our friends at Cockroach Labs, the makers of CockroachDB,
[2407.16 --> 2413.08]  the most highly evolved database on the planet. With CockroachDB, you can scale fast, survive
[2413.08 --> 2419.64]  anything, and thrive everywhere. It's open source, Postgres wire compatible, and Kubernetes friendly,
[2419.64 --> 2424.04]  which means you can launch and run it anywhere. For those who need more, you can build and scale
[2424.04 --> 2429.32]  fast with Cockroach Cloud, which is CockroachDB hosted as a service. It's the simplest way to deploy
[2429.32 --> 2434.60]  CockroachDB and is available instantly on AWS and Google Cloud. With Cockroach Cloud,
[2434.60 --> 2440.36]  a team of world-class SREs maintains and manages your database infrastructure so you can focus less
[2440.36 --> 2445.24]  on ops and more on code. Get started for free with a 30-day free trial or try their new forever
[2445.24 --> 2450.04]  free tier that's super generous. Head to CockroachLabs.com slash changelog to learn more.
[2450.04 --> 2453.08]  Again, CockroachLabs.com slash changelog.
[2453.08 --> 2468.60]  The way I approach this is what is a system that can manage all these things in a way that doesn't
[2469.24 --> 2474.76]  have me worrying about versions as much? Because we use Terraform and we had to do upgrades because
[2474.76 --> 2480.84]  it was running locally. We had plugin issues, we had to upgrade those. And the issues were like
[2480.84 --> 2486.04]  stuff like things that you, problems that you wouldn't expect to have that we were having
[2486.04 --> 2491.80]  because of like this different tooling that we're using. We used Ansible. Did we use Chef at some
[2491.80 --> 2495.64]  point? No, we didn't use. We only used Ansible at some point many, many years ago. By the way,
[2495.64 --> 2499.56]  there was like a progression. So every year we blogged about this. We talked about this.
[2499.56 --> 2504.44]  It didn't just come out of the blue. I know, let's use Kubernetes. No, we've been using Ansible for years.
[2504.44 --> 2509.72]  We've been using Concourse CI to run the builds, to do the deploys. We used Docker Compose and then
[2509.72 --> 2515.64]  Docker Swarm for again, a couple of years. So we grew into this architecture. And right now,
[2516.52 --> 2522.68]  everything is stored, like all the YAML, all the config is stored in the repo. Okay, we have some
[2522.68 --> 2529.24]  Make Glue, which I'm not very proud of. It's great, but I know there's a better way. Maybe Argo CD. I don't
[2529.24 --> 2534.04]  know. GitOps. I keep hearing about that. Maybe we try that. I don't know. But can we have something
[2534.04 --> 2538.68]  that continuously applies those configs and you don't have to have your machine to run that stuff?
[2539.56 --> 2545.16]  So maybe something like a control plane, which is different from your service. And I know that
[2545.16 --> 2549.56]  you mentioned like large scale. I don't think changelog is very large scale. It's a simple app,
[2550.20 --> 2555.80]  but it's still serving many of terabytes every month of traffic. And there's the CDN. When the CDN
[2555.80 --> 2559.88]  goes down, there's a big problem as we had a couple of days ago. And you have to know how to
[2559.88 --> 2565.80]  basically update it very quickly, which we could. And you have to have that space and room. So the
[2565.80 --> 2570.12]  answer is a bit more complicated. It's contextual. And it's not because I like Kubernetes, it's because
[2570.12 --> 2576.84]  it makes all these concerns easier than if we used anything else than we did before, by the way. It
[2576.84 --> 2584.20]  improves on that. Yeah. What do you think about that? Easier for you, I would say. For me, it's like,
[2584.20 --> 2590.60]  I barely know where I would start on making Kubernetes do this. And I did start looking at
[2590.60 --> 2596.76]  K3S specifically because I wanted the CD part. I wanted something to pick up my finished Docker
[2596.76 --> 2602.84]  containers and spin up the new version. That's essentially why I wanted to set that up to have
[2602.84 --> 2611.72]  a very, very lightweight approach to what Kubernetes can do. The thing is, I don't see sort of keeping the
[2611.72 --> 2620.76]  load balancer up to date or keeping certificates up to date as that complicated of an endeavor with
[2620.76 --> 2627.80]  sort of current baseline tools like Let's Encrypt. So I wouldn't bring in layers to solve them.
[2628.60 --> 2635.00]  It could be a bash script. It could be some fairly tightly specced tool. So for example, in Elixir,
[2635.00 --> 2641.72]  there is a fantastic library by Sasha Jurich, which is called Site Encrypt, which will simply do the
[2641.72 --> 2647.08]  Let's Encrypt dance for you if you configure your Phoenix app to use it. So when you start your
[2647.08 --> 2653.16]  application, it checks, do we already have certificates lying around? I'll use those. If not, I'll talk to
[2653.16 --> 2660.76]  Let's Encrypt. We'll shake hands. I'll get some certificates. And now we're certified. And with that,
[2660.76 --> 2666.20]  to some extent, you might not even need Nginx at that point. I bet you would probably be able to
[2666.20 --> 2672.20]  serve changelog with the previously mentioned SQLite performance of like 10k reads a second.
[2672.84 --> 2678.28]  You were talking about terabytes and that's like the MP3 files, right? So file serving is one of the
[2678.28 --> 2686.20]  places where I would typically reach for sort of proprietary cloud stuff like S3 or Linode Object
[2686.20 --> 2694.68]  store or one of those because it just solves a lot of the like, okay, I want to have some redundancy
[2694.68 --> 2702.92]  in this. I want to be able to scale it essentially arbitrarily. For file serving, I would typically use
[2702.92 --> 2708.92]  a service like that. Just it's super annoying dealing with large drives and RAID. So I'd rather not.
[2708.92 --> 2714.28]  So pragmatism, I don't think you should like peel everything off, but I'm also not sure like,
[2714.76 --> 2720.44]  when do you actually need a load balancer? Having Nginx in front of your app can be very nice
[2721.80 --> 2727.16]  because it allows you to do things like, oh, actually we're down for maintenance right now.
[2727.16 --> 2732.12]  I still want to show something nice to the user or pointing to different instances that you're
[2732.12 --> 2737.64]  starting up or whatever. But there's also the potential risk of your Nginx being
[2737.64 --> 2746.12]  misconfigured or less well configured than your application and actually being a bottleneck
[2746.12 --> 2752.12]  to your application. So I've seen that happen too. Typically, I would set something up with Nginx.
[2752.68 --> 2758.84]  But also one of the things with Kubernetes is all this, like any node can go away at any time where
[2758.84 --> 2766.20]  we're on very moving ground cloud infrastructure. We only use what we need, but you always need some.
[2767.08 --> 2774.28]  So usually you're at a base level, like we have these instances up constantly. At that point,
[2774.28 --> 2780.92]  I'm like, but do you need a cluster of three instances running the actual Kubernetes and then
[2780.92 --> 2788.04]  like an app instance and a DB instance and like a load balancer instance? Or is this like one
[2788.04 --> 2792.68]  application instance and one database instance? Would that do?
[2792.68 --> 2797.88]  I think it would. And if you look at changelog at its core, that's exactly what we have. We have
[2797.88 --> 2802.76]  the application and we have the database, single instance PostgreSQL. There's a great story how we
[2802.76 --> 2807.80]  used replicated PostgreSQL and how that was the cause of a couple of downtimes. I think we cover
[2807.80 --> 2809.88]  that in the episode one. Yeah.
[2809.88 --> 2815.08]  A different story. And CockroachDB, that's something which I definitely want to try out.
[2815.08 --> 2820.84]  Distributed PostgreSQL with a PostgreSQL compatible wire format. That's a very interesting one to try
[2820.84 --> 2827.88]  out for sure. It's on my list. But I think what I'm hearing, going back to what you were saying,
[2827.88 --> 2835.72]  is that for you, getting started with Kubernetes seems very complicated for a value that isn't very
[2835.72 --> 2841.48]  clear. Like what is the value proposition? A lot of the things that you can do today,
[2841.48 --> 2849.08]  I mean, does Kubernetes make them any different? And maybe the answer is no, from your perspective,
[2849.08 --> 2854.60]  right? You're saying like, let's just use a cron job. In my mind, I think this is where I wish we had
[2854.60 --> 2859.00]  more time to dig into this. So what I'm proposing is a follow-up because we will run out of time.
[2859.00 --> 2864.68]  But there's so much more. So there's so much more to like, for example, the monitoring,
[2864.68 --> 2868.68]  the shipping of logs, like all those things. And you have to configure them somehow. Then you have
[2868.68 --> 2875.00]  to worry about OS patches, whichever host OS you're running. That is not an issue when you're running in
[2875.00 --> 2881.56]  the context of Kubernetes because it's just your container, right? And you don't care about the node,
[2881.56 --> 2887.24]  the worker node that runs the kubelet, that runs like the Kubernetes infrastructure, so to speak.
[2887.24 --> 2892.68]  When it comes to Nginx, you don't install Nginx. You have ingress Nginx, which is a component
[2892.68 --> 2899.00]  that exposes certain CRDs, custom resource definitions. And it's more like it implements
[2899.64 --> 2904.92]  ingresses. Now, what is an ingress? Do you care about it? Well, you do because you need to know
[2904.92 --> 2912.28]  how to configure it. But beyond that, how that maps to a Nginx concepts, that's abstracted away from
[2912.28 --> 2916.84]  you. And you have like this self-discovery service, and it's all just happening behind the hood.
[2916.84 --> 2920.68]  And you're right, it feels a bit magical, but it's no different to a framework. Like,
[2920.68 --> 2925.80]  for example, if you use Phoenix. But that's the whole thing. See,
[2925.80 --> 2932.12]  Phoenix is a fairly explicit framework. It has a few things that feel a bit magical.
[2932.12 --> 2937.72]  Yes. But it is quite explicit about what everything does.
[2937.72 --> 2939.32]  And Kubernetes isn't.
[2939.32 --> 2947.40]  Yeah, it's not the impression I'm getting. But what I see when you're bringing in something like
[2947.40 --> 2952.52]  Kubernetes, you're placing a lot of abstractions in place, and you're going to be working with those
[2952.52 --> 2959.24]  abstractions. Those abstractions are still doing all of the things under the hood. And you need to be
[2959.24 --> 2966.76]  aware of how they do those to be able to do it gracefully. Most of the use cases and most of the
[2967.96 --> 2975.40]  the way you want to work with infrastructure should be ideally enshrined in how Kubernetes handles this.
[2976.20 --> 2983.80]  But I don't feel like you can just say, okay, but now I don't have to care about this. Still have to care
[2983.80 --> 2993.48]  about sort of updating Linux. You still have to care about how your search are propagated, or you could
[2993.48 --> 3001.32]  get kicked off of let's encrypt or there's a lot of automation, but it's also very generalized. So
[3002.20 --> 3009.00]  this is a thing where I think Kubernetes ends up being a bit over, I wouldn't say it's over-engineered.
[3009.00 --> 3015.16]  It's a, it's don't repeat yourself taking quite far. And that's the correct move for some cases.
[3016.12 --> 3022.36]  For example, you'll see an enterprise software, things are often very generalized and the software
[3022.92 --> 3028.28]  is generally not that tight to work with. It's, it's usually a little bit annoying and a little bit
[3028.28 --> 3034.60]  too much. And that's sort of the experience I'm, I'm getting from everything I see and hear about
[3034.60 --> 3039.88]  Kubernetes. It, it tries to solve everything and I don't need my everything's solved.
[3041.88 --> 3047.16]  So there is this opposite direction. I can take things in when working with Erlang Elixir and the
[3047.16 --> 3054.28]  Beam, where the Beam, which is meant to handle sort of high availability, high reliability,
[3054.28 --> 3060.12]  concurrent distributed systems. And I can bring all of my application concerns in there. It's like,
[3060.12 --> 3068.60]  do I need an SSH server? Well, they have one. Do I need to talk to DNS? Do I need to do DNS? Yeah,
[3068.60 --> 3074.76]  there's probably something in there for that. And that's, that's a very rare runtime that you can,
[3075.72 --> 3081.88]  that you can lean on to, to do that kind of thing. But let's say, for example, shipping updates to your
[3081.88 --> 3087.00]  app, the Beam can hot code update your app while it's still running without ever taking it down.
[3088.20 --> 3094.36]  That's a little bit trickier to use than a lot of other ways. It's not like bringing your container
[3094.36 --> 3101.08]  down and then bringing up another one, but it's definitely a capacity that's, that's there. And I
[3101.08 --> 3107.64]  think like a Beam application can handle like everything that I need to get done, but also
[3108.60 --> 3115.96]  the 99% case or the 90% case for small products and SaaS. Like if you need a bit of observability,
[3117.00 --> 3123.32]  you have, for example, live dashboard, which gives a baseline of observability with no effort,
[3123.32 --> 3129.16]  or you install something like Promex and then you need to have Prometheus and Grafana stood up
[3129.16 --> 3134.60]  somewhere. Then you're starting to get a little bit more infrastructure or you use the cloud offerings.
[3134.60 --> 3140.04]  And I think that's sort of always what it boils down to. Like at a certain point, you need more,
[3140.04 --> 3146.44]  more visibility into the details. Okay. At a certain point, you should probably start looking at
[3146.44 --> 3152.20]  installing something to give you that. But Kubernetes is installing all of it at once.
[3153.08 --> 3158.92]  And you have to care about search. You have to care about the DNS details. You have to care about the
[3158.92 --> 3165.80]  ingress. You have to care about all of it. And I think the, both the barrier and sort of the
[3165.80 --> 3172.20]  maintenance cost of it is something I wouldn't choose to take on in lightly in any project.
[3173.48 --> 3178.20]  Because I think it's too, typically too early for Kubernetes. And I'm thinking it's probably too
[3178.20 --> 3185.08]  early for Kubernetes in most projects before they're like at an international scale. Like if you need
[3185.08 --> 3193.00]  high availability across many regions and time zones, that's probably a good reason to use Kubernetes.
[3193.00 --> 3200.52]  But I also realized like, if you spend a lot of time working with Kubernetes, setting it up might not be
[3200.52 --> 3210.04]  that much effort. I'd rather code a fairly custom sort of deployment setup that I find explicit and simple,
[3210.04 --> 3219.48]  than lean on something I understand so poorly, and which would take me years to have a good grasp of,
[3220.52 --> 3221.72]  which is Kubernetes.
[3221.72 --> 3227.16]  I think there is a lot of, well, okay. So first of all, there's simplicity and complexity,
[3227.72 --> 3232.44]  and the other way around. But in this case, in Kubernetes, it's complex, but it's also simple,
[3232.92 --> 3238.12]  if you look at it from a certain perspective. So things are fairly well defined. Like,
[3238.12 --> 3242.68]  you know what you need to reach out for and how to combine things. And there's like a whole community
[3242.68 --> 3247.48]  around it. There's like so many projects which are solving specific issues. The interface is very
[3247.48 --> 3253.00]  clear. You know how to interact with it. There's an API. It's this single API by which you request
[3253.00 --> 3258.28]  anything, including other VMs, other load balancers. Do you want a SQLite instance with
[3258.28 --> 3262.76]  such and such provider? You can get that. Okay. You have to extend Kubernetes in order to benefit
[3262.76 --> 3268.76]  from these features, but it's possible. And there's only one way that you can do this. And that's very
[3268.76 --> 3276.84]  powerful. I think the separation of concerns, it gets a bit more clear. So anybody just ship us a
[3276.84 --> 3282.52]  container image. It doesn't matter what language you have. It doesn't matter what VM you're running.
[3282.52 --> 3287.96]  Ship us a container image will take care of the rest. Okay. Now I know it's too simplistic,
[3288.92 --> 3294.84]  but it works. Like Heroku, for example, shipping containers, they made it popular. You just get push
[3294.84 --> 3300.44]  and things happen. And guess what? The way the changelog is being developed hasn't changed. You get push
[3300.44 --> 3306.12]  and things happen behind the scenes. And because that contract has never been broken with the
[3306.12 --> 3313.80]  developers, everybody's happy. Yeah. Gerald would be pissed if he had to, as his agent to the servers,
[3313.80 --> 3318.36]  to set things up. There you go. Yeah. That's no good. Yeah. Do you really care about like which OS
[3318.36 --> 3323.48]  you're running? No, you don't. Do you want to switch Erlang versions? Super easy. Guess what? All you have to do is
[3323.48 --> 3329.24]  change the container. Hot code reloading? Yes, you can do it. It's hard. Maybe you don't need to.
[3329.24 --> 3335.24]  And again, it doesn't matter whether you use Erlang or Elixir or Ruby or Python or Go. It really doesn't
[3335.24 --> 3340.68]  matter. Do you want to use serverless? Well, guess what? You have all these projects which you can set
[3340.68 --> 3347.08]  up and you can run it on in the same context. And the list goes on and on. I mean, it's really,
[3347.08 --> 3354.68]  it just goes forever. And it's not like I have used Chef for many years. I was G Chef at one point,
[3354.68 --> 3360.12]  Gerhard Chef. That's like even in Oregon, GitHub. So I spent like a fair time with that knife when that
[3360.12 --> 3365.12]  was a thing. I don't think many people were using, because Chef server was so difficult. I was there.
[3365.24 --> 3372.40]  I remember that period. Ansible, I loved it when it was a thing. Certain things were difficult with it,
[3372.40 --> 3381.38]  but it was saner than Chef. Is Kubernetes saner than Ansible? I don't know. For us,
[3381.58 --> 3386.14]  it felt like the next evolution. You're right. There is a learning curve. Like Vim, there will be,
[3386.24 --> 3393.76]  or Emacs. Kubernetes is definitely a big step in some direction from Ansible. It's not just the next
[3393.76 --> 3399.12]  sort of iteration on scripting your servers. That's not what it is. It's something different.
[3399.12 --> 3404.58]  And you did ask me for a sort of hot take that you could put as the title on this. And I think,
[3404.92 --> 3410.16]  like, would it be fair to say Kubernetes is the electron of operations?
[3410.54 --> 3415.92]  It's the electron. Oh, okay. Wow. I think people are like, what is electron? That would be the
[3415.92 --> 3417.00]  first thing I would ask. What?
[3417.52 --> 3423.28]  What is electron? Which electron do you mean? Do you mean the physical one or the electron JavaScript?
[3423.28 --> 3432.32]  Oh, you're like, ooh, physics. No, I mean, yeah. I mean, in that it makes operations at the outset,
[3432.76 --> 3442.68]  a lot simpler, but it also paves over everything that you could get right in the details. I feel like,
[3443.08 --> 3449.34]  I think you have access to every little detail you would need in Kubernetes, but it doesn't
[3449.34 --> 3456.08]  particularly seem to encourage you getting into all the details. So whenever you add abstraction
[3456.08 --> 3464.90]  layers, and I think that's sort of my, my hesitance on adding more tools, especially tools that sit on
[3464.90 --> 3475.02]  top and sort of obscure what's going on is that I've come to rely on explicit things, because if you can
[3475.02 --> 3481.18]  just read the code and see what it's going to do, that's, that's very powerful. I mean, it's not
[3481.18 --> 3488.52]  declarative. People like declarative for particular things and declarative can be nice, but it also
[3488.52 --> 3497.90]  doesn't make it clear like A to B to C what is going on, what's being done. And for most server installs,
[3497.90 --> 3500.08]  they don't have to be very complicated. Yeah.
[3500.08 --> 3505.42]  And if it doesn't have to be very complicated and there's not a lot of complexity to manage,
[3505.72 --> 3510.70]  if you bring in a larger abstraction layer, which is supposed to hide a lot of complexity and
[3510.70 --> 3518.42]  make managing very complex things possible, which I think is, is a fair, fair thing to say about
[3518.42 --> 3524.32]  Kubernetes. It seems to make it possible to manage very, very complex things. If you bring that into a
[3524.32 --> 3529.08]  fairly, already fairly simple thing, I think you're shooting yourself in the foot.
[3529.08 --> 3536.22]  But, but it's, it also depends on what tools are you comfortable with? Like you've spent years and
[3536.22 --> 3539.60]  years deeply immersed in, in ops and like.
[3539.60 --> 3541.82]  Tried decades, but yes, I agree.
[3543.42 --> 3543.94]  Yeah.
[3544.46 --> 3551.84]  I've spent much more time building the actual applications. I spent a fair bit of time on servers
[3551.84 --> 3559.68]  and operations, but not nearly the majority of my time because I care much more about,
[3559.98 --> 3567.26]  about the building of the thing. And I consider the operations and a part of what I do. I don't
[3567.26 --> 3573.16]  want to hand off a container particularly to, to operations and just guess how it's going to be run.
[3573.16 --> 3594.58]  I see there's a lot of, I don't want to call it full stack, maybe end to end stack. Like I want to care about the whole and I have no idea what's going on in half of the whole. If I, if I bring in a cool like tool like Kubernetes, I definitely would use it for, and I would learn it.
[3594.58 --> 3616.22]  If I saw that I definitely had the need, if I was going to run hundreds and hundreds of instances or, or scale across continents. Yeah. It probably makes sense to bring in something that lets me take that, that overview, that like 10,000 miles view of the world.
[3616.22 --> 3630.54]  And then like, Oh yeah, we have decent performance in Asia. Oh, we're dropping performance in Antarctica. Like, but that's typically not where I operate. And it's typically not what I go for first.
[3630.54 --> 3659.98]  And on that thought, thank you, Lars, very much for joining me. This was a pleasure. I do realize that we have so much more to talk about. Dev and Ops talking finally. I think for decades, we tried to do that and it's finally happening. We have respect for each other. We know that each context is difficult, challenging, but worth exploring. And I don't think we should be just shoving code across the fence. Like, here you go.
[3659.98 --> 3686.64]  You run this, figure out what to do with it. I think it's nicer when we agree on what the abstractions should be. Everybody benefits. And when things go wrong, because they will go wrong, people know what to do. And it's not a reactive approach. It's like a planned, you know, we kind of know what, what we need to do. So I'm really excited about that world. Thank you very much for joining me. This was a pleasure, Lars. I look forward to seeing you next time and talking to you next time, whenever that may be. Hopefully soon.
[3686.98 --> 3688.86]  Happy to come back. Thanks for having me.
[3689.98 --> 3719.96]  Happy to come back.
[3720.32 --> 3725.12]  Come hang with us on Slack. They're knowing posters. Everyone is welcome.
[3725.72 --> 3730.00]  Huge thanks again to our partners. Fastly, LaunchDarkly and Minout.
[3730.34 --> 3735.04]  Also, thanks to Breakmaster Cylinder for making all our awesome beats.
[3735.50 --> 3737.76]  That's it for this week. See you next week.
[3737.76 --> 3767.74]  Thank you.
[3767.76 --> 3797.74]  Thank you.
