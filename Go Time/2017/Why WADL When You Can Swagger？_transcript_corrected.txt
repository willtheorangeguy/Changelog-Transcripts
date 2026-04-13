[0.00 → 2.98] Bandwidth for Changelog is provided by Vastly.
[3.46 → 5.50] Learn more at Fastly.com.
[5.80 → 7.58] And we're hosted on Linde servers.
[8.02 → 10.16] Head to linode.com slash changelog.
[10.84 → 13.44] I'm Ivan Portacarero, and this is Go Time.
[24.52 → 29.28] It's Go Time, a weekly podcast where we discuss interesting topics around the Go programming
[29.28 → 31.76] language, the community, and everything in between.
[32.14 → 36.20] If you currently write Go or aspire to, this is the show for you.
[46.48 → 49.90] Welcome back, everybody, to another episode of Go Time.
[50.26 → 56.50] Today's episode is number 60, and your hosts for today are myself, Eric St. Martin, and
[56.50 → 57.28] Brian Kettle son.
[57.92 → 58.44] Hello.
[59.28 → 60.56] And Galicia Pint.
[61.46 → 61.92] Hi there.
[62.54 → 68.72] And our special guest for today is probably best known for his Go Swagger implementation.
[69.38 → 71.32] Please welcome Ivan Portacarero.
[72.20 → 72.46] Hi.
[73.00 → 73.44] Hi.
[73.90 → 78.34] And Ivan, do you want to give like maybe a kind of brief history about yourself, kind
[78.34 → 83.08] of who you are, what you do, just for the listeners to kind of familiarize themselves with you?
[83.08 → 84.08] Okay.
[84.08 → 84.10] Okay.
[84.10 → 84.12] Okay.
[84.12 → 84.14] Okay.
[84.14 → 84.20] Okay.
[84.20 → 86.62] I'm an engineer.
[86.62 → 94.96] I've been working in the cloud-related field for the past 15 years or something.
[94.96 → 105.32] I currently work for VMware, where I am the tech lead on a product called PKS, which is a hosted
[105.32 → 108.60] version of Kubernetes on VMware infrastructure.
[108.60 → 117.86] In the past, I've worked on machine learning systems, and I've programmed in several different languages.
[117.86 → 124.30] So I'm going to use Go as my main tool for programming.
[124.30 → 124.74] Yeah.
[124.80 → 130.50] So I saw that somebody had mentioned that you had written kind of like a Sinatra implementation
[130.50 → 131.66] in Scala.
[132.32 → 136.24] And that would mean that you probably were familiar with Ruby as well.
[137.10 → 137.30] Yeah.
[137.30 → 142.26] So, yeah, a long time ago, I was on .NET.
[142.44 → 143.20] I did C Sharp.
[143.68 → 145.32] That's how I got started, I guess.
[145.42 → 151.22] And then I got dissatisfied with the lack of open source within Microsoft, but they did
[151.22 → 151.84] Iron Ruby.
[151.94 → 160.22] And that's how I got into Ruby more or less by contributing and talking about the Microsoft's
[160.22 → 163.64] Ruby on .NET system.
[163.64 → 168.32] So I helped build or helped work on Iron Ruby at the time.
[169.84 → 171.14] Did you work with Jeff Lamb?
[172.62 → 175.26] No, Jeff, a little bit.
[175.32 → 176.84] It was more with the people.
[177.90 → 183.74] I forget the names because I'm getting old, and it's been a long time.
[185.84 → 187.64] I worked with Sri BARDA.
[187.78 → 190.38] Jeff Lamb was involved in the early days of this.
[190.38 → 198.90] So this was really around the DLR and this whole Iron Python or the dynamic language runtime
[198.90 → 202.32] for .NET, basically.
[203.06 → 206.06] But Sri BARDA was the team lead at the time.
[206.22 → 210.76] And then there was a Jim Neville involved and a few more people.
[210.76 → 218.28] So I worked with Iron Ruby by writing a book for Manning, which never got published because
[218.28 → 222.22] Microsoft cancelled the project before the book was finished.
[224.72 → 227.48] Or at the same time that the book was finished, really.
[228.44 → 235.52] And so then from there, I also started a startup at that point where I was going to do real-time
[235.52 → 236.92] social media filtering.
[236.92 → 244.60] You can look at today, which probably would be the most similar to IFTTT, because you could
[244.60 → 246.24] set up some query parameters.
[246.58 → 252.58] And if a Twitter feed or a Facebook feed or whatever social media feed would raise an event
[252.58 → 258.34] that matches those query parameters, it would trigger yet another webhook or some other event
[258.34 → 261.12] that you could then react to.
[262.08 → 267.18] To do so, I had to analyze the Twitter files and so on.
[267.42 → 270.10] And Ruby didn't get me far enough.
[270.22 → 272.70] So I started looking for something else, and I found Scala.
[274.04 → 278.52] Scala at that time only had Lyft as a web framework.
[279.04 → 282.16] And Lyft, people said it was very interesting.
[282.30 → 287.74] But from my point of view, it was a web framework that conflated all kinds of responsibilities.
[288.34 → 294.90] And so I started looking for something that looked like Sinatra, because Sinatra was as
[294.90 → 300.42] concise as I could think of for developing web apps or APIs.
[301.24 → 307.30] And so there was a proof of concept at the time, which had just been renamed to Scala.
[307.48 → 308.74] And so I started contributing.
[309.34 → 314.34] And after a while, I was one of the main contributors on that open source project.
[314.34 → 316.18] It was fairly successful.
[316.74 → 319.34] But Scala itself has problems.
[320.02 → 320.92] The language is good.
[321.48 → 323.54] The community is very divided.
[325.70 → 333.80] And if you work with it on a team, it's not very conducive, in my opinion,
[334.40 → 339.66] to have people with very different backgrounds come together and get up to speed very quickly.
[339.66 → 343.70] And so I started looking at Go to find out.
[344.66 → 349.82] Or I wanted to know if Go would actually deliver on that promise, that you can have a team,
[349.92 → 351.94] you can get your team to expand fairly quickly.
[353.22 → 360.30] And people shouldn't have to have weeks of ramp-up time just to learn how to leverage the language
[360.30 → 361.16] to their advantage.
[362.00 → 363.90] And so far, it's been delivering.
[363.90 → 366.68] And so that got me here.
[367.66 → 372.22] In the meantime, through Scala, I got into Swagger because we have to document APIs.
[372.76 → 376.14] The company that invented Swagger, they hired me.
[376.28 → 381.18] And so that's how I got deeper and deeper into that entire Swagger and open API story.
[383.08 → 385.60] And when I switched to Go, there was nothing there.
[385.60 → 390.74] And so I figured people in Go also write lots of APIs.
[390.98 → 396.32] So they should have a way to document them and use them so that other people can generate
[396.32 → 398.22] clients for it in whatever language.
[398.94 → 400.70] And so that's how I got to write in Go Swagger.
[401.16 → 404.22] So let's back up just a second, too.
[404.34 → 410.48] And let's give a little bit of a rundown on what Swagger is for anybody who may not have
[410.48 → 411.66] used it or familiar with it.
[411.66 → 420.82] So Swagger is currently known as OpenAI, I guess, but it started its name as Swagger.
[421.72 → 427.16] The reason it was named Swagger, because the only alternative we had was something that
[427.16 → 429.76] is the acronym of WALL.
[429.90 → 433.06] So in the office, people would go, why Waddle if you can Swagger?
[433.50 → 435.22] And that's how the name came to be.
[435.22 → 446.80] So from there, everybody who writes an API ends up having the same problems, right?
[446.86 → 452.24] So now you have a bunch of clients who are talking to your API.
[452.74 → 455.44] You still want to be able to evolve your API over time.
[456.08 → 457.78] You bring new people on board.
[458.60 → 460.28] They don't know how to use your API.
[460.28 → 464.00] They don't know what the inputs are, what the outputs are, especially if you're writing
[464.00 → 467.60] a dynamic language kind of API.
[468.70 → 475.46] So to formalize those expectations between the boundaries that existed within our teams,
[476.06 → 482.94] we came up, and many people like us have come up with a format to describe what goes into
[482.94 → 483.38] the API.
[483.38 → 489.42] So essentially, it's just a schema for your input and output parameters that captures
[489.42 → 493.06] what some people look at as a contract for your API.
[493.96 → 499.60] Once you have a machine-readable version of something like that, you can take it in many
[499.60 → 500.44] different forms.
[500.68 → 506.92] So the very first thing that we then did was make a UI for it, because now you have this
[506.92 → 507.26] API.
[507.66 → 512.90] If you run the UI, you point it to this description, which is hosted with your API.
[513.38 → 521.04] So you can show nice documentation, especially if you add some markdown or some richer form
[521.04 → 525.04] of documentation, and that documentation lives with your code.
[525.70 → 532.56] So that's important, so that for every version of your code, you actually have a complete form
[532.56 → 536.26] of documentation for the API that that application exposes.
[536.26 → 544.80] From there, obviously, machine-readable makes it also that it's easy to generate clients for
[544.80 → 549.76] your API, because you now know exactly what goes in and out of the API, so you can generate
[549.76 → 550.52] a client for it.
[551.16 → 556.92] If you then take that a little bit further, and you make the API specification easy to define,
[556.92 → 564.70] from there, you could also look at it, oh, now, why don't I do contract first, and I start
[564.70 → 565.68] generating a server?
[566.66 → 573.10] And here it goes particularly strong, because it allows for these broken up definitions in
[573.10 → 574.40] many files and so on.
[575.10 → 581.34] So I took this from what we've tried with Scala, take an API specification, and just generate
[581.34 → 583.82] servers for it that implement the entire specification.
[583.82 → 590.94] So you don't have to really think about all the ceremony, but just start writing about
[590.94 → 595.90] the things you care about, the things that happen after all the common code.
[596.78 → 599.76] And so that's a rundown of what Swagger is.
[600.26 → 605.94] Of course, there are marketplaces now where you can look at all the APIs other companies
[605.94 → 606.50] expose.
[607.06 → 613.68] And so the bigger dream here is if every API exposes a Swagger spec, then you never have to
[613.68 → 615.38] download a client SDK anymore.
[615.76 → 617.44] You can just always generate one.
[618.46 → 624.64] Yeah, one of my favourite things, too, is whenever you use a new API for something, you're always
[624.64 → 627.14] kind of poking around at it and trying things out.
[627.30 → 633.38] And the fact that you can just go into the Swagger UI and kind of play with the example requests
[633.38 → 637.80] and submit them and see how they return and things like that is extremely valuable.
[637.80 → 644.92] So it's wasteful to spend a lot of time building these little example things just to poke at
[644.92 → 645.72] the API.
[646.98 → 647.08] Yeah.
[647.40 → 656.90] So Ivan, describe in a bit more detail, how do you go from the Go code to having that beautiful
[656.90 → 661.42] HTML API documentation?
[661.42 → 662.80] And what do you need?
[662.88 → 667.20] Do you need to boot up a server to serve that HTML?
[667.50 → 668.20] How does it work?
[669.20 → 669.40] Okay.
[669.62 → 670.20] So, yeah.
[670.44 → 681.00] So what you need is you download the binary, a Swagger binary, and you add some vocabulary
[681.00 → 682.54] in your document comment.
[682.80 → 686.62] So the way, because there are two main use cases here, right?
[686.62 → 693.30] So generating a specification from an existing code base, which I suspect, but I really have
[693.30 → 694.48] no way of tracking that.
[694.92 → 701.18] I suspect most people use something like JIN or whatever, and they just want to get a
[701.18 → 704.08] Swagger JSON file come out.
[704.88 → 710.40] In that case, what I've tried to do is define a number of documentation comments that also
[710.40 → 715.94] look good when you just do Godot to describe what is in your API.
[715.94 → 721.46] So you document your routes with some of the expectations that are required for Swagger.
[721.68 → 725.56] You document your models, and you just write doc comments, basically.
[726.36 → 733.30] And then you run Swagger generates spec, and you point it to your main package, and it will
[733.30 → 737.88] reflect over your application and generate the Swagger JSON file.
[738.38 → 743.46] From there, you take the Swagger binary, and you do Swagger serve, and point it to the
[743.46 → 747.62] spec document that you just created, and it will serve up an HTML UI for you.
[748.62 → 757.24] So if I want to have a system where I can share this documentation with my entire team, should
[757.24 → 760.98] I have them download the Swagger?
[760.98 → 762.56] Swagger, what's the best way?
[762.70 → 764.14] That's what I'm trying to think.
[764.68 → 767.28] Should they download the binary and run?
[767.64 → 771.40] For example, I can have the Swagger document station file on GitHub somewhere.
[771.84 → 775.34] Maybe together with my project, they download that, they run it themselves.
[775.76 → 782.66] Or should I put up a server to run so we can all access online?
[782.66 → 789.70] So you don't have to download the server necessarily, as long as you publish the Swagger JSON somewhere.
[790.32 → 794.02] Yeah, not a server, the binary, the Swagger binary, right?
[794.12 → 794.52] The tool.
[795.40 → 800.82] Yeah, once you have a Swagger JSON document, you don't really need the binary anymore.
[802.18 → 804.30] Oh, because it's generated already.
[804.56 → 805.78] Yeah, you have the Swagger JSON.
[805.78 → 822.28] So if you push the Swagger JSON onto like a gist or something, then people could use the raw URL and use it with petstore.swagger.io to leverage the UI that is published there and just paste that in the address box there.
[822.38 → 824.64] And then it will serve you the UI there.
[825.44 → 834.56] If I have it on a GitHub repo, would I get the nice interaction?
[835.78 → 838.34] No, no, you need to have your API running.
[838.48 → 839.98] Yeah, you need to have your API running.
[839.98 → 853.44] So the best way to do it is what was originally specified or part of the specification was it would always be at the root slash Swagger JSON of your API.
[853.62 → 858.04] So if you run your server, you have to make sure that it serves the Swagger spec somewhere.
[858.70 → 859.14] I see.
[859.14 → 872.20] You get it with your API so that the host and the base path and so on are all filled in correctly so that any client who can look at it knows how to use your API because it has the URL where you can find it.
[872.70 → 877.82] And at the same time, it has all the documentation or all of the expectations filled out.
[878.68 → 878.94] Gotcha.
[879.44 → 879.96] Thank you.
[879.96 → 909.94] Thank you.
[909.96 → 939.94] Thank you.
[939.96 → 969.94] Thank you.
[969.96 → 971.96] Thank you.
[971.96 → 975.96] Thank you.
[999.96 → 1002.74] trying libraries to do JSON schema.
[1002.98 → 1006.22] We didn't go, but most of them had some problems,
[1006.40 → 1008.28] and I tried to submit some PRs.
[1008.32 → 1010.66] They never got accepted, so I decided to fork
[1010.66 → 1013.18] and just make it work the way I wanted it to work.
[1014.76 → 1016.60] And so, yeah, it's in many places.
[1018.80 → 1021.46] Last week, there was a project,
[1022.46 → 1025.26] Mecca.io or something, I can post it later on
[1025.26 → 1026.28] in the Slack channel,
[1026.28 → 1031.24] that generates a whole series of tests for your API.
[1031.46 → 1034.44] So it will then try to first test your API
[1034.44 → 1037.56] when you generate it based on the Swagger spec.
[1038.38 → 1039.18] Oh, that's nice.
[1039.86 → 1042.42] Yeah, I agree.
[1044.38 → 1050.08] So now you're at VMware working on the PKS team?
[1050.56 → 1050.78] Yeah.
[1051.26 → 1054.80] I think it's kind of amusing that half of the tech industry
[1054.80 → 1058.70] is employed now in some way, shape, or form around Kubernetes.
[1059.70 → 1059.98] Yeah.
[1060.18 → 1061.78] Well, when I joined VMware,
[1061.90 → 1063.92] I started making noise about Kubernetes,
[1064.72 → 1066.28] and after several false starts,
[1066.38 → 1068.14] we landed on doing this PKS thing.
[1070.08 → 1074.36] Kubernetes has been this interesting evolution, right?
[1074.44 → 1078.68] It's like, let's do OpenStack, but not OpenStack.
[1078.76 → 1079.76] Let's make it a lot better,
[1080.08 → 1081.30] make it our hand containers.
[1081.30 → 1087.22] I do think it solves a problem that most people have at the moment.
[1087.40 → 1092.46] So it's been a very interesting process to see that grow up, that project.
[1093.20 → 1095.74] Yeah, it's really, really exploded.
[1096.52 → 1101.86] And I think that it was a really awesome initiative to begin with.
[1101.86 → 1106.66] But a common conversation I have with people with adoption of Kubernetes
[1106.66 → 1112.28] is just maintenance of the infrastructure in itself is work.
[1112.98 → 1115.36] So people will be quick to implement it,
[1115.42 → 1120.04] but then they find they're struggling with having to maintain Kubernetes
[1120.04 → 1124.38] and all the little failure scenarios and things like that,
[1124.38 → 1126.56] and not their business logic.
[1126.82 → 1129.48] And then they end up with a team that just supports Kubernetes.
[1130.14 → 1133.52] And that's why I like all these amazing product offerings
[1133.52 → 1136.12] for managed Kubernetes, PKS,
[1136.68 → 1138.88] and Microsoft's new AKS,
[1139.14 → 1139.84] and GKE.
[1141.14 → 1142.04] Wait, what's...
[1142.04 → 1144.04] GCE.
[1145.14 → 1145.62] GKE.
[1145.62 → 1147.40] GKE, yeah.
[1149.04 → 1150.08] So, yeah, I mean,
[1150.18 → 1152.92] that's kind of like the perfect world, right?
[1153.14 → 1154.98] You get all the benefits of Kubernetes.
[1155.24 → 1156.56] You only have to focus on
[1156.56 → 1160.16] developing apps that are kind of cloud native and run on it,
[1160.20 → 1161.92] and you don't have to worry about the infrastructure.
[1163.92 → 1164.78] Yeah, well,
[1165.92 → 1166.64] at VMware,
[1166.64 → 1170.40] it's a fairly interesting mix here
[1170.40 → 1171.84] because by definition,
[1172.14 → 1174.22] people are worrying about the infrastructure
[1174.22 → 1177.32] because we have this sphere product.
[1178.30 → 1180.52] So the people we go to
[1180.52 → 1183.44] typically know how to deal with hardware
[1183.44 → 1186.62] and all the failure scenarios that come from there.
[1187.72 → 1188.86] I do think that
[1188.86 → 1191.54] it's this interesting thing.
[1191.68 → 1193.62] So Kubernetes allows you to package your app
[1193.62 → 1196.02] and deploy the containers
[1196.02 → 1197.70] and do all of that service discovery,
[1197.82 → 1198.90] all the cloud native stuff
[1198.90 → 1202.38] you actually require running these larger infrastructures,
[1202.38 → 1205.12] but I think most people are surprised
[1205.12 → 1206.92] by how much Linux you have to know
[1206.92 → 1208.82] to really operate it well
[1208.82 → 1211.40] because it doesn't hide anything from you.
[1211.56 → 1212.62] It's there.
[1212.76 → 1215.42] It makes extremely creative use of the kernel facilities.
[1216.50 → 1217.38] And so it's a very...
[1218.44 → 1220.22] Technically, it's a very interesting project.
[1220.22 → 1222.60] Yeah, it's a lot of fun.
[1223.44 → 1226.58] And I think that there should be experts in that stuff too.
[1226.72 → 1227.46] Don't get me wrong,
[1227.58 → 1229.32] but a lot of businesses,
[1229.56 → 1231.06] especially smaller businesses,
[1231.40 → 1232.98] they're worried about
[1232.98 → 1237.20] having to scale fast and things like that.
[1237.20 → 1238.50] And then, you know,
[1238.56 → 1241.52] once you start hitting odd scenarios
[1241.52 → 1242.46] and stuff like that
[1242.46 → 1244.00] and you hit saturation points
[1244.00 → 1246.26] and things fail in odd ways,
[1246.34 → 1249.08] and then your team who was developing features
[1249.08 → 1251.16] now becomes firefighters
[1251.16 → 1254.22] trying to figure out some of the issues
[1254.22 → 1255.18] and things like that.
[1255.88 → 1256.84] So, yeah.
[1256.94 → 1258.94] And I mean, it's a fun world, right?
[1259.00 → 1260.70] Like some of us enjoy doing that,
[1260.76 → 1262.90] but not everybody has the extra resources
[1262.90 → 1264.30] to be able to do that.
[1264.30 → 1265.30] And like you said,
[1265.46 → 1267.96] with the on-prem people and stuff like that
[1267.96 → 1269.36] that are used to running sphere
[1269.36 → 1270.52] and things like that,
[1270.66 → 1275.32] they've already got that expertise on their team.
[1276.08 → 1278.74] And not every team is fortunate enough
[1278.74 → 1281.52] to have the kind of infrastructure expertise.
[1282.60 → 1282.80] Yeah.
[1283.22 → 1284.68] I'm very interested to see
[1284.68 → 1286.54] what's going to happen with Into
[1286.54 → 1290.04] because that's a very puzzling project to me.
[1290.26 → 1293.18] Like I understand the problem it's trying to solve,
[1293.18 → 1295.42] but I think most businesses
[1295.42 → 1296.86] who are looking at these solutions
[1296.86 → 1298.06] are latency sensitive
[1298.06 → 1299.70] and I don't know how Into
[1299.70 → 1301.76] is going to solve that particular problem.
[1303.18 → 1304.24] Because at the moment,
[1304.66 → 1305.84] when we run our simulations,
[1306.98 → 1308.58] it adds so many hops
[1308.58 → 1310.98] that it becomes a weird proposition.
[1311.72 → 1313.96] I really want to see the service meshes take out
[1313.96 → 1315.34] because in the end,
[1315.42 → 1316.76] the distributed system problems
[1316.76 → 1317.92] are being solved there
[1317.92 → 1320.16] with the circuit breakers
[1320.16 → 1322.16] and all of these calling patterns
[1322.16 → 1323.50] that they encapsulate.
[1324.18 → 1326.84] But it's going to take some work still.
[1327.48 → 1328.58] So that's the thing
[1328.58 → 1330.10] I've been looking into lately.
[1331.16 → 1331.28] Yeah.
[1331.30 → 1332.68] There are a lot of interesting things
[1332.68 → 1333.48] that have popped up
[1333.48 → 1335.80] in maybe the last six to nine months.
[1335.80 → 1336.92] You've got Into,
[1337.22 → 1338.20] Envoy,
[1339.04 → 1340.36] that came out of Lyft.
[1340.80 → 1341.96] Like that's fascinating.
[1342.72 → 1344.28] And all of these are so early,
[1344.28 → 1345.26] and they work
[1345.26 → 1346.46] and they solve problems.
[1346.58 → 1347.90] But I'm really interested to see
[1347.90 → 1350.36] what the version twos
[1350.36 → 1352.14] and threes of those look like.
[1352.56 → 1353.14] Because like you said,
[1353.20 → 1354.98] you kind of add additional hops
[1354.98 → 1356.90] and virtual interfaces
[1356.90 → 1358.30] and all these things,
[1358.60 → 1360.44] which on top of adding latency,
[1360.44 → 1363.42] also add more points of failure
[1363.42 → 1365.44] and weird debugging.
[1366.44 → 1367.60] Yeah, that's, I think,
[1367.64 → 1370.62] one of the unsolved problems so far.
[1370.82 → 1371.36] It is just,
[1371.36 → 1373.48] how can I get you to,
[1373.58 → 1374.56] how can we tell you
[1374.56 → 1376.30] what's broken right now?
[1377.32 → 1379.26] And how do you get out of it?
[1380.06 → 1380.28] Yeah.
[1380.82 → 1382.68] I think one of the hardest parts right now
[1382.68 → 1384.28] is everything's moving so fast
[1384.28 → 1386.58] and there are so many cool projects popping up
[1386.58 → 1389.14] is kind of like that analysis paralysis.
[1389.56 → 1392.46] Like which one of these will be the thing, right?
[1392.84 → 1394.90] Like you could adopt Into
[1394.90 → 1397.44] and in six months,
[1397.54 → 1398.58] nobody's using Into.
[1398.72 → 1400.00] There's some new thing, right?
[1400.00 → 1402.24] And everything's just moving
[1402.24 → 1403.50] at the speed of light
[1403.50 → 1404.90] in the kind of container
[1404.90 → 1406.40] and orchestration world right now
[1406.40 → 1407.62] that it gets really hard
[1407.62 → 1409.58] to settle in
[1409.58 → 1411.68] and just commit to something.
[1411.98 → 1412.70] Because especially
[1412.70 → 1414.46] if you're a large infrastructure, right?
[1414.52 → 1416.06] Like if you pick Envoy
[1416.06 → 1417.88] or Into or something today,
[1419.00 → 1420.38] you know, swapping that out later
[1420.38 → 1422.40] could be a huge effort.
[1423.20 → 1424.32] Yeah, and you probably already
[1424.32 → 1426.00] have solutions in place, right?
[1426.00 → 1428.38] So most of these companies
[1428.38 → 1429.48] probably already have
[1429.48 → 1432.42] like a library like Go Kit
[1432.42 → 1433.40] in their infrastructure
[1433.40 → 1435.90] that allows you to encapsulate
[1435.90 → 1437.44] all of those calling patterns.
[1437.98 → 1440.04] Like call all the services at once,
[1440.28 → 1441.64] drop all the requests on lists
[1441.64 → 1443.50] when I have the first response
[1443.50 → 1444.10] and so on.
[1444.82 → 1447.08] That's essentially what's being captured there.
[1447.88 → 1448.06] Yeah.
[1448.06 → 1449.78] So anyway,
[1449.90 → 1451.34] so it's going to be interesting
[1451.34 → 1452.16] to see it play out.
[1452.22 → 1453.24] I'm going to be a spectator
[1453.24 → 1453.84] in this one
[1453.84 → 1455.06] because
[1455.06 → 1460.18] this whole go swagger thing
[1460.18 → 1461.32] keeps you fairly busy.
[1461.32 → 1461.66] So
[1461.66 → 1464.30] in between my work.
[1464.94 → 1465.74] Is that what you work on
[1465.74 → 1466.40] most of the time?
[1467.48 → 1467.88] Actually,
[1468.04 → 1469.02] I used to.
[1469.18 → 1469.46] So
[1469.46 → 1471.08] I used to work on it
[1471.08 → 1471.82] most of the time.
[1472.06 → 1472.96] I wrote it originally
[1472.96 → 1474.06] just to prove a point.
[1474.06 → 1476.66] But then
[1476.66 → 1478.70] it became fairly useful
[1478.70 → 1480.02] and VMware started
[1480.02 → 1481.04] adopting it as well.
[1481.18 → 1481.30] So
[1481.30 → 1482.88] now
[1482.88 → 1483.94] I have somebody else
[1483.94 → 1485.56] working on it
[1485.56 → 1486.08] who
[1486.08 → 1487.04] is steadily
[1487.04 → 1488.00] fixing bugs.
[1488.12 → 1489.60] So I got corporate sponsorship
[1489.60 → 1490.08] finally.
[1491.44 → 1492.12] And
[1492.12 → 1493.10] I am personally
[1493.10 → 1494.84] much more
[1494.84 → 1495.90] interested in
[1495.90 → 1496.66] distributed
[1496.66 → 1497.78] decentralized
[1497.78 → 1499.06] distributed databases
[1499.06 → 1499.48] or
[1499.48 → 1500.26] having
[1500.26 → 1502.76] another
[1502.76 → 1503.78] unsolved problem
[1503.78 → 1504.56] that exists
[1504.56 → 1504.90] but
[1504.90 → 1506.04] I don't know
[1506.04 → 1506.90] how many people
[1506.90 → 1508.68] are actually
[1508.68 → 1509.62] confronted with it
[1509.62 → 1510.38] is
[1510.38 → 1511.02] gossip
[1511.02 → 1512.30] doesn't work well.
[1513.44 → 1513.96] So
[1513.96 → 1515.32] I'm sure
[1515.32 → 1515.88] you're familiar
[1515.88 → 1516.20] with
[1516.20 → 1516.54] serve
[1516.54 → 1516.78] or
[1516.78 → 1517.16] console
[1517.16 → 1518.04] at the very least
[1518.04 → 1518.76] from HashiCorp.
[1519.42 → 1519.68] Oh yeah,
[1519.88 → 1520.16] definitely.
[1521.16 → 1521.32] Yeah,
[1521.44 → 1521.76] or
[1521.76 → 1522.80] Cassandra
[1522.80 → 1524.56] for example.
[1525.24 → 1525.52] And so
[1525.52 → 1526.20] all of these
[1526.20 → 1526.70] systems
[1526.70 → 1527.22] the
[1527.22 → 1527.98] ACA
[1527.98 → 1529.14] is another one
[1529.14 → 1529.92] from the JVM.
[1530.36 → 1530.98] All these systems
[1530.98 → 1531.72] are gossip-based
[1531.72 → 1532.10] membership
[1532.10 → 1533.32] systems.
[1533.78 → 1534.70] And
[1534.70 → 1535.54] they
[1535.54 → 1538.34] exhibit
[1538.34 → 1538.84] very
[1538.84 → 1539.62] interesting
[1539.62 → 1540.12] failure
[1540.12 → 1540.66] behaviour.
[1541.66 → 1542.14] When you
[1542.14 → 1542.72] turn off
[1542.72 → 1543.10] like
[1543.10 → 1543.84] if you have
[1543.84 → 1544.22] a deployment
[1544.22 → 1544.66] of 100
[1544.66 → 1545.26] or 1,000
[1545.26 → 1545.62] nodes
[1545.62 → 1545.90] and you
[1545.90 → 1546.24] turn off
[1546.24 → 1546.86] 50%
[1546.86 → 1549.00] or 60%
[1549.00 → 1549.32] of the
[1549.32 → 1549.64] nodes
[1549.64 → 1550.70] things
[1550.70 → 1551.12] aren't
[1551.12 → 1551.36] going to
[1551.36 → 1551.98] go well.
[1553.32 → 1553.70] Cassandra
[1553.70 → 1554.32] gets to
[1554.32 → 1555.16] data loss
[1555.16 → 1556.84] console
[1556.84 → 1557.98] has
[1557.98 → 1558.84] takes a
[1558.84 → 1559.34] long time
[1559.34 → 1560.22] to stabilize
[1560.22 → 1561.96] ACA
[1561.96 → 1562.92] similarly.
[1564.14 → 1564.42] And so
[1564.42 → 1565.68] what I've
[1565.68 → 1566.58] been working
[1566.58 → 1567.64] on
[1567.64 → 1568.24] or
[1568.24 → 1568.86] what I've
[1568.86 → 1569.48] been spending
[1569.48 → 1570.20] my free time
[1570.20 → 1570.84] on with the
[1570.84 → 1571.64] VMware research
[1571.64 → 1571.92] group
[1571.92 → 1572.42] is
[1572.42 → 1574.46] improving
[1574.46 → 1575.06] the gossip
[1575.06 → 1575.78] algorithm.
[1576.10 → 1576.38] And so
[1576.38 → 1576.94] I'm working
[1576.94 → 1577.66] on that
[1577.66 → 1578.04] actually
[1578.04 → 1579.24] in my
[1579.24 → 1580.44] GitHub
[1580.44 → 1580.98] account.
[1581.98 → 1582.42] And so
[1582.42 → 1583.16] the results
[1583.16 → 1583.64] we have
[1583.64 → 1584.34] is we go
[1584.34 → 1584.78] from
[1584.78 → 1585.62] interesting
[1585.62 → 1586.00] failure
[1586.00 → 1586.56] conditions
[1586.56 → 1587.16] to ideal
[1587.16 → 1587.58] case.
[1588.48 → 1588.66] And so
[1588.66 → 1588.90] I want
[1588.90 → 1589.24] to prove
[1589.24 → 1589.56] that out
[1589.56 → 1589.82] a little
[1589.82 → 1590.30] bit more
[1590.30 → 1590.84] and then
[1590.84 → 1591.90] hopefully
[1591.90 → 1592.44] submit some
[1592.44 → 1592.90] talks next
[1592.90 → 1593.12] year.
[1594.16 → 1594.28] That's
[1594.28 → 1594.72] funny
[1594.72 → 1595.06] because I
[1595.06 → 1595.66] was creeping
[1595.66 → 1596.02] on your
[1596.02 → 1596.30] GitHub
[1596.30 → 1596.68] account
[1596.68 → 1597.00] today
[1597.00 → 1597.26] and I
[1597.26 → 1597.50] found
[1597.50 → 1597.80] that
[1597.80 → 1598.50] Go Rapid
[1598.50 → 1599.66] repository
[1599.66 → 1600.06] and it
[1600.06 → 1600.78] looks like
[1600.78 → 1601.12] that's what
[1601.12 → 1601.48] you're doing
[1601.48 → 1601.98] there is
[1601.98 → 1603.76] decentralized
[1603.76 → 1605.42] computing.
[1606.68 → 1606.82] Yeah,
[1606.92 → 1607.22] that's
[1607.22 → 1607.90] exactly it.
[1608.68 → 1609.80] We submitted
[1609.80 → 1610.34] a paper
[1610.34 → 1611.48] to ACM
[1611.48 → 1612.68] SITCOM
[1612.68 → 1613.34] earlier this
[1613.34 → 1613.60] year.
[1613.78 → 1614.04] It got
[1614.04 → 1614.46] rejected
[1614.46 → 1614.88] because we
[1614.88 → 1615.30] forgot to
[1615.30 → 1615.90] compare against
[1615.90 → 1616.34] Zookeeper.
[1616.56 → 1618.38] Obviously,
[1618.96 → 1619.20] we were
[1619.20 → 1619.52] all like
[1619.52 → 1620.06] who uses
[1620.06 → 1620.48] Zookeeper
[1620.48 → 1621.10] these days?
[1622.92 → 1623.52] Anybody
[1623.52 → 1624.00] with a
[1624.00 → 1624.34] Kafka
[1624.34 → 1624.90] cluster.
[1625.64 → 1625.82] Yeah,
[1625.84 → 1626.08] it depends
[1626.08 → 1626.68] on what
[1626.68 → 1627.12] circle.
[1628.22 → 1628.44] Does
[1628.44 → 1628.82] Cassandra
[1628.82 → 1629.12] still
[1629.12 → 1629.72] require
[1629.72 → 1629.88] a
[1629.88 → 1630.18] Zookeeper
[1630.18 → 1630.58] cluster?
[1631.54 → 1631.78] No,
[1631.86 → 1632.16] Cassandra
[1632.16 → 1632.54] has their
[1632.54 → 1632.70] own
[1632.70 → 1632.98] gossip
[1632.98 → 1633.50] protocol.
[1634.44 → 1635.02] Kafka
[1635.02 → 1635.38] does
[1635.38 → 1635.80] Zookeeper,
[1636.50 → 1636.98] then
[1636.98 → 1637.48] Missiles,
[1637.60 → 1638.08] I believe,
[1638.80 → 1639.72] uses Zookeeper
[1639.72 → 1640.22] as well.
[1640.72 → 1641.02] There are
[1641.02 → 1641.28] a few
[1641.28 → 1642.06] people who
[1642.06 → 1642.84] choose
[1642.84 → 1643.26] Zookeeper.
[1644.06 → 1644.72] I think
[1644.72 → 1645.12] they go
[1645.12 → 1645.48] by,
[1645.48 → 1646.30] it works
[1646.30 → 1646.80] really well,
[1646.86 → 1647.26] but I
[1647.26 → 1648.50] would say
[1648.50 → 1650.10] for some
[1650.10 → 1650.76] definition of
[1650.76 → 1651.04] well,
[1651.92 → 1652.44] that
[1652.44 → 1652.88] works really
[1652.88 → 1653.18] well.
[1653.92 → 1654.52] If you have
[1654.52 → 1654.80] a small
[1654.80 → 1655.14] cluster,
[1655.28 → 1655.56] it might
[1655.56 → 1655.98] be okay,
[1656.08 → 1656.60] but the
[1656.60 → 1656.98] operational
[1656.98 → 1657.52] cost and
[1657.52 → 1657.96] overhead of
[1657.96 → 1658.20] it is
[1658.20 → 1658.64] just not
[1658.64 → 1659.10] worth it.
[1659.10 → 1659.38] Anyway,
[1659.50 → 1661.82] so now we
[1661.82 → 1662.30] submitted our
[1662.30 → 1662.82] paper again.
[1663.56 → 1663.98] Once it's
[1663.98 → 1664.30] accepted,
[1664.44 → 1664.98] I can publish
[1664.98 → 1665.32] it because
[1665.32 → 1665.68] it's a
[1665.68 → 1666.18] double-blind
[1666.18 → 1666.54] paper,
[1666.62 → 1666.84] so I
[1666.84 → 1667.52] can't just
[1667.52 → 1669.10] publish it
[1669.10 → 1670.18] before it
[1670.18 → 1670.74] gets accepted
[1670.74 → 1671.16] by some
[1671.16 → 1671.52] confidence.
[1671.52 → 1672.80] So tell
[1672.80 → 1673.22] us how
[1673.22 → 1674.36] PKS works.
[1674.88 → 1676.20] PKS is
[1676.20 → 1678.18] an implementation
[1678.18 → 1679.00] of Kubernetes
[1679.00 → 1680.14] for
[1680.14 → 1681.92] distribution
[1681.92 → 1682.94] on VMware,
[1683.54 → 1684.22] so does
[1684.22 → 1685.90] it provisions
[1685.90 → 1686.86] Kubernetes
[1686.86 → 1688.26] on VMware
[1688.26 → 1688.92] systems?
[1690.16 → 1690.66] Yes,
[1691.00 → 1691.64] but it does
[1691.64 → 1692.42] more than
[1692.42 → 1692.70] that.
[1692.96 → 1693.48] So it
[1693.48 → 1694.24] is a
[1694.24 → 1694.84] joint effort
[1694.84 → 1695.34] between
[1695.34 → 1696.22] Pivotal
[1696.22 → 1698.56] and VMware,
[1698.56 → 1700.42] and to
[1700.42 → 1700.62] some
[1700.62 → 1701.12] extent also
[1701.12 → 1702.04] Google for
[1702.04 → 1702.68] the Cloud
[1702.68 → 1703.28] Foundry stuff
[1703.28 → 1703.72] on Google.
[1703.88 → 1704.02] Now,
[1704.48 → 1705.58] this doesn't
[1705.58 → 1705.96] mean that
[1705.96 → 1706.80] PKS requires
[1706.80 → 1707.48] Cloud Foundry,
[1707.58 → 1708.00] it can be
[1708.00 → 1708.46] used next
[1708.46 → 1708.84] to it,
[1709.44 → 1710.00] and it
[1710.00 → 1710.24] can be
[1710.24 → 1710.44] used
[1710.44 → 1710.80] standalone.
[1711.02 → 1711.30] So what
[1711.30 → 1712.26] I work
[1712.26 → 1713.58] on at
[1713.58 → 1713.94] the VMware
[1713.94 → 1714.62] side at
[1714.62 → 1716.90] least is
[1716.90 → 1718.70] the
[1718.70 → 1719.14] integrations
[1719.14 → 1719.44] with the
[1719.44 → 1720.22] VMware stack,
[1720.90 → 1722.56] then the
[1722.56 → 1724.14] optimizations we
[1724.14 → 1724.70] can do at
[1724.70 → 1725.36] the hypervisor
[1725.36 → 1725.96] level to
[1725.96 → 1726.68] work with
[1726.68 → 1728.40] something like
[1728.40 → 1728.82] Kubernetes,
[1729.64 → 1730.14] so that you
[1730.14 → 1730.54] get these
[1730.54 → 1731.24] benefits of
[1731.24 → 1731.66] maintenance
[1731.66 → 1732.46] mode and
[1732.46 → 1733.40] the separation
[1733.40 → 1733.92] between your
[1733.92 → 1734.88] hardware and
[1734.88 → 1735.76] your actual
[1735.76 → 1737.22] workloads,
[1738.12 → 1739.64] and it
[1739.64 → 1740.34] uses Bosch.
[1740.46 → 1740.74] So that's
[1740.74 → 1741.06] the only
[1741.06 → 1741.74] required,
[1741.96 → 1742.60] that's the
[1742.60 → 1743.34] one component
[1743.34 → 1744.06] that's required
[1744.06 → 1745.26] is the
[1745.26 → 1746.10] Bosch piece.
[1747.18 → 1747.88] Bosch, if
[1747.88 → 1748.16] you're not
[1748.16 → 1748.76] familiar with
[1748.76 → 1749.18] it, is a
[1749.18 → 1749.44] lifecycle
[1749.44 → 1750.46] manager for
[1750.46 → 1751.28] applications,
[1752.12 → 1752.62] and so
[1752.62 → 1754.00] it's something
[1754.00 → 1754.50] that will
[1754.50 → 1755.12] monitor your
[1755.12 → 1756.00] application or
[1756.00 → 1756.98] your infrastructure,
[1758.02 → 1758.52] if something
[1758.52 → 1759.06] goes wrong,
[1759.14 → 1759.60] it's going to
[1759.60 → 1760.26] take immediate
[1760.26 → 1760.90] action.
[1761.72 → 1763.14] So if one
[1763.14 → 1763.60] of the nodes
[1763.60 → 1764.00] becomes
[1764.00 → 1764.74] unresponsive,
[1764.78 → 1765.26] for example,
[1765.88 → 1767.60] or some
[1767.60 → 1768.40] failure condition
[1768.40 → 1769.14] happens, it's
[1769.14 → 1769.70] going to try to
[1769.70 → 1770.22] restart the
[1770.22 → 1770.66] processes.
[1770.88 → 1771.06] If the
[1771.06 → 1772.98] processes aren't
[1772.98 → 1773.38] to blame,
[1773.44 → 1773.78] it's going to
[1773.78 → 1774.50] recreate the
[1774.50 → 1774.70] VM.
[1775.66 → 1777.06] So that's in a
[1777.06 → 1777.60] nutshell what it
[1777.60 → 1777.78] does.
[1777.88 → 1778.22] So it's a
[1778.22 → 1778.98] managed unattended
[1778.98 → 1779.58] version of
[1779.58 → 1779.98] Kubernetes.
[1780.44 → 1780.92] Earlier,
[1781.18 → 1782.44] somebody mentioned
[1782.44 → 1784.26] that operating
[1784.26 → 1784.82] these things
[1784.82 → 1785.98] is annoying.
[1786.56 → 1786.88] This is
[1786.88 → 1787.48] exactly the
[1787.48 → 1787.92] type of
[1787.92 → 1788.68] intelligence we
[1788.68 → 1789.16] are trying to
[1789.16 → 1789.88] encapsulate in
[1789.88 → 1790.46] that project.
[1791.14 → 1792.76] It takes away
[1792.76 → 1793.46] the operational
[1793.46 → 1794.80] heart headaches
[1794.80 → 1795.10] of it.
[1795.60 → 1796.48] It will also
[1796.48 → 1797.50] do zero
[1797.50 → 1798.74] downtime upgrades
[1798.74 → 1799.44] and so on
[1799.44 → 1800.66] over time.
[1801.92 → 1802.82] I think that's
[1802.82 → 1803.32] in a nutshell
[1803.32 → 1804.08] what PKS
[1804.08 → 1804.52] is.
[1805.88 → 1807.42] Other than
[1807.42 → 1807.90] that, we
[1807.90 → 1808.76] make sure that
[1808.76 → 1809.58] it can leverage
[1809.58 → 1811.20] just all of
[1811.20 → 1811.88] this stuff that
[1811.88 → 1812.66] VMware already
[1812.66 → 1814.56] has, like a
[1814.56 → 1815.32] login site for
[1815.32 → 1816.36] log aggregation
[1816.36 → 1818.58] and Wavefront
[1818.58 → 1819.24] for metrics
[1819.24 → 1820.14] aggregation and
[1820.14 → 1820.70] so forth.
[1822.32 → 1823.92] I'm employed
[1823.92 → 1824.40] by VMware
[1824.40 → 1825.02] after all.
[1825.78 → 1826.28] Well, that
[1826.28 → 1826.78] makes sense.
[1827.42 → 1828.50] So on the
[1828.50 → 1830.38] networking side,
[1830.44 → 1831.16] does it use
[1831.16 → 1832.88] VMware's networks
[1832.88 → 1834.22] or Kubernetes
[1834.22 → 1835.08] overlays?
[1836.12 → 1836.56] Oh, yes.
[1836.62 → 1836.84] Sorry.
[1837.00 → 1837.66] Yes, it does
[1837.66 → 1838.92] NEXT.
[1838.92 → 1840.42] So it
[1840.42 → 1841.40] includes NEXT,
[1842.12 → 1844.10] which is
[1844.10 → 1844.90] VMware's overlay
[1844.90 → 1845.36] network.
[1845.52 → 1846.20] It's the second
[1846.20 → 1847.22] generation of
[1847.22 → 1847.40] it.
[1848.52 → 1849.10] And what this
[1849.10 → 1849.98] does over
[1849.98 → 1851.52] any of the
[1851.52 → 1852.20] other solutions
[1852.20 → 1853.04] that are out
[1853.04 → 1853.36] there, because
[1853.36 → 1854.46] most people will
[1854.46 → 1855.60] typically go with
[1855.60 → 1856.42] Flannel originally
[1856.42 → 1857.18] and then maybe
[1857.18 → 1858.04] look at something
[1858.04 → 1858.92] like Calico for
[1858.92 → 1859.64] the policies.
[1859.64 → 1861.98] it actually
[1861.98 → 1863.90] gives every
[1863.90 → 1865.54] pod a
[1865.54 → 1865.88] container
[1865.88 → 1866.44] interface that
[1866.44 → 1866.72] can be
[1866.72 → 1868.02] managed outside
[1868.02 → 1870.00] of just the
[1870.00 → 1870.76] environment.
[1870.92 → 1871.30] So you can
[1871.30 → 1871.82] have a network
[1871.82 → 1872.66] administrator who
[1872.66 → 1873.12] sets up a
[1873.12 → 1874.26] bunch of global
[1874.26 → 1875.26] policies in some
[1875.26 → 1875.88] other system,
[1876.18 → 1876.96] the NSX
[1876.96 → 1877.82] management plane,
[1878.32 → 1878.96] and that will
[1878.96 → 1880.02] then translate
[1880.02 → 1880.84] into rules for
[1880.84 → 1881.54] Kubernetes, for
[1881.54 → 1881.90] example.
[1883.56 → 1884.48] There's more
[1884.48 → 1885.28] stuff to it,
[1885.34 → 1885.74] right, because
[1885.74 → 1886.72] NEXT is quite
[1886.72 → 1887.48] an extensive
[1887.48 → 1888.82] piece of work.
[1890.44 → 1891.68] So it's pretty
[1891.68 → 1892.92] optimized in how
[1892.92 → 1893.44] it deals with
[1893.44 → 1894.14] sending traffic
[1894.14 → 1896.30] and doing the
[1896.30 → 1897.40] routing rules and
[1897.40 → 1897.98] so on, but those
[1897.98 → 1898.68] are implementation
[1898.68 → 1900.08] details of NEXT
[1900.08 → 1900.50] itself.
[1902.10 → 1903.32] What is unique,
[1903.40 → 1904.40] I think, is that
[1904.40 → 1905.26] it has a
[1905.26 → 1905.56] centralized
[1905.56 → 1906.52] management plane
[1906.52 → 1907.38] for all types
[1907.38 → 1907.94] of container
[1907.94 → 1908.54] interfaces.
[1909.96 → 1910.76] And that is
[1910.76 → 1912.66] where Kubernetes
[1912.66 → 1913.50] also takes
[1913.50 → 1914.30] advantage of it.
[1914.70 → 1915.48] So NEXT
[1915.48 → 1916.40] has, or the
[1916.40 → 1917.46] NSX team,
[1917.48 → 1919.30] has an
[1919.30 → 1920.08] integration for
[1920.08 → 1920.88] Kubernetes that
[1920.88 → 1921.50] it also works
[1921.50 → 1922.74] with some of
[1922.74 → 1922.98] the other
[1922.98 → 1923.40] Kubernetes
[1923.40 → 1924.78] distributions.
[1925.90 → 1926.48] And so, yes,
[1926.50 → 1926.92] it's a very
[1926.92 → 1927.58] important piece
[1927.58 → 1928.36] of it, the
[1928.36 → 1930.64] security aspects
[1930.64 → 1931.44] that NEXT
[1931.44 → 1932.08] brings to bear.
[1932.72 → 1933.66] Now, if I
[1933.66 → 1934.26] remember right,
[1934.32 → 1935.08] there's a lot
[1935.08 → 1935.74] of components
[1935.74 → 1936.52] that have been
[1936.52 → 1937.86] built by either
[1937.86 → 1939.06] Pivotal or
[1939.06 → 1940.92] VMware that
[1940.92 → 1941.64] kind of contribute
[1941.64 → 1942.32] to this system.
[1942.40 → 1943.22] I know there
[1943.22 → 1943.54] was something
[1943.54 → 1944.30] called KBO,
[1944.44 → 1945.12] that's related
[1945.12 → 1945.68] to this, right?
[1945.68 → 1946.86] Yeah, so
[1946.86 → 1948.30] KBO is the
[1948.30 → 1948.90] Kubernetes on
[1948.90 → 1949.10] Bosch.
[1949.20 → 1949.60] So that is
[1949.60 → 1950.20] the piece
[1950.20 → 1953.70] that interacts
[1953.70 → 1954.38] with Bosch,
[1954.76 → 1956.02] which Bosch
[1956.02 → 1956.72] works through
[1956.72 → 1957.66] a system
[1957.66 → 1957.96] called
[1957.96 → 1958.60] Releases.
[1959.10 → 1960.66] Releases is
[1960.66 → 1961.48] some archive
[1961.48 → 1962.42] that has some
[1962.42 → 1963.76] metadata in
[1963.76 → 1964.86] addition to
[1964.86 → 1966.52] having all
[1966.52 → 1967.16] of the
[1967.16 → 1968.12] source code,
[1968.52 → 1969.60] potentially all
[1969.60 → 1970.02] of the source
[1970.02 → 1970.90] code to rebuild
[1970.90 → 1971.72] that particular
[1971.72 → 1972.32] release from
[1972.32 → 1972.72] scratch.
[1972.72 → 1972.76] package.
[1973.40 → 1974.12] And it
[1974.12 → 1974.50] then has
[1974.50 → 1975.08] also all
[1975.08 → 1975.32] of the
[1975.32 → 1975.72] monitoring
[1975.72 → 1977.56] and failure
[1977.56 → 1979.36] conditions that
[1979.36 → 1979.76] it knows
[1979.76 → 1980.88] about and
[1980.88 → 1981.62] the remediation.
[1981.76 → 1982.00] So it
[1982.00 → 1982.64] encapsulates all
[1982.64 → 1983.12] of that in a
[1983.12 → 1983.70] single package
[1983.70 → 1984.24] and that is
[1984.24 → 1985.20] what KBO is.
[1985.58 → 1986.26] KBO is open
[1986.26 → 1986.80] source and
[1986.80 → 1987.32] everybody can
[1987.32 → 1987.76] use it.
[1988.56 → 1989.18] It's not
[1989.18 → 1990.04] very involved,
[1990.26 → 1991.34] but it does
[1991.34 → 1991.90] require some
[1991.90 → 1992.34] work to get
[1992.34 → 1992.78] that set up
[1992.78 → 1993.02] in your
[1993.02 → 1993.54] environment.
[1994.40 → 1994.82] And then
[1994.82 → 1996.22] PKS is the
[1996.22 → 1996.76] piece that
[1996.76 → 1997.44] will make it
[1997.44 → 1998.78] easy to set
[1998.78 → 1999.12] that up in
[1999.12 → 1999.68] your environment
[1999.68 → 2000.70] with a UI and
[2000.70 → 2001.52] so all of
[2001.52 → 2001.94] the management
[2001.94 → 2002.42] tools that
[2002.42 → 2002.64] you would
[2002.64 → 2004.20] expect for
[2004.20 → 2004.82] an enterprise
[2004.82 → 2005.38] environment.
[2006.26 → 2006.66] So hooking
[2006.66 → 2007.10] it into
[2007.10 → 2007.88] Active Directory
[2007.88 → 2009.96] and setting
[2009.96 → 2012.14] up RAC and
[2012.14 → 2012.94] all of that
[2012.94 → 2013.70] kind of stuff,
[2013.78 → 2014.42] all of those
[2014.42 → 2015.34] controls that
[2015.34 → 2015.88] you expect from
[2015.88 → 2016.30] an enterprise
[2016.30 → 2017.64] application is
[2017.64 → 2017.98] what goes
[2017.98 → 2018.64] into PKS,
[2018.78 → 2019.10] which is
[2019.10 → 2019.62] closed source.
[2020.34 → 2020.76] Nice.
[2021.48 → 2023.18] So far it's
[2023.18 → 2023.82] been working
[2023.82 → 2024.54] fairly well.
[2025.12 → 2025.80] We hope to
[2025.80 → 2027.00] release this
[2027.00 → 2028.10] by December.
[2029.22 → 2029.82] Somewhere in
[2029.82 → 2030.18] December,
[2030.30 → 2030.60] I'll put it
[2030.60 → 2030.94] that way.
[2031.00 → 2031.34] I can't
[2031.34 → 2032.48] say exactly
[2032.48 → 2035.98] when because
[2035.98 → 2037.44] it's a
[2037.44 → 2038.10] natural process
[2038.10 → 2038.58] so it's
[2038.58 → 2039.00] more like
[2039.00 → 2039.62] around this
[2039.62 → 2041.38] time something
[2041.38 → 2041.82] will get
[2041.82 → 2042.18] released.
[2043.06 → 2043.40] Awesome.
[2043.58 → 2044.32] So I think
[2044.32 → 2045.38] we are
[2045.38 → 2045.94] probably like
[2045.94 → 2047.10] two-thirds
[2047.10 → 2047.80] is away
[2047.80 → 2048.52] through the
[2048.52 → 2048.78] show.
[2049.50 → 2049.80] Do you guys
[2049.80 → 2050.28] want to jump
[2050.28 → 2051.24] into some
[2051.24 → 2051.92] projects and
[2051.92 → 2052.28] news?
[2053.08 → 2053.56] And Ivan,
[2053.86 → 2054.82] feel free to
[2054.82 → 2055.78] jump in too
[2055.78 → 2056.88] and mention
[2056.88 → 2058.00] stuff or
[2058.00 → 2059.12] comment on
[2059.12 → 2059.84] things that
[2059.84 → 2061.08] we bring
[2061.08 → 2061.30] up.
[2062.14 → 2062.28] Okay.
[2062.74 → 2063.40] So who
[2063.40 → 2063.78] wants to
[2063.78 → 2064.14] kick this
[2064.14 → 2064.86] off with
[2064.86 → 2065.52] stuff they've
[2065.52 → 2065.98] kind of ran
[2065.98 → 2066.44] into this
[2066.44 → 2066.68] week?
[2067.20 → 2067.92] I'll start
[2067.92 → 2068.20] it off.
[2068.40 → 2068.84] I think
[2068.84 → 2069.28] there's an
[2069.28 → 2070.00] exciting new
[2070.00 → 2070.70] project called
[2070.70 → 2072.12] Factory from
[2072.12 → 2072.92] Mike Durham,
[2073.40 → 2074.22] who is
[2074.22 → 2075.22] probably most
[2075.22 → 2076.26] popular for
[2076.26 → 2077.30] the Sidekick
[2077.30 → 2078.98] project that
[2078.98 → 2079.62] most Rails
[2079.62 → 2080.42] apps use for
[2080.42 → 2081.42] background tasks.
[2082.08 → 2082.80] Factory seems
[2082.80 → 2083.98] to be pretty
[2083.98 → 2085.38] much a Sidekick
[2085.38 → 2086.30] successor, but
[2086.30 → 2087.16] written in
[2087.16 → 2088.62] Go and
[2088.62 → 2089.34] it supports
[2089.34 → 2090.72] Go and
[2090.72 → 2091.74] Ruby natively.
[2091.80 → 2091.96] It looks
[2091.96 → 2092.52] pretty slick
[2092.52 → 2094.70] and it
[2094.70 → 2095.44] feels like
[2095.44 → 2096.12] maybe it's
[2096.12 → 2098.16] the thing
[2098.16 → 2098.74] that happened
[2098.74 → 2099.30] after you
[2099.30 → 2099.90] learn from
[2099.90 → 2100.22] building
[2100.22 → 2100.72] Sidekick.
[2100.90 → 2101.62] So I'm
[2101.62 → 2102.04] excited to
[2102.04 → 2102.48] play with
[2102.48 → 2104.18] Factory and
[2104.18 → 2105.76] I'm more
[2105.76 → 2106.92] excited because
[2106.92 → 2108.00] Mike has
[2108.00 → 2108.92] done a really
[2108.92 → 2109.90] good job of
[2109.90 → 2110.46] something that
[2110.46 → 2111.44] most open
[2111.44 → 2113.08] source companies
[2113.08 → 2113.76] can't do,
[2114.00 → 2114.80] which is
[2114.80 → 2115.68] make a
[2115.68 → 2116.42] living off
[2116.42 → 2117.14] of a
[2117.14 → 2117.42] single
[2117.42 → 2118.00] open source
[2118.00 → 2118.56] project.
[2118.74 → 2118.92] So he's
[2118.92 → 2119.50] got Sidekick
[2119.50 → 2120.10] and Sidekick
[2120.10 → 2121.50] Pro and
[2121.50 → 2122.28] I'm pretty
[2122.28 → 2122.70] sure he's
[2122.70 → 2123.02] paying the
[2123.02 → 2123.76] bills with
[2123.76 → 2124.30] just Sidekick
[2124.30 → 2124.56] Pro.
[2124.80 → 2125.36] So I hope
[2125.36 → 2126.44] that he can
[2126.44 → 2127.14] continue to
[2127.14 → 2127.82] evolve that
[2127.82 → 2128.46] model because
[2128.46 → 2128.88] that's really
[2128.88 → 2129.20] slick.
[2130.24 → 2130.64] It's going to
[2130.64 → 2131.12] be interesting
[2131.12 → 2132.18] to watch if
[2132.18 → 2133.06] it's going to
[2133.06 → 2134.54] change what's
[2134.54 → 2135.16] behind the
[2135.16 → 2136.62] service from
[2136.62 → 2137.16] Ruby to
[2137.16 → 2137.48] Go.
[2139.34 → 2140.12] This is
[2140.12 → 2140.68] great, by
[2140.68 → 2140.94] the way,
[2140.98 → 2141.68] great finds.
[2141.68 → 2142.94] Yeah, I've
[2142.94 → 2143.64] used Sidekick
[2143.64 → 2144.36] a lot in
[2144.36 → 2144.84] the past.
[2145.90 → 2146.28] Yeah, same
[2146.28 → 2146.96] thing back in
[2146.96 → 2148.32] my Ruby days,
[2148.40 → 2148.66] I used
[2148.66 → 2149.18] Sidekick a
[2149.18 → 2149.40] lot.
[2150.52 → 2150.94] And you can
[2150.94 → 2151.46] do your own
[2151.46 → 2151.94] code for
[2151.94 → 2152.34] this, but
[2152.34 → 2153.38] it has a
[2153.38 → 2154.70] nice dashboard
[2154.70 → 2156.12] and so
[2156.12 → 2156.60] easy to
[2156.60 → 2156.98] use.
[2158.10 → 2159.74] So last
[2159.74 → 2160.70] episode, we
[2160.70 → 2161.22] told everybody
[2161.22 → 2162.00] to update
[2162.00 → 2162.78] to Go
[2162.78 → 2164.78] 191 and
[2164.78 → 2167.26] Go 184,
[2167.42 → 2167.94] I think it
[2167.94 → 2168.16] was.
[2168.82 → 2169.74] So there
[2169.74 → 2170.40] is a minor
[2170.40 → 2171.20] patch release
[2171.20 → 2173.22] 192 and
[2173.22 → 2175.78] 185, which
[2175.78 → 2176.64] has just
[2176.64 → 2177.58] some basic
[2177.58 → 2178.28] updates to
[2178.28 → 2178.86] the compiler
[2178.86 → 2179.40] and runtime
[2179.40 → 2179.96] and stuff.
[2180.16 → 2181.84] But if you
[2181.84 → 2182.38] are noticing
[2182.38 → 2183.56] issues with
[2183.56 → 2184.76] Go Get on
[2184.76 → 2185.38] non-Git
[2185.38 → 2186.32] repositories,
[2186.84 → 2187.70] those will
[2187.70 → 2188.32] fix it.
[2189.08 → 2190.08] That bug was
[2190.08 → 2190.96] introduced in
[2190.96 → 2191.98] the last
[2191.98 → 2192.66] batch release.
[2194.06 → 2195.16] Other updates,
[2195.38 → 2195.86] Go Bot
[2195.86 → 2198.58] released 1.7.0,
[2198.58 → 2200.38] Go Bot
[2200.38 → 2201.56] which has
[2201.56 → 2202.62] OpenCV3
[2202.62 → 2203.32] support in
[2203.32 → 2203.50] it.
[2204.16 → 2204.72] So now we
[2204.72 → 2205.42] can do all
[2205.42 → 2205.92] kinds of
[2205.92 → 2206.74] vision stuff
[2206.74 → 2207.62] with our
[2207.62 → 2208.54] hardware projects.
[2209.28 → 2209.82] And they
[2209.82 → 2210.62] introduced, I'm
[2210.62 → 2210.84] trying to
[2210.84 → 2211.26] remember the
[2211.26 → 2211.74] names of
[2211.74 → 2212.58] them, but
[2212.58 → 2213.30] from the
[2213.30 → 2214.04] Go4Con hack
[2214.04 → 2215.38] day, a
[2215.38 → 2215.90] couple people
[2215.90 → 2217.06] implemented
[2217.06 → 2218.28] support for
[2218.28 → 2219.20] some other
[2219.20 → 2220.24] drones and
[2220.24 → 2220.88] robots and
[2220.88 → 2221.16] stuff.
[2221.16 → 2222.42] Oh, nice.
[2223.42 → 2224.00] Yeah, Ron
[2224.00 → 2224.76] is a
[2224.76 → 2225.20] machine.
[2226.42 → 2226.56] Do you
[2226.56 → 2226.86] know that
[2226.86 → 2227.32] Ron is
[2227.32 → 2228.12] going to
[2228.12 → 2228.40] go for
[2228.40 → 2228.84] Con Brazil?
[2229.96 → 2230.38] Oh, really?
[2230.94 → 2231.56] That's awesome.
[2232.28 → 2232.76] Yeah, that's
[2232.76 → 2233.08] awesome.
[2233.62 → 2234.42] Pretty sure he
[2234.42 → 2234.72] is.
[2235.14 → 2235.58] Well, no,
[2235.64 → 2236.10] yeah, he's
[2236.10 → 2236.82] scheduled to
[2236.82 → 2237.38] speak about
[2237.38 → 2238.00] Go Bot
[2238.00 → 2239.14] and IoT.
[2240.46 → 2241.56] I love
[2241.56 → 2241.88] Ron.
[2242.00 → 2242.64] He's just so
[2242.64 → 2243.32] passionate and
[2243.32 → 2243.94] full of energy.
[2245.28 → 2245.84] Yeah.
[2246.28 → 2246.92] Just an
[2246.92 → 2247.54] amazing guy.
[2248.80 → 2249.20] Yeah, I'm
[2249.20 → 2249.80] definitely going to
[2249.80 → 2250.62] find a way to
[2250.62 → 2251.02] have dinner
[2251.02 → 2251.42] with them
[2251.42 → 2252.12] when we
[2252.12 → 2252.54] are there.
[2253.38 → 2253.82] Nice.
[2254.90 → 2255.64] So I came
[2255.64 → 2256.22] across another
[2256.22 → 2257.16] interesting project
[2257.16 → 2257.74] called
[2257.74 → 2259.58] Outhouse, and
[2259.58 → 2260.00] this is at
[2260.00 → 2261.16] GitHub.com
[2261.16 → 2261.60] slash
[2261.60 → 2263.88] I-M-Q-S-A-U
[2263.88 → 2264.76] slash
[2264.76 → 2267.54] A-U-T-H-A-U-S.
[2268.08 → 2269.32] And I haven't
[2269.32 → 2270.02] played with it
[2270.02 → 2270.58] yet, but it
[2270.58 → 2271.40] looks like it
[2271.40 → 2272.16] might be
[2272.16 → 2273.28] the beginning
[2273.28 → 2274.32] or maybe the
[2274.32 → 2275.56] evolution of
[2275.56 → 2277.56] something that
[2277.56 → 2278.10] could be a
[2278.10 → 2278.80] really solid
[2278.80 → 2279.58] user authentication
[2279.58 → 2280.48] system for
[2280.48 → 2280.68] Go.
[2281.22 → 2282.34] Back in my
[2282.34 → 2283.08] Ruby days, we
[2283.08 → 2285.08] had device
[2285.08 → 2286.04] and all of
[2286.04 → 2287.16] those other
[2287.16 → 2288.92] Ruby things
[2288.92 → 2290.06] that really
[2290.06 → 2290.44] did Auth
[2290.44 → 2291.38] well, and
[2291.38 → 2291.80] there's really
[2291.80 → 2292.96] nothing that's
[2292.96 → 2293.92] kind of shown
[2293.92 → 2295.16] on the Go
[2295.16 → 2296.64] side in
[2296.64 → 2297.24] terms of
[2297.24 → 2297.78] authentication
[2297.78 → 2299.18] and authorization.
[2299.56 → 2299.82] So I'm
[2299.82 → 2300.40] really hoping
[2300.40 → 2302.42] that something
[2302.42 → 2302.92] will come
[2302.92 → 2304.04] out that
[2304.04 → 2305.38] isn't a
[2305.38 → 2305.60] law.
[2305.60 → 2307.48] we need
[2307.48 → 2307.84] an easy
[2307.84 → 2308.18] way to
[2308.18 → 2308.66] add
[2308.66 → 2309.72] authentication
[2309.72 → 2310.32] to our
[2310.32 → 2310.82] Go apps.
[2311.16 → 2311.48] So I'm
[2311.48 → 2311.92] excited to
[2311.92 → 2312.22] play with
[2312.22 → 2312.64] this one
[2312.64 → 2313.12] at some
[2313.12 → 2313.46] point when
[2313.46 → 2313.66] I have
[2313.66 → 2314.00] some free
[2314.00 → 2315.36] time and
[2315.36 → 2316.22] hopefully
[2316.22 → 2317.88] it's as
[2317.88 → 2318.12] good as
[2318.12 → 2318.54] it looks.
[2318.54 → 2319.54] Go.
[2319.54 → 2321.64] Let us
[2321.64 → 2322.10] know how
[2322.10 → 2322.56] it goes.
[2323.24 → 2323.86] I'm
[2323.86 → 2324.92] feeling so
[2324.92 → 2326.06] proud of
[2326.06 → 2326.42] Go right
[2326.42 → 2326.64] now.
[2326.76 → 2326.92] I feel
[2326.92 → 2327.58] like it
[2327.58 → 2329.06] grew from
[2329.06 → 2329.62] a teenager
[2329.62 → 2330.40] into a
[2330.40 → 2331.04] young adult.
[2332.90 → 2333.56] It's
[2333.56 → 2334.26] maturing.
[2335.84 → 2336.44] Do you
[2336.44 → 2336.78] know how
[2336.78 → 2337.18] that's going
[2337.18 → 2337.72] to compare
[2337.72 → 2338.96] to some
[2338.96 → 2339.16] of the
[2339.16 → 2340.40] modules for
[2340.40 → 2341.92] Auth boss?
[2341.92 → 2342.76] I know
[2342.76 → 2343.06] they had
[2343.06 → 2343.92] a password
[2343.92 → 2345.38] authentication
[2345.38 → 2345.96] and they've
[2345.96 → 2347.02] got email
[2347.02 → 2347.78] confirmation
[2347.78 → 2349.12] and things
[2349.12 → 2349.62] like that.
[2350.88 → 2351.16] So the
[2351.16 → 2351.96] last time
[2351.96 → 2352.30] I looked
[2352.30 → 2353.02] at Auth boss
[2353.02 → 2354.28] and I
[2354.28 → 2354.60] don't know
[2354.60 → 2355.74] if this
[2355.74 → 2356.44] still applies
[2356.44 → 2356.84] but the
[2356.84 → 2357.26] last time
[2357.26 → 2357.66] I looked
[2357.66 → 2358.94] there
[2358.94 → 2361.04] were a
[2361.04 → 2361.30] lot of
[2361.30 → 2361.58] broken
[2361.58 → 2362.12] things in
[2362.12 → 2362.66] Auth boss
[2362.66 → 2364.88] and they
[2364.88 → 2365.44] didn't really
[2365.44 → 2366.02] seem to
[2366.02 → 2367.14] want to
[2367.14 → 2367.62] fix them.
[2367.74 → 2368.14] They wanted
[2368.14 → 2368.60] to do a
[2368.60 → 2368.98] rewrite
[2368.98 → 2371.10] and kind
[2371.10 → 2371.46] of fix
[2371.46 → 2371.88] the
[2371.88 → 2372.84] overall
[2372.84 → 2373.38] architecture.
[2373.56 → 2373.72] So I
[2373.72 → 2373.96] don't know
[2373.96 → 2374.58] if Auth boss
[2374.58 → 2376.34] has been
[2376.34 → 2376.80] rewritten.
[2377.06 → 2377.36] There were
[2377.36 → 2377.74] a lot of
[2377.74 → 2378.06] things it
[2378.06 → 2378.36] didn't
[2378.36 → 2378.84] support
[2378.84 → 2380.34] when I
[2380.34 → 2380.64] looked at
[2380.64 → 2380.84] it a
[2380.84 → 2381.22] year or
[2381.22 → 2381.64] so ago.
[2382.72 → 2383.06] So I
[2383.06 → 2383.42] don't know
[2383.42 → 2383.76] if I can
[2383.76 → 2384.18] answer that
[2384.18 → 2384.86] question very
[2384.86 → 2385.16] well.
[2386.82 → 2387.42] In its
[2387.42 → 2388.20] 1.0
[2388.20 → 2388.82] version,
[2389.02 → 2389.46] Auth boss
[2389.46 → 2390.74] was not
[2390.74 → 2391.70] all that I
[2391.70 → 2392.14] wanted it
[2392.14 → 2392.52] to be.
[2393.80 → 2393.92] Yeah,
[2393.94 → 2394.18] and that's
[2394.18 → 2394.42] the thing
[2394.42 → 2394.84] with most
[2394.84 → 2395.70] open source
[2395.70 → 2396.30] projects.
[2396.62 → 2397.08] You see
[2397.08 → 2397.32] them and
[2397.32 → 2397.60] you're like,
[2397.64 → 2398.00] I want
[2398.00 → 2398.62] this thing,
[2398.72 → 2398.98] but it's
[2398.98 → 2399.86] not production
[2399.86 → 2400.24] ready.
[2400.24 → 2402.12] We're all
[2402.12 → 2402.80] guilty of
[2402.80 → 2403.00] it.
[2403.24 → 2403.46] It's like,
[2403.50 → 2403.80] oh, it's
[2403.80 → 2404.30] on GitHub.
[2404.58 → 2404.84] I can
[2404.84 → 2405.48] totally use
[2405.48 → 2405.74] it in
[2405.74 → 2406.14] production.
[2408.38 → 2410.24] Well, it
[2410.24 → 2410.78] doesn't bother
[2410.78 → 2411.42] me to jump
[2411.42 → 2412.00] in and help
[2412.00 → 2412.58] them make
[2412.58 → 2413.14] it production
[2413.14 → 2413.46] ready.
[2414.20 → 2414.64] I just
[2414.64 → 2415.06] like the
[2415.06 → 2415.54] idea that
[2415.54 → 2416.28] somebody has
[2416.28 → 2417.70] taken a
[2417.70 → 2418.14] vision and
[2418.14 → 2418.64] started to
[2418.64 → 2418.98] see it
[2418.98 → 2419.36] through to
[2419.36 → 2419.78] reality.
[2420.58 → 2421.36] That's usually
[2421.36 → 2421.90] when I find
[2421.90 → 2422.44] the projects
[2422.44 → 2422.90] too, is
[2422.90 → 2424.32] somewhere in
[2424.32 → 2425.12] between vision
[2425.12 → 2425.78] and reality.
[2425.78 → 2427.66] So our
[2427.66 → 2428.44] next one,
[2428.80 → 2429.42] I am
[2429.42 → 2430.06] particularly
[2430.06 → 2431.66] excited about
[2431.66 → 2432.52] who wants
[2432.52 → 2432.98] to talk
[2432.98 → 2434.00] about GRV.
[2434.94 → 2435.72] Oh, wow.
[2435.82 → 2436.34] GRV is
[2436.34 → 2436.68] awesome.
[2437.60 → 2438.16] Have you
[2438.16 → 2438.48] pulled it
[2438.48 → 2438.90] down yet?
[2439.64 → 2440.30] Yeah, I
[2440.30 → 2440.56] have.
[2441.12 → 2441.88] Oh, my
[2441.88 → 2442.24] God.
[2442.28 → 2442.82] It's awesome.
[2443.72 → 2444.14] Have you
[2444.14 → 2445.40] seen GRV,
[2445.64 → 2445.84] Ivan?
[2446.76 → 2447.70] No, I'm
[2447.70 → 2448.30] looking at it
[2448.30 → 2448.94] right now.
[2450.94 → 2451.54] Looks
[2451.54 → 2451.90] cool.
[2453.10 → 2453.52] I wonder
[2453.52 → 2453.78] how it
[2453.78 → 2454.40] compares to
[2454.40 → 2454.76] TIG.
[2454.92 → 2455.32] Because I've
[2455.32 → 2455.76] used TIG
[2455.76 → 2456.00] in the
[2456.00 → 2456.28] past.
[2458.68 → 2459.24] Which
[2459.24 → 2459.48] tool?
[2460.22 → 2460.56] TIG.
[2461.48 → 2461.90] It's
[2461.90 → 2464.16] similar in
[2464.16 → 2464.52] goals.
[2465.22 → 2465.66] It's also
[2465.66 → 2466.40] a CLI,
[2466.92 → 2468.04] a terminal
[2468.04 → 2469.22] version of
[2469.22 → 2469.74] a Git
[2469.74 → 2470.08] client.
[2471.72 → 2472.48] I haven't
[2472.48 → 2472.88] seen that
[2472.88 → 2473.14] one.
[2474.08 → 2475.76] It looks
[2475.76 → 2476.42] really awesome
[2476.42 → 2476.76] and it's
[2476.76 → 2477.28] probably going
[2477.28 → 2477.84] to solve
[2477.84 → 2478.86] a lot of
[2478.86 → 2479.32] the use
[2479.32 → 2479.90] cases where
[2479.90 → 2480.34] I try to
[2480.34 → 2480.66] pull up
[2480.66 → 2480.98] GitHub
[2480.98 → 2481.80] for stuff.
[2482.22 → 2483.44] So I'm
[2483.44 → 2484.12] actually really
[2484.12 → 2484.80] excited about
[2484.80 → 2485.32] trying to
[2485.32 → 2485.74] use it
[2485.74 → 2486.04] more.
[2486.98 → 2487.46] Anything
[2487.46 → 2488.20] that keeps
[2488.20 → 2488.52] me in
[2488.52 → 2488.72] my
[2488.72 → 2489.08] terminal
[2489.08 → 2489.40] makes
[2489.40 → 2489.58] me
[2489.58 → 2489.94] happy.
[2490.78 → 2490.96] This
[2490.96 → 2491.16] looks
[2491.16 → 2491.42] really
[2491.42 → 2491.78] good.
[2492.22 → 2492.68] So we
[2492.68 → 2492.82] should
[2492.82 → 2493.22] probably
[2493.22 → 2494.52] explain what
[2494.52 → 2495.44] this is.
[2496.62 → 2497.28] I don't
[2497.28 → 2497.80] think anybody
[2497.80 → 2498.40] has mentioned
[2498.40 → 2498.70] that.
[2499.20 → 2499.62] So this
[2499.62 → 2500.40] is actually
[2500.40 → 2502.48] a command
[2502.48 → 2504.02] line UI
[2504.02 → 2505.14] for Git
[2505.14 → 2506.78] and allows
[2506.78 → 2507.02] you to
[2507.02 → 2507.44] kind of see
[2507.44 → 2507.98] all the
[2507.98 → 2508.66] remote branches
[2508.66 → 2509.70] and the
[2509.70 → 2510.28] branches that
[2510.28 → 2510.64] are there
[2510.64 → 2511.18] and tags
[2511.18 → 2511.68] visually
[2511.68 → 2512.20] and kind
[2512.20 → 2512.58] of like a
[2512.58 → 2512.96] column.
[2513.74 → 2513.96] You can
[2513.96 → 2514.22] kind of
[2514.22 → 2514.62] jump through
[2514.62 → 2515.20] the commits
[2515.20 → 2515.94] and see
[2515.94 → 2516.62] the diffs
[2516.62 → 2517.74] and all
[2517.74 → 2518.18] that good
[2518.18 → 2519.18] stuff just
[2519.18 → 2519.66] from like
[2519.66 → 2520.82] console UI.
[2521.18 → 2522.02] It's actually
[2522.02 → 2523.50] ridiculously cool
[2523.50 → 2524.86] and with it
[2524.86 → 2525.96] just starting
[2525.96 → 2526.48] out like this
[2526.48 → 2526.86] I'm excited
[2526.86 → 2527.40] to see what
[2527.40 → 2527.88] gets added
[2527.88 → 2528.30] later.
[2529.14 → 2529.48] It's got a
[2529.48 → 2530.10] great UI
[2530.10 → 2532.80] and I
[2532.80 → 2533.22] think it's
[2533.22 → 2534.26] going to be
[2534.26 → 2534.64] a pretty
[2534.64 → 2535.84] useful tool
[2535.84 → 2536.94] in my
[2536.94 → 2537.34] toolbox.
[2537.94 → 2538.22] The
[2538.22 → 2538.76] installation
[2538.76 → 2539.50] isn't
[2539.50 → 2540.04] the most
[2540.04 → 2541.34] fun in
[2541.34 → 2542.04] terms of
[2542.04 → 2542.96] Go apps.
[2543.10 → 2543.52] It does
[2543.52 → 2545.00] require CMake
[2545.00 → 2545.56] because you've
[2545.56 → 2546.10] got to build
[2546.10 → 2547.80] libgit2.
[2548.70 → 2551.08] So when
[2551.08 → 2551.54] you go
[2551.54 → 2553.12] get gov
[2553.12 → 2554.00] there's actually
[2554.00 → 2554.32] a make
[2554.32 → 2554.72] file that
[2554.72 → 2555.00] you've got
[2555.00 → 2555.34] to run
[2555.34 → 2557.42] and so
[2557.42 → 2557.84] it works
[2557.84 → 2558.86] wonderfully on
[2558.86 → 2559.30] Mac and
[2559.30 → 2559.66] Linux.
[2560.10 → 2560.82] I'm going
[2560.82 → 2561.36] to bet
[2561.36 → 2561.74] that it
[2561.74 → 2562.22] doesn't work
[2562.22 → 2562.62] so great
[2562.62 → 2563.28] on Windows.
[2564.66 → 2564.92] But this
[2564.92 → 2565.24] is really
[2565.24 → 2565.70] cool.
[2565.70 → 2567.46] I use
[2567.46 → 2569.44] an actual
[2569.44 → 2571.28] GUI tool
[2571.28 → 2571.88] to see
[2571.88 → 2572.90] diffs because
[2572.90 → 2573.86] it's the
[2573.86 → 2574.64] quickest for
[2574.64 → 2574.88] me.
[2575.80 → 2576.40] But you
[2576.40 → 2576.78] can do
[2576.78 → 2577.96] search on
[2577.96 → 2578.66] those tools
[2578.66 → 2579.44] and I see
[2579.44 → 2579.72] that you
[2579.72 → 2580.02] can do
[2580.02 → 2580.60] queries.
[2581.86 → 2582.64] It seems
[2582.64 → 2583.24] like it has
[2583.24 → 2583.90] not only
[2583.90 → 2584.26] you can do
[2584.26 → 2584.92] queries it
[2584.92 → 2585.42] seems that
[2585.42 → 2585.96] it has a
[2585.96 → 2586.16] lot of
[2586.16 → 2586.74] flexibility.
[2588.30 → 2588.66] So that
[2588.66 → 2589.00] is really
[2589.00 → 2589.26] cool.
[2589.68 → 2590.28] I only know
[2590.28 → 2590.50] how to
[2590.50 → 2591.06] query one
[2591.06 → 2591.48] thing is
[2591.48 → 2592.36] like git
[2592.36 → 2593.44] dash
[2593.44 → 2594.54] capital S
[2594.54 → 2595.16] logs.
[2595.70 → 2597.34] It's the
[2597.34 → 2597.60] only thing
[2597.60 → 2597.82] I can
[2597.82 → 2598.22] remember.
[2599.62 → 2600.16] I'm going
[2600.16 → 2600.42] to drop
[2600.42 → 2600.94] a screenshot
[2600.94 → 2601.50] into our
[2601.50 → 2601.84] Slack.
[2601.96 → 2602.28] I just
[2602.28 → 2604.90] ran GRV
[2604.90 → 2606.40] on the
[2606.40 → 2606.96] GOV
[2606.96 → 2607.56] repository
[2607.56 → 2608.66] which is
[2608.66 → 2608.88] kind of
[2608.88 → 2609.32] meta but
[2609.32 → 2609.54] that's
[2609.54 → 2609.80] okay.
[2610.70 → 2612.08] And I'll
[2612.08 → 2612.42] drop a
[2612.42 → 2613.10] screenshot in
[2613.10 → 2613.52] our Slack
[2613.52 → 2613.96] because it's
[2613.96 → 2614.52] so cute.
[2615.56 → 2615.94] It reminds
[2615.94 → 2616.46] me a lot
[2616.46 → 2620.62] of what's
[2620.62 → 2620.96] the mail
[2620.96 → 2621.46] program,
[2621.46 → 2623.34] the Unix
[2623.34 → 2624.00] mail program
[2624.00 → 2624.56] like BUT
[2624.56 → 2625.06] or
[2625.06 → 2628.80] very similar
[2628.80 → 2629.26] to that
[2629.26 → 2629.62] in terms
[2629.62 → 2629.98] of look
[2629.98 → 2630.42] and feel.
[2631.88 → 2632.06] Okay,
[2632.22 → 2632.50] so what
[2632.50 → 2632.82] else we
[2632.82 → 2633.16] have?
[2634.84 → 2634.98] Oh,
[2635.14 → 2635.40] DEP
[2635.40 → 2638.16] 0.3.2
[2638.16 → 2640.00] was also
[2640.00 → 2641.02] released and
[2641.02 → 2641.48] that added
[2641.48 → 2641.90] kind of
[2641.90 → 2642.80] import
[2642.80 → 2643.92] support for
[2643.92 → 2644.94] GPT and
[2644.94 → 2646.34] GB and
[2646.34 → 2646.86] it had some
[2646.86 → 2647.36] other kind
[2647.36 → 2647.64] of bug
[2647.64 → 2648.24] fixes and
[2648.24 → 2648.90] improvements.
[2648.90 → 2649.94] so if you
[2649.94 → 2650.40] are currently
[2650.40 → 2651.06] using DEP
[2651.06 → 2652.08] or we're
[2652.08 → 2652.88] waiting for
[2652.88 → 2653.40] something that
[2653.40 → 2653.84] would auto
[2653.84 → 2654.82] import from
[2654.82 → 2655.46] GVT or
[2655.46 → 2657.06] GB, I
[2657.06 → 2657.48] encourage you
[2657.48 → 2657.70] to play
[2657.70 → 2658.10] with that.
[2659.06 → 2659.52] That's been
[2659.52 → 2660.06] one of the
[2660.06 → 2663.36] best blog
[2663.36 → 2663.88] posts I've
[2663.88 → 2664.38] ever read
[2664.38 → 2665.22] about version
[2665.22 → 2665.88] management.
[2665.88 → 2666.78] of the
[2666.78 → 2667.08] guy.
[2667.08 → 2667.88] Yeah,
[2669.08 → 2669.60] Shane Boyer.
[2670.76 → 2671.50] Or Sam Boyer,
[2671.56 → 2671.70] yeah.
[2672.42 → 2672.76] I don't know why
[2672.76 → 2673.44] I said Shane.
[2674.18 → 2674.62] What is the
[2674.62 → 2675.22] name of the
[2675.22 → 2676.00] blog post?
[2677.76 → 2678.74] So you think
[2678.74 → 2679.14] you want to
[2679.14 → 2679.70] write a version
[2679.70 → 2680.78] management system?
[2681.44 → 2682.10] Something like that.
[2683.24 → 2683.52] Yeah,
[2683.66 → 2684.58] that was very
[2684.58 → 2685.30] well thought
[2685.30 → 2685.84] through and
[2685.84 → 2686.86] very well
[2686.86 → 2688.14] explained.
[2689.02 → 2689.24] Yeah.
[2689.24 → 2690.40] Yeah,
[2690.48 → 2691.06] it definitely
[2691.06 → 2691.62] gives you an
[2691.62 → 2692.62] appreciation for
[2692.62 → 2693.22] the people who
[2693.22 → 2694.02] have to solve
[2694.02 → 2694.84] these dependency
[2694.84 → 2695.50] management
[2695.50 → 2696.20] problems.
[2697.36 → 2697.58] Yeah,
[2697.96 → 2698.42] because it's
[2698.42 → 2698.82] always your
[2698.82 → 2699.30] problem is
[2699.30 → 2699.70] always the
[2699.70 → 2700.32] easy one to
[2700.32 → 2700.62] solve,
[2700.80 → 2700.96] right?
[2701.00 → 2701.44] It's all the
[2701.44 → 2701.90] other ones.
[2705.08 → 2705.90] So the
[2705.90 → 2707.50] last thing I
[2707.50 → 2708.78] have in the
[2708.78 → 2710.88] news and
[2710.88 → 2711.98] projects is
[2711.98 → 2712.64] the latest
[2712.64 → 2713.72] issue of
[2713.72 → 2714.42] Just for Funk
[2714.42 → 2715.40] from Frances.
[2716.08 → 2717.10] Camp Boyer is
[2717.10 → 2717.98] amazing,
[2718.46 → 2718.94] amazing,
[2718.94 → 2719.34] amazing.
[2719.66 → 2720.54] It's got the
[2720.54 → 2721.14] Go Tracer
[2721.14 → 2722.64] in it and
[2722.64 → 2723.32] he walks you
[2723.32 → 2723.64] through how
[2723.64 → 2724.38] to use it
[2724.38 → 2725.60] from start
[2725.60 → 2726.44] to finish and
[2726.44 → 2727.36] it's awesome.
[2727.60 → 2728.00] I love the
[2728.00 → 2728.66] Go Tracer so
[2728.66 → 2729.66] much but
[2729.66 → 2731.30] it's severely
[2731.30 → 2732.38] lacking in
[2732.38 → 2733.00] documentation.
[2734.02 → 2734.64] Severely
[2734.64 → 2735.20] lacking.
[2735.30 → 2735.82] Tell us what
[2735.82 → 2736.50] the Go Tracer
[2736.50 → 2736.94] does.
[2737.70 → 2738.38] I actually
[2738.38 → 2739.04] looked to see
[2739.04 → 2739.70] if that was
[2739.70 → 2740.54] explained anywhere
[2740.54 → 2741.46] and it really
[2741.46 → 2741.92] isn't.
[2742.44 → 2742.96] It isn't.
[2743.02 → 2743.48] Go Tracer
[2743.48 → 2745.08] allows you to
[2745.08 → 2746.60] instrument your
[2746.60 → 2748.00] Go applications
[2748.00 → 2749.44] and capture
[2749.44 → 2753.42] performance metrics
[2753.42 → 2754.84] that you can
[2754.84 → 2755.80] then put
[2755.80 → 2756.46] through
[2756.46 → 2757.86] different
[2757.86 → 2758.76] tracing tools.
[2759.26 → 2759.66] Go Tracer
[2759.66 → 2760.62] is one of
[2760.62 → 2760.86] them.
[2762.32 → 2762.88] And it
[2762.88 → 2763.60] lets you
[2763.60 → 2764.10] see,
[2764.46 → 2765.10] for example,
[2766.26 → 2767.12] what you're
[2767.12 → 2767.64] spending most
[2767.64 → 2768.20] of your CPU
[2768.20 → 2769.18] time on or
[2769.18 → 2769.76] where you're
[2769.76 → 2770.40] allocating the
[2770.40 → 2771.02] most memory.
[2772.14 → 2772.82] The better
[2772.82 → 2773.32] tools are
[2773.32 → 2774.02] visual and
[2774.02 → 2775.08] you can click
[2775.08 → 2775.64] on things
[2775.64 → 2776.08] and find
[2776.08 → 2776.46] out,
[2776.54 → 2777.48] you know,
[2777.56 → 2778.52] because the
[2778.52 → 2778.94] graph is
[2778.94 → 2779.30] bigger,
[2779.86 → 2780.46] this is where
[2780.46 → 2780.94] I'm spending
[2780.94 → 2781.48] more of my
[2781.48 → 2781.88] time and
[2781.88 → 2782.36] you can drill
[2782.36 → 2783.34] in and get
[2783.34 → 2783.72] all the way
[2783.72 → 2784.18] down to the
[2784.18 → 2784.90] function level.
[2785.44 → 2785.60] All right,
[2785.66 → 2786.40] this code
[2786.40 → 2787.30] takes more
[2787.30 → 2787.68] time than
[2787.68 → 2788.34] anything else
[2788.34 → 2789.26] or I'm
[2789.26 → 2789.74] calling this
[2789.74 → 2790.44] one function
[2790.44 → 2791.32] so many
[2791.32 → 2791.90] times that
[2791.90 → 2792.38] it's taking
[2792.38 → 2792.90] all of my
[2792.90 → 2793.64] CPU time.
[2793.80 → 2794.06] So you
[2794.06 → 2794.90] can drill
[2794.90 → 2795.44] into your
[2795.44 → 2796.00] app and
[2796.00 → 2797.34] find performance
[2797.34 → 2798.08] issues that
[2798.08 → 2798.36] way.
[2799.36 → 2799.72] Cool.
[2799.72 → 2801.22] So it's
[2801.22 → 2802.24] a good
[2802.24 → 2802.54] video.
[2802.72 → 2803.70] Go watch
[2803.70 → 2803.86] that.
[2804.46 → 2804.90] I do
[2804.90 → 2805.56] have one
[2805.56 → 2806.40] and I'm
[2806.40 → 2806.58] going to
[2806.58 → 2806.90] get the
[2806.90 → 2807.46] link now,
[2807.94 → 2808.16] but I
[2808.16 → 2808.54] forgot to
[2808.54 → 2809.02] put it on
[2809.02 → 2809.64] the doc.
[2810.52 → 2811.06] Bill
[2811.06 → 2811.48] Kennedy
[2811.48 → 2812.30] came out
[2812.30 → 2812.62] with a
[2812.62 → 2813.40] blog post
[2813.40 → 2814.12] explaining
[2814.12 → 2814.84] channels.
[2816.22 → 2816.90] And if
[2816.90 → 2818.58] you use
[2818.58 → 2819.42] channels but
[2819.42 → 2819.82] you don't
[2819.82 → 2820.68] understand them
[2820.68 → 2821.20] really
[2821.20 → 2822.24] completely,
[2822.92 → 2823.36] or if you
[2823.36 → 2824.06] don't use
[2824.06 → 2824.54] them because
[2824.54 → 2824.96] you don't
[2824.96 → 2825.94] understand how
[2825.94 → 2826.52] they work,
[2827.10 → 2827.62] if you read
[2827.62 → 2828.54] this blog post,
[2828.70 → 2829.44] I promise
[2829.44 → 2830.12] you will.
[2830.90 → 2831.20] It might
[2831.20 → 2831.66] take you a
[2831.66 → 2832.16] while to
[2832.16 → 2832.50] digest
[2832.50 → 2833.02] everything,
[2833.18 → 2833.38] but he
[2833.38 → 2833.96] explains it
[2833.96 → 2834.86] really well.
[2835.70 → 2836.70] He gives
[2836.70 → 2837.30] perfect
[2837.30 → 2839.16] contrasts and
[2839.16 → 2840.20] he speaks
[2840.20 → 2843.54] in a very
[2843.54 → 2844.76] simple language.
[2846.00 → 2847.70] So I
[2847.70 → 2848.26] thought it
[2848.26 → 2848.58] was a
[2848.58 → 2849.40] really great
[2849.40 → 2850.34] public service
[2850.34 → 2851.64] for him to
[2851.64 → 2852.46] do that post.
[2852.56 → 2853.34] And I
[2853.34 → 2853.98] happen to
[2853.98 → 2854.48] know it
[2854.48 → 2855.14] took him a
[2855.14 → 2855.72] month to
[2855.72 → 2856.02] put it
[2856.02 → 2856.38] together.
[2857.08 → 2857.56] It's really
[2857.56 → 2858.10] well done.
[2859.04 → 2859.20] Oh,
[2859.26 → 2859.40] wow.
[2860.00 → 2860.66] I saw it
[2860.66 → 2861.06] come out.
[2861.54 → 2861.92] I haven't
[2861.92 → 2862.22] had the
[2862.22 → 2862.66] chance to
[2862.66 → 2862.94] read it
[2862.94 → 2863.16] yet.
[2863.84 → 2864.44] I'm trying
[2864.44 → 2864.92] to convince
[2864.92 → 2865.54] myself I
[2865.54 → 2865.92] have time
[2865.92 → 2866.34] to code
[2866.34 → 2866.86] right now.
[2869.74 → 2870.18] Okay,
[2870.38 → 2871.70] so are
[2871.70 → 2872.24] we ready
[2872.24 → 2872.74] to move
[2872.74 → 2873.36] into Free
[2873.36 → 2873.58] Software
[2873.58 → 2873.88] Friday?
[2874.40 → 2874.96] Let's do
[2874.96 → 2875.14] it.
[2876.00 → 2876.28] So,
[2876.52 → 2876.74] Ivan,
[2876.82 → 2877.06] I don't
[2877.06 → 2877.34] know whether
[2877.34 → 2877.66] you listen
[2877.66 → 2878.00] to the
[2878.00 → 2878.20] show,
[2878.34 → 2879.22] but basically
[2879.22 → 2879.58] what we
[2879.58 → 2880.58] do every
[2880.58 → 2881.88] week is
[2881.88 → 2882.60] we give
[2882.60 → 2883.20] a shout
[2883.20 → 2883.46] out to
[2883.46 → 2884.26] an OSS
[2884.26 → 2885.52] maintainer
[2885.52 → 2886.40] group or
[2886.40 → 2888.28] project just
[2888.28 → 2888.58] to kind
[2888.58 → 2889.06] show the
[2889.06 → 2889.28] love.
[2889.38 → 2889.64] It does
[2889.64 → 2890.30] not have
[2890.30 → 2890.60] to be
[2890.60 → 2891.08] written in
[2891.08 → 2891.30] Go.
[2892.20 → 2893.14] So anything
[2893.14 → 2893.80] is up in
[2893.80 → 2894.14] the air.
[2894.26 → 2894.86] We often
[2894.86 → 2896.22] give shout
[2896.22 → 2896.62] outs to
[2896.62 → 2897.30] tools and
[2897.30 → 2897.70] things like
[2897.70 → 2898.04] that
[2898.04 → 2898.50] we use.
[2899.30 → 2899.74] Okay.
[2899.74 → 2903.28] I haven't
[2903.28 → 2903.68] given it
[2903.68 → 2904.54] much thought
[2904.54 → 2904.84] though.
[2905.84 → 2906.64] Yeah,
[2906.64 → 2907.06] you don't
[2907.06 → 2907.36] have to
[2907.36 → 2907.58] have
[2907.58 → 2907.98] anything.
[2908.98 → 2909.62] It's just
[2909.62 → 2909.82] fine.
[2909.88 → 2910.24] I'll start.
[2910.68 → 2911.02] I wanted
[2911.02 → 2911.72] to shout
[2911.72 → 2912.06] out to
[2912.06 → 2912.72] Frances
[2912.72 → 2914.58] because the
[2914.58 → 2915.04] work that
[2915.04 → 2915.36] he does
[2915.36 → 2915.66] for the
[2915.66 → 2916.26] Go community
[2916.26 → 2917.24] and the
[2917.24 → 2917.80] effort that
[2917.80 → 2918.20] he puts
[2918.20 → 2918.82] into his
[2918.82 → 2919.70] podcast and
[2919.70 → 2920.18] his blog
[2920.18 → 2921.40] posts and
[2921.40 → 2922.38] his tooling
[2922.38 → 2923.28] and his
[2923.28 → 2924.06] documentation,
[2924.82 → 2926.42] incredible.
[2926.42 → 2927.94] very few
[2927.94 → 2928.46] people work
[2928.46 → 2929.00] that hard.
[2929.60 → 2931.26] São Francisco
[2931.26 → 2932.30] Campos, we
[2932.30 → 2932.96] love you.
[2933.08 → 2933.54] Thank you so
[2933.54 → 2934.34] much for all
[2934.34 → 2934.80] of the things
[2934.80 → 2935.16] that you do
[2935.16 → 2935.54] for the Go
[2935.54 → 2935.98] community.
[2937.00 → 2937.52] Yeah, that
[2937.52 → 2939.44] whole series,
[2939.68 → 2940.00] like everything
[2940.00 → 2940.82] he does is
[2940.82 → 2941.46] amazing.
[2942.52 → 2943.00] Oh my God,
[2943.02 → 2943.30] I couldn't
[2943.30 → 2943.92] agree more.
[2945.20 → 2945.96] One of my
[2945.96 → 2946.40] favourite things
[2946.40 → 2946.78] he did was
[2946.78 → 2947.52] that Go
[2947.52 → 2947.90] tooling
[2947.90 → 2948.78] repository.
[2949.30 → 2950.00] That's just
[2950.00 → 2951.06] so awesome.
[2951.64 → 2952.94] It's like a
[2952.94 → 2953.66] read me with
[2953.66 → 2954.66] all the
[2954.66 → 2955.62] awesome Go
[2955.62 → 2956.06] tools.
[2957.30 → 2958.06] Let's have a
[2958.06 → 2958.72] link on the
[2958.72 → 2959.64] notes for
[2959.64 → 2959.96] sure.
[2960.66 → 2961.04] Looking.
[2963.08 → 2963.78] I don't know
[2963.78 → 2964.32] if I've run
[2964.32 → 2964.84] into that.
[2965.38 → 2965.52] I don't
[2965.52 → 2965.94] remember.
[2967.70 → 2968.36] Galicia, did
[2968.36 → 2968.58] you have
[2968.58 → 2968.94] anybody you
[2968.94 → 2969.50] wanted to
[2969.50 → 2969.96] shout out
[2969.96 → 2970.44] to while he
[2970.44 → 2970.72] pulls up
[2970.72 → 2971.02] the link?
[2972.76 → 2973.38] Well, besides
[2973.38 → 2974.82] seconding what
[2974.82 → 2975.48] Brian just
[2975.48 → 2975.92] said about
[2975.92 → 2976.46] Frances
[2976.46 → 2978.20] Campos, I'm
[2978.20 → 2978.54] going to take
[2978.54 → 2979.30] that lead and
[2979.30 → 2979.74] say the same
[2979.74 → 2980.86] about Bill
[2980.86 → 2981.38] Kennedy,
[2982.42 → 2983.08] William
[2983.08 → 2983.86] Kennedy, but
[2983.86 → 2984.38] we call him
[2984.38 → 2984.72] Bill.
[2985.74 → 2986.42] Just, you
[2986.42 → 2986.96] know, I was
[2986.96 → 2987.72] so inspired by
[2987.72 → 2988.98] the post.
[2989.16 → 2990.02] He just did
[2990.02 → 2991.34] about channels,
[2991.68 → 2992.04] which by the
[2992.04 → 2992.64] way is called
[2992.64 → 2993.68] the behaviour
[2993.68 → 2994.52] of channels.
[2996.08 → 2997.48] He just, you
[2997.48 → 2998.04] know, just by
[2998.04 → 2999.66] doing blog
[2999.66 → 3000.42] posts and
[3000.42 → 3001.30] his tweets
[3001.30 → 3003.76] and little
[3003.76 → 3004.82] big things
[3004.82 → 3005.56] that he does
[3005.56 → 3006.58] all the time.
[3007.06 → 3007.36] And he
[3007.36 → 3008.24] travels a lot
[3008.24 → 3008.94] and does kind
[3008.94 → 3009.32] of free
[3009.32 → 3010.00] workshops.
[3010.86 → 3011.98] things like
[3011.98 → 3012.28] that.
[3012.94 → 3013.12] Yeah.
[3013.56 → 3014.42] He's a big
[3014.42 → 3015.24] support of
[3015.24 → 3015.78] the community.
[3016.50 → 3016.98] He's always
[3016.98 → 3017.28] giving.
[3019.22 → 3020.40] So mine
[3020.40 → 3020.82] for this
[3020.82 → 3022.30] week is
[3022.30 → 3023.26] Gone.
[3023.94 → 3024.78] And if you
[3024.78 → 3025.42] haven't seen
[3025.42 → 3027.64] it, it is
[3027.64 → 3028.80] filled with
[3028.80 → 3030.28] libraries for
[3030.28 → 3030.72] like linear
[3030.72 → 3031.16] algebra,
[3031.46 → 3031.98] statistics,
[3032.22 → 3032.70] probability,
[3033.54 → 3034.48] things like
[3034.48 → 3034.78] that.
[3034.78 → 3035.58] And I'm
[3035.58 → 3036.52] really excited
[3036.52 → 3037.48] to see how
[3037.48 → 3038.82] this progresses.
[3039.70 → 3040.42] It is a
[3040.42 → 3041.16] world I'm
[3041.16 → 3042.54] not as
[3042.54 → 3043.22] smart in.
[3044.46 → 3045.36] So I'm
[3045.36 → 3045.96] glad people
[3045.96 → 3046.96] are writing
[3046.96 → 3047.68] these algorithms
[3047.68 → 3048.34] for me.
[3048.82 → 3049.48] But I'm
[3049.48 → 3050.18] mostly excited
[3050.18 → 3050.68] about it
[3050.68 → 3052.64] because Python
[3052.64 → 3053.58] with the
[3053.58 → 3054.26] NumPy
[3054.26 → 3055.56] library seems
[3055.56 → 3056.58] really to be
[3056.58 → 3057.62] the area that
[3057.62 → 3058.34] people are
[3058.34 → 3059.06] working in
[3059.06 → 3059.46] some of the
[3059.46 → 3060.06] more scientific
[3060.06 → 3061.56] regions.
[3061.56 → 3062.84] So seeing
[3062.84 → 3063.28] these things
[3063.28 → 3064.18] introduced in
[3064.18 → 3066.30] Go makes
[3066.30 → 3066.78] me hopeful
[3066.78 → 3067.12] that we'll
[3067.12 → 3067.66] start seeing
[3067.66 → 3068.20] more of
[3068.20 → 3068.98] those projects
[3068.98 → 3070.92] being completed
[3070.92 → 3071.50] in Go as
[3071.50 → 3071.76] well.
[3072.46 → 3072.68] That would
[3072.68 → 3073.00] be awesome.
[3073.76 → 3074.38] Go is
[3074.38 → 3074.86] growing.
[3076.30 → 3076.92] And look at
[3076.92 → 3077.60] this documentation.
[3078.06 → 3078.92] I love it.
[3080.20 → 3081.12] Pretty awesome.
[3082.32 → 3082.94] Really well
[3082.94 → 3083.42] put together.
[3084.90 → 3086.86] So do we
[3086.86 → 3087.34] have any
[3087.34 → 3087.84] other shoutouts
[3087.84 → 3088.20] we want to
[3088.20 → 3088.48] do?
[3088.94 → 3089.62] If not,
[3089.68 → 3090.36] we can wrap
[3090.36 → 3090.72] this thing
[3090.72 → 3091.52] up and we
[3091.52 → 3092.16] will play
[3092.16 → 3092.76] around with
[3092.76 → 3093.10] some of the
[3093.10 → 3093.68] people in
[3093.68 → 3094.44] the Slack
[3094.44 → 3095.02] for our
[3095.02 → 3095.54] after show.
[3097.00 → 3097.78] Let's tie a
[3097.78 → 3098.24] bow on it.
[3099.40 → 3100.10] All right.
[3101.14 → 3102.82] So definitely
[3102.82 → 3103.24] thank you
[3103.24 → 3103.78] everybody for
[3103.78 → 3104.34] being on the
[3104.34 → 3104.60] show.
[3104.76 → 3105.24] Huge thank
[3105.24 → 3105.94] you to Ivan
[3105.94 → 3106.48] for taking
[3106.48 → 3106.96] time out of
[3106.96 → 3107.30] your busy
[3107.30 → 3108.04] schedule to
[3108.04 → 3108.52] come and
[3108.52 → 3109.14] join us and
[3109.14 → 3109.60] talk about
[3109.60 → 3110.10] all things
[3110.10 → 3110.50] swagger.
[3111.02 → 3111.44] Thank you,
[3111.50 → 3111.70] Ivan.
[3112.30 → 3112.88] Thanks for
[3112.88 → 3113.34] having me.
[3114.32 → 3114.98] And a huge
[3114.98 → 3115.48] thank you to
[3115.48 → 3116.22] all of our
[3116.22 → 3116.64] listeners.
[3116.86 → 3117.14] Definitely
[3117.14 → 3118.18] share the
[3118.18 → 3118.76] show with
[3118.76 → 3119.32] friends,
[3119.46 → 3119.90] co-workers,
[3120.36 → 3120.88] all that
[3120.88 → 3121.40] good stuff.
[3121.80 → 3122.04] You can
[3122.04 → 3122.42] follow us
[3122.42 → 3122.86] on Twitter
[3122.86 → 3123.22] at
[3123.22 → 3124.22] gotimefm.
[3124.88 → 3125.74] If you
[3125.74 → 3126.24] have
[3126.24 → 3127.52] questions for
[3127.52 → 3128.52] the guests
[3128.52 → 3129.64] or hosts
[3129.64 → 3130.64] or you
[3130.64 → 3130.80] want to
[3130.80 → 3130.94] make
[3130.94 → 3131.44] recommendations
[3131.44 → 3132.78] for guests
[3132.78 → 3133.36] or topics,
[3133.66 → 3134.22] please file
[3134.22 → 3134.64] an issue
[3134.64 → 3134.94] at
[3134.94 → 3135.88] GitHub.com
[3135.88 → 3136.30] slash
[3136.30 → 3137.28] gotimefm
[3137.28 → 3137.68] slash
[3137.68 → 3138.08] ping.
[3139.00 → 3139.76] And with
[3139.76 → 3140.20] that,
[3140.42 → 3140.92] goodbye
[3140.92 → 3141.24] everybody.
[3141.34 → 3141.54] We'll see
[3141.54 → 3141.78] you next
[3141.78 → 3142.06] week.
[3143.40 → 3143.94] I just
[3143.94 → 3145.26] like to
[3145.26 → 3145.64] point out
[3145.64 → 3146.18] before we
[3146.18 → 3146.64] go off
[3146.64 → 3147.04] the air
[3147.04 → 3147.96] that the
[3147.96 → 3148.54] holiday season
[3148.54 → 3149.04] is coming.
[3149.04 → 3149.82] You know,
[3149.88 → 3150.58] it's now
[3150.58 → 3151.22] we're recording
[3151.22 → 3151.62] this at the
[3151.62 → 3151.86] end of
[3151.86 → 3152.26] October.
[3152.44 → 3152.70] You'll be
[3152.70 → 3153.48] listening in
[3153.48 → 3153.92] November.
[3154.66 → 3155.58] So remember
[3155.58 → 3156.48] that go time
[3156.48 → 3157.44] is the best
[3157.44 → 3158.04] gift that you
[3158.04 → 3158.66] can give your
[3158.66 → 3159.28] friends and
[3159.28 → 3159.76] your family
[3159.76 → 3160.38] for the
[3160.38 → 3160.68] holidays.
[3161.46 → 3162.62] So just
[3162.62 → 3163.14] keep that in
[3163.14 → 3163.56] mind as the
[3163.56 → 3164.08] holidays come
[3164.08 → 3164.44] close.
[3165.10 → 3165.46] Steal their
[3165.46 → 3165.88] phone,
[3166.64 → 3167.68] subscribe to
[3167.68 → 3168.20] the podcast
[3168.20 → 3168.78] on their
[3168.78 → 3169.74] behalf and
[3169.74 → 3170.10] tell them
[3170.10 → 3170.78] you're welcome.
[3172.38 → 3172.94] Nothing
[3172.94 → 3173.64] says love
[3173.64 → 3174.24] like giving
[3174.24 → 3174.68] the gift
[3174.68 → 3175.32] of go time.
[3176.68 → 3177.00] Goodbye,
[3177.16 → 3177.48] everybody.
[3177.48 → 3180.12] All right,
[3180.14 → 3180.46] that's it
[3180.46 → 3180.78] for this
[3180.78 → 3181.68] episode of
[3181.68 → 3182.20] go time
[3182.20 → 3182.56] tuning in
[3182.56 → 3183.24] live on
[3183.24 → 3184.30] Thursdays at
[3184.30 → 3185.14] 3 p.m.
[3185.52 → 3185.96] U.S.
[3186.10 → 3186.76] Eastern at
[3186.76 → 3187.66] changelog.com
[3187.66 → 3188.40] slash live.
[3188.92 → 3189.12] Join the
[3189.12 → 3189.72] community and
[3189.72 → 3190.22] slack with
[3190.22 → 3190.82] us in real
[3190.82 → 3191.16] time during
[3191.16 → 3191.66] the shows
[3191.66 → 3192.00] at the
[3192.00 → 3193.40] changelog.com
[3193.40 → 3194.08] slash community.
[3194.34 → 3195.08] Follow us on
[3195.08 → 3195.32] Twitter.
[3195.44 → 3196.04] We're at
[3196.04 → 3197.10] go time FM.
[3197.48 → 3198.30] Special thanks
[3198.30 → 3199.10] to Vastly,
[3199.18 → 3199.58] our bandwidth
[3199.58 → 3200.04] partner.
[3200.48 → 3200.66] Head to
[3200.66 → 3201.34] fastly.com
[3201.34 → 3201.86] to learn more.
[3202.42 → 3202.60] Also,
[3202.76 → 3203.06] Linde,
[3203.18 → 3203.58] we host
[3203.58 → 3204.18] everything we
[3204.18 → 3204.74] do on
[3204.74 → 3205.60] Linde servers.
[3206.00 → 3206.20] Head to
[3206.20 → 3206.88] linode.com
[3206.88 → 3207.84] slash changelog.
[3208.28 → 3208.96] Go time is
[3208.96 → 3209.46] edited by
[3209.46 → 3210.34] Jonathan Young blood
[3210.34 → 3210.72] and the
[3210.72 → 3211.28] theme music for
[3211.28 → 3211.92] go time is
[3211.92 → 3212.64] produced by the
[3212.64 → 3213.04] mysterious
[3213.04 → 3213.56] Break master
[3213.56 → 3214.00] Cylinder.
[3214.44 → 3214.84] We'll see you
[3214.84 → 3215.46] again next week.
[3215.76 → 3216.08] Thanks for
[3216.08 → 3216.32] listening.
