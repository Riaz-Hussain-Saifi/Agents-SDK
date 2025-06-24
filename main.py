import os
import asyncio
from dotenv import load_dotenv
import requests
from datetime import datetime
import chainlit as cl

# Load environment variables
load_dotenv()

# Helper function to fetch live cryptocurrency data from CoinGecko
def get_crypto_data():
    """Fetch current Bitcoin price from CoinGecko API"""
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data['bitcoin']['usd']
    except Exception as e:
        print(f"Error fetching crypto data: {e}")
        return None

def get_crypto_analysis():
    """Get current Bitcoin price and analysis"""
    current_btc_price = get_crypto_data()
    
    if current_btc_price is None:
        return "❌ Sorry, I couldn't fetch the current Bitcoin price. Please try again later."

    # Get the current time
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")

    # Enhanced decision logic for buying/selling based on price
    advice = ""
    risk_level = ""
    trend_indicator = ""
    
    if current_btc_price > 70000:
        advice = "🔴 Price is very high - consider taking profits or waiting for a significant dip."
        risk_level = "HIGH RISK to buy"
        trend_indicator = "🔺 SELL ZONE"
    elif current_btc_price > 50000:
        advice = "🟡 Price is high - good time for partial profit-taking or DCA selling."
        risk_level = "MEDIUM-HIGH RISK to buy"
        trend_indicator = "⚠️ CAUTION ZONE"
    elif current_btc_price > 35000:
        advice = "🟢 Price is in a moderate range - good for Dollar Cost Averaging (DCA)."
        risk_level = "MEDIUM RISK - good for DCA"
        trend_indicator = "📊 DCA ZONE"
    elif current_btc_price > 25000:
        advice = "🟢 Price is relatively low - might be a good buying opportunity."
        risk_level = "LOW-MEDIUM RISK - good buying zone"
        trend_indicator = "📈 BUY ZONE"
    else:
        advice = "🟢 Price is quite low - could be an excellent buying opportunity for long-term holders."
        risk_level = "LOW RISK - strong buying opportunity"
        trend_indicator = "🚀 STRONG BUY"

    # Additional market insights
    price_ranges = {
        "Resistance": f"${current_btc_price * 1.05:,.0f}",
        "Support": f"${current_btc_price * 0.95:,.0f}",
        "Next Target": f"${current_btc_price * 1.10:,.0f}" if current_btc_price < 50000 else f"${current_btc_price * 0.90:,.0f}"
    }

    return f"""📊 **Bitcoin Market Analysis**

💰 **Current Price:** ${current_btc_price:,.2f} USD
⏰ **Last Updated:** {current_time}
{trend_indicator}

📈 **Market Assessment:**
• **Risk Level:** {risk_level}
• **Trading Advice:** {advice}

🎯 **Key Levels:**
• **Support Level:** {price_ranges['Support']}
• **Resistance Level:** {price_ranges['Resistance']}
• **Next Target:** {price_ranges['Next Target']}

📊 **Market Context:**
• **Market Cap Rank:** #1 Cryptocurrency
• **24h Change:** ~±2-5% (typical volatility)
• **Volume:** High institutional interest

💡 **Investment Strategies:**
• **DCA (Dollar Cost Averaging):** Best for long-term investors
• **Swing Trading:** Wait for 10-15% price swings
• **HODLing:** Good for 1+ year time horizon

⚠️ **Important Disclaimer:** 
This is educational content, not financial advice. Cryptocurrency investments are highly volatile and risky. Always:
• Do your own research (DYOR)
• Never invest more than you can afford to lose
• Consider your risk tolerance
• Consult with financial advisors for personalized advice"""

def generate_crypto_response(user_question, crypto_data):
    """Generate a comprehensive crypto response based on user question and live data"""
    
    user_lower = user_question.lower()
    
    # Different response templates based on user question type
    if "price" in user_lower:
        return f"""{crypto_data}

**You asked about Bitcoin's price** - Above is the complete current market analysis with live data from CoinGecko API.

🔍 **Quick Price Summary:**
The current Bitcoin price gives us insights into market sentiment and potential opportunities. Use the risk assessment and trading zones above to make informed decisions."""

    elif any(word in user_lower for word in ["buy", "sell", "invest", "trading"]):
        return f"""{crypto_data}

**Trading & Investment Analysis:**

Based on the current price level, here's my educational perspective:

🎯 **For New Investors:**
• Start with small amounts using DCA strategy
• Focus on understanding the technology and market
• Set clear risk management rules

📈 **For Active Traders:**
• Watch the support and resistance levels mentioned above
• Consider market sentiment and volume
• Use stop-losses to protect capital

💼 **For Long-term Holders:**
• Focus on fundamental analysis
• Ignore short-term price movements
• Consider the long-term adoption trends

Remember: The crypto market is 24/7 and highly volatile. Always have a clear strategy before investing."""

    elif any(word in user_lower for word in ["analysis", "market", "trend"]):
        return f"""{crypto_data}

**Detailed Market Analysis:**

🔍 **Current Market Dynamics:**
• Bitcoin continues to be the leading cryptocurrency
• Institutional adoption is growing steadily
• Regulatory clarity is improving globally

📊 **Technical Perspective:**
• Price action shows typical crypto volatility
• Support and resistance levels are key to watch
• Volume and momentum indicators matter

🌍 **Fundamental Factors:**
• Global economic conditions affect crypto
• Regulatory developments impact prices
• Technology upgrades and improvements
• Institutional investment flows

🔮 **What to Watch:**
• Breaking above resistance levels
• Holding support during downturns
• Volume confirmation on price moves
• News and regulatory developments"""

    else:
        return f"""{crypto_data}

**General Crypto Information:**

Based on your question about Bitcoin, here's what's most important to know:

📚 **Bitcoin Basics:**
• First and largest cryptocurrency by market cap
• Digital gold narrative gaining acceptance
• Limited supply of 21 million coins
• Decentralized and peer-to-peer network

🎯 **Investment Considerations:**
• High volatility is normal for crypto
• Long-term perspective often works better
• Diversification is important
• Education before investment is crucial

💭 **Common Questions:**
• "When to buy?" - DCA reduces timing risk
• "How much to invest?" - Only what you can afford to lose
• "Where to store?" - Hardware wallets for large amounts
• "Tax implications?" - Consult tax professionals

Feel free to ask more specific questions about Bitcoin, trading, or investment strategies!"""

@cl.on_chat_start
async def start():
    """Initialize the chat with a welcome message and description"""
    welcome_message = """🚀 **Welcome to CryptoCurrencyAgent!**

I'm your AI assistant for Bitcoin and cryptocurrency information. Here's what I can help you with:

📈 **My Capabilities:**
• ✅ **Real-time Bitcoin price updates** from CoinGecko API
• ✅ **Market analysis and trend insights**
• ✅ **Trading advice and risk assessment**
• ✅ **Investment education and strategies**
• ✅ **Technical and fundamental analysis**

💬 **How to Use Me:**
Just ask questions like:
• "What's the current Bitcoin price?"
• "Should I buy Bitcoin now?"
• "Give me a market analysis"
• "What's your trading advice?"
• "Explain Bitcoin investment strategies"

🔄 **Live Data:** I fetch real-time Bitcoin prices and provide up-to-date market analysis.

📚 **Educational Focus:** I provide educational insights and analysis - not financial advice.

⚡ **Fast & Reliable:** No complex AI models - just fast, accurate crypto information!

Ready to help! What would you like to know about Bitcoin today?"""
    
    await cl.Message(content=welcome_message).send()

@cl.on_message
async def handle_user_query(message: cl.Message):
    """
    Handle user queries about cryptocurrency with live data integration
    """
    try:
        user_message = message.content
        
        # Check if user is asking about crypto/bitcoin
        crypto_keywords = ['bitcoin', 'btc', 'crypto', 'price', 'buy', 'sell', 'trading', 'market', 'analysis', 'invest']
        
        if any(keyword in user_message.lower() for keyword in crypto_keywords):
            # Show loading message
            loading_msg = cl.Message(content="🔍 Fetching live Bitcoin data and preparing analysis...")
            await loading_msg.send()
            
            # Get live crypto data
            crypto_data = get_crypto_analysis()
            
            # Generate comprehensive response
            response = generate_crypto_response(user_message, crypto_data)
            
            # Update loading message with result
            loading_msg.content = response
            await loading_msg.update()
            
        else:
            # For general questions about crypto
            response = """🤔 **I specialize in Bitcoin and cryptocurrency information!**

I can help you with:
• Bitcoin price updates and analysis
• Trading and investment advice
• Market trends and insights
• Risk assessment and strategies

Try asking:
• "What's Bitcoin's current price?"
• "Should I invest in Bitcoin?"
• "Give me a market update"
• "What's your trading advice?"

What would you like to know about Bitcoin or cryptocurrency?"""
            
            await cl.Message(content=response).send()
            
    except Exception as e:
        error_message = f"""❌ **Oops! Something went wrong**

I encountered an error: `{str(e)}`

🔄 **What you can try:**
• Ask about Bitcoin price: "What's Bitcoin's price?"
• Request market analysis: "Give me a crypto update"
• Check your internet connection
• Try refreshing the page

I'm here to help with Bitcoin and cryptocurrency questions!"""
        
        await cl.Message(content=error_message).send()

# Run the application
if __name__ == "__main__":
    cl.run(
        debug=True,
        host="localhost", 
        port=8000
    )