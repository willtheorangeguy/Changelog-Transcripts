[0.00 → 21.90] welcome to changelog and friends our weekly talk show about mostly local a big thank you to our
[21.90 → 28.66] friends and partners over at fly.io the home of changelog.com and the cloud for developers who
[28.66 → 36.02] ship that's you that's us check them out at fly.io okay lets local first
[36.02 → 45.76] what's up friends I'm here with Kurt Mickey co-founder and CEO of fly as you know we love fly
[45.76 → 51.82] that is the home of changelog.com but Kurt I want to know how you explain fly to developers do you
[51.82 → 57.26] tell them a story first how do you do it i kind of change how I explain it based on almost like the
[57.26 → 62.74] generation of developer I'm talking to so like for me, I built and shipped apps on Heroku which is
[62.74 → 67.18] you've never used Heroku is roughly like building and shipping an app on oversell today it's just it's
[67.18 → 72.80] 2024 instead of 2008 or whatever and what frustrated me about doing that was I didn't I got stuck you
[72.80 → 78.02] can build and ship a rails' app with a Postgres on Heroku the same way you can build and ship a next
[78.02 → 83.08] JS app on oversell but as soon as you want to do something interesting like as soon as you want to
[83.08 → 87.60] at the time I think one of the things I ran into is like I wanted to add what used to be like kind
[87.60 → 92.70] of the basis for elastic search I want to do full text search in my applications you kind of hit this
[92.70 → 96.86] wall with something like Heroku where you can't really do that I think lately we've seen it with
[96.86 → 102.66] like people wanting to add LLM's kind of inference stuff to their applications on oversell or Heroku or
[102.66 → 107.50] Cloudflare or whoever these days they've they've started like releasing abstractions that sort of let
[107.50 → 113.10] you do this but I can't just run the model I'd run locally on these black box platforms that are
[113.10 → 118.32] very specialized for the people my age it's always like oh Heroku was great but I outgrew it and one
[118.32 → 122.14] of the things that I felt like I should be able to do when I was using Heroku was like run my app
[122.14 → 127.40] close to people in Tokyo for users that were in Tokyo and that was never possible for modern generation
[127.40 → 132.88] devs it's its a lot more oversell based it's a lot like oversell is great right up until you hit one
[132.88 → 136.96] of their hard line boundaries, and then you're kind of stuck there's the other one we've had someone
[136.96 → 141.06] within the company I can't remember the name of this game, but the tagline was like five minutes
[141.06 → 145.48] to start forever to master its sort of how we're pitching fly is like you can get an app going in
[145.48 → 149.30] five minutes but there's so much depth to the platform that you're never going to run out of
[149.30 → 157.26] things you can do with it so unlike AWS or Heroku or oversell which are all great platforms the cool
[157.26 → 163.36] thing we love here at changelog most about fly is that no matter what we want to do on the platform
[163.36 → 170.98] we have primitives we have abilities and we as developers can charge our own mission on fly it is
[170.98 → 177.02] a no limits platform built for developers, and we think you should try it out go to fly.io to learn
[177.02 → 182.78] more launch your app in five minutes too easy once again fly.io
[182.78 → 199.26] we are here with a couple of local first aficionados and frequent changelog guests I think for both of
[199.26 → 205.92] you this is your fourth appearance on our pod so welcome back we have Johannes shackling and jams
[205.92 → 212.20] long what's up guys not much greater to be here I'm super excited to be back talking more about local first
[212.20 → 215.94] what was my third time I know I came and talked about actual and then I talked about
[215.94 → 220.44] something else I didn't know this was my fourth. You're leading me on the spot. Sorry about that.
[220.60 → 226.60] So for a time for a little while we produced and shipped the React podcast here on this network
[226.60 → 232.30] so you were on changelog interviews 242 the burden of open source, and then you were on the React podcast
[232.30 → 238.16] talking about react and electron which we published and then actually, actually open source
[238.16 → 241.82] talking about actual so with us with Adam and i twice but on the network three times yeah
[241.82 → 249.34] got it technically with me several times nice and you just once jarred fair good fact checks guys
[249.34 → 253.66] cool fact checking you on here Johannes do you feel good about three does that sound right to you
[253.66 → 261.06] um yeah sounds about right I guess one or two maybe about graph cool prima yep another one about
[261.06 → 267.42] something afterwards I don't know about using the effect library are you still an effect fan oh yeah
[267.42 → 273.80] that was on JS jabber though I think that's JS party which is a far superior JavaScript podcast no just
[273.80 → 281.76] we're just doing conflict resolution right here live that's right all of our podcasts are resolved in a
[281.76 → 286.90] CRT so I just use that in a way which probably showed that I don't know exactly how it works
[286.90 → 293.26] but let's move on swiftly we want to talk about local first because we have of course Johannes the
[293.26 → 299.00] purveyor of local first dot FM and jams you've been doing things locally in the browser for a long
[299.00 → 305.88] time pushing the limits I would say both of you and jams recently posted a post which is what you do
[305.88 → 311.66] now you don't tweet any more you post in which you said that after a long time of trying it doing it
[311.66 → 318.60] etc you don't think it's the future for all kinds of apps which there's a question about is that the
[318.60 → 323.84] case now it's a blog post in progress whenever I see somebody with a blog post in progress or
[323.84 → 328.56] it should be a blog, but it isn't yet, and they're talking I think let's have an actual conversation
[328.56 → 334.78] because this will help all of us think through things and iron out our thoughts, and so I want
[334.78 → 340.36] to start there but before even that I think the definition of local first is also ambiguous or
[340.36 → 345.04] perhaps up for debate so maybe we can get on the same page about what a local first web app is
[345.04 → 350.28] and is even the word web supposed to be in there I think it is but Johannes maybe start there we'll
[350.28 → 356.94] see if all four of us agree about what local first really is yeah I would say that uh web is not a
[356.94 → 365.48] necessity of local first I think local first is um has kind of so far gone through two rounds of like a
[365.48 → 373.64] definition attempt the first one was through the ink and switch essay I think in 2019 or so by
[373.64 → 381.30] martin Lehman pH and so on and that was outlined in a set of seven ideals that define what local
[381.30 → 388.08] first software is and that's along the lines of like no spinners the network being optional etc none of
[388.08 → 395.78] that is really about any platform I think at the end of the day software runs wherever we use a certain
[395.78 → 402.22] device and at some point it might run wherever so the web is just a very common platform and then the
[402.22 → 408.02] second attempt to define what local first software it was last year or technically I guess this year
[408.02 → 414.02] from martin Lehman at the first local first conference where I think he tried to simplify it a
[414.02 → 420.46] little bit more what local first software is where I think he said it along the lines that a computer
[420.46 → 427.18] that you're not aware of even existing should not prevent your software from running and I would say
[427.18 → 433.48] that this is we can take it apart uh what that definition means but I think it's kind of intuitive
[433.48 → 440.48] and given that a lot of software runs in the browser I think that's where particularly our mind goes
[440.48 → 448.16] and I would say it's particularly hard to build local first grade software in the browser it's somewhat
[448.16 → 454.82] possible sometimes not fully practical and I think we'll go deep into that, but local first has
[454.82 → 462.28] and has nothing inherently is not inherently bound to the web jams anything to add or subtract
[462.28 → 466.88] agree or disagree with what he's saying there no I think that all sounds good I think the web is
[466.88 → 470.82] definitely kind of anti-local first in some ways, and so we're the community it feels like we're kind
[470.82 → 474.92] of pushing about that's why we have to push the boundaries because it has a lot of boundaries around
[474.92 → 481.58] doing things locally because I mean honestly it began as this uh you know client server model which is a
[481.58 → 485.82] really powerful model and so it that we're trying to figure out how to kind of pull it back from that
[485.82 → 491.66] but no totally agree I think it's I think this kind of terms are helpful for conversations because
[491.66 → 497.16] it's a very simplistic term it's like a code name almost, but these things always naturally are actually
[497.16 → 503.62] pretty ambiguous and uh difficult to nail down specifically and I think it's worthwhile to have
[503.62 → 508.98] conversations to actually define the nuances a little bit more, and they can also be under the umbrella of
[508.98 → 514.70] local first I think I don't think we need to you know mince words too much um, but it is worthwhile
[514.70 → 519.82] to kind of like take a step back and actually talk about what that means exactly to two different people
[519.82 → 527.06] right and I might also add that I think local first is often seen as sort of this binary thing
[527.06 → 533.44] but I think that's at least as of today not too helpful of a perspective I'd rather encourage people
[533.44 → 540.68] to think about local first as like an aspiration and a spectrum that you can take many steps in that direction
[540.68 → 548.40] would you have reached all the seven ideals of the local first manifesto or would you fully already
[548.40 → 553.98] nail the definition of like if another computer stops working does your software stop working
[553.98 → 561.50] probably not, but you're already well on your way there software like linear etc is not local first by definition
[561.50 → 566.80] but it's way further along the lines there compared to other software and I think that's what it's all
[566.80 → 574.00] about like being aspiring to building better software and I think local first is a way how you can think
[574.00 → 580.74] about getting there when you have the question of what you have to follow up with why so we know what it
[580.74 → 587.62] is now for we all agree why go local first why aspire to the spectrum why aspire to the binary
[587.62 → 596.34] why aspire at all towards this local first direction I can start with why i so i sort of naturally fell
[596.34 → 602.32] into this around 2017 which was around the time the I think the essay came out like a little bit later
[602.32 → 606.44] after I had started going down this path and it sort of crystallized a lot for me but yeah when I was
[606.44 → 610.84] building actual which is a personal finance app that I built and uh tried to sell for a couple
[610.84 → 615.06] years it actually met most of the principles of the original one where it's actually completely local
[615.06 → 620.20] first uh literally all of your data is local um and the server is a super dumb server and in that
[620.20 → 624.60] architecture you can even like end to end encrypt which felt appealing I think it was more appealing
[624.60 → 630.38] idealistically like or like ideologically appealing because it was just like hey like it's your personal
[630.38 → 636.82] finance data it sounds cool to encrypt it I think a lot of my evolution from this is like nobody really
[636.82 → 641.60] cared that much about that, and so I'm sort of reeling back from some of the like deep research I did back
[641.60 → 647.28] then but um anyway the main reason I did it was uh for performance and just like simplicity like it
[647.28 → 653.14] just felt really cool to just like to write SQL queries and have this SQL database totally available to your
[653.14 → 659.14] entire local machine what rather than like an http request that came back with like most of the fields
[659.14 → 663.46] but some of them were missing because they needed to join some table that was on a totally different
[663.46 → 667.62] sharded database and in a separate place and so then you have to do a follow-up http request and
[667.62 → 672.68] GraphQL sort of follows some of this, but it's GraphQL just feels like super overly complex and
[672.68 → 676.60] when you need to do mutations with GraphQL it's just like really locks you into this like specific
[676.60 → 680.44] format, and then you're always like waiting on loading spinners and things like that, and it's
[680.44 → 686.12] just like this super compelling simplicity of like hey SQL query get my data back within like
[686.12 → 691.12] five milliseconds render it and then like subscribe to that data, and it's all completely local and you
[691.12 → 695.86] don't need to like a web socket to a remote server that could die like die anytime now so that that was
[695.86 → 702.92] that was my main motivation and I think that might hold for your reasons Johannes is that right
[702.92 → 709.38] yeah i I think I want to i very much subscribe to what you've already said um I think there's two
[709.38 → 715.42] major perspectives for me one is the perspective from me as a builder who wants to build a product
[715.42 → 722.20] for end users so what do you want the experience the end user experience to be and obviously performance
[722.20 → 728.48] is one that very quickly comes to mind what I want the app to feel like it should be a great
[728.48 → 734.78] user experience and I think local first that's a really high bar this is where software like linear
[734.78 → 741.96] etc is so that makes it so clear that this is just like a high quality app and local first helps you get
[741.96 → 747.50] there but the other one is from a developer experience perspective and not just even from a developer
[747.50 → 753.66] experience perspective but also like you've mentioned the word simplicity I think this is
[753.66 → 758.86] what typically ruins both the user experience and the developer experience that we're just drowning in
[758.86 → 767.32] complexity and local first for me was sort of like a promise for like eventually we can do much better
[767.32 → 773.76] we can build more ambitious apps in a way that is actually simpler to build for the developer
[773.76 → 780.48] and this is a promise that I still strongly believe in we're not quite there, yet we've already made a
[780.48 → 787.12] lot of progress in that direction, but that is what is for me all about is like that like we're drowning
[787.12 → 793.38] in complexity typically the more ambitious of an app we are building and local first gives me hope
[793.38 → 801.24] and gives me a promise that we can do a lot better that we gain simplicity for some category of apps
[801.24 → 806.40] and this won't hold for all category of apps this is what where i also strongly agree with your
[806.40 → 813.88] point that you've shared local first is not the panacea for all apps but for some apps it can be a much
[813.88 → 821.44] better trade-off and this is what's got me so excited about it what category of apps do you think
[821.44 → 828.28] that applies to because when it comes to simplicity I think the mental model for developer
[828.28 → 835.98] that I operate a server and a client makes a request to my server and I do whatever I'm going
[835.98 → 843.04] to do and then I respond and the client renders it to me like it's hard to get more simplistic than
[843.04 → 850.24] that, but that admittedly is a very basic application however there are some applications where it's like
[850.24 → 855.76] you're reading a newspaper does it need to be local first because the actual newspaper content is not in
[855.76 → 861.32] the device it's on the server and so what good is it without the server so I'm sure there's like
[861.32 → 866.46] hit I mean you keep mentioning linear it's probably like hit out of the ballpark use cases there's
[866.46 → 870.12] probably like pretty good use cases and there's probably like maybe what jams has been finding
[870.12 → 875.78] is like well is it the future for all apps he doesn't think so in your definition
[875.78 → 881.78] Johanna, so your thoughts like what are like the greatest local first apps and then what are some good
[881.78 → 886.78] ones and then maybe we'll get to ones where it's like yeah doesn't really make sense yeah so I don't
[886.78 → 893.44] disagree with jams that it's like it is not the future for all apps I do think it could be a better
[893.44 → 900.94] future for some apps and so that how I would categorize this as a starting point at least is like
[900.94 → 909.44] anything that really centres around my data as a user or as a small group of users so for example a
[909.44 → 916.42] note-taking app I think that's a very prototypical example for where local first makes a lot of sense
[916.42 → 921.40] where it's simple to build and where it also from an end user perspective makes so much sense because
[921.40 → 929.98] all the data that's let's ever created in this app I probably created I've written down by myself at
[929.98 → 937.80] some point or dictated etc all the data is coming from me very opposed to like a newspaper where someone
[937.80 → 944.16] else has written everything I'll never going to read all of it so that I think is an it's an anti-use case
[944.16 → 951.64] for a local first anything that feels like a social network or newspaper etc anything where an individual
[951.64 → 958.72] user small group of users have created some data I think that is a very good use case this is where
[958.72 → 964.46] you have like if you think about the data as a graph you have liked it's a very highly connected dense
[964.46 → 970.72] graph, and it's very easy to in terms of the quantity of the data that it actually fits on the
[970.72 → 978.46] devices that we're using, so this is like a rough idea of what makes a good fit for a local first app
[978.46 → 985.90] but then it is also like scales a bit beyond that so for example if you want to not just work on some
[985.90 → 992.96] data by yourself but maybe in the realm of like a smaller group let's say your family or let's say
[992.96 → 999.74] your small team your medium team and the larger it gets, the less of a good fit it possibly is for
[999.74 → 1005.30] local first since trust is another matter like when you're you're probably trusting your all the members
[1005.30 → 1011.02] in your family you might also trust all the members in a small team once you're like a 5 000 person
[1011.02 → 1016.70] company you have like legal obligations etc that you need to have like strict boundaries in place and
[1016.70 → 1021.82] someone needs to be able to remotely delete all the data this is where it gets a little bit in
[1021.82 → 1029.22] tension but the more it is all about like a user's data or a small group of users I think this is
[1029.22 → 1035.74] where it's a great starting point so jams you said in your post that you think it's cool for some
[1035.74 → 1041.10] very specific apps like obsidian you use obsidian as an example of course this is an app that's
[1041.10 → 1046.14] operating on your local markdown files and then also building from there and doing additional stuff
[1046.14 → 1053.10] you built a personal finance app in the browser right or with web tech and that sounds like something
[1053.10 → 1059.18] Johannes is very much defining, and you gave it a shot so curious your thoughts on that being applicable
[1059.18 → 1065.62] in that circumstance or what you found with regard to what sounds like a good use case for a local
[1065.62 → 1071.14] first according to Johannes and makes sense to me yeah I think I mean it's just hard because
[1071.14 → 1077.26] that kind of reasoning still resonates with me, it's super amazing to just like to have this three
[1077.26 → 1082.80] megabyte SQLite file and for me personally like I have maybe eight years of transactions that's maybe
[1082.80 → 1088.56] scaled up to five megabytes like it's not ever going to be remotely a problem to have this all local
[1088.56 → 1093.18] and to me also it was really compelling at the very beginning so I actually started uh with web tech but
[1093.18 → 1097.44] it was wrapped with electron so it was a fully native app so I didn't have to be actually
[1097.44 → 1103.08] in the guardrails of the browser so it literally used native SQLite there was a SQLite file locally
[1103.08 → 1107.02] on my computer and what's so cool about that is I could just like fire it up from the terminal and
[1107.02 → 1112.12] just like run some select queries the problem there 's's a lot of things that kind of have
[1112.12 → 1116.76] tripped away at that for me that have made me kind of take a step back to kind of rethink some of it
[1116.76 → 1122.92] even for some of these apps that do seem at the up front um better one is like um the web is the
[1122.92 → 1128.50] biggest is the distribution king you cannot get away from the web like i it was very clear early
[1128.50 → 1135.06] on that like downloading this huge 300 I wasn't 300 I don't know it was like 75 megabyte electron
[1135.06 → 1139.20] app and everybody was like made fun of you for building this like web thing that was so new I was
[1139.20 → 1143.56] just like tired of having to deal with all of that stuff and also the um notarization and like
[1143.56 → 1147.74] actually deploying things through the native stuff it's just like it is the worst thing I've
[1147.74 → 1152.54] ever experienced and going I also built like React Native apps too which is I like biggest regret
[1152.54 → 1157.72] of actual was just like overextending myself but for every single thing that you distribute it to you
[1157.72 → 1161.22] have to like notarize it you have to pay money to actually distribute it through it, you have to like
[1161.22 → 1166.88] get a certificate for windows I had to get this other like weird section certificate chain so it was it
[1166.88 → 1172.22] was it was a lot so I deployed to the web and I could make a bug fix and deploy it in like three
[1172.22 → 1177.64] seconds it was amazing the problem there is like I lose the local SQLite file capability right so uh
[1177.64 → 1182.54] they do have this new technology so I built up stead SQL which was like this uh SQLite abstraction over
[1182.54 → 1188.36] index CB i just I still think it was like super cool now they have this like uh offs capability with
[1188.36 → 1194.16] like the file system access API so you can do real files, but they're sandboxed within the browser
[1194.16 → 1199.32] I don't know i they might exist somewhere locally but I'm pretty sure you're not really I don't think
[1199.32 → 1203.32] they do I think that they're compressed in a weird way that you can't actually just have a local SQLite
[1203.32 → 1208.80] file they give you basically like a virtual private file system and so you lose this ability to just
[1208.80 → 1213.18] like hey have a local SQLite file so you have to compile web assembly down and lose some performance i
[1213.18 → 1217.86] don't know exactly what that overhead is, but it's slower and it is Johannes you probably have way more
[1217.86 → 1222.20] experience because you've done a lot more of this like more recently so I'm curious what that perf is
[1222.20 → 1225.94] we can talk about that in just a second, but it is a little there's going to be a little bit of overhead
[1225.94 → 1232.10] right there like if it's uh c running I can fine tune it i can tweak it but i I mean web
[1232.10 → 1236.62] always blows me away like maybe there's maybe it actually matches the native SP now um but uh there's
[1236.62 → 1243.76] also just the fact that you uh your data is still sandboxed in this thing right and so that was one
[1243.76 → 1248.40] thing is that I lose the ability to just like locally query stuff and so now if I want to do that
[1248.40 → 1253.52] well now I have to like if I wanted like let's say that I had a script right that like I've had this
[1253.52 → 1257.24] idea that was kind of this weird idea where I think I saw this person on hacker news a couple
[1257.24 → 1262.96] weeks ago he had this printer that every day would uh like print out something and I love that idea and
[1262.96 → 1266.28] I'm actually going to do that I'm going to have this printer that prints out things and one of those
[1266.28 → 1269.88] things is going to be like my latest transactions things like how much have we spent on food and then
[1269.88 → 1274.08] I can go up and like print that on my refrigerator and my whole family can see like my wife can see like
[1274.08 → 1280.58] updates to our budget to do that to have a service running on my machine now has to it's just really
[1280.58 → 1284.84] awkward right it has to like I guess it has to become a client in this whole distributed system
[1284.84 → 1291.32] and so it has to download the entire SQL file the entire data and then download the whole app to
[1291.32 → 1296.80] interface with it and then like to run those queries whereas if it was just an http API I mean just like
[1296.80 → 1302.56] you said jarred this is incredibly simple you just make a request to the http API so it scales complexity
[1302.56 → 1308.18] wise across use cases that I think are more interesting, and so I think that there's like
[1308.18 → 1312.50] there's something that I love to talk about later in this podcast about like what I think could be
[1312.50 → 1317.50] the next step for some of these kinds of things but I do still think that like for like note-taking
[1317.50 → 1323.22] things and things like that it does still feel like I use bear which all uses like a local SQL
[1323.22 → 1328.42] database as far as I now and then it uses like the iCloud syncing and I love it because it's so fast
[1328.42 → 1333.52] like I can just like pull it up on my phone and I know that it will come up instantly because all the
[1333.52 → 1337.78] files are there so I think there are still used cases there, but there's still a case where like well
[1337.78 → 1342.00] then I can like I guess it feels nice there because I can just sync my files to my server and then I can
[1342.00 → 1348.16] build a little http thing like around it, but it just feels like this like complexity that I kept
[1348.16 → 1353.98] having to hit for like oh there's this like thing that everybody else is used to doing and I can't do
[1353.98 → 1360.70] that now because I've built this other thing that has good trade-offs but I'm I think that there might
[1360.70 → 1367.02] be architectures that have similar benefits without losing some of that kind of weirdness and also my final
[1367.02 → 1371.02] point I'll make is that like those complexity things and like there are these libraries now
[1371.02 → 1376.58] Johannes I need to look more at yours but like I'm scared to build on top of something if especially is
[1376.58 → 1382.14] it forces me to use their own APIs like their own database abstraction I like the ones that do let me
[1382.14 → 1389.54] use raw SQL, but even those are like this is a fundamental abstraction in your stack right if you
[1389.54 → 1395.18] are a startup that blows up, and you get stuck with that, and it turns out to not scale or be bad or that
[1395.18 → 1400.98] the people making that burn out and or like go away that is a hard place to be in um so we're
[1400.98 → 1404.92] going to have to be really like this is just like a chicken and the egg type thing where it's
[1404.92 → 1409.48] like if you want local first to be perfect and build these things you're going to have to work
[1409.48 → 1414.36] really, really hard and long to make this like a robust foundation so that's my initial number of
[1414.36 → 1419.18] thoughts happy to yeah so in your experience building actual are you saying that you kept hitting
[1419.18 → 1426.32] these walls, or you would hit the walls if you had to scale on and network and add clients or add
[1426.32 → 1432.66] collaboration so to speak this local first direction took you in places that locked you in and couldn't
[1432.66 → 1439.40] let you scale or do things differently I suppose I'm not finding the right words but essentially it
[1439.40 → 1444.84] locked you into a place or choices, and you couldn't get around them basically that that was one thing that
[1444.84 → 1449.60] was hard and like some of that is because I built it myself and so if I were was able to use if there
[1449.60 → 1454.02] is like amazing library like the one that Johannes has built is it live store is that the name of it
[1454.02 → 1457.92] there's a couple of them out there yeah I need to check that out like it would definitely would have
[1457.92 → 1463.14] helped me a lot if I had one already that was there that solves some of these problems for me but I think
[1463.14 → 1466.76] some of this is a fundamental piece of the architecture where like people just wanted to build a
[1466.76 → 1472.74] little client around it like themselves and access actuals API I was like hey okay we don't have an API
[1472.74 → 1477.68] I ended up building one, and you know how it worked it was the entire app which downloaded the entire
[1477.68 → 1484.24] data first and so to boot up the API the first time you run it takes you seconds like 10 seconds
[1484.24 → 1489.38] so very, very slow and not not very tenable and the other thing that I was going to say
[1489.38 → 1496.20] is uh things like protected data so if people wanted to like to have these like roles and authorization
[1496.20 → 1500.22] I think that's something that I think that that part I think is not fundamental I think that's
[1500.22 → 1504.58] solvable, but it is hard like if you wanted to say like this user it can like input this transaction
[1504.58 → 1508.92] and I want to hide it from my spouse because it's like for Christmas this kind of things just got
[1508.92 → 1513.28] really tricky and just these weird things were like okay you're logged out, and you stopped paying for the
[1513.28 → 1518.72] product, but you still have it all locally and so people could like keep using it, and it's just like
[1518.72 → 1522.72] these weird things where like you log out, and you log back in as a different user but the other local
[1522.72 → 1528.34] data is still there and like it's just like an odd to me, I was like I want to be a startup
[1528.34 → 1534.14] that focuses on the problem like the solving the actual and i I kept having to be dragged into
[1534.14 → 1540.44] this like weird mindset of like how do I deal with this like crazy weird mind-bending situation
[1540.44 → 1545.50] that local first so i I think that is the benefit of some of why the community has moved towards
[1545.50 → 1550.36] this newer model of local first where it's like a really heavy kind of cache where it's like
[1550.36 → 1554.08] it still is a little bit more dependent on the server, and it's not completely local first
[1554.08 → 1558.66] but it's it adheres to the principles where you query your data locally, but it's not as
[1558.66 → 1563.24] like I got a new name for everybody let's stop calling it local first let's call it mostly local
[1563.24 → 1570.56] okay mostly local you're swimming upstream there I think we have critical mass calling it local first
[1570.56 → 1577.04] at this point okay friends I'm a good friend of mine Akthar Swithin from timescale they are positioning
[1577.04 → 1584.84] Postgres for everything from IOT sensors AI dev tools crypto and finance apps so after I helped
[1584.84 → 1591.14] me understand why timescale feels Postgres is most well positioned to be the database for AI applications
[1591.14 → 1596.98] it's the most popular database according to the stack overflow developer survey and Postgres one of
[1596.98 → 1601.92] the distinguishing characteristics is that it's extensible and so you can extend it for use cases
[1601.92 → 1607.56] beyond just relational and transactional data for use cases like time series and analytics that's
[1607.56 → 1612.26] kind of where timescale the company started as well as now more recently vector search and vector storage
[1612.26 → 1618.38] which are super impactful for applications like rag recommendation systems and even AI agents which
[1618.38 → 1623.30] we're seeing you know more and more of those things today yeah Postgres is super powerful it's well
[1623.30 → 1629.14] loved by developers I feel like more devs because they know it is can enable more developers to become
[1629.14 → 1636.88] AI developers AI engineers and build AI apps from our side we think Postgres is really the no-brainer
[1636.88 → 1641.40] choice you don't have to manage a different database you don't have to deal with data synchronization
[1641.40 → 1646.74] and data isolation because you have like three different systems and three different sources of truth and
[1646.74 → 1652.12] one area where we've done work in is around the performance and scalability so we've built an extension
[1652.12 → 1657.40] called pg vector scale that enhances the performance and scalability of Postgres so that you can use it
[1657.40 → 1663.16] with confidence for large-scale AI applications like rag and agents and such and then also another
[1663.16 → 1667.66] area is coming back to something that you said enabling more and more developers to make the jump
[1667.66 → 1673.08] into building AI applications and become AI engineers using the expertise that they already have and so
[1673.08 → 1678.96] that's where we built the PGA extension that brings alms to Postgres to enable things like LLM reasoning
[1678.96 → 1683.84] on your Postgres data as well as embedding creation and for all those reasons I think you know when you're
[1683.84 → 1689.22] building an AI application you don't have to use something new you can just use Postgres well friends learn how
[1689.22 → 1697.00] timescale is making Postgres powerful over 3 million timescale databases power IOT sensors AI dev tools crypto
[1697.00 → 1703.38] and finance applications, and they do it all on Postgres timescale uses Postgres for everything, and now you can
[1703.38 → 1712.34] learn more at timescale.com again timescale.com and by our friends at eight sleep I love my eight sleep
[1712.34 → 1719.60] check them out eight sleep.com I've never slept better, and you know I love biohacking I love sleep science
[1719.60 → 1727.48] and this is all about sleep science mixed with AI to keep you at your best while you sleep this technology
[1727.48 → 1732.40] is pushing the boundaries of what's possible in our bedrooms let me tell you about eight sleep and their
[1732.40 → 1740.10] cutting edge pod for ultra so what exactly is the pod imagine a high-tech mattress cover that you can
[1740.10 → 1748.32] easily add to any bed, but this isn't just any cover it's packed with sensors heating and cooling elements
[1748.32 → 1754.66] and it's all controlled by sophisticated AI algorithms it's like having a sleep lab a smart
[1754.66 → 1761.22] thermostat and a personal sleep coach all rolled into one single device and the pod uses a network of
[1761.22 → 1768.26] sensors to track a wide array of biometrics while you sleep it tracks sleep stages heart rate variability
[1768.26 → 1774.92] respiratory rate temperature and more and the really cool part is this it does all this without you
[1774.92 → 1781.46] having to wear any devices the accuracy of this thing rivals what you would get in a professional sleep lab
[1781.46 → 1787.06] now let me tell you about my personal favourite thing autopilot recap every day my eight sleep tells me
[1787.06 → 1792.36] what my autopilot did for me to help you sleep better at night here's what it said last night
[1792.36 → 1800.38] autopilot made adjustments to boost your REM sleep by 62 percent wow 62 percent that means that it updated
[1800.38 → 1807.78] and changed my temperature to cool to warm and helped me fine-tune exactly where I wanted to be with
[1807.78 → 1814.86] precision temperature control to get to that maximum REM sleep and sleep is the most important function we do
[1814.86 → 1819.38] every single day as you can probably tell I'm a massive fan of my eight sleep but I think you should
[1819.38 → 1825.46] get one so go to eightsleep.com slash changelog and right now they have an awesome deal for blind Friday
[1825.46 → 1831.86] going from November 11th through December 14th the discount code changelog will get you up to
[1831.86 → 1839.76] six hundred dollars off the pod for ultra when you bundle it again the code to use is changelog and that's
[1839.76 → 1846.36] from November 11th through December 14th once again that's eightsleep.com slash changelog I know
[1846.36 → 1851.50] you'll love it I sleep on this thing every night and I absolutely love if it's a game changer, and it's
[1851.50 → 1855.82] going to change your game once again eightsleep.com slash changelog
[1855.82 → 1865.24] it seems like the difference between jams and Johannes is like jams is trying to build an app
[1865.24 → 1872.26] for production and Johannes loves building dev tools and like things to enable developers and so
[1872.26 → 1877.68] you're kind of trying I mean almost like jams would be your eventual customer or user because
[1877.68 → 1882.46] like he's talking about this live store and like you, you see this future, and you're trying to create it
[1882.46 → 1889.48] right well that that's not entirely true so the reason why live store came into existence in the
[1889.48 → 1896.42] first place is actually based on a predecessor project called riffle that I collaborated on with
[1896.42 → 1903.62] Jeffrey list and Nicholas Schaeffer uh Jeffrey uh did his PhD project at MIT about this last year
[1903.62 → 1911.54] and uh this was like a two-year collaboration where we've worked on riffle the entire idea around riffle
[1911.54 → 1917.96] was what if you can make your app state management not just like the back-end data management but actually
[1917.96 → 1924.68] your app state management what if you could also use a database for that and bringing reactivity etc
[1924.68 → 1931.96] right into your app so kind of going one step even further to what jams landed on to using
[1931.96 → 1937.42] SQLite I think typically on a separate thread where you asynchronously work with that synchronous state
[1937.42 → 1943.24] that SQL database we took it one step further, and we saw SQLite being so fast that you could actually
[1943.24 → 1949.58] run it in the main thread that's a different can of worms uh technically very, very interesting and
[1949.58 → 1957.04] was also quite a challenge to build but the reason why I got involved is actually I took a bit of a step
[1957.04 → 1962.74] back from prima where it was all building dev tools I wanted to get back into the shoes of building my
[1962.74 → 1968.96] own app again so that was actually in terms of the chicken and egg where live store is maybe the
[1968.96 → 1975.00] the egg but the chicken that was also needed was me working on my own app and that's called
[1975.00 → 1981.12] overtone so overtone I think we talked about that on a previous time is a new music app that I'm
[1981.12 → 1987.14] building sort of like a third party client for wherever your music lives so think about it like
[1987.14 → 1995.30] what's superhuman is to Gmail overtone is to Spotify or to your own music collection to YouTube music to
[1995.30 → 2002.44] Bandcamp etc and that was my primary driver to even want something like riffle and like that now
[2002.44 → 2009.14] LEDs to live store and I'm developing both live store and overtone and tandem overtone is still sorted
[2009.14 → 2015.22] of the most demanding use case that informs all design decisions around live store but I'm not doing
[2015.22 → 2023.12] this in a vacuum even though I am like with one foot in the dev tool building uh situation but with the
[2023.12 → 2029.04] other foot I'm firmly in the app developing situation but I think where I can now also
[2029.04 → 2037.70] subscribe to the point you were making I am less strict about like making harsh time-wise
[2037.70 → 2044.94] trade-offs in favour of shipping earlier I'm taking a more long-term minded approach and I'm making design
[2044.94 → 2050.78] decisions around the technologies and around the product that might cost me a couple of months maybe
[2050.78 → 2056.04] sometimes years in terms of actually shipping everything where I take a more long-term minded
[2056.04 → 2062.32] approach and your typical startup thinks about like how can we reduce uh the scope for initial
[2062.32 → 2067.56] MVP and just launch it and this is where I take a different trade-off gotcha okay that makes a lot of
[2067.56 → 2074.16] sense so effectively what we have is a different way a new way of building for the web which is the
[2074.16 → 2078.50] opposite way that most of us have been building for the web right so client we call it client server but we
[2078.50 → 2083.92] really are server oriented and the client does things and the server is the source of truth and
[2083.92 → 2089.16] all of that and that's a new and perhaps better way of doing it however there's a bunch of
[2089.16 → 2092.88] groundwork that has to be laid because you're basically pioneering and what jams maybe you have
[2092.88 → 2098.82] found as you pioneered through this on your own with actual is like there's lots of different
[2098.82 → 2105.80] gnarly nasty problems that have to be solved in order to do this stuff that us architecture astronauts
[2105.80 → 2109.76] don't really think about when we're just you know on podcasts talking about new paradigms in
[2109.76 → 2114.36] a different way is like well what happens when somebody cancels their account, and it's local
[2114.36 → 2118.84] first like that's you ran into that in reality, and you're like oh I have a whole new problem I have
[2118.84 → 2125.38] to solve whereas on a traditional web app like we've been there we've done that you can just look
[2125.38 → 2130.44] it up or whatever you have to do to be like oh here's what you do and those trade-offs for you jams
[2130.44 → 2137.46] today at least or over the last few years have been not worth it fair yes I think that's fair and
[2137.46 → 2144.94] I do think that there are I think I want to make sure that my points are my main concern is that some
[2144.94 → 2151.02] of my problems are just completely inherent like if you are assuming that you're going to acquire your
[2151.02 → 2155.28] data locally like first and if it's like not there it can fall back to the server even if that
[2155.28 → 2161.38] there are things inherent into this that i I don't think are completely solvable and I don't mean
[2161.38 → 2166.42] that that means that it's dead in the water it's a bad idea but that there are problems that I think
[2166.42 → 2172.82] I don't see mentioned or that I think people say we'll get there like we'll right we'll figure it out
[2172.82 → 2177.70] and it but to me, it's like it's an inherent part of it so it's less that like there's all these
[2177.70 → 2183.10] things that I think i I don't mean and I don't mean to like to put cold water on this at all I do think
[2183.10 → 2188.74] that like live store and other things can make this significantly easier and solve a lot of the
[2188.74 → 2193.52] hard problems and there will be many apps built on things like that but I think there is uh there
[2193.52 → 2198.30] are a couple like trade-offs here that are just needed to be kept in mind as well that might make
[2198.30 → 2204.66] it is hard for other people right newsflash it's not a silver bullet yeah and not only are there problems
[2204.66 → 2209.28] that haven't been solved yet, but you think that just like anything there are trade-offs and there are
[2209.28 → 2212.84] problems that you don't think will be solved the API one is one I hadn't really thought about
[2212.84 → 2217.08] Johannes was kind of shaking his head in the affirmative as you talked about it is that a
[2217.08 → 2223.32] solved problem Johannes like you have client first apps like how do we build a generic API for a
[2223.32 → 2228.92] client first app like actionable for instance is there is that a solved problem now um when you say
[2228.92 → 2236.10] how do we build an API I'd love to hear a clarification of that since one idea around local first apps is
[2236.10 → 2241.90] that you actually you should ask yourself do we still need an API it's all about the client-side
[2241.90 → 2246.92] experience at the end of the day or some other things that you need to build maybe you want to
[2246.92 → 2252.34] send an email if a certain thing happens etc, and you might want to do that on some server-side thing
[2252.34 → 2261.38] but one of the ideas of local first is trying to nudge you away from that very API centric way of
[2261.38 → 2266.10] thinking of an architecture if you're building let's say a calculator app that just happens to
[2266.10 → 2273.70] synchronize between your phone and your tablet than you could try to think about that as like a
[2273.70 → 2279.90] oh we're going to have an API here etc but if you just start out working on that as an in a single
[2279.90 → 2284.96] player experience it would never think about do we need an API of our calculator no we just built that
[2284.96 → 2290.64] thing client-side and now if you have that as a starting point, and you want to synchronize data
[2290.64 → 2296.36] between your different clients you don't necessarily need an API for that you just need a transfer
[2296.36 → 2302.32] mechanism between the clients and that's where rather where the local first idea comes from that
[2302.32 → 2308.82] being said you can still interact and integrate with APIs but I think with local first you rather
[2308.82 → 2314.74] think about how do you synchronize the data and less how do I request response with an API sure
[2314.74 → 2319.66] well we don't have to invent hypothetical API scenarios because jams your customers were like
[2319.66 → 2324.56] asking you for this right yes they're like I'm in my terminal and I want to just like to write this
[2324.56 → 2329.76] script that like dumps things out and to like to put it on my second monitor like I think maybe it was
[2329.76 → 2336.38] just like maybe this is i I can't paint too broad of a of a stroke here because I think maybe this
[2336.38 → 2341.66] this is one app that just would have benefited from like a a standard API because people
[2341.66 → 2346.18] wanted to query their data they wanted to like yeah like write scripts on the remote server to like
[2346.18 → 2350.50] set up their own notifications for when like a transaction came through that was like too much
[2350.50 → 2357.12] and so I like I know in this specific case it would have been nice to have an API so the way how I'm
[2357.12 → 2365.20] starting to think about scenarios like those is similar to how we're using git I think we're thinking less
[2365.20 → 2371.56] about git as an API endpoint that you can correspond with, but you're thinking about git as a semantic
[2371.56 → 2378.94] protocol that you use in a very specific environment in this case how you evolve your code repository
[2378.94 → 2386.96] in a semantic way and I think the same analogy could have also hold true for your scenario so
[2386.96 → 2392.32] obviously this would have taken quite a bit more effort to define and develop this and so on like
[2392.32 → 2399.48] and build SDKs for the various target platforms etc but I think from a mental model perspective
[2399.48 → 2406.42] there's nothing inherent that this needs to be an API I think the synchronization mechanism still holds
[2406.42 → 2413.22] true to this and this is where git is sort of like a very commonly used synchronization mechanism
[2413.22 → 2422.88] and I would like for apps to embrace the sort of more git less APIs mindset where often that can be more
[2422.88 → 2429.06] declarative instead of like APIs often being kind of like very hand wavy in an imperative way
[2429.06 → 2437.18] but yeah it is will take time to get things off the ground there and kudos to you again for just putting in so much
[2437.18 → 2444.38] effort and the pioneering work that you've done over the years and particularly also targeting the web I think the
[2444.38 → 2453.48] the web is both like a blessing and a curse it is a blessing that it can already do all of those things that it's possible
[2453.48 → 2459.54] with right now the ubiquitous distribution you're getting with the web etc, but it also lacks behind
[2459.54 → 2467.20] in terms of capabilities that we've already had for decades on more native platforms I'm very bullish on
[2467.20 → 2473.24] the web even catching up with those native capabilities just want to add a few points on what
[2473.24 → 2480.36] you've mentioned before in regard to file system support etc so you've mentioned offs as sort of like this
[2480.36 → 2488.08] origin private file system which I think by definition is sort of like non-accessible to the
[2488.08 → 2493.66] user I think the current way how it works for example in chrome is there is actually like some
[2493.66 → 2500.04] folder somewhere I guess under like application support or library somewhere on macOS or in
[2500.04 → 2504.52] different places where you can actually see the real files, but this might just be an implementation
[2504.52 → 2510.28] detail it's not meant to be access user accessible however also in chrome there is
[2510.28 → 2516.00] an I'm not sure whether it's even newer but there's a separate API with mostly the same API surface
[2516.00 → 2523.14] where it lets a user actually mount a real file or a real folder system from their actual hard drive
[2523.14 → 2531.22] into the web app, and you can read and write from it so with that you get like real files in your app
[2531.22 → 2538.40] and those files don't go away if something happens to the web app unless the web app decides to delete it
[2538.40 → 2545.46] but this way we're already taking another big step towards native capability apps at least in chrome
[2545.46 → 2550.00] for now I'm not sure what the current status with other platforms with other browsers
[2550.00 → 2555.70] but stuff like that gives me a lot of hope and the way if I'm now wearing my application developer
[2555.70 → 2563.20] hat for overtone what I'll probably do is like I love those capabilities and I'll embrace them for the
[2563.20 → 2568.50] given browsers so I'll probably say like hey if you want to use the web version and not the desktop
[2568.50 → 2574.94] version and if you want to have the most advanced experience then please use chrome use arc etc
[2574.94 → 2583.16] and if you use another browser then I'll diffuse the capabilities a little bit and hopefully in two
[2583.16 → 2591.12] years safari and other browsers have caught up so I'm more long-term minded on this and I don't see it
[2591.12 → 2595.92] like I don't look at a feature and say if I can't have it on all platforms I'm not having it at all
[2595.92 → 2602.98] I'm rather like opting into features progressively enhancement way step by step yeah and that's i I had
[2602.98 → 2607.08] forgotten that I think that I saw that was released and I think you have to like there's a notification
[2607.08 → 2610.86] that pops up for the user right, and then they just have to say allow exactly and that's great that
[2610.86 → 2616.42] I love that I think that moving towards this kind of models for apps that this works well is going
[2616.42 → 2620.52] to unlock a lot of like really, really cool stuff I think that that is a huge blocker that that was
[2620.52 → 2625.92] one of my biggest gripes and so the fact that that is starting to be solved is amazing I think
[2625.92 → 2632.44] overall the web is sort of like in this weird spot where the web has traditionally always been like a
[2632.44 → 2639.52] website distribution mechanism, but we all want like more and more app-like experiences on the web
[2639.52 → 2646.54] but there isn't really this binary way of like flicking on the app mode in the browser and
[2646.54 → 2653.66] everything by default is treated as a website and that makes for a worse experience even so that like
[2653.66 → 2660.48] safari takes some pretty strong steps in that direction if you don't visit a website for I think
[2660.48 → 2667.32] seven days or so it just like wipes all of your data which can be very counterintuitive and very much
[2667.32 → 2673.24] I think hampers the trust that you can put in web apps making it again sort of like the self
[2673.24 → 2680.02] perpetuating prophecy that oh it's just a website, and you can't have real apps and I guess the closest
[2680.02 → 2684.50] we have in that regard is like that you pin something to your doc bar that actually does
[2684.50 → 2692.00] change the defaults quite a bit so but yeah that's sort of with my web optimism hat on yeah I think some
[2692.00 → 2699.90] of my reaction and pulling back and evolving my ideas I think are founded in like good stuff some of it
[2699.90 → 2704.82] it's just that i just so burned like so many times on things that aren't a problem anymore that
[2704.82 → 2709.66] i I'm still kind of evolving my ideas but like I did one like so I built absurd SQL which like was
[2709.66 → 2715.16] SQLite on top of index CB before all of this other stuff was available and like there was definitely just
[2715.16 → 2721.58] like a time when I loaded up actual and like it was like okay log in or I think I was logged in but
[2721.58 → 2726.58] like none of my data was there and had to redownload it and like luckily the syncing stuff was nice
[2726.58 → 2730.84] because I'm mostly online so I didn't really lose any data but like it's just a terrible
[2730.84 → 2736.66] taste in my mouth to be like man the web just sucks uh because like it just blew away my
[2736.66 → 2740.94] it just like all my index CB was gone I guess like my disc was running low on space or something
[2740.94 → 2746.50] um now to be totally clear like you were saying Johannes I think this has all been mostly solved
[2746.50 → 2750.88] and is way better especially if we're starting to use real local files I think I don't think the
[2750.88 → 2756.84] offs even suffers from this, but yeah like that the web has a lot of trust issues I think with
[2756.84 → 2761.78] with people or people have a lot of trust issues with the web and yeah well it's an attack vector
[2761.78 → 2766.54] right it's networked obviously there's going to be lack of trust yeah also it's not in your control
[2766.54 → 2772.10] because the browser vendors control right browsers and so it sounds like to both of your perspectives
[2772.10 → 2778.92] push against what the browser wants to be for an application for example it doesn't seem to
[2778.92 → 2786.24] want to be local first it wants to be connected it wants to assume the thing it's rendering is
[2786.24 → 2791.66] connected or wants to be connected so you're kind of fighting upstream to this to the platform
[2791.66 → 2799.54] essentially that you're building against so you have to get better buy-in from browsers I wouldn't
[2799.54 → 2804.74] subscribe full-heartedly to that statement I think this is mostly like a matter of like the
[2804.74 → 2811.40] hive mindset that we've developed on the web over the last decades really and I think this is also
[2811.40 → 2819.18] where the local first mindset gives you a bit of like a bias counter to that point since you can
[2819.18 → 2825.90] actually build a lot of web things where you treat the network as being optional and I think if we put
[2825.90 → 2831.88] ourselves at least temporarily in the perspective of a mobile app developer I think this is where it's
[2831.88 → 2838.50] much more common that you want to build for an assumption that a developer that an app that
[2838.50 → 2844.66] a user doesn't have a connectivity all the time so and the way how you build the best experience in
[2844.66 → 2851.98] that regard is by really treating the connectivity as an optional thing that enhances the app, and you can
[2851.98 → 2858.16] very much build a web app in the same way, and we have a lot of ingredients that I think are highly
[2858.16 → 2865.64] underused in that regard so we have like service workers etc and by just forcing you and constraining
[2865.64 → 2872.14] yourself in the way how you build the app where you say like actually I separate every network
[2872.14 → 2878.50] interaction behind like some little surface that I have like under my control in my application
[2878.50 → 2885.68] and I want to make sure that the application may be initially installed similar to how you install an app
[2885.68 → 2891.66] from the from an app store and from there the app is functional from there the app is enhanced with
[2891.66 → 2899.24] network both enhanced in terms of data synchronization loading media etc and also loading new app updates
[2899.24 → 2906.48] is very feasible to do that on the web I think it's just not really helped by major frameworks something
[2906.48 → 2912.28] like next.js etc doesn't help you at all with that so I think it's mostly a mindset thing and the mindset
[2912.28 → 2918.44] thing is also holding back the technologies that are being developed and the lack of those technologies
[2918.44 → 2923.62] don't evolve the mindset so I think it's a bit of a chicken egg problem in terms of the mindset and we
[2923.62 → 2930.18] see the most development coming really rather in the mobile world where those assumptions are much more
[2930.18 → 2936.86] common. I'm fascinated by overtone then as a local first application because I mean it's playing my
[2936.86 → 2943.00] Spotify playlists for me right like how is overtone useful in a local only context like in an offline
[2943.00 → 2950.24] mode that would make it like a great local first app yeah so and I think that's actually also raising an
[2950.24 → 2956.74] interesting question in regard to local first that it's again not binary that is like either fully
[2956.74 → 2963.66] local first, or it is like embracing all the APIs overtone is a great example where I need a hybrid
[2963.66 → 2969.72] I do want to integrate with all like the different music services music sources that you
[2969.72 → 2976.94] might have I also want to support or I do support things like RSS etc and there's also a licensing
[2976.94 → 2984.16] question and a copyright question that comes into play here some data I am allowed to download some
[2984.16 → 2991.20] data I'm allowed to actually cache or store locally some other data I'm just allowed to stream on demand
[2991.20 → 2996.74] so for example if I'm playing something from Spotify I obviously can't can just stream that
[2996.74 → 3002.56] but I can't download it whereas if I've bought something on Bandcamp that is something that i
[3002.56 → 3008.32] actually do want to bring on my hard drive so it really depends on the kind of situation there
[3008.32 → 3015.92] but I'm building this in a way that gives you kind of the best of both worlds that keeps local
[3015.92 → 3022.58] whatever you can, and you're allowed to keep local and that's kind of de facto yours stuff that I'm
[3022.58 → 3029.78] buying from Bandcamp or from other places or stuff that I already have in my Dropbox etc there 's
[3029.78 → 3036.60] shouldn't be any reason why I shouldn't be able to use that on my hard drive or on my computer while
[3036.60 → 3043.20] I'm doing a road trip whereas there's other data where I'm or other kind of content where I might
[3043.20 → 3048.94] already have seen the metadata and that metadata should still be accessible to me for example that
[3048.94 → 3055.02] I see it like oh I like those things or have the playback history but I'm not temporarily until I have
[3055.02 → 3063.12] connectivity I am not allowed or I'm not able to stream that data so it's sort of like a hybrid mix
[3063.12 → 3070.26] but typically with a web app that is built in a more traditional way at best you have like some
[3070.26 → 3077.14] offline caching that breaks the moment you first click on an album, and then it doesn't have all
[3077.14 → 3083.72] the data you need, and you don't you just get a spinner right do you think that i so I'm curious on
[3083.72 → 3087.32] your thoughts on this because there are two more points that I wanted to bring up in terms of the
[3087.32 → 3092.36] things that I've I have found hard one of them also it's just like integration with services and so
[3092.36 → 3097.08] with actual obviously like I want to pull down transactions data and so like that it's like you have to
[3097.08 → 3101.72] have a server obviously for you, it's so you need to pull down the music to actually play it, and it's
[3101.72 → 3107.40] you're right that so that forces you to have this kind of hybrid model and I always found it hard to
[3107.40 → 3113.62] like fully have a local thing but then bolt on all of these additional services I guess it was harder
[3113.62 → 3118.30] for actual especially because it was this whole privacy focus first thing where it's like it's all
[3118.30 → 3123.78] privacy focus and yet you have to pull down your transactions uh from this third party thing where you
[3123.78 → 3127.58] log in and give them your data, and then it has to flow through my server because I have to like have
[3127.58 → 3132.46] a key to work with that service so it flows through my server so it's like it's not it's not privacy
[3132.46 → 3138.48] focused at all so that was maybe a hard thing for me but really to step back even more so I love
[3138.48 → 3146.04] having I don't know I guess a hybrid can be it's just like an additional complexity and heart and like
[3146.04 → 3152.40] if it's all from the server all flowing down bolting on a new service is like it's flowing through the
[3152.40 → 3158.54] exact same pipes that everything else uses right now we have this like two different models and has
[3158.54 → 3162.96] that been hard to kind of like think through for you because for me sometimes I'm just like
[3162.96 → 3168.26] too many things going on, and it feels nice to have a single model but how has your approach been to
[3168.26 → 3174.20] sort of tackle that like overhead yeah I mean if you're just building a note app where the only
[3174.20 → 3179.50] person who's going to write down a note, and possibly you write it on your computer, and you write it in your
[3179.50 → 3186.08] phone and those are connected somehow that is much much much easier and this is where you're like in a
[3186.08 → 3194.56] fully isolated like homogenic local first world and once you're in that more hybrid world this is where
[3194.56 → 3202.24] there's a lot more that could go wrong and if I would be all focused on like shipping something
[3202.24 → 3209.30] within a couple of months and I need to like to get users etc maybe I've raised VC money and I need to
[3209.30 → 3214.28] like run faster on the treadmill this would have been the last approach that I would have taken
[3214.28 → 3222.22] however given that I want to build this for the long run I'm taking a much different kind of trade-off
[3222.22 → 3230.86] like I want to be able to like not hate my life building this app continuously once I've launched I don't
[3230.86 → 3237.08] want to just like to move the problems under the rug but I want to if i is there's something that
[3237.08 → 3242.92] can go wrong with a high probability it will go wrong, and so I'm basically just making this a
[3242.92 → 3249.16] problem of tomorrow and once you have more users uh this doesn't make things better so I want to
[3249.16 → 3256.72] address those in a more principled way and yes to answer your question yes it was pretty hard and took
[3256.72 → 3262.62] a pretty long time to figure out principled approaches principled solutions to those really
[3262.62 → 3269.50] hairy problems and I think my solutions that I found here are very tailored to this specific
[3269.50 → 3274.46] use case so I'm not sure whether it's going to be applicable to many others however what I found
[3274.46 → 3281.60] for this works really well for me so what I'm basically doing is I ask myself like what would
[3281.60 → 3289.02] make my life a lot easier working with those external data sources and de facto those data sources
[3289.02 → 3295.00] give you not sort of the git style history of everything that has happened but just give they
[3295.00 → 3303.32] just give you API endpoints of partial snapshots of like this is what our API things what our systems
[3303.32 → 3309.22] things like the current state is and so it gives you like a here's like the first 50 tracks in this
[3309.22 → 3315.20] playlist and then you can paginate over that etc and that is very much built for the sort of like
[3315.20 → 3321.64] temporary client experience the client doesn't remember everything but what would help me a lot
[3321.64 → 3327.78] is if I would get more of like the git style evolution of everything that has happened in this
[3327.78 → 3333.32] playlist everything like this track was added at this position those are the information about this
[3333.32 → 3340.72] particular album but this particular artist etc and I've built myself a little module that basically
[3340.72 → 3348.14] gives me that sort of that worldview and reconstructs a history of everything that has happened about
[3348.14 → 3355.70] so it gives me basically a changelog no pun intended about everything that has happened about this
[3355.70 → 3362.60] particular thing about this particular playlist etc and I basically isolate the heavy lifting eating my
[3362.60 → 3367.64] vegetables on that particular problem and once I have that changelog of all the histories
[3367.64 → 3375.40] then it's basically redux style just applying that so isolating separating the problems and that has
[3375.40 → 3381.30] made such a huge difference for me and that allows me to actually do it and this approach works for
[3381.30 → 3385.30] every data source that I've seen so far in regard to overtone cool
[3385.30 → 3395.82] well friends I'm here with a friend of mine Michael Greenwich co-founder and CEO of work OS we're big fans
[3395.82 → 3401.48] of work OS here Michael tell me about auth kit what is this how's it works why'd you make it
[3401.48 → 3406.14] work OS has been building stuff in authentication for a long time since the very beginning but we
[3406.14 → 3411.52] really focused initially on just enterprise off single sing on SAML authentication but a year or two
[3411.52 → 3416.08] into that we heard from more people that they wanted all the auth stuff covered two-factor auth
[3416.08 → 3422.04] password auth you know with blocking uh passwords that have been reused they wanted off with you know
[3422.04 → 3426.76] other third-party systems and they wanted really work on us to handle all the business logic around
[3426.76 → 3432.02] tying together identities provisioning users and even more advanced things like role-based access
[3432.02 → 3436.78] control and permissions so we started thinking about that more how we could offer it as an API
[3436.78 → 3443.32] and then we realized we had this amazing experience with radix with this API um really the
[3443.32 → 3449.02] component system for building front-end experiences for developers you know radix is downloaded tens of
[3449.02 → 3453.54] millions of times every month for doing exactly this so we glued those two things together and we
[3453.54 → 3458.66] built auth kit so auth kit is the easiest way to add auth to any app not just Next.js if you're building a
[3458.66 → 3464.38] rails app or a Django app or a just straight-up express app or something it comes with a hosted login
[3464.38 → 3469.66] box so you can customize that you can style it you can build your own login experience too it's extremely
[3469.66 → 3474.38] modular you can just use the back-end APIs in a headless fashion but out of the box it gives you
[3474.38 → 3479.22] everything you need to be able to serve customers, and it's tied into the work OS platform so you can
[3479.22 → 3483.30] really quickly add any enterprise features you need so we have a lot of companies that start
[3483.30 → 3486.92] using it because they anticipate they're going to grow up market and want to serve enterprise
[3486.92 → 3492.22] and they don't want to have to re-architect their auth stack when they do that so it's kind of a way to
[3492.22 → 3497.28] like future-proof your auth system for your future growth, and we had people that have done that people
[3497.28 → 3500.32] that started off, and they're like oh I'm just kicking the tires I'm just doing this and then
[3500.32 → 3503.46] poof their app gets a bunch of traction starts growing its awesome
[3503.46 → 3508.66] uh, and they go close Coinbase or Disney or United Airlines, or you know it's like a major
[3508.66 → 3513.84] customer and instead of saying oh no sorry we don't have any of these enterprise things, and we're
[3513.84 → 3518.18] going to have to rebuild everything just go into the work OS dashboard and check a box, and you're done
[3518.18 → 3524.16] aside from the fact that off kit is just awesome the real awesome thing is that it is free for up to
[3524.16 → 3533.02] one million users yes one million monthly active users are included in this out of the gate so
[3533.02 → 3539.00] use it from day one and when you need to scale to enterprise you're already ready too easy you
[3539.00 → 3547.28] can learn more at offkit.com or of course work os.com big fans check it out one million users for free
[3547.28 → 3551.68] wow work os.com or offkit.com
[3551.68 → 3563.70] so how warm is the water than Johannes in the local first world so you've been taking it slow and steady
[3563.70 → 3568.66] in order to solve a lot of the problems what about devs out there maybe they're more like jams or
[3568.66 → 3573.52] like I have a product I want to get it out there I have an idea maybe I have 18 months runway but I got
[3573.52 → 3581.16] I going from zero to customers in 12 to 18 months is it warm enough that local first can make sense or
[3581.16 → 3589.16] is it like ah you're going to have some tough sledding so I would say that right now if you're on a strict
[3589.16 → 3596.82] time budget than local first is probably not yet for you, I will probably give a different answer I would
[3596.82 → 3602.56] have most certainly given a much stricter answer along those lines two years ago so I think right
[3602.56 → 3610.34] now it's already less irrational to go this path but given that there is still a lot of like
[3610.34 → 3617.08] infrastructure missing, or it's not quite as mature yet I would say maybe in two years from now I would
[3617.08 → 3624.22] confidently say okay the water is pretty warm for those specific use cases I would say the more of a
[3624.22 → 3630.24] specific use case you have where you feel like no local first is so perfect for this and this will give
[3630.24 → 3635.42] me like a strategic benefit further down the road for example that you build something where user
[3635.42 → 3640.98] privacy really matters or for other reasons if you have a very specific reason then I would say
[3640.98 → 3647.58] actually the water is warm enough that you can swim or do whatever activity in there
[3647.58 → 3654.76] but as a so it's not a silver bullet, yet it's not like the catch-all scenario yet so I think for that
[3654.76 → 3661.42] you're probably still better off with your typical like three-tier web app, but it is it is trending
[3661.42 → 3668.26] in the right direction we have so many more off-the-shelf technologies already there that people can try out
[3668.26 → 3674.38] there's actually quite a couple that are just about to launch in the coming months, so the space is really
[3674.38 → 3682.32] getting there and I'm very confident that for this mentioned set of use cases I think within the coming years
[3682.32 → 3690.40] we'll see it flip that it gets easier and simpler to build apps in this way in the medium to long term
[3690.40 → 3696.72] since at the end of the day if you build apps that have a rich client-side experience there is just by
[3696.72 → 3702.58] definition there's a distributed system to be solved and this is what like notion is struggling with right
[3702.58 → 3709.00] now this is where many apps are actually getting worse over time my notion calendar doesn't work offline
[3709.00 → 3716.06] etc like those are things that is just almost impossible to retroactively address where you need
[3716.06 → 3721.62] to choose the right architecture from the get-go and I think this will be a better starting point in a
[3721.62 → 3727.60] not-so-distant future I feel a pain of notion honestly like I think notion is the unique scenario where
[3727.60 → 3735.12] you almost want slivers of it to be localism first or mostly local I'm still sticking to that
[3735.12 → 3744.54] because like obviously you want the calendar to work my cal.app from the know on native macOS
[3744.54 → 3751.62] works just fine offline why in the world is notions calendar not and the same thing with opening notion
[3751.62 → 3758.18] to write things you cannot do that it's very challenging it is just like you can render some
[3758.18 → 3761.52] of the things like it'll cache some of that stuff, and you can view it, but you can't interact with it
[3761.52 → 3769.00] so basically notion is unusable when not connected and that's super sad because you're mostly creating
[3769.00 → 3774.32] there are a lot of things that happen in notion because notion can be very simple and notion can
[3774.32 → 3780.58] be very very very complex yeah once you sort of add team members and scale databases and have
[3780.58 → 3786.44] permissions and different layers and all these things, and so I really do not envy the engineering
[3786.44 → 3793.90] challenge they have to solve their mostly local problem but there you go yeah and I mean I have
[3793.90 → 3800.46] so much admiration for the folks who have been building notion uh particularly in the early days but are also
[3800.46 → 3807.06] who are like scaling notion right now and I think it's like almost like an impossible trade-off to make
[3807.06 → 3814.24] right now because um something like Apple software apple notes etc they have a very specific
[3814.24 → 3820.80] target audience which is like you who bought the computer you as the primary user it can be all
[3820.80 → 3827.24] about you there won't be like some super sysadmin who says no like you, you won't have access to all of
[3827.24 → 3833.54] your notes any more it's your computer all of that stuff on that computer is yours whereas like with notion
[3833.54 → 3840.44] as they go more and more into enterprises this is where they need to have certain constraints and
[3840.44 → 3847.94] certain guarantees that some intern might uh if they accidentally got access to some uh confidential
[3847.94 → 3854.56] data that someone can revoke it and not store it for eternity on their device so it's very
[3854.56 → 3859.90] different trade-offs that are more in favour of an enterprise and less in favour of an individual
[3859.90 → 3866.40] who owns that data and I think that's almost an impossible trade-off to make and even that trade-off
[3866.40 → 3873.12] aside it's just a very tough engineering challenge if you start out with a relatively thin client and
[3873.12 → 3879.12] then slap on more and more caching you have to go all the way and treat this to some extent as your
[3879.12 → 3885.70] as your source of truth that you can reasonably build an app experience around that and in that regard
[3885.70 → 3892.20] apple has to if you uh is you're a bit more generous to the definition of local first
[3892.20 → 3899.40] apple has kind of been the OG of local first apps in some way and most iOS apps and so on I guess
[3899.40 → 3906.36] android apps as well are much more local first than the typical web apps yeah I think this uh idea of
[3906.36 → 3911.74] like partial sync basically is kind of what you're implying that notion is kind of needing this idea of
[3911.74 → 3917.40] like some of it is offline, but you can't download the whole thing right because the intern should not
[3917.40 → 3922.20] be able to access those private files so it can't be one big database so you need this like
[3922.20 → 3927.32] partial syncing thing where maybe it's like multiple databases and like one full database
[3927.32 → 3930.90] like can be individually downloaded and that's where I've seen some of the more modern
[3930.90 → 3937.28] electric SQL I think has partial sync and um what were the two other ones that I was just looking at
[3937.28 → 3941.78] power sync and uh yeah there was one more that there's this idea where you can like download part
[3941.78 → 3946.76] of it which solves some of my complaint where like you want to boot up this thing to use it as an API
[3946.76 → 3950.16] but because of the way it works kind of what you're saying Johannes it's like a git thing
[3950.16 → 3954.48] where you can just like download the data you could download just the data that you need to do
[3954.48 → 3959.18] the work that you need to do um, and it's like this partial leasing thing but to me that just sounds
[3959.18 → 3964.26] mind-bendingly complex to figure out how that works and I haven't dug into how the current things
[3964.26 → 3968.88] work, but it does seem like a very hard problem well as a notion user the things I want to do are
[3968.88 → 3974.60] I want to create a new document like I want to be able to note take I want the note-taking app to be
[3974.60 → 3980.20] able to take notes no matter if I'm connected or not I mean that's a very simplistic like don't
[3980.20 → 3986.36] give me anything else I can as an individual user I can understand trade-offs that okay I'm offline i
[3986.36 → 3992.40] can't see the full table I can't manipulate data in the cloud I get that and there may be some users
[3992.40 → 3997.14] out there who are less savvy I don't think that's very savvy honestly but maybe less savvy than that
[3997.14 → 4001.64] that don't get that they get upset but I want to create a note I want to be able to do things like
[4001.64 → 4007.16] that but I get the challenge there I mean there 's's so much complexity that you could have in
[4007.16 → 4014.82] notion with what it does and I just don't even envy the engineering task to even accomplish that
[4014.82 → 4020.00] mission they've got, but they need it they need it in certain ways that's why I think mostly some of it
[4020.00 → 4026.92] certain tasks could be local first or local minded one of the I think I would encourage if I was to say
[4026.92 → 4030.56] anything to the local first community right now I think one of the things that would get me
[4030.56 → 4037.32] very interested is an um incremental approach to all of this kind of stuff because I think my
[4037.32 → 4041.08] problem is like yes you want to create a note, and you want to write that note notion does a
[4041.08 → 4047.14] crap load of other things, and you might not care about 90 of those things working offline right you just
[4047.14 → 4052.38] don't care and so um but like we've been talking about it's you kind of need to buy into this from the
[4052.38 → 4057.20] very beginning right it's a very different development experience um, and it can be a great
[4057.20 → 4060.50] development experience if you have all your data locally you just like run like your SQL queries
[4060.50 → 4065.08] even on the main thread like Johanna said but if you like I want to just build my app the freaking way
[4065.08 → 4068.46] that everybody else is building it because then I can use all the services everybody else is using I can
[4068.46 → 4072.62] use all the analytics things that like everything that that was one of the things another thing I ran
[4072.62 → 4078.64] into actual when I wanted to use like mix panel I literally had to fork their client because it like
[4078.64 → 4082.68] didn't work in the way that I needed to with because it is like you have to run it locally right
[4082.68 → 4087.02] you can't run it on the server anymore and I remember it like didn't work in because I was
[4087.02 → 4092.72] like compiling node to run any web worker like doing something weird like that right and so, and it like
[4092.72 → 4097.02] of course like this third-party SDK which like assumes you're in like node in the server um would like
[4097.02 → 4101.72] work that way so I had to fork it fix all this bug and like every single time I had to do something
[4101.72 → 4108.12] different whenever you walk a different path it's hard um and I think the I will, I want to build my apps
[4108.12 → 4111.58] I want notion to build their apps the way that everybody else is building it the way that they're
[4111.58 → 4116.40] normally building it, and then you can figure out how to add on the local first thing, and it's a
[4116.40 → 4122.28] really hard problem but if you is they should be able to say I want to make the ability to add a note
[4122.28 → 4128.76] and sync or like sync like some basic properties of that note in that special cased way but the other
[4128.76 → 4134.40] things are just hitting in an API to me that sounds interesting I know that's like almost even harder
[4134.40 → 4140.82] because now we're back to like a real hybrid um but to me, it's like then I can do my startup focus
[4140.82 → 4146.20] on just the normal everything and then like as we get bigger and harder and things get harder and i
[4146.20 → 4151.76] can specialize parts of the app to be local first and that to me is that I don't know it sounds
[4151.76 → 4157.40] interesting to me yeah so for what it's worth a lot of the technologies that are in the works right now
[4157.40 → 4163.32] like off the shelf local first is technologies so you've mentioned some of them such as electric
[4163.32 → 4169.78] another one that's coming out soon it's called zero sync by the folks at Roscoe their previous
[4169.78 → 4176.18] product was called reply cache and so what both of those technologies have in common is that they lean
[4176.18 → 4183.56] into your existing Postgres database that you can partially sync the data that's in that Postgres
[4183.56 → 4190.66] database onto your client, and then you have an experience where you can still locally work with the data
[4190.66 → 4197.34] in either an optimistic way or like save some of the rights offline and process them when you get
[4197.34 → 4203.54] online again and sort of like that's that is sort of like a sliding spectrum of what is not yet
[4203.54 → 4209.94] possible eventually possible, but they're heavily leaning into that incremental adoption story which I think
[4209.94 → 4215.68] makes it much easier for people to say like hey we have our existing app we have our existing API we have
[4215.68 → 4221.50] our existing um for example Postgres database we want to build a new feature we want to overhaul
[4221.50 → 4228.48] this existing feature and for that we want to lean into sync we want to build a like a real-time
[4228.48 → 4235.24] collaboration experience so it is getting there but I think if someone does have the freedom and luxury
[4235.24 → 4243.88] to build a Greenfield app and who wants to really like um in the same way as people are trusting apple
[4243.88 → 4248.50] nodes it's like you pull it up you click that new note button and like off you go there's like
[4248.50 → 4254.20] nothing in your way if you want to have that sort of like no asterisk experience I think the best way
[4254.20 → 4259.04] to get there and also have a great developer experience is to fully lean into it well I've
[4259.04 → 4264.68] certainly clicked on new note inside apple notes and seen a loading spinner so I'm not sure if anybody
[4264.68 → 4270.66] necessarily has this problem solved wasn't there before iCloud sync but as soon as they added iCloud sync
[4270.66 → 4276.18] now all of a sudden it was waiting for something to update in the background and I could not enter
[4276.18 → 4281.94] text that was recently probably within the last year or so but I want a one-off which makes you
[4281.94 → 4286.20] think about the state of sync you mentioned these new tools that are upcoming we had DHH on the show
[4286.20 → 4291.70] a couple of weeks ago we were talking about rails 8's embrace of SQLite and some of the possibilities
[4291.70 → 4298.08] that unlocks he was very excited about the potential of having multi-tenant apps where each app gets
[4298.08 → 4302.66] their own SQLite database of course this is how many local first things work in the first place
[4302.66 → 4307.96] jams's actual app you know you get your own little SQLite database there in the browser and I mentioned
[4307.96 → 4313.04] yeah you could have liked your own little base camp right there in your client, and then it just syncs
[4313.04 → 4318.52] and everything's good, and he said he's very happy about that except for the one I said it just syncs
[4318.52 → 4324.90] and he's like I don't think sync is a solved problem like that and I'm curious what's the state of sync
[4324.90 → 4332.42] tools the community is it a solved problem is obviously partial sync is not a solved problem but
[4332.42 → 4339.38] can we rely on the state of the art in syncing libraries and tools I would say this is a heavy
[4339.38 → 4346.92] area of research development and in various attempts there are different trade-offs so probably
[4346.92 → 4352.34] not yet by the time when this episode comes out but in a couple of weeks from now I'm planning
[4352.34 → 4358.30] in collaboration with a friend of mine Jess martin we're working on a comparison landscape resource
[4358.30 → 4364.80] that compares the various like syncing engines the various local first stacks etc so that tries to
[4364.80 → 4369.78] give you a much more matter-of-fact nuanced differentiation of the different technologies
[4369.78 → 4376.62] but what I can already offer is like a high-level answer to this is that there's a couple of different
[4376.62 → 4384.40] approaches to syncing some of them are based on CRTs which has the trade-off that it can work in a fully
[4384.40 → 4391.36] peer-to-peer decentralized approach and then there can be also like approaches where you still have a central
[4391.36 → 4398.14] authority each of them have different trade-offs each of them have multiple technologies building those
[4398.14 → 4405.64] and it's really a matter of what is like a good fit for your application use case so for example if you
[4405.64 → 4413.38] still want to run a central sync entity that has the authority that implies a bunch of other technologies
[4413.38 → 4421.20] so things are coming along nicely there are also a few that synchronize SQLite databases for example
[4421.20 → 4428.88] directly so it really depends on what works well for your app and I would say we're a lot further along
[4428.88 → 4435.08] than compared to five years ago and in hopefully a couple of years from now there's just de facto
[4435.08 → 4440.86] the best technologies for the various trade-offs, and you can just use that a couple of shoutouts I would
[4440.86 → 4447.02] give at this point where I think it mostly just works for the use case that you have is something like
[4447.02 → 4453.94] yes or auto merge if you're using CRT so if you use something like firebase, but you want to go more
[4453.94 → 4460.56] local first those are great options there's also jazz tools, so this is for Greenfield apps and then
[4460.56 → 4467.62] for brownfield apps where you want to incrementally adopt it things like electric SQL parsing the
[4467.62 → 4474.98] upcoming zero etc and there's many others but I would say it's good if you're curious to build
[4474.98 → 4480.32] something with it just to tinker maybe not yet fully go into production now is certainly a great time
[4480.32 → 4485.66] to get started with it and for many production use cases much might be perfectly reasonable already
[4485.66 → 4491.24] I think a lot of the academic research is probably good enough to where we should be able to have
[4491.24 → 4495.54] something that would be really, really good, but it's just hard to actually build out the actual
[4495.54 → 4500.30] because the academic research is like really complex math and to distill that down into a
[4500.30 → 4505.00] product that's actually stable and has the trust of the community because they just literally just need
[4505.00 → 4509.82] to exist for five years to make sure that they're not going to go under that will take time but the I mean
[4509.82 → 4516.08] honestly like I did everything myself which was I overextended myself but syncing was not my
[4516.08 → 4521.14] near my top complaint like the crud stuff there was like amazing and like I can't, I'm not taking
[4521.14 → 4525.94] credit for that myself I just use hyperlogical clocks um it was like really cool how it worked
[4525.94 → 4530.60] and the research was there, and it like the syncing worked great like none of my complaints are
[4530.60 → 4535.38] about like it was hard to sync it's just like man when you start syncing all these other kind of
[4535.38 → 4540.86] things come up that are weird not to say that I even nearly solved it but like it was cool that i
[4540.86 → 4545.34] was able to take some existing research and just get this thing that worked actually reasonably well
[4545.34 → 4551.12] for my use case so i I'm I'm excited to see all these other things coming out but I think it now
[4551.12 → 4559.18] just takes like new generations of actual like experiences that are like always getting a level
[4559.18 → 4565.18] further than the ones before and I think step by step we can actually systematically solve and address
[4565.18 → 4570.22] some of those problems through off-the-shelf community packages or just by sharing sort of
[4570.22 → 4576.80] like best practices and building that tribe knowledge and I think that will already take things very far
[4576.80 → 4583.06] and what is so nice about syncing is I think it will really be like a step function in simplifying our
[4583.06 → 4591.82] app stacks in the same way as like declarative u programming such as react view solid etc this has
[4591.82 → 4598.08] made stuff that been like super gnarly and imperative before where you needed to use jQuery or manipulate
[4598.08 → 4603.78] the DOM manually to making everything just beautiful declarative and there's like entire category of
[4603.78 → 4609.54] stuff you didn't need to deal with anymore now if you get that for data across your different clients
[4609.54 → 4616.36] and servers etc that's what syncing gives you and this can liberate stuff so much and that's amazing
[4616.36 → 4622.40] jams you mentioned before we called a show you did want to give some thoughts on what you think
[4622.40 → 4631.42] maybe a future for mostly local community might look like uh that's that's an I threw Adam a bone there
[4631.42 → 4636.48] open floor for you jams just to share your thoughts on what you think might be compromise or whatever
[4636.48 → 4643.14] your ideas are there yeah so my current I'm kind of like kicking off my own research phase which i
[4643.14 → 4648.06] wanted to do this start a couple of weeks ago and then kids and life and holidays now so hopefully over the
[4648.06 → 4653.18] holidays I'll get some time to really dig in here I'm excited about something and this like again this
[4653.18 → 4657.36] is not mutually exclusive it's not zero-sum like I fully support the local force community I think it
[4657.36 → 4662.86] is a really, really cool idea and cool tech and i love I'm surprised at how like it's not
[4662.86 → 4668.34] mainstream but I'm surprised at how popular it's become i I was at some point was like there's no
[4668.34 → 4671.70] way people are going to actually really invest in this because this is so much work to build a whole
[4671.70 → 4679.36] new platform so really cool to see it but what I am thinking now is that a lot of the benefits at least
[4679.36 → 4686.64] that I was after I might be able to get them with doing things just more on the edge and so the way that
[4686.64 → 4692.80] my thoughts have been sort of evolving is that basically the way actual worked was it ran your
[4692.80 → 4698.08] whole SQLite database, and it did the entire back end of the app back end it was all local
[4698.08 → 4703.32] was in a web worker right so it was a different process but locally on your machine, and you could
[4703.32 → 4707.42] so once you're in the web worker you can do what like the SQL queries were literally synchronous
[4707.42 → 4712.66] like they weren't even async because it's actually faster like it's so fast that the async overhead
[4712.66 → 4718.36] of doing multiple promise calls is actually slowing it down and like just architecturally it was just
[4718.36 → 4722.14] like having to you know you introduce an async call somewhere and then all the call stack
[4722.14 → 4727.36] has to be it's just super annoying so like going back to Johanna's um development experience
[4727.36 → 4732.12] there just like it's amazing once you're in that web worker you async call into it but then once you're
[4732.12 → 4736.20] in there it's great but with all the problems that I've been saying like it's hard to integrate
[4736.20 → 4741.26] services it's just kind of this hybrid approach can be mentally taxing i just kind of want things to
[4741.26 → 4746.68] work the way everybody else works which is that you hit a server, and you get something back what if
[4746.68 → 4751.46] we do this multi-tenant approach is fascinating to me and there's a company torso
[4751.46 → 4756.42] terso.tech which is building out a scalable infrastructure for this where you every single
[4756.42 → 4763.34] person every single request even could possibly get their own SQL database and so what if basically i
[4763.34 → 4769.14] took this web worker back end that I was that is local, but it's not actually local, and it's at the
[4769.14 → 4775.00] the closest data centre point that could possibly be closest to you and so in that way I'm still
[4775.00 → 4779.72] accepting the fact that there is a network call that there is this boundary there, but it's very
[4779.72 → 4786.34] close so i just uh I'm hosting currently my website jlongster.com on the uh northern Virginia
[4786.34 → 4792.28] oz data centre or whatever and I'm in Richmond so I'm a couple of hours drive, and it's about 20 milliseconds
[4792.28 → 4796.56] overhead so I think we can assume 20 to 30 milliseconds overhead for a moderately
[4796.56 → 4803.32] non-fine-tuned uh network infrastructure I think that could even be faster that to me feels
[4803.32 → 4811.00] acceptable and once I accept that single round trip cost than I can move everything to my server
[4811.00 → 4816.30] still have the local SQLite database and have my development experience there and like possibly
[4816.30 → 4820.42] there's like the SQLite syncing going on in the back end so I'm not ditching syncing right you're
[4820.42 → 4825.34] probably going to have to like sync these changes across a back end distributed network, but it's just
[4825.34 → 4831.46] nice to now own that because now i can do analytics I can like to flip something on in just a
[4831.46 → 4836.28] minute without having to like to get everybody to refresh their clients right I can do a multitude
[4836.28 → 4841.36] of clients if I wanted a terminal app for my finances I could curl something really fast and get a
[4841.36 → 4848.68] like a boatload of charts I could do like a quick like I just get that API like instantly right like it
[4848.68 → 4853.14] crosses that network boundary which lets me do everything the way that everybody else is kind of doing it
[4853.14 → 4858.60] so like it's like the same stuff might be going on even the syncing because you're probably going
[4858.60 → 4862.70] to have to be syncing that SQLite database because you're just mutating it locally on that edge instance
[4862.70 → 4868.02] right it's going to have to replicate that somehow elsewhere, but it's like if you draw the line of the
[4868.02 → 4874.24] app and local first is like at least for the most part we're kind of having this hybrid thing where it
[4874.24 → 4879.34] like sort of depends on a server but for the most part a local first app in principle is like you draw
[4879.34 → 4884.70] the line of the entire app and all the data, and it's like all on your computer and then there's
[4884.70 → 4889.10] another circle which is the server, and then it's like syncing to the server this is like if you draw
[4889.10 → 4895.36] the line all around your app, but then it like reaches over into the server for like one little
[4895.36 → 4899.84] bit which is that like edge node and then the edge node is talking to all the complex server
[4899.84 → 4904.56] and the more I go down this the more it's like well i really just want to make a single request to the
[4904.56 → 4908.52] server right I don't want to have to go back and forth maybe I'm evolving to be a use the platform
[4908.52 → 4913.86] person and I'm just leaning into very, very light client apps and now I'm starting to lean into this
[4913.86 → 4920.88] whole react model where it streams live updates it's kind of fitting that it's taken years to get
[4920.88 → 4925.96] here, but it seems like react server components are actually a thing now, and it is a compelling model
[4925.96 → 4930.78] right a long time I was like this is the weirdest idea ever especially when I was local first I was
[4930.78 → 4936.06] like this doesn't benefit me at all now suddenly if I'm flipping my position a little bit it's like
[4936.06 → 4940.56] react server components are amazing because I can run the entire app on the back end get all of this
[4940.56 → 4944.54] stuff that I want stream in just a couple lightweight client components that I want to
[4944.54 → 4950.10] I do full navigations maybe even possibly and the thing that also gets me is the ability to
[4950.10 → 4955.10] flip open new tabs instantly that's one of the things that I'm I'm a little bit like
[4955.10 → 4960.82] because things are all local it's just slow to boot up the app and normally I was like well you boot
[4960.82 → 4964.42] up the app once, and you're digging in your finances for like an hour like I don't really care
[4964.42 → 4970.66] but the thing that does feel nice is just to like command click a link and open up a new window use my
[4970.66 → 4978.50] local macOS windowing system to split the screen have different tabs and just like very quickly in
[4978.50 → 4984.26] light in a very lightweight way just like spawn tons of tabs and those tabs load in just like a hat
[4984.26 → 4990.32] like 30 milliseconds right that can be hard to do local first because you're buying into this thing
[4990.32 → 4995.96] where the entire thing must run locally and so it has to boot up it has to boot up the thing and
[4995.96 → 5002.50] Johannes I mean maybe I'm wrong that you can get a 25 millisecond boot up time on a complex app I'm
[5002.50 → 5008.80] curious what however cast feels if you've optimized for that but that that is where I'm going to be
[5008.80 → 5015.64] researching and kind of diving into so not to say that this is the solution either, but it's something
[5015.64 → 5021.98] that I'm very excited about I applaud you for going down this path in the pursuit of simplicity
[5021.98 → 5028.42] and I think this is why you went down the local first path in the first place, and you've gotten
[5028.42 → 5034.72] really far I think you saw like some glimpses of reward and where you can see like working with
[5034.72 → 5041.20] SQLite locally etc affords you a lot of simplicity, but they're like you, you also revealed a bunch
[5041.20 → 5046.26] of problems that need to be addressed, and you didn't have the time for that and I think there
[5046.26 → 5051.54] will probably be a similar situation there given that a lot of the things are server side the
[5051.54 → 5058.14] constraints are not as severe as on a client that could potentially be like in outer space or something
[5058.14 → 5066.02] so I think this is where you're our traditional knowledge as a web dev community etc more broadly
[5066.02 → 5074.64] applies however I would say this works well for um still like very connected applications so I think
[5074.64 → 5082.22] it's takes server side applications to the next level but if you want to use that for example to build
[5082.22 → 5090.94] like your next notion that should work on crappy plain Wi-Fi then this won't get you far since you'll now get
[5090.94 → 5096.62] even further removed from the next edge worker I think it's going to be a little while until you
[5096.62 → 5105.18] have like edge workers natively in an airplane but I think if connectivity is the slightest concern
[5105.18 → 5112.30] and then I think there might still be challenges or otherwise you kind of need to still solve the
[5112.30 → 5118.46] local first problems since then you need to uh it's all a matter of like you get if you're connected you
[5118.46 → 5125.18] get better latency, but there's actually no difference between being offline and high latency
[5125.18 → 5131.94] being offline is just very, very high latency until you get online again, and fundamentally you still
[5131.94 → 5138.60] need to solve the same problems and if your app can't deal with high latency if it like loses everything
[5138.60 → 5143.66] then you still either you don't support that, and you can't write down your note or something
[5143.66 → 5149.08] or you still need to address it and I think this is where you still need to address some of the
[5149.08 → 5156.28] underlying local first problems but overall it certainly seems like a huge step on the server side and i
[5156.28 → 5161.42] think this is where we'll make progress from both ends like from the all the server side stuff is
[5161.42 → 5167.16] getting better all the local stuff is getting better and hopefully like it in some cases is already
[5167.16 → 5172.34] meeting in the middle I think torso is doing some really, really cool stuff there but yeah it's going to
[5172.34 → 5178.70] take a little while certainly yeah and I agree like it's not it sucks if it's accepting the trade-off
[5178.70 → 5186.62] that on very slow connections or on the plane uh you will have that problem and so that to me is the
[5186.62 → 5189.32] thing that I'm kind of kicking down the road a little bit where it's like if I can specialize
[5189.32 → 5195.54] a very small critical part of the app to be local first and then there might be specific things that i
[5195.54 → 5200.76] would end up building and support there but totally accept that maybe that is like very hard and
[5200.76 → 5206.40] actually doing that later is like can be hard too, and it's a viable position to say that you need you
[5206.40 → 5210.92] do need to embrace it fully from the front end I'm sort of balancing that and I'm kind of curious to see
[5210.92 → 5218.46] if is I could get to that point i will say that like I'm people cared that my app was fast and uh
[5218.46 → 5225.18] I don't know i I think we are a very well-connected world and not to say that like it's not meaningful at
[5225.18 → 5231.08] all but I think I'm kind of just falling back into the like it's I'm ditching some of that complexity
[5231.08 → 5237.08] just in acceptance that like it might not work as well right sometimes yeah two thoughts on that
[5237.08 → 5243.86] actually uh kind of tragic just today uh today is Tuesday they're just in the Baltic Sea between
[5243.86 → 5250.88] Germany and Finland there was like the um sub-ocean fiber connection was cut
[5250.88 → 5257.00] probably by like a state actor really so that shows like how brittle or like everything is
[5257.00 → 5263.86] always connected assumption can be, and it's one thing if like you're you're like whatever your
[5263.86 → 5270.74] access to x or blue sky or whatever is uh is taking a hit, but it's another thing of like more critical
[5270.74 → 5276.54] systems are being taken down and the other way like you don't even need to step into a plane or
[5276.54 → 5283.30] something just go to like a coffee shop and use the public Wi-Fi there and try to like just do work
[5283.30 → 5290.38] for like half an hour, and you'll notice like how all of your apps are just like are rendered completely
[5290.38 → 5297.74] useless and I think having sort of that uh constant assumption everything is like fibre grade 5g grade
[5297.74 → 5304.90] connected I think can bite back at some point in uh Europe for example we people use actually trains
[5304.90 → 5312.14] quite a bit and uh trains has like similar Wi-Fi compared to like your public coffee shop or your
[5312.14 → 5318.42] your plane and so it's more ubiquitous than you think well that leads us back to trade-offs because
[5318.42 → 5324.42] while I completely agree with yo Johannes on that all that sometimes the best app is the one that you
[5324.42 → 5329.34] can actually build and I think that's some of what jams is hitting up with is like what trade-offs is he
[5329.34 → 5334.46] willing to take as a solo dev trying to build whatever it is that you're currently building jams you're
[5334.46 → 5338.40] still working on actual as an open source right are you moving on to another product now as well
[5338.40 → 5342.34] I've pretty much uh the community is fully maintaining it I'm not really part of the
[5342.34 → 5348.06] community any more okay which is the great so cool on to greener pastures but whatever it is that
[5348.06 → 5352.94] you're trying to build i I applaud both of you Johannes for pushing the industry forward in this
[5352.94 → 5359.32] direction and jams for tinkering experimenting while you build and like willing to try new things that
[5359.32 → 5366.30] most of us wouldn't even try to try and exploring that way and helping us discover what might be good
[5366.30 → 5374.52] compromises where it fails etc so you all have me excited about the future regardless of where it is
[5374.52 → 5380.50] I feel like I'm warming up Johannes to the waters as the waters themselves warm up keep us updated keep
[5380.50 → 5386.00] us in the loop as this tooling and this ecosystem fleshes out and matures so we can keep our listeners
[5386.00 → 5390.94] in the know as well because at a certain point I hope you're right, and that pendulum flips
[5390.94 → 5396.72] or that switch flips pendulums don't flip they swing that flip switches to where it becomes actually
[5396.72 → 5405.10] easier to do it this way because I do think the virtues are better than the drawbacks but I think
[5405.10 → 5409.56] like you said for certain people at certain places with certain apps it's still probably too hard
[5409.56 → 5415.28] so definitely as it matures I'm interested in hearing about that Adam anything else from you
[5415.28 → 5422.90] before we call the show notion figure it out I think they're on it to your point Johannes yeah they've
[5422.90 → 5429.70] they've known very well about this problem been working on it for many years it's really hard to
[5429.70 → 5438.08] bolt it on so yeah it's hard yeah a little plug uh on my behalf if this is interesting to any listener
[5438.08 → 5444.94] to dig more into local first when I plug the local first podcast local first FM it goes a lot more
[5444.94 → 5450.18] in depth on all things distributed systems and all things like various trade-offs we had the
[5450.18 → 5457.12] CTO of linear on there we had jams on there we have martin Lehman who's the author of auto merge and
[5457.12 → 5463.18] local first essay on there so if you're curious to learn more this might be a fun place very niche
[5463.18 → 5469.36] all about local first but in case you're curious about this um worthwhile checking out awesome we
[5469.36 → 5475.02] will link to that we will link to all the things jams anything to plug or shout out on our way out
[5475.02 → 5480.04] yeah I'll just say um if you are listening and interested in local first please do not let me
[5480.04 → 5486.92] dissuade you I think it's fascinating and I am choosing slightly different trade-offs every now and
[5486.92 → 5494.58] then, but you get excited, and you go and build and I am fuelled by proving people wrong and so if I say
[5494.58 → 5497.84] something that you disagree with prove me wrong and go build the tooling and support the community
[5497.84 → 5503.24] uh Johannes I'm very impressed and supportive with all the things that you all did uh with riffle
[5503.24 → 5508.12] too also I was following that for a long time so uh fully love what you're doing with live store
[5508.12 → 5513.02] I don't have anything top of mind for me to shout out specifically so that's all I'll say
[5513.02 → 5519.66] I'm very certain that all paths will meet again might be a couple of years realistically but I'm
[5519.66 → 5526.06] pretty sure that we'll get the best of both worlds awesome well that's all this time so we'll just say
[5526.06 → 5528.96] goodbye friends bye friends thank you so much
[5528.96 → 5540.48] fun conversation today with good friends on local first is it the future only time will tell but I think
[5540.48 → 5546.64] if applications like notion can pull it off that will be a big win for local first and all its offering
[5546.64 → 5551.92] and hey if you're at notion, or you know someone at notion let them know we want to talk to them about
[5551.92 → 5557.30] this upcoming feature how they're tackling it and all the good stuff and I guess on that note if you want to
[5557.30 → 5564.90] request an episode the easiest way to do that is to go to changelog.com slash request we love hearing from our
[5564.90 → 5569.56] listeners about what episodes you want to hear, and we're happy to do it again changelog.com slash request
[5569.56 → 5577.32] a big thank you to our friends at fly.io our friends at timescale.com and our friends
[5577.32 → 5582.50] at eight sleep I've never had better sleep I love my eight sleep check them out eightsleep.com their
[5582.50 → 5588.74] Black Friday sales are here use our code changelog and get a lot of money off check them out eightsleep.com
[5588.74 → 5596.56] slash changelog and to our friends at work os.com so awesome love the team there love Michael
[5596.56 → 5603.32] all they're doing okay BMC those beats are banging thank you so much BMC but this week is done this
[5603.32 → 5605.78] show is done so I guess we'll see you next week
[5605.78 → 5617.96] it's better
