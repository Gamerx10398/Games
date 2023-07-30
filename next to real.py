import random

class Employee:
    def __init__(self, name, salary, specialization):
        self.name = name
        self.salary = salary
        self.specialization = specialization
        self.age = 25
        self.skill = 0.5
        self.performance = 0.5
        self.morale = 0.5

    def improve_skill(self):
        self.skill = min(1, self.skill + 0.1)

    def boost_morale(self):
        self.morale = min(1, self.morale + 0.1)

    def decrease_morale(self):
        self.morale = max(0, self.morale - 0.1)

class Upgrade:
    def __init__(self, name):
        self.name = name
        self.level = 1

class Company:
    def __init__(self, name):
        self.name = name
        self.cash = 1000
        self.employees = []
        self.upgrades = {
            "Productivity": Upgrade("Productivity"),
            "Office Expansion": Upgrade("Office Expansion"),
            "Marketing": Upgrade("Marketing"),
            "Automation": Upgrade("Automation"),
            "Research and Development": Upgrade("Research and Development"),
            "Employee Training Program": Upgrade("Employee Training Program"),
            "Product Development": Upgrade("Product Development"),
            "Employee Benefits": Upgrade("Employee Benefits"),
            "Outsourcing": Upgrade("Outsourcing"),
            "Diversification": Upgrade("Diversification"),
            "Corporate Social Responsibility": Upgrade("Corporate Social Responsibility"),
            "Advanced Automation": Upgrade("Advanced Automation"),
            "International Expansion": Upgrade("International Expansion"),
            "Innovation Lab": Upgrade("Innovation Lab"),
            "Mergers and Acquisitions": Upgrade("Mergers and Acquisitions"),
            "Employee Motivation Program": Upgrade("Employee Motivation Program"),
            "Company Expansion": Upgrade("Company Expansion"),
            "Employee Training Efficiency": Upgrade("Employee Training Efficiency"),
            "Profit Optimization": Upgrade("Profit Optimization"),
            "Employee Wellness Program": Upgrade("Employee Wellness Program"),
            "Luxurious Office Space": Upgrade("Luxurious Office Space"),
            "Efficient Hiring": Upgrade("Efficient Hiring"),
            "Employee Loyalty Program": Upgrade("Employee Loyalty Program"),
            "Cash Generation Boost": Upgrade("Cash Generation Boost"),
            "Employee Training Automation": Upgrade("Employee Training Automation"),
            "Employee Mental Health Initiatives": Upgrade("Employee Mental Health Initiatives"),
            "Employee Productivity Tracking": Upgrade("Employee Productivity Tracking"),
            "Skill Development Opportunities": Upgrade("Skill Development Opportunities"),
            "Employee Time Off Policy": Upgrade("Employee Time Off Policy"),
            "Employee Skill Degradation": Upgrade("Employee Skill Degradation"),
            "Employee Retirement Planning": Upgrade("Employee Retirement Planning"),
            "Employee Disciplinary Actions": Upgrade("Employee Disciplinary Actions"),
            "Employee Work-Life Balance Programs": Upgrade("Employee Work-Life Balance Programs"),
            "Employee Skill Transfer Program": Upgrade("Employee Skill Transfer Program"),
            "Employee Skill Specialization": Upgrade("Employee Skill Specialization"),
            "Employee Health Checkups": Upgrade("Employee Health Checkups"),
            "Employee Stress Management": Upgrade("Employee Stress Management"),
            "Employee Parental Leave Policy": Upgrade("Employee Parental Leave Policy"),
            "Employee Onboarding Program": Upgrade("Employee Onboarding Program"),
            "Employee Offboarding Program": Upgrade("Employee Offboarding Program"),
            "Employee Stock Ownership Program": Upgrade("Employee Stock Ownership Program"),
            "Employee Sabbaticals": Upgrade("Employee Sabbaticals"),
            "Employee Mentorship Program": Upgrade("Employee Mentorship Program"),
            "Employee Surveys": Upgrade("Employee Surveys"),
            "Employee Reward System": Upgrade("Employee Reward System"),
            "Team Building Activities": Upgrade("Team Building Activities"),
            "Employee Cross Training": Upgrade("Employee Cross Training"),
            "Employee Suggestion Program": Upgrade("Employee Suggestion Program"),
            "Manager Mentorship Program": Upgrade("Manager Mentorship Program"),
            "Educational Assistance Program": Upgrade("Educational Assistance Program"),
            "Company Retreats": Upgrade("Company Retreats"),
            "Employee Training Evaluation": Upgrade("Employee Training Evaluation"),
            "Employee Focus Groups": Upgrade("Employee Focus Groups"),
            "Employee Professional Development Program": Upgrade("Employee Professional Development Program"),
            "Employee Side Projects Support": Upgrade("Employee Side Projects Support"),
            "Employee Counseling Services": Upgrade("Employee Counseling Services"),
            "Employee Skill Assessment": Upgrade("Employee Skill Assessment"),
            "Employee Innovation Program": Upgrade("Employee Innovation Program"),
            "Employee Support Groups": Upgrade("Employee Support Groups"),
            "Employee Mobility Program": Upgrade("Employee Mobility Program"),
            "Ergonomic Workstations": Upgrade("Ergonomic Workstations"),
            "Employee Mentorship": Upgrade("Employee Mentorship"),
            "Employee Idea Evaluation System": Upgrade("Employee Idea Evaluation System"),
            "Employee Wellbeing Benefits": Upgrade("Employee Wellbeing Benefits"),
            "Employee Feedback Loop": Upgrade("Employee Feedback Loop"),
            "Employee Skill Certification Program": Upgrade("Employee Skill Certification Program"),
            "Employee Team Collaboration Initiatives": Upgrade("Employee Team Collaboration Initiatives"),
            "Employee Wellness Resources": Upgrade("Employee Wellness Resources"),
            "Employee Career Fairs": Upgrade("Employee Career Fairs"),
            "Employee Leadership Training": Upgrade("Employee Leadership Training"),
            "Employee Resilience Program": Upgrade("Employee Resilience Program"),
            "Employee Healthcare Benefits": Upgrade("Employee Healthcare Benefits"),
            "Employee Stock Options": Upgrade("Employee Stock Options"),
            "Employee Exit Interviews": Upgrade("Employee Exit Interviews"),
            "Employee Safety Program": Upgrade("Employee Safety Program"),
            "Employee Fitness Initiatives": Upgrade("Employee Fitness Initiatives"),
            "Employee Innovation Challenge": Upgrade("Employee Innovation Challenge"),
            "Employee Workload Evaluation": Upgrade("Employee Workload Evaluation"),
            "Employee Fitness Facilities": Upgrade("Employee Fitness Facilities"),
            "Employee Job Rotation": Upgrade("Employee Job Rotation"),
            "Employee Stock Purchase Plan": Upgrade("Employee Stock Purchase Plan"),
            100: Upgrade(1),
        }

    def hire_employee(self, employee):
        hiring_cost = (200 / self.upgrades["Efficient Hiring"].level) + (200 * 18 / 100)
        if self.cash >= hiring_cost:
            self.cash -= hiring_cost
            self.employees.append(employee)
            print(f"{employee.name} has been hired!")
        else:
            print("Insufficient funds to hire an employee.")

    def fire_employee(self, employee):
        if random.random() > 0.1 * self.upgrades["Employee Loyalty Program"].level:
            self.employees.remove(employee)
            print(f"{employee.name} has been fired.")
        else:
            print(f"{employee.name} refused to leave the company!")

    def make_money(self):
        # Generate some random profit for the company based on upgrades and number of employees
        base_profit = random.randint(50, 200) * self.upgrades["Productivity"].level * len(self.employees) * self.upgrades["Product Development"].level
        profit = base_profit * self.upgrades["Marketing"].level * self.upgrades["Automation"].level * self.upgrades["Research and Development"].level * self.upgrades["Employee Benefits"].level * self.upgrades["Diversification"].level * self.upgrades["Corporate Social Responsibility"].level * self.upgrades["Advanced Automation"].level * self.upgrades["International Expansion"].level * self.upgrades["Innovation Lab"].level * self.upgrades["Mergers and Acquisitions"].level * self.upgrades["Employee Motivation Program"].level * self.upgrades["Company Expansion"].level * self.upgrades["Profit Optimization"].level
        self.cash += profit * self.upgrades["Cash Generation Boost"].level
        return profit

    def purchase_upgrade(self, upgrade_name, cost, increase):
        if self.cash >= cost:
            self.cash -= cost
            self.upgrades[upgrade_name].level += increase
            print(f"{upgrade_name} upgrade purchased!")
        else:
            print("Insufficient funds to purchase the upgrade.")

    def conduct_market_research(self):
        # Conduct market research to gain insights into the industry
        for employee in self.employees:
            if employee.specialization == "Market Research":
                if random.random() < 0.2:
                    self.upgrades["Productivity"].level += 1
                    self.upgrades["Marketing"].level += 1
                    print("Market research led to productivity and marketing improvements.")
                    break

    def stock_trading(self):
        # Engage in stock trading to potentially earn additional profits
        stock_price_change = random.randint(-50, 50) / 100
        self.cash *= (1 + stock_price_change)
        print(f"Stock trading resulted in a cash change of {stock_price_change:.2%}.")

    def establish_employee_resource_group(self):
        # Establish employee resource groups for diversity and inclusion
        if self.upgrades[61].level > 1:
            for employee in self.employees:
                if random.random() < (0.05 * self.upgrades[61].level):
                    print(f"{employee.name} participated in an employee resource group.")
                    employee.boost_morale()

    def encourage_employee_volunteering(self):
        # Encourage employees to participate in volunteering activities
        for employee in self.employees:
            if random.random() < 0.1:
                print(f"{employee.name} volunteered for a charitable cause.")
                employee.boost_morale()

    def conduct_employee_surveys(self):
        # Conduct employee surveys to gather feedback and suggestions
        for employee in self.employees:
            if random.random() < 0.1:
                print(f"{employee.name} participated in an employee survey.")
                if employee.morale > 0.5:
                    employee.performance = min(1, employee.performance + 0.1)
                else:
                    employee.performance = max(0, employee.performance - 0.1)

    def implement_employee_reward_system(self):
        # Implement an employee reward system to acknowledge outstanding contributions
        for employee in self.employees:
            if random.random() < (0.05 * self.upgrades[63].level):
                print(f"{employee.name} received a reward for their outstanding work.")
                employee.boost_morale()

    def organize_team_building_activities(self):
        # Organize team-building activities for improved collaboration
        for employee in self.employees:
            if random.random() < 0.1:
                print(f"{employee.name} participated in a team-building activity.")
                employee.boost_morale()

    def promote_employee_cross_training(self):
        # Promote employee cross-training for skill diversity
        for employee in self.employees:
            if random.random() < 0.1:
                employee.improve_skill()
                employee.boost_morale()

    def implement_employee_suggestion_program(self):
        # Implement an employee suggestion program to foster innovation
        for employee in self.employees:
            if random.random() < (0.05 * self.upgrades[66].level):
                employee.boost_morale()

    def establish_mentorship_program_for_managers(self):
        # Establish a mentorship program for managers to enhance leadership skills
        for employee in self.employees:
            if employee.position == "Manager" and random.random() < 0.1:
                employee.improve_skill()
                employee.boost_morale()

    def offer_educational_assistance(self):
        # Offer educational assistance for employees pursuing further studies
        for employee in self.employees:
            if random.random() < 0.1 and employee.age >= 25:
                print(f"{employee.name} received educational assistance.")
                employee.boost_morale()

    def organize_company_retreats(self):
        # Organize company retreats for team bonding and rejuvenation
        for employee in self.employees:
            if random.random() < 0.1:
                print(f"{employee.name} attended a company retreat.")
                employee.boost_morale()

    def implement_employee_training_evaluation(self):
        # Implement evaluations to measure the effectiveness of employee training
        for employee in self.employees:
            if random.random() < 0.1:
                print(f"{employee.name}'s training was evaluated.")
                if employee.morale > 0.5:
                    employee.performance = min(1, employee.performance + 0.1)
                else:
                    employee.performance = max(0, employee.performance - 0.1)

    def conduct_employee_focus_groups(self):
        # Conduct employee focus groups for in-depth discussions on company improvements
        for employee in self.employees:
            if random.random() < 0.1:
                print(f"{employee.name} participated in a focus group discussion.")
                employee.boost_morale()

    def implement_employee_professional_development_program(self):
        # Implement a program for employees' professional growth and career advancement
        for employee in self.employees:
            if random.random() < (0.05 * self.upgrades[72].level):
                employee.improve_skill()
                employee.boost_morale()

    def support_employee_side_projects(self):
        # Support employees in pursuing side projects to foster innovation
        for employee in self.employees:
            if random.random() < (0.05 * self.upgrades[73].level):
                employee.improve_skill()
                employee.boost_morale()

    def provide_employee_counseling_services(self):
        # Provide counseling services to employees for mental health support
        for employee in self.employees:
            if random.random() < 0.1:
                print(f"{employee.name} received counseling services.")
                employee.boost_morale()

    def implement_employee_skill_assessment(self):
        # Implement regular skill assessments to identify skill gaps and strengths
        for employee in self.employees:
            if random.random() < (0.05 * self.upgrades[75].level):
                print(f"{employee.name}'s skills were assessed.")
                if employee.morale > 0.5:
                    employee.performance = min(1, employee.performance + 0.1)
                else:
                    employee.performance = max(0, employee.performance - 0.1)

    def establish_employee_innovation_program(self):
        # Establish an innovation program to encourage employees' creative ideas
        for employee in self.employees:
            if random.random() < 0.1:
                print(f"{employee.name} participated in an innovation program.")
                employee.boost_morale()

    def organize_employee_support_groups(self):
        # Organize support groups to help employees cope with challenges and stress
        for employee in self.employees:
            if random.random() < 0.1:
                print(f"{employee.name} participated in a support group.")
                employee.boost_morale()

    def implement_employee_mobility_program(self):
        # Implement a program to provide mobility opportunities for employees' growth
        for employee in self.employees:
            if random.random() < (0.05 * self.upgrades[79].level):
                print(f"{employee.name} participated in a mobility program.")
                employee.boost_morale()

    def provide_ergonomic_workstations(self):
        # Provide ergonomic workstations for employee comfort and health
        for employee in self.employees:
            if random.random() < (0.05 * self.upgrades[80].level):
                print(f"{employee.name} received an ergonomic workstation.")
                employee.boost_morale()

    def implement_employee_mentorship(self):
        # Implement a mentorship program for employees' personal and professional growth
        for employee in self.employees:
            if random.random() < 0.1:
                print(f"{employee.name} participated in a mentorship program.")
                employee.boost_morale()

    def establish_employee_idea_evaluation_system(self):
        # Establish an idea evaluation system to evaluate and implement employee ideas
        for employee in self.employees:
            if random.random() < (0.05 * self.upgrades[82].level):
                employee.boost_morale()

    def provide_employee_wellbeing_benefits(self):
        # Provide comprehensive wellbeing benefits for employees' physical and mental health
        for employee in self.employees:
            if random.random() < 0.1:
                print(f"{employee.name} received wellbeing benefits.")
                employee.boost_morale()

    def establish_employee_feedback_loop(self):
        # Establish a feedback loop to address employee concerns and suggestions
        for employee in self.employees:
            if random.random() < 0.1:
                print(f"{employee.name}'s feedback was addressed.")
                employee.boost_morale()

    def implement_employee_skill_certification_program(self):
        # Implement a skill certification program for employees' expertise validation
        for employee in self.employees:
            if random.random() < (0.05 * self.upgrades[85].level):
                employee.improve_skill()
                employee.boost_morale()

    def encourage_employee_team_collaboration(self):
        # Encourage team collaboration and coordination for better outcomes
        for employee in self.employees:
            if random.random() < 0.1:
                employee.boost_morale()

    def provide_employee_wellness_resources(self):
        # Provide wellness resources to employees for a healthy work-life balance
        for employee in self.employees:
            if random.random() < 0.1:
                print(f"{employee.name} received wellness resources.")
                employee.boost_morale()

    def organize_employee_career_fair(self):
        # Organize career fairs for employees to explore internal opportunities
        for employee in self.employees:
            if random.random() < (0.05 * self.upgrades[88].level):
                print(f"{employee.name} attended a career fair.")
                employee.boost_morale()

    def implement_employee_leadership_training(self):
        # Implement leadership training programs for aspiring managers
        for employee in self.employees:
            if employee.age >= 30 and random.random() < 0.1:
                employee.improve_skill()
                employee.boost_morale()

    def establish_employee_resilience_program(self):
        # Establish a resilience program to help employees cope with challenges
        for employee in self.employees:
            if random.random() < 0.1:
                print(f"{employee.name} participated in a resilience program.")
                employee.boost_morale()

    def provide_employee_healthcare_benefits(self):
        # Provide comprehensive healthcare benefits for employees
        for employee in self.employees:
            if random.random() < 0.1:
                print(f"{employee.name} received healthcare benefits.")
                employee.boost_morale()

    def offer_employee_stock_options(self):
        # Offer employee stock options as part of their compensation
        for employee in self.employees:
            if random.random() < (0.05 * self.upgrades[91].level):
                print(f"{employee.name} received employee stock options.")
                employee.boost_morale()

    def conduct_exit_interviews(self):
        # Conduct exit interviews to gather feedback from departing employees
        for employee in self.employees:
            if random.random() < 0.1 and employee.morale < 0.3:
                print(f"{employee.name} participated in an exit interview.")
                self.employees.remove(employee)

    def implement_employee_safety_program(self):
        # Implement an employee safety program to ensure a safe work environment
        for employee in self.employees:
            if random.random() < (0.05 * self.upgrades[93].level):
                employee.boost_morale()

    def encourage_employee_fitness(self):
        # Encourage employees to engage in fitness activities for their well-being
        for employee in self.employees:
            if random.random() < 0.1:
                print(f"{employee.name} participated in a fitness challenge.")
                employee.boost_morale()

    def establish_employee_innovation_challenge(self):
        # Establish an innovation challenge to promote creativity and ideas
        if self.upgrades[95].level > 1:
            for employee in self.employees:
                if random.random() < (0.05 * self.upgrades[95].level):
                    print(f"{employee.name} participated in an innovation challenge.")
                    employee.boost_morale()

    def implement_employee_workload_evaluation(self):
        # Implement workload evaluations to ensure a balanced workload for employees
        for employee in self.employees:
            if random.random() < 0.1:
                print(f"{employee.name}'s workload was evaluated.")
                employee.boost_morale()

    def provide_employee_fitness_facilities(self):
        # Provide fitness facilities and resources for employee well-being
        for employee in self.employees:
            if random.random() < (0.05 * self.upgrades[98].level):
                print(f"{employee.name} received fitness facilities.")
                employee.boost_morale()

    def implement_employee_mentorship_program(self):
        # Implement a mentorship program for employee growth and development
        for employee in self.employees:
            if random.random() < 0.1:
                print(f"{employee.name} participated in a mentorship program.")
                employee.boost_morale()

    def establish_employee_art_and_culture_program(self):
        # Establish an art and culture program to promote creativity and cultural awareness
        if self.upgrades[100].level > 1:
            for employee in self.employees:
                if random.random() < (0.05 * self.upgrades[100].level):
                    print(f"{employee.name} participated in an art and culture program.")
                    employee.boost_morale()

def main():
    print("Welcome to Company Tycoon!")
    company_name = input("Enter your company's name: ")
    player_company = Company(company_name)

    while True:
        print("\n--- Menu ---")
        print("1. Hire an Employee")
        print("2. Fire an Employee")
        print("3. View Employees")
        print("4. Make Money")
        print("5. Purchase Upgrades")
        print("6. Check Company's Cash")
        print("7. Conduct Market Research")
        print("8. Stock Trading")
        print("9. Establish Employee Resource Group")
        print("10. Encourage Employee Volunteering")
        print("11. Conduct Employee Surveys")
        print("12. Implement Employee Reward System")
        print("13. Organize Team Building Activities")
        print("14. Promote Employee Cross Training")
        print("15. Implement Employee Suggestion Program")
        print("16. Establish Mentorship Program for Managers")
        print("17. Offer Educational Assistance")
        print("18. Organize Company Retreats")
        print("19. Implement Employee Training Evaluation")
        print("20. Conduct Employee Focus Groups")
        print("21. Implement Employee Professional Development Program")
        print("22. Support Employee Side Projects")
        print("23. Provide Employee Counseling Services")
        print("24. Implement Employee Skill Assessment")
        print("25. Establish Employee Innovation Program")
        print("26. Organize Employee Support Groups")
        print("27. Implement Employee Mobility Program")
        print("28. Provide Ergonomic Workstations")
        print("29. Implement Employee Mentorship")
        print("30. Establish Employee Idea Evaluation System")
        print("31. Provide Employee Wellbeing Benefits")
        print("32. Establish Employee Feedback Loop")
        print("33. Implement Employee Skill Certification Program")
        print("34. Encourage Employee Team Collaboration")
        print("35. Provide Employee Wellness Resources")
        print("36. Organize Employee Career Fair")
        print("37. Implement Employee Leadership Training")
        print("38. Establish Employee Resilience Program")
        print("39. Provide Employee Healthcare Benefits")
        print("40. Offer Employee Stock Options")
        print("41. Conduct Exit Interviews")
        print("42. Implement Employee Safety Program")
        print("43. Encourage Employee Fitness")
        print("44. Establish Employee Innovation Challenge")
        print("45. Implement Employee Workload Evaluation")
        print("46. Provide Employee Fitness Facilities")
        print("47. Implement Employee Mentorship Program")
        print("48. Establish Employee Art and Culture Program")
        print("49. Conduct Employee Skill Transfer Program")
        print("50. Organize Employee Hackathons")
        print("51. Implement Employee Mental Health Initiatives")
        print("52. Offer Employee Skill Development Opportunities")
        print("53. Establish Employee Time Off Policy")
        print("54. Implement Employee Skill Degradation")
        print("55. Provide Employee Retirement Planning")
        print("56. Offer Employee Disciplinary Actions")
        print("57. Implement Employee Work-Life Balance Programs")
        print("58. Provide Employee Parental Leave Policy")
        print("59. Offer Employee Onboarding Program")
        print("60. Implement Employee Offboarding Program")
        print("61. Establish Employee Stock Ownership Program")
        print("62. Offer Employee Sabbaticals")
        print("63. Implement Employee Art and Culture Program")
        print("64. Establish Employee Mental Health Initiatives")
        print("65. Offer Employee Skill Development Opportunities")
        print("66. Implement Employee Time Off Policy")
        print("67. Establish Employee Skill Degradation")
        print("68. Offer Employee Retirement Planning")
        print("69. Implement Employee Disciplinary Actions")
        print("70. Establish Employee Work-Life Balance Programs")
        print("71. Offer Employee Parental Leave Policy")
        print("72. Implement Employee Onboarding Program")
        print("73. Establish Employee Offboarding Program")
        print("74. Offer Employee Stock Ownership Program")
        print("75. Implement Employee Sabbaticals")
        print("76. Establish Employee Art and Culture Program")
        print("77. Offer Employee Skill Development Opportunities")
        print("78. Implement Employee Time Off Policy")
        print("79. Establish Employee Skill Degradation")
        print("80. Offer Employee Retirement Planning")
        print("81. Implement Employee Disciplinary Actions")
        print("82. Establish Employee Work-Life Balance Programs")
        print("83. Offer Employee Parental Leave Policy")
        print("84. Implement Employee Onboarding Program")
        print("85. Establish Employee Offboarding Program")
        print("86. Offer Employee Stock Ownership Program")
        print("87. Implement Employee Sabbaticals")
        print("88. Establish Employee Art and Culture Program")
        print("89. Offer Employee Skill Development Opportunities")
        print("90. Implement Employee Time Off Policy")
        print("91. Establish Employee Skill Degradation")
        print("92. Offer Employee Retirement Planning")
        print("93. Implement Employee Disciplinary Actions")
        print("94. Establish Employee Work-Life Balance Programs")
        print("95. Offer Employee Parental Leave Policy")
        print("96. Implement Employee Onboarding Program")
        print("97. Establish Employee Offboarding Program")
        print("98. Offer Employee Stock Ownership Program")
        print("99. Implement Employee Sabbaticals")
        print("100. Establish Employee Art and Culture Program")
        print("101. Exit")

        choice = input("Enter your choice (1-101): ")

        if choice == "1":
            name = input("Enter the employee's name: ")
            salary = int(input("Enter the employee's salary: "))
            specialization = input("Enter the employee's specialization: ")
            new_employee = Employee(name, salary, specialization)
            player_company.hire_employee(new_employee)

        elif choice == "2":
            print("Employees:")
            for i, employee in enumerate(player_company.employees, 1):
                print(f"{i}. {employee.name}")

            emp_choice = int(input("Enter the number of the employee to fire: ")) - 1
            if 0 <= emp_choice < len(player_company.employees):
                employee = player_company.employees[emp_choice]
                player_company.fire_employee(employee)
            else:
                print("Invalid choice!")

        elif choice == "3":
            print("Employees:")
            for i, employee in enumerate(player_company.employees, 1):
                print(f"{i}. {employee.name}")
                print(f"   - Salary: ${employee.salary}")
                print(f"   - Age: {employee.age}")
                print(f"   - Skill: {employee.skill}")
                print(f"   - Performance: {employee.performance}")
                print(f"   - Morale: {employee.morale}")
                print()

        elif choice == "4":
            profit = player_company.make_money()
            print(f"Profit earned: ${profit}")

        elif choice == "5":
            print("Available Upgrades:")
            for i, upgrade_name in enumerate(player_company.upgrades.keys(), 1):
                print(f"{i}. {upgrade_name} (Level: {player_company.upgrades[upgrade_name].level})")

            upgrade_choice = int(input("Enter the number of the upgrade to purchase: ")) - 1
            if 0 <= upgrade_choice < len(player_company.upgrades):
                upgrade_name = list(player_company.upgrades.keys())[upgrade_choice]
                upgrade_cost = 100 * player_company.upgrades[upgrade_name].level
                upgrade_increase = 1
                player_company.purchase_upgrade(upgrade_name, upgrade_cost, upgrade_increase)
            else:
                print("Invalid choice!")

        elif choice == "6":
            print(f"Company's cash: ${player_company.cash}")

        elif choice == "7":
            player_company.conduct_market_research()

        elif choice == "8":
            player_company.stock_trading()

        elif choice == "9":
            player_company.establish_employee_resource_group()

        elif choice == "10":
            player_company.encourage_employee_volunteering()

        elif choice == "11":
            player_company.conduct_employee_surveys()

        elif choice == "12":
            player_company.implement_employee_reward_system()

        elif choice == "13":
            player_company.organize_team_building_activities()

        elif choice == "14":
            player_company.promote_employee_cross_training()

        elif choice == "15":
            player_company.implement_employee_suggestion_program()

        elif choice == "16":
            player_company.establish_mentorship_program_for_managers()

        elif choice == "17":
            player_company.offer_educational_assistance()

        elif choice == "18":
            player_company.organize_company_retreats()

        elif choice == "19":
            player_company.implement_employee_training_evaluation()

        elif choice == "20":
            player_company.conduct_employee_focus_groups()

        elif choice == "21":
            player_company.implement_employee_professional_development_program()

        elif choice == "22":
            player_company.support_employee_side_projects()

        elif choice == "23":
            player_company.provide_employee_counseling_services()

        elif choice == "24":
            player_company.implement_employee_skill_assessment()

        elif choice == "25":
            player_company.establish_employee_innovation_program()

        elif choice == "26":
            player_company.organize_employee_support_groups()

        elif choice == "27":
            player_company.implement_employee_mobility_program()

        elif choice == "28":
            player_company.provide_ergonomic_workstations()

        elif choice == "29":
            player_company.implement_employee_mentorship()

        elif choice == "30":
            player_company.establish_employee_idea_evaluation_system()

        elif choice == "31":
            player_company.provide_employee_wellbeing_benefits()

        elif choice == "32":
            player_company.establish_employee_feedback_loop()

        elif choice == "33":
            player_company.implement_employee_skill_certification_program()

        elif choice == "34":
            player_company.encourage_employee_team_collaboration()

        elif choice == "35":
            player_company.provide_employee_wellness_resources()

        elif choice == "36":
            player_company.organize_employee_career_fair()

        elif choice == "37":
            player_company.implement_employee_leadership_training()

        elif choice == "38":
            player_company.establish_employee_resilience_program()

        elif choice == "39":
            player_company.provide_employee_healthcare_benefits()

        elif choice == "40":
            player_company.offer_employee_stock_options()

        elif choice == "41":
            player_company.conduct_exit_interviews()

        elif choice == "42":
            player_company.implement_employee_safety_program()

        elif choice == "43":
            player_company.encourage_employee_fitness()

        elif choice == "44":
            player_company.establish_employee_innovation_challenge()

        elif choice == "45":
            player_company.implement_employee_workload_evaluation()

        elif choice == "46":
            player_company.provide_employee_fitness_facilities()

        elif choice == "47":
            player_company.implement_employee_mentorship_program()

        elif choice == "48":
            player_company.establish_employee_art_and_culture_program()

        elif choice == "49":
            player_company.conduct_employee_skill_transfer_program()

        elif choice == "50":
            player_company.organize_employee_hackathons()

        elif choice == "51":
            player_company.implement_employee_mental_health_initiatives()

        elif choice == "52":
            player_company.offer_employee_skill_development_opportunities()

        elif choice == "53":
            player_company.establish_employee_time_off_policy()

        elif choice == "54":
            player_company.implement_employee_skill_degradation()

        elif choice == "55":
            player_company.provide_employee_retirement_planning()

        elif choice == "56":
            player_company.offer_employee_disciplinary_actions()

        elif choice == "57":
            player_company.implement_employee_work_life_balance_programs()

        elif choice == "58":
            player_company.provide_employee_parental_leave_policy()

        elif choice == "59":
            player_company.offer_employee_onboarding_program()

        elif choice == "60":
            player_company.implement_employee_offboarding_program()

        elif choice == "61":
            player_company.establish_employee_stock_ownership_program()

        elif choice == "62":
            player_company.offer_employee_sabbaticals()

        elif choice == "63":
            player_company.implement_employee_art_and_culture_program()

        elif choice == "64":
            player_company.establish_employee_mental_health_initiatives()

        elif choice == "65":
            player_company.offer_employee_skill_development_opportunities()

        elif choice == "66":
            player_company.implement_employee_time_off_policy()

        elif choice == "67":
            player_company.establish_employee_skill_degradation()

        elif choice == "68":
            player_company.offer_employee_retirement_planning()

        elif choice == "69":
            player_company.implement_employee_disciplinary_actions()

        elif choice == "70":
            player_company.establish_employee_work_life_balance_programs()

        elif choice == "71":
            player_company.offer_employee_parental_leave_policy()

        elif choice == "72":
            player_company.implement_employee_onboarding_program()

        elif choice == "73":
            player_company.establish_employee_offboarding_program()

        elif choice == "74":
            player_company.offer_employee_stock_ownership_program()

        elif choice == "75":
            player_company.implement_employee_sabbaticals()

        elif choice == "76":
            player_company.establish_employee_art_and_culture_program()

        elif choice == "77":
            player_company.offer_employee_skill_development_opportunities()

        elif choice == "78":
            player_company.implement_employee_time_off_policy()

        elif choice == "79":
            player_company.establish_employee_skill_degradation()

        elif choice == "80":
            player_company.offer_employee_retirement_planning()

        elif choice == "81":
            player_company.implement_employee_disciplinary_actions()

        elif choice == "82":
            player_company.establish_employee_work_life_balance_programs()

        elif choice == "83":
            player_company.offer_employee_parental_leave_policy()

        elif choice == "84":
            player_company.implement_employee_onboarding_program()

        elif choice == "85":
            player_company.establish_employee_offboarding_program()

        elif choice == "86":
            player_company.offer_employee_stock_ownership_program()

        elif choice == "87":
            player_company.implement_employee_sabbaticals()

        elif choice == "88":
            player_company.establish_employee_art_and_culture_program()

        elif choice == "89":
            player_company.offer_employee_skill_development_opportunities()

        elif choice == "90":
            player_company.implement_employee_time_off_policy()

        elif choice == "91":
            player_company.establish_employee_skill_degradation()

        elif choice == "92":
            player_company.offer_employee_retirement_planning()

        elif choice == "93":
            player_company.implement_employee_disciplinary_actions()

        elif choice == "94":
            player_company.establish_employee_work_life_balance_programs()

        elif choice == "95":
            player_company.offer_employee_parental_leave_policy()

        elif choice == "96":
            player_company.implement_employee_onboarding_program()

        elif choice == "97":
            player_company.establish_employee_offboarding_program()

        elif choice == "98":
            player_company.offer_employee_stock_ownership_program()

        elif choice == "99":
            player_company.implement_employee_sabbaticals()

        elif choice == "100":
            player_company.establish_employee_art_and_culture_program()
        elif choice == "101":
            print("Exiting game. Thank you for playing!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
