from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Student, CareerProgress


def login_view(request):
    """Handle student login"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')


def logout_view(request):
    """Handle student logout"""
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def dashboard(request):
    """Display main dashboard with 5 modules"""
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        student = None
    
    context = {
        'student': student,
        'modules': [
            {'id': 1, 'name': 'Coding Awareness', 'url': 'coding_awareness', 'icon': '💻'},
            {'id': 2, 'name': 'Project Guidance', 'url': 'project_guidance', 'icon': '📋'},
            {'id': 3, 'name': 'Hackathons', 'url': 'hackathons', 'icon': '🚀'},
            {'id': 4, 'name': 'Jobs & Internships', 'url': 'jobs_internships', 'icon': '💼'},
            {'id': 5, 'name': 'Branch-wise Roadmaps', 'url': 'roadmaps', 'icon': '🗺️'},
        ]
    }
    return render(request, 'dashboard.html', context)


@login_required(login_url='login')
def coding_awareness(request):
    """Module 1: Coding Awareness Page"""
    platforms = [
        {
            'name': 'HackerRank',
            'link': 'https://www.hackerrank.com',
            'description': 'Interactive coding challenges with instant feedback'
        },
        {
            'name': 'CodeChef',
            'link': 'https://www.codechef.com',
            'description': 'Competitive programming with monthly contests'
        },
        {
            'name': 'LeetCode',
            'link': 'https://www.leetcode.com',
            'description': 'Interview-focused coding problems'
        },
        {
            'name': 'GeeksforGeeks',
            'link': 'https://www.geeksforgeeks.org',
            'description': 'Comprehensive tutorials and DSA resources'
        },
        {
            'name': 'Codeforces',
            'link': 'https://codeforces.com',
            'description': 'Competitive programming and contests'
        },
    ]
    
    language_comparison = [
        {
            'language': 'Python',
            'difficulty': 'Easy',
            'use_case': 'Beginners, Data Science, Web Development',
            'popularity': '⭐⭐⭐⭐⭐'
        },
        {
            'language': 'Java',
            'difficulty': 'Moderate',
            'use_case': 'Enterprise, Android, Large-scale Applications',
            'popularity': '⭐⭐⭐⭐⭐'
        },
        {
            'language': 'C++',
            'difficulty': 'Hard',
            'use_case': 'Competitive Programming, System Software, Game Development',
            'popularity': '⭐⭐⭐⭐'
        },
        {
            'language': 'C',
            'difficulty': 'Moderate',
            'use_case': 'Operating Systems, Embedded Systems, Foundation Building',
            'popularity': '⭐⭐⭐⭐'
        },
    ]
    
    easy_languages = ['Python', 'JavaScript', 'Ruby']
    moderate_languages = ['Java', 'C', 'C#', 'Go']
    hard_languages = ['C++', 'Rust', 'Assembly']
    
    context = {
        'platforms': platforms,
        'language_comparison': language_comparison,
        'easy_languages': easy_languages,
        'moderate_languages': moderate_languages,
        'hard_languages': hard_languages,
    }
    
    return render(request, 'coding_awareness.html', context)


@login_required(login_url='login')
def project_guidance(request):
    """Module 2: Project Guidance Page"""
    code_editors = [
        {'name': 'VS Code', 'type': 'Code Editor', 'url': 'https://code.visualstudio.com'},
        {'name': 'Sublime Text', 'type': 'Code Editor', 'url': 'https://www.sublimetext.com'},
        {'name': 'Notepad++', 'type': 'Code Editor', 'url': 'https://notepad-plus-plus.org'},
    ]
    
    language_ides = [
        {'language': 'Java', 'ide': 'Eclipse', 'url': 'https://www.eclipse.org'},
        {'language': 'Python', 'ide': 'PyCharm', 'url': 'https://www.jetbrains.com/pycharm'},
        {'language': 'C/C++', 'ide': 'Code::Blocks', 'url': 'http://www.codeblocks.org'},
    ]
    
    deployment_platforms = [
        {'name': 'GitHub', 'url': 'https://github.com', 'type': 'Repository'},
        {'name': 'Netlify', 'url': 'https://www.netlify.com', 'type': 'Frontend Hosting'},
        {'name': 'Render', 'url': 'https://render.com', 'type': 'Full Stack Hosting'},
    ]
    
    timeline = [
        {'year': '1st Year', 'description': 'Learn fundamentals, start mini projects'},
        {'year': '2nd Year', 'description': 'Build projects with databases'},
        {'year': '3rd Year', 'description': 'Major projects with full stack'},
        {'year': '4th Year', 'description': 'Professional projects, deployment'},
    ]
    
    context = {
        'code_editors': code_editors,
        'language_ides': language_ides,
        'deployment_platforms': deployment_platforms,
        'timeline': timeline,
    }
    
    return render(request, 'project_guidance.html', context)


@login_required(login_url='login')
def hackathons(request):
    """Module 3: Hackathons Page"""
    certifications = [
        {
            'name': 'Google',
            'link': 'https://www.google.com/careers',
            'description': 'Google Cloud Skills Boost, Cybersecurity Certifications'
        },
        {
            'name': 'Coursera',
            'link': 'https://www.coursera.org',
            'description': 'Professional Certificates from Top Universities'
        },
        {
            'name': 'NPTEL',
            'link': 'https://nptel.ac.in',
            'description': 'Indian government platform for online courses with certificates'
        },
        {
            'name': 'Infosys Springboard',
            'link': 'https://www.infosys.com/infosys-springboard',
            'description': 'Free courses in emerging technologies'
        },
    ]
    
    hackathon_benefits = [
        'Build real-world projects quickly',
        'Network with industry professionals',
        'Gain hands-on experience with new technologies',
        'Win prizes and recognition',
        'Add impressive projects to portfolio',
        'Improve problem-solving skills under pressure',
    ]
    
    career_impact = [
        'Demonstrate technical skills to employers',
        'Stand out in campus placements',
        'Build a strong project portfolio',
        'Networking opportunities with recruiters',
        'Potential job offers during hackathons',
        'Resume enhancement with hackathon wins',
    ]
    
    context = {
        'certifications': certifications,
        'hackathon_benefits': hackathon_benefits,
        'career_impact': career_impact,
    }
    
    return render(request, 'hackathons.html', context)


@login_required(login_url='login')
def jobs_internships(request):
    """Module 4: Jobs & Internships Page - Comprehensive Career & Internship Guidance"""
    
    # Expanded career options with enhanced details
    career_options = [
        # SOFTWARE CAREERS
        {
            'id': 'soft-dev',
            'category': 'Software',
            'title': 'Software Developer',
            'package': '₹5-12 LPA',
            'entry_level': '₹5-8 LPA',
            'experience_needed': '0-2 years',
            'description': 'Develops software applications and systems using programming languages and frameworks',
            'skills': ['Programming (C/C++/Java)', 'DSA', 'Software Design Patterns', 'Testing & Debugging', 'Version Control'],
            'tools': ['VS Code', 'Git', 'JIRA', 'Jenkins'],
            'roles': ['Junior Developer', 'Senior Developer', 'Tech Lead'],
            'companies': ['Google', 'Microsoft', 'Amazon', 'Adobe', 'Flipkart'],
            'growth_path': 'Junior Dev → Senior Dev → Tech Lead → Engineering Manager',
            'remote_friendly': True,
        },
        {
            'id': 'web-dev',
            'category': 'Software',
            'title': 'Web Developer',
            'package': '₹4-10 LPA',
            'description': 'Creates websites and web applications',
            'skills': ['HTML/CSS', 'JavaScript', 'Backend (Node/Django/Flask)', 'Databases', 'APIs', 'Responsive Design'],
            'tools': ['React', 'Vue.js', 'Node.js', 'MongoDB', 'PostgreSQL'],
            'roles': ['Frontend Developer', 'Backend Developer', 'Full Stack Developer'],
            'companies': ['Flipkart', 'Swiggy', 'Airbnb', 'Uber', 'OLX'],
        },
        {
            'id': 'fullstack-dev',
            'category': 'Software',
            'title': 'Full Stack Developer',
            'package': '₹6-14 LPA',
            'description': 'Develops both frontend and backend of web applications',
            'skills': ['Frontend (React/Vue)', 'Backend (Node/Django)', 'Databases', 'APIs', 'DevOps Basics', 'Cloud Services'],
            'tools': ['React/Vue', 'Node.js/Django', 'MongoDB/PostgreSQL', 'Docker', 'AWS'],
            'roles': ['Full Stack Developer', 'Tech Lead', 'Architect'],
            'companies': ['Startup Hub', 'Tech Giants', 'Fintech Companies'],
        },
        {
            'id': 'mobile-app',
            'category': 'Software',
            'title': 'Mobile App Developer',
            'package': '₹5-12 LPA',
            'description': 'Develops Android/iOS mobile applications',
            'skills': ['Android (Java/Kotlin)', 'iOS (Swift)', 'Mobile UI/UX', 'APIs Integration', 'Cross-platform'],
            'tools': ['Android Studio', 'Xcode', 'React Native', 'Flutter'],
            'roles': ['Android Developer', 'iOS Developer', 'Cross-platform Developer'],
            'companies': ['Google', 'Apple', 'Paytm', 'PhonePe', 'Zomato'],
        },
        {
            'id': 'data-analyst',
            'category': 'Software',
            'title': 'Data Analyst',
            'package': '₹4-8 LPA',
            'description': 'Analyzes data to provide business insights',
            'skills': ['SQL', 'Python/R', 'Data Visualization', 'Excel', 'Statistics', 'Tableau/PowerBI'],
            'tools': ['Python', 'Tableau', 'PowerBI', 'Excel', 'SQL'],
            'roles': ['Data Analyst', 'BI Developer', 'Analytics Manager'],
            'companies': ['Flipkart', 'Amazon', 'Jio', 'Adobe', 'PayPal'],
        },
        {
            'id': 'data-scientist',
            'category': 'Software',
            'title': 'Data Scientist',
            'package': '₹8-18 LPA',
            'description': 'Builds ML models and insights from data',
            'skills': ['Python', 'Machine Learning', 'Deep Learning', 'Statistics', 'Data Visualization', 'SQL'],
            'tools': ['Python', 'TensorFlow', 'Scikit-learn', 'Jupyter', 'Pandas'],
            'roles': ['Data Scientist', 'ML Engineer', 'Research Scientist'],
            'companies': ['Google', 'Microsoft', 'Amazon', 'Tesla', 'IBM'],
        },
        {
            'id': 'ml-engineer',
            'category': 'Software',
            'title': 'Machine Learning Engineer',
            'package': '₹8-16 LPA',
            'description': 'Develops and deploys ML models in production',
            'skills': ['Python', 'ML Algorithms', 'Deep Learning', 'Model Optimization', 'TensorFlow/PyTorch', 'MLOps'],
            'tools': ['TensorFlow', 'PyTorch', 'Scikit-learn', 'Docker', 'Kubernetes'],
            'roles': ['ML Engineer', 'ML Research Engineer', 'ML Ops Engineer'],
            'companies': ['Google', 'OpenAI', 'Tesla', 'Facebook', 'Netflix'],
        },
        {
            'id': 'ai-engineer',
            'category': 'Software',
            'title': 'AI Engineer',
            'package': '₹10-20 LPA',
            'description': 'Develops AI solutions and LLM applications',
            'skills': ['Python', 'AI Frameworks', 'NLP', 'LLMs', 'Prompt Engineering', 'Deep Learning'],
            'tools': ['PyTorch', 'Hugging Face', 'OpenAI API', 'LangChain', 'Vector DBs'],
            'roles': ['AI Engineer', 'Prompt Engineer', 'GenAI Developer'],
            'companies': ['OpenAI', 'Google', 'Microsoft', 'Meta', 'Anthropic'],
        },
        {
            'id': 'cloud-engineer',
            'category': 'Software',
            'title': 'Cloud Engineer',
            'package': '₹7-16 LPA',
            'description': 'Manages cloud infrastructure and services',
            'skills': ['AWS/Azure/GCP', 'Linux', 'Networking', 'Databases', 'Infrastructure as Code', 'Security'],
            'tools': ['AWS', 'Azure', 'Docker', 'Kubernetes', 'Terraform'],
            'roles': ['Cloud Engineer', 'DevOps Engineer', 'Solutions Architect'],
            'companies': ['AWS', 'Microsoft', 'Google Cloud', 'Accenture', 'Cognizant'],
        },
        {
            'id': 'devops-engineer',
            'category': 'Software',
            'title': 'DevOps Engineer',
            'package': '₹7-14 LPA',
            'description': 'Automates deployment and infrastructure',
            'skills': ['Linux', 'Docker', 'Kubernetes', 'CI/CD Pipelines', 'Infrastructure As Code', 'Scripting'],
            'tools': ['Jenkins', 'GitLab CI', 'Docker', 'Kubernetes', 'Terraform'],
            'roles': ['DevOps Engineer', 'SRE Engineer', 'Infrastructure Engineer'],
            'companies': ['TCS', 'Infosys', 'Cognizant', 'Tech Startups'],
        },
        {
            'id': 'cyber-security',
            'category': 'Software',
            'title': 'Cyber Security Engineer',
            'package': '₹6-14 LPA',
            'description': 'Protects systems and networks from security threats',
            'skills': ['Network Security', 'Ethical Hacking', 'Penetration Testing', 'Cryptography', 'Security Protocols'],
            'tools': ['Kali Linux', 'Metasploit', 'Wireshark', 'Burp Suite'],
            'roles': ['Security Analyst', 'Penetration Tester', 'Security Architect'],
            'companies': ['Microsoft', 'Google', 'Cisco', 'SecureIT Companies'],
        },
        {
            'id': 'blockchain',
            'category': 'Software',
            'title': 'Blockchain Developer',
            'package': '₹8-18 LPA',
            'description': 'Develops blockchain applications and smart contracts',
            'skills': ['Solidity', 'Smart Contracts', 'Ethereum', 'Cryptography', 'Distributed Systems'],
            'tools': ['Truffle', 'Remix', 'Web3.js', 'Hardhat'],
            'roles': ['Blockchain Developer', 'Smart Contract Developer', 'Blockchain Architect'],
            'companies': ['Coinbase', 'Polygon', 'Crypto Companies', 'BitCoin'],
        },
        {
            'id': 'game-dev',
            'category': 'Software',
            'title': 'Game Developer',
            'package': '₹5-12 LPA',
            'description': 'Develops video games and game engines',
            'skills': ['C++/C#', 'Game Physics', '3D Graphics', 'Game Design', 'Multiplayer Networking'],
            'tools': ['Unity', 'Unreal Engine', 'C++', 'Blender'],
            'roles': ['Game Developer', 'Graphics Programmer', 'Game Designer'],
            'companies': ['EA Games', 'Activision', 'Ubisoft', 'Rockstar'],
        },
        {
            'id': 'qa-engineer',
            'category': 'Software',
            'title': 'QA Engineer',
            'package': '₹3-7 LPA',
            'description': 'Tests software for bugs and quality assurance',
            'skills': ['Manual Testing', 'Automation Testing', 'Test Frameworks', 'SQL', 'API Testing', 'Excel'],
            'tools': ['Selenium', 'JUnit', 'TestNG', 'Postman'],
            'roles': ['QA Engineer', 'Automation QA', 'QA Lead'],
            'companies': ['TCS', 'Infosys', 'Tech Companies'],
        },

        # HARDWARE / CORE ENGINEERING CAREERS
        {
            'id': 'embedded-systems',
            'category': 'Hardware',
            'title': 'Embedded Systems Engineer',
            'package': '₹4-10 LPA',
            'description': 'Designs embedded systems and microcontroller applications',
            'skills': ['C/C++', 'Microcontrollers (Arduino/ARM)', 'IoT', 'Circuits', 'RTOS', 'Hardware Design'],
            'tools': ['Arduino', 'STM32', 'Embedded Linux', 'UART/SPI'],
            'roles': ['Embedded Systems Designer', 'Firmware Engineer', 'IoT Developer'],
            'companies': ['Tesla', 'Qualcomm', 'ST Microelectronics', 'Apple'],
        },
        {
            'id': 'vlsi-design',
            'category': 'Hardware',
            'title': 'VLSI Design Engineer',
            'package': '₹6-14 LPA',
            'description': 'Designs and develops integrated circuits (ICs)',
            'skills': ['Verilog/VHDL', 'Circuit Design', 'Logic Design', 'ASIC Design', 'Cadence Tools'],
            'tools': ['Cadence', 'Verilog', 'VHDL', 'LTspice'],
            'roles': ['VLSI Design Engineer', 'Physical Design Engineer', 'Verification Engineer'],
            'companies': ['Intel', 'AMD', 'NVIDIA', 'Broadcom'],
        },
        {
            'id': 'electronics-design',
            'category': 'Hardware',
            'title': 'Electronics Design Engineer',
            'package': '₹4-9 LPA',
            'description': 'Designs electronic circuits and PCBs',
            'skills': ['Circuit Design', 'PCB Design', 'Signal Processing', 'Analog/Digital Electronics', 'CAD Design'],
            'tools': ['Eagle CAD', 'KiCAD', 'Proteus', 'LTspice'],
            'roles': ['Hardware Designer', 'PCB Designer', 'Electronics Engineer'],
            'companies': ['Phillips', 'Siemens', 'Bosch'],
        },
        {
            'id': 'hardware-engineer',
            'category': 'Hardware',
            'title': 'Hardware Engineer',
            'package': '₹5-11 LPA',
            'description': 'Develops and tests computer hardware',
            'skills': ['Hardware Design', 'Testing & Debugging', 'System Architecture', 'Troubleshooting', 'CAD'],
            'tools': ['CAD Tools', 'Oscilloscope', 'Multimeter', 'Hardware Testing'],
            'roles': ['Hardware Engineer', 'Systems Engineer', 'Firmware Engineer'],
            'companies': ['Dell', 'HP', 'Intel', 'Cisco'],
        },
        {
            'id': 'network-engineer',
            'category': 'Hardware',
            'title': 'Network Engineer',
            'package': '₹5-11 LPA',
            'description': 'Designs and manages networking infrastructure',
            'skills': ['Networking (TCP/IP)', 'Routing & Switching', 'Network Security', 'Cloud Networking', 'Firewalls'],
            'tools': ['Cisco Routers', 'Firewalls', 'Wireshark', 'Network Simulators'],
            'roles': ['Network Engineer', 'Network Administrator', 'Network Architect'],
            'companies': ['Cisco', 'Juniper', 'Infosys', 'TCS'],
        },
        {
            'id': 'iot-engineer',
            'category': 'Hardware',
            'title': 'IoT Engineer',
            'package': '₹5-12 LPA',
            'description': 'Develops Internet of Things solutions',
            'skills': ['Embedded Systems', 'IoT Protocols (MQTT/CoAP)', 'Sensors', 'Wireless Communication', 'Cloud Integration'],
            'tools': ['Arduino', 'Raspberry Pi', 'MQTT', 'AWS IoT Core'],
            'roles': ['IoT Developer', 'IoT Architect', 'Sensor Specialist'],
            'companies': ['Bosch', 'Philips', 'Cisco', 'GE'],
        },
        {
            'id': 'robotics',
            'category': 'Hardware',
            'title': 'Robotics Engineer',
            'package': '₹6-13 LPA',
            'description': 'Designs and develops robotic systems',
            'skills': ['Robotics', 'Control Systems', 'Mechanical Design', 'AI/ML for Robotics', 'ROS (Robot OS)'],
            'tools': ['ROS', 'MATLAB', 'Simulink', 'CAD Tools', 'Arduino/Embedded'],
            'roles': ['Robotics Engineer', 'Controls Engineer', 'Roboticist'],
            'companies': ['Boston Dynamics', 'Tesla', 'Amazon Robotics'],
        },
        {
            'id': 'automation',
            'category': 'Hardware',
            'title': 'Automation Engineer',
            'package': '₹5-10 LPA',
            'description': 'Automates industrial processes and systems',
            'skills': ['PLC Programming', 'SCADA', 'Automation Design', 'Electrical Systems', 'Troubleshooting'],
            'tools': ['PLC', 'HMI', 'SCADA', 'Ladder Logic'],
            'roles': ['Automation Engineer', 'Controls Engineer', 'Process Engineer'],
            'companies': ['Siemens', 'ABB', 'Honeywell'],
        },
        {
            'id': 'control-systems',
            'category': 'Hardware',
            'title': 'Control Systems Engineer',
            'package': '₹6-12 LPA',
            'description': 'Designs control systems for industrial applications',
            'skills': ['Control Theory', 'Signal Processing', 'MATLAB/Simulink', 'System Modeling', 'PLC'],
            'tools': ['MATLAB', 'Simulink', 'PLC', 'LabVIEW'],
            'roles': ['Control Systems Engineer', 'Design Engineer', 'Systems Engineer'],
            'companies': ['Siemens', 'General Electric', 'Honeywell'],
        },
        {
            'id': 'power-systems',
            'category': 'Hardware',
            'title': 'Power Systems Engineer',
            'package': '₹5-11 LPA',
            'description': 'Designs power generation, transmission, and distribution systems',
            'skills': ['Power Systems', 'Grid Analysis', 'MATLAB/ETAP', 'Solar/Wind Renewable', 'Electrical Design'],
            'tools': ['ETAP', 'MATLAB', 'PSCAD', 'PSS/E'],
            'roles': ['Power System Engineer', 'Grid Engineer', 'Renewable Energy Specialist'],
            'companies': ['Power Grid Companies', 'Renewable Energy Companies', 'GE'],
        },
        {
            'id': 'telecom-engineer',
            'category': 'Hardware',
            'title': 'Telecom Engineer',
            'package': '₹5-10 LPA',
            'description': 'Designs and maintains telecommunication systems',
            'skills': ['5G/4G Technology', 'Network Protocols', 'Signal Processing', 'RF Engineering', 'Optics'],
            'tools': ['Network Simulators', 'Signal Analyzers', 'Telecom Tools'],
            'roles': ['Telecom Engineer', 'Network Engineer', '5G Specialist'],
            'companies': ['Jio', 'Airtel', 'Vodafone', 'Ericsson', 'Nokia'],
        },
    ]
    
    internship_platforms = [
        {'name': 'Internshala', 'url': 'https://www.internshala.com'},
        {'name': 'LinkedIn', 'url': 'https://www.linkedin.com/jobs/internships'},
        {'name': 'AICTE Portal', 'url': 'https://www.aicteindia.org'},
    ]
    
    semester_roadmap = [
        {
            'semester': '1-2',
            'focus': 'Foundation Building',
            'skills': ['Programming Basics', 'DSA Fundamentals', 'Web Basics'],
        },
        {
            'semester': '3-4',
            'focus': 'Specialization',
            'skills': ['Advanced DSA', 'Web/Mobile Dev', 'Database Design'],
        },
        {
            'semester': '5-6',
            'focus': 'Project & Internships',
            'skills': ['Full Stack Development', 'Problem Solving', 'System Design'],
        },
        {
            'semester': '7-8',
            'focus': 'Placement Readiness',
            'skills': ['Interview Prep', 'Portfolio Building', 'Professional Skills'],
        },
    ]
    
    resume_tips = [
        'Technical Skills: Languages, Frameworks, Tools',
        'Projects: 3-4 major projects with descriptions',
        'Internships: Achievements and learnings',
        'Certifications: Relevant online courses and achievements',
        'Achievements: Hackathons, competitions, awards',
        'Contact: Email, LinkedIn, GitHub profile',
    ]
    
    context = {
        'career_options': career_options,
        'internship_platforms': internship_platforms,
        'semester_roadmap': semester_roadmap,
        'resume_tips': resume_tips,
        'career_paths': [
            {
                'name': 'Full Stack Web Development',
                'duration': '6-12 months',
                'skills_needed': ['JavaScript', 'React/Vue', 'Node.js/Django', 'Databases', 'APIs'],
                'avg_package': '₹6-10 LPA',
                'companies': ['Startups', 'Tech Companies', 'Product Companies'],
                'difficulty': 'Intermediate',
            },
            {
                'name': 'Data Science & AI/ML',
                'duration': '8-12 months',
                'skills_needed': ['Python', 'Statistics', 'Machine Learning', 'Deep Learning', 'Data Visualization'],
                'avg_package': '₹8-15 LPA',
                'companies': ['Tech Giants', 'Fintech', 'Research Labs'],
                'difficulty': 'Advanced',
            },
            {
                'name': 'DevOps & Cloud Engineering',
                'duration': '6-9 months',
                'skills_needed': ['Linux', 'Docker', 'Kubernetes', 'AWS/Azure', 'CI/CD'],
                'avg_package': '₹7-14 LPA',
                'companies': ['Cloud Providers', 'Tech Companies', 'Enterprises'],
                'difficulty': 'Intermediate',
            },
            {
                'name': 'Cybersecurity Engineering',
                'duration': '8-12 months',
                'skills_needed': ['Network Security', 'Ethical Hacking', 'Cryptography', 'Linux', 'Threat Analysis'],
                'avg_package': '₹6-14 LPA',
                'companies': ['Security Firms', 'Tech Giants', 'Enterprises'],
                'difficulty': 'Advanced',
            },
            {
                'name': 'Mobile App Development',
                'duration': '6-9 months',
                'skills_needed': ['Android/iOS', 'Mobile UI/UX', 'APIs', 'Databases', 'Version Control'],
                'avg_package': '₹5-12 LPA',
                'companies': ['Tech Companies', 'Startups', 'Product Companies'],
                'difficulty': 'Intermediate',
            },
            {
                'name': 'Embedded Systems & IoT',
                'duration': '8-12 months',
                'skills_needed': ['C/C++', 'Microcontrollers', 'RTOS', 'IoT Protocols', 'Hardware'],
                'avg_package': '₹5-11 LPA',
                'companies': ['Hardware Companies', 'Automotive', 'Electronics'],
                'difficulty': 'Hard',
            },
        ],
        'job_search_resources': [
            {
                'name': 'LeetCode',
                'type': 'Coding Practice',
                'url': 'https://www.leetcode.com',
                'description': 'Practice coding interview questions with 2000+ problems'
            },
            {
                'name': 'GeeksforGeeks',
                'type': 'Learning & Practice',
                'url': 'https://www.geeksforgeeks.org',
                'description': 'Comprehensive tutorials on DSA, System Design, and interviews'
            },
            {
                'name': 'HackerRank',
                'type': 'Coding Practice',
                'url': 'https://www.hackerrank.com',
                'description': 'Interactive coding challenges with instant feedback'
            },
            {
                'name': 'GitHub',
                'type': 'Portfolio Building',
                'url': 'https://www.github.com',
                'description': 'Build your coding portfolio and showcase projects'
            },
            {
                'name': 'LinkedIn',
                'type': 'Networking & Jobs',
                'url': 'https://www.linkedin.com',
                'description': 'Professional networking and job discovery'
            },
            {
                'name': 'Glassdoor',
                'type': 'Company Reviews',
                'url': 'https://www.glassdoor.com',
                'description': 'Company reviews, salaries, and interview experiences'
            },
        ],
        'interview_tips': [
            {
                'title': 'DSA Preparation',
                'description': 'Master Arrays, Linked Lists, Trees, Graphs, Dynamic Programming. Practice 200+ problems.',
                'time': '2-3 months'
            },
            {
                'title': 'System Design',
                'description': 'Learn scalability, databases, caching, load balancing, and distributed systems.',
                'time': '1-2 months'
            },
            {
                'title': 'Technical Communication',
                'description': 'Practice explaining solutions clearly, asking clarifying questions, and optimizing approaches.',
                'time': 'Ongoing'
            },
            {
                'title': 'Mock Interviews',
                'description': 'Practice with friends or use platforms like Pramp for real mock interviews.',
                'time': '2-4 weeks'
            },
            {
                'title': 'Behavioral Prep',
                'description': 'Prepare STAR method stories, learn about company culture, and practice HR questions.',
                'time': '1 week'
            },
        ]
    }
    
    return render(request, 'jobs_internships.html', context)


@login_required(login_url='login')
def roadmaps(request):
    """Module 5: Branch-wise Roadmaps"""
    branch = request.GET.get('branch', 'CSE')
    
    roadmaps_data = {
        'CSE': {
            'name': 'Computer Science & Engineering',
            'semesters': [
                {
                    'semester': '1st Year',
                    'courses': ['Programming (C/C++/Java)', 'Data Structures', 'Web Basics'],
                    'skills': ['Coding Fundamentals', 'Problem Solving'],
                    'tools': ['VS Code', 'Git', 'GitHub'],
                    'projects': ['Simple Programs', 'Data Structure Problems'],
                },
                {
                    'semester': '2nd Year',
                    'courses': ['DSA', 'DBMS', 'Web Development', 'Operating Systems'],
                    'skills': ['Advanced DSA', 'Database Design', 'Frontend Development'],
                    'tools': ['MySQL', 'Node.js', 'React'],
                    'projects': ['Todo App', 'Blog Website', 'Chat Application'],
                },
                {
                    'semester': '3rd Year',
                    'courses': ['System Design', 'Cloud Computing', 'ML Basics', 'Microservices'],
                    'skills': ['Backend Development', 'Scalability', 'Cloud Services'],
                    'tools': ['AWS/Google Cloud', 'Docker', 'Kubernetes'],
                    'projects': ['E-commerce Platform', 'Social Media App'],
                },
                {
                    'semester': '4th Year',
                    'courses': ['Advanced System Design', 'DevOps', 'AI/ML Advanced'],
                    'skills': ['Full Stack Mastery', 'Deployment', 'Architecture'],
                    'tools': ['CI/CD Pipeline', 'Terraform', 'Prometheus'],
                    'projects': ['Production-ready Application', 'Open Source Contribution'],
                },
            ]
        },
        'ECE': {
            'name': 'Electronics & Communication Engineering',
            'semesters': [
                {
                    'semester': '1st Year',
                    'courses': ['Circuit Theory', 'Digital Electronics', 'Programming Basics'],
                    'skills': ['Circuit Analysis', 'Logic Design'],
                    'tools': ['Proteus', 'LTspice'],
                    'projects': ['Simple Circuits', 'Digital Logic Designs'],
                },
                {
                    'semester': '2nd Year',
                    'courses': ['Microprocessors', 'Signals & Systems', 'Embedded Systems'],
                    'skills': ['Microcontroller Programming', 'Signal Processing'],
                    'tools': ['Arduino', 'Oscilloscope'],
                    'projects': ['IoT Sensors', 'Wireless Communication Projects'],
                },
                {
                    'semester': '3rd Year',
                    'courses': ['VLSI Design', 'Communication Systems', 'Network Security'],
                    'skills': ['FPGA Programming', 'Protocol Design'],
                    'tools': ['Verilog/VHDL', '5G Concepts'],
                    'projects': ['IoT Devices', 'Smart Home Projects'],
                },
                {
                    'semester': '4th Year',
                    'courses': ['Advanced VLSI', 'RF Engineering', 'Mobile Networks'],
                    'skills': ['Hardware Design', 'Network Architecture'],
                    'tools': ['CAD Tools', 'Network Simulators'],
                    'projects': ['Complete IoT Solution', 'Communication System Design'],
                },
            ]
        },
        'EEE': {
            'name': 'Electrical & Electronics Engineering',
            'semesters': [
                {
                    'semester': '1st Year',
                    'courses': ['Circuit Theory', 'Electrical Machines', 'Programming'],
                    'skills': ['Circuit Analysis', 'Power Systems Basics'],
                    'tools': ['MATLAB', 'PSPICE'],
                    'projects': ['Power System Simulations'],
                },
                {
                    'semester': '2nd Year',
                    'courses': ['Power Generation', 'Power Distribution', 'Control Systems'],
                    'skills': ['Load Flow Analysis', 'Power Factor Correction'],
                    'tools': ['ETAP', 'PSCAD'],
                    'projects': ['Smart Grid Projects', 'Renewable Energy Systems'],
                },
                {
                    'semester': '3rd Year',
                    'courses': ['High Voltage Engineering', 'Electrical Protection', 'Renewable Energy'],
                    'skills': ['Grid Management', 'Solar/Wind Systems'],
                    'tools': ['Power System Simulators'],
                    'projects': ['Solar Energy Systems', 'Grid Stability Projects'],
                },
                {
                    'semester': '4th Year',
                    'courses': ['Advanced Power Systems', 'Smart Grids', 'Electric Vehicles'],
                    'skills': ['Energy Efficiency', 'Sustainable Technologies'],
                    'tools': ['Modern Grid Tools'],
                    'projects': ['Complete Power System Design', 'EV Charging Solutions'],
                },
            ]
        },
        'MECH': {
            'name': 'Mechanical Engineering',
            'semesters': [
                {
                    'semester': '1st Year',
                    'courses': ['Engineering Graphics', 'Mechanics', 'Thermodynamics Basics'],
                    'skills': ['CAD Basics', 'Problem Solving'],
                    'tools': ['AutoCAD', 'FreeCAD'],
                    'projects': ['2D Designs', '3D Models'],
                },
                {
                    'semester': '2nd Year',
                    'courses': ['Thermodynamics', 'Fluid Mechanics', 'Manufacturing Processes'],
                    'skills': ['CFD Analysis', 'Manufacturing Design'],
                    'tools': ['ANSYS', 'SolidWorks'],
                    'projects': ['Fluid Flow Simulations', 'Machine Components Design'],
                },
                {
                    'semester': '3rd Year',
                    'courses': ['Machine Design', 'Vibrations', 'Heat Transfer', 'Robotics'],
                    'skills': ['Structural Analysis', 'Automation Design'],
                    'tools': ['CATIA', 'MATLAB Simulink'],
                    'projects': ['Robotic Systems', 'Thermal Analysis Projects'],
                },
                {
                    'semester': '4th Year',
                    'courses': ['Advanced Design', 'Renewable Energy', 'AI in Manufacturing'],
                    'skills': ['Product Design', 'Automation Leadership'],
                    'tools': ['Industry 4.0 Tools'],
                    'projects': ['Complete Product Design', 'Autonomous Systems'],
                },
            ]
        },
        'CIVIL': {
            'name': 'Civil Engineering',
            'semesters': [
                {
                    'semester': '1st Year',
                    'courses': ['Engineering Mechanics', 'Building Materials', 'Surveying Basics'],
                    'skills': ['Structural Analysis Basics', 'Site Understanding'],
                    'tools': ['AutoCAD', 'Total Station'],
                    'projects': ['Site Surveys', 'Material Testing'],
                },
                {
                    'semester': '2nd Year',
                    'courses': ['Structural Analysis', 'Concrete Technology', 'Geotechnical Engineering'],
                    'skills': ['Beam & Column Design', 'Foundation Design'],
                    'tools': ['STAAD Pro', 'Soil Testing Equipment'],
                    'projects': ['Building Designs', 'Soil Investigation Reports'],
                },
                {
                    'semester': '3rd Year',
                    'courses': ['Reinforced Concrete Design', 'Steel Structures', 'Water Resources'],
                    'skills': ['RCC Design', 'Hydraulics Analysis'],
                    'tools': ['ETabs', 'HEC-RAS'],
                    'projects': ['Bridge Designs', 'Water Systems'],
                },
                {
                    'semester': '4th Year',
                    'courses': ['Advanced Design', 'Project Management', 'Sustainable Infrastructure'],
                    'skills': ['Integrated Design', 'Project Leadership'],
                    'tools': ['BIM Tools', 'Project Management Software'],
                    'projects': ['Complete Infrastructure Design', 'Smart City Solutions'],
                },
            ]
        }
    }
    
    selected_roadmap = roadmaps_data.get(branch, roadmaps_data['CSE'])
    branches = list(roadmaps_data.keys())
    
    context = {
        'branches': branches,
        'selected_branch': branch,
        'roadmap': selected_roadmap,
    }
    
    return render(request, 'roadmaps.html', context)


def register(request):
    """Student registration page"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        roll_number = request.POST.get('roll_number')
        branch = request.POST.get('branch', 'CSE')
        year = request.POST.get('year', 1)
        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return redirect('register')
        
        if Student.objects.filter(roll_number=roll_number).exists():
            messages.error(request, 'Roll number already exists.')
            return redirect('register')
        
        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        
        # Create student profile
        Student.objects.create(
            user=user,
            roll_number=roll_number,
            branch=branch,
            year=year
        )
        
        # Create career progress tracker
        student = Student.objects.get(user=user)
        CareerProgress.objects.create(student=student)
        
        messages.success(request, 'Registration successful! Please login.')
        return redirect('login')
    
    context = {
        'branches': [
            ('CSE', 'Computer Science & Engineering'),
            ('ECE', 'Electronics & Communication Engineering'),
            ('EEE', 'Electrical & Electronics Engineering'),
            ('MECH', 'Mechanical Engineering'),
            ('CIVIL', 'Civil Engineering'),
        ],
        'years': [(1, '1st Year'), (2, '2nd Year'), (3, '3rd Year'), (4, '4th Year')],
    }
    
    return render(request, 'register.html', context)
