---
layout: page
title: .rego
description: Linear regression with Shapley and Owen decomposition of R-squared
img: assets/img/logo_rego.png
importance: 3
category: Shapley value
---

<div align=right><img src="/assets/img/logo_rego.png" alt="[. rego] Linear regression with Shapley and Owen value decomposition of R-squared"></div>

---

<h3 style="color: #bb2222;">Purpose</h3>

<img src="/assets/img/rego_tiny.png" alt="rego" style="vertical-align: middle;">
is a <a href="http://www.stata.com/" target="_blank">Stata</a> module
that decomposes R<sup>2</sup> (share of explained variance) of an OLS model
into contributions of (groups of) regressor variables with the help of
Shapley or Owen values. The use of "groups" of variables that belong to
the same category (such as the variables that belong to a polynomial in *age*),
computational effort is lower than in the "classical" Shapley decomposition without groupings.
<img src="/assets/img/rego_tiny.png" alt="rego" style="vertical-align: middle;"> has an implemented option to
bootstrap the decomposition results in order to obtain percentile confidence intervals.

---

<h3 style="color: #bb2222;">Example</h3>

In the example below, <img src="/assets/img/rego_tiny.png" alt="rego" style="vertical-align: middle;">
is used to decompose the R<sup>2</sup> of a wage regression.
The backslash ("\\") symbol is used in the syntax to delimit groups of regressor variables.
The option "(detail)" requests the computation of within-group decomposition. This would take a considerable
amount of time if the number of variables in a group is large. The example below required 0.25 seconds computation time.

<div align="center">
<img src="/assets/img/rego_example.png" alt="rego example" style="margin: 20px 0;">
</div>

---

<h3 style="color: #bb2222;">Download</h3>

<img src="/assets/img/rego_tiny.png" alt="rego" style="vertical-align: middle;"> is published under the terms and conditions of the
<a href="http://www.gnu.org/licenses/gpl-3.0.html">GNU General Public License 3</a>.<a href="#asis">*</a>
The program is still "in development", and no warranty is provided regarding the "soundness" of results. If you encounter **bugs**, please <a href="mailto:sunder@wifa.uni-leipzig.de">report them</a>.

In order to install the current version for Stata 9 or higher, execute the following commands in the command window:

```
. net from http://www.marco-sunder.de/stata/
. net install rego
```

Alternatively, download <a href="/assets/files/rego.zip"><b>this zip file</b></a> and place its content either
into your working directory or into a different
folder that you specify with the `adopath` command.

---

<h3 style="color: #bb2222;">References</h3>

<img src="/assets/img/rego_tiny.png" alt="rego" style="vertical-align: middle;"> is written and maintained by
<a href="https://huettner.io">Frank Huettner</a>
and
<a href="http://www.marco-sunder.de">Marco Sunder</a>, University of Leipzig.

Huettner, F.; Sunder, M. (2012). "Axiomatic arguments for decomposing goodness of fit according to Shapley and Owen values." *Electronic Journal of Statistics*, 6, 1239-1250. <a href="https://doi.org/10.1214/12-EJS710">https://doi.org/10.1214/12-EJS710</a>

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

---

<small>
<a name="asis">* THIS SOFTWARE IS PROVIDED "AS IS" AND ANY EXPRESSED OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
</small>
