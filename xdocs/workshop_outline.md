# Let's Build an API Test Agent! - 3-Hour Workshop Outline

## Pre-Workshop Setup (15 minutes before start)
- **Python IDE** (VS Code, PyCharm, or similar) installed
- **OpenAI API access** (free tier or paid plan)
- **Required Python packages**: `requests`, `openai`, `json`, `pytest` (optional)
- **Sample API endpoints** for testing (provided list)

---

## **Hour 1: Foundation & Quick Wins (60 minutes)**

### Opening & Introductions (10 minutes)
- Welcome and brief introductions
- Workshop goals and what you'll build
- Quick poll: Experience with APIs and AI tools

### What Makes an AI Agent? (10 minutes)
- **Theory**: Agent vs. Script vs. Tool
- **Our agent's workflow**: Plan → Generate → Execute → Validate → Report

### **Exercise 1: First Success - API Analysis Agent (25 minutes)**
**🎯 GOAL: See immediate AI-powered results**
- **START WITH**: Complete working code template
- **MODIFY**: Add your OpenAI API key
- **RUN**: Analyze a real API endpoint
- **SEE**: AI generates test ideas instantly!

```python
# PROVIDED STARTER CODE
class APITestAgent:
    def __init__(self, openai_api_key):
        # Complete implementation provided
        
    def analyze_api(self, api_endpoint):
        # Working LLM integration provided
        
    def generate_test_ideas(self, endpoint_info):
        # Complete prompt engineering provided
```

### **Exercise 2: Generate Your First Test Cases (15 minutes)**
**🎯 GOAL: Get personalized test scenarios**
- **START WITH**: Working test case generator
- **CUSTOMIZE**: Try different API endpoints
- **EXPERIMENT**: Modify prompts for different test types
- **RESULT**: See 5-10 intelligent test ideas per API

---

## **Hour 2: Code Generation & Execution (60 minutes)**

### **Exercise 3: Generate Working Test Code (30 minutes)**
**🎯 GOAL: AI writes Python test code for you**
- **START WITH**: Complete code generation framework
- **MODIFY**: Prompts for different test scenarios
- **GENERATE**: Real Python test functions
- **VALIDATE**: Check syntax and logic

```python
# PROVIDED FRAMEWORK
def generate_test_code(self, test_idea, api_endpoint):
    # Complete prompt engineering provided
    # Syntax validation included
    # Multiple test types supported
```

### **Exercise 4: Execute and See Results (20 minutes)**
**🎯 GOAL: Run AI-generated tests against real APIs**
- **START WITH**: Safe execution environment
- **RUN**: Generated test code
- **CAPTURE**: Results, timing, status codes
- **DISPLAY**: Real-time test results

### **Exercise 5: Basic Validation (10 minutes)**
**🎯 GOAL: AI validates API responses**
- **START WITH**: Simple validation template
- **EXPERIMENT**: Different validation criteria
- **SEE**: AI identifies issues and anomalies

---

## **Hour 3: Complete Agent & Advanced Features (60 minutes)**

### **Exercise 6: Full Agent Workflow (25 minutes)**
**🎯 GOAL: Complete end-to-end agent execution**
- **START WITH**: Integrated agent class
- **RUN**: Full workflow: Analyze → Generate → Execute → Validate → Report
- **CUSTOMIZE**: Add your own API endpoints
- **RESULT**: Complete test report with AI insights

### **Exercise 7: Intelligent Reporting (15 minutes)**
**🎯 GOAL: AI generates executive summaries**
- **START WITH**: Report generation framework
- **GENERATE**: Professional test reports
- **CUSTOMIZE**: Report formats and audiences

### **OPTIONAL Exercise 8: Advanced Features (20 minutes)**
**⚡ TIME PERMITTING: Choose your adventure**
- **Option A**: Test Prioritization Intelligence
- **Option B**: Custom Validation Rules
- **Option C**: Performance Testing Integration

---

## **Alternative "Core Results" Timeline (If Running Behind)**

### **Essential Path - Focus on these for maximum impact:**

**Hour 1 (Streamlined):**
- **Exercise 1**: API Analysis Agent (20 min) - *Must do*
- **Exercise 2**: Test Case Generation (15 min) - *Must do*
- **Demo**: Code Generation (10 min) - *Show don't code*

**Hour 2 (Core Experience):**
- **Exercise 3**: Generate Test Code (25 min) - *Must do*
- **Exercise 4**: Execute Tests (20 min) - *Must do*
- **Demo**: Validation (10 min) - *Show results*

**Hour 3 (Complete Success):**
- **Exercise 6**: Full Agent Workflow (35 min) - *Must do*
- **Exercise 7**: Generate Reports (15 min) - *Must do*
- **Wrap-up**: What you built (10 min)

### **Skip if Time is Tight:**
- ❌ Exercise 5: Basic Validation (becomes demo)
- ❌ Exercise 8: Advanced Features (becomes discussion)
- ❌ Detailed theory sections (focus on doing)

### **Always Include (Non-negotiable):**
- ✅ Exercise 1: First AI results
- ✅ Exercise 3: Code generation
- ✅ Exercise 4: Test execution
- ✅ Exercise 6: Full workflow
- ✅ Exercise 7: Report generation

---

## **Wrap-up & Next Steps (15 minutes)**

### What You've Built
- Review the complete agent architecture
- Discuss key learnings and insights
- Share results from final exercise

### Making It Production-Ready
- Configuration management
- Logging and monitoring
- Scaling considerations
- Security best practices

### Advanced Features to Explore
- **Multi-API testing workflows**
- **Performance testing integration**
- **Continuous testing pipelines**
- **Custom validation rules**
- **Integration with existing test frameworks**

### Q&A and Resources
- Open discussion
- Recommended reading and tools
- Community resources for AI testing

---

## **Starter Code Templates Needed**

### **Exercise 1 - Complete Working Template:**
```python
# Complete APITestAgent class with OpenAI integration
# Participants just add API key and run
class APITestAgent:
    def __init__(self, openai_api_key):
        # Full implementation provided
        
    def analyze_api(self, api_endpoint):
        # Complete LLM prompt and response handling
        
    def generate_test_ideas(self, endpoint_info):
        # Working prompt engineering with examples
```

### **Exercise 3 - Code Generation Framework:**
```python
# Complete prompt templates for different test types
# Syntax validation and error handling included
def generate_test_code(self, test_idea, api_endpoint):
    # Multiple test templates provided
    # Validation logic included
```

### **Exercise 4 - Safe Execution Environment:**
```python
# Complete test runner with safety checks
# Result capture and formatting included
def execute_test_safely(self, test_code, timeout=30):
    # Error handling and result capture provided
```

### **Exercise 6 - Integrated Agent:**
```python
# Complete end-to-end workflow
# All components connected and working
def run_full_analysis(self, api_endpoints):
    # Complete pipeline implementation
```

---

## **Success Metrics for Each Exercise**

### **Exercise 1**: 
- ✅ See AI analyze an API endpoint
- ✅ Get 5-10 test ideas generated
- ✅ Understand what the agent "sees"

### **Exercise 3**: 
- ✅ AI generates valid Python test code
- ✅ Code passes syntax validation
- ✅ Multiple test scenarios covered

### **Exercise 4**: 
- ✅ Generated tests run successfully
- ✅ See real API responses
- ✅ Capture timing and status codes

### **Exercise 6**: 
- ✅ Complete workflow executes end-to-end
- ✅ Professional test report generated
- ✅ AI provides actionable insights

**Result**: Participants leave with a working AI agent that they've seen analyze, generate, execute, and report on API tests - even if they skip optional exercises.