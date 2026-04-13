**Gerhard Lazy:** Hey, welcome to the show. We have Alex today with us, Alex Outmost. Some of you may know him from Beam Radio, for those that are listening. Elixir - you have Elixir Tips going; tip \#100 landed not long ago, right?

**Alex Outmost:** I do indeed, yeah. And then I'm taking a small hiatus from Twitter tips regarding Elixir; but I will be back into it shortly, don't worry everyone.

**Gerhard Lazy:** Yeah. So Alex has been around the Erlang/Elixir community for some years now; I don't know how many...

**Alex Outmost:** I think it's got to be like six years now. I read NASA Auric's book "Elixir in Action" back in 2015, and I was hooked on the Beam since then. Yeah, I guess since 2015 I've been working on the Beam.

**Gerhard Lazy:** That sounds awesome. So the way I know you, Alex, is from the work that you've been doing on the Changelog app, which happens to be an Elixir/Phoenix/Erlang behind the scenes' app. You've been doing some fantastic optimizations, especially with those N+1 queries. Thank goodness for that, because the website will be much slower without...

**Alex Outmost:** Oh, yeah.

**Gerhard Lazy:** Yeah. And those things didn't happen in a void, right? So you had this amazing library, which you just happen to have; I don't know how many libraries you have, but I'm sure you have a few... But this is prom\_ex, or Prom E-X, as I like to pronounce it, because of that underscore... Prom Ex - can you tell us a bit more about that, what that is, the library?

**Alex Outmost:** \[04:14\] Sure thing. I guess the elevator pitch for Prom Ex is that you drop in this one library, you add it to your application supervision tree, and then you do some slight configuration, kind of like in an Ecto repo, where you slightly configure your repo, you slightly configure your Prom Ex module, and then you say "Hey, I want a metrics plugin for Phoenix, a metrics plugin for Ecto", I also have one for Oban, and Live View... So you kind of pull in whatever plugins you want that are applicable to your project... And then that's literally it. That's all you have to do. And then you have Prometheus metrics for all the plugins that you configured, and then for every plugin that I write that captures Prometheus metrics there's also a corresponding Grafana dashboard that Prom Ex will also upload to Grafana for you if you choose to have Prom Ex do that. That's kind of like an end-to-end solution for monitoring. You can set Prom Ex up and get dashboards and metrics in five minutes.

**Gerhard Lazy:** I really like that part, especially the Grafana dashboards. Sometimes it's just so difficult to integrate it just right, get the correct labels, get the correct things... What happens when there's an update? Then you'd have to update the Grafana dashboard. And the one fascinating thing that Prom Ex - I'm pronouncing it the way you're pronouncing it, Alex; it's your library, so you're the boss here... So Prom Ex - I like how it manages all aspects of metrics, all the way from the Erlang VM, all the metrics, not just Erlang metrics, but as you mentioned, all those libraries, all those components of an Elixir/Phoenix app... And end-to-end, including when you have new deploys.

**Alex Outmost:** Exactly.

**Gerhard Lazy:** I felt those annotations were so sweet, because it basically owns the entire chain. It will annotate your Grafana dashboards when there are deploys. I felt that was amazing. Like, never mind managing them, which is super-cool, you also got annotations as to who deployed, and which commit was deployed. That was so cool.

**Alex Outmost:** Oh, yeah. These have been pain points for me personally probably since like 2017, because I've been using Prometheus and Grafana for some time now... And I feel like every project I was doing the same boilerplate every single time, with the annotations and stuff like that. But even after I set up that boilerplate, I'd still have problems where it's like "Oh, look, a library maintainer updated their Prometheus package" and you've got some slightly different metrics. Now I have to manually know about that and then go pull down their JSON definition for the Grafana dashboard, and then I have to go onto Grafana, copy and paste it... Lo and behold, there's some slight label discrepancies... This churn all the time - there had to have been a better way.

I've been playing around with these ideas for probably a couple of years now. Prom Ex is kind of that materialization of all those ideas. It's slightly opinionated; I feel like a good tool should have some opinions... If those opinions align with the library consumers, that's great. Else, maybe look elsewhere and see if some other solutions fit your problems better.

**Gerhard Lazy:** That's right. I remember your early days - I would say maybe the beginning of Prom Ex, when we were trying to figure out what dashboards are missing, and can we improve them slightly... So I remember us working together, a little bit - it wasn't a massive amount; just enough to make them nice. The integration was really nice. I remember when you added support for custom dashboards, which we do make use of, by the way... So we have some custom dashboards as well, that Prom Ex can upload for you. That was a great feature... So now we store our Grafana Cloud dashboards with the app, and Prom Ex updates them. So we have nice version control going around.

\[07:49\] And you heard that right, we do use Grafana Cloud. We used to run our own Grafana, but then it was much easier to set up Grafana Agent, scrape all the metrics, scrape all the logs from our apps, from all the pods, from everything; we have even the Node Exporter integration in the Grafana Cloud Agent. We ship all those things to Grafana Cloud, Prom Ex handles most of the dashboards for us, which is really cool, and we have that nice integration going from our infrastructure, which is running Kubernetes (implementation detail, I suppose). Furthermore, we have a really nice setup, all version-controlled, and Prom Ex handles a lot of the automation between the Grafana Cloud and our app... Or should I say the other way around - between our app and the Grafana Cloud.

So just to backtrack a little bit, all this was possible -- I think the beginning was the application. So Changelog.com, it's publicly available, freely available source code; it's a Phoenix application. That was an excellent idea, Jerold. I don't want to say it's one of the best ones you've had, but it was a genius idea to do that. It was so good. And what that meant is that we were exposed to this whole ecosystem which is Erlang, Elixir, Phoenix, and there are so many good things happening in it.

So the app, Changelog, is running Phoenix 1.5 right now, Elixir 1.11, but 1.12 came out, so I'm really excited to try that out... And Erlang 23. But as we all know, Erlang 24 got shipped not long ago, and that is an amazing release. What gets you excited about Erlang 24, Alex?

**Alex Outmost:** I think the biggest thing is probably the most obvious one, which is the just-in-time compiler that landed in OTP 24. That has some big promises in store for everyone running Elixir and Phoenix applications. I think a few months ago I was actually playing around with the OTP 24 release and I had a dummy Phoenix app... And I just hit it with an HTTP stress tester. It was a very simple app; I don't even think it had a database backend to it. It was literally just pass some JSON, get a response back. And there were measurable differences between the OTP 24 - I think it was release candidate 1 I was running at the time - and OTP 23. I was pretty impressed that it was just a very simple Hello World style REST endpoint; you still saw some pretty big performance gains.

So I'm really curious to see people taking measurements in production with actual live traffic, and see what the performance characteristics look like for applications with the changeover.

**Gerhard Lazy:** Yeah. I mean, Changelog can definitely benefit from that. It would be great to measure by how much; I think that's one of the plans, to try -- now that OTP 24 is properly out, we had the first patch release land, and we also had just today, a few hours ago, thanks to Twitter and thanks to Alex, ARM support. ARM64 support for OTP 24 with the just-in-time compiler.

So for those that have tried it or would like to try it, and are wondering why, the performance increases between 30% and 50%. So it can be up to 50% faster whatever you're running, just simply by upgrading to 24. And yeah, depending on how it was compiled, how your code was compiled, it could be even higher. So it depends based on which optimizations you're picking up from OTP 24.

Okay, so how would someone using Prom Ex - how would someone figure out what is faster? So you have your app, your Phoenix app or your Elixir app... I'm imagining that Prom Ex works with Elixir as well; I don't have to have Phoenix. Is that right?

**Alex Outmost:** Yeah. And the idea was to decouple the two. Because you might want to grab Prometheus metrics on your application, but maybe it's like a key worker. There's not going to be a Phoenix component there. But as we all know, Prometheus needs to scrape something over HTTP, unless you're using remote write. We'll get into that a little bit later.

So Prom Ex actually does ship with a very lightweight HTTP server, and it'll just serve your metrics for you. So you could very easily run Prom Ex inside of like a key worker, expose that one endpoint and have your Prometheus instance come and scrape it at its regular interval.

**Gerhard Lazy:** Yeah, that's right. And you expose metrics. Just metrics.

**Alex Outmost:** \[12:10\] Yeah, for now it's metrics. Earlier you mentioned Grafana Agent, and the idea is to eventually ship that as part of Prom Ex. It will be like an optional download. So as Prom Ex is starting, if you configure it to push Prometheus metrics, you can have Prom Ex download the agent, get it up and running in a supervision tree... Then you don't even need to have Prom Ex serve up an HTTP server. You can push metrics directly.

I've actually used Grafana's cloud offering. It's quite nice, and it makes the observability story super nice, especially if you're running in Heroku, or Gigalith, places where maybe you don't own the infrastructure end-to-end, and it's tough to have a Prometheus instance scraping your stuff over the public internet. So remote write, Grafana Agent - all super-exciting things, and hopefully coming soon to Prom Ex.

**Gerhard Lazy:** That's fascinating. So this is such an amazing piece of information, which I don't know how I've missed, but I'm glad that you've mentioned this... Because we were thinking a couple of weeks back "How can we run the Changelog app on Render and have all the metrics and all the logs ship to Grafana Cloud, without having to set up something else that scrapes the metrics, and tails the logs, and then forwards them?

So this is super-exciting, because you have metrics already. I feature requesting logs, please, so that we can ship the logs as well using the Grafana Cloud agent, which I know it supports them. And then the only thing remaining would be traces, which by the way, it also supports.

So we have metrics, logs and events. That is a very special trio. Can you tell us a bit more about that, Alex? What are your thoughts on that special trio?

**Gerhard Lazy:** We could start with the abstract, and then we can work down into the technical nitty-gritty. So those three that you mentioned just happen to be the pillars of observability. All three of those are the pillars of observability. It's theorized that if you have all three of these pillars in your app, you've achieved the coveted observability, and all your Sees and your DevOps people in your organization will come and shake your hand, and all will be well in the world.

But jokes aside, the idea is that these three different types of observability tools yield different benefits for your application. So with logs, if you're capturing logs in your applications or your services, you can see in very nitty-gritty detail what's happening on every single request, what's happening if there are errors, if there are warnings, if you're having trouble connecting to other services... You get very fine-grained detail as to what's going on. This is super-awesome, and it's very helpful to have this very in-depth information.

The problem is that you can kind of be inundated by too much information, and it's very difficult to extrapolate higher meaning out of all this nitty-gritty detail. Then, if you've ever run like an ELK Stack and had to administer that, you know the pains of trying to index all this data.

Then you might say "Okay, let's only log what's important", and I'm sure people with production apps have had their DevOps people come to them and say "Hey, let's dial back the logging. It's a little too much, and Elasticsearch is just keeling over."

Then you reach for other tools, like metrics. Metrics eventually find their way into some sort of time series database, and they're usually pretty efficient in comparison to logs, because they're more bounded. You have a measurement, you have a timestamp, and you have some labels associated with it. A little asterisk there, because that kind of depends on what your time series database of choice is. But that's kind of roughly speaking what goes into capturing time series data.

\[15:57\] So given that you've paired down what information you're capturing, you could start a lot more efficiently, and it's a lot easier to query, and you can keep these for way longer periods of time. But the problem is there that you've now traded off high-fidelity logs for explicit metrics that you're capturing over time. Again, a trade-off, and there are different tools for the job, and you kind of reach for what's best at that particular point in time.

And then traces is kind of like a merger of the two, logs and metrics, where you can see how long your application is sitting in different parts of the application; if you're making external service calls, how long are you waiting for those external service calls... If you have something like Into setup, and you can track requests across services, you can see how long it takes to balance across service A, B, C and D, and how long it takes to unroll and go all the way back to the original caller... And then again, you get some metadata associated with those traces, and timestamps, and stuff like that.

Again, all three of these are different tools, they have some overlap, but it's really a matter of picking the best tool for the job. It'd be nice if you have all three of those in your company or application, but in the real world it is tough to get all three of these stood up and running efficiently, and running effectively.

**Gerhard Lazy:** I really like the way you think about this, I have to say... There is something pragmatic about, and something like - you can have this within five minutes... But I also am very wary, because I've been following Charity Majors' Honeycomb and those perspectives for many years, and my understanding is that the only thing you should care about is events. And if you have a data store that understands arbitrarily-wide events, something that can query them just in time, at scale, then you don't have to trade off the cardinality constraints that metrics have, versus the volume of logs that is just too much, and the indexing, and how basically that happens behind the scenes. So the implementation that limits you to how you use those logs.

So I think that perspective is very interesting, and I will definitely follow up on that some more in the context of this show, of Ship It. But I'm also aware of where we are today - and when I say "we", I mean the Changelog app - what we have already set up, and that ideal, which is that everything is an event. I think whether we want to or not, I can see how we are going on the journey, maybe some are more frustrated, others are more enlightened, but I can see how events potentially have the answer to all these things. But right now, the reality is that we still have to make this choice between metrics or logs. Traces as well. They're like separate components. And I think that Grafana Cloud is doing a pretty good job with Cortex, which is a Prometheus that scales, basically, Loki, which is for indexing logs, and it's great to derive insights out of that, and Tempo, which I haven't used yet, which is for traces. But these are the three components in the Grafana Cloud that serve these three different functions.

I think it's very interesting to get to that tool which unifies them all, and Grafana Cloud could be it, but there are others as well. Now, I'm not going to go through all the names, because that's boring, but what is interesting is that we seem to be going in the same direction. And we may argue between ourselves whether the pillars of observability are a thing, or are just a big joke - different perspectives - but I think ultimately what really matters is being able to understand what is happening in your application, or what is happening with your website, or your service, or whatever. Unknown unknowns. I'm not going to open that can of worms... But the point being is "Do you understand what is happening?" It may be imperfect, it may be limited, but do you have at least an idea of where to look, where the problems are?

\[19:59\] And I do know that Prom Ex helped us or helped you with the N+1 queries. It was very obvious "Hey, we have a problem in Ecto, and this is what that problem looks like, and this is how we fix it. And yes, we fixed it. Does Erlang 24 improve things to Erlang 23, and in what way?" And we can answer those questions as well.

So I think that monitoring is not going anywhere, and I think everybody respects it for what it is... But we also are aware that there are better ways, and we should improve this. So with that in mind, where do you see Prom Ex going? What are the hopes and the goals for the project?

**Alex Outmost:** Yeah, sure thing. So I'm gonna first address a couple of points that you've made, and then I'll answer the question.

**Gerhard Lazy:** Sure.

**Alex Outmost:** And this is just my own personal opinion. I don't see everything rolling up into one solution. I just don't think it's feasible at the moment. Like, would it be nice if everything was an event, and we could easily search it, and everything is hunky-dory? I think everyone would agree that yes, that would be great. And I think we've tried this in the past - stuff everything in ELK, write some nice regex expressions, and extrapolate metrics from those regex expressions from your Elasticsearch database. From organizations that have gone down that route, it's extremely painful.

I think for now, for the foreseeable future, having those explicit tools for explicit purposes I think makes sense, just because they're very different problems that are trying to be solved, and trying to have one unifying tool that does all the things I don't think will pan out well.

But I do like the approach that Grafana is taking, and the observability community in general, where they're trying to provide bridges from one pillar to another. A perfect example is exemplars in Prometheus, where your Prometheus metrics can have an exemplar tag on them, and it'll effectively say "Hey, this metric data point is applicable to this trace." And you can kind of jump and say "Okay, something weird is happening here in the metrics. I'm getting a ton of 500's. Let me look at an exemplar for that 500." You can click through, and you can kind of shift your focus from metrics and go to traces, but still have that context of that problem that I was having 500s.

So I like that approach better, where you can bounce between the different pillars of observability, but still have the context of "I'm trying to solve this problem. What is going on at this moment in time?" I like that approach. Again, that's just my personal opinion.

And to that end - and I'll go back to your original question now - I would like to get Prom Ex to a point where it does take into account things like traces, and you could use exemplars... And if Grafana Agent's incorporated into Prom Ex, you could very easily use Syslog and export logs from your application via Syslog to Grafana Agent, and then those find their way to Loki... So I don't want to tailor Prom Ex solely to Grafana, but I do see that Grafana is offering a lot of tooling that is very powerful, and I would love to leverage it. Hopefully that answers the question there.

**Gerhard Lazy:** I think that's a very interesting perspective. I love that.

**Break:** \[23:11\]

**Gerhard Lazy:** That was a fascinating point that you've made, Alex, just before the break, and I would like to dig into it a little bit more. I would like to hear more about Prom Ex, the hopes and goals, because I think there's more to unpack there... But I find it very interesting how the exemplars that you have in metrics, how they link to traces. You've mentioned something very interesting about logs, and how a lot of information can be derived from them if the logs are in the right format.

In our Changelog app, just to give that example, we have a lot of logs - actually, most logs are still in the standard, unstructured format. So you have long lines of text, and that's okay, but that's where the regex are needed, to extract meaning from those lines.

So the thing which I've found to work a lot better, for example Ingress NGINX, which we also run, is to use JSON logging. So we put all the different information, which you can think of them as metrics, in that one very wide event which is the log line.

For example, status 200, how many bytes, how long it took, which was the refer, stuff like that. And that information, when it ends up in Loki, writing Local queries, which are very similar to Promo queries, makes it easy to derive graphs, which we would typically get from metrics, from your logs.

So then the boundaries between metrics and logs are blurry. You don't really know whether "Was this a log, or was this a metric?" Does this really matter? It's what your understanding is from metrics and logs.

So that makes me wonder, how are logs and metrics different if you use logs as JSON, and you have this arbitrarily wide metric, if you wish - because it's a kind of metric, right? You have all these metrics like status, as I said, bytes, time taken - all those are metrics, and they all appear in a single line. So what is the difference then between the metrics that you get in Prometheus, which have a slightly different format, and the value is at the end, and then you have many metrics that you may put together, like for example for samples or summaries... But in logs they're slightly different, and yet the end result is very similar. What are your thoughts on that?

**Alex Outmost:** Yeah, I think in the spirit of just-in-time/JIT, I think that's effectively what we're doing with logs when we try to extrapolate the metrics out of them, is through this event into the ether with a bunch of data associated with it. Maybe we don't know what we want to do with it at the end, but given that that event is in the database, we can extrapolate some metrics out of it. So we're just-in-time kind of getting some metrics out of that log. You could go down that route.

I think that for some scenarios that may be your only option. Let's say you're running an external service, and all it's giving you is structured logs out. There's no way to tie in maybe an agent inside there, or get internal events and hook in your own Prometheus exporter... For some scenarios, that may be your only option. And then I think that's a valid use case. Read the structured logs, and generate some metrics out of them.

But for when you can control those things, I think storing them in a time-series database will be beneficial for the team, because it's less stress on the infrastructure, it'll be far more performant... So that's, again, a bit of a trade-off there as to what route you go down.

**Gerhard Lazy:** That's interesting. Okay. So Prom Ex - big on metrics. Maybe logs? Are you thinking maybe log?

**Alex Outmost:** \[28:07\] Perhaps... I think the extent of the log support out of Prom Ex will be just the shipping mechanism, given that the plan is to have Grafana Agent as part of Prom Ex's optional download. You can target that Grafana Agent for exporting logs to Loki. But I don't think Prom Ex will transform into a library where it also provides structured logging mechanisms. I think there's some good stuff already built into the Elixir logger on that front... But that's not a problem I'd like to tackle in the Prom Ex library.

**Gerhard Lazy:** Okay, that makes sense. What about events?

**Alex Outmost:** So like traces, for example?

**Gerhard Lazy:** I'm thinking events we have from the Erlang library and the Erlang ecosystem. It's very rich, in that it can expose all sorts of events, and I think this is where we are touching on the Open Telemetry and the sort of things that the Erlang and Elixir ecosystem have going for them, which I think is a very good implementation, a very good story around telemetry.

**Alex Outmost:** Yes, yes. So let's rewind a little bit out of Prom Ex and talk about what you're hinting at here... So there are a couple projects in the Elixir and Erlang ecosystem. Open Telemetry as far as I understand right now is an implementation of the Open Telemetry spec. I think it's solely just for tracing. I think even that library, so Open Telemetry, builds upon another Elixir and Erlang library called Telemetry; that lives in a GitHub organization - I think its beam-telemetry. But that library, Telemetry, offers library authors a way to surface internal library events to whoever is using that library. It's completely agnostic for how you structure these things, aside from you capture some measurements associated with that event and some metadata. That's pretty much it.

So every library can surface events, and you as the consumer of that library can say "Okay, I want to pull out these measurements from the event, and maybe this metadata from the event." A perfect example would be the Phoenix web framework will surface an event when it's completed a request, when it's serviced a request. And inside that event it'll have a measurement for how long it took to surface that request, so that'll be your duration... And then the metadata may be the route that the person hit, or the response status code, the length of the response payload etc. And then if you choose to hook on to that telemetry event, you can use all that data. If you don't hook on to that event, it's effectively like a no-op. So you're not losing any performance per se here.

That's effectively how Prom Ex works. All these libraries that I attach to are emitting these telemetry events. I just so happen to hook into all these telemetry events, and then generate Prometheus metrics out of them.

I think the story there in Elixir and Erlang is unique, because the ecosystem has kind of said, "Okay, we're all going to use these foundational building blocks." And I think -- the last time I looked on hex. Pm, I think there were like 140 libraries using telemetry, which means now across the ecosystem we have this ubiquitous language for how do we surface internal events in our libraries... Which is very powerful, because now I don't need to learn how Phoenix exports events, and how Oban exports events, and how Ecto exports events... It's all the same thing; I just need to hook into an ID for what that event is, and I'm off to the races at that point, and I can capture any information that I like.

**Gerhard Lazy:** \[31:45\] That explains why Prom Ex was such a -- I wouldn't say straightforward, but almost like it was obvious how to put it together. It was obvious what users want and need, because you have all these libraries that expose these events; they're there, you can consume them. So Ecto this week, Oban next week... I'm simplifying it, a lot, but roughly, that's how you were able to ship support for all the different libraries, because they all standardized on how they expose events. Is that a fair summary?

**Alex Outmost:** Yeah, that's exactly right. It is quite a bit simplified...

**Gerhard Lazy:** It's an oversimplification, of course.

**Alex Outmost:** Because a lot of times I'll sit down to write a Prom Ex plugin, and as I'm writing plugin, I'm like "Hm, I need some more data here." So I'll make a PR to the library author, and say "Hey, I think we need some additional metadata here, some additional measurements", and then we have to go through that PR cycle, and I have to wait for a new release to get cut, and then I have to make the Grafana dashboard... So there's a good amount of work. But yeah, effectively, that's it - see what events that library emits, hook into them, convert them into meaningful Prometheus metrics, make the Grafana dashboard, and then ship it.

**Gerhard Lazy:** That's a good one, actually. I like that, especially the last part. Especially the ship it parts.

**Alex Outmost:** Yeah, I thought you'd like that.

**Gerhard Lazy:** Okay. So you have all these events... So I'm wondering if - you're ingesting events, you're translating them into metrics... Is there a point where you could just expose those events raw, and then something like for example Honeycomb, which loves events, could just consume them. I think that's how the Honeycomb agent, in some languages, works. They just expose the raw events.

**Alex Outmost:** I'd have to play around with that and see... Some of these events have a lot of metadata associated with them. Again, let's say that Honeycomb is infinitely scalable, and it doesn't take any compute time - yeah, sure thing; just dump a couple of thousand lines of metadata per event into Honeycomb. But yeah, I'd have to play around with Honeycomb specifically to see if that's even possible.

**Gerhard Lazy:** I'm also fascinated by it, because I think the take is very interesting, and I can see the uniqueness, I would like to understand it more, how they make that possible, for sure... And the challenges -- I mean, if they pulled it off, which apparently they have, that's impressive. And I think it takes an understanding of how complicated these layers are, just to understand what a feat that is in itself. So that's interesting...

So we telemetry, we have Prom Ex, you mentioned plugins... Is there anything specific that you would like to add to Prom Ex next, anything that users are maybe asking for, anything that you would like to ship, which you know would be a hit?

**Alex Outmost:** Yeah, so aside from Grafana Agent, which I think some people are excited about...

**Gerhard Lazy:** I am. Big fan. Please...

**Alex Outmost:** \[laughs\] So one thing I forgot to mention was -- so in addition to supporting all these first-party plugins and Grafana dashboards (and you kind of hinted at this before), users of Prom Ex are encouraged to make their own Prom Ex plugins and their own Grafana dashboards... And those plugins and dashboards are treated identical to how the first-party things are. So you're able to upload those dashboards automatically on application unit, your events will be attached automatically... So all those first-party plugins are kind of Gooding the architecture. I wanted to see how easy it was to create plugins and dashboards and have them all kind of co-exist together.

So the idea is that you use Prom Ex for all the shared libraries in the ecosystem, and then you write your own plugins and Grafana dashboards for things that are specific to your business, that obviously are not going to be supported in Prom Ex. So that's one thing I forgot to touch on. And then what was the original question?

**Gerhard Lazy:** I was asking if there are any specific libraries that you are looking to integrate with. And I'm looking at the available plugins list, and I can see which ones are stable. This is, by the way, on github.com/akoutmos/prom\_ex. And there's a list of available plugins. A bunch of them are stable: Phoenix, Oban, Ecto, Phoenix-Bream, and the application... And then some are coming soon, like Broadway, Absinthe... I'm not sure whether I'm pronouncing that correctly...

**Alex Outmost:** Yeah, yeah. Just like the booze.

**Gerhard Lazy:** Right. I don't know... I really don't know.

**Alex Outmost:** \[36:17\] Yeah, me neither.

**Gerhard Lazy:** Okay.

**Alex Outmost:** So Broadway - that plugin is more or less done. I've made some changes to Broadway itself, and those changes were accepted and merged into the Broadway project. I don't think there's been a release cut as of us recording right now. So that plugin is kind of on hold until a release gets cut, and then I can kind of say that Prom Ex depends on this version of Broadway, if you choose to use the Broadway plugin... Because I added some additional telemetry events.

**Gerhard Lazy:** The idea is to get Broadway wrapped up. For those who don't know what Broadway is - it's a really nifty library where you can drop it into your project, and you could read from various queue implementations, and it takes care of a lot of the boilerplate in setting up a concurrent and parallelized worker. So you can read from Rabbit, and you can configure "Hey, I want 100 Beam processes reading from Rabbit at the same time and processing the work from there." I think it supports Rabbit, Kafka, and I think Regis as well.

But yeah, Broadway is on the list... And then Absinthe is on the list after that, because that's the Elixir GraphQL framework. So that seems to be pretty popular. Yeah, after those two are wrapped up, I'm just going to go on hex. Pm, see which one has the most downloads after that, and just -- think of that as a priority queue. Whatever libraries have the most downloads and are the most popular, just make plugins for them, as long as they support telemetry.

**Gerhard Lazy:** That makes so much sense. Of course. The way you put it, it's obvious. What's the most popular? That thing. Okay... Well, that will have the most users and will be the most successful, and people will find it the most useful. So yeah, that makes perfect sense. I like that. Very sensible.

**Break:** \[38:00\]

**Gerhard Lazy:** So one of the things that we wanted to do - I think we were mentioning this towards the beginning of the show... We were saying how Erlang 24 just shipped. It was a few weeks ago, the final 24 release. We have the first patch release... And we wanted to upgrade the Changelog app to use Erlang 24. So here's the plan... By the time you're listening to this, either next day or a few days after, we will be performing a live upgrade on the Changelog.com website, from Erlang 23 to Erlang 24. We have Prom Ex running, we have all the metrics, and we will see live what difference Erlang 24 makes to Changelog.com.

\[39:40\] Prom Ex is obviously instrumental, all the metrics and all the logs get shipped to Grafana Cloud, so that's how we will be observing things, and we will be commenting out what is different, what is better, what is worse. So with that in mind, I'm wondering if there are any assumptions or expectations that we can set ahead of time. What are you thinking, Alex?

**Alex Outmost:** Yeah, so I've been thinking about this for a little while... Because measuring things before and after changes - it just excites me, to see that you've made a change, and you have some measurable differences between how it was before and how it is afterwards. So I've been thinking about this, and some of my hypotheses are that memory usage will go up slightly, because that interpreted code that was compiled to native needs to be stored somewhere. So memory usage will go up slightly... And then I imagine most things CPU-bound will be sped up. So serializing and deserializing from JSON, serializing and deserializing from Postgres database - all these things, we should see a considerable change in performance. Those are kind of top of mind at the moment. How about you?

**Gerhard Lazy:** I'm thinking that the end result that the users will see, because of those serialization speed-ups, is a lower latency. So responses will be quicker. Now, if you have listened to the Changelog 2021 setup, you will know that if you're accessing Changelog, you're going through the CDN. So every single request now goes through Vastly. And what that means is that the responses are already ten times faster, or maybe faster still. So your responses are served within 50 milliseconds; that's what the Grafana Cloud probes are telling us.

So the website is already very fast, because it's served from Vastly. What we will see, however - we have probes that also hit the website directly. So expect the response latency, if you go directly to the backend - or to the origin, as the CDN calls it - it will be slightly lower. I also expect the PostgreSQL - maybe not the queries necessarily, but the responses, as you mentioned, Alex, because of the serialization, to be slightly faster. So I would expect the data from the database to load quicker. And that will also result in quicker response time to the end users.

I'm very curious what happens with context switches. Are we going to have fewer context switches, so less work on the CPU, or more? Obviously context switches are not just like the work the CPU does, but I think things will be a lot less work to do, so fewer context switches. CPU utilization - I think it will go slightly down, but right now we don't have to worry about that because we have 32 CPUs. All the AMD Epics, the latest one - thank you, Linde; those are amazing. Everything is so much quicker. And we have the NVMe SSDs... Everything is super-quick. But yeah, for more, listen to the 2021 Changelog setup where we cover some of these. And I think the blog post will come out.

That's what I expect to see... So will it make a difference for the users? I don't think it will, because they have the CDN. So everything is already super-quick, as fast as it can be. You have TLS optimizations, you have data locality of all the good stuff, because the CDN just serves requests from where you are.

For the logged-in users, because obviously those requests we can't cache, things will be slightly quicker. So for Adam, for Jerold, whoever is working on the admin, those things will be quicker.

Another thing which I do know that we do - we do background processing on some of the S3 files, the logs and stuff like that... So expect those to be quicker. But I don't know by how much. I think we're using Oban for that, aren't we, Alex?

**Alex Outmost:** Yeah, we're using Oban. I think Oban was set up just to send out asynchronous emails. I don't know if there was any other work being done by Oban. But now that you mention those things, we probably should have metrics in place to capture those S3 processing jobs, see how long they take pre and post OTP 24.

**Gerhard Lazy:** Yeah, that's right. That's a perfect one. That'll be a great one to add. Okay, I'm really looking forward to that. And if you've listened to this, you can watch it live. And if you haven't, that's okay; you'll see it on Twitter. We will post. Maybe we'll even do a scheduled livestream. Does that make sense for you, Alex? What do you think?

**Alex Outmost:** Yeah, it works for me.

**Gerhard Lazy:** \[44:06\] Okay. So no impromptu. We'll schedule it, and we'll say "On this time, at this day, at this hour." Okay, I like that. That's a great idea, actually. So we'll have like at least a few days of heads up, and then you can listen to this, and then you can watch that, how we do it. Great. That makes me very excited. Okay.

So we're approaching the end, and I think we need to end on a high... Because it's Friday when we're recording this, it was a good week, and the weekend is just around the corner... So what do you have planned for this weekend, Alex? Anything fun?

**Alex Outmost:** This weekend... I think I have one thing I want to do in Prom Ex, but then I'll be building a garden. So I'll be outdoors, using the table saw, and the meter saw, and the nail gun, and putting together some nice garden beds.

**Gerhard Lazy:** Okay, well that sounds amazing. You have to balance all the Prom Ex and all the Erlang/Elixir work somehow, right?

**Alex Outmost:** Oh, yeah. You need to find a healthy balance between open source work, the full-time job, and a little bit of fun for yourself.

**Gerhard Lazy:** Yeah, that's for sure. So building a garden - that sounds amazing. You must be either very good or very brave, I'm not sure which one. Either a great Diver, or very brave, you'll figure it out. Which one is it?

**Alex Outmost:** I don't want to be arrogant or anything, but I think I'm a decent Diver. I also used to tinker around with cars quite a bit before I had a family... When it was okay to financially irresponsible and buy a $3,000 motor just because I felt like it. Nowadays, you can't do that... \[laughter\]

**Gerhard Lazy:** Okay, different times... Right?

**Alex Outmost:** Yeah, exactly.

**Gerhard Lazy:** Different world.

**Alex Outmost:** I could buy a motorcycle anytime I wanted to. I didn't have to worry about providing for my kiddos. I go with safe hobbies, like building garden beds or doing some woodworking.

**Gerhard Lazy:** Okay, that sounds great. So I hope the weather is going to be great, because for me, the weather has been rubbish for the whole week. Windy... I wouldn't say it's cold, but it's not nice; it's been raining all day every day, we had some downpours as well... So it hasn't been really great. And right now I'm looking at it like -- I was going to do a barbecue; I love barbecuing, the proper charcoal one... But the weather is not good. Maybe we get the parasol out, so it doesn't rain on my barbecue regardless, maybe... I don't know. But what we have to do is post the pictures. Because how can people appreciate how good of a Diver you actually are if they don't see your work?

**Alex Outmost:** Well played, sir. Well played. I'll have to take some selfies. I usually stray from the selfies... \[laughs\]

**Gerhard Lazy:** And videos. Those are very important, because if you don't take videos, someone else could be doing the work and you just take pictures. No... That would never happen, right? Only in movies. \[laughter\]

**Alex Outmost:** Never, never.

**Gerhard Lazy:** Alright, Alex. Well, it's been a pleasure to have you on the show. I really enjoyed this. I'm looking forward to doing what we said we will do. That's super exciting. Shipping Erlang 24 for Changelog.com - that'll be great. And which version of Prom Ex are we at now? Do you know which one is the latest?

**Alex Outmost:** I don't remember... I think 1.1.0 is the latest... And I think the Changelog is on 1.0.1.

**Gerhard Lazy:** Right. So not that far behind, but...

**Alex Outmost:** Yeah, we'll bump it up.

**Gerhard Lazy:** That's great, okay. So we shipped that. That is exciting. Ship a garden in the meantime as well; maybe a barbecue. We'll see. This has been tremendous fun. Thank you, Alex. Looking forward to the next time.

**Alex Outmost:** Likewise, thank you.
