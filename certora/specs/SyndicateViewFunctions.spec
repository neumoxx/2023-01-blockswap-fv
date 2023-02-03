using MocksETH as sETHToken

methods {
    //// Regular methods
    totalETHReceived() returns (uint256) envfree
    isKnotRegistered(bytes32) returns (bool) envfree

    //// Resolving external calls
	// stakeHouseUniverse
	stakeHouseKnotInfo(bytes32) returns (address,address,address,uint256,uint256,bool) => DISPATCHER(true)
    memberKnotToStakeHouse(bytes32) returns (address) => DISPATCHER(true) // not used directly by Syndicate
    // stakeHouseRegistry
    getMemberInfo(bytes32) returns (address,uint256,uint16,bool) => DISPATCHER(true) // not used directly by Syndicate
    // slotSettlementRegistry
	stakeHouseShareTokens(address) returns (address)  => DISPATCHER(true)
	currentSlashedAmountOfSLOTForKnot(bytes32) returns (uint256)  => DISPATCHER(true)
	numberOfCollateralisedSlotOwnersForKnot(bytes32) returns (uint256)  => DISPATCHER(true)
	getCollateralisedOwnerAtIndex(bytes32, uint256) returns (address) => DISPATCHER(true)
	totalUserCollateralisedSLOTBalanceForKnot(address, address, bytes32) returns (uint256) => DISPATCHER(true)
    // sETH
    sETHToken.balanceOf(address) returns (uint256) envfree
    // ERC20
    name()                                returns (string)  => DISPATCHER(true)
    symbol()                              returns (string)  => DISPATCHER(true)
    decimals()                            returns (string) envfree => DISPATCHER(true)
    totalSupply()                         returns (uint256) => DISPATCHER(true)
    balanceOf(address)                    returns (uint256) => DISPATCHER(true)
    allowance(address,address)            returns (uint)    => DISPATCHER(true)
    approve(address,uint256)              returns (bool)    => DISPATCHER(true)
    transfer(address,uint256)             returns (bool)    => DISPATCHER(true)
    transferFrom(address,address,uint256) returns (bool)    => DISPATCHER(true)

    //// Harnessing
    // harnessed variables
    accruedEarningPerCollateralizedSlotOwnerOfKnot(bytes32,address) returns (uint256) envfree
    totalETHProcessedPerCollateralizedKnot(bytes32) returns (uint256) envfree
    sETHStakedBalanceForKnot(bytes32,address) returns (uint256) envfree
    sETHTotalStakeForKnot(bytes32) returns (uint256) envfree
    // harnessed functions
    deRegisterKnots(bytes32) 
    deRegisterKnots(bytes32,bytes32)
    stake(bytes32,uint256,address)
    stake(bytes32,bytes32,uint256,uint256,address)
    unstake(address,address,bytes32,uint256)
    unstake(address,address,bytes32,bytes32,uint256,uint256)
    claimAsStaker(address,bytes32)
    claimAsStaker(address,bytes32,bytes32)
    claimAsCollateralizedSLOTOwner(address,bytes32)
    claimAsCollateralizedSLOTOwner(address,bytes32,bytes32)
    registerKnotsToSyndicate(bytes32)
    registerKnotsToSyndicate(bytes32,bytes32)
    addPriorityStakers(address)
    addPriorityStakers(address,address)
    batchUpdateCollateralizedSlotOwnersAccruedETH(bytes32)
    batchUpdateCollateralizedSlotOwnersAccruedETH(bytes32,bytes32)

    // added by neumo
    getCorrectAccumulatedETHPerFreeFloatingShareForBLSPublicKey(bytes32) returns(uint256) envfree
    sETHUserClaimForKnot(bytes32, address) returns(uint256) envfree
    PRECISION() returns(uint256) envfree
    lastAccumulatedETHPerFreeFloatingShare(bytes32) returns(uint256) envfree
    owner() returns (address) envfree
    updatePriorityStakingBlock(uint256)
    accumulatedETHPerFreeFloatingShare() returns(uint256) envfree
    accumulatedETHPerCollateralizedSlotPerKnot() returns(uint256) envfree
    isNoLongerPartOfSyndicate(bytes32) returns (bool) envfree
    priorityStakingEndBlock() returns (uint256) envfree
    isPriorityStaker(address) returns (bool) envfree
    lastSeenETHPerCollateralizedSlotPerKnot() returns(uint256) envfree
    lastSeenETHPerFreeFloating() returns(uint256) envfree
    calculateETHForFreeFloatingOrCollateralizedHolders() returns(uint256) envfree
    calculateUnclaimedFreeFloatingETHShare(bytes32, address) returns(uint256) envfree
    previewUnclaimedETHAsFreeFloatingStaker(address, bytes32) returns(uint256) envfree
    getETHBalance(address) returns(uint256) envfree
    batchPreviewUnclaimedETHAsFreeFloatingStaker(address, bytes32) returns(uint256) envfree
    calculateNewAccumulatedETHPerFreeFloatingShare() returns (uint256) envfree
    batchPreviewUnclaimedETHAsCollateralizedSlotOwner(address, bytes32) returns(uint256) envfree
    previewUnclaimedETHAsCollateralizedSlotOwner(address, bytes32) returns(uint256) envfree
    getUnprocessedETHForAllFreeFloatingSlot() returns (uint256) envfree
    getUnprocessedETHForAllCollateralizedSlot() returns (uint256) envfree
    numberOfRegisteredKnots() returns (uint256) envfree
    totalFreeFloatingShares() returns (uint256) envfree
    calculateNewAccumulatedETHPerCollateralizedSharePerKnot() returns (uint256) envfree
    totalClaimed() returns (uint256) envfree
    calculateCollateralizedETHOwedPerKnot() returns (uint256) envfree
    calculateNewAccumulatedETHPerCollateralizedShare(uint256) returns (uint256) envfree
    updateAccruedETHPerShares()
    updateCollateralizedSlotOwnersAccruedETH(bytes32)
    initialize(address, uint256, address, bytes32)
    isInitialized() returns(bool) envfree
}

/// We defined additional functions to get around the complexity of defining dynamic arrays in cvl. We filter them in 
/// normal rules and invariants as they serve no purpose.
definition notHarnessCall(method f) returns bool = 
    f.selector != batchUpdateCollateralizedSlotOwnersAccruedETH(bytes32).selector
    && f.selector != batchUpdateCollateralizedSlotOwnersAccruedETH(bytes32,bytes32).selector
    && f.selector != deRegisterKnots(bytes32).selector
    && f.selector != deRegisterKnots(bytes32,bytes32).selector
    && f.selector != stake(bytes32,uint256,address).selector
    && f.selector != stake(bytes32,bytes32,uint256,uint256,address).selector
    && f.selector != unstake(address,address,bytes32,uint256).selector
    && f.selector != unstake(address,address,bytes32,bytes32,uint256,uint256).selector
    && f.selector != claimAsStaker(address,bytes32).selector
    && f.selector != claimAsStaker(address,bytes32,bytes32).selector
    && f.selector != claimAsCollateralizedSLOTOwner(address,bytes32).selector
    && f.selector != claimAsCollateralizedSLOTOwner(address,bytes32,bytes32).selector
    && f.selector != registerKnotsToSyndicate(bytes32).selector
    && f.selector != registerKnotsToSyndicate(bytes32,bytes32).selector
    && f.selector != addPriorityStakers(address).selector
    && f.selector != addPriorityStakers(address,address).selector
    && f.selector != batchPreviewUnclaimedETHAsFreeFloatingStaker(address,bytes32).selector
    && f.selector != getETHBalance(address).selector
    && f.selector != calculateCollateralizedETHOwedPerKnot().selector
    && f.selector != calculateNewAccumulatedETHPerCollateralizedShare(uint256).selector
    && f.selector != getCorrectAccumulatedETHPerFreeFloatingShareForBLSPublicKey(bytes32).selector
    && f.selector != isInitialized().selector
    && f.selector != initialize(address,uint256,address,bytes32).selector
    && f.selector != getETHBalance(address).selector;


/// Functions with onlyOwner modifier.
definition onlyOwnerFunctions(method f) returns bool = 
    f.selector == deRegisterKnots(bytes32[]).selector
    || f.selector == registerKnotsToSyndicate(bytes32[]).selector
    || f.selector == addPriorityStakers(address[]).selector
    || f.selector == updatePriorityStakingBlock(uint256).selector;


/// Corrollary that can be used as requirement after sETH solvency is proven.
function sETHSolvencyCorrollary(address user1, address user2, bytes32 knot) returns bool {
    return sETHStakedBalanceForKnot(knot,user1) + sETHStakedBalanceForKnot(knot,user2) <= sETHTotalStakeForKnot(knot);
}

/*-------------------------------------------------
|         View functions return values             |
--------------------------------------------------*/

/**
 * calculateUnclaimedFreeFloatingETHShare: returns as expected
 */
rule calculateUnclaimedFreeFloatingETHShareReturnsAsExpected() {

    env e;

    address user;
    bytes32 blsPubKey;

    uint256 stakedBal = sETHStakedBalanceForKnot(blsPubKey, user);

    uint256 accumulatedETHPerShare = lastAccumulatedETHPerFreeFloatingShare(blsPubKey) > 0 ?
        lastAccumulatedETHPerFreeFloatingShare(blsPubKey) :
        accumulatedETHPerFreeFloatingShare();

    uint256 userShare = (accumulatedETHPerShare * stakedBal) / PRECISION();
    

    assert stakedBal < 1000000000 => calculateUnclaimedFreeFloatingETHShare(blsPubKey, user) == 0, "Wrong value for calculateUnclaimedFreeFloatingETHShare";
    assert stakedBal >= 1000000000 => calculateUnclaimedFreeFloatingETHShare(blsPubKey, user) == userShare - sETHUserClaimForKnot(blsPubKey, user), "Wrong value for calculateUnclaimedFreeFloatingETHShare";

}

/**
 * calculateETHForFreeFloatingOrCollateralizedHolders: returns as expected
 */
rule calculateETHForFreeFloatingOrCollateralizedHoldersReturnsAsExpected() {

    assert calculateETHForFreeFloatingOrCollateralizedHolders() == (totalETHReceived() / 2), "Wrong value for calculateETHForFreeFloatingOrCollateralizedHolders";

}

/**
 * batchPreviewUnclaimedETHAsFreeFloatingStaker: returns as expected
 */
rule batchPreviewUnclaimedETHAsFreeFloatingStakerReturnsAsExpected() {

    address staker;
    bytes32 blsPubKey;

    assert batchPreviewUnclaimedETHAsFreeFloatingStaker(staker, blsPubKey) == previewUnclaimedETHAsFreeFloatingStaker(staker, blsPubKey), "Wrong value for batchPreviewUnclaimedETHAsFreeFloatingStaker";

}

/**
 * previewUnclaimedETHAsFreeFloatingStaker: returns as expected
 */
rule previewUnclaimedETHAsFreeFloatingStakerReturnsAsExpected() {

    address user;
    bytes32 blsPubKey;

    uint256 stakedBal = sETHStakedBalanceForKnot(blsPubKey, user);

    uint256 accumulatedETHPerShare = accumulatedETHPerFreeFloatingShare() + calculateNewAccumulatedETHPerFreeFloatingShare();

    uint256 userShare = (accumulatedETHPerShare * stakedBal) / PRECISION();

    assert previewUnclaimedETHAsFreeFloatingStaker(user, blsPubKey) == userShare - sETHUserClaimForKnot(blsPubKey, user), "Wrong value for previewUnclaimedETHAsFreeFloatingStaker";

}

/**
 * batchPreviewUnclaimedETHAsCollateralizedSlotOwner: returns as expected
 */
rule batchPreviewUnclaimedETHAsCollateralizedSlotOwnerReturnsAsExpected() {

    address staker;
    bytes32 blsPubKey;

    assert batchPreviewUnclaimedETHAsCollateralizedSlotOwner(staker, blsPubKey) == previewUnclaimedETHAsCollateralizedSlotOwner(staker, blsPubKey), "Wrong value for batchPreviewUnclaimedETHAsCollateralizedSlotOwner";

}

/**
 * getUnprocessedETHForAllFreeFloatingSlot: returns as expected
 */
rule getUnprocessedETHForAllFreeFloatingSlotReturnsAsExpected() {

    address staker;
    bytes32 blsPubKey;

    require calculateETHForFreeFloatingOrCollateralizedHolders() >= lastSeenETHPerFreeFloating();

    assert getUnprocessedETHForAllFreeFloatingSlot() == calculateETHForFreeFloatingOrCollateralizedHolders() - lastSeenETHPerFreeFloating(), "Wrong value for getUnprocessedETHForAllFreeFloatingSlot";

}

/**
 * getUnprocessedETHForAllCollateralizedSlot: returns as expected
 */
rule getUnprocessedETHForAllCollateralizedSlotReturnsAsExpected() {

    address staker;
    bytes32 blsPubKey;

    require numberOfRegisteredKnots() > 0;
    require calculateETHForFreeFloatingOrCollateralizedHolders() >= lastSeenETHPerCollateralizedSlotPerKnot();

    assert getUnprocessedETHForAllCollateralizedSlot() == (calculateETHForFreeFloatingOrCollateralizedHolders() - lastSeenETHPerCollateralizedSlotPerKnot()) / numberOfRegisteredKnots(), "Wrong value for getUnprocessedETHForAllCollateralizedSlot";

}

/**
 * calculateNewAccumulatedETHPerFreeFloatingShare: returns as expected
 */
rule calculateNewAccumulatedETHPerFreeFloatingShareReturnsAsExpected() {

    address staker;
    bytes32 blsPubKey;

    assert calculateNewAccumulatedETHPerFreeFloatingShare() == (totalFreeFloatingShares() > 0 ? (getUnprocessedETHForAllFreeFloatingSlot() * PRECISION()) / totalFreeFloatingShares() : 0), "Wrong value for calculateNewAccumulatedETHPerFreeFloatingShare";

}

/**
 * calculateNewAccumulatedETHPerCollateralizedSharePerKnot: returns as expected
 */
rule calculateNewAccumulatedETHPerCollateralizedSharePerKnotReturnsAsExpected() {

    address staker;
    bytes32 blsPubKey;

    assert calculateNewAccumulatedETHPerCollateralizedSharePerKnot() == (getUnprocessedETHForAllCollateralizedSlot() + accumulatedETHPerCollateralizedSlotPerKnot()), "Wrong value for calculateNewAccumulatedETHPerCollateralizedSharePerKnot";

}

/**
 * totalETHReceived: returns as expected
 */
rule totalETHReceivedReturnsAsExpected() {

    assert totalETHReceived() == (getETHBalance(currentContract) + totalClaimed()), "Wrong value for totalETHReceived";

}

/**
 * calculateNewAccumulatedETHPerCollateralizedShare: returns as expected
 */
rule calculateNewAccumulatedETHPerCollateralizedShareReturnsAsExpected() {

    uint256 ethSinceLastUpdate;

    assert calculateNewAccumulatedETHPerCollateralizedShare(ethSinceLastUpdate) == ((ethSinceLastUpdate * PRECISION()) / (numberOfRegisteredKnots() * 4000000000000000000)), "Wrong value for calculateNewAccumulatedETHPerCollateralizedShare";

}

/**
 * getCorrectAccumulatedETHPerFreeFloatingShareForBLSPublicKey: returns as expected
 */
rule getCorrectAccumulatedETHPerFreeFloatingShareForBLSPublicKeyReturnsAsExpected() {

    bytes32 blsPublicKey;

    assert getCorrectAccumulatedETHPerFreeFloatingShareForBLSPublicKey(blsPublicKey) == (lastAccumulatedETHPerFreeFloatingShare(blsPublicKey) > 0 ? lastAccumulatedETHPerFreeFloatingShare(blsPublicKey) : accumulatedETHPerFreeFloatingShare()), "Wrong value for getCorrectAccumulatedETHPerFreeFloatingShareForBLSPublicKey";

}



/*-------------------------------------------------
|         Invariants, ghosts and hooks             |
--------------------------------------------------*/

/**
 * Address 0 must have zero sETH balance.
 */
invariant addressZeroHasNoBalance()
    sETHToken.balanceOf(0) == 0

/**
 * If knot is no longer part of syndicate, it must be registered
 */
invariant noLongerPartOfSyndicateImpliesRegistered(bytes32 blsPubKey)
    isNoLongerPartOfSyndicate(blsPubKey) => isKnotRegistered(blsPubKey)