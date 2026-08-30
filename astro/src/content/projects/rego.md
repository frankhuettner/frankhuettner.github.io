---
title: .rego
summary: Linear regression with Shapley and Owen decomposition of R-squared.
order: 3
url: /assets/files/rego.zip
tags: ["Stata", "Shapley value"]
---

## Purpose

`rego` is a [Stata](http://www.stata.com/) module that decomposes R² (share of
explained variance) of an OLS model into contributions of (groups of) regressor
variables with the help of Shapley or Owen values. By using "groups" of variables
that belong to the same category — such as the variables that belong to a
polynomial in _age_ — computational effort is lower than in the "classical"
Shapley decomposition without groupings. `rego` has an implemented option to
bootstrap the decomposition results in order to obtain percentile confidence
intervals.

## Example

In the example below, `rego` is used to decompose the R² of a wage regression.
The backslash (`\`) symbol delimits groups of regressor variables. The option
`(detail)` requests the computation of within-group decomposition. This would
take a considerable amount of time if the number of variables in a group is
large; the example below required 0.25 seconds.

![rego example](/assets/img/rego_example.png)

## Download

`rego` is published under the terms and conditions of the
[GNU General Public License 3](http://www.gnu.org/licenses/gpl-3.0.html).[^asis]
The program is still in development, and no warranty is provided regarding the
soundness of results.

To install the current version for Stata 9 or higher, execute the following in
the command window:

```
. net from http://www.marco-sunder.de/stata/
. net install rego
```

Alternatively, download [this zip file](/assets/files/rego.zip) and place its
contents either into your working directory or into a different folder that you
specify with the `adopath` command.

## References

`rego` is written and maintained by [Frank Huettner](https://huettner.io) and
[Marco Sunder](http://www.marco-sunder.de), University of Leipzig.

Huettner, F.; Sunder, M. (2012). "Axiomatic arguments for decomposing goodness of
fit according to Shapley and Owen values." _Electronic Journal of Statistics_, 6,
1239–1250. [doi:10.1214/12-EJS710](https://doi.org/10.1214/12-EJS710)

```bibtex
@article{HueSun2012EJS,
    author  = {Frank Huettner and Marco Sunder},
    title   = {Axiomatic arguments for decomposing goodness of fit
               according to Shapley and Owen values},
    journal = {Electronic Journal of Statistics},
    volume  = {6},
    pages   = {1239--1250},
    year    = {2012},
    doi     = {10.1214/12-EJS710}
}
```

[^asis]: THIS SOFTWARE IS PROVIDED "AS IS" AND ANY EXPRESSED OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
