from asyncio.windows_events import NULL


{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 1 - Import test data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[*********************100%***********************]  1 of 1 completed\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Adj Close</th>\n",
       "      <th>Volume</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Datetime</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2022-10-07 00:00:00</th>\n",
       "      <td>0.979624</td>\n",
       "      <td>0.979624</td>\n",
       "      <td>0.979144</td>\n",
       "      <td>0.979240</td>\n",
       "      <td>0.979240</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2022-10-07 00:15:00</th>\n",
       "      <td>0.979336</td>\n",
       "      <td>0.979912</td>\n",
       "      <td>0.979240</td>\n",
       "      <td>0.979912</td>\n",
       "      <td>0.979912</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2022-10-07 00:30:00</th>\n",
       "      <td>0.979912</td>\n",
       "      <td>0.980104</td>\n",
       "      <td>0.979528</td>\n",
       "      <td>0.979528</td>\n",
       "      <td>0.979528</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2022-10-07 00:45:00</th>\n",
       "      <td>0.979528</td>\n",
       "      <td>0.979528</td>\n",
       "      <td>0.978953</td>\n",
       "      <td>0.979144</td>\n",
       "      <td>0.979144</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2022-10-07 01:00:00</th>\n",
       "      <td>0.979528</td>\n",
       "      <td>0.979720</td>\n",
       "      <td>0.978953</td>\n",
       "      <td>0.979048</td>\n",
       "      <td>0.979048</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2022-12-02 21:15:00</th>\n",
       "      <td>1.054074</td>\n",
       "      <td>1.054407</td>\n",
       "      <td>1.053963</td>\n",
       "      <td>1.054407</td>\n",
       "      <td>1.054407</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2022-12-02 21:30:00</th>\n",
       "      <td>1.054407</td>\n",
       "      <td>1.054407</td>\n",
       "      <td>1.053963</td>\n",
       "      <td>1.054074</td>\n",
       "      <td>1.054074</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2022-12-02 21:45:00</th>\n",
       "      <td>1.053963</td>\n",
       "      <td>1.054519</td>\n",
       "      <td>1.053963</td>\n",
       "      <td>1.054407</td>\n",
       "      <td>1.054407</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2022-12-02 22:00:00</th>\n",
       "      <td>1.053075</td>\n",
       "      <td>1.053075</td>\n",
       "      <td>1.053075</td>\n",
       "      <td>1.053075</td>\n",
       "      <td>1.053075</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2022-12-02 22:15:00</th>\n",
       "      <td>1.053075</td>\n",
       "      <td>1.053075</td>\n",
       "      <td>1.053075</td>\n",
       "      <td>1.053075</td>\n",
       "      <td>1.053075</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>3877 rows × 6 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                         Open      High       Low     Close  Adj Close  Volume\n",
       "Datetime                                                                      \n",
       "2022-10-07 00:00:00  0.979624  0.979624  0.979144  0.979240   0.979240       0\n",
       "2022-10-07 00:15:00  0.979336  0.979912  0.979240  0.979912   0.979912       0\n",
       "2022-10-07 00:30:00  0.979912  0.980104  0.979528  0.979528   0.979528       0\n",
       "2022-10-07 00:45:00  0.979528  0.979528  0.978953  0.979144   0.979144       0\n",
       "2022-10-07 01:00:00  0.979528  0.979720  0.978953  0.979048   0.979048       0\n",
       "...                       ...       ...       ...       ...        ...     ...\n",
       "2022-12-02 21:15:00  1.054074  1.054407  1.053963  1.054407   1.054407       0\n",
       "2022-12-02 21:30:00  1.054407  1.054407  1.053963  1.054074   1.054074       0\n",
       "2022-12-02 21:45:00  1.053963  1.054519  1.053963  1.054407   1.054407       0\n",
       "2022-12-02 22:00:00  1.053075  1.053075  1.053075  1.053075   1.053075       0\n",
       "2022-12-02 22:15:00  1.053075  1.053075  1.053075  1.053075   1.053075       0\n",
       "\n",
       "[3877 rows x 6 columns]"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import yfinance as yf\n",
    "import pandas as pd\n",
    "\n",
    "dataF = yf.download(\"EURUSD=X\", start=\"2022-10-7\", end=\"2022-12-5\", interval='15m')\n",
    "dataF.iloc[:,:]\n",
    "#dataF.Open.iloc"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 2 - Define your signal function"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "def signal_generator(df):\n",
    "    open = df.Open.iloc[-1]\n",
    "    close = df.Close.iloc[-1]\n",
    "    previous_open = df.Open.iloc[-2]\n",
    "    previous_close = df.Close.iloc[-2]\n",
    "    \n",
    "    # Bearish Pattern\n",
    "    if (open>close and \n",
    "    previous_open<previous_close and \n",
    "    close<previous_open and\n",
    "    open>=previous_close):\n",
    "        return 1\n",
    "\n",
    "    # Bullish Pattern\n",
    "    elif (open<close and \n",
    "        previous_open>previous_close and \n",
    "        close>previous_open and\n",
    "        open<=previous_close):\n",
    "        return 2\n",
    "    \n",
    "    # No clear pattern\n",
    "    else:\n",
    "        return 0\n",
    "\n",
    "signal = []\n",
    "signal.append(0)\n",
    "for i in range(1,len(dataF)):\n",
    "    df = dataF[i-1:i+1]\n",
    "    signal.append(signal_generator(df))\n",
    "#signal_generator(data)\n",
    "dataF[\"signal\"] = signal"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    3527\n",
       "2     178\n",
       "1     172\n",
       "Name: signal, dtype: int64"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataF.signal.value_counts()\n",
    "#dataF.iloc[:, :]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 3 - Connect to the market and execute trades"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "from apscheduler.schedulers.blocking import BlockingScheduler\n",
    "from oandapyV20 import API\n",
    "import oandapyV20.endpoints.orders as orders\n",
    "from oandapyV20.contrib.requests import MarketOrderRequest\n",
    "from oanda_candles import Pair, Gran, CandleClient\n",
    "from oandapyV20.contrib.requests import TakeProfitDetails, StopLossDetails"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "True\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "from config import access_token, accountID\n",
    "def get_candles(n):\n",
    "    #access_token='XXXXXXX'#you need token here generated from OANDA account\n",
    "    client = CandleClient(access_token, real=False)\n",
    "    collector = client.get_collector(Pair.EUR_USD, Gran.M15)\n",
    "    candles = collector.grab(n)\n",
    "    return candles\n",
    "\n",
    "candles = get_candles(3)\n",
    "for candle in candles:\n",
    "    print(float(str(candle.bid.o))>1)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "def trading_job():\n",
    "    candles = get_candles(3)\n",
    "    dfstream = pd.DataFrame(columns=['Open','Close','High','Low'])\n",
    "    \n",
    "    i=0\n",
    "    for candle in candles:\n",
    "        dfstream.loc[i, ['Open']] = float(str(candle.bid.o))\n",
    "        dfstream.loc[i, ['Close']] = float(str(candle.bid.c))\n",
    "        dfstream.loc[i, ['High']] = float(str(candle.bid.h))\n",
    "        dfstream.loc[i, ['Low']] = float(str(candle.bid.l))\n",
    "        i=i+1\n",
    "\n",
    "    dfstream['Open'] = dfstream['Open'].astype(float)\n",
    "    dfstream['Close'] = dfstream['Close'].astype(float)\n",
    "    dfstream['High'] = dfstream['High'].astype(float)\n",
    "    dfstream['Low'] = dfstream['Low'].astype(float)\n",
    "\n",
    "    signal = signal_generator(dfstream.iloc[:-1,:])#\n",
    "    \n",
    "    # EXECUTING ORDERS\n",
    "    #accountID = \"XXXXXXX\" #your account ID here\n",
    "    client = API(access_token)\n",
    "         \n",
    "    SLTPRatio = 2.\n",
    "    previous_candleR = abs(dfstream['High'].iloc[-2]-dfstream['Low'].iloc[-2])\n",
    "    \n",
    "    SLBuy = float(str(candle.bid.o))-previous_candleR\n",
    "    SLSell = float(str(candle.bid.o))+previous_candleR\n",
    "\n",
    "    TPBuy = float(str(candle.bid.o))+previous_candleR*SLTPRatio\n",
    "    TPSell = float(str(candle.bid.o))-previous_candleR*SLTPRatio\n",
    "    \n",
    "    print(dfstream.iloc[:-1,:])\n",
    "    print(TPBuy, \"  \", SLBuy, \"  \", TPSell, \"  \", SLSell)\n",
    "    signal = 2\n",
    "    #Sell\n",
    "    if signal == 1:\n",
    "        mo = MarketOrderRequest(instrument=\"EUR_USD\", units=-1000, takeProfitOnFill=TakeProfitDetails(price=TPSell).data, stopLossOnFill=StopLossDetails(price=SLSell).data)\n",
    "        r = orders.OrderCreate(accountID, data=mo.data)\n",
    "        rv = client.request(r)\n",
    "        print(rv)\n",
    "    #Buy\n",
    "    elif signal == 2:\n",
    "        mo = MarketOrderRequest(instrument=\"EUR_USD\", units=1000, takeProfitOnFill=TakeProfitDetails(price=TPBuy).data, stopLossOnFill=StopLossDetails(price=SLBuy).data)\n",
    "        r = orders.OrderCreate(accountID, data=mo.data)\n",
    "        rv = client.request(r)\n",
    "        print(rv)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4 - Executing orders automatically with a scheduler"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": NULL,
   "metadata": {},
   "outputs": [],
   "source": [
    "trading_job()\n",
    "\n",
    "#scheduler = BlockingScheduler()\n",
    "#scheduler.add_job(trading_job, 'cron', day_of_week='mon-fri', hour='00-23', minute='1,16,31,46', start_date='2022-01-12 12:00:00', timezone='America/Chicago')\n",
    "#scheduler.start()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": NULL,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.10.8 64-bit",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.8"
  },
  "vscode": {
   "interpreter": {
    "hash": "c0ff92a541b5eb8a0f75470c34280cf0dea79e8b819847822bd36e33345fddf3"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
