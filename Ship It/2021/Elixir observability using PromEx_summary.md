• Alex Koutmos discusses his work on Elixir projects, including Changelog app optimizations
• PromEx library for Prometheus metrics and Grafana dashboards is introduced
• Features of PromEx include automatic configuration, plugin support, and annotations for deploys
• Discussion on the challenges of manual Prometheus and Grafana setup and how PromEx addresses them
• Alex Koutmos shares his experience with Erlang 24's just-in-time compiler and its potential benefits for Elixir and Phoenix applications
• Elixir OTP 24 performance improvements (30-50% increase)
• PromEx and its integration with Prometheus metrics and Grafana Agent
• Observability pillars: metrics, logs, and traces, and their benefits and trade-offs
• Potential advantages of using events as a single observability data store
• Differences between metrics and logs
• Current limitations of monitoring tools (metrics/logs/traces)
• Potential for unified observability tool or approach
• Benefits of explicit tools for specific purposes vs. one unifying tool
• The role of exemplars in bridging the gap between metrics, traces, and logs
• Challenges of using logs as a source of metrics and performance data
• Log support in PromEx is limited to shipping mechanism
• PromEx uses Grafana Agent for exporting logs to Loki
• Discussion of events and how they are used in Elixir/Erlang ecosystem
• OpenTelemetry implementation for tracing in Elixir/Erlang
• Telemetry library for surfacing internal library events
• PromEx converts telemetry events into Prometheus metrics
• Users can create their own plugins and Grafana dashboards for specific needs
• Integration with Honeycomb for exposing raw events considered but not currently implemented
• Discussion of available plugins for PromEx, including Phoenix, Oban, Ecto, and Broadway
• Plans for updating Changelog.com to Erlang 24, with a live upgrade from Erlang 23
• Expected benefits of upgrading to Erlang 24, including reduced memory usage, improved serialization speed, and lower latency
• Discussion of metrics and monitoring for the upgrade, including Grafana Cloud probes
• Plans for documenting the upgrade process through blog posts and livestreams
• Plans for the weekend: gardening and DIY projects
• Balancing work (PromEx/Erlang) with personal interests/hobbies
• Discussion of DIY skills/experience
• Weather conditions affecting plans (barbecue)
• Importance of documenting work with photos/videos