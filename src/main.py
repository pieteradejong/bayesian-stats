"""
Bayesian stats

"""
import logging
from dotenv import load_dotenv
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def init():
    load_dotenv()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    logging.info("Initializing applicaiton...")
    logging.info("Loaded environment variables")


def main():
    logging.info("Running application..")

    # Step 1: Initialize distributions
    # Let's assume we want to estimate a normal distribution
    true_mean = 5
    true_std = 2
    samples = []

    # Step 2: Sampling from the distribution
    for _ in range(1000):  # Number of samples
        sample = np.random.normal(true_mean, true_std)
        samples.append(sample)

        # Step 3: Update estimation
        # For simplicity, we're just calculating the sample mean and std
        estimated_mean = np.mean(samples)
        estimated_std = np.std(samples)

        # Step 4: Plot the current estimation against the true distribution
        if _ % 50 == 0:  # Plot every 50 samples
            plt.hist(samples, bins=30, density=True, alpha=0.6, color="g")
            xmin, xmax = plt.xlim()
            x = np.linspace(xmin, xmax, 100)
            p = norm.pdf(x, true_mean, true_std)
            q = norm.pdf(x, estimated_mean, estimated_std)
            plt.plot(x, p, "k", linewidth=2)
            plt.plot(x, q, "r", linewidth=2)
            title = f"Estimation vs True Distribution after {_+1} samples"
            plt.title(title)
            plt.show()


if __name__ == "__main__":
    init()
    main()
