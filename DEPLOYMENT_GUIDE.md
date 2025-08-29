# Deployment Guide - Array Processing REST API

This guide provides step-by-step instructions for deploying the Array Processing REST API to various hosting platforms.

## 🚀 Quick Deploy Options

### 1. Render (Recommended - Free Tier Available)

**Step 1:** Create a Render Account
- Go to [render.com](https://render.com)
- Sign up with GitHub

**Step 2:** Deploy from GitHub
1. Click "New +" → "Web Service"
2. Connect your GitHub repository
3. Select the repository
4. Configure:
   - **Name:** `array-processing-api`
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`
   - **Plan:** Free

**Step 3:** Set Environment Variables (Optional)
- `FULL_NAME`: Your full name for user_id generation
- `PORT`: Leave as default (Render sets this automatically)

**Step 4:** Deploy
- Click "Create Web Service"
- Wait for deployment (2-3 minutes)

**Your API will be available at:** `https://your-app-name.onrender.com/bfhl`

### 2. Railway (Alternative - Free Tier Available)

**Step 1:** Create a Railway Account
- Go to [railway.app](https://railway.app)
- Sign up with GitHub

**Step 2:** Deploy
1. Click "New Project" → "Deploy from GitHub repo"
2. Select your repository
3. Railway will automatically detect it's a Python app
4. Deploy

**Step 3:** Set Environment Variables (Optional)
- `FULL_NAME`: Your full name for user_id generation

**Your API will be available at:** `https://your-app-name.railway.app/bfhl`

### 3. Heroku (Paid - $5/month minimum)

**Step 1:** Install Heroku CLI
```bash
# Windows
# Download from https://devcenter.heroku.com/articles/heroku-cli

# macOS
brew tap heroku/brew && brew install heroku

# Linux
curl https://cli-assets.heroku.com/install.sh | sh
```

**Step 2:** Login and Create App
```bash
heroku login
heroku create your-app-name
```

**Step 3:** Deploy
```bash
git push heroku main
```

**Step 4:** Set Environment Variables
```bash
heroku config:set FULL_NAME="your_full_name"
```

**Your API will be available at:** `https://your-app-name.herokuapp.com/bfhl`

### 4. Vercel (Alternative)

**Step 1:** Create Vercel Account
- Go to [vercel.com](https://vercel.com)
- Sign up with GitHub

**Step 2:** Deploy
1. Click "New Project"
2. Import your GitHub repository
3. Configure as Python project
4. Deploy

**Your API will be available at:** `https://your-app-name.vercel.app/bfhl`

## 🔧 Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `FULL_NAME` | Your full name for user_id generation | `kishan_madhav_a_g` | No |
| `PORT` | Port number for the server | `5000` | No |

## 📋 Pre-deployment Checklist

- [ ] All files are committed to Git
- [ ] `requirements.txt` is up to date
- [ ] `Procfile` is present (for Heroku/Railway)
- [ ] `runtime.txt` is present (for Heroku)
- [ ] Environment variables are configured
- [ ] API endpoint `/bfhl` is working locally
- [ ] Tests pass locally

## 🧪 Post-deployment Testing

After deployment, test your API:

### 1. Health Check
```bash
curl https://your-app-url.com/health
```

### 2. API Test
```bash
curl -X POST https://your-app-url.com/bfhl \
  -H "Content-Type: application/json" \
  -d '{"array": ["Hello", "World", 123, 456, "!", "@", "Python", 7.5, "API"]}'
```

### 3. Expected Response
```json
{
    "is_success": true,
    "user_id": "your_name_29082025",
    "email_id": "user_20250829_112050@example.com",
    "college_roll_number": "202408291120",
    "even_numbers": [456],
    "odd_numbers": [123, 7.5],
    "alphabets_uppercase": ["HELLO", "WORLD", "PYTHON", "API"],
    "special_characters": ["!", "@"],
    "sum_of_numbers": 586.5,
    "concatenated_alphabets_reverse_alternating": "IaP nOhTyP dLrOw OlLeH"
}
```

## 🛠️ Troubleshooting

### Common Issues

1. **Build Fails**
   - Check `requirements.txt` is correct
   - Ensure Python version is compatible
   - Check for syntax errors in code

2. **App Crashes on Start**
   - Check logs for error messages
   - Verify `app.py` has correct port configuration
   - Ensure all dependencies are installed

3. **API Returns 500 Error**
   - Check application logs
   - Verify request format is correct
   - Test locally first

4. **Environment Variables Not Working**
   - Restart the application after setting variables
   - Check variable names are correct
   - Verify deployment platform supports the variables

### Getting Logs

**Render:**
- Go to your service dashboard
- Click on "Logs" tab

**Railway:**
- Go to your project dashboard
- Click on "Deployments" → "View Logs"

**Heroku:**
```bash
heroku logs --tail
```

**Vercel:**
- Go to your project dashboard
- Click on "Functions" → "View Logs"

## 📊 Monitoring

### Health Check Endpoint
All deployments include a health check endpoint:
```
GET /health
```

### Response:
```json
{
    "status": "healthy",
    "message": "API is running successfully"
}
```

## 🔄 Continuous Deployment

Most platforms support automatic deployment:

1. **Connect GitHub repository**
2. **Enable auto-deploy**
3. **Push changes to trigger deployment**

## 📝 Custom Domain (Optional)

### Render
1. Go to your service dashboard
2. Click "Settings" → "Custom Domains"
3. Add your domain
4. Configure DNS

### Railway
1. Go to your project dashboard
2. Click "Settings" → "Domains"
3. Add custom domain

### Heroku
```bash
heroku domains:add yourdomain.com
```

## 🎯 Performance Optimization

1. **Enable Caching** (if needed)
2. **Use CDN** for static assets
3. **Monitor Response Times**
4. **Scale Resources** as needed

## 🔒 Security Considerations

1. **HTTPS Only** - All platforms provide SSL
2. **Input Validation** - Already implemented
3. **Rate Limiting** - Consider adding for production
4. **Environment Variables** - Never commit secrets

## 📞 Support

If you encounter issues:

1. **Check platform documentation**
2. **Review application logs**
3. **Test locally first**
4. **Check GitHub issues**

---

**Recommended Platform:** Render (Free tier, easy setup, good performance)
**Alternative:** Railway (Free tier, good for development)
**Production:** Heroku (Paid, enterprise features)
