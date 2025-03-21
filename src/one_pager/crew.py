from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import BraveSearchTool, ScrapeWebsiteTool, FileWriterTool

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


# Initiate the BraveSearchTool
brave_search_tool = BraveSearchTool()
scrape_website_tool = ScrapeWebsiteTool()
file_writer_tool = FileWriterTool()

@CrewBase
class OnePager():
	"""OnePager crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools

	@agent
	def question_designer(self) -> Agent:
		return Agent(
			config=self.agents_config['question_designer'],
			verbose=True
		)

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			tools=[brave_search_tool],
			verbose=True
		)

	@agent
	def web_scraper(self) -> Agent:
		return Agent(
			config=self.agents_config['web_scraper'],
			tools=[scrape_website_tool],
			verbose=True
		)

	@agent
	def insight_generator(self) -> Agent:
		return Agent(
			config=self.agents_config['insight_generator'],
			verbose=True
		)
	
	@agent
	def question_designer2(self) -> Agent:
		return Agent(
			config=self.agents_config['question_designer2'],
			verbose=True
		)
	
	@agent
	def researcher2(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher2'],
			tools=[brave_search_tool],
			verbose=True
		)

	@agent 
	def web_scraper2(self) -> Agent:
		return Agent(
			config=self.agents_config['web_scraper2'],
			verbose=True
		)
	
	@agent
	def insight_generator2(self) -> Agent:
		return Agent(
			config=self.agents_config['insight_generator2'],
			verbose=True
		)
	
	# @agent
	# def writer(self) -> Agent:
	# 	return Agent(
	# 		config=self.agents_config['writer'],
	# 		verbose=True
	# 	)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			tools=[file_writer_tool],
			verbose=True
		)

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def question_design_task(self) -> Task:
		return Task(
			config=self.tasks_config['question_design'],
		)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
		)

	@task
	def web_scraping_task(self) -> Task:
		return Task(
			config=self.tasks_config['web_scraping_task'],
		)

	# @task
	# def writing_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['writing_task']		
	# 		)
	
	@task
	def insight_generation_task(self) -> Task:
		return Task(
			config=self.tasks_config['insight_generation_task'],
		)
	
	@task
	def question_design_task2(self) -> Task:
		return Task(
			config=self.tasks_config['question_design_task2'],
		)
	
	@task
	def research_task2(self) -> Task:
		return Task(
			config=self.tasks_config['research_task2'],
		)

	@task
	def web_scraping_task2(self) -> Task:
		return Task(
			config=self.tasks_config['web_scraping_task2'],
		)
	
	@task
	def insight_generation_task2(self) -> Task:
		return Task(
			config=self.tasks_config['insight_generation_task2'],
		)	
	

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task'],
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the OnePager crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			# manager_llm="ollama/llama3.1",
			# process=Process.hierarchical,
			# planning=True,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
