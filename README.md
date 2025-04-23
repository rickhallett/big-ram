# Big Ram – Automated Mini-PC Watch-Dog  
*A plain-English tour of what this repo does & how it came to be.*

---

## 1. Why does this exist?

1. **Showcase OpenAI “Deep Research o3” planning**  
   We asked ChatGPT’s new reasoning model to **design an entire coding
   project up-front**.  It produced a build-plan that listed every file,
   dependency, test and commit message in order.  
2. **Turn that plan into a real, self-running tool**  
   The generated code now **checks weekly** for  
   * new BIOS / firmware posts from PC vendors  
   * any UK price swing of ± 5 % for our favourite mini-PCs  
   and writes a simple Markdown report straight into the repo.

---

## 2. How does it work? (Jargon-free)

| Stage | What happens | In everyday words |
|-------|--------------|-------------------|
| **Collect firmware news** | We read each vendor’s RSS feed. | *“Did Beelink or Asus post a new BIOS?”* |
| **Fetch today’s prices** | We open each retailer page and pick out the first “£ …”. | *“How much is the Minisforum box on Amazon right now?”* |
| **Compare with last week** | A little maths flags changes over 5 %. | *“Price dropped 7 % – worth noting!”* |
| **Write the report** | A Markdown template lists new BIOS links and a table of price moves. | *“Here’s a tidy text file you can read on GitHub.”* |
| **Save snapshots** | Today’s prices are stored in a CSV ready for next week’s diff. | *“Remember what things cost so we can spot changes later.”* |

Everything runs in **GitHub Actions** every Wednesday at 06:00 UTC.  
If the report changes, the bot commits:



---

## 3. Using it yourself

| Action | Command |
|--------|---------|
| **Run once locally** | `uv venv .venv --python 3.11 && source .venv/bin/activate`<br>`uv pip sync`<br>`uv run python -m reportgen.cli weekly` |
| **Add / edit models** | Open `models.yaml`; add the model name, OEM RSS url, and retailer links. |
| **Read the latest report** | Open `weekly_report.md` in this repo. |

*No coding tools needed – just edit a YAML file and let GitHub do the work.*

---

## 4. What we learned building it

* **Up-front planning works** – the agent produced a working repo in one afternoon.
* **Quality gates pay off** – every commit was linted, formatted and tested automatically.
* **Small friction points** – we had to:  
  * relax strict type-checks early on  
  * remember to add the virtual-env’s `bin` directory to the Action’s `PATH`.  
  Once fixed, the pipeline is hands-free.

---

## 5. Can I adapt this for my own gadgets?

Absolutely:

1. Fork the repo.  
2. Replace `models.yaml` with your own products & retailers.  
3. Push – the scheduled Action will start writing reports for you.

---

### Credits

*Project boot-strapped by OpenAI’s **o3** reasoning model, refined with a
sprinkle of human patience.*  






See [Reflection](docs/project_reflections.md) for project reflections

# UK Windows Options vs. M4 Mac mini

Welcome to the guide. This series helps you choose the best Windows-based mini-PC or laptop in the UK market, comparing to the base M4 Mac mini, and explaining why specs like RAM and CPU choice matter for heavy multitasking.

## Navigate
- [1. Mini-PC Options](lib/mini-pcs.md)
  _A selection of compact desktop PCs with 32GB RAM available in the UK._
- [2. Laptop Options](lib/laptops.md)
  _Portable powerhouses featuring 32GB RAM for multitasking on the go._
- [3. Direct Comparison](lib/comparison.md)
  _How the Windows options stack up against the base M4 Mac mini spec-for-spec._
- [4. Why Specs Matter on Windows](lib/rationale.md)
  _Explaining the importance of RAM, CPU, NPU, and I/O for heavy Windows usage._
- [BIOS Information](lib/bios.md)
  _Details on BIOS versions and settings._
- [CPU/GPU Roadmap](lib/cpu_gpu_roadmap.md)
  _Information on upcoming processor and graphics technology._
- [Diff Report](lib/diff_report.md)
  _Comparison of changes between different versions or configurations._
- [Performance Tests](lib/perf_test.md)
  _Benchmark results and performance analysis._
- [Price History](lib/price_history.md)
  _Tracking historical pricing for listed models._
- [Specification Sheets](lib/spec_sheets.md)
  _Detailed technical specifications for hardware._
- [Thermal Performance](lib/thermals.md)
  _Analysis of cooling solutions and temperature measurements._